# Plan du portfolio
 
**1.Projet  analyse de données : système d'actionnariat chez Terre de Liens**
 
**2.Modélisation statistique en données de panel : application de la méthode des prix hédoniques au marché immobilier Lyonnais**

**3.Modélisation statistique en données de panel : analyse des déterminants des salaires aux Etats-Unis**


# 1.Projet  analyse de données : système d'actionnariat chez Terre de Liens

## Présentation du contexte de l'analyse de données
J'ai pu réaliser ce projet d'analyse de données lors de mon stage en tant que data analyst chez Terre de Lien. Resituons dans un premier temps le système d’actionnariat mis en place par Terre de Liens. Ce dernier permet à tout individu d’acheter des actions auprès de sa société foncière afin d’augmenter le capital lui permettant d’acheter des terres agricoles et d’y installer des personnes ayant des projets d’installation agricole.

Il est donc possible de souscrire à la Foncière Terre de liens en achetant une ou plusieurs actions et d’affecter ce montant à 3 post différents (à une ferme ou terre agricole en particulier, à la Fondation Terre de liens ou à une association régionale Terre de Liens.

Ayant la volonté de mieux connaître et comprendre la stabilité de ce système, de lepérenniser et d’augmenter le capital de la foncière, Terre de Liens m’a missionné pour produire une analyse de ce système d’actionnariat. Il s’agissait de comprendre avant tout sur quels types d’actionnaires reposait ce systèmes (en termes de profils et de montants investis), ainsi que d’identifier leurs comportements vis-à-vis de la société foncière (volume d’achat d’actions et de rachats, intervalles en reprises d’actions, rachats d’actions, etc).

Il était ensuite possible de procéder à différents tests statistiques pour mettre en lumière de potentielles corrélations ou pas entre différents profils d’actionnaires et différents comportements.

La base de données utilisée pour ce travail comportait dans sa version brute 39 476 lignes et 25 champs d’intérêt. Dans un souci de protection des données, une base fictive a été recrée pour transmettre la méthodologie employée lors de ce chantier. Cette base fictive reproduit la structure de données initialement utilisées. Il est possible de la retrouver au sein de ce portafoglio dans le document 2. Jupyter notebook analyse actionnariat.ipynb, elle est alimentée aléatoirement par de nouvelles données à chaque fois que le code qui permet l’analyse est exécuté.

## Code et quelques éléments de data vizualisation

Le code de ce chantier d'analyse est disponible via ce [lien](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/main/Jupyter_notebook_analyse_actionnariat.ipynb). Il s'agit d'un code en python réalisé en Jupyter Notebook sous VS Code

Le document complet de l'analyse qui contient plus de 100 indicateurs est retrouvable à ce [lien](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/fe1335462faf97cd26af4c2f2847227b83d1d6f4/doc%20complet/3.%20Export%20PDF%20des%20r%C3%A9sultats%20de%20l'analyse.pdf) quant à lui 

**Voici quelques indicateurs extraits de l'analyse :**

