// 5가지 배열 변형 메서드
// 1. filter
// 기존 배열에서 조건을 만족하는 요소들만 필터링하여 새로운 배열로 반환
let arr1 = [
  { name: "임준희", hobby: "풋살" },
  { name: "이명욱", hobby: "테니스" },
  { name: "오승환", hobby: "게임" },
  { name: "최재원", hobby: "게임" },
];

const gamePeople = arr1.filter((item) => item.hobby === "게임");
// console.log(gamePeople);

// 2. map
// 배열의 모든 요소를 순회하면서 각각 콜백함수를 실행하고 그 결과값들을 새로운 배열로 반환
let arr2 = [1, 2, 3];
const mapResult1 = arr2.map((item, idx, arr) => {
  return item * 2;
});
// console.log(mapResult1);

let names = arr1.map((item) => item.name);
// console.log(names);

// 3. sort
// 배열을 사전순으로 정렬하는 메서드
// 숫자의 대소비교를 통해 정렬하는게 아닌, 그냥 사전순으로 정렬
let arr3 = [10, 5, 3, 7, 1, 6];
arr3.sort();
console.log(arr3);
// 대소관계를 기준으로 정렬하고싶으면 콜백함수를 같이 사용해야 함
arr3.sort((a, b) => {
  if (a > b) {
    //b가 a 앞에 와라
    return 1; // 양수 반환시 b, a 배치
  } else if (a < b) {
    // a가 b 앞에 와라
    return -1; // 음수 반환시 a, b 배치
  } else {
    // 두 값의 자리를 바꾸지 마라
    return 0; // 0 반환시 a, b 자리를 그대로 유지
  }
});
console.log(arr3);

// 4. toSorted (최근에 추가된 최신 함수)
// 원본배열은 놔두고 새로운 배열을 반환
let arr5 = ["c", "a", "b"];
const sorted = arr5.toSorted();

console.log(arr5);
console.log(sorted);

// 5. join
// 배열의 모든 요소를 하나의 문자열로 합쳐서 반환하는 메서드
let arr6 = ["hi", "im", "junhee"];
const joined = arr6.join(" "); // 구분자 변경 가능
console.log(joined);
