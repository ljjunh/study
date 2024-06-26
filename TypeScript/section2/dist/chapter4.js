let user = {
    id: 1,
    name: "임준희",
    nickname: "junhee",
    bio: "안녕하세요",
    location: "광주",
};
let user2 = {
    id: 2,
    name: "준희",
    nickname: "junhee",
    bio: "안녕하세요",
    location: "광주",
};
let countryCodes = {
    Korea: "ko",
    UnitedState: "us",
    UnitedKingdom: "uk",
};
// 인덱스 시그니처는 규칙을 위반하지 않으면 ㄱㅊ
// 그래서 아무것도 안써도 규칙을 위반한게 아니라 오류 안남
let countryNumberCodes = {
    Korea: 410,
    UnitedState: 840,
    UnitedKingdom: 826,
};
export {};
