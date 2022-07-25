from django.urls import path

from cocktail.views import CocktailAPI, CocktailListAPI


urlpatterns = [
    path('/', CocktailListAPI.as_view()),
    path('/<int:pk>', CocktailAPI.as_view()),
]
