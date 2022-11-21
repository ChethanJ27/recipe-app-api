from django.db import models
from user.models import UserModel

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=255,unique=True)
    user = models.ForeignKey(UserModel,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=255,unique=True)
    user = models.ForeignKey(UserModel,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    user = models.ForeignKey(UserModel,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    calories = models.CharField(max_length=50)
    avg_price = models.DecimalField(max_digits=5,decimal_places=2)
    time_to_cook = models.IntegerField()
    ingredients = models.ManyToManyField('Ingredient')
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title

