from django.db import models
from django.conf import settings

# Create your models here.

class Project(models.Model):
    """Cette classe permet de creer une table Project avec les champs ci-dessous
    grâce à l'ORM de django"""

    TYPE_CHOICES = (
        ('BE','Back-End'),
        ('Fr','Front-End'),
        ('IOS','IOS'),
        ('An','Android'),
    )

    title = models.CharField('Titre', max_length=128)
    description = models.TextField('Description', max_length=2048, blank=True)
    project_type = models.CharField('Type',max_length=100,choices=TYPE_CHOICES)
    author_user_id = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL,
        related_name='authors')

    def __str__(self):
        """Cette methode permet d'afficher le titre de l'objet Project à la place de l'objet"""
        return self.title
    
    class Meta:
        """Cette classe permet permet de specifier certain comportement
        de la table Project."""
        verbose_name = "Projet"
        verbose_name_plural = "Projets"

class Contributor(models.Model):
    ROLE_CHOICES = (
        ('A', 'Auteur'),
        ('R', 'Responsable'),
        ('C', 'Créateur'),
    )
    PERMISSION_CHOICES = (
        ('C', 'Création'),
        ('R', 'Lecture'),
        ('U', 'Modification'),
        ('D', 'Suppression'),
    )

    user_id = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='contributors')
    
    project_id = models.ForeignKey(
        to=Project,
        on_delete=models.CASCADE,)

    permission = models.CharField(max_length=100,choices=PERMISSION_CHOICES)
    role = models.CharField(max_length=100,choices=ROLE_CHOICES)

    class Meta:
        """Cette classe permet permet de specifier certain comportement
        de la table Contributors"""
        unique_together = ('user_id', 'project_id',)
        verbose_name = "Collaborateur"
        verbose_name_plural = "Collaborateurs"

class Issue(models.Model):
    """Cette classe permet de creer une table Issue avec les champs ci-dessous
    grâce à l'ORM de django"""

    PRIORITY_CHOICES = (
        ('F', 'FAIBLE'),
        ('M', 'MOYENNE'),
        ('E', 'ÉLEVÉE'),
    )
    STATUS_CHOICES = (
        ('AF','À faire'),
        ('EC','En cours'),
        ('T','Terminé'),
    )
    TAG_CHOICES = (
        ('B','BUG'),
        ('A','AMÉLIORATION'),
        ('T','TÂCHE'),
    )

    title = models.CharField('Titre', max_length=128)
    description = models.TextField('Description', max_length=2048, blank=True)
    tag = models.CharField('Balise',max_length=100,choices=TAG_CHOICES)
    priority = models.CharField('Priorité',max_length=100,choices=PRIORITY_CHOICES)
    status = models.CharField('Status',max_length=100,choices=STATUS_CHOICES)
    created_time = models.DateTimeField('Date',auto_now_add=True)

    project_id = models.ForeignKey(
        to=Project,
        on_delete=models.CASCADE, related_name='issues')
    
    author_user_id = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,)

    assigned_user_id = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='assigned',
        default=author_user_id)

    def __str__(self):
        """Cette methode permet d'afficher le titre de l'objet Issue à la place de l'objet"""
        return self.title

    class Meta:
        """Cette classe permet permet de specifier certain comportement
        de la table Issues."""
        verbose_name = "Problème"
        verbose_name_plural = "Problèmes"

class Comment(models.Model):
    """Cette classe permet de creer une table Comments avec les champs ci-dessous
    grâce à l'ORM de django"""

    description = models.TextField('Description', max_length=2048, blank=True)

    author_user_id = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,)

    issue_id = models.ForeignKey(
        to=Issue,
        on_delete=models.CASCADE,
        related_name='comments')

    created_time = models.DateTimeField('Date',auto_now_add=True)
    
    def __str__(self):
        return "Commentaire de {}".format(self.author_user_id.username)

    class Meta:
        """Cette classe permet permet de specifier certain comportement
        de la table Comments."""
        verbose_name = "Commentaire"
        verbose_name_plural = "Commentaires"