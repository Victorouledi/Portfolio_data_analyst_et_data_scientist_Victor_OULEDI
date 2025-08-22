# 3. Analyse factorielle des correspondances (AFC): elections présidentielles 2022, focus sur l'Ile de France. 

Ce travail a été effectué dans le cadre d'une auto-formation grâce aux supports de cours de LeCoinstat. Grâce à des données retraçant le nombre de votes pour les différents candidats en liste pour les élections présidentielles de 2022 au seins des différents départements d'Ile de France, il s'agissait de mettre en place une analyse factorielle des correspondances entre différents candidats et différents départements. Il s'agissait ici d'effectuer également une réduction de dimensions des données, faisant face à des variables catégorielles (candidats et départements), une AFC s'imposait plutôt qu'une ACP. 

L'objectif de ce travail était alors de pouvoir rapprocher des candidats et des départements entre eux en fonction de la typologie des votes. 

## Code et quelques éléments de data vizualisation
La base de données est à retrouver [ici](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/df2d470fc0f39606d0e5b3fd9c6a14ed38f80e5c/docs/asset/ACF_elections_presidentielles/data/election_2022_FRA.xlsx). Le code qui a permi la réalisation du travail est à retrouver sous forme de jupyter notebook via ce [lien](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/df2d470fc0f39606d0e5b3fd9c6a14ed38f80e5c/docs/asset/ACF_elections_presidentielles/notebooks/AFC_With_Python%20Election%20pre%CC%81sidentielle%20.ipynb). 

**Tableau de contingence entre les différentes variables**

![](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/df2d470fc0f39606d0e5b3fd9c6a14ed38f80e5c/docs/asset/ACF_elections_presidentielles/images/TB%20contingence.png)

**Classements des candidats par nombre de votes**

![](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/df2d470fc0f39606d0e5b3fd9c6a14ed38f80e5c/docs/asset/ACF_elections_presidentielles/images/classement%20e%CC%81lecteur.png)

**Qualité de la représentativité des variables parmi les composants**

Après avoir déterminé qu'il faille garder composants pour cette analyse car explicants à eux deux une assez forte variabilité des données, il s'agissait de regarder si les différentes variables étaient bien représentées parmi les composants. Pour cela il faut s'inétéresser au cos2 qui  mesurent l'association entre chaque variable et chaque axe factoriel sur un plan formé par nos 2 composantes principales. Ainsi il a été possible de s'intéresser aux profils lignes (les départements) et aux profils colonnes(les candidats). Il sera possible d'interpréter les positionnements relatifs des départements et des candidats uniquement si leur cosinus carré est supérieur à 0,5 en considérant les axes factoriels 1 et 2 (composantes 1 et 2). 

![](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/df2d470fc0f39606d0e5b3fd9c6a14ed38f80e5c/docs/asset/ACF_elections_presidentielles/images/Qualite%CC%81%20de%20la%20repre%CC%81sentativite%CC%81%20.png)

**Factor maps superposées des analyses de profils lignes et colonnes**

En obtenant une factor map il est possible de rapprocher ou distinguer certains candidats en fonction de leur points communs en termes de votes parmi les différents départements, et il est egalement possible de rapprocher ou distinguer des départements en fonction des votes qu'ils ont comptabilisé pour différents candidats. Comme précisé précédemment, il sera possible de tirer des conclusions concernant la position relative des candidats et des département entre eux uniquement si ces derniers ont une assez bonne représentativité dans la détermination des composants sélectionnés. 

![](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/df2d470fc0f39606d0e5b3fd9c6a14ed38f80e5c/docs/asset/ACF_elections_presidentielles/images/Factor%20map.png)
