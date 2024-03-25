# Vérifier si le répertoire de l'environnement virtuel existe
if [ ! -d ".env" ]; then
    # Créer un environnement virtuel Python
    python -m venv .env
fi

# Activer l'environnement virtuel
source ./.env/bin/activate

# Installer les dépendances depuis le fichier requirements.txt
pip -r install requirements.txt

# Naviguer vers le répertoire du projet AbsenceManager
cd AbsenceManager

# Ouvrir le navigateur Firefox avec l'URL du serveur local
firefox "http://127.0.0.1:8000/"

# Démarrer le serveur Django
python manage.py runserver