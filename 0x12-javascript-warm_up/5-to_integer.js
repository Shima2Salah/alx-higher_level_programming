#!/usr/bin/node
const args = process.argv;
if (isNaN(Number(args[2])) === true) {
  console.log('Not a number');
} else {
  console.log(`My number: ${Number(args[2])}`);
}
