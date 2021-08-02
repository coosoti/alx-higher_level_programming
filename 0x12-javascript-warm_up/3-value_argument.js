#!/usr/bin/node
// This script prints the first argument passed to it

const args = process.argv;
if (args[2] === undefined) {
  console.log('No argument');
} else {
  console.log(args[2]);
}
