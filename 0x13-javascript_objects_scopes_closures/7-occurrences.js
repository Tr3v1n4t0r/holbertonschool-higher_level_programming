#!/usr/bin/node
exports.nbOccurrences = function (list, searchElement) {
  let number = 0;
  for (const item of list) {
    if (item === searchElement) {
      number++;
    }
  }
  return number;
};
