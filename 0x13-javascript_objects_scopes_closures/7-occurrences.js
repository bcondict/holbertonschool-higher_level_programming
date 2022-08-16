#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  var occurences = 0;
  for (var i = 0; i < list.length; i++) {
    if (searchElement === list[i]) {
      occurences++;
    }
  }
  return occurences;
}
