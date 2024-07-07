/**
 * keyof 연산자
 * 타입에만 사용할 수 있음
 */

type Person = typeof person;
// type을 정의할때 typeof를 쓰면 person의 타입을 추론해서 타입별칭에 정의해줌

// keyof를 쓰면 객체 타입으로부터 모든 프로퍼티를 union타입으로 추출해줌
function getPropertyKey(person: Person, key: keyof typeof person) {
  return person[key];
}

const person = {
  name: "임준희",
  age: 29,
};

getPropertyKey(person, "name");
