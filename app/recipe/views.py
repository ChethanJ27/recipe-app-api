from recipe.utils import get_or_create_tags,get_or_create_ingredients
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import  Response
from rest_framework.permissions import IsAuthenticated
from recipe.serializers import TagSerializer,IngredientSerializer,RecipeSerializer
from recipe.models import Tag,Ingredient,Recipe
import json,logging
from .utils import CursorModelPagination

# Create your views here.

class TagView(APIView):

    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        if 'tag/delete' in request.path:
            return self.deleteTag(request=request)
        user = self.request.user
        print(user)
        tag = Tag(name=request.POST['name'],user=user)
        tag.save()
        return Response({'msg': tag.name}, status=status.HTTP_200_OK)
    
    def deleteTag(self,request):
        id = request.data["id"]
        Tag.objects.filter(id=id).update(is_deleted=True)
        return Response({'msg':'Successfully deleted'},status=status.HTTP_200_OK)

    def get(self,request):
        tags = Tag.objects.all().filter(is_deleted=False)
        searializer = TagSerializer(tags,many=True)
        return Response({'msg': searializer.data}, status=status.HTTP_200_OK)

    # def get(self,pk):
    #     model = Tag.objects.contains(name=pk)
    #     serializer = TagSerializer(model,many=True)
    #     return Response({'data':serializer.data},status=status.HTTP_200_OK)


class IngredientView(APIView):

    permission_classes = [IsAuthenticated, ]

    def post(self,request):
        if 'ingredient/delete' in request.path:
            return self.deleteIngredient(request=request)
        user = request.user
        model = Ingredient(name=request.POST['name'],user=user)
        model.save()
        return Response({"msg":"object created" ,'data':model.name},status=status.HTTP_200_OK)

    def get(self,request):
        model = Ingredient.objects.all()
        serializer = IngredientSerializer(model,many = True)
        return Response({'data':serializer.data},status=status.HTTP_200_OK)
    
    def deleteIngredient(self,request):
        id = request.data["id"]
        Ingredient.objects.filter(id=id).update(is_deleted=True)
        return Response({"msg":"Successfully deleted"},status=status.HTTP_200_OK)

class RecipeView(APIView):

    permission_classes = [IsAuthenticated, ]
    # pagination_class = CursorSetPagination

    def post(self,request):
        if '/recipe/delete' in request.path:
            return self.deleteRecipe(request=request)
        data = request.data
        data["user"] = request.user
        tags = request.data["tags"]
        ingredients = request.data["ingredients"]
        del data["tags"]
        del data["ingredients"]
        model = Recipe.objects.create(**data)

        tag = get_or_create_tags(tags=tags,user=request.user)
        for t in tag:
            model.tags.set(t)

        ingredient = get_or_create_ingredients(ingredients=ingredients,user=request.user)
        for t in ingredient:
            model.ingredients.set(t)

        return Response({"msg":model.title},status=status.HTTP_200_OK)

    def get(self,request):
        id = self.request.query_params.get('id',0)
        logging.debug(id)
        # query = 'SELECT * from recipe_recipe where id > %s limit 10 ' %id 
        # queryset = Recipe.objects.raw(query)
        paginator = CursorModelPagination()
        queryset = paginator.get_paginated_data(model=Recipe,cursor=id,ordering_param='id',page_size=5)
        serializer = RecipeSerializer(queryset,many=True)
        # 'id' field should be hashed before sending the response 
        return Response({'data':serializer.data,'id':id},status=status.HTTP_200_OK)
    
    def deleteRecipe(self,request):
        id = request.data["id"]
        Recipe.objects.filter(id=id).update(is_deleted=True)
        return Response({"msg":"Successfully deleted"},status=status.HTTP_200_OK)


class SearchRecipe(generics.ListAPIView):
    """return recipes by its recipe name"""
    permission_classes = [IsAuthenticated, ]
    serializer_class = RecipeSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name',None)
        print(name)
        return Recipe.objects.filter(title=name)