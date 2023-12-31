# Generated by Django 4.2.7 on 2023-11-30 17:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('department', '0007_alter_beststudent_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(default='profile2.png', null=True, upload_to='')),
                ('mat_no', models.CharField(blank=True, max_length=200, null=True)),
                ('firstname', models.CharField(blank=True, max_length=200, null=True)),
                ('middlename', models.CharField(blank=True, max_length=200, null=True)),
                ('lastname', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.CharField(blank=True, max_length=200, null=True)),
                ('state', models.CharField(blank=True, max_length=200, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('username', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('twitter_profile', models.CharField(blank=True, max_length=200, null=True)),
                ('facebook_profile', models.CharField(blank=True, max_length=200, null=True)),
                ('instagram_profile', models.CharField(blank=True, max_length=200, null=True)),
                ('level', models.CharField(blank=True, choices=[('100', '100'), ('200', '200'), ('300', '300'), ('400', '400'), ('alumni', 'alumni'), ('lecturer', 'lecturer')], max_length=200, null=True)),
                ('date_created', models.DateTimeField(blank=True, max_length=200, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
