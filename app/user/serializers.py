from dataclasses import fields
from django.contrib.auth import get_user_model

from rest_framework import serializers

class UserSerializers(ModelSerializer):
    """serializer for user model"""

    class Meta:
        model = get_user_model()
        fields = {'email', 'password', 'name'}
        **kwargs = {'password':{ 'write_only':true, min_length:8 }}

    def create(self,validated_data):
        """create new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)