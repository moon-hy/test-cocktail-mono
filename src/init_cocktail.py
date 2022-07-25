import csv
import os

import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()


""" Create Cocktail Objects and Recipe Objects """
from ingredient.models import Ingredient
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
    
    for row in reader:
        print(row)
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

        total_alcohol = 0
        total_volume = 0.0001
        errors = []
        recipe = []
        ingredients, volumes, units, optionals = map(map_split_strip, [ingredients, volumes, units, optionals])
        print(ingredients,volumes,units,optionals)
        assert len(set(map(len, [ingredients, volumes, units, optionals]))) == 1

        for ingredient, volume, unit, optional in zip(ingredients, volumes, units, optionals):
            try:
                this_ingredient = Ingredient.objects.get(name=ingredient)
                abv = this_ingredient.alcohol_by_volume
                
                total_alcohol += volume * abv
                total_volume += volume
                recipe.append(Recipe(
                    cocktail=cocktail,
                    ingredient=Ingredient.objects.get(name=ingredient),
                    volume=volume,
                    unit=unit,
                    optional=optional
                ))
            except:
                errors.append(ingredient)
                # print(ingredient)
        
        Recipe.objects.bulk_create(recipe)
        cocktail.alcohol_by_volume = round(total_alcohol / total_volume, 2)
        cocktail.save()
