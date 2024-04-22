#!/usr/bin/node
// A Script that prints two arguments passed to it with "is" in middle
const { argv } = require('process');
if (argv[2]) {
  console.log(argv[2] + (argv[3] ? ' is ' + argv[3] : ' is undefined'));
} else {
  console.log('undefined is undefined');
}
