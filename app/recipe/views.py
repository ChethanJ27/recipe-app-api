from rest_framework import viewsets

from recipe.serializers import TagSerializer,IngredientSerializer,RecipeSerializer
from recipe.models import Tag,Ingredient,Recipe

# Create your views here.

class TagViewSet(viewsets.ModelViewSet):

    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class IngredientViewSet(viewsets.ModelViewSet):

    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()


class RecipeViewSet(viewsets.ModelViewSet):

    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()