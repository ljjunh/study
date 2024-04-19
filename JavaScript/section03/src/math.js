// math모듈

export function add(a, b) {
  //function 앞에 export붙여도 됨
  return a + b;
}

export function sub(a, b) {
  return a - b;
}

export default function multiply(a, b) {
  // default붙이면, import 할 때 중괄호 없이 가능
  return a * b;
}
// common JS
// module.exports = {
//   add,
//   sub,
// };
// export { add, sub }; //Esmodule 이렇게 사용해도 되고
