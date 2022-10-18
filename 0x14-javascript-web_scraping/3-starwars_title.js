#!/usr/bin/node
/**
  prints the title of a Star Wars movie
  where the episode number matches a given integer
  usage: ./3-starwars_title.js id
 */
  const request = require('request');
  const endPoint = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
  request({ url: endPoint, methods: 'GET' }, function (err, response, body) {
    if (err) {
      console.log(err);
    } else {
      console.log(body && JSON.parse(body).title);
    }
  });
