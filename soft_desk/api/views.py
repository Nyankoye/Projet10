from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serialisers import SerializerUser, SerializerProject
from .models import Project
from django.contrib.auth.models import User
# Create your views here.
@api_view(['POST'])
def register(request):
    if request.method == 'POST':
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

@api_view(['GET','POST'])
def projects_list(request):
    if request.method == 'GET':
        try:
            projects = Project.objects.filter(author_user_id=request.user)
        except Project.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serialiser = SerializerProject(projects, many=True)
        return Response(serialiser.data)
    
    if request.method == 'POST':
        data = request.data
        project = Project.objects.create(title=data['title'],description=data['description'],\
                        project_type=data['project_type'])
        for user in data['author_user_id']:
            user_object = User.objects.filter(username=user['username'])
            project.author_user_id.add(user_object)

        serialiser = SerializerProject(data=project)
        if serialiser.is_valid():
            serialiser.save()
            return Response(serialiser.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

        
