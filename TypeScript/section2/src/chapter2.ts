// 배열
let numArr: number[] = [1, 2, 3];

let strArr: string[] = ["hello", "hi"];

// 제네릭 문법
let boolArr: Array<boolean> = [true, false, true];

// 배열에 들어가는 요소들의 타입이 다양할 경우
let multiArr: (string | number)[] = [1, "hello"];

// 다차원 배열의 타입을 정의하는 방법
let doubleArr: number[][] = [
  [1, 2, 3],
  [4, 5],
];

// 튜플 (js에는 없고 ts엔 있음)
// 길이와 타입이 고정된 배열

let tup1: [number, number] = [1, 2];

let tup2: [number, string, boolean] = [1, "2", true];
tup1.push(1);
tup1.pop();
tup1.pop();
// 배열로 인식되기때문에 배열메서드는 사용해도 길이고정이 발동되지 않음

const users: [string, number][] = [
  ["가나다", 1],
  ["나다라", 2],
  ["다라마", 3],
  ["라마바", 4],
];
