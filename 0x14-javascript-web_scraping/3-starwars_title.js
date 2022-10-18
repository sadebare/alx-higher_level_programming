#!/usr/bin/node
// script that prints the title of a Star Wars movie

const request = require('request');
let url = 'http://swapi.co/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
