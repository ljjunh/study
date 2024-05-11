<template>
  <div class="container">
    <SideNavBar />
    <TopNavBar />
    <RouterView />
  </div>
</template>
<script setup>
import { RouterLink, RouterView } from "vue-router";
import SideNavBar from "@/components/SideNavBar.vue";
import TopNavBar from "./components/TopNavBar.vue";
</script>

<style scoped>
.container {
  display: flex;
  height: 100vh;
  width: 100vw;
}
</style>
