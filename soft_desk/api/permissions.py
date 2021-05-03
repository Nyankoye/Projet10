from rest_framework.permissions import BasePermission
from rest_framework import permissions
from .models import Contributor, Project
class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author_user_id == request.user

class IsProjectAuthorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        id = request.resolver_match.kwargs.get('project_id')
        project = Project.objects.get(id=id)
        if request.method in permissions.SAFE_METHODS:
            return True
        elif project.author_user_id == request.user:
            return True
        else:
            return False

class ContributorsOnly(BasePermission):
    def has_permission(self, request, view):
        id = request.resolver_match.kwargs.get('project_id')
        project = Project.objects.get(id=id)
        contributors = project.project_contrib.all()
        if project.author_user_id == request.user:
            return True
        else:
            for contributor in contributors:
                if contributor.user_id == request.user:
                    return True
                return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author_user_id == request.user