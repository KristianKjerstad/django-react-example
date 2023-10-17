<template>
  <div class="container">
    <v-card class="recipeCard" title="Recipe for XX" subtitle="A drink made with ....">
      <div>Ingredients:</div>
      <ol>
        <li>A</li>
        <li>B</li>
      </ol>
      <div>instructions:</div>
      <ol type="1">
        <li>find x</li>
        <li>find y</li>
      </ol>
    </v-card>
  </div>
</template>

<script lang="ts"></script>

<style scoped>
.recipeCard {
  width: 300px;
  height: 300px;
  background-color: rgb(48, 48, 48);
  color: white;
}

.container {
  margin: auto;
  display: flex;
  justify-content: center;
  padding: 20px;
  background-color: #000102;

  height: 100vh;
}
</style>
