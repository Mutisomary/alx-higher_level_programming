#!/usr/bin/node

// prints the number of movies
const request = require('request');
const apiUrl = process.argv[2];

// Make an HTTP GET request to the API
request(apiUrl, function (error, response, body) {
  if (!error) {
    const results = JSON.parse(body).results;
    const moviesWithWedge = results.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0);
    console.log(moviesWithWedge);
  }
});
