#!/usr/bin/node

const Rectangle = require('./5-square');
// Create a class that inherits from Rectangle class

module.exports = class Square extends Rectangle {
  // instance method tha prints the rectangle
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) { console.log(c.repeat(this.width)); }
      }
  }
};       
