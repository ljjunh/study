<template>
  <section>
    <div class="movie-container">
      <div>
        <div class="movie-wrapper">
          <iframe
            class="movie-video"
            src="https://www.youtube.com/embed/pMAPj6WVsT4?autoplay=1&controls=0&loop=1&playlist=pMAPj6WVsT4&mute=1"
            allow="autoplay"
          ></iframe>
        </div>
      </div>
      <div class="content">
        <div class="content-span">
          <span>1.</span>
          <div class="star-score">
            <i class="bx bxs-star"></i>
            <span class="score">4.3</span>
          </div>
        </div>
        <div class="content-text">
          <h1>범죄도시4</h1>
          <div class="gern">
            <span>액션</span>
            <span class="release-date">개봉일 2024.04.12</span>
          </div>
          <p>
            "신종 마약 사건 3년 뒤, 괴물형사 ‘마석도’(마동석)와 서울 광수대는
            배달앱을 이용한 마약 판매 사건을 수사하던 중 수배 중인 앱 개발자가
            필리핀에서 사망한 사건이 대규모 온라인 불법 도박 조직과 연관되어
            있음을 알아낸다. 필리핀에 거점을 두고 납치, 감금, 폭행, 살인 등으로
            대한민국 온라인 불법 도박 시장을 장악한 특수부대 용병 출신의 빌런
            ‘백창기’(김무열)와 한국에서 더 큰 판을 짜고 있는 IT업계 천재 CEO
            ‘장동철’(이동휘). ‘마석도’는 더 커진 판을 잡기 위해
            ‘장이수’(박지환)에게 뜻밖의 협력을 제안하고 광역수사대는 물론,
            사이버수사대까지 합류해 범죄를 소탕하기 시작하는데… 나쁜 놈 잡는데
            국경도 영역도 제한 없다! 업그레이드 소탕 작전! 거침없이 싹
            쓸어버린다!"
          </p>
        </div>
        <div class="poster">
          <img src="@/assets/poster.jpeg" alt="" />
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
  background-color: #bd995a;
  padding-top: 70px;
}
.movie-container {
  display: flex;
  align-items: center;
  flex-direction: column;
}
.movie-container .movie-video {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  border-radius: 20px;
  object-fit: cover;
  box-shadow: 10px 10px 50px 5px black;
  border-radius: 20px;
  box-shadow: 10px 10px 50px 5px black;
}
.movie-wrapper {
  width: 1115px;
  height: 500px;
  position: relative;
}
.movie-container .content {
  color: #fff;
  display: flex;
  margin-bottom: 50px;
  width: 1200px;
  height: 300px;
}
.movie-container .content h1 {
  font-size: 48px;
  font-weight: 600;
}

.movie-container .content .content-span {
  display: flex;
  flex-direction: column;
  font-size: 48px;
  text-align: right;
}
.movie-container .content .content-span .star-score {
  display: flex;
  flex-direction: column;
  margin-top: 50px;
}
.movie-container .content .content-span .score {
  font-size: 20px;
}
.movie-container .content .content-span i {
  font-size: 25px;
}
.movie-container .content .content-text {
  margin-left: 25px;
  font-size: 17px;
  line-height: 145%;
}
.movie-container .content .content-text .gern {
  margin: 20px 0px;
  margin-left: 10px;
}
.movie-container .content .content-text p {
  margin-left: 10px;
}
.movie-container .content .content-text .gern .release-date {
  margin-left: 10px;
}
.movie-container .content .poster {
  margin-left: 100px;
  margin-right: 100px;
  /* position: absolute;
  top: 580px;
  right: 300px; */
}
.movie-container .content .poster img {
  width: 204px;
  height: 304px;
  border-radius: 5px;
  box-shadow: 0px 5px 50px 5px black;
}
</style>
