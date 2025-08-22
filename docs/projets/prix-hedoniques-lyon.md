# 4.Modélisation statistique en données de panel en R : application de la méthode des prix hédoniques au marché immobilier Lyonnais 

## Présentation du contexte de la modélisation statistique portant sur l’application de la méthode des prix hédoniques au marché immobilier lyonnaise

Le travail de modélisation statistique s’est fait à partir de 6 bases de données différentes comportant des informations sur des biens immobiliers mises à la vente sur Lyon et sur leur valeur foncière. Ce sont des bases de données open source à retrouver sur
https://app.dvf.etalab.gouv.fr/. Il s’agissait avant tout pour ce travail de tester l’effet de l’éloignement au centre ville sur la détermination des prix des caractéristiques des biens (nombre de chambre, pièces, types de bien,etc). Il aura fallu s’intéresser aux valeurs foncières de biens de 2 quartiers à chaque fois, un loin du centre et un autre près du centre pour 2 arrondissements différents de Lyon (ayant plus ou moins la même réputation) et 2 quartiers (loin et près) de Villeurbanne (commune frontalière de Lyon). Les bases de données sont à retrouver dans le [document suivant](../asset/data_analysis_DVF/data).


## Code et quelques éléments de data vizualisation

Le code qui aura permis de réaliser l'analyse de données et ensuite de spécifier un modèle statistique est disponible [ici](../asset/data_analysis_DVF/notebooks/COTT%20cv.rmd). Le code a été écrit en language R et écrit sous Rstudio en markdown

**Voici quelques statistiques descriptives ainsi qu'un des modèles spécifiés tirés du projet**
 
**Statisitiques descrives portant sur les valeurs d'intérets de la base de données utilisée**

![](../asset/data_analysis_DVF/images/Statisitiques%20descrives%20portant%20sur%20les%20valeurs%20d%E2%80%99inte%CC%81rets%20de%20la%20base%20de%20donne%CC%81es%20utilise%CC%81e%20%20.png)

**Box plot des valeurs foncières dépendant des catégories de biens regroupés par nombre de pièces dont ils disposent**

![](../asset/data_analysis_DVF/images/Box%20plot%20des%20valeurs%20foncie%CC%80res%20de%CC%81pendant%20des%20cate%CC%81gories%20de%20biens%20regroupe%CC%81s%20par%20nombre%20de%20pie%CC%80ces%20dont%20ils%20disposent%20%20.png)


**Modèle statististique permettant de tester l'effet l'éloignement au centre sur le prix des biens en isolant les effets de "prestige des arrondissements"**

![](../asset/data_analysis_DVF/images/Mode%CC%80le%20statististique%20permettant%20de%20tester%20l%E2%80%99effet%20l%E2%80%99e%CC%81loignement%20au%20centre%20sur%20le%20prix%20des%20biens%20en%20isolant%20les%20effets%20de%20%E2%80%9Cprestige%20des%20arrondissements%E2%80%9D%20%20.png)
