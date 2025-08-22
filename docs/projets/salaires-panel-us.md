---
title: "Économétrie (panel, R) — Déterminants des salaires aux États-Unis"
permalink: /projets/salaires-panel-us/
layout: single
classes: wide
toc: true
---

## Contexte & objectif
Analyse des **déterminants des salaires** sur données de **panel** (individus × années) issues de `wooldridge::wagepan`.  
Objectifs :
1) choisir une **spécification** crédible (FE/RE/FD) et un **estimateur** adapté,  
2) **identifier** les effets de variables **invariantes** (race/sex, etc.) malgré FE,  
3) évaluer la **robustesse** (tests & SE) et interpréter les **élasticités**.

- Notebook / Rmd : [code](../asset/Panel_analysis_educ_USA/notebooks/3.Code%20en%20R%20pour%20la%20re%CC%81alisation%20de%20la%20mode%CC%81lisation%20statistique.rmd)

## Données & variables (exemples)
Variables usuelles : `wage`, `educ`, `exper`, `tenure`, `union`, `married`, variables démographiques (invariantes), **année**.  
Cible recommandée : **`ln(wage)`** (stabilise la variance ; élasticités interprétables).

## Visualisations descriptives
### Distribution des salaires disponibles dans la base

![](../asset/Panel_analysis_educ_USA/images/Distribution%20des%20salaires%20disponibles%20dans%20la%20base%20%20.png)

### Box Plots des moyennes des salaires sur la période étudiée en fonction des catégories de métiers des individus présents dans la base

![](../asset/Panel_analysis_educ_USA/images/Box%20Plots%20des%20moyennes%20des%20salaires%20sur%20la%20pe%CC%81riode%20e%CC%81tudie%CC%81e%20en%20fonction%20des%20cate%CC%81gories%20de%20me%CC%81tiers%20des%20individus%20pre%CC%81sents%20dans%20la%20base%20%20.png)

### Evolution des salaires moyens par secteurs d'activités sur la période étudiée

![](../asset/Panel_analysis_educ_USA/images/Evolution%20des%20salaires%20moyens%20par%20secteurs%20d%E2%80%99activite%CC%81s%20sur%20la%20pe%CC%81riode%20e%CC%81tudie%CC%81e%20%20.png)

## Modèles estimés : Modèle Haussmann Taylor permettant d'attester des effets de régresseurs constants dans le temps dans le cadre d'une estimation within à effet fixe

![](../asset/Panel_analysis_educ_USA/images/re%CC%81sultats%20de%20la%20spe%CC%81cification%20d%E2%80%99un%20mode%CC%80le%20Haussmann%20Taylor.png)
