// number
let num1: number = 123;
// 타입 어노테이션(주석)
// 변수 이름 뒤에 :을써서 타입을 지정
let num2: number = -123;
let num3: number = 0.123;
let num4: number = -0.123;
let num5: number = Infinity;
let num6: number = -Infinity;
let num7: number = NaN;

// string
let str1: string = "hello";
let str2: string = "hello";
let str3: string = `hello`;
let str4: string = `hello ${num1}`;

// boolean
let bool1: boolean = true;
let bool2: boolean = false;

// null
let null1: null = null;

// undefined
let unde1: undefined = undefined;

// 초기값을 null로 할당 하고 싶으면
// tsconfig.json에 strictNullChecks:false (엄격한 null 검사)

// 리터럴 타입
let numA: 10 = 10;
let strA: "hello" = "hello";
let boolA: true = true;
// 변수의 타입을 값 그 자체로 지정
