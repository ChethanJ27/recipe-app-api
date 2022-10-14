import email
from multiprocessing.managers import BaseManager
from django.db import models

# Create your models here.
class UserModel(BaseManager):
    name : models.CharField(max_length=50)
    email : models.EmailField()
    password : models.CharField(max_length=50)