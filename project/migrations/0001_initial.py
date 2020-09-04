# Generated by Django 3.0.8 on 2020-09-04 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IndustrialProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Date de création')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Date de la dernière modification')),
                ('content', models.TextField(verbose_name='Texte')),
                ('file', models.FileField(upload_to='', verbose_name='Fichier joint')),
            ],
            options={
                'verbose_name': 'Projet industriel',
                'verbose_name_plural': 'Projets industriels',
            },
        ),
        migrations.CreateModel(
            name='InstitutionalProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Date de création')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Date de la dernière modification')),
                ('content', models.TextField(verbose_name='Texte')),
                ('file', models.FileField(upload_to='', verbose_name='Fichier joint')),
            ],
            options={
                'verbose_name': 'Projet institutionel',
                'verbose_name_plural': 'Projets institutionels',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Date de création')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Date de la dernière modification')),
                ('owner', models.CharField(max_length=100, verbose_name='Nom(s) et Prénom(s) du porteur de projet')),
                ('filiere', models.CharField(blank=True, max_length=255, verbose_name='Filière')),
                ('school_out_date', models.DateField(blank=True, verbose_name="Date de sortie de l'ENSAI")),
                ('name', models.CharField(max_length=255, verbose_name='Désignation du projet')),
                ('description', models.TextField(verbose_name='Résumé du projet')),
                ('estimatif_cost', models.CharField(help_text='Coût en FCFA', max_length=250, verbose_name='Coût estimatif')),
                ('federation', models.TextField(verbose_name="Particularité en terme de fédération des filères de l'ENSAI")),
                ('selected', models.BooleanField(verbose_name='Souhaitez vous participer à toutes             les phases de mise en oeuvre de ce projet si jamais il est retenu ?')),
            ],
            options={
                'verbose_name': 'Idées de projet fédérateurs des filières ENSAI',
            },
        ),
    ]
