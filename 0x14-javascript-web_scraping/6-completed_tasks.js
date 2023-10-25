#!/usr/bin/node

// script that computes the number of tasks completed by user id
const request = require('request');
const apiUrl = process.argv[2];

const dictionary = {};

// Make an HTTP GET request to the API URL
request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    data.forEach(function (result) {
      if (result.completed === true) {
        const userid = result.userId;
        if (!(userid in dictionary)) {
          dictionary[userid] = 0;
        }
        dictionary[userid] += 1;
      }
    });
    console.log(dictionary);
  }
});
