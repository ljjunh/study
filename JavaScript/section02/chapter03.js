// 1. 배열의 구조 분해 할당
let arr = [1, 2, 3];

// let one = arr[0];
// let two = arr[1];
// let three = arr[2];

// let [one, two, three] = arr;
// 위에처럼 하나씩 넣지 말고 이렇게 한번에 구조분해 할당으로 넣을 수 있음

// let [one, two] = arr;
// 마지막꺼 안넣고싶으면 안넣어도 됨

// let [one, two, three, four] = arr;
// 값이 모자라게 넣어도 에러는 안나고 four를 출력해보면 undefined가 출력됨

let [one, two, three, four = 4] = arr;
// 값이 모자라는 상황에 기본값 설정 가능

// 2. 객체의 구조 분해 할당
let person = {
  name: "임준희",
  age: 27,
  hobby: "축구",
};

// let name = person.name;
// let age = person.age;
// let hobby = person.hobby;
// 이렇게 하나씩 넣을 필요 없이 구조 분해 할당을 이용해서 값을 넣을 수 있음
let { name, age: myAge, hobby } = person;
// 변수명도 다르게 설정 가능
// console.log(name, myAge, hobby);

// 3. 객체 구조 분해 할당을 이용해서 함수의 매개변수를 받는 방법
const func = ({ name, age, hobby }) => {
  console.log(name, age, hobby);
};
func(person);
