#!/usr/bin/node

// Define a function to add two integers
function add (a, b) {
  return a + b;
}

// Get the first and second arguments passed to the script
const arg1 = process.argv[2];
const arg2 = process.argv[3];

// Convert the arguments to integers
const int1 = parseInt(arg1);
const int2 = parseInt(arg2);

// Check if both arguments are valid integers
if (!isNaN(int1) && !isNaN(int2)) {
  const result = add(int1, int2);
  console.log(result);
} else {
  console.log('NaN');
}
