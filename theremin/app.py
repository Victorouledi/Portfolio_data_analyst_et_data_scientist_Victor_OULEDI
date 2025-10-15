# -*- coding: utf-8 -*-
# Theremin à pinch (pouce-pouce) + dièse/bémol selon la diagonale

# --- Stabilité macOS / MediaPipe / asyncio ---
import os, asyncio
os.environ["MEDIAPIPE_DISABLE_GPU"] = "1"  # force CPU: évite les crashs Metal/GL sur mac
asyncio.set_event_loop_policy(asyncio.DefaultEventLoopPolicy())

import math
from typing import List, Optional

import cv2
import numpy as np
import streamlit as st
import streamlit.components.v1 as components
from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration, VideoProcessorBase

# ==========================
#  Config Streamlit
# ==========================
st.set_page_config(page_title="Theremin Pinch Dièse/Bémol", layout="wide")
st.title("🖐️🎶 Theremin à pinch : distance des pouces → notes, diagonale → ♯/♭")

with st.sidebar:
    st.subheader("Réglages")
    # réseau: local=pas de STUN (dev mac), internet=STUN (déploiement)
    use_stun = st.toggle("Connexion internet (activer STUN)", value=False,
                         help="Active les serveurs STUN pour le déploiement en ligne. Désactive en local.")
    base_octave = st.slider("Octave de base (C)", 2, 6, 4)
    note_span = st.slider("Étendue (notes de la gamme)", 5, 14, 8,
                          help="Nombre de degrés autour de l'octave (Do majeur).")
    min_freq = st.slider("Fréquence min (Hz)", 50, 600, 196)     # G3 ≈ 196 Hz
    max_freq = st.slider("Fréquence max (Hz)", 200, 2000, 988)   # B5 ≈ 988 Hz
    smoothing = st.slider("Lissage (0=réactif, 1=très lissé)", 0.0, 0.95, 0.25)
    pinch_thresh = st.slider("Seuil pinch (normalisé)", 0.02, 0.15, 0.06, step=0.01,
                             help="Plus petit = pince très serrée exigée.")
    angle_thresh_deg = st.slider("Seuil angle pour ♯/♭ (°)", 5, 45, 15)
    volume = st.slider("Volume", 0.0, 1.0, 0.5)
    show_overlay = st.toggle("Afficher repères & métriques", value=True)

st.caption(
    "Joue **uniquement** quand les deux mains pincent (pouce–index rapprochés). "
    "Plus les **pouces** s’éloignent, plus la **note monte**. "
    "Si la ligne entre les deux pouces est **montante** → ♯, **descendante** → ♭."
)

# ==========================
#  Musique / notes
# ==========================
SEMITONES = ["C", "C♯/D♭", "D", "D♯/E♭", "E", "F", "F♯/G♭", "G", "G♯/A♭", "A", "A♯/B♭", "B"]

def note_to_freq(n: int) -> float:
    return 440.0 * (2.0 ** ((n - 69) / 12.0))

def freq_to_midi(freq: float) -> float:
    return 69 + 12 * math.log2(max(freq, 1e-6) / 440.0)

def major_scale_midi(octave: int, span: int) -> List[int]:
    """Do majeur centré sur C@octave, renvoie 'span' degrés autour."""
    C_midi = 12 * (octave + 1)
    degrees = [0, 2, 4, 5, 7, 9, 11, 12]  # C D E F G A B C
    pool = []
    for off in (-12, 0, +12, +24):
        pool += [C_midi + d + off for d in degrees]
    pool = sorted(pool)
    pool = sorted(pool, key=lambda x: abs(x - C_midi))[:span]
    return sorted(pool)

def midi_to_name(m: int, prefer_sharp: Optional[bool]=None) -> str:
    name_ix = m % 12
    octave = m // 12 - 1
    name = SEMITONES[name_ix]
    if "♯/♭" in name:
        sharp, flat = name.split("/")
        sharp, flat = sharp.strip(), flat.strip()
        chosen = sharp if (prefer_sharp or prefer_sharp is None) else flat
        return f"{chosen}{octave}"
    return f"{name}{octave}"

