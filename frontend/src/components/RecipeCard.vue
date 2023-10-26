<template>
  <v-card class="recipeCard">
    <!-- <v-img src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg" height="200px" cover></v-img> -->

    <v-card-title> {{ recipe.name }} </v-card-title>

    <v-card-subtitle>
      Ingredients:
      <ul class="padding">
        <li v-for="ingredient in recipe.ingredients" :key="ingredient">
          {{ ingredient }}
        </li>
      </ul></v-card-subtitle
    >

    <v-card-actions>
      <v-btn color="orange-darken-2" variant="text" @click="toggleIsOpen()"> Show steps </v-btn>
      <v-spacer></v-spacer>
      <v-btn :icon="isOpen ? 'mdi-chevron-up' : 'mdi-chevron-down'" @click="toggleIsOpen()"></v-btn>
    </v-card-actions>

    <v-expand-transition>
      <div v-show="isOpen">
        <v-divider></v-divider>

        <v-card-text>
          <ol class="padding">
            <li v-for="step in recipe.steps" :key="step">{{ step }}</li>
          </ol>
        </v-card-text>
      </div>
    </v-expand-transition>
  </v-card>
</template>
<script lang="ts">
import { defineComponent } from 'vue'

import type { Ingredient, Recipe } from '../types'

export default defineComponent({
  data() {
    return {
      isOpen: true,
      ingredients: [] as Ingredient[]
    }
  },
  props: {
    recipe: {
      type: Object as () => Recipe,
      required: true
    }
  },
  methods: {
    isNumericString(input: string) {
      return typeof input === 'string' && !Number.isNaN(input)
    },
    toggleIsOpen() {
      console.log('new')
      this.isOpen = !this.isOpen
    }
    // replaceIngredientIdsWithName(recipe: Recipe) {
    //   recipe.ingredients.map((ingredientId) => {
    //     if (this.isNumericString(ingredientId)) {
    //     }
    //   })
    // }
  }
})
</script>

<style>
.recipeCard {
  width: 400px;
  margin: 20px;
}

.padding {
  padding-left: 16px;
}
</style>
