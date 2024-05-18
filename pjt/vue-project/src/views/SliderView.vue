<template>
  <div class="container">
    <vueper-slides
      :touchable="false"
      class="no-shadow"
      :visible-slides="5"
      slide-multiple
      :gap="3"
      :bullets="false"
      :arrows-outside="false"
      :slide-ratio="1 / 5"
      :dragging-distance="200"
      :breakpoints="{ 800: { visibleSlides: 2, slideMultiple: 2 } }"
    >
      <vueper-slide
        v-for="movie in movies"
        :key="movie.id"
        :image="movie.url"
      />
    </vueper-slides>
  </div>
</template>
<script setup>
import { VueperSlides, VueperSlide } from "vueperslides";
import "vueperslides/dist/vueperslides.css";
const movies = [
  {
    id: 0,
    url: "https://image.tmdb.org/t/p/w500/plNOSbqkSuGEK2i15A5btAXtB7t.jpg",
  },
  {
    id: 1,
    url: "https://image.tmdb.org/t/p/w500/1ZNOOMmILNUzVYbzG1j7GYb5bEV.jpg",
  },
  {
    id: 2,
    url: "https://image.tmdb.org/t/p/w500/pmemGuhr450DK8GiTT44mgwWCP7.jpg",
  },
  {
    id: 3,
    url: "https://image.tmdb.org/t/p/w500/9GAOhSzXjXJR4AxYCa2AMzMGPVg.jpg",
  },
  {
    id: 4,
    url: "https://image.tmdb.org/t/p/w500/57g3pHYi3p0JNVO1LkcyYbeMDBf.jpg",
  },
  {
    id: 5,
    url: "https://image.tmdb.org/t/p/w500/jwswXltzpGaKZCtz1CiDjXHQYAs.jpg",
  },
  {
    id: 6,
    url: "https://image.tmdb.org/t/p/w500/ynyN9hdxL5vq7GnSX8Fdz3TfoTE.jpg",
  },
  {
    id: 7,
    url: "https://image.tmdb.org/t/p/w500/2JO8X8aT97BwxMMGr9ChrCl4xGQ.jpg",
  },
  {
    id: 8,
    url: "https://image.tmdb.org/t/p/w500/tE6tvHXlAZ8hqM4k9ZvtWtBk4pc.jpg",
  },
  {
    id: 9,
    url: "https://image.tmdb.org/t/p/w500/qApkjVJzZ2nkFUcFhcYkTBaRnNj.jpg",
  },
  {
    id: 10,
    url: "https://image.tmdb.org/t/p/w500/vpo99XjnIdkM9QDlQRTj5XEuUOH.jpg",
  },
  {
    id: 11,
    url: "https://image.tmdb.org/t/p/w500/zTgjeblxSLSvomt6F6UYtpiD4n7.jpg",
  },
  {
    id: 12,
    url: "https://image.tmdb.org/t/p/w500/dB7jNL5I3hb7b1zsGD5OEoSl2BQ.jpg",
  },
];
</script>

<style scoped></style>
