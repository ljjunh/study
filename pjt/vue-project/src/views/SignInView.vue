<template>
  <main>
    <div class="sign-in-container">
      <div>
        <span>로그인</span>
        <a href="#">비밀번호를 잊어버리셨나요?</a>
      </div>
      <form class="sign-in-form">
        <div><input type="text" /></div>
        <div><input type="text" /></div>
        <div><button>로그인</button></div>
      </form>
      <p>다른 방법으로 로그인하기</p>
      <ul>
        <li></li>
        <li></li>
        <li></li>
        <li></li>
        <li></li>
      </ul>
    </div>
  </main>
</template>

<script setup></script>

<style scoped>
main {
  display: flex;
  justify-content: center;
  align-items: center;
}
.sign-in-container {
  margin-top: 50px;
}
</style>
