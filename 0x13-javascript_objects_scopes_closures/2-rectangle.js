#!/usr/bin/node

// Class definition for Rectangle with width and height attributes
module.exports = class Rectangle {
    constructor (w, h) {
        if (w > 0 && h > 0) {
            this.width = w;
            this.height = h;
        }
    }
};
