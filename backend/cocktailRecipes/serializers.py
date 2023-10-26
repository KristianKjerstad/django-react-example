from rest_framework import serializers

from . import models


class CocktailRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CocktailRecipe
        fields = ["id", "name", "ingredients", "steps"]

    # def validate(self):
    #     """Validate data."""
    #     if not (
    #         isinstance(self.data["name"], CharField)
    #         and isinstance(self.data["ingredients"], JSONField)
    #         and isinstance(self.data["steps"], JSONField)
    #     ):
    #         raise serializers.ValidationError("Invalid data type for CocktailRecipe object")
