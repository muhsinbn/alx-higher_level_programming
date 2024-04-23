#!/usr/bin/node
// A Script that computes and prints a factorial of the arg passed

function factorial (n) {
  if (n === 0 || n === 1 || isNaN(n)) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const { argv } = require('process');

if (argv.length < 3) {
  console.log(factorial(NaN));
}

if (!isNaN(parseInt(argv[2]))) {
  console.log(factorial(argv[2]));
}
