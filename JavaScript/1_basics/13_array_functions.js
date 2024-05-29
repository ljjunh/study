/**
 * Array Functions
 */
let iveMembers = ["장원영", "안유진", "가을", "레이", "리즈", "이서"];
console.log(iveMembers);

// push() 배열의 마지막에 값 추가, 반환값 : 추가 한 뒤 배열의 길이
console.log(iveMembers.push("임준희"));
console.log(iveMembers);
console.log("-------------------");

// pop() 배열의 마지막 값 삭제, 반환값 : 삭제 한 엘리먼트 반환
console.log(iveMembers.pop());
console.log(iveMembers);
console.log("-------------------");

// shift() 배열의 첫번째 값 삭제, 반환값 : 삭제 한 엘리먼트 반환
console.log(iveMembers.shift());

// unshift() 배열의 맨 앞에 추가, 반환값 : 추가 한 뒤 배열의 길이
console.log(iveMembers.unshift("장원영"));
console.log(iveMembers);
console.log("-------------------");

// splice(시작값, 몇개 삭제할지) 반환값 : 삭제 한 엘리먼트 반환, 원본 배열에 영향o
console.log(iveMembers.splice(0, 3));
console.log(iveMembers);

// 지금까지는 배열 원본에 영향을 줘서 사용하는거 추천x
console.log("-------------------");
iveMembers = ["장원영", "안유진", "가을", "레이", "리즈", "이서"]; // 초기화
console.log(iveMembers);

// 여기부터는 원본 배열에 영향x 이걸 사용해야됨
// concat() push와 같이 배열의 맨 뒤에 추가하지만 원본에 영향x 새로운 배열을 만들어 반환
console.log(iveMembers.concat("임준희"));

// slice(시작 인덱스, 몇번 인덱스까지 삭제할지) 0,3쓰면 0, 1, 2 지워짐
// splice랑 비슷하지만 원본 배열에 영향 x
console.log(iveMembers.slice(0, 3));
console.log(iveMembers);
console.log("-------------");

// spread operator
let iveMembers2 = [...iveMembers];
console.log(iveMembers2);

// join() 값들을 string으로 엮을때 사용
console.log(iveMembers.join());
console.log(iveMembers.join("/"));

// sort() 반환값x, 원본 배열에 영향o
// 오름차순
iveMembers.sort();
console.log(iveMembers);
// 내림차순
console.log(iveMembers.reverse());

let numbers = [1, 9, 7, 5, 3];
console.log(numbers);
// a, b를 비교했을때
// 1) a를 b보다 나중에 정렬하려면 (뒤에 두려면) 0 보다 큰 숫자를 반환
// 2) a를 b보다 먼저 정렬하려면 (앞에 두려면) 0 보다 작은 숫자를 반환
// 3) 원래 순서를 그대로 두려면 0을 반환
numbers.sort((a, b) => {
  return a > b ? 1 : -1;
});
console.log(numbers);

numbers.sort((a, b) => (a > b ? -1 : 1));
console.log(numbers);

// map() array의 모든 값을 순회, 새로운 배열 반환, 원본에 영향x
console.log("--------------");
console.log(iveMembers.map((x) => `아이브: ${x}`));

// filter()
numbers = [1, 8, 7, 6, 3];
console.log(numbers.filter((x) => x % 2 === 0));

// find() 가장 첫번째로 해당되는 값만 반환
console.log(numbers.find((x) => x % 2 === 0));

// findIndex() 가장 첫번째로 해당되는 값의 인덱스 반환
console.log(numbers.findIndex((x) => x % 2 === 0));

// reduce()
console.log(numbers.reduce((p, n) => p + n, 0));
