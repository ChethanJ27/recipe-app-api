from dataclasses import fields
from django.contrib.auth import get_user_model,authenticate
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers
from user.models import UserModel

class UserSerializers(serializers.ModelSerializer):
    """serializer for user model"""
    class Meta:
        model = UserModel
        fields = ('id','name','email','password')
        extra_kwargs = {'password':{ 'write_only':'true', 'min_length':8 }}

    def create(self,validated_data):
        """create new user with encrypted password and return it"""
        print(validated_data)
        print("validated")
        return UserModel.objects.create_user(validated_data)


class AuthenticateSerializer(serializers.Serializer):
    """serializer for authentication object"""
    email = serializers.CharField()
    password = serializers.CharField(
        style = {'input_type':'password'}
    )

    def validate(self,attrs):
        """validate and authenticate user"""
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )
        if not user:
            msg=_('Unable to authenticate with provided creds')
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user']=user
        return attrs
