# Generated by Django 4.2.7 on 2023-11-30 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0006_beststudent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beststudent',
            name='picture',
            field=models.ImageField(upload_to='best_student_pics/'),
        ),
    ]
