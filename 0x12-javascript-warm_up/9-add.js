#!/usr/bin/node
const first = parseInt(process.argv[2]);
const sec = parseInt(process.argv[3]);

function add (a, b) {
  const sum = a + b;
  console.log(sum);
}
add(first, sec);
