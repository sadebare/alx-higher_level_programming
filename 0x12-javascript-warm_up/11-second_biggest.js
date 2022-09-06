#!/usr/bin/node
// Write a script that searches the second biggest integer in the list of arguments.
const secLargest = process.argv;
if (secLargest.length <= 3) {
  console.log(0);
} else {
  console.log(secLargest.sort((x, y) => y - x).slice(3)[0]);
}
