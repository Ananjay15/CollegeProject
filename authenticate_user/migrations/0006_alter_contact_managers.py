# Generated by Django 4.0.6 on 2022-09-18 06:19

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate_user', '0005_contact'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='contact',
            managers=[
                ('contact', django.db.models.manager.Manager()),
            ],
        ),
    ]
