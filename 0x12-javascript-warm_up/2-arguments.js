#!/usr/bin/node
// This prints a message depending on the number of aegumenets passed

const args = process.argv;
if (args.length === 2) {
  console.log('No argument');
} else if (args.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
