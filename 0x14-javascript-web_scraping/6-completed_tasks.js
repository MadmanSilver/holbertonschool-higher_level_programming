#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, res, body) {
  if (err) {
    return console.log(err);
  }

  const json = JSON.parse(body);
  const dict = {};

  json.forEach(task => {
    if (task.completed === true) {
      if (dict[task.userId]) {
        dict[task.userId] += 1;
      } else {
        dict[task.userId] = 1;
      }
    }
  });

  console.log(dict);
});
