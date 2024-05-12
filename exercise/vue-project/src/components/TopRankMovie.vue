<template>
  <article>
    <div class="movie-container">
      <iframe
        class="movie-video"
        width="1300"
        height="530"
        src="https://www.youtube.com/embed/pMAPj6WVsT4?autoplay=1&controls=0&loop=1&playlist=pMAPj6WVsT4&mute=1"
        allow="autoplay"
      ></iframe>
    </div>
  </article>
</template>
<script setup></script>
<style scoped>
article {
  width: 100vw;
  height: 100vh;
  background-color: #bd995a;
}
.movie-container {
  display: flex;
  justify-content: center;
}
.movie-video {
  margin-top: 50px;
  border-radius: 20px;
  box-shadow: 10px 10px 15px 5px;
}
</style>
