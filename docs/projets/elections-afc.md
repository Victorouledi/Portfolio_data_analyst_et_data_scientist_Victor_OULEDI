---
title: "AFC — Élections présidentielles 2022 (Île-de-France)"
permalink: /projets/elections-afc/
layout: single
classes: wide
toc: true
---

## Contexte & objectif
Analyse factorielle des correspondances (**AFC**) sur les résultats des **élections présidentielles 2022** en **Île-de-France**.  
Objectifs :
1. Construire un **tableau de contingence** *départements × candidats*.
2. Réaliser une **AFC** pour réduire la dimension et **visualiser les proximités/contrastes** entre départements et candidats.
3. Interpréter les axes via **cos²** (qualité de représentation) et **contributions** (poids dans la construction des axes).

## Données & code
- Données : [election_2022_FRA.xlsx](../asset/ACF_elections_presidentielles/data/election_2022_FRA.xlsx)  
- Notebook : [AFC_With_Python_Election_presidentielle.ipynb](../asset/ACF_elections_presidentielles/notebooks/AFC_With_Python%20Election%20pre%CC%81sidentielle%20.ipynb)  
- Stack : **pandas**, **numpy**, **prince** (ou `mca`), **matplotlib** / **seaborn** / **plotly**

## Stack & outillage
- **Python** : pandas/NumPy, **prince** (AFC) ou `mca`
- **Viz** : Matplotlib/Seaborn/Plotly (maps/factor maps)


## Tableau de contingence
Reconstitution des effectifs *département × candidat* (1ᵉʳ tour). Cette base sert d’entrée à l’AFC.

![Tableau de contingence](../asset/ACF_elections_presidentielles/images/TB%20contingence.png)

## Classement des candidats par nombre de votes
Vue globale des volumes pour apprécier les ordres de grandeur avant l’AFC.

![Classement des candidats](../asset/ACF_elections_presidentielles/images/classement%20e%CC%81lecteur.png)

## Qualité de représentation (cos²) sur les deux premiers axes
Après analyse de l’inertie, on retient **2 axes** (cumul d’inertie expliqué le plus élevé et ruptures visibles).  
Le **cos²** indique si un point (département/candidat) est bien représenté sur le plan factoriel (axes 1 & 2).  
> Règle pratique : interpréter prioritairement les points de **cos² ≥ 0,5**.

![Qualité de représentation (cos²)](../asset/ACF_elections_presidentielles/images/Qualite%CC%81%20de%20la%20repre%CC%81sentativite%CC%81%20.png)

## Factor maps (profils lignes & colonnes)
Les deux factor maps permettent :
- de **rapprocher** les départements qui partagent des profils de vote similaires,  
- de **rapprocher** les candidats co-plébiscités par des zones proches,  
- d’identifier des **oppositions** (positions opposées sur l’axe 1 ou 2).

![Factor_map](../asset/ACF_elections_presidentielles/images/Factor%20map.png)
