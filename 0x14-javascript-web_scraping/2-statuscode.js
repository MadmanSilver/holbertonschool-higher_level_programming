#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, res, body) {
  console.log('code: ' + res.statusCode);
});
