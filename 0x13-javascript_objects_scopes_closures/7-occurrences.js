#!/usr/bin/node
// number of times

exports.nbOccurences = function (list, searchElement) {
  return list.filter((value) => (value === searchElement)).length;
};
