# Generated by Django 5.1.3 on 2024-12-17 08:30

import reservasAPP.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservasAPP', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='cantidad_personas',
            field=models.PositiveIntegerField(validators=[reservasAPP.models.validar_cantidad_personas]),
        ),
    ]