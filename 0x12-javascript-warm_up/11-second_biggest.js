#!/usr/bin/node
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  let big = 0;
  let sec = 0;

  for (let i = 2; i < process.argv.length; i++) {
    const arg_ = parseInt(process.argv[i]);
    if (arg_ > big) {
      big = arg_;
    }
  }

  for (let i = 2; i < process.argv.length; i++) {
    const arg_ = parseInt(process.argv[i]);
    if (arg_ > sec && arg_ < big) sec = arg_;
  }

  console.log(sec);
}
