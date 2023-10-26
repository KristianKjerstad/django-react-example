from django.urls import path

from .views import CocktailRecipeView

urlpatterns = [
    # path("", get_all, name="get_all"),
    path("", CocktailRecipeView.as_view(), name="cockatilRecipes"),
    # path("<int:id>/", get, name="get_one"),
]
