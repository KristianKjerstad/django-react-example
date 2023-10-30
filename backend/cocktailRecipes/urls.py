from django.urls import path

from .views import (
    CocktailRecipeDetail,
    CocktailRecipeIngredientsView,
    CocktailRecipeList,
    get_filtered,
)

urlpatterns = [
    path("", CocktailRecipeList.as_view(), name="recipe_list"),
    path("<int:id>/", CocktailRecipeDetail.as_view(), name="recipe_detail"),
    path("filtered/", get_filtered, name="ingredients"),
    path("ingredients/", CocktailRecipeIngredientsView.as_view(), name="ingredients"),
]
