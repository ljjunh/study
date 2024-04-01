// 1. 대입 연산자
// 이렇게 let var1 = 1처럼 변수의 값을 저장할 때 사용하는 가장 기초적인 연산자(변수 이름 = 저장할 값)
let var1 = 1;

// 2. 산술 연산자
let num1 = 3 + 2;
let num2 = 3 - 2;
let num3 = 3 * 2;
let num4 = 3 / 2;
let num5 = 3 % 2;

let num6 = (1 + 2) * 10;
console.log(num6);

// 3. 복합 대입 연산자
// 산술연산자와 대입 연산자가 복합되어 있다고 생각하면 됨
let num7 = 10;
//num7 = num7 + 20;
num7 += 20;
num7 -= 10;
num7 *= 5;
num7 /= 2;
num7 %= 3;
console.log(num7);

// 4. 증감 연산자
// 값을 1씩 늘리거나, 1씩 줄일 때 사용하는 연산자
let num8 = 10;
num8++; // 전위 연산
console.log(num8++); // 후위 연산
console.log(num8);

// 5. 논리 연산자
// Boolean타입의 값을 다룰 때 사용하는 연산자
let or = true || false;
let and = true && true;
let not = !true;
console.log(or, and, not);

//6. 비교 연산자
// 두개의 값을 서로 비교하는 연산자
let comp1 = 1 === 2;
let comp2 = 1 !== 2;
// 다른언어에서는 ==인데 왜 js에서는 ===씀?
// ==두개만 써서 비교하면 값의 자료형까지 같은지는 비교 안됨
let comp3 = 1 == "1"; //true
let comp4 = 1 === "1"; //false
console.log(comp1, comp2);
console.log(comp3, comp4);
