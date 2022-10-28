
from rest_framework import serializers
from user.models import UserModel

class UserSerializers(serializers.ModelSerializer):
    """serializer for user model"""
    class Meta:
        model = UserModel
        fields = ("__all__")
        extra_kwargs = {'password':{ 'write_only':'true', 'min_length':8 }}
