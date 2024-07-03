/**
 * 함수 타입 정의
 */

// 함수를 설명하는 가장 좋은 방법
// js: 어떤 매개변수를 받고, 어떤 결과값을 반환하는지 이야기
// ts: 어떤 [타입의] 매개변수를 받고, 어떤 [타입의] 결과값을 반환하는지 이야기
function func(a: number, b: number) {
  return a + b;
}

/**
 * 화살표 함수의 타입을 정의하는 방법
 */
const add = (a: number, b: number): number => a + b;
// 반환값을 기준으로 자동추론해서 타입 생략가능

/**
 * 함수의 매개변수
 */

const introduce = (name = "임준희", age?: number) => {
  console.log(`name: ${name}`);
  if (typeof age === "number") {
    console.log(`age: ${age + 1}`);
  }
};
introduce("임준희", 20);
introduce("임준희");
function getSum(...rest: number[]) {
  let sum = 0;
  rest.forEach((it) => (sum += it));
  return sum;
}
getSum(1, 2, 3); // 6
getSum(1, 2, 3, 4, 5); // 15
