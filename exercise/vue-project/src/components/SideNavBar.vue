<template>
  <div class="sidenav" :style="{ width: sidenavState + 'px' }">
    <input type="checkbox" id="click" />
    <label @click="sidenavToggle" for="click"
      ><i class="menu-btn bx bx-menu"></i><i class="close-btn bx bx-x"></i
    ></label>

    <div class="icon_items">
      <ul>
        <li class="active">
          <i class="bx bx-home-alt"></i
          ><RouterLink :to="{ name: 'home' }">홈</RouterLink>
        </li>
        <li><i class="bx bx-user"></i><a href="#">User</a></li>
        <li><i class="bx bx-message-rounded"></i><a href="#">Message</a></li>
        <li><i class="bx bx-bar-chart-alt-2"></i><a href="#">Activity</a></li>
        <li><i class="bx bx-shopping-bag"></i><a href="#">Products</a></li>
        <li><i class="bx bx-bell"></i><a href="#">Notification</a></li>
        <li><i class="bx bx-group"></i><a href="#">Group</a></li>
        <li><i class="bx bx-help-circle"></i><a href="#">Help</a></li>
        <li><i class="bx bx-cog"></i><a href="#">Setting</a></li>
      </ul>
    </div>
  </div>
</template>
<script setup>
import { ref } from "vue";
const sidenavState = ref(70);
const sidenavToggle = () => {
  if (sidenavState.value === 70) {
    sidenavState.value = 260;
  } else {
    sidenavState.value = 70;
  }
  // sidenav 요소들 전부 메뉴버튼 누르면 크기랑 요소 조절로 보이게 했는데
  // 메뉴버튼도 스크롤 내릴때 같이 아래로 내려가야되서 sidenav의 자식으로 넣었음
  // 그렇게 하면 css로는 부모요소 조작할 방법이 없어서
  // 기본값 115px로 넣어주고 버튼 누를때마다 함수써서 115 <-> 260으로 크기 조절
};
</script>
<style scoped>
.sidenav {
  height: 100vw;
  overflow: hidden;
  position: fixed;
  top: 50px;
  left: 0;
  padding: 32px 16px;
  background-color: #030303;
  transition: width 0.6s;
  border-right: 3px solid #4b4651;
}

.sidenav label .close-btn {
  display: none;
}

/* .sidenav .logo h2 {
    font-size: 20px;
    text-transform: uppercase;
    text-align: center;
    opacity: 0;
    pointer-events: none;
    transition: 0.3s ease;
  } 로고 넣을때 다시 사용 */

.sidenav .icon_items ul {
  list-style: none;
  margin-top: 32px;
  padding: 0 10px;
}

.sidenav .icon_items ul li {
  cursor: pointer;
  margin: 4px;
  padding: 12px 0;
  border-radius: 8px;
  display: flex;
  align-items: center;
  translate: 0.5s ease;
}

.icon_items .active,
.sidenav .icon_items ul li:hover {
  background-color: #1e1e31;
}

.sidenav .icon_items ul li i {
  font-size: 26px;
  padding: 0 9px;
  color: white;
}

.sidenav .icon_items ul li a {
  text-decoration: none;
  color: white;
  font-size: 17px;
  padding-left: 18px;
  opacity: 0;
  pointer-events: none;
  transition: 0.3s ease;
}

#click {
  display: none;
}

.sidenav label {
  position: absolute;
  left: 36%;
  top: 2%;
  font-size: 30px;
  z-index: 1;
  cursor: pointer;
  color: white;
}

#click:checked ~ .icon_items ul li a {
  opacity: 1;
  pointer-events: auto;
}

#click:checked ~ .logo h2 {
  opacity: 1;
  pointer-events: auto;
}

#click:checked ~ label {
  left: 13%;
}

#click:checked ~ label .close-btn {
  display: block;
}

#click:checked ~ label .menu-btn {
  display: none;
}

/* #click:checked ~ .sidenav {
    width: 260px;
  } */
/* 이거는 부모요소라 방법이 없어서 js로 해야됨 */
</style>
