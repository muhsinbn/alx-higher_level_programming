#!/usr/bin/node

// Destructure the third element of process.argv to get the argument
const [, , arg] = process.argv;

// Convert the argument to an integer using parseInt
const number = parseInt(arg, 10);

// Check if the argument can be converted to an integer and print the result
if (!isNaN(number)) {
  console.log(`My number: ${number}`);
} else {
  console.log('Not a number');
}
