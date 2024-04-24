#!/usr/bin/node

// Destructure the third element of process.argv to get the argument
const [,, arg] = process.argv;

// Check if an argument was passed and print it, or print "No argument"
if (arg === undefined) {
  console.log('No argument');
} else {
  console.log(arg);
}
