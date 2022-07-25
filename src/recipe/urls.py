from django.urls import path

from recipe.views import RecipeAPI, SearchAPI


urlpatterns = [
    path('/cocktails/<int:cocktail_id>/recipe', RecipeAPI.as_view()),
    path('/availables', SearchAPI.as_view()),
]
