/**
 * Getter and Setter
 */
class IdolModel {
  name;
  year;

  constructor(name, year) {
    this.name = name;
    this.year = year;
  }
  // getter
  // 데이터를 가공해서 새로운 데이터를 반환할때
  // private한 값을 반환할때
  get nameAndYear() {
    return `${this.name}-${this.year}`;
  }

  // setter
  // 값을 새로 저장할 때
  // 파라미터를 무조건 한개만 받게 되어있음
  // setter를 쓰게되면 정의한 값을 변경하는거라서 자주 안씀
  set setName(name) {
    this.name = name;
  }
}

const yuJin = new IdolModel("안유진", 2003);
console.log(yuJin);
console.log(yuJin.nameAndYear);

yuJin.setName = "장원영";
console.log(yuJin);

class IdolModel2 {
  //private한 값을 정의할땐 # (ES7이상만 사용 가능)
  #name;
  year;

  constructor(name, year) {
    this.#name = name;
    this.year = year;
  }

  get name() {
    return this.#name;
  }
  set name(name) {
    this.#name = name;
  }
}
const yuJin2 = new IdolModel2("안유진", 2003);
console.log(yuJin2); //IdolModel2 { year: 2003 }
// private이라 access못함
// private값을 가져오려면 getter를 써야됨
console.log(yuJin2.name); //안유진 getter로 private값을 가져올 수 있음
// private값을 변경하려면 setter를 써야됨
yuJin2.name = "장원영";
console.log(yuJin2.name); // 장원영
