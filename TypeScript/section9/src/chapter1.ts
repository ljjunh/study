/**
 * 분산적인 조건부 타입
 */

type StringNumberSwitch<T> = T extends number ? string : number;

let a: StringNumberSwitch<number>;

let b: StringNumberSwitch<string>;

// 조건부타입에 유니온타입을 할당하면 그때부턴 분산적인 조건부 타입이 됨
let c: StringNumberSwitch<number | string>;
//let c: StringNumberSwitch<number | number>;
//let c: StringNumberSwitch<number | string>;
// 이렇게 두번 들어가고 분리된 결과를 유니온으로 묶어줌

let d: StringNumberSwitch<boolean | number | string>;
// 1단계
// StringNumberSwitch<boolean> |
// StringNumberSwitch<number> |
// StringNumberSwitch<string>

// 2단계
// number |
// string |
// number

// 결과
// number | string

/**
 * 실용적인 예제
 */

type Exclude<T, U> = T extends U ? never : T;

type A = Exclude<number | string | boolean, string>;
// 1단계
// Exclude<number, string> |
// Exclude<string, string> |
// Exclude<boolean, string>

// 2단계
// number |
// never |
// boolean

// 결과
// number | never | boolean
// never는 공집합인데, 유니온으로 합치면 never가 사라짐

type Extract<T, U> = T extends U ? T : never;
type B = Extract<number | string | boolean, string>;
// 1단계
// Extract<number, string> |
// Extract<string, string> |
// Extract<boolean, string>

// 2단계
// never |
// string |
// never

// 결과
// string
