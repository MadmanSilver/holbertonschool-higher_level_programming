#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, res, body) {
  if (err) {
    return console.log(err);
  }

  let count = 0;
  const json = JSON.parse(body);

  json.results.forEach(film => {
    film.characters.forEach(character => {
      if (character.includes('18')) {
        count++;
      }
    });
  });

  console.log(count);
});
