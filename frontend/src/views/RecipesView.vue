<template>
  <h1>Recipes</h1>
  <FilterRecipes @getSelectedIngredients="getSelectedIngredients" />
  <div class="recipeCardContainer">
    <div v-if="filteredRecipes.length === 0">
      <div v-for="recipe in recipes" :key="recipe.id">
        <RecipeCard :recipe="recipe" />
      </div>
    </div>
    <div v-if="filteredRecipes.length > 0">
      <div v-for="recipe in filteredRecipes" :key="recipe.id">
        <RecipeCard :recipe="recipe" />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import { getAllRecipes, getFilteredRecipes } from '../api'
import type { Ingredient, Recipe } from '../types'
import RecipeCard from '../components/RecipeCard.vue'
import FilterRecipes from '../components/FilterRecipes.vue'

export default defineComponent({
  components: { RecipeCard, FilterRecipes },
  name: 'RecipesView',
  data() {
    return {
      newInput: '',
      recipes: [] as Recipe[],
      filteredRecipes: [] as Recipe[]
    }
  },
  created() {
    getAllRecipes().then((recipes) => {
      console.log('recipes', recipes)
      this.recipes = recipes
    })
  },
  methods: {
    async getSelectedIngredients(ingredients: Ingredient[]) {
      const filteredRecipesBasedOnIngredients = await getFilteredRecipes(ingredients)
      this.filteredRecipes = filteredRecipesBasedOnIngredients
      console.log('new recipes', filteredRecipesBasedOnIngredients)
    }
  }
})
</script>

<style scoped>
h1 {
  text-align: center;
}

.recipeCardContainer {
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  flex-wrap: wrap;
}
</style>
