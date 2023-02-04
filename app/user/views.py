from user.models import UserModel
from django.contrib.auth import authenticate, login, logout
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import  Response
from rest_framework.permissions import IsAuthenticated
from .utils import get_tokens_for_user,add_token_to_blackList
from .tasks import send_verification_mail

from user.serializers import UserSerializers

# Create your views here.
class CreateUserView(generics.CreateAPIView):
    """create a user in the system"""
    serializer_class = UserSerializers

    def get_queryset(self):
        return UserModel.objects.create_user(**validated_data)

    def create(self, request,*args,**kwargs):
        result = super(CreateUserView, self).create(request, *args, **kwargs)
        send_verification_mail.delay(username=request.data["name"],email=request.data["email"])
        return result
    


class LoginUserView(APIView):

    def post(self, request):
        if 'email' not in request.data or 'password' not in request.data:
            return Response({'msg': 'Credentials missing'}, status=status.HTTP_400_BAD_REQUEST)
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        usr = UserModel.objects.get(email=email)
        if user is not None and not usr.is_deleted:
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
        

class DeleteUserView(APIView):
    permission_classes = [IsAuthenticated,]
        
    def post(self, request):
        refresh_token = request.data['refresh_token']
        id = request.data['id']
        try:
            logout(request)
            add_token_to_blackList(refresh_token)
            usr = UserModel.objects.filter(id=id).update(is_deleted=True)
            # usr = UserModel.objects.filter(id=id).delete()
            if usr is not None:
                return Response({'msg': 'Successfully Deleted user'}, status=status.HTTP_200_OK)
            return Response( status=status.HTTP_404_BAD_REQUEST )
        except Exception as e:
            return Response( status=status.HTTP_400_BAD_REQUEST )
