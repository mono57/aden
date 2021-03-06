# Generated by Django 3.0.8 on 2020-09-05 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('us', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalassembly',
            name='file',
            field=models.FileField(upload_to='', verbose_name='Fichier joint'),
        ),
        migrations.AlterField(
            model_name='generalassembly',
            name='version',
            field=models.CharField(choices=[('en', 'Anglaise'), ('fr', 'Française')], max_length=3, verbose_name='Version de langue du fichier'),
        ),
    ]
