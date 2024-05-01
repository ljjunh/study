<template>
  <div class="black-bg" v-if="modalState">
    <div class="white-bg">
      <img :src="onerooms[clickNum].image" />
      <h4>{{ onerooms[clickNum].title }}</h4>
      <p>{{ onerooms[clickNum].content }}</p>
      <p>{{ onerooms[clickNum].price }} 원</p>
      <!-- <button @click="modalState = false">닫기</button> 이건 props직접 수정하는거라 못씀-->
      <button @click="send">닫기</button>
    </div>
  </div>
</template>
<script>
export default {
  name: "ModalComponent",
  props: {
    onerooms: Array,
    clickNum: Number,
    modalState: Boolean,
  },
  methods: {
    send() {
      this.$emit("closeModal");
    },
  },
};
</script>
<style></style>
