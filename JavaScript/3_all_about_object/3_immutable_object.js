/**
 * Immutable Object
 */
const yuJin = {
  name: "안유진",
  year: 2003,

  get age() {
    return new Date().getFullYear() - this.year;
  },
  set age(age) {
    this.year = new Date().getFullYear() - age;
  },
};

console.log(yuJin);

/**
 * Extensible 확장 가능한지
 * false면 삭제는 가능하지만 추가는 불가능
 */
console.log(Object.isExtensible(yuJin));
yuJin["position"] = "vocal";
console.log(yuJin);
Object.preventExtensions(yuJin);
console.log(Object.isExtensible(yuJin));
yuJin["groupName"] = "아이브";
console.log(yuJin);
delete yuJin["position"];
console.log(yuJin);
console.log("---------------");
/**
 * Seal 봉인
 * Object.isSeales() 봉인이 되어있는지
 * configurable을 false로 만드는거랑 같음
 * 값 추가, 삭제 둘다 안됨
 */
const yuJin2 = {
  name: "안유진",
  year: 2003,

  get age() {
    return new Date().getFullYear() - this.year;
  },
  set age(age) {
    this.year = new Date().getFullYear() - age;
  },
};

console.log(Object.isSealed(yuJin2)); // false
Object.seal(yuJin2); // 봉인
console.log(Object.isSealed(yuJin2)); //true

yuJin2["groupName"] = "아이브";
console.log(yuJin2);
delete yuJin2["name"];
console.log(yuJin2); //삭제도 안됨

Object.defineProperty(yuJin2, "name", {
  value: "장원영",
});
console.log(Object.getOwnPropertyDescriptor(yuJin2, "name"));

/**
 * Freezed
 * 읽기 외에 모든 기능을 불가능하게 만든다.
 */
const yuJin3 = {
  name: "안유진",
  year: 2003,

  get age() {
    return new Date().getFullYear() - this.year;
  },
  set age(age) {
    this.year = new Date().getFullYear() - age;
  },
};
console.log(Object.isFrozen(yuJin3)); // false
Object.freeze(yuJin3);
console.log(Object.isFrozen(yuJin3)); // true

yuJin3["groupName"] = "아이브";
console.log(yuJin3); // 추가 안됨

delete yuJin3["name"];
console.log(yuJin3); // 삭제도 안됨

// Object.defineProperty(yuJin3, "name", {
//   value: "장원영",
// }); //에러남 벨류도 안바뀜
console.log(Object.getOwnPropertyDescriptor(yuJin3, "name"));
// enumerable 빼고는 다 false로 만든다.

const yuJin4 = {
  name: "안유진",
  year: 2003,
  wonYoung: {
    name: "장원영",
    year: 2004,
  },
};
Object.freeze(yuJin4);
console.log(Object.isFrozen(yuJin4));
console.log(Object.isFrozen(yuJin4["wonYoung"])); // 내부 객체는 같이 얼려지지 않음
