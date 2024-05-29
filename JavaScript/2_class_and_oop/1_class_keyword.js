/**
 * Class Keyword
 * 클래스는 객체지향 프로래밍에서 특정 객체(인스턴스)를 생성하기 위한 변수와 메소드(함수)를 정의하는 일종의 틀이다.
 * 정보를 일반화해서 정리하는 방법이라고 생각하면 됨
 */
class IdolModel {
  name; // JS에선 이렇게 프로퍼티를 정의하는게 옵션임 근데 명시적으로 정의하는게 좋음
  year;
  // constructor - 생성자
  constructor(name, year) {
    this.name = name;
    // class 내의 name , 전달받은 name
    this.year = year;
  }
  //메서드 정의
  sayName() {
    return `안녕하세요 저는 ${this.name}입니다.`;
  }
}

const yuJin = new IdolModel("안유진", 2003);
console.log(yuJin);
const wonYoung = new IdolModel("장원영", 2004);
console.log(wonYoung);

console.log(yuJin.name); // 똑같이 프로퍼티 접근 가능

console.log(yuJin.sayName());
console.log(wonYoung.sayName());

console.log(typeof IdolModel); // function
console.log(typeof wonYoung); // object
