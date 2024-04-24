#!/usr/bin/node

let count = 0;

// logMe function that prints the number of arguments
exports.logMe = function(item) {
	console.log(`${count}: ${item}`);
	count++;
};
