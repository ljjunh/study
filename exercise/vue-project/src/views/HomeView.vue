<template>
  <div>
    <TopRankMovie />
  </div>
</template>
<script setup>
import TopRankMovie from "@/components/TopRankMovie.vue";
import { useMovieStore } from "@/stores/movie.js";
const store = useMovieStore();
</script>

<style scoped></style>
