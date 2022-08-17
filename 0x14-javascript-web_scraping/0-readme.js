#!/usr/bin/node
/* Write a script that reads and prints the content of a file.
The first argument is the file path
The content of the file must be read in utf-8
If an error occurred during the reading, print the error object */
const { argv } = require('process');
const { readFile } = require('fs');
const filename = argv[2];

try {
  readFile(filename, (err, data) => {
    if (err) {
      console.log(err);
    } else {
      console.log(data.toString('utf8'));
    }
  });
} catch (err) {
  console.log(err);
}
