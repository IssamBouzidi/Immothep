# Immothep
## Introduction
Module d'estimation de biens basé sur l'intelligence artificielle en Python

## Pré-requis
veuillez installer les modules dans le fichier requirements.txt `conda install --yes --file requirements.txt`  

## Livrables  
Trois Notebooks, un Notebbok pour le traitements et le nettoyage des données(src/immothep.ipynb) et deux Notebooks pour la génération des estimations(src/appartement_train.ipynb) et (src/maison_train.ipynb)  
Une api Fast API pour l'exposition du service d'estimation  

## Procédure à suivre pour générer les modèles d'estimation  
1. **Traitement et nettoyage des données**   
Le notebook immothep.ipynb est le premier notebook à executer afin de préparer les données qui vont être utilisées poure la generation de l'estimation  

2. **Génération des modèles de prédiction des prix de vente**  
Deux notebooks ont été mis en place un pour estimer les valeurs des appartements `src/appartement_train.ipynb` et un autre pour estimer les valeurs des maisons `src/maison_train.ipynb`  

## Exploitation de l’api  
Le lancement de l’api se fait à partir du fichier api/app.py
Pour récupérer l’estimation d’un bien, envoyez une requête à l’url suivant
`http://localhost:5003/api/estimate/?metre_carre=50&nb_pieces=3&terrain=50&code_postal=63`


**Les parametres obligatoires pour envoyer la requête**  
metre_carre: valeur numérique  
nb_pieces: valeur numérique  
terrain: valeur numérique  
code_postal: valeur numérique
type_bien: valeur entier (0 pour appartement et 1 pour maison)  

Vous pouvez utiliser le lien `http://localhost:5003/docs` pour exploiter l'api
