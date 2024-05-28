/**
 * Loops
 *
 * 1) for
 * 2) while
 */
for (let i = 0; i < 10; i++) {
  console.log(i);
}
console.log("------------");
for (let i = 10; i > 0; i--) {
  console.log(i);
}
console.log("--------------");

for (let i = 0; i < 3; i++) {
  for (let j = 3; j > 0; j--) {
    console.log(i, j);
  }
}

// *을 이용해서 6x6의 정사각형을 출력해라
let square = "";
let side = 6;

for (let i = 0; i < side; i++) {
  for (let j = 0; j < side; j++) {
    square += "*";
  }
  square += "\n";
}
console.log(square);
console.log("---------------");
/**
 * for ...in
 * object에서는 key값
 * array에서는 index
 */
const yuJin = {
  name: "안유진",
  year: 2003,
  group: "아이브",
};
for (let key in yuJin) {
  console.log(key, yuJin[key]);
}
console.log("----------------------");
const iveMembersArray = ["안유진", "가을", "레이", "장원영", "리즈", "이서"];
for (let key in iveMembersArray) {
  console.log(`${key}:${iveMembersArray[key]}`);
}

/**
 * for ... of
 * array에서 사용시 값이 나옴
 */
for (let value of iveMembersArray) {
  console.log(value);
}

/**
 * while
 */
let number = 0;
while (number < 10) {
  number++;
  console.log(number);
}

/**
 * do...while
 * 먼저 do의 코드를 실행하고 while의 조건을 판단
 * 안쓰는거 추천
 */
number = 0;
do {
  number++;
} while (number < 10);
console.log(number);
console.log("-------------------");
/**
 * break
 */
for (let i = 0; i < 10; i++) {
  if (i === 5) {
    break;
  }
  console.log(i);
}
console.log("----------------");

number = 0;
while (number < 10) {
  if (number === 5) {
    break;
  }
  number++;
  console.log(number);
}

/**
 * continue
 * continue를 만나면 그 반복을 스킵함
 */
for (let i = 0; i < 10; i++) {
  if (i === 5) {
    continue;
  }
  console.log(i);
}
console.log("-------------");

number = 0;
while (number < 10) {
  number++;
  if (number === 5) {
    continue;
  }
  console.log(number);
}
