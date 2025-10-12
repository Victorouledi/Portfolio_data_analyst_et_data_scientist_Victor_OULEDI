import streamlit as st
import numpy as np
import cv2
import requests
from tensorflow.keras.models import load_model
from PIL import Image
import tempfile
import os
from io import StringIO

# Fonction pour charger le modèle depuis GitHub
def load_model_from_github(url):
    response = requests.get(url)
    with tempfile.NamedTemporaryFile(suffix='.h5', delete=False) as temp_file:
        temp_file.write(response.content)
        model = load_model(temp_file.name)
    return model

# URL du modèle sur GitHub
model_url = 'https://raw.githubusercontent.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/main/CNN_computer_vision/CNN_imageries_medicales2.h5'

# Charger le modèle depuis GitHub
model = load_model_from_github(model_url)

# Paramètres de l'image
img_height, img_width = 200, 200
class_names = ['Autres', 'Cerveau', 'Poumon']

# ---- Page config + thème visuel (fond + overlay + widgets) ----
st.set_page_config(
    page_title="Classification d'imageries médicales",
    page_icon="🩺",   # icône médicale
    layout="wide"
)

def set_bg_and_text_minimal(
    image_url: str,
    text_color: str = "#E8FFF1",       # texte vert-blanc apaisant
    sidebar_bg: str = "#143D26",       # vert forêt foncé (sidebar)
    sidebar_text: str = "#E8FFF1",     # texte lisible sur fond vert
    overlay_opacity: float = 0.45,     # opacité moyenne
    widget_bg: str = "#1C5031",        # fond vert bouteille pour inputs
    accent_green: str = "#4CAF50"      # vert médical clair pour boutons
):

    st.markdown(f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background:
          linear-gradient(rgba(13,27,42,{overlay_opacity}), rgba(13,27,42,{overlay_opacity})),
          url('{image_url}') no-repeat center center fixed !important;
        background-size: cover !important;
    }}
    [data-testid="stSidebar"] > div:first-child {{
        background: {sidebar_bg} !important;
        color: {sidebar_text} !important;
    }}
    [data-testid="stSidebar"] * {{ color: {sidebar_text} !important; }}
    .stApp, .stApp * {{ color: {text_color} !important; }}
    .block-container {{ background: transparent !important; }}

    /* Boutons (upload / actions) */
    div.stButton > button:first-child,
    div.stDownloadButton > button,
    div[data-testid="stFileUploader"] button {{
        background-color: {accent_green} !important;
        color: #fff !important;
        border: 0 !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        transition: 0.2s ease;
    }}
    div.stButton > button:first-child:hover,
    div.stDownloadButton > button:hover,
    div[data-testid="stFileUploader"] button:hover {{
        filter: brightness(0.95); transform: translateY(-1px);
    }}

    /* Uploader */
    [data-testid="stFileUploaderDropzone"] {{
        background: {widget_bg} !important;
        color: {text_color} !important;
        border: 1px dashed rgba(255,255,255,0.25) !important;
        border-radius: 12px !important;
    }}

    /* Inputs / code / texte long */
    .stTextInput > div > div,
    .stNumberInput > div > div,
    .stTextArea > div > textarea,
    .stTextInput input, .stNumberInput input,
    pre, code, .stCodeBlock, .stMarkdown code {{
        background: {widget_bg} !important;
        color: {text_color} !important;
        border: 1px solid rgba(255,255,255,0.12) !important;
        border-radius: 8px !important;
    }}
    hr {{ border-color: rgba(255,255,255,0.12) !important; }}
    </style>
    """, unsafe_allow_html=True)

# Choisis l’un de ces fonds (ou remplace par ton URL)
medical_bg = "https://www.alcimed.com/wp-content/uploads/2023/10/intelligence-artificielle-imagerie-medicale-2.webp"


set_bg_and_text_minimal(
    image_url=medical_bg,
    text_color="#E8FFF1",
    sidebar_bg="#143D26",
    sidebar_text="#E8FFF1",
    overlay_opacity=0.45,
    widget_bg="#1C5031",
    accent_green="#4CAF50"
)

st.markdown("<h1 style='text-align:center;'>🩺 Classification d'imageries médicales</h1>", unsafe_allow_html=True)

st.write("Cette interface a pour but de classer des documents d'imagerie médicale et permet de prédire la classe d'une image comme étant soit une imagerie du cerveau, des poumons ou aucune de ces classes précédentes")

# Afficher le résumé du modèle
st.write("Les prédictions se basent sur un modèle simple de réseau de neurones convolutif dont voici les paramètres :")
model_summary = StringIO()  # Créer un objet StringIO pour capturer la sortie
model.summary(print_fn=lambda x: model_summary.write(x + '\n'))  # Capturer le résumé du modèle
st.text(model_summary.getvalue())  # Afficher le résumé dans l'application

# Chargement de l'image par l'utilisateur
uploaded_file = st.file_uploader("Choisissez une image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Afficher l'image chargée
    image = Image.open(uploaded_file)
    st.image(image, caption='Image Importée', use_column_width=True)
    st.write("")
    st.write("Classification en cours...")

    # Prétraiter l'image pour la prédiction
    image_to_predict = np.array(image.convert("RGB"))
    img_to_predict = np.expand_dims(cv2.resize(image_to_predict, (img_width, img_height)), axis=0)
    
    # Afficher la forme de l'image à prédire
    st.write(f"Forme de l'image à prédire : {img_to_predict.shape}")

    # Prédiction
    try:
        predictions = model.predict(img_to_predict)[0]
        st.write("Prédiction réussie.")
    except Exception as e:
        st.write(f"Erreur lors de la prédiction : {e}")
        st.stop()  # Stoppe l'exécution si une erreur se produit

    # Trier les indices des classes par ordre de probabilité décroissante
    sorted_indices = np.argsort(predictions)[::-1]
    top_class_index = sorted_indices[0]
    top_class_confidence = predictions[top_class_index]
    
    # Vérifier la confiance et choisir la classe prédite
    if top_class_confidence >= 0.90:
        predicted_class_index = top_class_index
    else:
        predicted_class_index = sorted_indices[1]
    
    predicted_class_name = class_names[predicted_class_index]
    
    # Afficher le résultat
    st.write(f"L'image est prédite comme : **{predicted_class_name}** avec une confiance de **{predictions[predicted_class_index]:.2f}**")
else:
    st.write("Veuillez importer une image pour la prédiction.")
