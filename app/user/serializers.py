
from rest_framework import serializers
from user.models import UserModel

class UserSerializers(serializers.ModelSerializer):
    """serializer for user model"""
    class Meta:
        model = UserModel
        fields = ("__all__")
        extra_kwargs = {'password':{ 'write_only':'true', 'min_length':8 }}

    def save(self):
        user = UserModel(email=self.validated_data['email'])
        password = self.validated_data['password']
        # password2 = self.validated_data['password2']
        # if password != password2:
        #     raise serializers.ValidationError({'password': 'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user
