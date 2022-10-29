from rest_framework import serializers
from recipe.models import Tag,Ingredient,Recipe

class TagSerializer(serializers.ModelSerializer):
    """ """
    class Meta:
        model = Tag
        fields = ["name","user"]


class IngredientSerializer(serializers.ModelSerializer):
    """ """
    class Meta:
        model = Ingredient
        fields = ["name","user"]


class RecipeSerializer(serializers.ModelSerializer):
    """ """

    class Meta:
        model = Recipe
        fields = ["user","title","description","calories","avgPrice","timeToCook","ingredients","tags"]