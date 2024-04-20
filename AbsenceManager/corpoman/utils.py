#Le fichier utils.py contient des fonctions utilitaires 
#réutilisables dans plusieurs parties de l'application, 
#permettant de garder le code propre en séparant la logique métier de la logique d'accès aux données.
import random
import string

def generate_matricule():
    letters = string.ascii_uppercase
    random_letters = ''.join(random.choice(letters) for i in range(2))
    random_digits = ''.join(random.choice(string.digits) for i in range(8))
    return random_letters + random_digits
