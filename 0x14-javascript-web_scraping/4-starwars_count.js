#!/usr/bin/node
// A script that prints the number of movies where the character
// Wedge Antilles is present. The char ID is 18
const request = require('request');
const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.log('Error:', error);
  }
  const results = JSON.parse(body).results;
  const count = results.reduce((count, movie) => {
    return movie.characters.some(character => character.endsWith('/18/')) ? count + 1 : count;
  }, 0);
  console.log(`${count}`);
});
