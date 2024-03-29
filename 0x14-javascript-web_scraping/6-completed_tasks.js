#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const dict = {};
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const res = JSON.parse(body);
    for (let i = 0; i < res.length; i++) {
      if (res[i].completed === true) {
        if (dict[res[i].userId] === undefined) {
          dict[res[i].userId] = 1;
        } else {
          dict[res[i].userId] += 1;
        }
      }
    }
    console.log(dict);
  }
});
