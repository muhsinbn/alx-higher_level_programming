#!/usr/bin/node
// A script that prints title of a star war movie where the episode number
// matches a given integer
const request = require('request');
const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.log('Error:', error);
  } else {
    const movie = JSON.parse(body);
    console.log(`${movie.title}`);
  }
});
