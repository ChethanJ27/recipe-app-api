from xml.etree.ElementInclude import include
from django.urls import path
from recipe.views import IngredientView, RecipeView,TagView
from rest_framework import routers

from recipe import views

router = routers.SimpleRouter()

urlpatterns = [
    path("search/",views.SearchRecipe.as_view(),name = "recipeSearch"),
    path("tag/",views.TagView.as_view(),name = "tagView"),
    path("tag/delete",views.TagView.as_view(),name = "tagView"),
    path("ingredient/",views.IngredientView.as_view(),name = "IngredientView"),
    path("recipe/",views.RecipeView.as_view(),name = "RecipeView"),
]

urlpatterns = urlpatterns+router.urls