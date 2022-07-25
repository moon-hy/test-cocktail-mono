from django.contrib import admin

from ingredient.models import Category, Ingredient, Representation

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(Representation)
admin.site.register(Category)