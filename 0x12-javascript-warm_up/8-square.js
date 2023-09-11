#!/usr/bin/node

// Get the first argument passed to the script
const sizeArg = process.argv[2];

// Convert the argument to an integer using parseInt
const size = parseInt(sizeArg);

// Check if the conversion resulted in a valid integer
if (!isNaN(size)) {
  // Use a loop to print a square of size x
  for (let i = 0; i < size; i++) {
    let row = '';
    for (let j = 0; j < size; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
