#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const dest = process.argv[3];

request(url, function (err, response, body) {
  if (err) throw err;
  fs.writeFile(`${dest}`, body, 'utf-8', function (err) {
    if (err) console.log(err);
  });
});
