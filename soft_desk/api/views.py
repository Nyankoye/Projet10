from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serialisers import SerializerUser

# Create your views here.
@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = SerializerUser(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['succès'] = "Votre compte a été créer"
            data['email'] = user.email
            data['username'] = user.username
        else:
            data = serializer.errors
        return Response(data=data)