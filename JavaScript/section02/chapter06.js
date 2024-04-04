// 1. 배열 순회
let arr = [1, 2, 3];

// 1.1. 배열 인덱스
for (let i = 0; i < arr.length; i++) {
  //   console.log(arr[i]);
}

let arr2 = [4, 5, 6, 7, 8];
for (let i = 0; i < arr2.length; i++) {
  //   console.log(arr2[i]);
}

// 1.2. for of 반복문
// -> 배열을 순회하기 위해서만 존재하는 반복문
let arr3 = [10, 20, 30];
for (let i of arr3) {
  console.log(i);
}

// 2. 객체 순회
let person = {
  name: "임준희",
  age: 29,
  hobby: "풋살",
};

// 2.1 Object.keys 사용
// -> 객체에서 key값들만 뽑이서 새로운 배열로 반환
let keys = Object.keys(person);
console.log(keys);
for (let i = 0; i < keys.length; i++) {
  console.log(keys[i]);
}
for (let i of keys) {
  const value = person[i];
  console.log(i, value);
}
// 2.2 Object.values 사용
// -> 객체에서 value 값들만 뽑아서 새로운 배열로 반환
let values = Object.values(person);
console.log(values);
for (let i = 0; i < values.length; i++) {
  console.log(values[i]);
}
for (let i of values) {
  console.log(i);
}
// 2.3 for in
for (let key in person) {
  const value = person[key];
  console.log(key, value);
}
// 객체를 순회할때는 for in, 배열을 순회할때는 for of
