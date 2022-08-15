#!/usr/bin/node
// Write a script that prints two arguments passed to it, in the following format: “ is ”

const { argv } = require('process');
if (argv.length) {
  console.log(argv[2], 'is', argv[3]);
}
