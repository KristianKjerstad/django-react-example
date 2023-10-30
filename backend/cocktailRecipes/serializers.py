from rest_framework import serializers

from . import models


class CocktailRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CocktailRecipe
        fields = ["id", "name", "ingredients", "steps"]
        # depth = 1  - include full ingredient object instead of just not id

    def validate(self, data):
        # ingredients = data.get("ingredients")
        steps = data.get("steps")

        if not (isinstance(steps, list) and all(isinstance(step, str) for step in steps)):
            raise serializers.ValidationError("Steps must be a list of strings")

        return data


class CocktailRecipeIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ingredient
        fields = ["id", "name"]


class ListParameterSerializer(serializers.Serializer):
    """Serializer for list parameters that checks if all values are numbers."""

    values = serializers.ListField(child=serializers.CharField())

    def validate(self, attrs):
        if not all(attr.isnumeric() for attr in attrs["values"][0].split(",")):
            raise serializers.ValidationError("Values must be a list of numbers")
        return super().validate(attrs)
