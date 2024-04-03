for (let idx = 0; idx <= 10; idx++) {
  if (idx % 2 === 0) {
    continue;
  }
  console.log(idx);
  if (idx >= 5) {
    console.log("멈춤");
    break;
  }
}
