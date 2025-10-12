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
    text_color: str = "#EAF6FF",   # blanc bleuté lisible
    sidebar_bg: str = "#0B1F3A",   # bleu nuit (sidebar)
    sidebar_text: str = "#EAF6FF", # texte sidebar
    overlay_opacity: float = 0.50, # léger voile bleu
    widget_bg: str = "#102A43",    # bleu sombre pour inputs
    accent_green: str = "#2F80ED"  # bleu action (boutons)
):
    st.markdown(f"""
    <style>
    /* Fond global */
    [data-testid="stAppViewContainer"] {{
      background:
        linear-gradient(rgba(10,25,47,{overlay_opacity}), rgba(10,25,47,{overlay_opacity})),
        url('{image_url}') no-repeat center center fixed !important;
      background-size: cover !important;
    }}
    /* Sidebar */
    [data-testid="stSidebar"] > div:first-child {{ background:{sidebar_bg} !important; color:{sidebar_text} !important; }}
    [data-testid="stSidebar"] * {{ color:{sidebar_text} !important; }}

    /* Texte global + container */
    .stApp, .stApp * {{ color:{text_color} !important; }}
    .block-container {{ background: transparent !important; }}

    /* Boutons (Upload / actions) */
    div.stButton > button:first-child,
    div.stDownloadButton > button,
    div[data-testid="stFileUploader"] button {{
      background-color:{accent_green} !important; color:#fff !important;
      border:0 !important; border-radius:10px !important; font-weight:600 !important;
      transition:.2s ease;
    }}
    div.stButton > button:first-child:hover,
    div.stDownloadButton > button:hover,
    div[data-testid="stFileUploader"] button:hover {{
      filter:brightness(0.95); transform:translateY(-1px);
    }}

    /* Dropzone & inputs */
    [data-testid="stFileUploaderDropzone"],
    .stTextInput > div > div, .stNumberInput > div > div,
    .stTextArea > div > textarea, .stTextInput input, .stNumberInput input,
    pre, code, .stCodeBlock, .stMarkdown code {{
      background:{widget_bg} !important; color:{text_color} !important;
      border:1px solid rgba(255,255,255,0.15) !important; border-radius:10px !important;
    }}

    /* Cartes centrées et cartes/sections */
    .hero, .card {{
      max-width: 1100px; margin: 0 auto;   /* <-- centre horizontalement */
    }}
    .hero {{ text-align:center; }}
    .card {{ margin-top:14px; padding:14px; background:rgba(16,42,67,0.55); border-radius:12px; }}

    /* Résumé du modèle : pré monospacé scrollable, centré via container */
    .model-summary {{
      max-height: 360px; overflow:auto; padding:12px 14px; line-height:1.2;
      font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
      background:{widget_bg}; border-radius:10px; border:1px solid rgba(255,255,255,.12);
    }}
    </style>
    """, unsafe_allow_html=True)

# Choisis l’un de ces fonds (ou remplace par ton URL)
medical_bg = "https://www.alcimed.com/wp-content/uploads/2023/10/intelligence-artificielle-imagerie-medicale-2.webp"


set_bg_and_text_minimal(
    image_url=medical_bg,
    text_color="#EAF6FF",
    sidebar_bg="#0B1F3A",
    sidebar_text="#EAF6FF",
    overlay_opacity=0.50,
    widget_bg="#102A43",
    accent_green="#2F80ED"
)

st.markdown("""
<div class="hero">
  <h1>🩺 Classification d'imageries médicales</h1>
  <p>Cette interface classe des images d’imagerie médicale (cerveau, poumons ou autre) et affiche une prédiction basée sur un modèle CNN.</p>
  <p>Les prédictions se basent sur un modèle simple de réseau de neurones convolutif dont voici les paramètres :<p>
</div>
""", unsafe_allow_html=True)


# Afficher le résumé du modèle
model_summary = StringIO()
model.summary(print_fn=lambda x: model_summary.write(x + "\n"))
summary_text = model_summary.getvalue()

c1, c2, c3 = st.columns([1, 3, 1])
with c2:
    st.code(summary_text, language="text")

st.markdown(f"""
<style>
.summary-wrap {{
  display: block;
  max-width: 980px;           /* largeur max du cartouche */
  margin: 0 auto 1rem auto;   /* centre horizontalement */
}}
.summary-box {{
  background: rgba(13,27,42,0.65);
  border: 1px solid rgba(255,255,255,0.12);
  border-radius: 12px;
  padding: 14px 18px;
  width: fit-content;         /* s'ajuste au contenu */
  max-width: 100%;            /* mais ne dépasse pas la wrap */
  margin: 0 auto;             /* centre la box dans la wrap */
  overflow-x: auto;           /* scroll si trop large */
}}
.summary-box pre {{
  white-space: pre;            /* respecte les espacements */
  margin: 0;
  font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
  font-size: 14px; line-height: 1.35;
  color: #E8FFF1 !important;
}}
</style>

<div class="summary-wrap">
  <div class="summary-box"><pre>{summary_text}</pre></div>
</div>
""", unsafe_allow_html=True)

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
