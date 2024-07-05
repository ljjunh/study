/**
 * 함수 타입의 호환성
 * 특정 함수 타입을 다른 함수 타입으로 취급해도 괜찮은가를 판단
 * 2가지 체크
 * 1. 반환값의 타입이 호환되는지
 * 2. 매개변수의 타입이 호환되는지
 */

// 기준 1. 반환값이 호환되는가
type A = () => number;
type B = () => 10;

let a: A = () => 10;
let b: B = () => 10;

a = b; // a에 b를 넣는다는건 number에 리터럴10을 넣는다는거(업캐스팅) 가능
// b = a; // b에 a를 넣는다는건 리터럴10에 number를 넣는다는거(다운캐스팅)여서 안됨

// 기준 2. 매개변수의 타입이 호환되는지
// 2-1. 매개변수의 개수가 같을 때
type C = (value: number) => void;
type D = (value: 10) => void;

let c: C = (value) => {};
let d: D = (value) => {};
// c = d; // 매개변수의 타입을 기준으로 호환성을 판단할때는
// 업캐스팅은 호환x 다운캐스팅은 호환o
d = c; // 다운캐스팅

// 매개변수가 객체타입을 사용하는 예시를 살펴보면 이해하기 쉬움
type Animal = {
  name: string;
};
type Dog = {
  name: string;
  color: string;
};

let animalFunc = (animal: Animal) => {
  console.log(animal.name);
};
let dogFunc = (dog: Dog) => {
  console.log(dog.name);
  console.log(dog.color);
};

// animalFunc = dogFunc; // 업캐스팅인데 안됨
let testFunc = (animal: Animal) => {
  console.log(animal.name);
  //   console.log(animal.color); animal이 슈퍼타입이고 dog가 sub타입인데,
  // 만약 업캐스팅을 허용한다면 animal타입에 없는 color타입이 필요하니까
};
dogFunc = animalFunc;
let testFunc2 = (dog: Dog) => {
  console.log(dog.name);
  console.log(dog.color);
};

// 2-2. 매개변수의 개수가 다를 때
type Func1 = (a: number, b: number) => void;
type Func2 = (a: number) => void;

let func1: Func1 = (a, b) => {};
let func2: Func2 = (a) => {};

func1 = func2; //func1에 func2을 넣는다는건 타입으로 보면
// func2타입을 func1타입으로 취급한다는것과 같음
// func2의 매개변수는 1개 func1의 매개변수는 2개
// func2 = func1; // func1을 func2로 취급한다고 하면
// func1은 매개변수가 2개 func2는 1개로 타입에 맞지 않음
// 매개변수의 개수가 다를때에는 할당하려고 하는쪽의 매개변수가 더 적을때만 호환 가능
// 아예 매개변수의 타입이 다르면 안됨
