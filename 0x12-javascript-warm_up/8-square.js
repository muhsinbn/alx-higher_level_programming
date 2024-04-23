#!/usr/bin/node
// A Script that prints a square, first arg is the size of the square
// X must be the character to print the square
const { argv } = require('process');
if (!isNaN(parseInt(argv[2]))) {
  const size = parseInt(argv[2]);
  if (size > 0) {
    for (let i = 0; i < size; i++) {
      console.log('X'.repeat(size));
    }
  }
} else {
  console.log('Missing size');
}
