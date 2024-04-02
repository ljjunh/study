// 1. null 병합 연산자
// -> 존재하는 값을 추려내는 기능
// -> null이나 undefined가 아닌 값을 찾아내는 연산자

let var1;
let var2 = 10;
let var3 = 20;

let var4 = var1 ?? var2;
console.log(var4);
let var5 = var2 ?? var3;
console.log(var5); //둘다 null이나 undefined가 아니면 앞의 값을 할당

let userName = "임준희";
let userNickName = "junhee";
let displayName = userName ?? userNickName;
console.log(displayName);

// 2. typeof 연산자
// -> 값의 타입을 문자열로 반환하는 기능을 하는 연산자
let var7 = 1;
var7 = "hello";
// js에서는 숫자값으로 변수를 초기화 했더라도, 해당 변수에 다른 자료형을 넣어주는게 가능하다. 그래서 변수의 타입이 고정되어 있지 않고, 코드 실행에 따라서 동적으로 바뀐다.
// 이 때 현재 변수에 저장된 값의 타입이 궁금하면 typeof 연산자를 사용하면 된다.
console.log(typeof var7); // string

// 3. 삼항 연산자
// -> 항을 3개 사용하는 연산자
// -> 조건식을 이용해서 참, 거짓일 때의 값을 다르게 반환
let var8 = 10;
// 요구사항 : 변수 res에 var8의 값이 짝수 -> "짝", 홀수 -> "홀"
let res = var8 % 2 === 0 ? "짝수" : "홀수";
console.log(res);
