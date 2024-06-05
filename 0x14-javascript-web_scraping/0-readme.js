#!/usr/bin/node
// A script that Reads a file content
const fs = require('fs');

const filepath = process.argv[2];
fs.readFile(filepath, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
