# Generated by Django 4.0.6 on 2022-11-08 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0017_alter_applyforjob_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='applyforjob',
            name='application_status',
            field=models.CharField(choices=[('PENDING', 'PENDING'), ('SELECTED', 'SELECTED'), ('REJECTED', 'REJECTED')], default='PENDING', max_length=150),
        ),
    ]
