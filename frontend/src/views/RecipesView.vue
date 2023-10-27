<template>
  <h1>Recipes</h1>
  <FilterRecipes @getSelectedIngredients="getSelectedIngredients" />
  <div class="recipeCardContainer">
    <div v-for="recipe in recipes" :key="recipe.id">
      <RecipeCard :recipe="recipe" />
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import { getAllRecipes } from '../api'
import type { Ingredient, Recipe } from '../types'
import RecipeCard from '../components/RecipeCard.vue'
import FilterRecipes from '../components/FilterRecipes.vue'

export default defineComponent({
  components: { RecipeCard, FilterRecipes },
  name: 'RecipesView',
  data() {
    return {
      newInput: '',
      recipes: [] as Recipe[]
    }
  },
  created() {
    getAllRecipes().then((recipes) => {
      console.log('recipes', recipes)
      this.recipes = recipes
    })
  },
  methods: {
    getSelectedIngredients(ingredients: Ingredient[]) {
      console.log('getSelectedIngredients', ingredients)
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
