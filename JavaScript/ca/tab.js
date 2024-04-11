// 버튼0 누르면
// - 모든 버튼에 붙은 orange 클래스명 제거
// - 버튼0에 orange 클래스명 추가
// 모든 div에 show 클래스명 제거
// div0에 show 클래스명 추가

var tb = document.querySelectorAll(".tab-button");
var tc = document.querySelectorAll(".tab-content");
var cnt = document.querySelectorAll(".tab-button").length;
for (let i = 0; i < cnt; i++) {
  tb[i].addEventListener("click", () => {
    for (let j = 0; j < 3; j++) {
      tb[j].classList.remove("orange");
      tc[j].classList.remove("show");
    }
    tb[i].classList.add("orange");
    tc[i].classList.add("show");
  });
}
