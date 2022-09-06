#!/usr/bin/node
// Write a script that computes and prints a factorial
const x = parseInt(process.argv[2]);
function Factorial (x) {
  if ((Number.isNaN(x)) || (x === 1)) {
    return 1;
  }
  return Factorial(x - 1) * x;
}

console.log(Factorial(x));
