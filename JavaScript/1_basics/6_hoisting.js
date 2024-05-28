/**
 * Hoisting
 */
console.log("Hellow");
console.log("World");

/**
 * Hoisting은 무엇인가?
 * 모든 변수 선언문이 코드의 최상단으로 이동되는 것처럼 느껴지는 현상을 이야기한다.
 */

// console.log(name); // 1번
// var name = "코드팩토리";
// console.log(name);

// var name; // 2번
// console.log(name);
// name = "코드팩토리";
// console.log(name);
// 1번 코드가 2번 코드처럼 실행되는 느낌

// console.log(yuJin); //ReferenceError: Cannot access 'yuJin' before initialization
// let yuJin = "안유진";
// let의 호이스팅
// 선언, 할당 전에 yuJin을 찍어보면 cannot access before initialization이 뜬다.
// 즉, 호이스팅이 되긴 하지만 let이나 const로 선언한 변수가 할당 되기 전에 접근이 불가능 함

// console.log(yuJin); //ReferenceError: yuJin is not defined
// 선언, 할당 하지 않고 yuJin을 찍어보면 not defined가 뜬다.
