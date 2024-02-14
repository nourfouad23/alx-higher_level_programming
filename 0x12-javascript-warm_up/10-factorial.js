#!/usr/bin/node

function factorial (numToPass) {
  if (isNaN(parseInt(numToPass))) {
    return (1);
  }
  if (numToPass === 1) {
    return (1);
  }
  return (numToPass * factorial(numToPass - 1));
}

console.log(factorial(parseInt(process.argv[2])));
