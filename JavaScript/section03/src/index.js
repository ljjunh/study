// const { add, sub } = require("./math"); //common JS
import mul, { add, sub } from "./math.js"; //ESmodule
import randomColor from "randomcolor";

const color = randomColor();
console.log(color);

// console.log(add(1, 2));
// console.log(sub(1, 2));
// console.log(mul(1, 2));
