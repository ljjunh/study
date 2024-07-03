/**
 * 타입 단언
 * type assertion
 */
type Person = {
  name: string;
  age: number;
};
let person = {} as Person;
person.name = "asdfdfs";
person.age = 22;

type Dog = {
  name: string;
  color: string;
};

let dog = {
  name: "돌돌이",
  color: "brown",
  breed: "진도",
} as Dog;

/**
 * 타입 단언의 규칙
 * 단언식 : 값 as 단언
 * A as B
 * A가 B의 슈퍼타입이거나
 * A가 B의 서브타입이여야 함
 */

let num1 = 10 as never;
let num2 = 10 as unknown;

// let num3 = 10 as string; // number가 string의 슈퍼타입이나 서브타임이 아니여서 에러

/**
 * const 단언
 */
let num4 = 10 as const; // const처럼 number리터럴10이 됨

let cat = {
  name: "야옹이",
  color: "yellow",
} as const;
// 객체 뒤에 as const를 붙이면 모든 프로퍼티가 읽기전용이 됨
// cat.name="멍멍이" // 값 수정을 못함

/**
 * Non Null 단언
 * 어떤 값이 null이나 undefined가 아니라고 타입스크립트한테 알려주는 역할
 */
type Post = {
  title: string;
  author?: string;
};

let post: Post = {
  title: "게시글1",
  author: "임준희",
};

// author의 이름의 길이를 출력하려면
const len: number = post.author!.length;
// 옵셔널체이닝을 사용하면 undefined가 될수도있으니 number타입에 들어가면 에러남
// 이럴땐 non null 단언으로 !를 사용하면 됨
// ! : non, null이 아닐것이라고 믿게하는거
