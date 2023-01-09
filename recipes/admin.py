from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient

class IngredientAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Recipe)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(RecipeIngredient)