from rest_framework import status, views
from rest_framework.decorators import api_view
from rest_framework.response import Response

from cocktailRecipes.models import CocktailRecipe

from .serializers import CocktailRecipeSerializer


class CocktailRecipeView(views.APIView):
    serializer_class = CocktailRecipeSerializer

    # def get_serializer_context(self):
    #     return {"request": self.request, "format": self.format_kwarg, "view": self}

    # def get_serializer(self, *args, **kwargs):
    #     kwargs["context"] = self.get_serializer_context()
    #     return self.serializer_class(*args, **kwargs)

    def get(self, request, id):
        # serializer = self.get_serializer()
        queryset = CocktailRecipe.objects.filter(pk=id)
        serializer = CocktailRecipeSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(http_method_names=["GET"])
def get_all(request):
    queryset = CocktailRecipe.objects.all()
    serializer = CocktailRecipeSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(http_method_names=["GET"])
def get(request, id):
    print("x")
    queryset = CocktailRecipe.objects.filter(pk=id)
    serializer = CocktailRecipeSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
