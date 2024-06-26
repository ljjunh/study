// void
// 아무것도 없음을 의미하는 타입

function func1(): string {
  return "hello";
}

// 반환값이 아무것도 없을때 void
function func2(): void {
  console.log("hello");
}

// void변수에는 undefined를 제외한 값은 들어올 수 없음
let a: void;
// a = 1;
// a = "hello";
// a = {};
a = undefined;

// never
// 불가능한 타입
function func3(): never {
  while (true) {}
}

function func4(): never {
  throw new Error();
}
// never타입은 진짜 아무것도 못담음
// let b:never;
// b=1;
// b=undefined;
// b=null;
