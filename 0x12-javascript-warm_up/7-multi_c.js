#!/usr/bin/node
// Write a script that prints x times “C is fun”
const x = process.argv[2];
for (let i = 0; i < x; i++) {
  console.log('C is fun');
}
