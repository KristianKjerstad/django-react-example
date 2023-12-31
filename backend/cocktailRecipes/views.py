from django.http import JsonResponse
from rest_framework import status, views
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from cocktailRecipes.models import CocktailRecipe, Ingredient

from .serializers import (
    CocktailRecipeIngredientSerializer,
    CocktailRecipeSerializer,
    ListParameterSerializer,
)


class CocktailRecipeDetail(views.APIView):
    serializer_class = CocktailRecipeSerializer
    parser_classes = [JSONParser]

    def get(self, request, id):
        try:
            queryset = CocktailRecipe.objects.get(pk=id)
        except CocktailRecipe.DoesNotExist:
            return Response({"error": "CocktailRecipe does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = CocktailRecipeSerializer(queryset, many=False)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)


class CocktailRecipeList(views.APIView):
    serializer_class = CocktailRecipeSerializer
    parser_classes = [JSONParser]

    def get(self, request):
        """Get all recipes from the database."""
        queryset = CocktailRecipe.objects.all()
        serializer = CocktailRecipeSerializer(queryset, many=True)
        return JsonResponse(
            serializer.data,
            status=status.HTTP_200_OK,
            safe=False,
        )

    def post(self, request):
        """Create a new CocktailRecipe object."""
        serializer = CocktailRecipeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # serializer.validate()

        if CocktailRecipe.objects.filter(name=request.data["name"]).exists():
            raise Exception(f"CocktailRecipe with name {request.data['name']} already exists")
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CocktailRecipeIngredientsView(views.APIView):
    serializer_class = CocktailRecipeIngredientSerializer
    parser_classes = [JSONParser]

    def get(self, request):
        """Get all ingredients from the database."""
        queryset = Ingredient.objects.all()
        serializer = CocktailRecipeIngredientSerializer(queryset, many=True)
        return JsonResponse(
            serializer.data,
            status=status.HTTP_200_OK,
            safe=False,
        )


@api_view(http_method_names=["GET"])
@parser_classes([JSONParser])
def get_filtered(request):
    """Get all recipes that contains all ingredients in the list of ingredients sent in as query parameter,
    as a list of ingredient ids.
    """
    serializer = ListParameterSerializer(data=request.query_params)
    serializer.is_valid(raise_exception=True)
    ingredient_ids_as_strings: list[str] = serializer.data["values"][0].split(",")
    ingredient_ids: list[int] = [int(ingredient_id) for ingredient_id in ingredient_ids_as_strings]
    all_recipes = CocktailRecipe.objects.all()
    filtered_recipes = []
    for recipe in all_recipes:
        recipe_ingredient_ids: list[int] = [
            ingredient["id"]
            for ingredient in CocktailRecipeIngredientSerializer(recipe.ingredients.all(), many=True).data
        ]
        if all(ingredient_id in recipe_ingredient_ids for ingredient_id in ingredient_ids):
            filtered_recipes.append(CocktailRecipeSerializer(recipe).data)

    return JsonResponse(filtered_recipes, status=status.HTTP_200_OK, safe=False)
