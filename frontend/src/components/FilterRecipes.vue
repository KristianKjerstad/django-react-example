<template>
  <v-select
    label="Select your available ingredients!"
    multiple
    chips
    :items="ingredients"
    :item-props="itemProps"
    variant="outlined"
    v-model="selectedIngredients"
    return-object
  ></v-select>
  <v-btn color="#4d4d4d" outlined @click="$emit('getSelectedIngredients', selectedIngredients)"
    >Search</v-btn
  >
</template>
<script lang="ts">
import { defineComponent } from 'vue'

import type { Ingredient } from '../types'
import { getAllIngredients } from '../api'
import { toRaw } from 'vue'

export default defineComponent({
  data() {
    return {
      inputValue: '',
      isOpen: true,
      ingredients: [] as Ingredient[],
      selectedIngredients: [] as Ingredient[]
    }
  },
  props: {},
  created() {
    getAllIngredients().then((ingredients) => {
      this.ingredients = ingredients
    })
  },
  methods: {
    itemProps(ingredient: Ingredient) {
      return {
        title: ingredient.name
      }
    }
  }
})
</script>

<style></style>
