from enum import unique
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

# Create your models here.
class UserManager(BaseUserManager):

    def create_user(self,email,password=None,**extra_fields):
        user = self.model(email=self.normalize_email(email),**extra_fields)
        user.set_password(password)

        user.save()
        return user


class UserModel(AbstractBaseUser,PermissionsMixin):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)

    objects = UserManager()

    USERNAME_FIELD = 'id'