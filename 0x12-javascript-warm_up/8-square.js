#!/usr/bin/node
// a script that prints a square

'use strict';
const x = process.argv[2];
if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    console.log('X'.repeat(x));
  }
}
