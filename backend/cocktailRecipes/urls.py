from django.urls import path

from .views import (
    CocktailRecipeIngredientsView,
    CocktailRecipeView,
    get_filtered,
    get_one,
)

urlpatterns = [
    path("", CocktailRecipeView.as_view(), name="cockatilRecipes"),
    path("<int:id>/", get_one, name="get_one"),
    path("filtered/", get_filtered, name="filtered_recipes"),
    path("ingredients/", CocktailRecipeIngredientsView.as_view(), name="ingredients"),
]
