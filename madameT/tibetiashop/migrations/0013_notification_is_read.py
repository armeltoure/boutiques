# Generated by Django 5.0.3 on 2024-09-10 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tibetiashop', '0012_notification_user_alter_notification_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
    ]
