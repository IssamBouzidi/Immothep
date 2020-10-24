# Immothep
## Introduction
Module d'estimation de biens basé sur l'intelligence artificielle en Python

## Pré-requis
veuillez installer les modules dans le fichier requirements.txt `conda install --yes --file requirements.txt`  

## Procédure à suivre pour générer les modèles d'estimation  
### Notebooks de préparation et analyse des données
Ces notebook doivent être executés dans l'ordre suivant:
![0-global_analysis.ipynb](./src/0-main_analysis.ipynb)
![1-maison_analysis.ipynb](./src/0-main_analysis.ipynb)
![2-appartement_analysis.ipynb](./src/0-main_analysis.ipynb)

### Notebook de comparaison des modèles d'IA
![3-prediction_comparator.ipynb](./src/3-prediction_comparator.ipynb)

### Notebook de test du modèle
![4-test_prediction.ipynb](./src/4-test_prediction.ipynb)


## Exploitation de l’api  
Une api Fast API pour l'exposition du service d'estimation dans le répertoire api.
Le lancement de l’api se fait à partir du fichier api/app.py
Pour récupérer l’estimation d’un bien, envoyez une requête à l’url suivant
`http://127.0.0.1:5003/api/estimate/?insee_code=63113&range_km=15&property_type=1&surface=100&ground_surface=500&nb_rooms=5`

**Les paramètres obligatoires pour envoyer la requête**  
insee_code: integer  (correspondance Code postal/Code Insee disponible ![ici][./data/in/correspondance-code-insee-code-postal.csv]
range_km: integer  
property_type: 1 pour maison et 2 pour appartement  
surface: integer
ground_surface: integer
nb_rooms : integer

Vous pouvez utiliser le lien `http://localhost:5003/docs` pour exploiter l'api
