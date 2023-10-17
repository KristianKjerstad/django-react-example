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

<script setup lang="ts"></script>

<style scoped>
.searchBox {
  padding-top: 48px;
  min-width: 300px;
  max-width: 600px;
}

h1 {
  color: -webkit-linear-gradient(#eee, #333);
}
</style>
