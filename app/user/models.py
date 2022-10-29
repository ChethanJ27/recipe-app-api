
from django.db import models


class UserModel(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique= True)
    password = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name+self.email
