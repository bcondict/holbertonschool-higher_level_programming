#!/usr/bin/node

exports.esrever = function (list) {
  var myList = [];
  var i = 0;

  while (i < list.length - 1) i++;

  for (var j = 0; j < list.length; j++) {
    myList[j] = list[i];
    i--;
  }
  return myList;
}