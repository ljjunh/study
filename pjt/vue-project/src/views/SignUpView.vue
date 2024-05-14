<template>
  <main>
    <div class="signup-container">
      <h1>회원 가입</h1>
      <form class="signup-form">
        <label for="">
          <input type="text" placeholder="이름 (2자 이상)" />
        </label>
        <label class="email-wrapper" for="">
          <input type="text" placeholder="이메일 (example@gmail.com)" />
        </label>
        <label class="pwd-wrapper" for="">
          <input type="text" placeholder="비밀번호 (8자 이상)" />
        </label>
        <div class="checkbox-wrapper">
          <div><label for=""></label></div>
          <div><label for=""></label></div>
          <div><label for=""></label></div>
          <div><label for=""></label></div>
          <div><label for=""></label></div>
          <div><label for=""></label></div>
        </div>
        <div class="btn-wrapper">
          <button><span>가입하기</span></button>
        </div>
        <p>결제 정보요? 충분히 둘러보시고 입력해도 늦지 않아요</p>
      </form>
    </div>
  </main>
</template>

<script setup></script>

<style scoped>
main {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100vw;
  height: 100vh;
  background-image: url("../assets/loginBackground.webp");
}
.signup-container {
  width: 310px;
  height: 446px;
}
.signup-container h1 {
  margin-bottom: 16px;
  text-align: center;
  color: #fff;
  font-size: 20px;
}
.signup-container .signup-form .checkbox-wrapper {
  margin-top: 24px;
}

.signup-container .signup-form input {
  padding: 13px 11px;
  border: 1px solid #48484b;
  height: 20px;
  margin-bottom: 4px;
  background-color: #191a1c;
  border-radius: 5px;
  color: #fff;
  outline: none;
}

.signup-container .signup-form .pwd-wrapper {
  margin-top: 4px;
}
.signup-container .signup-form input {
  width: 100%;
}

.signup-container .signup-form .btn-wrapper {
  margin: 14px 0px;
  background-color: #f82f62;
  border-radius: 5px;
  width: 334px;
  height: 40px;
  display: flex;
  justify-content: center;
}

.signup-container .signup-form .btn-wrapper button {
  background: none;
  border: none;
  padding: 0px 16px;
}
.signup-container .signup-form .btn-wrapper span {
  color: #fff;
  font-size: 15px;
}
</style>
