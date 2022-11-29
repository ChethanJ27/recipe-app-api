
from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
from .tasks import create_task

class UserManager(BaseUserManager):
    """ """
    def create_user(self,email,password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email :
            raise('user must have a email')
        user = self.model(email)
        user.set_password(password)
        user.save(using=self._db)
        create_task.delay(1)
        return user

    def create_superuser(self, email, name, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            name,
        )
        user.set_password(password)
        user.is_admin = True
        user.save(using=self._db)
        return user
        

class UserModel(AbstractBaseUser):

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique= True)
    password = models.CharField(max_length=255)
    is_admin = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self) -> str:
        return self.name+self.email
