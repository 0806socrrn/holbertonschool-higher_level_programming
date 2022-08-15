#!/usr/bin/node
// Write a script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer
const argv = require('process').argv;
const number = parseInt(Number(argv[2]));
console.log(isNaN(number) ? 'Not a number' : `My number: ${number}`);
