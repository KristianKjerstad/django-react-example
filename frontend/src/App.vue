<script setup lang="ts">
import { RouterView } from 'vue-router'
</script>

<template>
  <div class="app">
    <div class="appContent">
      <RouterView />
    </div>
  </div>
</template>

<style scoped>
/* import base.css */
@import './assets/base.css';

.app {
  min-height: 100vh;
  color: rgb(216, 216, 216);
  background: #000102;
  padding-top: 12px;
  padding-bottom: 24px;
  padding-left: 18px;
  padding-right: 18px;
  /* max-width: 100%; */
  height: auto;
  background-image: url('assets/background.jpg');
  background-repeat: no-repeat;
  background-position: bottom center;
}

.appContent {
  /* max-width: 1200px; */
}

header {
  line-height: 1.5;
  max-height: 100vh;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>
