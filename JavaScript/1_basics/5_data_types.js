/**
 * Data Types
 *
 * 6개의 Primitive Type과
 * 1개의 Object Type이 있다.
 *
 * 1) Number(숫자)
 * 2) String(문자열)
 * 3) Boolean(불리언)
 * 4) undefined(언디파인드)
 * 5) null(널)
 * 6) Symbol(심볼)
 *
 * 7) Object(객체)
 *      Function
 *      Array
 *      Object
 */

// Number
const age = 32;
const tempature = -10;
const pi = 3.14;
console.log(typeof age);
console.log(typeof tempature);
console.log(typeof pi);
console.log("-------------");

const infinity = Infinity;
const nInfinity = -Infinity;

console.log(typeof infinity);
console.log(typeof nInfinity);
console.log("-------------");

// String
const codeFactory = '"코드"팩토리';
console.log(codeFactory);
console.log(typeof codeFactory);

const ive = "'아이브'장원영";
console.log(ive);
console.log("-------------");

/**
 * Template Literal
 * Escaping Caracter
 * 1) newLine -> \n
 * 2) tab -> \t
 * 3) 백슬래시를 스트링으로 표현하고싶으면 두번 입력
 */
const iveYuJin = "아이브\n안유진";
console.log(iveYuJin);
const iveWonYoung = "아이브\t장원영";
console.log(iveWonYoung);
const backSlash = "아이브\\리즈";
console.log(backSlash);

const iveWonYoung2 = `아'이'\\브
장/원/영`;
console.log(iveWonYoung2);
const groupName = "아이브";
console.log(groupName + "안유진");
console.log(`${groupName}안유진`);

// Boolean

const isTrue = true;
const isFalse = false;
console.log(typeof isTrue);
console.log(typeof isFalse);

/**
 * undefined
 * 사용자가 직접 값을 초기화하지 않았을때 지정되는 값
 *
 * 직접 undefined로 값을 초기화하는건 지양
 */
let noInit;
console.log(noInit);
console.log(typeof noInit);

/**
 * null 타입
 *
 * undefined와 마찬가지로 값이 없다는 뜻이나
 * JS에서는 개발자가 명시적으로 없는 값으로 초기화할때 사용된다
 */
let init = null;
console.log(init);
console.log(typeof null); //object로 나오는데 버그임
console.log("-----------------------");
/**
 * Symbol 타입
 * 유일무이한 값을 생성할때 사용
 * 다른 프리미티브 값들과 다르게 Symbol 함수를
 * 호출해서 사용한다.
 */
const test1 = "1";
const test2 = "1";
console.log(test1 === test2);

const symbol1 = Symbol("1");
const symbol2 = Symbol("1");
console.log(symbol1 === symbol2); //false
// 같은 값을 넣어도 false 반환
// 넣은 값은 보존되지만 유일무이한 값으로 인식

/**
 * Object 타입
 * key:value 쌍으로 이루어져있다.
 */
const dictionary = {
  red: "빨간색",
  orange: "주황색",
  yellow: "노란색",
};
console.log(dictionary);
console.log(dictionary["red"]);
console.log(dictionary["orange"]);
console.log(dictionary.yellow);
console.log(typeof dictionary);

/**
 * Array 타입
 * 값을 리스트로 나열 할 수 있는 타입
 * index 0부터 시작
 */
const iveMembersArray = ["안유진", "가을", "레이", "리즈", "이서", "장원영"];
console.log(iveMembersArray);
console.log(iveMembersArray[0]);
console.log(iveMembersArray[5]);
iveMembersArray[0] = "유진";
console.log(iveMembersArray[0]);
console.log(typeof iveMembersArray);

/**
 * static typing -> 변수를 선언할때 어떤 타입의 변수를 선언할지 명시한다.
 *
 * dynamic typing -> 변수의 타입을 명시적으로 선언하지 않고 갑에 의해 타입을 추론한다.
 * JS -> dynamic typing
 */
