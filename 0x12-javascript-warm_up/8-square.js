#!/usr/bin/node
const args = process.argv;
let sqr = '';
if (parseInt(args[2])) {
  for (let y = 0; y < parseInt(args[2]); y++) {
    for (let x = 0; x < parseInt(args[2]); x++) {
      sqr += 'X';
    }
    if (y !== parseInt(args[2]) - 1) {
      sqr += '\n';
    }
  }
  console.log(sqr);
} else {
  console.log('Missing size');
}
