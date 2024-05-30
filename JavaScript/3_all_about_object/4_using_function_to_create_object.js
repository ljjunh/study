/**
 * Using function to create objects
 */

// 생성자 함수
function IdolModel(name, year) {
  if (!new.target) {
    return new IdolModel(name, year);
  } // new 키워드 까먹을때도 제대로 돌아가도록 new 붙여서 재호춣해줌

  this.name = name;
  this.year = year;

  this.dance = function () {
    return `${this.name}이 춤을 춥니다.`;
  };
}
const yuJin = new IdolModel("안유진", 2003);
console.log(yuJin);
console.log(yuJin.dance());
const yuJin2 = IdolModel("안유진", 2003);
console.log(yuJin2); // undefined
// new 키워드없이 그냥 함수 쓰듯이 쓰면 return값이 없기 때문에 undefined가 반환됨
// 그럼 name이랑 year는 어디로 갔나
// console.log(global.name); // 안유진
// new 키워드를 안썻기 때문에 생성자 함수 안의 this가 global에 붙어서 global로 들어간다. 하지마셈

//arrow function으로 생성자 함수 만들기
const IdolModelArrow = (name, year) => {
  this.name = name;
  this.year = year;
};
const yuJin3 = new IdolModelArrow("안유진", 2003);
// new 키워드는 arrowfunction에서 못씀 일반 function에서만 사용 가능
// new를 호출하면 새로운 객체가 생성되고 이 객체가 this로 바인딩 됨
// arrow function에서는 this가 없어서 부모스코프의 this를 받아서 쓰기 때문에
// arrow function에서는 new 키워드를 사용할 수 없음
// 생성자 함수를 사용하려면 일반함수를 써야함
