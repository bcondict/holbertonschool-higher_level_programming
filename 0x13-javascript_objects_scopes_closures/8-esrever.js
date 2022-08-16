#!/usr/bin/node

exports.esrever = function (list) {
  const myList = [];
  let i = 0;

  while (i < list.length - 1) i++;

  for (let j = 0; j < list.length; j++) {
    myList[j] = list[i];
    i--;
  }
  return myList;
};
