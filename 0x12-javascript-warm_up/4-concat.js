#!/usr/bin/node

// Destructure the third and fourth elements of process.argv to get the arguments
const [,, arg1, arg2] = process.argv;

// Print the arguments in the specified format
console.log('${arg1} is ${arg2}');
