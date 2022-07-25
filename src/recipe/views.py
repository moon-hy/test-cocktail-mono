from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from recipe.models import Recipe
from cocktail.models import Cocktail
from recipe.serializers import RecipeSerializer


class RecipeAPI(APIView):
    serializer_class = RecipeSerializer

    def get(self, request, cocktail_id):
        recipe = Recipe.objects.filter(cocktail_id=cocktail_id)
        serializer = RecipeSerializer(recipe, many=True)
        return Response(data=serializer.data)

class SearchAPI(APIView):
    ''' get으로 테스트 '''
    serializer_class = RecipeSerializer

    def get(self, request):
        ingredients = set([1, 129, 147])
        recipe = Recipe.objects.raw('''
            SELECT * from COCKTAIL_RECIPE where ingredient in %s
        ''', ingredients)
        serializer = self.serializer_class(recipe, many=True)
        print(recipe)
        return Response(data=serializer.data)
