# Generated by Django 3.0.8 on 2020-08-30 23:48

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('us', '0009_auto_20200829_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actionplan',
            name='content',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Texte régit'),
        ),
        migrations.AlterField(
            model_name='actionplan',
            name='file',
            field=models.FileField(blank=True, upload_to='', verbose_name="Fichier du plan d'action"),
        ),
        migrations.AlterField(
            model_name='internalregulation',
            name='content',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Texte régit'),
        ),
        migrations.AlterField(
            model_name='internalregulation',
            name='file',
            field=models.FileField(blank=True, upload_to='', verbose_name='Joindre le fichier'),
        ),
        migrations.AlterField(
            model_name='status',
            name='content',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Texte régit'),
        ),
        migrations.AlterField(
            model_name='status',
            name='file',
            field=models.FileField(blank=True, upload_to='', verbose_name='Joindre le fichier de statut'),
        ),
    ]