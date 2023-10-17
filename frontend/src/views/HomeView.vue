<template>
  <h1>Recipe finder</h1>

  <v-text-field
    label="Search for recipes"
    class="searchBox"
    density="compact"
    variant="outlined"
    append-inner-icon="mdi-magnify"
  ></v-text-field>
</template>

<script setup lang="ts">
import NavigationBar from '../components/NavigationBar.vue'
</script>

<style scoped>
.searchBox {
  padding-top: 48px;
  min-width: 300px;
  max-width: 600px;
  display: block;
  margin-left: auto;
  margin-right: auto;
}

h1 {
  text-align: center;
}
</style>
