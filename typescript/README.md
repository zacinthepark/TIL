## Why?

---

![banana](https://user-images.githubusercontent.com/86648892/231346435-4d569727-b3c3-4632-96bb-5c471c442697.png)

```js
null * 213 // 0
undefined * 8976 // NaN
const shape = { width: 14, height: 12 };
shape.heigth // undefined
```

> Typescript is a static type checker. Detects errors in our code without running it. Javascript compiles and runs the code.

## 설치 및 설정

---

- `npm install -g typescript`
- `tsc -v`
- `.ts` 파일 확장자
- `tsc`
  - compiles into js code

## 타입 애너테이션 기초

---

### Type Annotation

```ts
let movieTitle: string = 'Amadeus'
movieTitle = 'Arrival'
// movieTitle = 9
movieTitle.toUpperCase()

let numCatLives: number = 42
numCatLives = 60
numCatLives += 1
// numCatLives = 'Hello'

let gameOver: boolean = false
gameOver = true
// gameOver = 'true'
```

### Type Inference

```ts
let tvShow = 'Olive Kitteridge'
tvShow = 'The Other Two'
// tvShow = false
```

### Any Type

```ts
let thing: any = 'hello'
thing = 1
thing = false
thing()
thing.toUpperCase()
```

### Implicit Typing

```ts
const movies = ['Arrival', 'The Thing', 'Aliens', 'Amadeus']
let foundMovie: string
for (let movie of movies) {
  if (movie === 'Amadeus') {
    foundMovie = 'Amadeus'
  }
}
```

## 함수

---

```ts
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
```

## 객체 타입

---

