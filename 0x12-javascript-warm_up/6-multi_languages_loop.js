#!/usr/bin/node
// prints 3 lines: (like 1-multi_languages.js) but by using an array of string and a loop

'use strict';
const args = ['C is fun', 'Python is cool', 'Javascript is amazing'];
for (const arg in args) {
  console.log(args[arg]);
}
