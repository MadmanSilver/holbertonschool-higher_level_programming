#!/usr/bin/node
const sqr = require('./5-square');

class Square extends sqr {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let y = 0; y < this.height; y++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
