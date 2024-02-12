#!/usr/bin/node
const args = process.argv.length;
if (args === 2 || args === 3) {
  console.log(0);
} else {
  const x = [];
  for (let i = 2; i < process.argv.length; i++) {
    x.push(+process.argv[i]);
  }
  x.sort((a, b) => b - a);
  console.log(x[1]);
}
