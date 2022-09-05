#!/usr/bin/node
/*
Script that prints a new message
depending on the number of argument passed
 */
const noArgs = process.argv.length;
if (noArgs < 3) {
  console.log('No argument');
} else if (noArgs === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
