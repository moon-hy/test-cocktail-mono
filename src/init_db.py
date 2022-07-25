import csv
from decimal import Decimal
import os

import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()


from ingredient.models import Ingredient, Representation, Category


""" Create Ingredient Objects """
with open('ingredient_v2.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',',)
    next(reader, None)
    categories = set()
    representations = set()
    ingredients = set()

    for row in reader:
        category, representation, ingredient, abv = row
        if category not in categories and not Category.objects.filter(name=category).exists():
            categories.add(category)
        if (category, representation) not in representations and not Representation.objects.filter(name=representation).exists():
            representations.add((category, representation))
        if (representation, ingredient) not in ingredients and not Ingredient.objects.filter(name=ingredient).exists():
            ingredients.add((category, representation, ingredient, abv))

    category_objects = []
    for category in categories:
        category_objects.append(Category(name=category))
    Category.objects.bulk_create(category_objects)

    representation_objects = []
    for category, representation in representations:
        representation_objects.append(Representation(
            category=Category.objects.get(name=category), 
            name=representation))
    Representation.objects.bulk_create(representation_objects)

    ingredient_objects = []
    for _, representation, ingredient, abv in ingredients:
        ingredient_objects.append(Ingredient(
            representation=Representation.objects.get(name=representation),
            name=ingredient,
            alcohol_by_volume=abv,
            created_by=1))
    Ingredient.objects.bulk_create(ingredient_objects)

""" Create Cocktail Objects and Recipe Objects """

from cocktail.models import Cocktail, Tag
from recipe.models import Recipe


def map_split_strip(object):
    return list(map(str.strip, object.split(',')))

with open('cocktail.csv') as csvfile:
    '''
    * volumes
        0: few
        -1: fill up

    name|base|glass|technique|description|detail|ingredients|volumes|units|optionals|garnish
    '''
    reader = csv.reader(csvfile, delimiter=',',)
    next(reader, None)

    cocktails = []
    errors = set()

    for row in reader:
        name, base, glass, technique, description, detail, ingredients, volumes, units, optionals, garnish = row

        cocktail = Cocktail.objects.create(
            name=name,
            base=base,
            # glass=glass,
            # technique=technique,
            description=description,
            detail=detail,
            created_by=1
        )

        total_alcohol = Decimal(0)
        total_volume = Decimal(0.0001)
        recipe = []
        ingredients, volumes, units, optionals = map(map_split_strip, [ingredients, volumes, units, optionals])
        assert len(set(map(len, [ingredients, volumes, units, optionals]))) == 1

        for ingredient, volume, unit, optional in zip(ingredients, volumes, units, optionals):
            try:
                this_ingredient = Ingredient.objects.get(name=ingredient)
                if unit in set(['ml', 'oz', 'fill up']):
                    abv = this_ingredient.alcohol_by_volume

                    total_alcohol += Decimal(volume) * abv if unit != 'fill up' else Decimal(120) * abv
                    total_volume += Decimal(volume) if unit != 'fill up' else Decimal(120)

                recipe.append(Recipe(
                    cocktail=cocktail,
                    ingredient=this_ingredient,
                    volume=volume,
                    unit=unit,
                    optional=optional=='true'
                ))
            except:
                errors.add(ingredient)
        
        Recipe.objects.bulk_create(recipe)
        cocktail.alcohol_by_volume = round(total_alcohol / total_volume, 2)
        cocktail.save()
    print(errors)
