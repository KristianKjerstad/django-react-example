from rest_framework import serializers

from . import models


class CocktailRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CocktailRecipe
        fields = ["id", "name", "ingredients", "steps"]

    def validate(self, data):
        ingredients = data.get("ingredients")
        steps = data.get("steps")

        if not (isinstance(ingredients, list) and all(isinstance(ingredient, str) for ingredient in ingredients)):
            raise serializers.ValidationError("Ingredients must be a list of strings")

        if not (isinstance(steps, list) and all(isinstance(step, str) for step in steps)):
            raise serializers.ValidationError("Steps must be a list of strings")

        return data
