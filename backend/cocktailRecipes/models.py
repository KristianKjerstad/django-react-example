from django.db import models

# Create your models here.


class CocktailRecipe(models.Model):
    """Model definition for CocktailRecipe."""

    id = models.AutoField(primary_key=True)
    name = models.CharField("Name", max_length=200)
    ingredients = models.ManyToManyField("Ingredient", related_name="cocktail_recipes")
    steps = models.JSONField("Steps", default=list, blank=False)

    def __str__(self):
        """Unicode representation of CocktailRecipe."""
        return self.name


class Ingredient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("Name", max_length=200)

    def __str__(self):
        """Unicode representation of Ingredient."""
        return self.name
