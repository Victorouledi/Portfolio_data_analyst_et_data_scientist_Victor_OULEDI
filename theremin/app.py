# app.py — Webcam via TURN only (TCP 443), aucun traitement
import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration

st.set_page_config(page_title="Webcam (TURN only)", layout="centered")
st.title("🎥 Webcam (forcée via TURN:443)")

st.info(
    "Clique **START**, accepte l’accès caméra. "
    "Connexion WebRTC forcée via TURN TCP:443 pour traverser les pare-feu stricts."
)

def build_turn_only():
    # 1) TURN depuis secrets (si fournis)
    if "TURN_URLS" in st.secrets:
        urls = st.secrets["TURN_URLS"].split()
        return [{
            "urls": urls,
            "username": st.secrets.get("TURN_USERNAME"),
            "credential": st.secrets.get("TURN_CREDENTIAL"),
        }]
    # 2) Fallback public OpenRelay, on **priorise TCP:443**
    return [{
        "urls": [
            "turn:openrelay.metered.ca:443?transport=tcp",
            "turn:openrelay.metered.ca:443",
            "turn:openrelay.metered.ca:80",
        ],
        "username": "openrelayproject",
        "credential": "openrelayproject",
    }]

RTC_CONFIGURATION = RTCConfiguration({
    "iceServers": build_turn_only(),
    # Forcer l’usage exclusif du TURN (pas de direct, pas de STUN)
    "iceTransportPolicy": "relay",
})

webrtc_streamer(
    key="cam-turn-only",
    mode=WebRtcMode.SENDRECV,
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
    async_processing=False,
)

