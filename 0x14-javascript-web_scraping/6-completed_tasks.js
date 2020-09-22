#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, res, body) {
  const json = JSON.parse(body);
  let dict = {};

  json.forEach(task => {
    if (task['completed'] === true) {
      if (dict[task['userId']]) {
        dict[task['userId']] += 1;
      } else {
        dict[task['userId']] = 1;
      }
    }
  });

  console.log(dict);
});
