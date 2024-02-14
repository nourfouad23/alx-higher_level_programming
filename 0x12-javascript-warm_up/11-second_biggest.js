#!/usr/bin/node

function second (myArray) {
  if (myArray.length === 2 || myArray.length === 3) { return (0); }

  let maxNum = myArray[2];
  let secondMaxNum = myArray[3];

  for (let i = 2; i < myArray.length; i++) {
    if (myArray[i] > maxNum) {
      secondMaxNum = maxNum;
      maxNum = myArray[i];
    } else if (myArray[i] > secondMaxNum && myArray[i] < maxNum) {
      secondMaxNum = myArray[i];
    }
  }
  return (secondMaxNum);
}

console.log(second(process.argv));
