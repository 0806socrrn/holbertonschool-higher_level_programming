#!/usr/bin/node
// Write a function that executes x times a function.
exports.callMeMoby = function (x, theFunction) {
  let i = 0;
  for (; i < x; i++) {
    theFunction();
  }
};
