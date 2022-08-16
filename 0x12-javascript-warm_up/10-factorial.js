#!/usr/bin/node

function factorial (n) {
  let total = 1;
  for (let i = 1; i <= n; i++) {
    total = total * i;
  }
  return total;
}

const myNum = parseInt(process.argv[2]);
console.log(factorial(myNum));
