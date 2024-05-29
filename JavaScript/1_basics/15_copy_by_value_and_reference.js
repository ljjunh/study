/**
 * copy by value 값에 의한 전달
 * copy by reference 참조에 의한 전달
 *
 * 1) 기본적으로 모든 원시타입은 copy by value다
 * 2) 객체타입은 copy by reference다
 */
let original = "안녕하세요";
let clone = original;
console.log(original);
console.log(clone);
clone += " 안유진 입니다.";
console.log("------------------");
console.log(original);
console.log(clone); // 복사본을 변경해도 원본에 영향 x 값을 복사한거임
console.log("------------------");

let originalObj = {
  name: "안유진",
  group: "아이브",
};
let cloneObj = originalObj;
console.log(originalObj);
console.log(cloneObj);
console.log("-------------");

originalObj["group"] = "코드팩토리";
console.log(originalObj);
console.log(cloneObj);
// originalObj만 변경해도 cloneObj까지 변경됨
console.log(originalObj === cloneObj); // true
console.log(original === clone); // false
// 결국 object의 복사는 copy by reference임 값이 아니라 주소값을 참조
// 그래서 원본이나 복사본 둘중 하나만 변경해도 둘 다 값이 변경됨

const yuJin1 = {
  name: "안유진",
  group: "아이브",
};
const yuJin2 = yuJin1;
const yuJin3 = {
  name: "안유진",
  group: "아이브",
};

console.log(yuJin1 === yuJin2); // true
console.log(yuJin1 === yuJin3); // false
console.log(yuJin2 === yuJin3); // false

// spread를 쓰면 object 복사할때 값만 복사 가능
const yuJin4 = {
  ...yuJin3,
};
console.log(yuJin4);
console.log(yuJin4 === yuJin3); // copy by value여서 false가 나옴
