#!/usr/bin/node

// Define a recursive function to compute the factorial
function factorial (n) {
  if (isNaN(n)) {
    return 1; // Factorial of NaN is 1
  } else if (n === 0 || n === 1) {
    return 1; // Base case: factorial of 0 or 1 is 1
  } else {
    return n * factorial(n - 1); // Recursive case
  }
}

// Get the first argument passed to the script
const arg = process.argv[2];

// Convert the argument to an integer using parseInt
const num = parseInt(arg);

// Compute the factorial
const result = factorial(num);

// Print the result
console.log(result);
