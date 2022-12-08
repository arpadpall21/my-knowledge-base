"use strict";
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
function isString(val) {
    return true;
}
console.log(isString(3));
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
