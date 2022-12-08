function getBack<T1, T2>(a: T1, b:T2): (T1|T2)[] {      // captures the entry type 
    return [a, b]
}

console.log( getBack(1, false) );           // -> [1, false]
console.log( getBack('a', [2]) );           // -> ['a', [2]]


function getBac2<T>(a:T, b:T): T {
    if (typeof a === 'number' && typeof b === 'number') {       // type narrowing is very limited on Generics 
        return a + b;                                           // -! thros an error (type not narrowed)
    }
}

type sn = 'a' | 'b';

function getBac3<T extends sn>(a:T): T {
}




/*-------------------------------------------------------------------*/
/*-------------------------------------------------------------------*/
/*-------------------------------------------------------------------*/
// type Person = {
//     name: string | null | undefined
// }

// const peter: Person = { name: 'Péter' }
// const adam: Person = { name: null }

// console.log( peter.name?.toUpperCase() )        // -> 'PÉTER'
// console.log( adam.name?.toUpperCase() )         // -> undefined (statement shortcircuited because <mark>adam.name</mark> is a falsy type)


// const myArray : any = [1];

// console.log( myArray?.[0] );            // -> 1
// console.log( myArray?.[1] );            // -> undefined 


// let myFunction :any;
// console.log( myFunction?.('w') )        // -> undefined 

// myFunction = (a:any):any => a;
// console.log( myFunction('x') );         // -> 'x'


/*-------------------------------------------------------------------*/
/*-------------------------------------------------------------------*/
/*-------------------------------------------------------------------*/
// type PersonType = { name:string }
// // type PersonType = { age:number }         // throws an error (duplicate type name)

// interface PersonInterface { name:string }
// interface PersonInterface { age:number }    // interfaces can be 'opened' (extended like this)

// const john: PersonInterface = {
//     name: 'John',
//     age: 32
// }


// interface Animal {
//     origin: string
//     hasLegs: boolean
// }

// interface Cat extends Animal {
//     cunning: boolean
// }

// const cili: Cat = {
//     origin: 'home',
//     hasLegs: true,
//     cunning: true
// }

// console.log( cili );        // -> { origin:'home', hasLegs:true, cunning:true }



/*-------------------------------------------------------------------*/
/*-------------------------------------------------------------------*/
/*-------------------------------------------------------------------*/
// interface Camera {
//     cameraType: string
//     takePhoto(): string
// }

// interface ScreenX {
//     screenSize: number
//     getBrightness(): number
// }

// // interface properties must be implemented in the implementation class some way
// class MobilePhone1 implements Camera, ScreenX {
//     cameraType: string = 'sony';        // interface properties are implemented here
//     screenSize: number = 21;

//     takePhoto(): string { return 'take photo...'}
//     getBrightness(): number { return 32 }
// }

// class MobilePhone2 implements Camera, ScreenX {
//     constructor(public cameraType: string, public screenSize: number) {   // interface properties are implemented here
//         this.cameraType = cameraType;
//         this.screenSize = screenSize;
//     }

//     takePhoto(): string { return 'take photo...'}
//     getBrightness(): number { return 32 }
// }


// const phone1 = new MobilePhone1()
// const phone2 = new MobilePhone2('fuji', 44)     // interface implementation in constructor

// console.log( phone1 )   // -> {cameraType:'sony', screenSize:21}
// console.log( phone2 )   // -> {cameraType:'fuji', screenSize:44}



/*-------------------------------------------------------------------*/
/*-------------------------------------------------------------------*/
/*-------------------------------------------------------------------*/
// class Person {
//     name:string
//     readonly age:number
//     nationality:string = 'Hungarian'        // default value
//     private _sex:string = 'male'            // private field
    
//     constructor(name:string, age:number) {
//         this.name = name;
//         this.age = age;
//     }
    
//     getSex() {
//         return this._sex;                   // returns the private filed value
//     }
// }

// const pepe = new Person('Pepe', 32);
// console.log( pepe );     // -> { nationality: 'Hungarian', name: 'Pepe', age: 32 }
// console.log( pepe.getSex() );


// class Person2 {
//     constructor(
//             public name:string,             // pretty syntax
//             public age:number) {
//         this.name = name;
//         this.age = age;
//     }
// }

// const ede = new Person2('Ede', 41);
// console.log( ede );     // -> { name:'Ede', age:41 }



/*-------------------------------------------------------------------*/
/*-------------------------------------------------------------------*/
/*-------------------------------------------------------------------*/
// class A {
//     private priv: string = 'priv';      // accessible only within this class
//     protected prot: string = 'prot';    // accessible within this class and all classes that inherits from this class 
// }

// class B extends A { 
//     getInsides() {
//         console.log( this.prot )        // -> 'prot'
//         console.log( this.priv )        // !- Error
//     }
// }



