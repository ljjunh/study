/**
 * Super and Override
 */
class IdolModel {
  name;
  year;

  constructor(name, year) {
    this.name = name;
    this.year = year;
  }
  sayHello() {
    return `안녕하세요 ${this.name}입니다.`;
  }
}

class FemaleIdolModel extends IdolModel {
  // 부모에겐 없지만, 따로 더 받고싶은 인스턴스
  part;
  // constructor에 부모가 가지고있지 않은거 추가할땐 constructor 다시 설정
  // Override
  constructor(name, year, part) {
    super(name, year); // 부모의 constructor
    this.part = part;
  }
  // 부모의 메서드도 재정의 가능
  sayHello() {
    // return `안녕하세요 ${this.name}입니다. ${this.part}를 맡고있습니다.`;
    return `${super.sayHello()} ${this.part}를 맡고 있습니다`;
    // super로 함수는 실행 가능
  }
}
const yuJin = new FemaleIdolModel("안유진", 2003, "보컬");
console.log(yuJin); // FemaleIdolModel { name: '안유진', year: 2003, part: '보컬' }

const wonYoung = new IdolModel("장원영", 2002);
console.log(wonYoung);
console.log(wonYoung.sayHello());
console.log(yuJin.sayHello());
