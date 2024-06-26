// enum 타입
// 여러가지 값들에 각각 이름을 부여해 열거해두고 사용하는 타입

enum Role {
  //   ADMIN = 0,
  //   USER = 1,
  //   GUEST = 2,

  // 숫자할당을 안하면 위에서부터 0,1,2로 자동지정
  ADMIN,
  USER,
  GUEST,
}
enum Language {
  korean = "ko",
  english = "en",
}

// 프로그래머가 헷갈리지 않도록 숫자분류를 도와줌
const user1 = {
  name: "장원영",
  role: Role.ADMIN, // 0 <= 관리자
  language: Language.korean,
};
const user2 = {
  name: "안유진",
  role: Role.USER, // 1 <= 일반유저
};
const user3 = {
  name: "레이",
  role: Role.GUEST, // 2 <= 게스트
};
console.log(user1, user2, user3);
