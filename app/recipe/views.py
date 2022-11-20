from rest_framework import viewsets, generics,status
from rest_framework.views import APIView
from rest_framework.response import  Response
from rest_framework.permissions import IsAuthenticated
from recipe.serializers import TagSerializer,IngredientSerializer,RecipeSerializer
from recipe.models import Tag,Ingredient,Recipe
import json,logging

# Create your views here.

class TagView(APIView):

    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        user = self.request.user
        print(user)
        tag = Tag(name=request.POST['name'],user=user)
        tag.save()
        return Response({'msg': tag.name}, status=status.HTTP_200_OK)

    def get(self,request):
        tags = Tag.objects.all()
        searializer = TagSerializer(tags,many=True)
        return Response({'msg': searializer.data}, status=status.HTTP_200_OK)

    # def get(self,pk):
    #     model = Tag.objects.contains(name=pk)
    #     serializer = TagSerializer(model,many=True)
    #     return Response({'data':serializer.data},status=status.HTTP_200_OK)


class IngredientView(APIView):

    permission_classes = [IsAuthenticated, ]

    def post(self,request):
        user = request.user
        model = Ingredient(name=request.POST['name'],user=user)
        model.save()
        return Response({"msg":"object created" ,'data':model.name},status=status.HTTP_200_OK)

    def get(self,request):
        model = Ingredient.objects.all()
        serializer = IngredientSerializer(model,many = True)
        return Response({'data':serializer.data},status=status.HTTP_200_OK)

class RecipeView(APIView):

    permission_classes = [IsAuthenticated, ]

    def post(self,request):
        d = request.data
        logging.warning(d)
        data = json.loads(d.decode('utf-8'))
        data.user = request.user
        print("data"+json)
        logging.warning("data"+data)
        # model = Recipe(data)
        # print("recipe model"+model)
        # model.save()
        dat = json.dumps(data)
        return Response({"msg":dat},status=status.HTTP_200_OK)


    def get(self,request):
        model = Recipe.objects.all()
        serializer = RecipeSerializer(model,many=True)
        return Response({'data':serializer.data},status=status.HTTP_200_OK)

class SearchRecipe(generics.ListAPIView):
    """return recipes by its recipe name"""
    permission_classes = [IsAuthenticated, ]
    serializer_class = RecipeSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name',None)
        print(name)
        return Recipe.objects.filter(title=name)