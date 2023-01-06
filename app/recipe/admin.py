from django.contrib import admin
from .models import Recipe

# Register your models here.
# class FlatPageRecipe(admin.ModelAdmin):
#     fieldsets = (
#         (None, {
#             'fields': ('title', 'description', 'avg_price','tags','ingredients')
#         }),
#     )

admin.site.register(Recipe)