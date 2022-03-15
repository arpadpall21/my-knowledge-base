class BaseClass {
    constructor(){
        this.p1 = 21
    }
}

class TestClass extends BaseClass {
    constructor(){
        super()
    }
}

const myObj = new TestClass()

console.log( myObj )