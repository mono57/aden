# Generated by Django 3.0.8 on 2020-09-04 10:43

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Date de création')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Date de la dernière modification')),
                ('question', models.CharField(max_length=200, verbose_name='Question')),
                ('response', models.TextField(verbose_name='Reponse')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Galery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Date de création')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Date de la dernière modification')),
                ('name', models.CharField(max_length=250, verbose_name="Nom de l'album")),
                ('slug', models.SlugField(blank=True)),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('is_visible', models.BooleanField(default=True, verbose_name='Visible sur le site ?')),
                ('creator', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Album',
                'verbose_name_plural': 'Albums',
            },
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Date de création')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Date de la dernière modification')),
                ('name', models.CharField(max_length=100, verbose_name='Nom')),
                ('slug', models.SlugField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RevueInterface',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Date de création')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Date de la dernière modification')),
                ('subject', models.TextField(verbose_name='Sujet')),
                ('file', models.FileField(upload_to='', verbose_name='Joindre un fichier')),
            ],
            options={
                'verbose_name': 'Revue interface',
                'verbose_name_plural': 'Revues interfaces',
            },
        ),
        migrations.CreateModel(
            name='StrategicComity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Date de création')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Date de la dernière modification')),
                ('object', models.CharField(max_length=100, verbose_name='Objet')),
                ('content', models.TextField(verbose_name='Message')),
                ('file', models.FileField(blank=True, upload_to='', verbose_name='Fichier joint')),
            ],
            options={
                'verbose_name': 'Communiqué Comité Stratégique',
                'verbose_name_plural': 'Communiqué(s) Comité Stratégique',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Date de création')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Date de la dernière modification')),
                ('title', models.CharField(max_length=255, verbose_name="Titre de l'article")),
                ('slug', models.SlugField(blank=True)),
                ('content', models.TextField(verbose_name="Contenu de l'article")),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='Image de couverture')),
                ('is_visible', models.BooleanField(default=True, verbose_name='Visible sur le site ?')),
                ('category', models.ManyToManyField(blank=True, related_name='posts', to='com.PostCategory', verbose_name="Categories d'article")),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Article de blog',
                'verbose_name_plural': 'Articles de blog',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Date de création')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Date de la dernière modification')),
                ('title', models.CharField(max_length=255, verbose_name="Titre de l'actualité")),
                ('slug', models.SlugField(blank=True)),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='Image de couverture')),
                ('content', models.TextField(verbose_name="Contenu de l'article")),
                ('is_visible', models.BooleanField(default=True, verbose_name='Visible sur le site ?')),
                ('category', models.ManyToManyField(blank=True, related_name='news', to='com.PostCategory')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Actualité',
                'verbose_name_plural': 'Actualités',
            },
        ),
        migrations.CreateModel(
            name='GaleryImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Date de création')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Date de la dernière modification')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('galery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='com.Galery', verbose_name='Album')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Date de création')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Date de la dernière modification')),
                ('title', models.CharField(max_length=100, verbose_name='Titre')),
                ('slug', models.SlugField(blank=True)),
                ('start_date', models.DateField(blank=True, verbose_name='Date de debut')),
                ('end_date', models.DateField(blank=True, verbose_name='Date de fin')),
                ('start_time', models.TimeField(blank=True, verbose_name='Heure de debut')),
                ('end_time', models.TimeField(blank=True, verbose_name='Heure de Fin')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('location', models.CharField(blank=True, max_length=50, verbose_name='Lieu')),
                ('location_city', models.CharField(default='Yaoundé', max_length=50, verbose_name='Ville')),
                ('expired', models.BooleanField(default=False, verbose_name='Expiré')),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Image de couverture')),
                ('published', models.BooleanField(default=True, verbose_name='Publier')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to=settings.AUTH_USER_MODEL)),
                ('galery', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='com.Galery', verbose_name='Joindre un album photos')),
                ('registration', models.ManyToManyField(blank=True, related_name='register_events', to=settings.AUTH_USER_MODEL, verbose_name='Inscris')),
            ],
            options={
                'verbose_name': 'Agenda',
                'verbose_name_plural': 'Agendas',
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Date de création')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Date de la dernière modification')),
                ('title', models.CharField(blank=True, max_length=100, verbose_name='Nom du document')),
                ('file', models.FileField(upload_to='documents/', verbose_name='Fichier')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Propriétaire')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
