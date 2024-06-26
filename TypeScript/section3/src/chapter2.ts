// unknown타입

function unknownExam() {
  // 모든 집합의 슈퍼타입이라서 모든 타입 업캐스팅 가능
  let a: unknown = 1;
  let b: unknown = "hello";
  let c: unknown = true;
  let d: unknown = null;
  let e: unknown = undefined;

  let unknownVar: unknown;
  // 다운캐스팅 불가능
  //   let num: number = unknownVar;
  //   let str: string = unknownVar;
}

// never 타입
// 모든 집합의 서브타입
function neverExam() {
  function neverFunc(): never {
    while (true) {}
  }
  // 모든 타입의 서브타입이라 업캐스팅 가능
  let num: number = neverFunc();
  let str: string = neverFunc();
  let bool: boolean = neverFunc();

  // 다운캐스팅 불가능
  //   let never1: never= 10;
  //   let never2: never = "string"
}

// void 타입
function voidExam() {
  function voidFunc(): void {
    console.log("hi");
  }
  // void의 서브타입 undefined는 업캐스팅 가능
  let voidVar: void = undefined;
}

// any 타입(치트키)
// 모든 타입의 슈퍼타입으로 위치하기도 하고
// 모든 타입의 서브타입으로도 위치하기도 함(never만 빼고)
// 타입계층도 무시(안쓰는걸로)
function anyExam() {
  let unknownVar: unknown;
  let anyVar: any;
  let undefinedVar: undefined;
  let neverVar: never;
  anyVar = unknownVar;
  undefinedVar = anyVar;
  //   neverVar = anyVar;
  // never는 공집합이여서 무슨타입이든 다운캐스팅 불가능 심지어 any도 안됨
}
