#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // instance method to print rectangle using chacter X
  print () {
    for (let i = 0; i < this.height; i++) { console.log('X'.repeat(this.width)); }
  }

  // instance method to exchange the width and the height
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  // instance method to double the width and height
  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
