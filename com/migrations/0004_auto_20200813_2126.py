# Generated by Django 3.0.8 on 2020-08-13 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('com', '0003_auto_20200813_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='posts', to='com.PostCategory', verbose_name="Categories d'article"),
        ),
    ]
