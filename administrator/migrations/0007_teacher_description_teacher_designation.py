# Generated by Django 4.0.6 on 2022-11-13 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0006_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='designation',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
