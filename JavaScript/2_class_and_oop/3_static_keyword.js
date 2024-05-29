/**
 * Static Keyword
 */
class IdolModel {
  name;
  year;
  static groupName = "아이브"; //static을 쓰면 프로퍼티가 객체에 귀속되지 않음
  // 클래스 자체에 귀속됨

  constructor(name, year) {
    this.name = name;
    this.year = year;
  }

  static returnGroupName() {
    return "아이브";
  }
}

const yuJin = new IdolModel("안유진", 2003);
console.log(yuJin);
console.log(IdolModel);
console.log(IdolModel.returnGroupName());

/**
 * factory constructor
 */
class IdolModel2 {
  name;
  year;

  constructor(name, year) {
    this.name = name;
    this.year = year;
  }
  static fromObject(object) {
    return new IdolModel2(object.name, object.year);
  }

  static fromList(list) {
    return new IdolModel2(list[0], list[1]);
  }
}
const yuJin3 = IdolModel2.fromObject({
  name: "안유진",
  year: 2003,
});
console.log(yuJin3);

const yuJin4 = IdolModel2.fromList(["안유진", 2003]);
console.log(yuJin4);
