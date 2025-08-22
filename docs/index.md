---
layout: splash
title: "Victor Ouledi"
subtitle: "Data Scientist & Analyst — NLP · Computer Vision · Économétrie"
classes: wide
author_profile: false

# Bandeau (hero)
header:
  overlay_color: "#0b1220"
  overlay_filter: "0.6"
  actions:
    - label: "🚀 Voir les projets"
      url: "/projets/"
    - label: "✉️ Me contacter"
      url: "/contacts/"

# Bloc intro centré
intro:
  - excerpt: >
      **Data Scientist / Data Analyst / ML & AI Engineer** (NLP, Computer Vision).  
      ~2 ans d’expérience. Passionné par la statistique, l’IA, et la mise en production
      de solutions data utiles. Curiosité, rigueur, sens produit.  
      👉 Parcourez quelques réalisations ci-dessous.

# Rangée 1 (⚠️ chaque carte commence par un tiret '-')
feature_row:
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
  - title: "Analyse — Terre de Liens"
    excerpt: "Profilage actionnaires • comportements d’investissement."
    url: "/projets/terre-de-liens/"
    btn_label: "Détails"
    btn_class: "btn--primary"

# Rangée 2
feature_row2:
  - title: "Clustering & ACP — Criminalité (USA)"
    excerpt: "KMeans • PCA • critères coude/silhouette."
    url: "/projets/crime-usa/"
    btn_label: "Détails"
    btn_class: "btn--primary"
  - title: "AFC — Élections 2022 (IDF)"
    excerpt: "Correspondence Analysis • tableaux de contingence."
    url: "/projets/elections-afc/"
    btn_label: "Détails"
    btn_class: "btn--primary"
  - title: "Certifications"
    excerpt: "SQL • ML supervisé / non supervisé • Excel."
    url: "/projets/certifications/"
    btn_label: "Voir"
    btn_class: "btn--primary"

# Rangée 3
feature_row3:
  - title: "R (panel) — Prix hédoniques (Lyon)"
    excerpt: "DVF • modèles panel (plm/fixest) • tidyverse • ggplot2."
    url: "/projets/prix-hedoniques-lyon/"
    btn_label: "Détails"
    btn_class: "btn--primary"
  - title: "R (panel) — Salaires (US)"
    excerpt: "Within/Between • Hausman-Taylor • diagnostics robustes."
    url: "/projets/salaires-panel-us/"
    btn_label: "Détails"
    btn_class: "btn--primary"
  - title: "Télécharger mon CV"
    excerpt: "CV 1 page (PDF)."
    url: "/asset/CV/Victor_OULEDI_CV.pdf"
    btn_label: "Télécharger"
    btn_class: "btn--inverse"
---

{% include feature_row id="intro" type="center" %}
{% include feature_row %}
{% include feature_row id="feature_row2" %}
{% include feature_row id="feature_row3" %}

