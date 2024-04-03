// 함수 선언
function greeting() {
  console.log("안녕하세요!");
}
console.log("호출 전");
greeting();
console.log("호출 후");

function getArea(width, height) {
  let area = width * height;
  return area;
}

let area1 = getArea(10, 20);
console.log(area1);
console.log(getArea(20, 30));