def nearest_from_scale(midi_float: float, scale_midis: List[int]) -> int:
    return min(scale_midis, key=lambda x: abs(x - midi_float))

# ==========================
#  WebRTC / MediaPipe
# ==========================
RTC_CONFIGURATION = RTCConfiguration(
    {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]} if use_stun else {"iceServers": []}
)

try:
    import mediapipe as mp
    mp_hands = mp.solutions.hands
except Exception:
    st.error("❌ MediaPipe introuvable. Vérifie l'installation des dépendances.")
    st.stop()

class PinchTheremin(VideoProcessorBase):
    def __init__(self):
        # modèle le plus stable (CPU) sur macOS ARM
        self.hands = mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=2,
            min_detection_confidence=0.6,
            min_tracking_confidence=0.6,
            model_complexity=0,   # 0 = plus léger et robuste
        )
        self.freq: float = 0.0
        self.note_txt: str = ""
        self.play: bool = False
        self._sfreq: Optional[float] = None

    def _smooth(self, new_val: float, alpha: float) -> float:
        if self._sfreq is None:
            self._sfreq = new_val
        else:
            self._sfreq = (1 - alpha) * new_val + alpha * self._sfreq
        return self._sfreq

    @staticmethod
    def _norm_distance(p1, p2, norm_by: float) -> float:
        return math.hypot(p1[0]-p2[0], p1[1]-p2[1]) / max(norm_by, 1.0)

    def _extract_points(self, img_bgr: np.ndarray):
        """Retourne liste d'infos mains: handed, thumb, index, bbox_w."""
        h, w, _ = img_bgr.shape
        img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
        res = self.hands.process(img_rgb)
        if not res.multi_hand_landmarks:
            return []
        infos = []
        for lm, handed in zip(res.multi_hand_landmarks, res.multi_handedness):
            pts = [(int(pt.x * w), int(pt.y * h)) for pt in lm.landmark]
            xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
            bbox_w = max(max(xs) - min(xs), 1)
            infos.append({
                "handed": handed.classification[0].label,  # 'Left'/'Right'
                "thumb": pts[4],   # thumb tip
                "index": pts[8],   # index tip
                "bbox_w": bbox_w
            })
        return infos

    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        h, w, _ = img.shape

        hands = self._extract_points(img)
        if len(hands) < 2:
            self.play = False
            self.freq = 0.0
            self.note_txt = ""
            return frame.from_ndarray(img, format="bgr24")

        left = next((h for h in hands if h["handed"] == "Left"), None)
        right = next((h for h in hands if h["handed"] == "Right"), None)
        if left is None or right is None:
            left, right = hands[0], hands[1]

        # PINCH (pouce-index) normalisé par largeur de main
        pinch_L = self._norm_distance(left["thumb"], left["index"], left["bbox_w"])
        pinch_R = self._norm_distance(right["thumb"], right["index"], right["bbox_w"])
        is_pinch = (pinch_L < pinch_thresh) and (pinch_R < pinch_thresh)

        # Distance entre pouces (normalisé largeur image)
        pL = left["thumb"]; pR = right["thumb"]
        dist_norm = math.hypot(pL[0]-pR[0], pL[1]-pR[1]) / float(w)
        dist_norm = float(np.clip(dist_norm, 0.0, 1.0))

        # Angle pour ♯ / ♭
        dx = pL[0] - pR[0]
        dy = pL[1] - pR[1]
        angle_deg = math.degrees(math.atan2(-dy, dx))  # y écran vers bas → on inverse
        accidental = 0
        if angle_deg >= angle_thresh_deg:
            accidental = +1
        elif angle_deg <= -angle_thresh_deg:
            accidental = -1

        # Mapping distance → fréquence
        f_raw = min_freq + (max_freq - min_freq) * dist_norm
        f_s = self._smooth(f_raw, alpha=smoothing) if smoothing > 0 else f_raw

        # Quantifier sur Do majeur + dièse/bémol
        scale_midis = major_scale_midi(base_octave, note_span)
        m_est = freq_to_midi(f_s)
        m_near = nearest_from_scale(m_est, scale_midis)
        m_final = int(np.clip(m_near + accidental, 0, 127))
        f_final = note_to_freq(m_final)

        prefer_sharp = True if accidental > 0 else (False if accidental < 0 else None)
        note_name = midi_to_name(m_final, prefer_sharp=prefer_sharp)

        self.play = bool(is_pinch)
        self.freq = f_final if self.play else 0.0
        self.note_txt = note_name if self.play else ""

        if show_overlay:
            for p in [pL, pR, left["index"], right["index"]]:
                cv2.circle(img, p, 8, (0, 255, 0), -1)
            cv2.line(img, pL, pR, (0, 200, 255), 2)
            lines = [
                f"pinch_L: {pinch_L:.3f}  pinch_R: {pinch_R:.3f}  (seuil {pinch_thresh:.3f})",
                f"dist_norm: {dist_norm:.3f}",
                f"angle: {angle_deg:+.1f}°  → {'♯' if accidental>0 else ('♭' if accidental<0 else '♮')}",
                f"midi: {m_final}  freq: {self.freq:.1f} Hz",
                f"note: {self.note_txt or '-'}",
                f"play: {self.play}",
            ]
            y0 = 28
            for i, t in enumerate(lines):
                cv2.putText(img, t, (10, y0 + i*26), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (40, 220, 40), 2, cv2.LINE_AA)

        return frame.from_ndarray(img, format="bgr24")

