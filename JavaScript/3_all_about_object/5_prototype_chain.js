/**
 * Prototype
 */
const testObj = {};

// __proto__ 는 모든 객체에 존재하는 프로퍼티다.
// class 배울때 상속에서 부모 클래스에 해당되는 값이다.
console.log(testObj.__proto__);

function IdolModel(name, year) {
  this.name = name;
  this.year = year;
}
console.log(IdolModel.prototype);
console.dir(IdolModel.prototype, {
  showHidden: true,
});

// circular reference 서로가 서로를 참조
console.log(IdolModel.prototype.constructor === IdolModel);
console.log(IdolModel.prototype.constructor.prototype === IdolModel.prototype);

const yuJin = new IdolModel("안유진", 2003);
console.log(yuJin.__proto__);
console.log(yuJin.__proto__ === IdolModel.prototype); // true
console.log(testObj.__proto__ === Object.prototype); // true

console.log(IdolModel.__proto__ === Function.prototype); // true
console.log(Function.prototype.__proto__ === Object.prototype); // true
console.log(IdolModel.prototype.__proto__ === Object.prototype); // true

console.log(yuJin.toString());
console.log(Object.prototype.toString());

function IdolModel2(name, year) {
  this.name = name;
  this.year = year;
  this.sayHello = function () {
    return `${this.name}이 인사를 합니다.`;
  };
}
const yuJin2 = new IdolModel2("안유진", 2003);
const wonYoung2 = new IdolModel2("장원영", 2004);

console.log(yuJin2.sayHello());
console.log(wonYoung2.sayHello());
console.log(yuJin2.sayHello === wonYoung2.sayHello); // false

console.log(yuJin2.hasOwnProperty("sayHello")); // true: 고유 프토퍼티라는거 yuJin3 객체 안에 선언되어있음
// 그래서 위에 yuJin2랑 wonYoung2의 sayHello가 다르다고 나온거임

function IdolModel3(name, year) {
  this.name = name;
  this.year = year;
}
IdolModel3.prototype.sayHello = function () {
  return `${this.name}이 인사를 합니다.`;
};
const yuJin3 = new IdolModel3("안유진", 2003);
const wonYoung3 = new IdolModel3("장원영", 2004);
console.log(yuJin3.sayHello());
console.log(wonYoung3.sayHello());
console.log(yuJin3.sayHello === wonYoung3.sayHello); // true
// 이젠 한 공간에만 sayHello 메소드가 있는거임(리소스 더 효율적으로 사용 가능)
console.log(yuJin3.hasOwnProperty("sayHello")); // false 이제는 고유 프로퍼티가 아님(상속받은 프로퍼티)

IdolModel3.sayStaticHello = function () {
  return `안녕하세요 저는 static method 입니다.`;
};
console.log(IdolModel3.sayStaticHello());

/**
 * Overriding
 */
function IdolModel4(name, year) {
  this.name = name;
  this.year = year;
  this.sayHello = function () {
    return "안녕하세요 저는 인스턴스 메서드입니다.";
  };
}
IdolModel4.prototype.sayHello = function () {
  return "안녕하세요 저는 prototype 메서드입니다";
};
const yuJin4 = new IdolModel4("안유진", 2003);
console.log(yuJin4.sayHello());
// 프로토타입 메서드는 인스턴스의 메서드로 덮어쓸수있음

/**
 * getPrototypeOf, setPrototypeOf
 * 인스턴스의 __proto__ 변경 vs 함수의 prototype 변경
 */
function IdolModel(name, year) {
  this.name = name;
  this.year = year;
}
IdolModel.prototype.sayHello = function () {
  return `${this.name} 인사를 합니다.`;
};

function FemaleIdolModel(name, year) {
  this.name = name;
  this.year = year;
  this.dance = function () {
    return `${this.name}가 춤을 춥니다.`;
  };
}

const gaEul = new IdolModel("가을", 2004);
const ray = new FemaleIdolModel("레이", 2004);

console.log(gaEul.__proto__);
console.log(gaEul.__proto__ === IdolModel.prototype);
console.log(Object.getPrototypeOf(gaEul) === IdolModel.prototype);

console.log(gaEul.sayHello());
console.log(ray.dance());
// console.log(ray.sayHello()) // 당연히 안됨. sayHello가 없으니까
console.log(Object.getPrototypeOf(ray) === FemaleIdolModel.prototype);
Object.setPrototypeOf(ray, IdolModel.prototype);
console.log(ray.sayHello()); // 프로토타입 체인을 바꿔서 이제 sayHello 가능
console.log(ray.constructor === IdolModel); // true 프로토를 바꿔서 IdolModel로 바뀜
console.log(Object.getPrototypeOf(ray) === FemaleIdolModel.prototype); // false 원래 프로토타입과 연결이 끊김
console.log(Object.getPrototypeOf(ray) === IdolModel.prototype); // true
console.log(FemaleIdolModel.prototype === IdolModel.prototype); // false
// FemaleIdolModel의 프로토타입은 그대로지만, FemaleIdolModel과 ray객체의 연결만 끊긴거

// 함수의 프로토타입 변경
FemaleIdolModel.prototype = IdolModel.prototype;
const eSeo = new FemaleIdolModel("이서", 2007);
console.log(Object.getPrototypeOf(eSeo) === FemaleIdolModel.prototype); // true
console.log(FemaleIdolModel.prototype === IdolModel.prototype); // true
