# Generated by Django 4.0.6 on 2022-09-17 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_alter_applyforjob_options_remove_applyforjob_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='applyforjob',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='applyforjob',
            name='interview_end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='applyforjob',
            name='interview_start_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]