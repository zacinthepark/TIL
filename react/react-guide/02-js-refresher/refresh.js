// Arrow Function
// const multiply = (number) => {
//   return number * 2
// }
// const multiply = number => number * 2
// console.log(multiply(2))


// Exports and Imports
// export default는 파일에서 어떤 것을 import하면 항상 default export가 내보낸 것을 기본값으로 가져온다는 것
// named export의 경우 import 시에 import { targetName }으로 import
// named export의 경우 import {{ targetName as myName }}으로 변형 가능
// import * as bundled와 같은 방식도 가능


// Classes
// ES6
// class Human {
//   constructor() {
//     this.gender = 'male'

//   }
//   printGender() {
//     console.log(this.gender)
//   }
// }

// class Person extends Human {
//   // constructor는 인스턴스를 생성할 때마다 실행
//   constructor() {
//     super() // 상위 클래스의 생성자
//     this.name = 'Max'
//     this.gender = 'female'
//   }

//   printMyName() {
//     console.log(this.name)
//   }
// }
// const person = new Person()
// person.printMyName()
// person.printGender()

// ES7
// class Human {
//   gender = 'male'
//   printGender = () => {
//     console.log(this.gender)
//   }
// }

// class Person extends Human {
//   name = 'Max'
//   gender = 'female'
//   printMyName = () => {
//     console.log(this.name)
//   }
// }

// const person = new Person()
// person.printMyName()
// person.printGender()


// Spread & Rest Operators
// Spread
// const numbers = [1, 2, 3]
// const newNumbers = [...numbers, 4]
// console.log(newNumbers)

// const person = {
//   name: 'Max'
// }
// const newPerson = {
//   ...person,
//   age: 28
// }
// console.log(newPerson)

// // Rest
// // 레스트 연산자는 함수의 매개변수들을 array로 만들어줌
// const filter = (...args) => {
//   return args.filter(el => el===1)
// }
// console.log(filter(1, 2, 3))


// Destructuring (구조분해할당)
// 배열의 원소나 객체의 프로퍼티를 쉽게 추출하여 변수에 저장

// Array Destructuring
// const numbers = [1, 2, 3]
// const [num1, num2] = numbers
// const [num3, , num4] = numbers
// console.log(num1, num2) // 1 2
// console.log(num3, num4) // 1 3

// // Object Destructuring
// const person = {
//   name: 'Max',
//   age: 28
// }
// const {name} = person
// console.log(name) // Max


// Primitive Type and Reference Type

// Primitive Type: number, string, boolean, ...
// 값 복사가 이루어짐

// Reference Type: object, array
// 참조 포인터 복사가 이루어짐
// 그렇다면 새로 객체를 생성하여 복사하고 싶다면? --> spread operator 사용 --> 객체로부터 프로퍼티와 프로퍼티 값을 쭉 가져와서 새로운 객체에 복사해준다고 생각
// const person = {
//   name: 'Max'
// }
// const secondPerson = {
//   ...person
// }
// person.name = 'Manu'
// console.log(secondPerson)


// Array Functions
// const numbers = [1, 2, 3]
// const doubleNumbers = numbers.map(num => num * 2)
// console.log(doubleNumbers)
