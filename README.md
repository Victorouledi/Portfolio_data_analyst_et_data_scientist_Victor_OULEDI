# Projet  analyse de données : système d'actionnariat chez Terre de Liens
## Présentation du contexte de l'analyse de données
J'ai pu réaliser ce projet d'analyse de données lors de mon stage en tant que data analyst chez Terre de Lien. Resituons dans un premier temps le système d’actionnariat mis en place par Terre de Liens. Ce dernier permet à tout individu d’acheter des actions auprès de sa société foncière afin d’augmenter le capital lui permettant d’acheter des terres agricoles et d’y installer des personnes ayant des projets d’installation agricole.

Il est donc possible de souscrire à la Foncière Terre de liens en achetant une ou plusieurs actions et d’affecter ce montant à 3 post différents (à une ferme ou terre agricole en particulier, à la Fondation Terre de liens ou à une association régionale Terre de Liens.

Ayant la volonté de mieux connaître et comprendre la stabilité de ce système, de lepérenniser et d’augmenter le capital de la foncière, Terre de Liens m’a missionné pour produire une analyse de ce système d’actionnariat. Il s’agissait de comprendre avant tout sur quels types d’actionnaires reposait ce systèmes (en termes de profils et de montants investis), ainsi que d’identifier leurs comportements vis-à-vis de la société foncière (volume d’achat d’actions et de rachats, intervalles en reprises d’actions, rachats d’actions, etc).

Il était ensuite possible de procéder à différents tests statistiques pour mettre en lumière de potentielles corrélations ou pas entre différents profils d’actionnaires et différents comportements.

La base de données utilisée pour ce travail comportait dans sa version brute 39 476 lignes et 25 champs d’intérêt. Dans un souci de protection des données, une base fictive a été recrée pour transmettre la méthodologie employée lors de ce chantier. Cette base fictive reproduit la structure de données initialement utilisées. Il est possible de la retrouver au sein de ce portafoglio dans le document 2. Jupyter notebook analyse actionnariat.ipynb, elle est alimentée aléatoirement par de nouvelles données à chaque fois que le code qui permet l’analyse est exécuté.

## Code et quelques éléments de data vizualisation

Le code de ce chantier d'analyse est disponible via ce [lien](https://github.com/Victorouledi/Portfolio-data-analyst-scientist/blob/5a26a1dabbc65a9b7792e66a4ad4848349767290/Jupyter_notebook_analyse_actionnariat.ipynb)

Le document complet de l'analyse qui contient plus de 100 indicateurs est retrouvable à ce [lien](https://github.com/Victorouledi/Portfolio-data-analyst-scientist/blob/main/doc%20complet/3.%20Export%20PDF%20des%20r%C3%A9sultats%20de%20l'analyse.pdf) quant à lui 

**Voici quelques indicateurs extraits de l'analyse :**

**Analyse de la variation moyenne du nombre d'actions souscrites entre chaque rang de souscriptions prises**
![](https://github.com/Victorouledi/Portfolio-data-analyst-scientist/blob/main/image/Capture%20d'%C3%A9cran%202023-10-10%20125047.png) 

**Distribution des types de variations du nombre d'actions prises entre la septième et sixième  et entre la huitième et septième souscription**
![](https://github.com/Victorouledi/Portfolio-data-analyst-scientist/blob/main/image/Capture%20d'%C3%A9cran%202023-10-10%20125115.png)

**Box plot des durée entre reprises de souscription en fonction des différents types d'actionnaires**
![](https://github.com/Victorouledi/Portfolio-data-analyst-scientist/blob/main/image/Capture%20d'%C3%A9cran%202023-10-10%20125152.png)

**Répartition des parts du capital possédé parmi les ç derniers centiles des actionnaires les plus riches**
![](https://github.com/Victorouledi/Portfolio-data-analyst-scientist/blob/main/image/Capture%20d'%C3%A9cran%202023-10-10%20125214.png)

**Régression linéaire du temps moyens pour reprises de souscription en fonction du moyen d'actions par souscriptions prises par personnes**
![](https://github.com/Victorouledi/Portfolio-data-analyst-scientist/blob/main/image/Capture%20d'%C3%A9cran%202023-10-10%20125255.png)

**Test Chi-2 et test post ANOVA pour définir la relation entre l'affectation des différentes souscriptions et le nombre moyens d'actions par souscription**

![](https://github.com/Victorouledi/Portfolio-data-analyst-scientist/blob/main/image/Capture%20d'%C3%A9cran%202023-10-10%20125319.png)

# Modélisation statistique en données de panel : application de la méthode des prix hédoniques au marché immobilier Lyonnais 

## Présentation du contexte de la modélisation statistique portant sur l’application de la méthode des prix hédoniques au marché immobilier lyonnaise

Le travail de modélisation statistique s’est fait à partir de 6 bases de données différentes comportant des informations sur des biens immobiliers mises à la vente sur Lyon et sur leur valeur foncière. Ce sont des bases de données open source à retrouver sur
https://app.dvf.etalab.gouv.fr/. Il s’agissait avant tout pour ce travail de tester l’effet de l’éloignement au centre ville sur la détermination des prix des caractéristiques des biens (nombre de chambre, pièces, types de bien,etc). Il aura fallu s’intéresser aux valeurs foncières de biens de 2 quartiers à chaque fois, un loin du centre et un autre près du centre pour 2 arrondissements différents de Lyon (ayant la même réputation) et 2 quartiers (loin et près) de Villeurbanne (commune frontalière de Lyon). Les bases de données sont à retrouver dans le dossier “Bases de données à utiliser”.

Les résultats de cette analyse statistique auront permis de quantifier l’impact de l’éloignement ainsi que la dotation d’autres caractéristiques des logements sur la détermination de leur prix. Les résultats sont à retrouver dans le document “Rapport final de la modélisation statistique”
