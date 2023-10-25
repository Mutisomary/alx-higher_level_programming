#!/usr/bin/node

// script that gets the contents of a webpage and stores it in a file.
const request = require('request');
const fs = require('fs');

const apiUrl = process.argv[2];
const file = process.argv[3];

// Make an HTTP GET request to the specified URL
request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(file, body, 'utf-8', function (error, data) {
      if (error) {
        console.error(error);
      }
    });
  }
});
