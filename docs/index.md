---
layout: splash
title: "Victor Ouledi"
subtitle: "Data Scientist / Data Analyst / ML & AI Engineer"
classes: wide
author_profile: false

header:
  overlay_color: "#0b1220"
  overlay_filter: "0.6"
  actions:
    - label: "🚀 Voir les projets"
      url: "/projets/"
    - label: "✉️ Me contacter"
      url: "/contacts/"
 
# 1 rangée d'aperçu sur la home
feature_row_home:
  - title: "NLP — Classification de plaintes"
    excerpt: "66 699 textes • BiLSTM • pipeline NLP complet."
    url: "/projets/nlp-lstm/"
    btn_label: "Détails"
    btn_class: "btn--primary"
  - title: "Computer Vision — Imagerie médicale"
    excerpt: "CNN • scikit-image • Keras/PyTorch • démo Streamlit."
    url: "/projets/imagerie-medicale/"
    btn_label: "Détails"
    btn_class: "btn--primary"
  - title: "Data Analyse — Profils actionnaires Terre de Liens"
    excerpt: "Profilage actionnaires • comportements d’investissement."
    url: "/projets/terre-de-liens/"
    btn_label: "Détails"
    btn_class: "btn--primary"
---

<!-- Photo flottante à droite, responsive -->
<img src="{{ site.baseurl }}/asset/CV/photo-id.jpg" alt="Victor Ouledi" class="hero-photo" />


**Data Scientist / Data Analyst / ML & AI Engineer (NLP, Computer Vision)**.  
~2 ans d’expérience. 
Passionné par la statistique, l’IA et la mise en production de solutions data utiles. 
Curiosité, rigueur, et sens produit.  
👉 Parcourez un aperçu ci-dessous.

<!-- On “déroule” les cartes projets -->
{% include feature_row id="feature_row_home" %}

<!-- Boutons centrés -->
<p style="text-align:center;margin-top:1rem;clear:both;">
  <a class="btn btn--primary" href="{{ site.baseurl }}/projets/">Voir tous les projets →</a>
  <a class="btn" style="margin-left:.6rem"
     href="{{ site.baseurl }}/asset/CV/Victor_OULEDI_CV.pdf"
     target="_blank" rel="noopener" download>
     📄 Télécharger mon CV (PDF)
  </a>
</p>

