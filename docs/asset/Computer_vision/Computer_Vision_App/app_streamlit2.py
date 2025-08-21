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

# Interface de l'application
st.markdown("<h1 style='text-align: center;'>Classification d'imageries médicales</h1>", unsafe_allow_html=True)

# Modifier la couleur de fond
st.markdown(
    """
    <style>
    .reportview-container {
        background: #f0f2f5; /* Changez cette couleur selon vos besoins */
    }
    </style>
    """,
    unsafe_allow_html=True
)

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
