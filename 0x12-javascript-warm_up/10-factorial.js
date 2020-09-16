#!/usr/bin/node
const args = process.argv;

function factorial (num) {
  if (num === 0 || isNaN(num)) {
    return 1;
  } else {
    return (num * factorial(num - 1));
  }
}

console.log(factorial(parseInt(args[2])));
