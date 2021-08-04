#!/usr/bin/node
// class Square that defines a square and inherits from Square of 5-square.js

const Square1 = require('./5-square.js');

module.exports = class Square extends Square1 {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.width; i++) {
        console.log(c.repeat(this.height));
      }
    }
  }
};