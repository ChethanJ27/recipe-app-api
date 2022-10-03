import imp

from django.shortcuts import render
from app.user import serializers
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from serializers import UserSerializers,AuthenticateSerializer
# Create your views here.

class CreateUserView(generics.CreateApiView):
    """create a user in the system"""
    serializer_class = UserSerializers

class CreateTokenView(ObtainAuthToken):
    """create a new auth token"""
    serializer_class = AuthenticateSerializer
    renderer_class = api_settings.Default_Rendere_Classes