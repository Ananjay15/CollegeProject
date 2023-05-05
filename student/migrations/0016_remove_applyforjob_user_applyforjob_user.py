# Generated by Django 4.0.6 on 2022-11-08 05:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0015_studentqualification_course_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applyforjob',
            name='user',
        ),
        migrations.AddField(
            model_name='applyforjob',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_query_name='user_jobs', to=settings.AUTH_USER_MODEL),
        ),
    ]
