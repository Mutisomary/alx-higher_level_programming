#!/usr/bin/node

// Get the arguments passed to the script
const args = process.argv.slice(2);

// Ensure there are at least two arguments to find the second biggest
if (args.length < 2) {
  console.log(0);
} else {
  // Convert the arguments to integers and sort them in descending order
  const integers = args.map(arg => parseInt(arg)).sort((a, b) => b - a);

  // Find and print the second biggest integer
  const secondBiggest = integers[1];
  console.log(secondBiggest);
}