# ==========================
#  WebRTC
# ==========================
webrtc_ctx = webrtc_streamer(
    key="theremin-pinch-sharp-flat",
    mode=WebRtcMode.SENDRECV,
    video_processor_factory=PinchTheremin,
    rtc_configuration=RTC_CONFIGURATION,
    media_stream_constraints={"video": True, "audio": False},
)

# ==========================
#  Audio WebAudio côté client
# ==========================
def webaudio(freq: float, play: bool, volume: float):
    freq = max(0.0, float(freq))
    gain = float(volume) if (play and freq > 0.0) else 0.0
    components.html(
        f"""
        <div id="webaudio"></div>
        <script>
        (function(){{
            const AudioContext = window.AudioContext || window.webkitAudioContext;
            if(!window.ctx) {{
                window.ctx = new AudioContext();
            }}
            const ctx = window.ctx;

            if(!window.osc) {{
                window.osc = ctx.createOscillator();
                window.osc.type = 'sine';
                window.gain = ctx.createGain();
                window.osc.connect(window.gain).connect(ctx.destination);
                window.osc.start();
            }}

            const resume = () => {{
                if (ctx.state !== 'running') {{ ctx.resume(); }}
                window.removeEventListener('click', resume);
                window.removeEventListener('touchstart', resume);
                window.removeEventListener('keydown', resume);
            }};
            window.addEventListener('click', resume);
            window.addEventListener('touchstart', resume);
            window.addEventListener('keydown', resume);

            const f = {freq};
            const g = {gain};
            if (f > 0) {{
                window.osc.frequency.setTargetAtTime(f, ctx.currentTime, 0.01);
            }}
            window.gain.gain.setTargetAtTime(g, ctx.currentTime, 0.02);
        }})();
        </script>
        """,
        height=0,
    )

if webrtc_ctx and webrtc_ctx.video_processor:
    webaudio(webrtc_ctx.video_processor.freq,
             webrtc_ctx.video_processor.play,
             volume)
    st.markdown(
        f"**Note :** {webrtc_ctx.video_processor.note_txt or '-'} &nbsp;|&nbsp; "
        f"**Fréquence :** {webrtc_ctx.video_processor.freq:.1f} Hz &nbsp;|&nbsp; "
        f"**Lecture :** {'on' if webrtc_ctx.video_processor.play else 'off'}"
    )
else:
    st.info("Active la webcam (autorisation navigateur).")
