# Generated by Django 4.0.6 on 2022-10-18 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('human_resource', '0012_alter_traningcategory_options_traningapplication'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='traningapplication',
            options={'verbose_name': 'Traning Application'},
        ),
        migrations.AddField(
            model_name='traningapplication',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]