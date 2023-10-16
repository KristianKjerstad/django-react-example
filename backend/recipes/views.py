import json

from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from rest_framework import status

from recipes.models import CocktailRecipe


@method_decorator(csrf_exempt, name="dispatch")
class CocktailRecipesView(TemplateView):
    template_name = "cocktail_recipes"

    def get(self, request):
        """Get all cocktail recipes"""
        data = CocktailRecipe.objects.all()
        return HttpResponse(json.dumps(list(data.values())), status=status.HTTP_200_OK, content_type="application/json")

    def post(self, request):
        """Create a single cocktail recipe"""

        data: CocktailRecipe = CocktailRecipe.objects.create(**json.loads(request.body))
        data.save()
        return HttpResponse("OK", status=status.HTTP_201_CREATED)
