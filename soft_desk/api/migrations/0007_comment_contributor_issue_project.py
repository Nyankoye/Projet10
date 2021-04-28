# Generated by Django 3.2 on 2021-04-27 08:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0006_auto_20210427_1020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Titre')),
                ('description', models.TextField(blank=True, max_length=2048, verbose_name='Description')),
                ('project_type', models.CharField(choices=[('Back-End', 'Back-End'), ('Front-End', 'Front-End'), ('IOS', 'IOS'), ('Android', 'Android')], max_length=100, verbose_name='Type')),
                ('author_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authors', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Projet',
                'verbose_name_plural': 'Projets',
            },
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Titre')),
                ('description', models.TextField(blank=True, max_length=2048, verbose_name='Description')),
                ('tag', models.CharField(choices=[('BUG', 'BUG'), ('AMÉLIORATION', 'AMÉLIORATION'), ('TÂCHE', 'TÂCHE')], max_length=100, verbose_name='Balise')),
                ('priority', models.CharField(choices=[('FAIBLE', 'FAIBLE'), ('MOYENNE', 'MOYENNE'), ('ÉLEVÉE', 'ÉLEVÉE')], max_length=100, verbose_name='Priorité')),
                ('status', models.CharField(choices=[('À faire', 'À faire'), ('En cours', 'En cours'), ('Terminé', 'Terminé')], max_length=100, verbose_name='Status')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('assigned_user_id', models.ForeignKey(default=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL), on_delete=django.db.models.deletion.CASCADE, related_name='assigned', to=settings.AUTH_USER_MODEL)),
                ('author_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issues', to='api.project')),
            ],
            options={
                'verbose_name': 'Problème',
                'verbose_name_plural': 'Problèmes',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=2048, verbose_name='Description')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('author_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('issue_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='api.issue')),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='api.project')),
            ],
            options={
                'verbose_name': 'Commentaire',
                'verbose_name_plural': 'Commentaires',
            },
        ),
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(blank=True, choices=[('Auteur', 'Auteur'), ('Responsable', 'Responsable'), ('Créateur', 'Créateur')], max_length=100, null=True)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_contrib', to='api.project')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contributors', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Collaborateur',
                'verbose_name_plural': 'Collaborateurs',
                'unique_together': {('user_id', 'project_id')},
            },
        ),
    ]