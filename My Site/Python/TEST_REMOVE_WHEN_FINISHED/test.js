class GrandpaClass {
    prop = []

    grandpaMethod(){
        return 'grandpa method-val'
    }
}

class Parent extends GrandpaClass {}

class TestClass extends Parent{
    method(){
        console.log( super.grandpaMethod )
    }
}

const myObj = new TestClass()

myObj.method()