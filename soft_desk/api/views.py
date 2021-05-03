from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.decorators import api_view, action
from .serialisers import (
    SerializerUser, 
    SerializerProject,
    SerializerIssue,
    SerializerContributor,
    SerializerComment)
from .pagination import PageLimitOffsetPagination
from .permissions import IsAuthorOrReadOnly, ContributorsOnly, IsProjectAuthorOrReadOnly
from .models import Project, Contributor, Issue, Comment
from django.contrib.auth.models import User


class RegisterView(APIView):
    """
    View de classe permettant à un utilisateur de s'incrire
    """
    
    def post(self, request, format=None):
        serializer = SerializerUser(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['infos'] = "Votre compte a été créer"
            data['email'] = user.email
            data['username'] = user.username
        else:
            data = serializer.errors
        return Response(data=data)


class ProjectView(viewsets.ModelViewSet):
    serializer_class = SerializerProject
    permission_classes = (permissions.IsAuthenticated,IsAuthorOrReadOnly,)
    pagination_class = PageLimitOffsetPagination
    def get_queryset(self):
        return Project.objects.filter(author_user_id=self.request.user)|\
                Project.objects.filter(project_contrib__user_id=self.request.user)


class ContibutorView(viewsets.ModelViewSet):
    serializer_class = SerializerContributor
    permission_classes = (permissions.IsAuthenticated,IsProjectAuthorOrReadOnly,)

    def get_queryset(self):
        id = self.kwargs['project_id']
        return Contributor.objects.filter(project_id=id)


class IssueView(viewsets.ModelViewSet):
    serializer_class = SerializerIssue
    permission_classes = (permissions.IsAuthenticated,ContributorsOnly,)

    def get_queryset(self):
        id = self.kwargs['project_id']
        return Issue.objects.filter(project_id=id).order_by('-created_time')


class CommentView(viewsets.ModelViewSet):
    serializer_class = SerializerComment
    permission_classes = (permissions.IsAuthenticated,ContributorsOnly,)

    def get_queryset(self):
        issue_id = self.kwargs['issue_id']
        return Comment.objects.filter(issue_id=issue_id).order_by('-created_time')