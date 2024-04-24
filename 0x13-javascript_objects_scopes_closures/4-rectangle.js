#!/usr/bin/node

// Class definition for Rectangle with width and height attributes
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // Instance method to print the rectangle using the character 'X'
  print () {
        if (this.width === 0 || this.height === 0) {
            console.log('');
        } else {
            for (let i = 0; i < this.height; i++) {
                console.log('X'.repeat(this.width));
            }
        }
    }

    // Instance method to exchange the width and height of the rectangle
    rotate() {
        [this.width, this.height] = [this.height, this.width];
    }

    // Instance method to double the width and height of the rectangle
    double() {
        this.width *= 2;
        this.height *= 2;
    }
}

module.exports = Rectangle;
