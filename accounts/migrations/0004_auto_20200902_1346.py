# Generated by Django 3.0.8 on 2020-09-02 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200826_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='filiere',
            field=models.CharField(default='', max_length=50, verbose_name='Filière'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('male', 'Masculin'), ('female', 'Feminin')], default='', max_length=10, verbose_name='Sexe'),
            preserve_default=False,
        ),
    ]
