#!/usr/bin/node
const args = process.argv;
let big = parseInt(args[2]);
let big2 = 0;

args.forEach(element => {
  if (parseInt(element) > big) {
    big2 = big;
    big = parseInt(element);
  }
});

console.log(big2);
