#!/usr/bin/node

// esrever.js
// Function that returns the reversed version of a list
exports.esrever = function(list) {
	let reversedList = [];
	for (let i = list.length - 1; i >= 0; i--) {
	  reversedList.push(list[i]);
  }
	return reversedList;
};
