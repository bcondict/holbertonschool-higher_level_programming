#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const title = String(process.argv[2]) + '/';

request(`${url}${title}`, function (err, response, body) {
  if (err) console.log(err);
  else {
    console.log(JSON.parse(body).title);
  }
});
