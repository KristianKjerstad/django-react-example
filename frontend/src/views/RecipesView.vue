<template>
  <h1>Recipes</h1>

  <div v-for="recipe in recipes" :key="recipe.id">{{ recipe.name }}</div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import { getAllRecipes } from '../api'
import type { Recipe } from '../types'

export default defineComponent({
  name: 'RecipesView',
  data() {
    return {
      recipes: [] as Recipe[]
    }
  },
  created() {
    getAllRecipes().then((recipes) => {
      console.log('recipes', recipes)
      this.recipes = recipes
    })
  },
  methods: {}
})
</script>

<style scoped>
h1 {
  text-align: center;
}
</style>
