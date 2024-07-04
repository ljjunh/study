/**
 * 함수 타입 표현식
 */

type Operation = (a: number, b: number) => number;
//       매개변수 a와 b의 타입 number  반환값도 number
const add: Operation = (a, b) => a + b;
const sub: Operation = (a, b) => a - b;
const multiply: Operation = (a, b) => a * b;
// 함수 타입 표현식을 쓰면 비슷한 함수를 한번의 타입으로 설정 가능

// 타입 별칭 없이도 표현식만으로 타입 정의 가능
const divide: (a: number, b: number) => number = (a, b) => a + b;

/**
 * 호출 시그니처
 * (콜 시그니처)
 */
type Operation2 = {
  (a: number, b: number): number;
};

const add2: Operation2 = (a, b) => a + b;
const sub2: Operation2 = (a, b) => a - b;
const multiply2: Operation2 = (a, b) => a * b;
const divide2: (a: number, b: number) => number = (a, b) => a + b;
