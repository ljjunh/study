import { ref, computed } from "vue";
import { defineStore } from "pinia";

export const useMovieStore = defineStore("movie", () => {
  const YOUTUBE_API_KEY = import.meta.env.VITE_YOUTUBE_API_KEY;
  return { YOUTUBE_API_KEY };
});
