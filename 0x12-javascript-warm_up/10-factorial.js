#!/usr/bin/node
const arg = parseInt(process.argv[2]);

function factorial (a) {
  if (isNaN(a) || a === 1) {
    return 1;
  } else if (a === 0) {
    return 0;
  } else {
    return a * factorial(a - 1);
  }
}

console.log(factorial(arg));
