<template>
  <v-layout>
    <div>
      <v-navigation-drawer class="navBar" floating v-model="drawer" permanent>
        <v-list density="compact" nav>
          <v-list-item prepend-icon="mdi-close" @click="drawer = !drawer"></v-list-item>
          <v-list-item
            prepend-icon="mdi-home"
            title="Home"
            value="home"
            @click="$router.push('/')"
          ></v-list-item>
          <v-list-item
            prepend-icon="mdi-view-list"
            title="All recipes"
            value="recipes"
            @click="$router.push('/recipes')"
          ></v-list-item>
          <v-list-item prepend-icon="mdi-plus" title="Add recipe" disabled></v-list-item>
        </v-list>
      </v-navigation-drawer>
    </div>
  </v-layout>
  <v-app-bar-nav-icon variant="text" @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
</template>

<script lang="ts">
export default {
  name: 'NavigationBar',
  data: () => ({
    drawer: false
  })
}
</script>

<style scoped>
.navBar {
  color: white;
  background-color: rgb(48, 48, 48);
}
</style>
