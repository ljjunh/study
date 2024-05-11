<template>
  <div class="topnav">
    <img src="@/assets/logo.webp" />
    <form action="#">
      <i class="bx bx-search"></i>
      <input type="text" placeholder="검색어를 입력해주세요" />
    </form>
    <div class="links">
      <ul>
        <li>
          <i class="bx bx-bell"></i>
        </li>
        <li><a href="#" class="login">로그인</a></li>
        <li><a href="#" class="signup">회원가입</a></li>
      </ul>
    </div>
  </div>
</template>

<script setup></script>

<style scoped>
.topnav {
  background-color: #030303;
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  max-width: 100vw;
  height: 50px;
  position: fixed;
  top: 0px;
}
.topnav form {
  height: 60%;
  background-color: #2d2634;
  display: flex;
  align-items: center;
  border-radius: 10px;
  margin-left: 10px;
}
.topnav form input {
  flex: 1;
  margin: 15px;
  border: none;
  font-size: 20px;
  background-color: #2d2634;
}

.topnav form i {
  color: #fff;
  cursor: pointer;
  transition: all 0.2s;
  margin-left: 10px;
}

.topnav .links ul {
  display: flex;
}

.topnav .links ul li {
  margin-right: 20px;
}

.topnav .links ul li i {
  color: #fff;
}
.topnav .links ul li a {
  text-decoration: none;
  color: #fff;
  padding: 5px 10px;
  border-radius: 5px;
}

.topnav .links ul li .signup {
  background-color: #f82e62;
}

.topnav img {
  width: 100px;
}
/*

.topnav form button:hover {
  background-color: rgb(9, 91, 91);
}
.topnav form button i {
  font-size: 25px;
  color: #fff;
} */
</style>
