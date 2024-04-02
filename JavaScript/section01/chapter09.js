// 1. if 조건문
// if문은 if로 시작해서 else로 끝나거나 if로 시작해서 else없이 끝나야 한다.
// else if로 시작하거나 끝나는게 불가능
let num = 4;

if (num >= 10) {
  console.log("num은 10 이상입니다.");
} else if (num >= 5) {
  console.log("num은 5 이상입니다.");
} else if (num >= 3) {
  console.log("num은 3 이상입니다.");
} else {
  console.log("num은 10 미만입니다.");
}

// 2. Switch 문
// -> if문과 기능 자체는 동일
// -> 다수의 조건을 처리할 때 if보다 더 직관적이다.
let animal = "11";

switch (animal) {
  case "cat": {
    console.log("고양이");
    break;
  }
  case "dog": {
    console.log("강아지");
    break;
  }
  case "bear": {
    console.log("곰");
    break;
  }
  case "snake": {
    console.log("뱀");
    break;
  }
  case "tiger": {
    console.log("호랑이");
    break;
  }
  default: {
    console.log("그런 동물은 없습니다.");
  }
}
