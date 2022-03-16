class TestClass {
    prop = 'prop-val'
}

const myObj = new TestClass()

console.log( Object.getOwnPropertyNames(myObj) )