# app.py — Webcam toute simple (aucun traitement)

import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration

st.set_page_config(page_title="Webcam simple", layout="centered")
st.title("🎥 Aperçu webcam (WebRTC)")

st.info("Clique sur **START**, accepte l’accès caméra. Aucune analyse n’est faite ici.")

def build_ice_servers():
    servers = []
    # 1) TURN depuis les secrets (si renseignés)
    if "TURN_URLS" in st.secrets:
        urls = st.secrets["TURN_URLS"].split()
        user = st.secrets.get("TURN_USERNAME")
        cred = st.secrets.get("TURN_CREDENTIAL")
        servers.append({"urls": urls, "username": user, "credential": cred})
    # 2) STUN Google
    servers.append({"urls": ["stun:stun.l.google.com:19302"]})
    # 3) Fallback TURN public si pas de secrets
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

webrtc_streamer(
    key="cam-only",
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

