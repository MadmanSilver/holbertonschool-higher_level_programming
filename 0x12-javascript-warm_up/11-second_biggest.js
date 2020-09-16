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

if (big === parseInt(args[2]) && args.length > 3) {
  big2 = parseInt(args[3]);
  args.forEach(element => {
    if (parseInt(element) !== big && parseInt(element) > big2) {
      big2 = parseInt(element);
    }
  });
}

console.log(big2);
