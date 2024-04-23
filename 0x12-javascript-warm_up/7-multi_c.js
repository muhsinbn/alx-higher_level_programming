#!/usr/bin/node
// This script prints "C is fun" x times, where x is the first argument

const x = parseInt(process.argv[2]);

if (isNaN(x)) {
	console.log('issing number of occurrences';
} else {
	let count = 0;
	while (count < x) {
		console.log('C is fun');
		count++;
    }
}
