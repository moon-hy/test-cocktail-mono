from rest_framework import serializers

from recipe.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    cocktail_name = serializers.CharField(source='cocktail.name')
    ingredient_name = serializers.CharField(source='ingredient.name')
    
    class Meta:
        model = Recipe
        fields = '__all__'
