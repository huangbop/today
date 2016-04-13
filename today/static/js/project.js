

function cubeme(incomingNum) {
  if (incomingNum == 1) {
    return 'Waht are yout doing?';
  } else {
    return Math.pow(incomingNum, 3);
  }
}


theNum = 3;
finalNum = cubeme(theNum);

alert('cubeme the ' + theNum + ' is ' + finalNum );
