/**
 * Property Attribute
 * 1) 데이터 프로퍼티 - 키와 값으로 형성된 실질적 값을 갖고 있는 프로퍼티
 * 2) 액세서 프로퍼티 - 자체적으로 값을 갖고 있지 않지만 다른 값을 가져오거나
 *                  설정할 때 호출되는 함수로 구성된 프로퍼티(getter와 setter)
 *
 */
const yuJin = {
  name: "안유진",
  year: 2003,
};
console.log(Object.getOwnPropertyDescriptor(yuJin, "year"));

/**
 * 1) value - 실제 프로퍼티의 값
 * 2) writable - 값을 수정 할 수 있는지 여부. false로 설정하면 프로퍼티 값을 수정할 수 없음
 * 3) enumerable - 열거가 가능한지 여부. for...in 등을 사용 할 수 있으면 true 반환
 * 4) configurable - 프로퍼티 어트리뷰트의 재정의가 가능한지 여부를 판단
 *                   false일 경우 프로퍼티 삭제나 어트리뷰트 변경이 금지
 *                   단, writable이 true인 경우 value와 writable을 변경하는건 가능
 */

console.log(Object.getOwnPropertyDescriptor(yuJin, "name"));
console.log(Object.getOwnPropertyDescriptors(yuJin)); //모든 프로퍼티의 arribute가 출력

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
console.log(yuJin2);
console.log(yuJin2.age);
yuJin2.age = 32;
console.log(yuJin2.age);
console.log(yuJin2.year);

console.log(Object.getOwnPropertyDescriptor(yuJin2, "age"));

// yuJin2.height = 172; // 이렇게 프로퍼티를 추가하면 writable, enumerable, configurable 모두 true로 들어감
// console.log(Object.getOwnPropertyDescriptor(yuJin2, "height"));
console.log("---------------------------");

// Attribute까지 직접 설정하는 방법 writable, enumerable, configurable 지정안하면 기본값은 false로 들어감
Object.defineProperty(yuJin2, "height", {
  value: 172,
  writable: true,
  enumerable: true,
  configurable: true,
});
console.log(yuJin2);
console.log(Object.getOwnPropertyDescriptor(yuJin2, "height"));

// writable
// writable이 true면 value 변경 가능
yuJin2.height = 180;
console.log(yuJin2);
console.log("------------------");
// writable이 false인 경우
Object.defineProperty(yuJin2, "height", {
  writable: false,
});
console.log(Object.getOwnPropertyDescriptor(yuJin2, "height"));
yuJin2.height = 172;
console.log(yuJin2.height); // 180 값 변경이 안됨
console.log("---------------");
// enumerable
console.log(Object.keys(yuJin2));
for (let key in yuJin2) {
  console.log(key);
}
Object.defineProperty(yuJin2, "name", {
  enumerable: false,
});
console.log(Object.keys(yuJin2)); //[ 'year', 'age', 'height' ] name이 안나옴
for (let key in yuJin2) {
  console.log(key); // year age height만 나옴 name 안나옴
}
console.log(yuJin2); // 여기서도 name은 안나옴
// 그렇다고해서 name이 사라진건 아님
console.log(yuJin2.name); // 안유진 출력 잘됨

// configurable
Object.defineProperty(yuJin2, "height", {
  configurable: false,
});
console.log(Object.getOwnPropertyDescriptor(yuJin2, "height")); //configurable: false로 잘 바뀜
