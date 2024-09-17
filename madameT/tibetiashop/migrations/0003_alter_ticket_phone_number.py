# Generated by Django 5.0.3 on 2024-08-11 21:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tibetiashop', '0002_alter_ticket_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='phone_number',
            field=models.CharField(max_length=14, unique=True, validators=[django.core.validators.RegexValidator(message='Le numéro de téléphone doit être au format international (ex: +225XXXXXXXX).', regex='^\\+225\\d{10}$')]),
        ),
    ]
