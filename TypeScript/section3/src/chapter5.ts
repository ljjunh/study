// 타입 추론
// 모든 상황에서 타입을 정확히 추론하지는 못함

// 일반적인 변수 선언의 경우 초기값을 기준으로 타입이 잘 추론 됨
let b = "hello"; // string 타입으로 추론
let a = 10; // number 타입으로 추론
let c = {
  // id, name, profile, urls 프로퍼티가 있는 타입으로 추론
  id: 1,
  name: "임준희",
  profile: {
    nickname: "asdf",
  },
};

let { id, name, profile } = c;
let [one, two, three] = [1, "hello", true];

// 함수의 반환값 타입을 추론할 때는 초기화하는
// 값이 아니라 return문 뒤의 반환값 기준으로 추론
function func(message = "hello") {
  return "hello";
}

let d; // 초기값 없이 변수를 선언하면 암묵적 any타입으로 추론 아무거나 넣을 수 있음
d = 10; // number
d.toFixed();

d = "hi"; // string
d.toUpperCase();
// 이렇게 초기값을 지정하지 않으면 타입이 진화한다는건 알겠는데, 쓰지는 말자

const num = 10; // number가 아니라 10 리터럴타입으로 지정됨
// 상수는 초기화 때 설정한 값을 변경할 수 없기 때문에 특별히 가장 좁은 타입으로 추론 됨

// 모든 배열요소들의 타입을 비교해서 최적의 공통 타입으로 추론해줌
let arr = [1, "string"]; // (number | string)[] 타입으로 추론

// 타입을 추론할 때 상수는 리터럴타입으로 딱
// 변수는 범용적으로 사용할 수 있도록 더 넓은 타입으로 추론해줌(타입 넓히기)
