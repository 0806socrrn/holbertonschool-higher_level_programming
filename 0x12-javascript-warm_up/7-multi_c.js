#!/usr/bin/node
// Write a script that prints x times “C is fun”
const argv = require('process').argv;

const number = parseInt(Number(argv[2]));

if (isNaN(number)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < number; i++) {
    console.log('C is fun');
  }
}
