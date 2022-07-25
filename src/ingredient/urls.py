from django.urls import path

from ingredient.views import IngredientAPI, IngredientListAPI


urlpatterns = [
    path('/', IngredientListAPI.as_view()),
    path('/<int:pk>', IngredientAPI.as_view()),
]
