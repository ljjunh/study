// 타입 별칭
// 동일 스코프 내의 여러개의 타입별칭 x
type User = {
  id: number;
  name: string;
  nickname: string;
  bio: string;
  location: string;
};
let user: User = {
  id: 1,
  name: "임준희",
  nickname: "junhee",
  bio: "안녕하세요",
  location: "광주",
};

let user2: User = {
  id: 2,
  name: "준희",
  nickname: "junhee",
  bio: "안녕하세요",
  location: "광주",
};

// 인덱스 시그니처
type CountryCodes = {
  [key: string]: string;
};
let countryCodes: CountryCodes = {
  Korea: "ko",
  UnitedState: "us",
  UnitedKingdom: "uk",
};

type CountryNumberCodes = {
  [key: string]: number;
  Korea: number; //만약 이렇게 꼭 있어야할 프로퍼티가 있으면 적어주면 됨
};
// 인덱스 시그니처는 규칙을 위반하지 않으면 ㄱㅊ
// 그래서 아무것도 안써도 규칙을 위반한게 아니라 오류 안남

let countryNumberCodes: CountryNumberCodes = {
  Korea: 410,
  UnitedState: 840,
  UnitedKingdom: 826,
};
