#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request(url, function (err, response, body) {
  if (err) throw err;

  const json = JSON.parse(body);
  const user = {};

  for (const name of json) {
    if (!name.completed) continue;
    const { id, completed } = name;
    if (user[id] === undefined) {
      user[id] = 0;
    }
    user[id] += Number(completed);
  }
  console.log(user);
});
