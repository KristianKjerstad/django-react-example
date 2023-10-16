# file for urls for recipes app

from django.urls import path

from recipes.views import CocktailRecipesView

urlpatterns = [
    path("", CocktailRecipesView.as_view(), name="cocktail_recipes"),
]
