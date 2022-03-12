class TestClass {
    method(){ return 'stMethod-val' };

    prop = 'stProp1-val';
}

class SubClass extends TestClass{}


testObj = new TestClass()
subObj = new SubClass()

console.log( testObj.prop )
console.log( subObj.prop )
console.log( testObj.method() )
console.log( subObj.method() )

// console.log( TestClass.stProp )
// console.log( TestClass.stMethod() )

// console.log( SubClass.stProp )
// console.log( SubClass.stMethod() )


