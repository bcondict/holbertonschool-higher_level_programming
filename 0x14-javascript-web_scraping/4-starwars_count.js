#!/usr/bin/node

const apiUrl = process.argv[2];
const request = require('request');

request(apiUrl, function (err, response, body) {
  if (err) console.log(err);
  else {
    const movies = JSON.parse(body).results;
    let appearances = 0;

    for (let film of movies) {
      for (let character of film.characters) {
        if (character.includes('18')) {
          appearances++;
        }
      }
    }
    console.log(appearances);
  }
});
