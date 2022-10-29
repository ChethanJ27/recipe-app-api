from user.models import UserModel
from rest_framework import generics

from user.serializers import UserSerializers
# Create your views here.

class CreateUserView(generics.CreateAPIView):
    """create a user in the system"""
    query_set = UserModel.objects.all()
    serializer_class = UserSerializers


class LoginUserView(generics.RetrieveAPIView):
    """check if user details are correct and then create a token and returns the response"""
    print("in Login view")
    queryset = UserModel.objects.all()
    serializer_class = UserSerializers
