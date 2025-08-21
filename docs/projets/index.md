# Projets

<div class="grid cards" markdown>

- :material-text-box-multiple: **NLP — Classification de plaintes financières**
  
  **Objectif** : catégoriser **66 699 plaintes** clients par type de service bancaire (recouvrement, rapports de crédit, prêt étudiant, prêt sur salaire).
  
  **Stack** : Python (PyTorch, `torch.nn`, `torchtext`), prétraitement (spaCy/NTLK, tokenisation, lemmatisation, stopwords), LSTM bi-directionnel, gestion du déséquilibre (class weights), évaluation (`scikit-learn`: métriques/ROC).
  
  [Détails →](nlp-lstm.md)

- :material-microscope: **Vision — Application Streamlit d’imagerie médicale**
  
  **Objectif** : classifier des images (cerveau, poumon, autre) via un **CNN** et proposer une **démo web** (Streamlit) d'outil de classification.
  
  **Stack** : Python (scikit-image, TensorFlow/Keras, éventuellement OpenCV), data viz (Matplotlib/Seaborn/Plotly), déploiement Streamlit.
  
  [Détails →](imagerie-medicale.md)

- :material-account-cash: **Analyse — Système d’actionnariat (Terre de Liens)**
  
  **Objectif** : profiler les actionnaires, suivre souscriptions/rachats, analyser la stabilité et les comportements d’investissement.
  
  **Stack** : Python (Pandas, NumPy, SciPy, Statsmodels), data viz (Matplotlib, Seaborn, Plotly), tests/statistiques descriptives, export rapport.
  
  [Détails →](terre-de-liens.md)

- :material-chart-bell-curve: **Clustering & ACP — Criminalité aux États-Unis**
  
  **Objectif** : regrouper les 50 États par profils de criminalité et **réduire la dimension** (ACP) pour interprétation.
  
  **Stack** : `scikit-learn` (KMeans, PCA), Pandas/NumPy, data viz (Seaborn, Matplotlib), critères d’aide au choix (coude/inertie, silhouette si besoin).
  
  [Détails →](crime-usa.md)

- :material-vote: **AFC — Élections présidentielles 2022 (Île-de-France)**
  
  **Objectif** : analyser les correspondances **départements × candidats** et visualiser proximités/contrastes.
  
  **Stack** : Python (Pandas, NumPy), **Correspondence Analysis** avec `prince` (ou `mca`), data viz (Matplotlib/Seaborn/Plotly), tableaux de contingence.
  
  [Détails →](elections-afc.md)

- :material-home-city: **R (panel) — Prix hédoniques, immobilier lyonnais**
  
  **Objectif** : estimer l’impact de la **localisation et des attributs** des biens sur les prix (données DVF).
  
  **Stack** : R (**tidyverse** : `dplyr`, `readr`, `tidyr`, **dataviz** : `ggplot2`/Plotly), modèles panel avec `plm`, `broom`, `car`, reporting (`stargazer`/`texreg`).
  
  [Détails →](prix-hedoniques-lyon.md)

- :material-cash: **R (panel) — Déterminants des salaires aux États-Unis**
  
  **Objectif** : identifier les effets (éducation, expérience, caractéristiques individuelles) via modèles panel (Within/Between, Hausman-Taylor).
  
  **Stack** : R (**tidyverse**, `plm`), diagnostics (`lmtest`, `sandwich`), **dataviz** (`ggplot2`/Plotly), mise en forme (`broom`, `stargazer`).
  
  [Détails →](salaires-panel-us.md)

- :material-certificate: **Certifications**
  
  **Objectif** : présenter les certificats clés (SQL, ML supervisé/non supervisé, Excel).
  
  **Stack** : pages statiques (Markdown) + scans/exports PDF/PNG.
  
  [Détails →](certifications.md)

</div>
