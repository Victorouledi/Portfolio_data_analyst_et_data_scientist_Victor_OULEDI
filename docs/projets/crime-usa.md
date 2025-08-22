# 2. Clustering, et Analyse en Composantes Principales en Python  sur la criminalité aux Etats-Unis

## Présentation du contexte de l'analyse de données
Ce travail a été effectué dans le cadre d'une auto formation grace aux supports de Formasys.La base de données étudiée comporte des observations pour les 50 états des USA concernant 4 variables d'intéret.

"Murder" représente le taux de meurtre pour 100 000 habitants dans chaque État.
"Assault" correspond au nombre d'agressions pour 100 000 habitants.
"UrbanPop" indique le pourcentage de la population résidant dans des zones urbaines.
"Rape" représente le taux de viols pour 100 000 habitants.

L'enjeux du travail consistait dans un premier temps à utiliser l'agorithme kmeans dans le but de regrouper les états au sein d'un nombre de cluster optimal ou le plus pertinent possible. Le nombre de clusters optimal a été déterminer à hauteur de 4.

Une fois le clustering effectué, il s'agissait d'effectuer une réduction de dimensions des données grâce à une ACP afin de pouvoir visualiser la répartition relative des états entre eux. Autrement dit il s'agissait de savoir sur quelles caractéristiques il était possible de rapprocher ou distinguer les états et de savoir sur quels critères les clusters avaient été établis. Notons que l'application d'un ACP se fait uniquement avec des données quantitatives


## Code et quelques éléments de data vizualisation
La base de données est à retrouver [ici](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/a56bcd8e730e852f0ed5949ac902ec4b930507d5/docs/asset/Clustering_USA_crime/data/dataset_USA.csv). Le code qui a permi la réalisation du travail est à retrouver sous forme de jupyter notebook via ce [lien](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/a56bcd8e730e852f0ed5949ac902ec4b930507d5/docs/asset/Clustering_USA_crime/notebooks/crime_usa_clustering.ipynb).  

**Analyse des variables**

![](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/a56bcd8e730e852f0ed5949ac902ec4b930507d5/docs/asset/Clustering_USA_crime/images/analyse%20variable.png)

**Détermination du nombre de clusters optimal**

![](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/a56bcd8e730e852f0ed5949ac902ec4b930507d5/docs/asset/Clustering_USA_crime/images/de%CC%81termination%20du%20nombre%20de%20cluster.png)

Ici on voit que le gain d'inertie ne devient plus significatif une fois atteint 4 clusters.

**Première visualisation des clusters sur différents plans relatifs à différentes combinaisons de 2 variables**

![](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/a56bcd8e730e852f0ed5949ac902ec4b930507d5/docs/asset/Clustering_USA_crime/images/Premie%CC%80re%20visualisation%20des%20cluster%20sur%20des%20plans%20relatifs%20a%CC%80%202%20variables.png)

**Nombre de composantes principales à garder pour la réduction de dimensions des données en fonction de la variabilité qu'elles expliquent pour ces-dernières**

![](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/a56bcd8e730e852f0ed5949ac902ec4b930507d5/docs/asset/Clustering_USA_crime/images/De%CC%81termination%20du%20nombre%20de%20composantes%20principales%20a%CC%80%20conserver.png)

On observe qu'en conservant 2 composantes qui sont une combinaison linéaire des différents variables, on captures déjà près de 87 % de la variabilité des données. 

**Visualisation des individus et clusters suite à la réduction de dimension superposée au cercle de corrélation de l'ACP**

![](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/a56bcd8e730e852f0ed5949ac902ec4b930507d5/docs/asset/Clustering_USA_crime/images/cercle%20de%20corre%CC%81lation.png)

Grâce à cette réduction de dimension il est ainsi possible de voir comment rapprocher ou distinguer les états et sur quels critères ces comparaisons peuvent être effectuées. 
