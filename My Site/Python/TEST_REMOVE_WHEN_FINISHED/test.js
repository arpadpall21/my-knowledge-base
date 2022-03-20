class NotArray extends Array {}

const myArray = new NotArray(1, 2, 3)

console.log( myArray )
console.log( typeof myArray )