@echo off
REM Vérifier si le répertoire de l'environnement virtuel existe
if not exist .env\Scripts\activate.bat (
    python -m venv .env
)

REM Activer l'environnement virtuel
call .\.env\Scripts\activate

REM Installer les dépendances depuis le fichier requirements.txt
pip install -r requirements.txt

REM Naviguer vers le répertoire du projet AbsenceManager
cd AbsenceManager


REM Ouvrir le navigateur Firefox avec l'URL du serveur local
start firefox "http://127.0.0.1:8000/"

REM Démarrer le serveur Django
python manage.py runserver

