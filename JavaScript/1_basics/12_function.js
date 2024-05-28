/**
 *
 * function -> 함수
 */

/**
 * 만약에 2라는 숫자에 * 10 / 2 %3 스트링으로 변환해서
 * 반환받고 싶다면 어떻게 해야 할까?
 */
console.log((((2 * 10) / 2) % 3).toString());
function calculate(number) {
  // number: 파라미터(입력 받은 값)
  console.log((((number * 10) / 2) % 3).toString());
}
calculate(4); // 4 : argument 입력하는 값

/**
 * 함수에서 입력받는 값에 대한 정의를 Parameter라고 한다.
 * 실제 입력하는 값은 argument라고 한다.
 */

function multiply(x, y) {
  console.log(x * y);
}
multiply(3, 4);

function multiply2(x, y = 10) {
  console.log(x * y);
}
multiply2(2, 4); // 8
multiply2(3); // 30 y값을 안넣어줘서 기본값 10이 되고, 3 * 10 = 30

/**
 * 반환 받기
 * return 받기
 */
console.log("----------------");
function multiply3(x, y) {
  return x * y;
}
const result1 = multiply3(2, 4);
console.log(result1);

const result2 = multiply3(4, 5);
console.log(result2);

/**
 * Arrow 함수
 */
const multiply4 = (x, y) => {
  return x * y;
};
console.log(multiply4(3, 4));

const multiply5 = (x, y) => x * y;
console.log(multiply5(4, 5));
// 간결하게 생략 가능

const multiply6 = (x) => x * 2;
// 파라미터가 1개면 앞에 ()도 생략 가능
console.log(multiply6(2));

function multiply7(x) {
  return function (y) {
    return function (z) {
      return `x: ${x} y: ${y} z: ${z}`;
    };
  };
}
console.log(multiply7(3)(4)(5));

const multiply8 = function (x, y) {
  return x * y;
};
console.log(multiply8(4, 5));

const multiplyThree = function (x, y, z) {
  console.log(arguments);
  return x * y * z;
};

console.log("---------------");
console.log(multiplyThree(4, 5, 6));
console.log("---------------");

const multiplyAll = function (...arguments) {
  return Object.values(arguments).reduce((a, b) => a * b, 1);
};
console.log(multiplyAll(3, 4, 5, 6, 7, 8, 9, 10));

// immediately invoked function
(function (x, y) {
  console.log(x * y);
})(4, 5);

console.log(typeof multiply);
console.log(multiply instanceof Object);
// 왼쪽에 있는게 오른쪽과 같은 타입인지
// true 함수는 Object임
