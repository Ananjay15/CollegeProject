# Generated by Django 4.0.6 on 2022-11-08 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate_user', '0013_course_date_course_description_course_image'),
        ('administrator', '0004_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=150)),
                ('date', models.DateField(auto_now_add=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='notice/')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authenticate_user.course')),
            ],
        ),
    ]
