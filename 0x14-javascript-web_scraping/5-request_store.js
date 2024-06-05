#!/usr/bin/node
// A script that gets the contents of a webpage and stores it in a file
const request = require('request');
const fs = require('fs');

const filename = process.argv[3];
const url = process.argv[2];
request.get(url, (error, response, body) => {
  if (error) {
    console.log('Error:', error);
  } else {
    fs.writeFile(filename, body, 'utf8', (err) => {
      if (err) {
        console.log('Error:', err);
      }
    });
  }
});
