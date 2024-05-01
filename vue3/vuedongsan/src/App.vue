<template>
  <!-- 모달창 -->
  <ModalComponent
    :onerooms="onerooms"
    :clickNum="clickNum"
    :modalState="modalState"
    @closeModal="modalState = false"
  />

  <div class="menu">
    <a v-for="(arr, idx) in menus" :key="idx">{{ arr }}</a>
    <!-- 자료안의 데이터 갯수만큼 반복됨, 작명한 변수는 데이터안의 자료를 순회 -->
    <!-- key는 반복문 돌린 요소를 컴퓨터가 구분하기 위해 씀(식별) 변하는 숫자나 문자가 들어가야 함 -->
    <!-- 반복문에서는 array내의 데이터와 인덱스 두가지를 쓸 수 있어서 key는 보통 두번째 인자 인덱스를 씀 -->
  </div>

  <DiscountComponent />

  <CardComponent
    @openModal="
      modalState = true;
      clickNum = $event;
    "
    v-for="item in onerooms"
    :key="item.id"
    :item="item"
  />
</template>

<script>
import data from "./assets/oneroom";
import DiscountComponent from "./Discount.vue";
import ModalComponent from "./Modal.vue";
import CardComponent from "./Card.vue";
// {{데이터바인딩}} 하는 이유
// 1. HTML에 하드코딩 해놓으면 나중에 변경 어려움
// 2. Vue의 실시간 자동 렌더링 쓰려고
// HTML속성도 데이터바인딩 가능
// :속성="데이터 이름"
export default {
  name: "App",
  data() {
    return {
      menus: ["Home", "Shop", "About"],
      modalState: false,
      onerooms: data,
      clickNum: 0,
    };
  },
  methods: {},
  components: {
    DiscountComponent: DiscountComponent,
    ModalComponent: ModalComponent,
    CardComponent: CardComponent,
  },
};
</script>

<style>
body {
  margin: 0;
}
div {
  box-sizing: border-box;
}
.discount {
  background-color: #eee;
  padding: 10px;
  margin: 10px;
  border-radius: 5px;
}
.black-bg {
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  position: fixed;
  padding: 20px;
}
.white-bg {
  width: 100%;
  background-color: white;
  border-radius: 8px;
  padding: 20px;
}
.room-img {
  width: 100%;
  margin-top: 40px;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.menu {
  background-color: darkslateblue;
  padding: 15px;
  border-radius: 5px;
}
.menu a {
  color: white;
  padding: 10px;
}
</style>
