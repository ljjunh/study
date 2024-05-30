/**
 * Scope
 */
var numberOne = 20;

function levelOne() {
  console.log(numberOne);
}

// levelOne(); // 20
// 함수 밖의 상위 스코프의 변수에 접근 가능

var numberOne = 20;

function levelOne() {
  var numberOne = 40;
  console.log(numberOne);
}
levelOne(); // 40 가장 가까운 스코프의 변수를 가져오기 때문
console.log(numberOne); // 20 함수안에 선언한 변수는 상위 스코프의 변수를 덮어쓰지 않음

function levelOne() {
  var numberOne = 40;
  function levelTwo() {
    var numberTwo = 99;
    console.log(`levelTwo numberTwo : ${numberTwo}`); // 99
    console.log(`levelOne numberOne : ${numberOne}`); // 40
  }
  levelTwo();
  console.log(`levelOne numberOne : ${numberOne}`); // 40
}
levelOne();
// 모든 선언은 가장 가까운 스코프에 있는 선언부터 활용
console.log(numberOne); // 20 전역변수 numberOne
// console.log(numberTwo); // error 하위스코프로는 접근 불가

/**
 * Js -> Lexical Scope
 * 선언된 위치가 상위 스코프를 정한다.
 *
 * 반대 Dynamic Scope
 * 실행한 위치가 상위 스코프를 정한다.
 */
var numberThree = 3;
function functionOne() {
  var numberThree = 100;
  functionTwo();
}
function functionTwo() {
  console.log(numberThree);
}
functionOne(); // 3이 나옴
// lexical scope기 때문에 선언된 위치에서 찾음

var i = 3;
for (var i = 0; i < 5; i++) {
  console.log(i);
}
console.log(`i in global scope : ${i}`);

i = 999;
// block level scope
for (let i = 0; i < 10; i++) {
  console.log(i);
}
console.log(`i in global scope : ${i}`);
// for문 안에선 블록레벨이라 전역에서 다시 출력하면 원래의 999가 나옴

/**
 * var 키워드는 함수 레벨 스코프만 만들어낸다
 * let, const 키워드는 함수 레벨 스코프와 블록 레벨 스코프를 만들어 낸다.
 */
