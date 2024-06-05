#!/usr/bin/node
// A script that prints all the characters of Star wars movie
const request = require('request');
const movieId = process.argv[2];
const baseUrl = 'https://swapi-api.alx-tools.com/api/films/';

request.get(`${baseUrl}${movieId}`, (error, response, body) => {
  if (error) {
    console.log('Error:', error);
  } else {
    const movie = JSON.parse(body);
    const charsUrls = movie.characters;
    charsUrls.forEach(url => {
      request.get(url, (error, response, body) => {
        if (error) {
          console.log('Error::', error);
        } else {
          const character = JSON.parse(body);
          console.log(character.name);
        }
      });
    });
  }
});
