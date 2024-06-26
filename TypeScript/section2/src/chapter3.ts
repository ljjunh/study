// 객체
// 객체 리터럴 타입으로 프로퍼티의 타입도 지정
let user: {
  id?: number; // 물음표 붙이면 옵셔널 프로퍼티
  name: string;
} = {
  id: 1,
  name: "임준희",
};

// api키 처럼 수정되면 안되는 프로퍼티가 있으면
// readonly를 붙여서 읽기전용으로 만들기
let config: {
  readonly apiKey: string;
} = {
  apiKey: "My API KEY",
};
// config.apiKey = "바꿈";
