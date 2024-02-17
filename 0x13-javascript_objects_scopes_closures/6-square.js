#!/usr/bin/node
const ParentSquare = require('./5-square');

class Square extends ParentSquare {
  charPrint (c) {
    if (!c) {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    } else {
      for (let j = 0; j < this.height; j++) {
        console.log(`${c}`.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
