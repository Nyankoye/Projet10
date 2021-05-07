# Projet10
Création d'une API sécurisée RESTful en utilisant Django REST
L'API vous permettra de créer divers projets, d'ajouter des utilisateurs à des projets spécifiques, de créer des problèmes au sein des projets et d'attribuer des libellés à ces problèmes en fonction de leurs priorités, de balises, etc.


# Documentation API
Veuillez trouver la documentation de l'api sur le lien suivant [API-REST](https://documenter.getpostman.com/view/14846551/TzRRC8Wm)
# Execution du code
 1. Cloner ce dépôt de code à l'aide de la commande: $ git clone https://github.com/Nyankoye/Projet10.git 
 2. Créez un environnement virtuel dans le projet en utilisant la commande: python -m venv env
 3. Activez l'environnement virtuel en utilisant la commande: source env/Scripts/activate
 4. Installer les paquets Python répertoriés dans le fichier requirements.txt en utilisant la commande : pip install -r requirements.txt
 5. Déplacez-vous  dans le fichier soft_desk en utilisant la commande : cd soft_desk
 6. Charger le contenu de la base de données en utilisant la commande : python manage.py migrate
 7. Lancer le serveur en utilisant la commande : python manage.py runserver
 8. Tapez cette adresse : http://127.0.0.1:8000/ dans votre navigateur pour commencer à utiliser la l'application web