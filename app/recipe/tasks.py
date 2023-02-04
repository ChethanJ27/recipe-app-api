from __future__ import absolute_import, unicode_literals
from celery import shared_task
from recipe.models import Recipe,Tag,Ingredient


@shared_task
def clean_up_deleted_data():
    Recipe.objects.filter(is_Deleted=True).delete()
    Tag.objects.filter(is_Deleted=True).delete()
    Ingredient.objects.filter(is_Deleted=True).delete()
