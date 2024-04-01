// 1. Number Type
let num1 = 27;
let num2 = 1.5;
let num3 = -20;

let inf = Infinity;
let mInf = -Infinity;

let nan = NaN; // Not a Number 연산이 실패했을때 Nan반환
// console.log(1 * "hello"); // Nan

// 2. String Type
let myName = "임준희";
let myLocation = "광주";
let introduce = myName + myLocation;
// 문자열끼리 덧셈 연산 지원
let introduceText = `${myName}는 ${myLocation}에 거주합니다`;
//backtick(`)을 사용하면 $와{}를 통해 변수의 값을 동적으로 문자열에 포함시킬 수 있음(템플릿 리터럴 문법)

// 3. Boolean Type
// 소문자 true, false
let isSwitchOn = true;
let isEmpty = false;

// 4. Null Type(아무것도 없다)
let empty = null; // 변수에 어떠한 값도 없다를 표현할 때 사용
print(empty);

// 5. Undefined Type
let none; // 변수를 초기화하지 못했거나 존재하지 않는 값을 불러오려고 할 때 발생할 수 있음
