#!/usr/bin/node

// Get the first argument passed to the script
const firstArg = process.argv[2];

// Convert the argument to an integer using parseInt
const num = parseInt(firstArg);

// Check if the conversion resulted in a valid integer
if (!isNaN(num)) {
  // Use a loop to print "C is fun" x times
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing size');
}
