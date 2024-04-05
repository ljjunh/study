// 5가지 요소 순회 및 탐색 메서드
// 1. forEach
// 배열의 모든 요소를 순회하면서, 각각의 요소에 특정 동작을 수행시키는 메서드
let arr1 = [1, 2, 3];

arr1.forEach(function (item, idx, arr) {
  //   console.log(idx, item * 2, arr);
});

let doubledArr = [];

arr1.forEach((item) => {
  doubledArr.push(item * 2);
});
// console.log(doubledArr);

// 2. includes
// 배열에 특정 요소가 있는지 확인하는 메서드
let arr2 = [1, 2, 3];
let isInclude = arr2.includes(4);
// console.log(isInclude);

// 3. indexOf
// 얕은 비교
// 특정 요소의 인덱스를 반환, 없으면 -1 반환
// 찾는 요소가 여러개면 제일 앞의 인덱스를 반환
let arr3 = [1, 1, 1, 3];
let index = arr3.indexOf(1);
// console.log(index);

// 4. findIndex
// 모든 요소를 순회하면서, 콜백함수를 만족하는 특정 요소의 인덱스(위치)를 반환하는 메서드
// 콜백함수를 만족하는 요소가 없으면 -1을 반환
let arr4 = [1, 2, 3];
const findedIndex = arr4.findIndex((item) => {
  if (item % 2 !== 0) return true;
});
console.log(findedIndex);

let objectArr = [{ name: "김민수" }, { name: "임준희" }];
console.log(objectArr.indexOf({ name: "임준희" }));
// -1이 출력됨. 못찾음
// indexOf는 얕은비교로 동작해서 그럼
// 객체값들은 참조값을 기준으로 비교되서 프로퍼티를 기준으로 비교안되서 그럼
// 그래서 findIndx가 있는거임
console.log(objectArr.findIndex((item) => item.name === "임준희"));

// 5. find
// 모든 요소를 순회하면서 콜백함수를 만족하는 요소를 찾는데, 인덱스가 아니라 요소를 반환
let arr5 = [{ name: "임준희" }, { name: "오승환", age: 26 }];
const finded = arr5.find((item) => item.name === "오승환");
console.log(finded);

// 일단 const 넣고 나중에 변경해야 할 때 let으로 바꾸면 됨
