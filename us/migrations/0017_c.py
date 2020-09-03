# Generated by Django 3.0.8 on 2020-09-03 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('us', '0016_auto_20200903_1107'),
    ]

    operations = [
        migrations.CreateModel(
            name='c',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Date de création')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Date de la dernière modification')),
                ('content', models.TextField(help_text='Lister les conditions séparées par des virgules(,) exceptée la dernière !', verbose_name="Liste des conditions d'adhésion")),
                ('file', models.FileField(blank=True, upload_to='', verbose_name='Joindre un fichier')),
                ('language', models.CharField(choices=[('en', 'Anglaise'), ('fr', 'Française')], max_length=3, verbose_name='Version de langue')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]