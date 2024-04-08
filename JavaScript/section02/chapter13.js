const promise = new Promise((resolve, reject) => {
  // 비동기 작업을 실행하는 함수(executor)
  setTimeout(() => {
    console.log("안녕");
  }, 2000);
});

console.log(promise);
