#!/usr/bin/node
module.exports.callMeMoby = callMeMoby;
// function that executes x times a funtion
function callMeMoby (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
    }
};
