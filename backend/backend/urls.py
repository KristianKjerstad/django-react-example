from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers

from cocktailRecipes import urls as cocktailRecipesUrls

router = routers.DefaultRouter()
# router.register(r"cocktailRecipes", CocktailRecipeView, basename="cocktailRecipes")
urlpatterns = router.urls


urlpatterns += [
    path("admin/", admin.site.urls),
    path("cocktailRecipes/", include(cocktailRecipesUrls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
]
