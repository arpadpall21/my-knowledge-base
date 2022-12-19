"use strict";
class AbsAnimal {
    constructor(species, // subclasses must implement all these properties    
    origin) {
        this.species = species;
        this.origin = origin;
        this.t = 'animal'; // default property (all instance will own it)
    }
    getT() { return this.t; } // instances will inherit this method (normal method)    
}
// const animal = new Animal('cat'. 'europe', 32)  // -! error thrown, abstract class cannot be initialized directly
class Cat extends AbsAnimal {
    constructor(species, // implementing abstract class properties
    origin) {
        super(species, origin);
        this.species = species;
        this.origin = origin;
        this.species = species;
        this.origin = origin;
    }
    getName() { return 'cili'; } // implementing abstract class method  
}
const cat = new Cat('cat', 'europe');
console.log(cat);
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
