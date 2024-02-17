#!/usr/bin/node
function factorial (a) {
  let x = 1;
  if (isNaN(+a) === true) {
    return 1;
  } else {
    for (let i = 1; i <= +a; i++) {
      x *= i;
    }
    return x;
  }
}
console.log(factorial(process.argv[2]));
