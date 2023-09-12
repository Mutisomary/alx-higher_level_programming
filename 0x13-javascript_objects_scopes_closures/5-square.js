#!/usr/bin/node

const Rectangle = require('./4-rectangle');
// Create a class that inherits from Rectangle class

module.exports = class Square extends Rectangle {
  constructor (size) {
  // Call the constructor of the Rectangle class using Super
    super(size, size);
  }
};
