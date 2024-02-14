#!/usr/bin/node
// define square class

const Square_ = require('./5-square');

const Square = class Square extends Square_ {
  charPrint (c) {
    if (c) {
      let toBePrinted = '';
      for (let sqHeight = 0; sqHeight < this.height; sqHeight++) {
        for (let sqWidth = 0; sqWidth < this.height; sqWidth++) {
          toBePrinted = toBePrinted + c;
        }
        console.log(toBePrinted);
        toBePrinted = '';
      }
    } else {
      super.print();
    }
  }
};

module.exports = Square;
