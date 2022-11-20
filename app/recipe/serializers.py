from rest_framework import serializers
from recipe.models import Tag,Ingredient,Recipe

class TagSerializer(serializers.ModelSerializer):
    """ """
    class Meta:
        model = Tag
        exclude = ['user']

class IngredientSerializer(serializers.ModelSerializer):
    """ """
    class Meta:
        model = Ingredient
        fields = ["name"]


class RecipeSerializer(serializers.ModelSerializer):
    """ """

    class Meta:
        model = Recipe
        fields = ["title","description","calories","avg_price","time_to_cook"]