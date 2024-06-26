// number
let num1 = 123;
// 타입 어노테이션(주석)
// 변수 이름 뒤에 :을써서 타입을 지정
let num2 = -123;
let num3 = 0.123;
let num4 = -0.123;
let num5 = Infinity;
let num6 = -Infinity;
let num7 = NaN;
// string
let str1 = "hello";
let str2 = "hello";
let str3 = `hello`;
let str4 = `hello ${num1}`;
// boolean
let bool1 = true;
let bool2 = false;
// null
let null1 = null;
// undefined
let unde1 = undefined;
// 초기값을 null로 할당 하고 싶으면
// tsconfig.json에 strictNullChecks:false (엄격한 null 검사)
// 리터럴 타입
let numA = 10;
let strA = "hello";
let boolA = true;
export {};
// 변수의 타입을 값 그 자체로 지정
