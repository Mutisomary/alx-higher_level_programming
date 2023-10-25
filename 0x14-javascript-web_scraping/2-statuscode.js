#!/usr/bin/node

// script that display the status code of a GET request
const request = require('request');
const url = process.argv[2];

// Make HTTP GET request and check for errors
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    console.log('code:', response.statusCode);
  }
});
