#!/usr/bin/node
let count = 0;
process.argv.forEach(function (val, index) {
  count++;
  if (index === 2) {
    console.log(val);
  }
});
if (count === 2) {
  console.log('No argument');
}
