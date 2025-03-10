# Generated by Django 5.0.4 on 2024-04-22 08:02

import corpoman.utils
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corpoman', '0008_collaborateur_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='collaborateur',
            name='matricule',
            field=models.CharField(default=corpoman.utils.generate_matricule, editable=False, max_length=11, unique=True, verbose_name='Matricule'),
        ),
        migrations.AlterField(
            model_name='collaborateur',
            name='user',
            field=models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='collaborateur', to=settings.AUTH_USER_MODEL),
        ),
    ]
