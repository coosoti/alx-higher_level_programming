#!/usr/bin/node
// function that returns the reversed version of a list

exports.esrever = function (list) {
  const rev = [];
  for (let i = 0; i < list.length; i++) {
    rev.unshift(list[i]);
  }
  return rev;
};
