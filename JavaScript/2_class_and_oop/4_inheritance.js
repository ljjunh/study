class IdolModel {
  name;
  year;

  constructor(name, year) {
    this.name = name;
    this.year = year;
  }
}

class FemaleIdolModel extends IdolModel {
  dance() {
    return "여자 아이돌이 춤을 춥니다.";
  }
}

class MaleIdolMoedl extends IdolModel {
  sing() {
    return "남자 아이돌이 노래를 부릅니다.";
  }
}

// 부모한테 상속받은 constructor를 그대로 사용 가능
const yuJin = new FemaleIdolModel("안유진", 2003);
console.log(yuJin);

const jiMin = new MaleIdolMoedl("지민", 1995);
console.log(jiMin);

console.log(yuJin.dance());
console.log(yuJin.name);

console.log(jiMin.sing());
console.log(jiMin.year);

const cf = new IdolModel("코드팩토리", 1992);
console.log(cf);
console.log(cf.name);
// console.log(cf.dance()); // 자식 프로퍼티는 부모가 사용x

console.log(yuJin instanceof IdolModel); // true 자식은 부모의 인스턴스다
console.log(yuJin instanceof FemaleIdolModel); // true
console.log(yuJin instanceof MaleIdolMoedl); // false 형제끼리는 아무 관계 없음
