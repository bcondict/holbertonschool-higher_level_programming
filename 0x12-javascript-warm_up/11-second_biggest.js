#!/usr/bin/node

const nums = process.argv.slice(2);
let result = 0;
function sec_big (a, b) {
  return a - b;
}

if (nums.length > 1) {
  nums.sort(sec_big);
  result = nums[nums.length - 2];
}

console.log(result);
