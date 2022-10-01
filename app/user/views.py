from rest_framework import generics

from serializers import UserSerializers
# Create your views here.

class CreateUserView(generics.CreateApiView):
    """create a user in the system"""
    serializer_class = UserSerializers