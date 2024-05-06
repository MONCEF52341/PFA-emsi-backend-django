# Validators permet de créer des critères de validations personnalisés

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_avatar(value):
    # Vérifier si le fichier est une image
    if not value.name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.svg')):
        raise ValidationError(_('Le fichier doit être une image (png, jpg, jpeg, gif ou svg).'))

    # Vérifier la taille du fichier (25 Mo ou moins)
    if value.size > 25 * 1024 * 1024:
        raise ValidationError(_('Le fichier ne doit pas dépasser 25 Mo.'))

    # Ouvrir l'image pour vérifier sa taille
    from PIL import Image
    img = Image.open(value)
    width, height = img.size

    # Vérifier les dimensions de l'image (entre 128x128 et 1080x1080)
    if not (128 <= width <= 1080 and 128 <= height <= 1080):
        raise ValidationError(_('Les dimensions de l\'image doivent être entre 128x128 et 1080x1080 pixels.'))
