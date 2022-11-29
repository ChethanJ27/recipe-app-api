from user.models import UserModel
from django.contrib.auth import authenticate, login, logout
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import  Response
from rest_framework.permissions import IsAuthenticated
from .utils import get_tokens_for_user,add_token_to_blackList
from .tasks import create_task,debug_task

from user.serializers import UserSerializers

# Create your views here.
class CreateUserView(generics.CreateAPIView):
    """create a user in the system"""
    serializer_class = UserSerializers

    def get_queryset(self):
        return UserModel.objects.create_user(**validated_data)

    def create(self, request,*args,**kwargs):
        result = super(CreateUserView, self).create(request, *args, **kwargs)
        create_task.delay(1)
        return result
    


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


class LogoutUserView(APIView):
    permission_classes = [IsAuthenticated,]

    def post(self,request):
        refresh_token = request.data['refresh_token']
        try:
            logout(request)
            add_token_to_blackList(refresh_token)
            return Response({'msg': 'Successfully Logged out'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response( status=status.HTTP_400_BAD_REQUEST )
