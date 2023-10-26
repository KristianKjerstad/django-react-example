from django.urls import path

from .views import CocktailRecipeView, get_one

urlpatterns = [
    path("", CocktailRecipeView.as_view(), name="cockatilRecipes"),
    path("<int:id>/", get_one, name="get_one"),
]
