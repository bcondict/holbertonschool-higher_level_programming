#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request(url, function (err, response, body) {
  if (err) console.log(err);

  else {
    const json = JSON.parse(body);
    const taksUser = {};

    for (const item of json) {
      if (!item.completed) {
        continue;
      }
      const { userId, completed } = item;
      if (taksUser[userId] === undefined) {
        taksUser[userId] = 0;
      }
      taksUser[userId] += Number(completed);
    }
    console.log(taksUser);
  }
});
