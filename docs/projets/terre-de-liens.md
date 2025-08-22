---
title: "Data Analyse — Système d’actionnariat (Terre de Liens)"
permalink: /projets/terre-de-liens/
layout: single
classes: wide
toc: true
---
 
## Contexte & objectif
Analyse du **système d’actionnariat** de la foncière Terre de Liens pour mieux comprendre :
- **qui** sont les actionnaires (profils, montants, affectations),
- **comment** ils se comportent (rythme de souscription, **rachats**, récurrence),
- **où** concentrer l’effort (segments, rétention, concentration du capital).

> Base brute : **39 476 lignes**, **25 champs** (extrait Salesforce, version **fictive** reconstruite pour confidentialité).

- Notebook : [Jupyter_notebook_analyse_actionnariat.ipynb](../asset/data_analysis_TDL/notebooks/Jupyter_notebook_analyse_actionnariat.ipynb)

## Stack & outillage

- **Langage & notebooks** : Python, Jupyter (VS Code)
- **Data & préparation** : pandas, NumPy, nettoyage/normalisation, *feature engineering* (RFM, délais entre souscriptions), anonymisation/pseudonymisation
- **Stats & tests** : SciPy (tests χ²/Kruskal), Statsmodels (ANOVA/GLM), corrections FDR
- **Modélisation (optionnel selon analyses)** : scikit-learn (LogReg, KMeans/GMM, métriques), **lifelines** (Kaplan–Meier, Cox), XGBoost, SHAP (explicabilité)
- **Dataviz** : Matplotlib, Seaborn, Plotly (interactif)


## Quelques indicateurs extraits de l'analyse :**

### Analyse de la variation moyenne du nombre d'actions souscrites entre chaque rang de souscriptions prises

![](../asset/data_analysis_TDL/images/Analyse%20de%20la%20variation%20moyenne%20du%20nombre%20d%E2%80%99actions%20souscrites%20entre%20chaque%20rang%20de%20souscriptions%20prises.png)


### Distribution des types de variations du nombre d'actions prises entre la septième et sixième  et entre la huitième et septième souscription

![](../asset/data_analysis_TDL/images/Distribution%20des%20types%20de%20variations%20du%20nombre%20d%E2%80%99actions%20prises%20entre%20la%20septie%CC%80me%20et%20sixie%CC%80me%20et%20entre%20la%20huitie%CC%80me%20et%20septie%CC%80me%20souscription%20%20.png)

### Box plot des durée entre reprises de souscription en fonction des différents types d'actionnaires

![](../asset/data_analysis_TDL/images/Box%20plot%20des%20dure%CC%81e%20entre%20reprises%20de%20souscription%20en%20fonction%20des%20diffe%CC%81rents%20types%20d%E2%80%99actionnaires%20.png)

### Répartition des parts du capital possédé parmi les 9 derniers centiles des actionnaires les plus riches

![](../asset/data_analysis_TDL/images/Re%CC%81partition%20des%20parts%20du%20capital%20posse%CC%81de%CC%81%20parmi%20les%209%20derniers%20centiles%20des%20actionnaires%20les%20plus%20riches%20%20.png)

### Test Chi-2 et test post ANOVA pour définir la relation entre l'affectation des différentes souscriptions et le nombre moyens d'actions par souscription

![](../asset/data_analysis_TDL/images/Test%20Chi-2%20et%20test%20post%20ANOVA%20pour%20de%CC%81finir%20la%20relation%20entre%20l%E2%80%99affectation%20des%20diffe%CC%81rentes%20souscriptions%20et%20le%20nombre%20moyens%20d%E2%80%99actions%20par%20souscription%20%20.png). 


