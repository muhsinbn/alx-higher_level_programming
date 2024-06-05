#!/usr/bin/node
// A script that prints all characters of a Star War movie
const request = require('request');
const movieId = process.argv[2];
const baseUrl = 'https://swapi-api.alx-tools.com/api/films/';

function fetchMovie (movieId) {
  return new Promise((resolve, reject) => {
    request(`${baseUrl}${movieId}`, (error, response, body) => {
      if (error) {
        console.log('Error:', error);
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}
// Function to fetch character details
function fetchCharacter (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        console.log('Error:', error);
        reject(error);
      } else {
        resolve(JSON.parse(body).name);
      }
    });
  });
}

// Main function to fetch movie and characters
function main () {
  fetchMovie(movieId)
    .then(movie => {
      const charsUrls = movie.characters;
      return Promise.all(charsUrls.map(fetchCharacter))
        .then(names => {
          names.forEach(name => {
            if (name) console.log(name);
          });
        });
    })
    .catch(error => {
      console.log('Error:', error);
    });
}
main();
