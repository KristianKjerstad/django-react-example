from django.db import models

# Create your models here.


class CocktailRecipe(models.Model):
    """Model definition for CocktailRecipe."""

    id = models.AutoField(primary_key=True)
    name = models.CharField("Name", max_length=200)
    ingredients = models.JSONField("Ingredients")
    steps = models.JSONField("Steps")

    def __str__(self):
        """Unicode representation of CocktailRecipe."""
        return self.name
