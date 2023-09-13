#!/usr/bin/node
// function that increments and calls a function.
module.exports.addMeMaybe = addMeMaybe;
function addMeMaybe (number, theFunction) {
  number += 1;
  theFunction(number);
}
