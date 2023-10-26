from django.contrib import admin

from cocktailRecipes.models import CocktailRecipe, Ingredient

# Register your models here.
admin.site.register(CocktailRecipe)
admin.site.register(Ingredient)
