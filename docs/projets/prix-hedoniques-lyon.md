---
title: "Économétrie — Prix hédoniques (marché immobilier lyonnais)"
permalink: /projets/prix-hedoniques-lyon/
layout: single
classes: wide
toc: true
---

## Contexte & objectif
Analyse hédonique des **prix immobiliers** sur Lyon/Villeurbanne à partir de **données DVF** et sources ouvertes.  
Objectif : estimer l’impact des **caractéristiques du bien** (surface, pièces, type…), de l’**éloignement au centre-ville** et d’effets géographiques locaux (« prestige ») sur le **prix**.

- Données : DVF (open data) — [accès DVF](https://app.dvf.etalab.gouv.fr/)  
- Dossier projet : [ressources](../asset/data_analysis_DVF/data)  
- Script RMarkdown : [COTT_cv.Rmd](../asset/data_analysis_DVF/notebooks/COTT%20cv.rmd)

## Stack & outillage
- **R** : tidyverse (`dplyr`, `readr`, `tidyr`), **ggplot2**
- **Éco/Panel** : `fixest` / `plm`, `lmtest`, `sandwich`, `car`, `splines`
- **Tables** : `stargazer` / `modelsummary`, `broom`


## Données & variables
Plusieurs jeux combinés (DVF + enrichissements) : biens vendus, caractéristiques (surface, nb pièces/chambres, type), **localisation** (arrondissement/quartier), et **distance au centre**.  
Comparaison de zones : deux arrondissements (quartiers proches/éloignés) et deux quartiers de Villeurbanne.


### Voici quelques statistiques descriptives ainsi qu'un des modèles spécifiés tirés du projet
 
### Statisitiques descrives portant sur les valeurs d'intérets de la base de données utilisée

![](../asset/data_analysis_DVF/images/Statisitiques%20descrives%20portant%20sur%20les%20valeurs%20d%E2%80%99inte%CC%81rets%20de%20la%20base%20de%20donne%CC%81es%20utilise%CC%81e%20%20.png)

### Box plot des valeurs foncières dépendant des catégories de biens regroupés par nombre de pièces dont ils disposent

![](../asset/data_analysis_DVF/images/Box%20plot%20des%20valeurs%20foncie%CC%80res%20de%CC%81pendant%20des%20cate%CC%81gories%20de%20biens%20regroupe%CC%81s%20par%20nombre%20de%20pie%CC%80ces%20dont%20ils%20disposent%20%20.png)


### Modèle statististique permettant de tester l'effet l'éloignement au centre sur le prix des biens en isolant les effets de "prestige des arrondissements"

![](../asset/data_analysis_DVF/images/Mode%CC%80le%20statististique%20permettant%20de%20tester%20l%E2%80%99effet%20l%E2%80%99e%CC%81loignement%20au%20centre%20sur%20le%20prix%20des%20biens%20en%20isolant%20les%20effets%20de%20%E2%80%9Cprestige%20des%20arrondissements%E2%80%9D%20%20.png)



