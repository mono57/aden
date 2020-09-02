# Generated by Django 3.0.8 on 2020-09-02 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200902_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='contribution',
            field=models.TextField(blank=True, verbose_name='Que pouvez vous apporter comme contribution pour que vos attentes soient comblées?'),
        ),
        migrations.AddField(
            model_name='profile',
            name='degree',
            field=models.CharField(blank=True, max_length=100, verbose_name='Intitulé du Diplome'),
        ),
        migrations.AddField(
            model_name='profile',
            name='entreprise',
            field=models.CharField(blank=True, max_length=100, verbose_name="Nom de l'entreprise qui vous emploi"),
        ),
        migrations.AddField(
            model_name='profile',
            name='in_ensai_year',
            field=models.DateField(blank=True, null=True, verbose_name="Année d'entrée à l'ENSAI"),
        ),
        migrations.AddField(
            model_name='profile',
            name='out_ensai_year',
            field=models.DateField(blank=True, null=True, verbose_name='Année de sortie'),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=20, verbose_name='Numéro de téléphone'),
        ),
        migrations.AddField(
            model_name='profile',
            name='poste',
            field=models.CharField(blank=True, max_length=100, verbose_name='Poste occupé'),
        ),
        migrations.AddField(
            model_name='profile',
            name='region',
            field=models.CharField(blank=True, max_length=50, verbose_name='Région'),
        ),
        migrations.AddField(
            model_name='profile',
            name='situation',
            field=models.CharField(blank=True, max_length=100, verbose_name='Situation actuelle'),
        ),
        migrations.AddField(
            model_name='profile',
            name='waiting',
            field=models.TextField(blank=True, verbose_name='Quelles sont vos attentes du groupe ALUMNI ENSAI?'),
        ),
    ]
