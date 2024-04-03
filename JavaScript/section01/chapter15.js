// 1. 객체 생성
let obj1 = new Object(); // 객체 생성자(내장함수)
let obj2 = {}; // 객체 리터럴(중괄호)

// 2. 객체 프로퍼티(객체 속성)
let person = {
  name: "임준희",
  age: 27,
  hobby: "풋살",
  10: 20,
  "like cat": false,
};
// name, age, hobby같은 객체의 정보값을 프로퍼티 또는 속성이라고 한다.
// 객체의 실질적인 정보를 담고 있는 역할
// key:value 쌍
// value 자료형 타입 제한x
// key값은 문자열이나 숫자만 가능
// key값은 따옴표 필요없음
// 하지만, like cat 같이 공백이 있으면 따옴표를 써줘야 한다.

// 3. 객체 프로퍼티를 다루는 방법
// 3.1 특정 프로퍼티에 접근(점 표기법, 괄호 표기법)
let name = person.name;
console.log(name); //타입스크립트 경고창이니 무시해도 됨

let age = person["age"];
console.log(age);

let property = "hobby";
let hobby = person[property];
console.log(hobby);

// 3.2 새로운 프로퍼티를 추가하는 방법
person.job = "fe developer";
person["favoriteFood"] = "치킨";

// 3.3 프로퍼티를 수정하는 방법
person.job = "educator";
person["favoriteFood"] = "초콜릿";

// 3.4 프로퍼티를 삭제하는 방법
delete person.job;
delete person["favoriteFood"];
console.log(person);

// 3.5 프로퍼티의 존재 유무를 확인하는 방법(in연산자)
let result1 = "name" in person;
let result2 = "cat" in person;
console.log(result1);
