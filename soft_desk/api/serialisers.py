from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Project, Issue, Comment, Contributor


class SerializerUser(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password','password2']
        extra_kwargs ={
            'password':{'write_only':True},
        }
    
    def save(self):
        user = User(
            username = self.validated_data['username'],
            email = self.validated_data['email'],
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password':'les mots de passe doivent correspondre'})
        user.set_password(password)
        user.save()
        return user


class SerializerProject(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id','title','description','author_user_id',]


class SerializerIssue(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = '__all__'

class SerializerContributor(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = '__all__'

class SerializerComment(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'