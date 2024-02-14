#!/usr/bin/node
// Script class Rectangle that defines a rectangle

const Rectangle = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let toBePrinted = '';
    for (let rectH = 0; rectH < this.height; rectH++) {
      for (let rectW = 0; rectW < this.width; rectW++) {
        toBePrinted = toBePrinted + 'X';
      }
      console.log(toBePrinted);
      toBePrinted = '';
    }
  }
};

module.exports = Rectangle;
