from xml.etree.ElementInclude import include
from django.urls import path
from recipe.views import IngredientViewSet, RecipeViewSet, TagViewSet
from rest_framework import routers

from recipe import views

router = routers.SimpleRouter()
router.register(r'ingredient',IngredientViewSet)
router.register(r'tag',TagViewSet)
router.register(r'recipe',RecipeViewSet)

urlpatterns = router.urls
