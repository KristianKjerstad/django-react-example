from django.test import TestCase

from cocktailRecipes.models import CocktailRecipe, Ingredient
from cocktailRecipes.serializers import CocktailRecipeSerializer


class CocktailRecipeTestCase(TestCase):
    example_recipe: CocktailRecipe

    def setUp(self):
        rum = Ingredient.objects.create(name="Rum")
        lime = Ingredient.objects.create(name="Lime")
        sugar = Ingredient.objects.create(name="Sugar")

        recipe1 = CocktailRecipe.objects.create(name="Test CocktailRecipe 1", steps=["d", "e", "f"])
        recipe2 = CocktailRecipe.objects.create(name="Test CocktailRecipe 2", steps=["a", "b", "c"])
        self.example_recipe = recipe2
        recipe1.ingredients.set([rum])
        recipe2.ingredients.set([lime, sugar, rum])

    def test_get_all_recipes(self):
        self.assertEqual(CocktailRecipe.objects.count(), 2)
        response = self.client.get("/cocktailRecipes/")
        self.assertEqual(response.status_code, 200)
        recipes = CocktailRecipe.objects.all()
        serializer = CocktailRecipeSerializer(recipes, many=True)
        self.assertEqual(response.json(), serializer.data)

    def test_single_recipe(self):
        recipe = CocktailRecipe.objects.filter().first()
        serializer = CocktailRecipeSerializer(recipe, many=False)
        # self.example_recipe.id
        response = self.client.get(f"/cocktailRecipes/{serializer.data['id']}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), serializer.data)

    def test_get_filtered_recipes(self):
        ID = 2
        # ingredients = Ingredient.objects.filter(id=ID)

        # serializer = CocktailRecipeIngredientSerializer(ingredients, many=False)
        response = self.client.get(f"/cocktailRecipes/filtered/?values={ID}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [CocktailRecipeSerializer(self.example_recipe).data])

    def test_create_recipe(self):
        new_recipe = {
            "name": "x",
            "ingredients": ["1", "2"],
            "steps": [
                "Blend rum, coconut cream, and pineapple juice with ice",
                "Pour into a chilled glass",
                "Garnish with a slice of pineapple and a cherry",
            ],
        }
        request = self.client.post("/cocktailRecipes/", data=new_recipe, content_type="application/json")
        self.assertEqual(request.status_code, 201)
        resulting_id = request.data["id"]
        self.assertEqual(CocktailRecipe.objects.filter(id=resulting_id).exists(), True)
