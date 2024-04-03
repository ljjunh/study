// 1. 함수 표현식

function funcA() {
  console.log("funcA");
}

let varA = funcA;
varA();

// funcA처럼 함수 선언문을 이용해서 만들지 않고
// varB처럼 값으로써 함수를 생성하는 방식을 함수표현식이라고 부름
// 호이스팅이 안됨
let varB = function () {
  console.log("funcB");
};
varB();

// 2. 화살표 함수
// 함수를 이전보다 더 빠르고 간결하게 생성해 줄 수 있도록 도와주는
// JavaScript 문법
let varC = (value) => {
  console.log(value);
  return value + 1;
};

console.log(varC(10));
