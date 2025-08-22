---
title: "Projets"
permalink: /projets/
layout: single
classes: wide

# Rangée 1
feature_row:
  - title: "NLP — Classification de plaintes"
    excerpt: "66 699 textes · BiLSTM · pipeline NLP complet."
    url: "{{ site.baseurl }}/projets/nlp-lstm/"
    btn_label: "Détails"
    btn_class: "btn--primary"
  - title: "Computer Vision — Imagerie médicale"
    excerpt: "Classification/segmentation · scikit-image · Keras/PyTorch."
    url: "{{ site.baseurl }}/projets/imagerie-medicale/"
    btn_label: "Détails"
    btn_class: "btn--primary"
  - title: "Analyse — Terre de Liens"
    excerpt: "Pandas/NumPy/Statsmodels · comportements d’investissement."
    url: "{{ site.baseurl }}/projets/terre-de-liens/"
    btn_label: "Détails"
    btn_class: "btn--primary"

# Rangée 2
feature_row2:
  - title: "Clustering & ACP — Criminalité (USA)"
    excerpt: "KMeans · PCA · critères coude/silhouette."
    url: "{{ site.baseurl }}/projets/crime-usa/"
    btn_label: "Détails"
    btn_class: "btn--primary"
  - title: "AFC — Élections 2022 (IDF)"
    excerpt: "Correspondence Analysis · tableaux de contingence."
    url: "{{ site.baseurl }}/projets/elections-afc/"
    btn_label: "Détails"
    btn_class: "btn--primary"
  - title: "Certifications"
    excerpt: "SQL · ML supervisé/non supervisé · Excel."
    url: "{{ site.baseurl }}/projets/certifications/"
    btn_label: "Voir"
    btn_class: "btn--primary"

# Rangée 3
feature_row3:
  - title: "R (panel) — Prix hédoniques (Lyon)"
    excerpt: "DVF · modèles panel (plm) · tidyverse · ggplot2."
    url: "{{ site.baseurl }}/projets/prix-hedoniques-lyon/"
    btn_label: "Détails"
    btn_class: "btn--primary"
  - title: "R (panel) — Salaires (US)"
    excerpt: "Within/Between · Hausman-Taylor · diagnostics."
    url: "{{ site.baseurl }}/projets/salaires-panel-us/"
    btn_label: "Détails"
    btn_class: "btn--primary"
---

{% include feature_row id="feature_row" type="left" %}
{% include feature_row id="feature_row2" type="left" %}
{% include feature_row id="feature_row3" type="left" %}
