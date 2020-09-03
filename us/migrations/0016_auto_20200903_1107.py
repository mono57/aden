# Generated by Django 3.0.8 on 2020-09-03 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('us', '0015_auto_20200903_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actionplan',
            name='file',
            field=models.FileField(upload_to='', verbose_name="Fichier du plan d'action"),
        ),
        migrations.AlterField(
            model_name='actionplan',
            name='title',
            field=models.CharField(blank=True, help_text='Ce champs est facultatif, à defaut le nom du fichier sera utilisé commme Intitulé', max_length=200, verbose_name='Intitulé ou petite description'),
        ),
    ]