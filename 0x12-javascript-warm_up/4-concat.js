#!/usr/bin/node

// Get the first and second arguments passed to the script
const arg1 = process.argv[2];
const arg2 = process.argv[3];

// Check if both arguments are provided
if (typeof arg1 !== 'undefined' && typeof arg2 !== 'undefined') {
  console.log(`${arg1} is ${arg2}`);
} else {
  console.log(`${arg1} is undefined`);
}
