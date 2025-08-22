# Modélisation statistique en données de panel en R : analyse des déterminants des salaires aux Etats-Unis

## Présentation du contexte de la modélisation statistique

Le travail de modélisation statistique s’est fait à partir de la base de données : wagepan disponible en open source dans le package wooldridge disponible avec R. Wooldridge. Elle contient des informations sur les salaires et les caractéristiques des travailleurs aux États-Unis. Il s’agit de données de panel donc ayant une dimension transversale et temporelle. L’enjeu principal du travail résidait dans le choix d’un estimateur adapté au contexte de l’étude (entre estimateur Within, Between, D1, Pooling) ainsi que dans le choix d’une spécification de modèle statistique le plus approprié permettant de comprendre la détermination des salaires aux Etats-Unis en vue des variables d’études à disposition.

Ainsi il s’agissait de savoir s’il était préférable de spécifier un modèle considérant des effets individuels ou non (à savoir si les variables explicatives ont les mêmes effets pour chaque individu), si les caractéristiques individuelles inobservées étaient à considérer de manières fixe ou aléatoire ( à savoir si les caractéristiques intrinsèques de chaque individu étaient corrélées aux variables explicatives, ex : motivation et poursuite de longues études). Après la spécification d’un modèle à effets individuels fixes donc grâce à un estimateur within, l’enjeu était de déterminer les effets des caractéristiques constantes dans le temps (effet de la couleur de peau sur les salaires) qui sont par nature neutralisés par l’estimation within. La solution préconisée face à ce problème aura été de spécifier un modèle dynamique qu’est celui d'Haussmann-Taylor.

Les résultats de cette analyse statistique auront permis de quantifier l’impact de différentes caractéristiques de personnes qu’elles soient constantes ou non dans le temps (origine ethnique, années d‘éducation vs expérience) sur la détermination des salaires d’Etats-uniens. 

## Code et quelques éléments de data vizualisation

Le code qui a été produit pour ce projet d'analyse de données et de modélisation statistique est disponible [ici](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/4cffee63d669b502189ad9905da7a34ff16ee3da/docs/asset/Panel_analysis_educ_USA/notebooks/3.Code%20en%20R%20pour%20la%20re%CC%81alisation%20de%20la%20mode%CC%81lisation%20statistique.rmd). Le code a été écrit en language R et écrit sous Rstudio en markdown

**Voici quelques statistiques descriptives ainsi qu'un des modèles spécifiés tirés du projet**

**Distribution des salaires disponibles dans la base**

![](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/4cffee63d669b502189ad9905da7a34ff16ee3da/docs/asset/Panel_analysis_educ_USA/images/Distribution%20des%20salaires%20disponibles%20dans%20la%20base%20%20.png)

**Box Plots des moyennes des salaires sur la période étudiée en fonction des catégories de métiers des individus présents dans la base**

![](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/4cffee63d669b502189ad9905da7a34ff16ee3da/docs/asset/Panel_analysis_educ_USA/images/Box%20Plots%20des%20moyennes%20des%20salaires%20sur%20la%20pe%CC%81riode%20e%CC%81tudie%CC%81e%20en%20fonction%20des%20cate%CC%81gories%20de%20me%CC%81tiers%20des%20individus%20pre%CC%81sents%20dans%20la%20base%20%20.png)

**Evolution des salaires moyens par secteurs d'activités sur la période étudiée**

![](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/4cffee63d669b502189ad9905da7a34ff16ee3da/docs/asset/Panel_analysis_educ_USA/images/Evolution%20des%20salaires%20moyens%20par%20secteurs%20d%E2%80%99activite%CC%81s%20sur%20la%20pe%CC%81riode%20e%CC%81tudie%CC%81e%20%20.png)

**Tableau des résultats de la spécification d'un modèle Haussmann Taylor permettant d'attester des effets de régresseurs constants dans le temps dans le cadre d'une estimation within à effet fixe**

![](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/4cffee63d669b502189ad9905da7a34ff16ee3da/docs/asset/Panel_analysis_educ_USA/images/re%CC%81sultats%20de%20la%20spe%CC%81cification%20d%E2%80%99un%20mode%CC%80le%20Haussmann%20Taylor.png)
