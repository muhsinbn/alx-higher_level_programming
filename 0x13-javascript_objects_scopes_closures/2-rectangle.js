#!/usr/bin/node

// Class definition for Rectangle with width and height attributes
class Rectangle {
    constructor(w, h) {
        if (w > 0 && h > 0 && Number.isInteger(w) && Number.isInteger(h)) {
            this.width = w;
            this.height = h;
        } else {
            // Create an empty object if w or h is 0 or not a positive integer
            this.width = 0;
            this.height = 0;
        }
    }
}

module.exports = Rectangle;
