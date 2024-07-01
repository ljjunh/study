/**
 * 대수 타입
 * -> 여러개의 타입을 합성해서 새롭게 만들어낸 타입
 * 합집합 타입과 교집합 타입이 존재함
 */

/**
 * 1. 합집합 - Union 타입
 * | 를 이용해서 여러개 타입 넣을 수 있음
 */

let a: string | number | boolean;
a = 1;
a = "hello";
a = true;

let arr: (number | string | boolean)[] = [1, "hello", true];

type Dog = {
  name: string;
  color: string;
};

type Person = {
  name: string;
  language: string;
};

type Union1 = Dog | Person;

let union1: Union1 = {
  name: "",
  color: "",
};

let union2: Union1 = {
  name: "",
  language: "",
};

let union3: Union1 = {
  name: "",
  color: "",
  language: "",
};

// let union4: Union1 = {
//   name: "",
// };
// Dog, Person, 교집합 어떤 부분에도 못들어가서 오류남

/**
 * 2. 교집합 타입 - Intersection 타입
 */
let variable: number & string;
// number랑 string은 교집합이 없기 떄문에 never 타입으로 만들어짐

type Intersection = Dog & Person;

// 프로퍼티가 하나라도 빠지면 안됨
let intersection1: Intersection = {
  name: "",
  color: "",
  language: "",
};
