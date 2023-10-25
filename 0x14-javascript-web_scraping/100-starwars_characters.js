#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

// Make an HTTP GET request to the Star Wars API to get information about the specified movie
request(`https://swapi.dev/api/films/${movieId}/`, function (error, response, body) {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(`Failed to retrieve movie information. Status code: ${response.statusCode}`);
  } else {
    const movieData = JSON.parse(body);
    const charactersUrls = movieData.characters;

    // Fetch character information for each character URL
    charactersUrls.forEach(characterUrl => {
      request(characterUrl, function (error, response, characterBody) {
        if (error) {
          console.error(error);
        } else if (response.statusCode !== 200) {
          console.error(`Failed to retrieve character information. Status code: ${response.statusCode}`);
        } else {
          const characterData = JSON.parse(characterBody);
          console.log(characterData.name);
        }
      });
    });
  }
});
