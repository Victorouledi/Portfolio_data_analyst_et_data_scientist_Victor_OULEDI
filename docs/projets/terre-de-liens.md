---
title: "Projet  analyse de données en Python: système d'actionnariat chez Terre de Liens"
permalink: /projets/terre-de-liens/
layout: single
---


# Projet  analyse de données en Python: système d'actionnariat chez Terre de Liens


## Présentation du contexte de l'analyse de données
Lors d'un stage effectué chez Terre de Liens, j'ai été missionné pour la réalisation d'une analyse de données sur le système d'actionnariat mis en place par la structure. Resituons dans un premier temps le système d’actionnariat mis en place par Terre de Liens. Ce dernier permet à tout individu d’acheter des actions auprès de sa société foncière afin d’augmenter le capital lui permettant d’acheter des terres agricoles et d’y installer des personnes ayant des projets d’installation agricole.

Il est donc possible de souscrire à la Foncière Terre de liens en achetant une ou plusieurs actions et d’affecter ce montant à 3 post différents (à une ferme ou terre agricole en particulier, à la Fondation Terre de liens ou à une association régionale Terre de Liens.

Ayant la volonté de mieux connaître et comprendre la stabilité de ce système, de le pérenniser et d’augmenter le capital de la foncière, Terre de Liens m’a missionné pour produire une analyse de ce système d’actionnariat. Il s’agissait de comprendre avant tout sur quels types d’actionnaires reposait ce système (en termes de profils et de montants investis), ainsi que d’identifier leurs comportements vis-à-vis de la société foncière (volume d’achat d’actions et de rachats, intervalles en reprises d’actions, rachats d’actions, etc).

Il était ensuite possible de procéder à différents tests statistiques pour mettre en lumière de potentielles corrélations ou pas entre différents profils d’actionnaires et différents comportements.

La base de données utilisée pour ce travail comportait dans sa version brute 39 476 lignes et 25 champs d’intérêt à extraire sur le cloud Salesforce de la strucutre. Dans un souci de protection des données, une base fictive a été recrée pour transmettre la méthodologie employée lors de ce chantier. Cette base fictive reproduit la structure de données initialement utilisées. Elle est alimentée aléatoirement par de nouvelles données à chaque fois que le code qui permet l’analyse est exécuté.

## Code et quelques éléments de data vizualisation

Le code de ce chantier d'analyse est disponible via ce [lien](../asset/data_analysis_TDL/notebooks/Jupyter_notebook_analyse_actionnariat.ipynb). Il s'agit d'un code en python réalisé en Jupyter Notebook sous VS Code
 

**Voici quelques indicateurs extraits de l'analyse :**

**Analyse de la variation moyenne du nombre d'actions souscrites entre chaque rang de souscriptions prises**

![](../asset/data_analysis_TDL/images/Analyse%20de%20la%20variation%20moyenne%20du%20nombre%20d%E2%80%99actions%20souscrites%20entre%20chaque%20rang%20de%20souscriptions%20prises.png)

**Distribution des types de variations du nombre d'actions prises entre la septième et sixième  et entre la huitième et septième souscription**

![](../asset/data_analysis_TDL/images/Distribution%20des%20types%20de%20variations%20du%20nombre%20d%E2%80%99actions%20prises%20entre%20la%20septie%CC%80me%20et%20sixie%CC%80me%20et%20entre%20la%20huitie%CC%80me%20et%20septie%CC%80me%20souscription%20%20.png)

**Box plot des durée entre reprises de souscription en fonction des différents types d'actionnaires**

![](../asset/data_analysis_TDL/images/Box%20plot%20des%20dure%CC%81e%20entre%20reprises%20de%20souscription%20en%20fonction%20des%20diffe%CC%81rents%20types%20d%E2%80%99actionnaires%20.png)

**Répartition des parts du capital possédé parmi les 9 derniers centiles des actionnaires les plus riches**

![](../asset/data_analysis_TDL/images/Re%CC%81partition%20des%20parts%20du%20capital%20posse%CC%81de%CC%81%20parmi%20les%209%20derniers%20centiles%20des%20actionnaires%20les%20plus%20riches%20%20.png)

**Test Chi-2 et test post ANOVA pour définir la relation entre l'affectation des différentes souscriptions et le nombre moyens d'actions par souscription**

![](../asset/data_analysis_TDL/images/Test%20Chi-2%20et%20test%20post%20ANOVA%20pour%20de%CC%81finir%20la%20relation%20entre%20l%E2%80%99affectation%20des%20diffe%CC%81rentes%20souscriptions%20et%20le%20nombre%20moyens%20d%E2%80%99actions%20par%20souscription%20%20.png). 


