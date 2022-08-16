#!/usr/bin/node
/* Write a function that returns the reversed version of a list:
Prototype: exports.esrever = function (list)
You are not allow to use the built-in method reverse */
exports.esrever = function (list) {
  if (list.length === 1) {
    return ([list.pop()]);
  }
  if (list.length === 0) {
    return ([]);
  }
  return [list.pop()].concat(exports.esrever(list));
};
