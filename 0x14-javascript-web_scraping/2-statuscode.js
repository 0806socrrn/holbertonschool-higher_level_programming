#!/usr/bin/node
/* Write a script that display the status code of a GET request.
The first argument is the URL to request (GET)
The status code must be printed like this: code: <status code>
You must use the module axios */
const { get } = require('request');
const { argv } = require('process');
const url = argv[2];

get(url, (err, { statusCode }, body) => {
  if (err) {
    return (console.log(err));
  }
  console.log(`code: ${statusCode}`);
});
