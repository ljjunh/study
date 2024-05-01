<template>
  <div>
    <img :src="item.image" class="room-img" />
    <h4 @click="send">
      {{ item.title }}
    </h4>
    <p>{{ item.price }} 원</p>
  </div>
</template>

<script>
export default {
  name: "CardComponent",
  props: {
    item: Object,
  },
  methods: {
    send() {
      this.$emit("openModal", this.item.id);
    },
  },
};
</script>

<style></style>
