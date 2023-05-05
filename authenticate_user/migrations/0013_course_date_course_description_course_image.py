# Generated by Django 4.0.6 on 2022-10-11 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate_user', '0012_course_user_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='course/'),
        ),
    ]