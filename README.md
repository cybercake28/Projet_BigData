# Projet Big Data

## Description
Ce projet Big Data est conçu pour analyser de grands ensembles de données à l'aide de Python. Il comprend un script principal (`projet.py`) ainsi qu'un notebook pour une exploration plus approfondie des données.

## Prérequis
- Python 3 doit être installé sur votre système.

## Installation
1. Téléchargez le fichier `projet.py`.
2. Téléchargez le notebook associé.
3. Assurez-vous que les fichiers sont stockés dans le même répertoire.

## Lancement du Projet
Pour lancer le projet, exécutez la commande suivante dans votre terminal :
```
python3 projet.py
```

## Instructions
1. Une fois le projet démarré, les différents packages nécessaires seront installés automatiquement.
2. Une fenêtre apparaîtra, cliquez sur le bouton "Start Notebook".
3. Le serveur Notebook se lancera et se connectera.
4. Accédez ensuite au notebook pour commencer l'analyse des données.

---


# Compte Rendu du Notebook

## Description
Ce notebook présente un projet d'analyse de données utilisant des données de pose humaine provenant du jeu de données SBU Kinect Interactions. Le projet vise à entraîner un modèle de reconnaissance d'interaction entre deux personnes à partir de leurs poses.

## Contenu du Notebook
1. **Importation des Bibliothèques :** Le notebook commence par l'importation des bibliothèques nécessaires telles que numpy, keras, et les fonctions utilitaires et le modèle spécifiés dans les fichiers `utils.py` et `model.py`.

2. **Téléchargement des Données :** Les liens vers les fichiers de données sont spécifiés et téléchargés à partir des sources en ligne.

3. **Création des Ensembles de Test et d'Entraînement :** Les données sont divisées en ensembles de test et d'entraînement, prêtes pour l'analyse.

4. **Configuration du Modèle et Entraînement :** Le modèle est configuré avec l'optimiseur Adam et la fonction de perte de l'erreur quadratique moyenne. Un résumé du modèle est affiché. Le modèle est ensuite entraîné sur plusieurs époques avec des données d'entraînement.

5. **Évaluation du Modèle :** Des étapes sont entreprises pour évaluer les performances du modèle, y compris des ajustements du taux d'apprentissage.

6. **Visualisation des Résultats :** Des exemples de poses humaines sont affichés pour illustrer le processus de reconnaissance.

## Objectifs
- Entraîner un modèle de reconnaissance d'interaction basé sur des données de pose humaine.
- Évaluer les performances du modèle sur des ensembles de données de test.
- Optimiser le modèle pour améliorer les résultats de classification.

## Perspectives Futures
- Explorer d'autres architectures de modèle pour améliorer les performances.
- Augmenter la taille et la diversité des ensembles de données pour une meilleure généralisation.
- Intégrer des techniques de prétraitement des données pour améliorer la qualité des entrées du modèle.

---
**Note :** Assurez-vous d'avoir les autorisations appropriées pour utiliser les données téléchargées à partir des liens fournis dans le notebook.
