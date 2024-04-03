// 1. 상수 객체
const animal = {
  type: "고양이",
  name: "나비",
  color: "black",
};

// animal = { a: 1 };
//상수 객체에 다른 객체를 생성해서 할당하는건 당연히 오류가 발생
animal.age = 2;
//객채에 새로운 프로퍼티를 추가하거나,
animal.name = "까망이";
//기존 객체에 들어있던 값을 수정하거나
delete animal.color;
//기존 객체에 들어있던 값을 삭제하는건 가능
console.log(animal);

// 2. 메서드
// -> 객체 프로퍼티 중 값이 함수인 프로퍼티
const person = {
  name: "임준희",
  //메서드 선언
  sayHi() {
    console.log("안녕!");
  },
};

person.sayHi();
person["sayHi"];
