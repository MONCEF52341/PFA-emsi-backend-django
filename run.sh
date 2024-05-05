source ./.env/bin/activate
cd AbsenceManager

# Ouvrir le navigateur Firefox avec l'URL du serveur local
firefox "http://127.0.0.1:8000/"

# Démarrer le serveur Django
python manage.py runserver