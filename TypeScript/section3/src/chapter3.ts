// 기본 타입간의 호환성
let num1: number = 10;
let num2: 10 = 10;
num1 = num2;

// 객체 타입간의 호환성
// 어떤 객체타입을 다른 객체타입으로 취급해도 괜찮은가?
type Animal = {
  name: string;
  color: string;
};

type Dog = {
  name: string;
  color: string;
  breed: string;
};

let animal: Animal = {
  name: "기린",
  color: "yellow",
};
let dog: Dog = {
  name: "짱구",
  color: "brown",
  breed: "포메",
};

animal = dog;
// dog = animal;

type Book = {
  //슈퍼타입
  name: string;
  price: number;
};

type ProgrammingBook = {
  //서브타입
  name: string;
  price: number;
  skill: string;
};

let book: Book;
let programingBook: ProgrammingBook = {
  name: "타입스크립트",
  price: 33000,
  skill: "typeScript",
};
book = programingBook; // 업캐스팅 가능
// programingBook = book; 다운캐스팅 불가능

// 초과 프로퍼티 검사
let book2: Book = {
  name: "타입스크립트",
  price: 33000,
  //   skill: "typeScript",
};

let book3: Book = programingBook;
// 초기화할때 객체리터럴을 사용하지 않아서 초과 프로퍼티검사가 발동안함

function func(book: Book) {}
// func({ name: "타입스크립트", price: 33000, skill: "typeScript" }); 객체리터럴 사용해서 초과 프로퍼티 검사 o
func(programingBook); //초과프로퍼티 검사 x
