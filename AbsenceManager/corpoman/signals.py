from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Collaborateur


@receiver(post_save, sender=Collaborateur)
def create_or_update_user_for_collaborateur(sender, instance, created, **kwargs):
    if created:
        user = User.objects.create_user(
            username=instance.nom.capitalize()[0] + "." + instance.prenom.upper(),
            password="Pa123456",
            email=instance.email_professionnel,
            first_name=instance.prenom,
            last_name=instance.nom
        )
        instance.user = user
        instance.save()


@receiver(pre_delete, sender=Collaborateur)
def disable_user_on_collaborateur_delete(sender, instance, **kwargs):
    try:
        user = instance.user
        if user:
            user.is_active = False
            user.save()
    except User.DoesNotExist:
        pass
