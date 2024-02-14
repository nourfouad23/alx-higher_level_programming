#!/usr/bin/node
let numOfTimes = process.argv[2];

if (isNaN(numOfTimes)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < numOfTimes; i++) {
    let square = '';
    for (let j = 0; j < numOfTimes; j++) {
      square = square + 'X';
    }
    console.log(square);
  }
}
