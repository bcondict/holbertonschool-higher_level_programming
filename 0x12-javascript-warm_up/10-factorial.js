#!/usr/bin/node

const myNum = parseInt(process.argv[2]);
function factorial (n) {
  let total = 1;
  for (let i = 1; i <= n; i++) {
    total = total * i;
  }
  return total;
}
