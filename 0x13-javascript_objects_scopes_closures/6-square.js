#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
  charPrint(c){
    var i = 0;
    if (c) {
      for (i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    } else {
      this.print();
    }
  }
}

module.exports = Square;
