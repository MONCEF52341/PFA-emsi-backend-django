#L'objectif du fichier signal est de créer automatiquement un compte utilisateur dès qu'un 
#collaborateur est créé, ou dès que ses informations de profil utilisateur (telles que le nom, le prénom ou l'e-mail) sont modifiées.

import secrets
import string
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Collaborateur


def generate_password():
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for i in range(8))


@receiver(post_save, sender=Collaborateur)
def create_user_for_collaborateur(sender, instance, created, **kwargs):
    if created:
        user = User.objects.create_user(
            username=instance.prenom.lower() + instance.nom.lower(),
            password=generate_password(),
            email=instance.email_personnel, 
            first_name=instance.prenom,
            last_name=instance.nom
        )

@receiver(post_save, sender=Collaborateur)
def update_user_for_collaborateur(sender, instance, created, **kwargs):
    if not created:
        user = instance.user
        user.username = instance.prenom.lower() + instance.nom.lower()
        user.email = instance.email_personnel
        user.first_name = instance.prenom
        user.last_name = instance.nom
        user.save()

