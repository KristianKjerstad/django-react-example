from django.db import models

# Create your models here.
# create a model class for cocktail recipes


class CocktailRecipe(models.Model):
    """Model definition for CocktailRecipe."""

    name = models.CharField("Name", max_length=200)
    ingredients = models.JSONField("Ingredients")
    steps = models.JSONField("Steps")
