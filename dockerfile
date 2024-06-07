# Utilisez l'image Python 3.9 comme base
FROM python:3.9

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez le fichier requirements.txt dans le conteneur
COPY requirements.txt .

# Installez les dépendances à partir du fichier requirements.txt
RUN pip install -r requirements.txt

# Copiez le code source de votre projet dans le conteneur
COPY . .

# Exposez le port HTTPS 443
EXPOSE 443

# Démarrez le serveur Django
CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:443"]
