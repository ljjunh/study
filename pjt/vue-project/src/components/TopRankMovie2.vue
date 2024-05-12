<template>
  <section>
    <div class="movie-container">
      <div>
        <iframe
          class="movie-video"
          width="1300"
          height="530"
          src="https://www.youtube.com/embed/sqCRP9LimsM?autoplay=1&controls=0&loop=1&playlist=sqCRP9LimsM&mute=1"
          allow="autoplay"
        ></iframe>
      </div>
      <div class="content">
        <div class="content-span">
          <span>2.</span>
          <div>
            <i class="bx bxs-star"></i>
            <span class="score">4.3</span>
          </div>
        </div>
        <div class="content-text">
          <h1>혹성탈출: 새로운 시대</h1>
          <div class="gern">
            <span>액션</span>
            <span class="release-date">개봉일 2024.05.08</span>
          </div>
          <p>
            "인류의 시대는 끝났고, 세상의 주인이 바뀌었다! 진화한 유인원과
            퇴화된 인간들이 살아가는 땅. 유인원 리더 '프록시무스'는 완전한
            군림을 위해 인간들을 사냥하며 자신의 제국을 건설한다. 한편, 또 다른
            유인원 '노아'는 우연히 숨겨진 과거의 이야기와 ‘시저’의 가르침을 듣게
            되고, 의문의 한 인간 소녀와 함께 자유를 향한 여정을 시작하게
            되는데…"
          </p>
        </div>
        <div class="poster">
          <img src="@/assets/poster2.jpeg" alt="" />
        </div>
      </div>
    </div>
  </section>
</template>
<script setup></script>
<style scoped>
section {
  width: 100vw;
  height: 100vh;
  background-color: #998679;
  padding-top: 70px;
}
.movie-container {
  display: flex;
  align-items: center;
  flex-direction: column;
}
.movie-video {
  border-radius: 20px;
  box-shadow: 10px 10px 50px 5px black;
}
.movie-container .content {
  color: #fff;
  display: flex;
  margin-bottom: 50px;
  width: 975px;
  height: 300px;
}
.movie-container .content h1 {
  font-size: 48px;
  font-weight: 600;
}

.movie-container .content .content-span {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  font-size: 48px;
  text-align: right;
}
.movie-container .content .content-span .score {
  font-size: 20px;
}
.movie-container .content .content-span i {
  font-size: 25px;
}
.movie-container .content .content-text {
  margin-left: 50px;
  font-size: 17px;
}
.movie-container .content .content-text .gern {
  margin: 20px 0px;
}
.movie-container .content .content-text .gern .release-date {
  margin-left: 10px;
}
.movie-container .content .poster {
  margin-left: 100px;
  margin-right: 100px;
}
.movie-container .content .poster img {
  width: 204px;
  height: 304px;
  border-radius: 5px;
  box-shadow: 0px 5px 50px 5px black;
}
</style>
