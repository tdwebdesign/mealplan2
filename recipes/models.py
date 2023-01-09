from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    directions = models.TextField()


class Ingredient(models.Model):
    name = models.CharField(max_length=255)


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=1.00)
    measure = models.TextField(max_length=255)


