#!/usr/bin/node

// Get the first argument passed to the script
const firstArg = process.argv[2];

// Convert the argument to an integer using parseInt
const num = parseInt(firstArg);

// Check if the conversion resulted in a valid integer
if (!isNaN(num)) {
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}
