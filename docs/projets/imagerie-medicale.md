# Application web de computer vision : Réseau de neuronnes convultif et classification d'imageries médicales

## Présentation de l'application streamlit et strucutre du modèle CNN

L'enjeu de ce projet était de créer une application web streamlit qui permet d'insérer une image, le modèle prédit ensuite s'il s'agit d'une imagerie médicale du cerveau, des poumons ou la classe autres qui signifie qu'il ne s'agit d'aucune de ces classes précédentes. L'application est accessible [ici](https://cnnimageriesmedicales.streamlit.app/).

Les prédictions se basent sur un modèle de neuronnes convultif simple. Il aura été entrainé sur 18 777 images représentant des imageries médicales de cerveaux, de poumons et d'autres photos random (visages, paysages, animaux, monuments, figures abstraites) en libre accès sur des base de données Kaggle. La validation a été faite sur 4 217 images par la suite. Le notebook qui a permis de réaliser ce modèle est accessible [ici](../asset/Computer_vision/notebooks/Pre%CC%81diction%20imagerie%20me%CC%81dicale.ipynb).

La réseaux de neuronnes a été consrtuit selon les paramètres suivants : 

- Normalisation de la taille des images 

- Différentes couches de convolution 2D avec 128, 64, 32, et 16 filtres de taile 4X4 

- Rajout de couche de maxpooling à chaque fois pour résumer les features maps obtenue par les couches de concolutions

- Rajout d'une couche  Flatten qui réduit la dimension des features maps en un vecteur pour simplification d'apprentissage

- Rajout de couche dense avec 64 neuronnes pour apprentissage des informations tirées des couhces de convultion, de pooling et de la couche Flatten.

- Dernière couche à 3 neuronnes retournant la probabilité qu'une image appartienne à une classe ou aux autres. 

- Entrainement du modèe sur 3 époques

Il se résume alors de la sorte :  

![](../asset/Computer_vision/images/perf1_CNN.png)
![](../asset/Computer_vision/images/perf2_CNN.png)





Les performances du modèle sont très élevées, ce qui pourrait laisser penser qu'il y a eu du sur apprentissage. En réalité ceci est du au manque de diversité entre les images du set d'apprentissage et du set d'entraînement. En effet même si les images n'étaient pas les mêmes elles se ressemblaient tout de même (Les IRM du cerveau se ressemblant toutes par exemple). 

## Limites du modèle

Ce modèle est un modèle simple, le set d'apprentissage est tout de même réduit et la diversité des images y étant inclues reste à relativiser. En effet face à des contraintes d'accès à des images assez diversifiées et face à une capacité de gestion de données réduite, le modèle peut avoir du mal a reconnaitre une image qui contiendrait tout de même une imagerie médicale de cerveau ou de poumons mais étant peu "conventionnel".

## Retour du modèle via l'application streamlit

![](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/59befe64823ff0e53c9c5f540ce118e9c84a7fc7/docs/asset/Computer_vision/images/app.png)
