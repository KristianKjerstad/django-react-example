from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from cocktailRecipes import urls as cocktailRecipesUrls

router = routers.DefaultRouter()
# router.register(r"cocktailRecipes", CocktailRecipeView, basename="cocktailRecipes")
urlpatterns = router.urls


urlpatterns += [path("admin/", admin.site.urls), path("cocktailRecipes/", include(cocktailRecipesUrls))]
