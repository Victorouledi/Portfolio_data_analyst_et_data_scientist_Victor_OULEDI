# IA & NLP :  Model LSTM pour  la prédiction du type de sujet conernant les réclamations et pleintes à l'encontre de services financiers

## Présentation du problème : 

Dans ce projet de traitement automatique du langage naturel (NLP), j’ai développé un modèle basé sur une architecture Bidirectional LSTM (Long Short-Term Memory) afin de classer des plaintes clients issues du secteur des services financiers. La base de données comprenait 66 699 plaintes textuelles, chacune décrivant un problème rencontré par un client avec sa banque , ici : Recouvrement de dettes, Rapports de crédit, Prêt étudiant, Prêt sur salaire. Le notebook du travail est disponible [ici](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/70e59cd02392419830b8a624defcdfde0c69a944/docs/asset/NLP_LSTM/notebooks/finance_complaints_NLP.ipynb). La base de données sur laquelle le travail a été fait [ici](https://www.kaggle.com/datasets/selener/consumer-complaint-database) : 

## Modèle LSTM 

Un LSTM (Long Short-Term Memory) est une variante des réseaux de neurones récurrents (RNN) conçue pour mieux gérer les dépendances à long terme dans des séquences.
Il est composé de cellules qui utilisent trois types de portes :

- Porte d’entrée (input gate) : contrôle quelles nouvelles informations sont ajoutées à la mémoire.
- Porte d’oubli (forget gate) : décide quelles informations passées sont conservées ou supprimées.
- Porte de sortie (output gate) : détermine quelles informations de la mémoire sont utilisées pour produire la sortie actuelle.
- Cette structure permet au LSTM de retenir le contexte pertinent sur de longues séquences, évitant le problème du vanishing gradient que rencontrent les RNN classiques.

Cette architecture rend le LSTM particulièrement adapté pour l’interprétation des séquences verbales complexes issues de ce type de données clients.

 ![](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/70e59cd02392419830b8a624defcdfde0c69a944/docs/asset/NLP_LSTM/images/LSTM_archi.png)

## Enjeux du travail

- Un point crucial de ce projet a été la préparation des données, notamment la tokenisation et le padding des séquences textuelles pour normaliser leur longueur avant l’apprentissage : Ainsi il aura fallu pré-traiter permis de nettoyer et homogénéiser les textes. Après suppression des URLs, nombres et ponctuation, puis tokenisation, lemmatisation et suppression des stopwords, le nombre de tokens par plainte a nettement diminué et les séquences sont devenues plus compactes. Ce travail prépare efficacement les données pour l’apprentissage du modèle LSTM. Voila l'évolution du format d'input avec le prétraitement :

![](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/70e59cd02392419830b8a624defcdfde0c69a944/docs/asset/NLP_LSTM/images/Tokenisation.png)

- Un autre défi a résidé dans la gestion des classes déséquilibrées (class imbalance), qui a nécessité des ajustements tels que la pondération des classes et des techniques de sur/sous-échantillonnage pour éviter un biais du modèle vers les classes majoritaires.

![](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/70e59cd02392419830b8a624defcdfde0c69a944/docs/asset/NLP_LSTM/images/DB_LSTM.png)

## Architecture retenue : 

Après avoir tester la sensibilité des performances du modèle avec différentes architectures, l'architecture suivante aura été sélectionnée : 

- Une couche d’embedding transforme chaque mot en un vecteur de 300 dimensions pour représenter son sens.
- Deux couches LSTM bidirectionnelles analysent le texte dans les deux sens pour mieux comprendre le contexte des phrases.
- Une couche dense affine les informations extraites avant la prédiction.
- Une couche de sortie prédit la catégorie de plainte parmi les quatre disponibles.
- Des techniques de régularisation comme le dropout sont utilisées pour éviter le surapprentissage et améliorer les performances du modèle. Egalement de la pondération de classe pour gérer les class inbalance.

![](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/b8359024717a385f84caf7fdb843ce60a8ae8480/docs/asset/NLP_LSTM/images/Model_LSTM.png)

## Résultats :

**Les performances du modèle optimal retenu ont été les suivantes :** 

![](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/70e59cd02392419830b8a624defcdfde0c69a944/docs/asset/NLP_LSTM/images/ROC_Curve_LSTM.png)
![](https://github.com/Victorouledi/Portfolio_data_analyst_et_data_scientist_Victor_OULEDI/blob/70e59cd02392419830b8a624defcdfde0c69a944/docs/asset/NLP_LSTM/images/Mconfution_LSTM.png)

