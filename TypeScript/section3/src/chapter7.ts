/**
 * 타입 좁히기
 * 조건문 등을 이용해 넓은타입에서 좁은타입으로
 * 타입을 상황에 따라 좁히는 방법
 */

type Person = {
  name: string;
  age: number;
};

// value => number : toFixed
// value => string : toUpperCase
// value => Date : getTime
// value => Person : name은 age살 입니다.
function func(value: number | string | Date | null | Person) {
  value; // string | number
  if (typeof value === "number") {
    // 넘버타입이 보장되서 타입 좁히기 됨
    console.log(value.toFixed()); // number
  } else if (typeof value === "string") {
    console.log(value.toUpperCase()); // string
  } else if (value instanceof Date) {
    // typeof로 쓰면 null도 통과되서 에러
    console.log(value.getTime());
  } else if (value && "age" in value) {
    console.log(`${value.name}은 ${value}살 입니다.`);
  }
}
