/**
 * Async / Await
 */
const getPromise = (seconds) =>
  new Promise((resolve, reject) => {
    setTimeout(() => {
      reject("에러");
    }, seconds * 1000);
  });

async function runner() {
  try {
    const result1 = await getPromise(1);
    console.log(result1);
    const result2 = await getPromise(2);
    console.log(result2);
  } catch (e) {
    console.log(e);
  } finally {
    console.log("---finally---");
  }
}
runner();
console.log("실행 끝"); // 먼저출력. await했을때 스레드를 막고 있지 않음
