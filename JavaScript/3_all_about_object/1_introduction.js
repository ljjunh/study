/**
 * All about objects
 *
 * 객체를 선언할 때 사용 할 수 있는 방법들
 * 1) object를 생성해서 객체 생성 - 기본기 {}
 * 2) class를 인스턴스화 해서 생성 - clas와 OOP
 * 3) function을 사용해서 객체 생성
 */

const yuJin = {
  // 1번 방법
  name: "안유진",
  year: 2003,
};
console.log(yuJin);

class IdolModel {
  name;
  year;
  constructor(name) {
    this.name = name;
    this.year = this.year;
  }
}
const yuJin2 = new IdolModel("안유진", 2003); // 2번 방법
console.log(yuJin2);

// 3번 생성자 함수
function IdolFunction(name, year) {
  this.name = name;
  this.year = year;
}
const gaEul = new IdolFunction("가을", 2002);
console.log(gaEul);
