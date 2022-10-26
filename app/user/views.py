import imp

from django.shortcuts import render
from rest_framework import generics,viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from user.serializers import UserSerializers,AuthenticateSerializer
# Create your views here.

class CreateUserView(generics.CreateAPIView):
    """create a user in the system"""
    serializer_class = UserSerializers

class CreateTokenView(ObtainAuthToken):
    """create a new auth token"""
    serializer_class = AuthenticateSerializer
    print(api_settings.DEFAULT_AUTHENTICATION_CLASSES)