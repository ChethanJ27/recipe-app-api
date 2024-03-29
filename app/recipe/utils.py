import logging
from recipe.models import Tag
from recipe.models import Recipe
from recipe.models import Ingredient

class CursorModelPagination():

    def get_paginated_data(self,model,cursor,ordering_param,page_size):
        results = model.objects.filter(id__gt=cursor).order_by(ordering_param)[:page_size]
        return results

def get_or_create_ingredients(ingredients,user):
    newingredients = []
    for ingredient in ingredients:
        val = Ingredient.objects.filter(name=ingredient)
        if not val:
            model = Ingredient(name=ingredient,user=user)
            model.save()
            val = Ingredient.objects.filter(name=ingredient)
            newingredients.append(val)
        else:
            newingredients.append(val)
    logging.debug(newingredients)
    return newingredients


def get_or_create_tags(tags,user):
    newtags = []
    for tag in tags:
        val = Tag.objects.filter(name=tag)
        if not val:
            model = Tag(name=tag,user=user)
            model.save()
            val = Tag.objects.filter(name=tag)
            newtags.append(val)
        else:
            newtags.append(val)
    logging.debug(newtags)
    return newtags