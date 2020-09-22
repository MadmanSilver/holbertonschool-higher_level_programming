#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, res, body) {
  let count = 0;
  const json = JSON.parse(body);

  json['results'].forEach(film => {
    if (film['characters'].includes('https://swapi-api.hbtn.io/api/people/18/')) {
      count++;
    }
  });

  console.log(count);
});
