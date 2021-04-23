from django.contrib import admin
from .models import Comment, Contributor, Project, Issue

# Register your models here.
@admin.register(Issue)
class adminIssue(admin.ModelAdmin):
    pass

@admin.register(Project)
class adminProject(admin.ModelAdmin):
    pass

@admin.register(Contributor)
class adminContributor(admin.ModelAdmin):
    pass

@admin.register(Comment)
class adminComment(admin.ModelAdmin):
    pass