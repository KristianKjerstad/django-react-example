from rest_framework import serializers

from . import models


class CocktailRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CocktailRecipe
        fields = ["id", "name", "ingredients", "steps"]
