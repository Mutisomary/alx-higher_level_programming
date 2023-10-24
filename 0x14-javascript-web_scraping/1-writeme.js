#!/usr/bin/node

// script that reads and prints the content of a file.

const fs = require('fs');
const file = process.argv[2];
const content = process.argv[3];

// Read the file
fs.writeFile(file, content, 'utf-8', (error) => {
  if (error) {
    console.error(error);
  }
});
