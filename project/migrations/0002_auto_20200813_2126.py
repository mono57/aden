# Generated by Django 3.0.8 on 2020-08-13 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='filiere',
            field=models.CharField(blank=True, max_length=255, verbose_name='Filière'),
        ),
        migrations.AlterField(
            model_name='project',
            name='owner',
            field=models.CharField(max_length=100, verbose_name='Nom(s) et Prénom(s) du porteur de projet'),
        ),
        migrations.AlterField(
            model_name='project',
            name='school_out_date',
            field=models.DateField(blank=True, verbose_name="Date de sortie de l'ENSAI"),
        ),
    ]
