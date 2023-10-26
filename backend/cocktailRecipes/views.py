from django.http import JsonResponse
from rest_framework import status, views
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from cocktailRecipes.models import CocktailRecipe

from .serializers import CocktailRecipeSerializer


class CocktailRecipeView(views.APIView):
    serializer_class = CocktailRecipeSerializer
    parser_classes = [JSONParser]

    def get(self, request):
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


@api_view(http_method_names=["GET"])
def get_one(request, id):
    try:
        queryset = CocktailRecipe.objects.get(pk=id)
    except CocktailRecipe.DoesNotExist:
        return Response({"error": "CocktailRecipe does not exist"}, status=status.HTTP_404_NOT_FOUND)

    serializer = CocktailRecipeSerializer(queryset, many=False)
    return JsonResponse(serializer.data, status=status.HTTP_200_OK)
