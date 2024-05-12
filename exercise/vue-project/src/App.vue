<template>
  <SideNavBar />
  <TopNavBar />
  <main>
    <RouterView />
  </main>
</template>
<script setup>
import { RouterLink, RouterView } from "vue-router";
import SideNavBar from "@/components/SideNavBar.vue";
import TopNavBar from "./components/TopNavBar.vue";
</script>

<style scoped>
main {
  padding-top: 50px;
  padding-left: 105px;
}
</style>
