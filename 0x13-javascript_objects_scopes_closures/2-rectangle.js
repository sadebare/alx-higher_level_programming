#!/usr/bin/node
// a class Rectangle that defines a rectangle
class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
      return this;
    } else {
      this.width= w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
