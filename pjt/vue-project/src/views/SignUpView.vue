<template>
  <main>
    <div class="signup-container">
      <h1>회원 가입</h1>
      <form class="signup-form">
        <label for="name">
          <input
            @input="nameCheck"
            v-model="name"
            id="name"
            type="text"
            placeholder="이름 (2자 이상)"
            :style="{
              border: nameState ? '1px solid #48484b' : '1px solid #e73e3e',
            }"
          />
        </label>
        <label class="email-wrapper" for="email">
          <input
            @input="emailCheck"
            v-model="email"
            id="email"
            type="text"
            placeholder="이메일 (example@gmail.com)"
            :style="{
              border: emailState ? '1px solid #48484b' : '1px solid #e73e3e',
            }"
          />
        </label>
        <label class="pwd-wrapper" for="password">
          <input
            @input="passwordCheck"
            v-model="password"
            id="password"
            type="text"
            placeholder="비밀번호 (8자 이상)"
            :style="{
              border: passwordState ? '1px solid #48484b' : '1px solid #e73e3e',
            }"
          />
        </label>
        <div class="checkbox-wrapper">
          <div>
            <input v-model="firstCheckBox" id="firstCheckBox" type="checkbox" />
            <label for="firstCheckBox">만 14세 이상입니다</label>
          </div>
          <div>
            <input
              v-model="secondCheckBox"
              id="secondCheckBox"
              type="checkbox"
            /><label for="secondCheckBox">회원가입에 동의합니다</label>
          </div>
        </div>
        <div
          :style="{ opacity: buttonActive ? '1' : '0.3' }"
          class="btn-wrapper"
        >
          <button><span>가입하기</span></button>
        </div>
      </form>
    </div>
  </main>
</template>

<script setup>
import { ref, computed } from "vue";
const name = ref("");
const email = ref("");
const password = ref("");
const firstCheckBox = ref(false);
const secondCheckBox = ref(false);

const nameState = ref("false");
const emailState = ref("false");
const passwordState = ref("false");

// 이름 2글자 이상 입력 -> border #e73e3e -> #48484b
const nameCheck = () => {
  if (name.value.length >= 2) {
    nameState.value = true;
  } else {
    nameState.value = false;
  }
};

// 이메일 @, . 포함 입력 -> border #e73e3e -> #48484b
const emailCheck = () => {
  if (email.value.includes("@") && email.value.includes(".")) {
    emailState.value = true;
  } else {
    emailState.value = false;
  }
};

// 비밀번호 8글자 이상 입력 -> border #e73e3e -> #48484b
const passwordCheck = () => {
  if (password.value.length >= 8) {
    passwordState.value = true;
  } else {
    passwordState.value = false;
  }
};

// 이름, 이메일, 비밀번호, 체크박스 모두 형식에 맞으면 로그인 버튼 활성화
const buttonActive = computed(() => {
  return (
    nameState &&
    emailState.value &&
    passwordState.value &&
    firstCheckBox.value &&
    secondCheckBox.value
  );
});
</script>

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
  margin-top: 20px;
  color: #fff;
}

.signup-container .signup-form .checkbox-wrapper div {
  display: flex;
  font-size: 12px;
  margin-bottom: 2px;
}
.signup-container .signup-form .checkbox-wrapper div input {
  width: 14px;
  height: 14px;
  margin: 1px;
  border: 1px solid #48484b;
  accent-color: #f82f62;
}

.signup-container .signup-form .checkbox-wrapper div label {
  margin-top: 3px;
  margin-bottom: 3px;
  padding-left: 4px;
}
.signup-container .signup-form input {
  padding: 13px 11px;
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
