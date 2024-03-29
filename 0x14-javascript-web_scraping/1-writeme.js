#!/usr/bin/node
/* Write a script that writes a string to a file.
The first argument is the file path
The second argument is the string to write
The content of the file must be written in utf-8
If an error occurred during while writing, print the error object */
const { argv } = require('process');
const { writeFile } = require('fs');
const filename = argv[2];
const content = argv[3];

try {
  writeFile(filename, content, err => {
    if (err) {
      console.log(err);
    }
  });
} catch (err) {
  console.log(err);
}
