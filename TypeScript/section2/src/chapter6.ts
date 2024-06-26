// any
// 특정 변수의 타입을 우리가 확실히 모를때
// 모든 타입의 값을 할당할 수 있음
// 모든 타입의 변수에 any타입의 변수를 넣을 수 있음
// 검사를 통과해서 런타임에 에러가남(타입스크립트 포기하는 느낌)
// 최대한 안쓰는걸로
let anyVar: any = 10;

// anyVar = "hello";
// anyVar = true;
// anyVar = {};
// anyVar = () => {};
// anyVar.toUpperCase();
// anyVar.toFixed();

// let num: number = 10;
// num = anyVar;

// unknown
let unknownVar: unknown;

unknownVar = "";
unknownVar = 1;
let num: number = 10;
