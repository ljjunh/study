<template>
  <section>
    <div class="movie-container">
      <div>
        <iframe
          class="movie-video"
          width="1300"
          height="530"
          src="https://www.youtube.com/embed/fvHqsg5y9oU?autoplay=1&controls=0&loop=1&playlist=fvHqsg5y9oU&mute=1"
          allow="autoplay"
        ></iframe>
      </div>
      <div class="content">
        <div class="content-span">
          <span>3.</span>
          <div>
            <i class="bx bxs-star"></i>
            <span class="score">4.3</span>
          </div>
        </div>
        <div class="content-text">
          <h1>쿵푸팬더4</h1>
          <div class="gern">
            <span>애니메이션</span>
            <span class="release-date">개봉일 2024.04.10</span>
          </div>
          <p>
            "오랜만이지! 드림웍스 레전드 시리즈 마침내 컴백! 마침내 내면의 평화…
            냉면의 평화…가 찾아왔다고 믿는 용의 전사 ‘포’ 이젠 평화의 계곡의
            영적 지도자가 되고, 자신을 대신할 후계자를 찾아야만 한다. “이제 용의
            전사는 그만둬야 해요?” 용의 전사로의 모습이 익숙해지고 새로운 성장을
            하기보다 지금 이대로가 좋은 ‘포’ 하지만 모든 쿵푸 마스터들의 능력을
            그대로 복제하는 강력한 빌런 ‘카멜레온’이 나타나고 그녀를 막기 위해
            정체를 알 수 없는 쿵푸 고수 ‘젠’과 함께 모험을 떠나게 되는데… 포는
            가장 강력한 빌런과 자기 자신마저 뛰어넘고 진정한 변화를 할 수
            있을까?"
          </p>
        </div>
        <div class="poster">
          <img src="@/assets/poster3.jpeg" alt="" />
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
  background-color: #708b99;
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
