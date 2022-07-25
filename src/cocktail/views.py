import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from cocktail.models import Cocktail
from cocktail.serializers import CocktailSerializer

# Create your views here.
class CocktailListAPI(APIView):
    serializer_class = CocktailSerializer

    def get(self, request):
        instance = Cocktail.objects.all()
        serializer = self.serializer_class(instance, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        ''' 칵테일 등록 '''
        pass

class CocktailAPI(APIView):
    serializer_class = CocktailSerializer

    def get(self, request, pk):
        instance = Cocktail.objects.get(pk=pk)
        serializer = self.serializer_class(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
