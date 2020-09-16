#!/usr/bin/node
const args = process.argv;
let big = args[2];
let big2 = 0;

args.forEach(element => {
  if (element > big) {
    big2 = big;
    big = element;
  }
});

console.log(big2);
