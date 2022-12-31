function computeKey(key) {
  return `keyIs${key}`;
}

const myObj = {
  [computeKey("x")]: false,
};

console.log( myObj );