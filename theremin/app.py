# -*- coding: utf-8 -*-
# Test webcam + mains : repères + trait entre les pouces (double pinch)

# --- Calmer les logs & forcer CPU ---
import os, asyncio, platform
os.environ["MEDIAPIPE_DISABLE_GPU"] = "1"
os.environ["GLOG_minloglevel"] = "3"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
asyncio.set_event_loop_policy(asyncio.DefaultEventLoopPolicy())

import math
from typing import Optional, List

import cv2
import numpy as np
import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration, VideoProcessorBase

st.set_page_config(page_title="Test Webcam + Mains", layout="wide")
st.title("🎥 Test webcam + détection des mains (MediaPipe)")

# --- UI ---
with st.sidebar:
    st.subheader("Réglages")
    pinch_thresh = st.slider("Seuil pinch (normalisé)", 0.02, 0.15, 0.06, step=0.01)
    angle_thresh_deg = st.slider("Seuil angle ♯/♭ (affiché)", 5, 45, 15)
    show_overlay = st.toggle("Afficher repères & métriques", value=True)

st.caption("Pinch = pouce–index rapprochés. Un trait s’affiche entre les **deux pouces** si les deux mains pincent.")

# --- ICE/TURN/STUN: secrets d'abord, sinon fallback OpenRelay ---
def build_ice_servers():
    servers = []
    if "TURN_URLS" in st.secrets:
        urls = st.secrets["TURN_URLS"].split()
        user = st.secrets.get("TURN_USERNAME")
        cred = st.secrets.get("TURN_CREDENTIAL")
        servers.append({"urls": urls, "username": user, "credential": cred})
    # STUN Google (utile même si TURN configuré)
    servers.append({"urls": ["stun:stun.l.google.com:19302"]})
    # Fallback public si pas de secrets
    if "TURN_URLS" not in st.secrets:
        servers.append({
            "urls": [
                "turn:openrelay.metered.ca:80",
                "turn:openrelay.metered.ca:443?transport=tcp",
                "turn:openrelay.metered.ca:443",
            ],
            "username": "openrelayproject",
            "credential": "openrelayproject",
        })
    return servers

RTC_CONFIGURATION = RTCConfiguration({"iceServers": build_ice_servers()})

# --- MediaPipe Hands ---
try:
    import mediapipe as mp
    mp_hands = mp.solutions.hands
except Exception as e:
    st.error("❌ MediaPipe introuvable. Vérifie requirements.txt.")
    st.stop()

class HandDebug(VideoProcessorBase):
    def __init__(self):
        self.hands = mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=2,
            min_detection_confidence=0.6,
            min_tracking_confidence=0.6,
            model_complexity=0,  # plus léger/stable en cloud
        )

    @staticmethod
    def _norm_distance(p1, p2, norm_by: float) -> float:
        return math.hypot(p1[0]-p2[0], p1[1]-p2[1]) / max(norm_by, 1.0)

    def _extract(self, img_bgr):
        h, w, _ = img_bgr.shape
        img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
        res = self.hands.process(img_rgb)
        items = []
        if not res.multi_hand_landmarks:
            return items
        for lm, handed in zip(res.multi_hand_landmarks, res.multi_handedness):
            pts = [(int(pt.x * w), int(pt.y * h)) for pt in lm.landmark]
            xs = [p[0] for p in pts]
            bbox_w = max(max(xs) - min(xs), 1)
            items.append({
                "handed": handed.classification[0].label,  # 'Left'/'Right'
                "thumb": pts[4],   # pouce (extrémité)
                "index": pts[8],   # index (extrémité)
                "bbox_w": bbox_w,
                "landmarks": pts
            })
        return items

    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        h, w, _ = img.shape

        hands = self._extract(img)

        # Dessin repères si demandé
        if show_overlay:
            for item in hands:
                # petits points sur quelques landmarks
                for pid in [4, 8]:
                    cv2.circle(img, item["landmarks"][pid], 6, (0, 255, 0), -1)

        # Si 2 mains, calcule pinch gauche/droite + trait entre pouces si double pinch
        info_text = []
        if len(hands) >= 2:
            left = next((x for x in hands if x["handed"] == "Left"), hands[0])
            right = next((x for x in hands if x["handed"] == "Right"), hands[1 if left is hands[0] else 0])

            pinch_L = self._norm_distance(left["thumb"], left["index"], left["bbox_w"])
            pinch_R = self._norm_distance(right["thumb"], right["index"], right["bbox_w"])
            is_pinch = (pinch_L < pinch_thresh) and (pinch_R < pinch_thresh)

            pL, pR = left["thumb"], right["thumb"]
            # distance normalisée par largeur d'image
            dist_norm = math.hypot(pL[0]-pR[0], pL[1]-pR[1]) / float(w)
            dist_norm = float(np.clip(dist_norm, 0.0, 1.0))

            # angle (pour info visuelle)
            dx, dy = pL[0]-pR[0], pL[1]-pR[1]
            angle_deg = math.degrees(math.atan2(-dy, dx))
            if show_overlay:
                color = (0, 200, 255) if is_pinch else (80, 80, 80)
                cv2.line(img, pL, pR, color, 3)
                cv2.circle(img, pL, 7, (0, 255, 255), -1)
                cv2.circle(img, pR, 7, (0, 255, 255), -1)

            info_text = [
                f"pinch_L: {pinch_L:.3f}  pinch_R: {pinch_R:.3f}  (seuil {pinch_thresh:.3f})",
                f"dist_norm(pouce↔pouce): {dist_norm:.3f}",
                f"angle: {angle_deg:+.1f}°  (≳{angle_thresh_deg}° = montante, ≲-{angle_thresh_deg}° = descendante)",
                f"double pinch détecté: {is_pinch}",
            ]

        if show_overlay:
            y0 = 28
            for i, t in enumerate(info_text):
                cv2.putText(img, t, (10, y0 + i*26),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (40, 220, 40), 2, cv2.LINE_AA)

        return frame.from_ndarray(img, format="bgr24")

# --- WebRTC (vidéo seule) ---
webrtc_ctx = webrtc_streamer(
    key="hand-test",
    mode=WebRtcMode.SENDRECV,
    video_processor_factory=HandDebug,
    rtc_configuration=RTC_CONFIGURATION,
    media_stream_constraints={
        "video": {
            "width": {"ideal": 640},
            "height": {"ideal": 480},
            "frameRate": {"ideal": 15, "max": 15},
            "facingMode": "user",
        },
        "audio": False,
    },
    async_processing=True,
)

if not (webrtc_ctx and webrtc_ctx.state.playing):
    st.info("Autorise la webcam puis regarde l’aperçu. Les repères et le trait s’affichent si double pinch.")
