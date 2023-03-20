// (1) 객체 생성법
function Dog(name, age) {
  this.name = name
  this.age = age
}

// (2) 객체 생성법 (ES6 이후)
class Cat {
  constructor(name, age) {
    this.name = name
    this.age = age
  }
}

const dog_attack = function () {
  console.log(`${this.name} 멍멍!`)
}
const cat_attack = function () {
  console.log(`${this.name} 냥냥!`)
}

Dog.prototype.attack = dog_attack
Cat.prototype.attack = cat_attack

// new를 통한 생성
let myDog = new Dog('우유', 4)
myDog.attack()
let myCat = new Cat('키티', 3)
myCat.attack()

// (3) .__proto__

let bird = {
  name: '새',
  age: 2,
  attack: function () {
    console.log(`${this.name} 짹짹!`)
  }
}

let cutebirdy = {
  name: '참새',
  age: 4
}

// 인스턴스의 prototype 속성 추가 (.__proto__)
cutebirdy.__proto__ = bird

console.log(bird.name)    // 새
console.log(typeof bird)  // object
bird.attack()             // 새 짹짹!
cutebirdy.attack()        // 참새 짹짹!