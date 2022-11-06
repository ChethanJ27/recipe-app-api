from user.models import UserModel
from django.contrib.auth import authenticate, login, logout
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import  Response
from .utils import get_tokens_for_user

from user.serializers import UserSerializers
# Create your views here.

class CreateUserView(generics.CreateAPIView):
    """create a user in the system"""
    query_set = UserModel.objects.all()
    serializer_class = UserSerializers


class LoginUserView(APIView):

    def post(self, request):
        if 'email' not in request.data or 'password' not in request.data:
            return Response({'msg': 'Credentials missing'}, status=status.HTTP_400_BAD_REQUEST)
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            auth_data = get_tokens_for_user(request.user)
            return Response({'msg': 'Login Success', **auth_data}, status=status.HTTP_200_OK)
        return Response({'msg': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
