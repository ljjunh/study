/**
 * Async theory
 */

// 동기
// function longWork() {
//   const now = new Date();
//   /**
//    * milliseconds since epoch
//    * 1970년도 1월 1일부터 지금까지의 시간을
//    * 밀리초로 반환
//    */
//   const milliseconds = now.getTime();
//   const afterTwoSecondes = milliseconds + 2 * 1000;

//   while (new Date().getTime() < afterTwoSecondes) {}
//   console.log("완료");
// }

// console.log("Hello");
// longWork();
// console.log("World");

// 비동기
function longWork() {
  setTimeout(() => {
    console.log("완료");
  }, 2000);
}
console.log("Hello");
longWork();
console.log("Work");
