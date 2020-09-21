#!/usr/bin/node

exports.esrever = function (list) {
  const rev = [];

  list.forEach(element => {
    rev.unshift(element);
  });

  return rev;
};
