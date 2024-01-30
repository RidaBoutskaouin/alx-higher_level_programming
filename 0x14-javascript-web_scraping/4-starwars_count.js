#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) throw err;
  const json = JSON.parse(body);
  let count = 0;
  for (const film of json.results) {
	for (const character of film.characters) {
	  if (character.includes('18')) {
		count++;
	  }
	}
  }
  console.log(count);
});
