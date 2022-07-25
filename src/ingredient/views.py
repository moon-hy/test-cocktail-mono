from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ingredient.models import Ingredient
from ingredient.serializers import IngredientSerializer

# Create your views here.
class IngredientListAPI(APIView):
    serializer_class = IngredientSerializer

    def get(self, request):
        ''' 재료 리스트 '''
        instance = Ingredient.objects.all()
        serializer = self.serializer_class(instance, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

class IngredientAPI(APIView):
    serializer_class = IngredientSerializer

    def get(self, reqeust, pk):
        ''' 단일 재료 검색 '''
        instance = Ingredient.objects.get(pk=pk)
        serializer = self.serializer_class(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