**Analyse de la variation moyenne du nombre d'actions souscrites entre chaque rang de souscriptions prises**
![](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/81e05caf950c09f7ea2af1e7eff2562db3c499a3/image/Capture%20d'%C3%A9cran%202023-10-10%20125047.png) 
![](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/81e05caf950c09f7ea2af1e7eff2562db3c499a3/image/Capture%20d'%C3%A9cran%202023-10-10%20125047.png) 

**Distribution des types de variations du nombre d'actions prises entre la septième et sixième  et entre la huitième et septième souscription**
![](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/fe1335462faf97cd26af4c2f2847227b83d1d6f4/image/Capture%20d'%C3%A9cran%202023-10-10%20125115.png)
![](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/fe1335462faf97cd26af4c2f2847227b83d1d6f4/image/Capture%20d'%C3%A9cran%202023-10-10%20125115.png)

**Box plot des durée entre reprises de souscription en fonction des différents types d'actionnaires**
![](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/fe1335462faf97cd26af4c2f2847227b83d1d6f4/image/Capture%20d'%C3%A9cran%202023-10-10%20125152.png)
![](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/fe1335462faf97cd26af4c2f2847227b83d1d6f4/image/Capture%20d'%C3%A9cran%202023-10-10%20125152.png)

**Répartition des parts du capital possédé parmi les ç derniers centiles des actionnaires les plus riches**
![](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/fe1335462faf97cd26af4c2f2847227b83d1d6f4/image/Capture%20d'%C3%A9cran%202023-10-10%20125214.png)
![](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/fe1335462faf97cd26af4c2f2847227b83d1d6f4/image/Capture%20d'%C3%A9cran%202023-10-10%20125214.png)

**Régression linéaire du temps moyens pour reprises de souscription en fonction du moyen d'actions par souscriptions prises par personnes**
![](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/fe1335462faf97cd26af4c2f2847227b83d1d6f4/image/Capture%20d'%C3%A9cran%202023-10-10%20125255.png)
![](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/fe1335462faf97cd26af4c2f2847227b83d1d6f4/image/Capture%20d'%C3%A9cran%202023-10-10%20125255.png)

**Test Chi-2 et test post ANOVA pour définir la relation entre l'affectation des différentes souscriptions et le nombre moyens d'actions par souscription**
![](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/fe1335462faf97cd26af4c2f2847227b83d1d6f4/image/Capture%20d'%C3%A9cran%202023-10-10%20125319.png)
![](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/fe1335462faf97cd26af4c2f2847227b83d1d6f4/image/Capture%20d'%C3%A9cran%202023-10-10%20125319.png)

# 2.Modélisation statistique en données de panel : application de la méthode des prix hédoniques au marché immobilier Lyonnais 

## Présentation du contexte de la modélisation statistique portant sur l’application de la méthode des prix hédoniques au marché immobilier lyonnaise

Le travail de modélisation statistique s’est fait à partir de 6 bases de données différentes comportant des informations sur des biens immobiliers mises à la vente sur Lyon et sur leur valeur foncière. Ce sont des bases de données open source à retrouver sur
https://app.dvf.etalab.gouv.fr/. Il s’agissait avant tout pour ce travail de tester l’effet de l’éloignement au centre ville sur la détermination des prix des caractéristiques des biens (nombre de chambre, pièces, types de bien,etc). Il aura fallu s’intéresser aux valeurs foncières de biens de 2 quartiers à chaque fois, un loin du centre et un autre près du centre pour 2 arrondissements différents de Lyon (ayant la même réputation) et 2 quartiers (loin et près) de Villeurbanne (commune frontalière de Lyon). Les bases de données sont à retrouver dans le [document suivant](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/tree/fe1335462faf97cd26af4c2f2847227b83d1d6f4/BD%20DVF).

Les résultats de cette analyse statistique auront permis de quantifier l’impact de l’éloignement ainsi que la dotation d’autres caractéristiques des logements sur la détermination de leur prix. Les résultats sont à retrouver sur le [document suivant](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/fe1335462faf97cd26af4c2f2847227b83d1d6f4/doc%20complet/2.Rapport%20final%20de%20la%20mod%C3%A9lisation%20statistique.pdf)

## Code et quelques éléments de data vizualisation

Le code qui aura permis de réaliser l'analyse de données et ensuite de spécifier un modèle statistique est disponible [ici](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/fe1335462faf97cd26af4c2f2847227b83d1d6f4/COTT%20cv.rmd). Le code a été écrit en language R et écrit sous Rstudio en markdown

**Voici quelques statistiques descriptives ainsi qu'un des modèles spécifiés tirés du projet**
 
**Statisitiques descrives portant sur les valeurs d'intérets de la base de données utilisée**
![](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/fe1335462faf97cd26af4c2f2847227b83d1d6f4/image/Capture%20d'%C3%A9cran%202023-10-10%20181154.png)
![](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/fe1335462faf97cd26af4c2f2847227b83d1d6f4/image/Capture%20d'%C3%A9cran%202023-10-10%20181154.png)

**Box plot des valeurs foncières dépendant des catégories de biens regroupés par nombre de pièces dont ils disposent**
![](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/fe1335462faf97cd26af4c2f2847227b83d1d6f4/image/Capture%20d'%C3%A9cran%202023-10-10%20181211.png)
![](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/fe1335462faf97cd26af4c2f2847227b83d1d6f4/image/Capture%20d'%C3%A9cran%202023-10-10%20181211.png)

**Scatter plot de la valeur foncières des biens en fonction de leur éloignement au centre**
![](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/fe1335462faf97cd26af4c2f2847227b83d1d6f4/image/Capture%20d'%C3%A9cran%202023-10-10%20181233.png)
![](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/fe1335462faf97cd26af4c2f2847227b83d1d6f4/image/Capture%20d'%C3%A9cran%202023-10-10%20181233.png)

**Modèle statististique permettant de tester l'effet l'éloignement au centre sur le prix des biens en isolant les effets de "prestige des arrondissements"**
![](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/fe1335462faf97cd26af4c2f2847227b83d1d6f4/image/Capture%20d'%C3%A9cran%202023-10-10%20181340.png)
![](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/fe1335462faf97cd26af4c2f2847227b83d1d6f4/image/Capture%20d'%C3%A9cran%202023-10-10%20181340.png)

# 3. Modélisation statistique en données de panel : analyse des déterminants des salaires aux Etats-Unis

## Présentation du contexte de la modélisation statistique

Le travail de modélisation statistique s’est fait à partir de la base de données : wagepan disponible en open source dans le package wooldridge disponible avec R. Wooldridge. Elle contient des informations sur les salaires et les caractéristiques des travailleurs aux États-Unis. Il s’agit de données de panel donc ayant une dimension transversale et temporelle. L’enjeu principal du travail résidait dans le choix d’un estimateur adapté au contexte de l’étude (entre estimateur Within, Between, D1, Pooling) ainsi que dans le choix d’une spécification de modèle statistique le plus approprié permettant de comprendre la détermination des salaires aux Etats-Unis en vue des variables d’études à disposition.

Ainsi il s’agissait de savoir s’il était préférable de spécifier un modèle considérant des effets individuels ou non (à savoir si les variables explicatives ont les mêmes effets pour chaque individu), si les caractéristiques individuelles inobservées étaient à considérer de manières fixe ou aléatoire ( à savoir si les caractéristiques intrinsèques de chaque individu étaient corrélées aux variables explicatives, ex : motivation et poursuite de longues études). Après la spécification d’un modèle à effets individuels fixes donc grâce à un estimateur within, l’enjeu était de déterminer les effets des caractéristiques constantes dans le temps (effet de la couleur de peau sur les salaires) qui sont par nature neutralisés par l’estimation within. La solution préconisée face à ce problème aura été de spécifier un modèle dynamique qu’est celui d'Haussmann-Taylor.

Les résultats de cette analyse statistique auront permis de quantifier l’impact de différentes caractéristiques de personnes qu’elles soient constantes ou non dans le temps (origine ethnique, années d‘éducation vs expérience) sur la détermination des salaires d’états-unis. Les résultats sont à retrouver dans le [document présent](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/226eb72438cfe9a102b06dbfa27a073cc399dca5/doc%20complet/2.Rapport%20final%20de%20la%20mod%C3%A9lisation%20statistique%20(1).pdf)

## Code et quelques éléments de data vizualisation

Le code qui a été produit pour ce projet d'analyse de données et de modélisation statistique est disponible [ici](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/226eb72438cfe9a102b06dbfa27a073cc399dca5/3.Code%20en%20R%20pour%20la%20r%C3%A9alisation%20de%20la%20mod%C3%A9lisation%20statistique.rmd). Le code a été écrit en language R et écrit sous Rstudio en markdown

**Voici quelques statistiques descriptives ainsi qu'un des modèles spécifiés tirés du projet**

**Distribution des salaires disponibles dans la base**
![](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/226eb72438cfe9a102b06dbfa27a073cc399dca5/image/Capture%20d'%C3%A9cran%202023-10-10%20184528.png)
![](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/226eb72438cfe9a102b06dbfa27a073cc399dca5/image/Capture%20d'%C3%A9cran%202023-10-10%20184528.png)

**Box Plots des moyennes des salaires sur la période étudiée en fonction des catégories de métiers des individus présents dans la base**
![](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/226eb72438cfe9a102b06dbfa27a073cc399dca5/image/Capture%20d'%C3%A9cran%202023-10-10%20184533.png)
![](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/226eb72438cfe9a102b06dbfa27a073cc399dca5/image/Capture%20d'%C3%A9cran%202023-10-10%20184533.png)

**Evolution des salaires moyens par secteurs d'activités sur la période étudiée**
![](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/226eb72438cfe9a102b06dbfa27a073cc399dca5/image/Capture%20d'%C3%A9cran%202023-10-10%20184548.png)
![](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/226eb72438cfe9a102b06dbfa27a073cc399dca5/image/Capture%20d'%C3%A9cran%202023-10-10%20184548.png)

**Tableau des résultats de la spécification d'un modèle Haussmann Taylor permettant d'attester des effets de régresseurs constant dans le temps dans le cadre d'une estimation within à effet fixe**

![](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/226eb72438cfe9a102b06dbfa27a073cc399dca5/image/Capture%20d'%C3%A9cran%202023-10-10%20184700.png)
![](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/226eb72438cfe9a102b06dbfa27a073cc399dca5/image/Capture%20d'%C3%A9cran%202023-10-10%20184700.png)
