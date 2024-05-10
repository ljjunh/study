<template>
  <div class="container">
    <NavBar />
    <RouterView />
  </div>
</template>
<script setup>
import { RouterLink, RouterView } from "vue-router";
import NavBar from "./components/NavBar.vue";
</script>

<style scoped>
* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
  font-family: "Poppins", sans-serif;
}
.container {
  width: 100%;
  height: 100vh;
  background-color: #0b1010;
  color: #fff;
}
</style>
