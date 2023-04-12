function square(num: number) {
  return num * num
}

function greet(person: string = 'stranger'): string {
  return `Hi there, ${person}`
}

const doSomething = (person: string, age:number, isFunny: boolean) => {}

greet()
greet('Tom Hardy')
doSomething('Tom', 26, true)

function rando(num: number) {
  if (Math.random() < 0.5) {
    return num.toString()
  }
  return num
}

const add = (x: number, y: number): number => {
  return x + y
}

const colors = ['red', 'orange', 'yellow']
colors.map(color => {
  return color.toUpperCase()
})

function printTwice(msg: string): void {
  console.log(msg)
  console.log(msg)
}

// Never Type

// exception
function makeError(msg: string): never {
  throw new Error(msg)
}

// infinite loop
function gameLoop(): never {
  while(true) {
    console.log('GAME LOOP RUNNING!')
  }
}
