# Generated by Django 5.0.4 on 2024-04-21 00:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corpoman', '0006_alter_compteurabsences_id_alter_contrat_date_fin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipe',
            name='responsable',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='corpoman.collaborateur', verbose_name='Manager/Responsable'),
        ),
    ]
