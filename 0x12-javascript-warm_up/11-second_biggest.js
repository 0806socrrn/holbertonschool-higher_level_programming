#!/usr/bin/node
// Write a script that searches the second biggest integer in the list of arguments.
const { argv } = require('process');

const penultimate = argv.slice(2)
  .sort((a, b) => b - a)
  .filter((item, index, array) => array.indexOf(item) === index)[1];

console.log(penultimate || 0);
