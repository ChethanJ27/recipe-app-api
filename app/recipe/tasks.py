from __future__ import absolute_import, unicode_literals
from celery import shared_task
from recipe.models import Recipe,Tag,Ingredient
import logging


logger = logging.getLogger("tasks")

@shared_task
def delete_recipes():
    try:
        Recipe.objects.filter(is_deleted=True).delete()
        result = Tag.objects.filter(is_deleted=True).delete()
        logger.info(result)
        Ingredient.objects.filter(is_deleted=True).delete()
    except Exception as e:
        logger.error(e)
