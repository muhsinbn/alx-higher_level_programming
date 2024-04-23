#!/usr/bin/node
// A Script that finds and prints the second largest int passed

const { argv } = require('process');

const integers = argv.slice(2).filter(arg => !isNaN(parseInt(arg)));
const mysort = integers.sort((a, b) => b - a);

if (mysort.length >= 2) {
  console.log(mysort[1]);
} else {
  console.log(0);
}
