// 버튼0 누르면
// - 모든 버튼에 붙은 orange 클래스명 제거
// - 버튼0에 orange 클래스명 추가
// 모든 div에 show 클래스명 제거
// div0에 show 클래스명 추가

var tb = document.querySelectorAll(".tab-button");
var tc = document.querySelectorAll(".tab-content");
var cnt = document.querySelectorAll(".tab-button").length;
// for (let i = 0; i < cnt; i++) {
//   탭열기(i)
// }

document.querySelector(".list").addEventListener('click', (e)=>{
  탭열기(parseInt(e.target.dataset.id))

})


function 탭열기(숫자){
  tb[숫자].addEventListener("click", () => {
    for (let j = 0; j < 3; j++) {
      tb[j].classList.remove("orange");
      tc[j].classList.remove("show");
    }
    tb[숫자].classList.add("orange");
    tc[숫자].classList.add("show");
  });
}