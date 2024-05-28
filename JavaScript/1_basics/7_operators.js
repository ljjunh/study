/**
 * Operators
 * 연산자
 */

/**
 * 산술 연산자
 * 1) 덧셈
 * 2) 뺄셈
 * 3) 곱셈
 * 4) 나눗셈
 * 5) 나머지
 */
console.log(10 + 10);
console.log(10 - 10);
console.log(10 * 10);
console.log(10 / 10);
console.log(10 % 10);
console.log(10 % 3);
console.log("-----------");

console.log(10 * (10 + 10));

/**
 * 증감연산자
 */
let number = 1;
number++;
console.log(number);

number--;
console.log(number);
console.log("-------------");
/**
 * 연산자의 위치
 */
let result = 1;
console.log(result);
result = number++; //number를 먼저 result에 대입하고 증감연산자 수행
console.log(result, number);

result = number--;
console.log(result, number);

result = ++number;
console.log(result, number);

result = --number;
console.log(result, number);

/**
 * 숫자 타입이 아닌 타입에 +, -를 사용하면?
 */
let sample = "99";
console.log(+sample);
console.log(typeof +sample);
console.log(sample);
console.log(typeof sample);

sample = true;
console.log(+sample);
console.log(typeof +sample);

sample = false;
console.log(+sample);
console.log(typeof +sample);

sample = "안유진";
console.log(+sample); //NaN -> Not a Number

/**
 * 할당 연산자 (assignment operator)
 */
number = 100;
console.log(number);

number += 10;
console.log(number);

number -= 10;
console.log(number);

number *= 10;
console.log(number);

number /= 10;
console.log(number);

number %= 10;
console.log(number);

/**
 * 비교 연산자
 * 1) 값의 비교
 * 2) 값과 타입의 비교
 */
console.log(5 == 5); // true
console.log(5 == "5"); // true
console.log(0 == ""); // true
console.log(true == 1); // true
console.log(true == "1"); // true
console.log(false == 0); // true

console.log(5 === 5); // true
console.log(5 === "5"); // false
console.log(0 === ""); // false
console.log(true === 1); // false
console.log(true === "1"); // false
console.log(false === 0); // false

console.log("-------------------");
console.log(5 != 5); // false
console.log(5 != "5"); // false
console.log(0 != ""); // false
console.log(true != 1); // false
console.log(true != "1"); // false
console.log(false != 0); // false

console.log("-------------------");
console.log(5 !== 5); // false
console.log(5 !== "5"); // true
console.log(0 !== ""); // true
console.log(true !== 1); // true
console.log(true !== "1"); // true
console.log(false !== 0); // true

console.log("------------------");
/**
 * 대소 관계 비교 연산자
 */
console.log(100 > 1);
console.log(100 < 1);
console.log(100 <= 1);
console.log(100 >= 1);

/**
 * 삼항 조건 연산자 (ternary operator)
 */
console.log(10 > 0 ? "10이 0보다 크다" : "10이 0보다 작다");

/**
 * 논리 연산자
 * 1) &&
 * 2) ||
 */

// && 조건은 모두 true여야 true를 반환
console.log(true && true);
console.log(true && false);
console.log(false && true);
console.log(false && false);
console.log("---------------------------");

// ||조건은 둘중 하나만 true 여도 true를 반환
console.log(true || true);
console.log(true || false);
console.log(false || true);
console.log(false || false);
console.log("---------------------------");

/**
 * 단축평가 (short circuit eevaluation)
 *
 * &&를 사용했을때 좌측이 true면 우측 값 반환
 * &&를 사용했을때 좌측이 false면 좌측 값 반환
 * ||를 사용했을때 좌측이 true면 좌측 값 반환
 * ||를 사용했을때 좌측이 false면 우측 값 반환
 */
console.log(true || "아이브");
console.log(false || "아이브");
console.log(false && "아이브");
console.log(true && "아이브");
console.log(true && true && "아이브");
console.log("------------------------");
/**
 * 지수 연산자
 */
console.log(2 ** 2);
console.log(10 ** 3);
console.log("---------------------------");

/**
 * null 연산자
 */
let name;
console.log(name);

name = name ?? "코드팩토리"; //좌측 값이 null or undefined 일 경우 우측 값 저장
console.log(name);

name = name ?? "아이브"; //좌측 값이 이미 할당되었기 때문에 ??의 우측값을 저장하지 않음
console.log(name);

let name2;
name2 ??= "코드팩토리";
console.log(name2);
