#!/usr/bin/node
/* Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.
The first argument is the movie ID
You must use the Star wars API with the endpoint https://swapi-api.hbtn.io/api/films/:id
You must use the module axios */
const request = require('request');
const url = 'http://swapi.co/api/films/';
const episode = process.argv[2];
request(url + episode, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const jsonobj = JSON.parse(body);
    console.log(jsonobj.title);
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});
