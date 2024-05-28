/**
 * Variable 선언하기
 *
 * 1) var - 더이상 쓰지 않는다.
 * 2) let -
 * 3) const -
 */
var name = "코드";
console.log(name);

var age = 20;
console.log(age);

let ive = "아이브";
console.log(ive);

/**
 * let과 var로 선언하면
 * 값을 추후에 변경할 수 있음
 */
ive = "장원영";
console.log(ive);

/**
 * const로 선언하면
 * 값을 추후에 변경 불가능
 */
const newJeans = "뉴진스";
console.log(newJeans);

// newJeans = "아일릿";

/**
 * 선언과 할당
 */
var name2; // 변수를 선언하는 것
name2 = "코드"; // 할당
console.log(name2);

let girlFriend; //선언(할당을 안하면 초기값이 undefined 할당)
console.log(girlFriend); // 선언만 하고 할당을 안했으니까 undefined

// const girlFriend2; // const는 선언만 하는건 불가(나중에 값을 못바꾸니까)
