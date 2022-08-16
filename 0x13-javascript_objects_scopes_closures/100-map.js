#!/usr/bin/node

const oldArr = require('./100-data').list;
console.log(oldArr);
console.log(oldArr.map((value, index) => value * index));