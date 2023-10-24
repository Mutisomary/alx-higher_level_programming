#!/usr/bin/node

// script that reads and prints the content of a file.

const fs = require('fs');
const file = process.argv[2];

// Read the file
fs.readFile(file, 'utf-8', (error, data) => {
  if (error) {
    console.error('Error reading file:', error);
    return;
  }
  console.log(data);
});
