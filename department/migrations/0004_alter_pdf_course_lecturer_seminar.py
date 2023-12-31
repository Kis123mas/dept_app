# Generated by Django 4.2.7 on 2023-11-30 13:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('department', '0003_rename_user_pdf_course_lecturer_remove_pdf_bio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdf',
            name='course_lecturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Seminar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=255)),
                ('pdf_file', models.FileField(upload_to='uploaded_pdfs/')),
                ('lecturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
