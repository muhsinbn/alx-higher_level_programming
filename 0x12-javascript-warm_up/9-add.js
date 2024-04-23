#!/usr/bin/node
// A Script that prints the addition of 2 integers

function add (a, b) {
  return a + b;
}

const { argv } = require('process');
if (!isNaN(parseInt(argv[2])) && !isNaN(parseInt(argv[3]))) {
  const a = parseInt(argv[2]);
  const b = parseInt(argv[3]);
  console.log(add(a, b));
} else {
  console.log('NaN');
}