/*-------------------------------------------------------------------*/
/*-------------------------------------------------------------------*/
/*-------------------------------------------------------------------*/
// abstract class Animal {
//     constructor(species: string) {}     // properties must be implemented in sub classes
//     abstract getSize(): number          // method must be implemented in subclasses
//     getLegs(): number { return 4}       // all subclaesses inherits this method
// }

// // const animal = new Animal('cat')        // -! this is not allowed (abstract calls cannot be implemented directly error thrown)

// // must implement abstract class properties an methods
// class Cat extends Animal {
//     constructor(public species: string) {
//         super(species);
//     }
    
//     getSize(): number {
//         return 32;
//     }
// }


/*-------------------------------------------------------------------*/
/*-------------------------------------------------------------------*/
/*-------------------------------------------------------------------*/
// function returnAnyType<Type>(arg:Type): Type {
//     return arg;
// }

// const returnAnyTypeArrowFunction = <T>(arg: T) => arg       // generic used in arrow function 

// console.log( returnAnyType(23) );               // -> 23
// console.log( returnAnyType('someString') );     // -> 'someString'
// console.log( returnAnyTypeArrowFunction('x') )  // -> 'x

// function returnArrayOfTypes<T>(arr: T[]): T {   // takse an array of generic types
//     return arr[0]
// }

// console.log( returnArrayOfTypes([1, 2]) )            // -> 1
// console.log( returnArrayOfTypes(['a', 'b']) )        // -> 'a'


// function getGen<AnyName>(a: AnyName): AnyName {     // can have any name
//     return a
// }

// console.log( getGen(false) )            // -> false


// function multipleGens<T1, T2> (a: T1, b: T2): T2 {      // multiple generics
//     return b
// }

// console.log( multipleGens(2, 'x') )     // -> 'x'



/*-------------------------------------------------------------------*/
/*-------------------------------------------------------------------*/
/*-------------------------------------------------------------------*/
// class Cart<Product> {
//     public cart: Product[] = [];

//     addProductCart(p: Product): void {
//         this.cart.push(p)
//     }

//     getAll(): Product[] {
//         return this.cart
//     }
// }

// const cart = new Cart();

// cart.addProductCart('apple');
// cart.addProductCart('mellon');
// cart.addProductCart(2);
// cart.addProductCart(true);
// console.log( cart.getAll() );   // -> ['apple', 'mellon', 2, true]



/*-------------------------------------------------------------------*/
/*-------------------------------------------------------------------*/
/*-------------------------------------------------------------------*/
// type myTypes = string | number | null

// function getCorrectType(a: myTypes): myTypes {
//     if (a)                  // narrowing null type
//         if (typeof a === 'string') {
//             return a.toUpperCase();
//         } else {
//             return a++;
//         }
    
//     return null
// }

// console.log( getCorrectType(null) )     // -> null
// console.log( getCorrectType('x') )      // -> 'X'
// console.log( getCorrectType(1) )        // -> 2

// type Person = {
//     name: string
//     surname?: string
// }

// function getName(p: Person): Person | null {
//     if ('surname' in p) {
//         return p
//     }

//     return null
// }

// console.log( getName({name:'Smith', surname:'John'}) )      // -> {name:'Smith', surname:'John'}   
// console.log( getName({name:'Frederick'}) )              // -> null



/*-------------------------------------------------------------------*/
/*-------------------------------------------------------------------*/
/*-------------------------------------------------------------------*/
// const a : any = 'some string'
// const b = a as string;      // identifies variable a as string type
// console.log( typeof b )     // -> 'string'


// type Fish = {
//     swimSpeed : number
// }
// type Bird = {
//     flySpeed : number
// }

// function getSpeed(animal: Fish | Bird): number {
//     if ('swimSpeed' in animal) {
//         return (animal as Fish).swimSpeed;
//     } else {
//         return (animal as Bird).flySpeed;
//     }
// }

// console.log( getSpeed({ swimSpeed:15 }) )       // -> 15
// console.log( getSpeed({ flySpeed:21 }) )        // -> 21



/*-------------------------------------------------------------------*/
/*-------------------------------------------------------------------*/
/*-------------------------------------------------------------------*/
// type narrowing with instanceof

// function isString(val: string | number): val is string {    // type narrowing function
//     return typeof val === "string";
// }
// function isNumber(val: string | number): val is number {    // type narrowing function
//     return typeof val === "number";
// }

// function duplicate(arg: any) {
//     if (isString(arg)) {        // type is narrowed to string
//         return arg + ' ' + arg;
//     } else if (isNumber(arg)) { // type is narrowed to number
//         return arg * 2;
//     }
//     throw Error('Not number of string type');
// }

// console.log( duplicate(3) )                 // -> 6
// console.log( duplicate('three') )           // -> 'three three'
// console.log( duplicate([1, 'one']) )        // -! error thrownd
