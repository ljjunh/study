/*
 * 선언 합침
 * 동일한 이름으로 선언한 인터페이스는 합쳐짐
 */

interface Person {
  name: string;
}

interface Person {
  //name: number; // 충돌
  age: number;
}

interface Developer extends Person {
  name: "hello";
}

const person: Person = {
  name: "",
  age: 27,
};

/**
 * 모듈 보강
 */

interface Lib {
  a: number;
  b: number;
}

interface Lib {
  c: string;
}

const lib: Lib = {
  a: 1,
  b: 2,
  c: "hello",
};
