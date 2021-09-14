#!/usr/bin/node
// prints all characters of a Star Wars movie

const request = require('request');
const movie = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/people/';

function moviecharacters (movie, url) {
  request(url, function (err, response, body) {
    if (err) {
      console.log(err);
    }
    const jsonObj = JSON.parse(body);
    const people = jsonObj.results;
    for (const i in people) {
      for (const j in people[i].films) {
        if (people[i].films[j].includes(movie)) {
          console.log(people[i].name);
        }
      }
    }
    if (jsonObj.next !== null) {
      moviecharacters(movie, jsonObj.next);
    }
  });
}
moviecharacters(movie, url);
