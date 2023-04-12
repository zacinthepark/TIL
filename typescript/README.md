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

```ts
// parameter type

function printName(person: {first: string, last: string}): void {
  console.log(`${person.first} ${person.last}`)
}

printName({first: 'Thomas', last: 'Jenkins'})

// let coordinate: {x: number, y: number} = {x: 34, y: 2}

// return type

function randomCoordinate(): {x: number, y: number} {
  return {x: Math.random(), y: Math.random()}
}

// 초과 프로퍼티

// 아래와 같이 직접 객체 리터럴을 전달하면 에러가 발생하지만
// 따로 변수에 저장하여 전달하면 지정된 프로퍼티 외에는 그냥 무시함
// printName({first: 'Mick', last: 'Jagger', age: 473})
const singer = {first: 'Mick', last: 'Jagger', age: 473}
printName(singer)

// Type Alias

type Point = {
  x: number,
  y: number
}

let coordinate: Point = {x: 34, y: 2}

function doublePoint(point: Point): Point {
  return {x: point.x *2, y:point.y * 2}
}

// Nested Objects

type Song = {
  title: string,
  artist: string,
  numStreams: number,
  credits: {
    producer: string,
    writer: string
  }
}

function calculatePayout(song: Song): number {
  return song.numStreams * 0.0033
}

function printSong(song: Song): void {
  console.log(`${song.title} - ${song.artist}`)
}

const mySong: Song = {
  title: "Unchained Melody",
  artist: 'Righteous Brothers',
  numStreams: 12873321,
  credits: {
    producer: 'Phil Spector',
    writer: 'Alex North'
  }
}

const earnings = calculatePayout(mySong)
console.log(earnings)
printSong(mySong)

// 선택적 프로퍼티

type Coordinate = {
  x: number,
  y: number,
  z?: number
}

const myCoordinate = {x: 1, y: 3}

// readonly

// primitive type인 경우 재할당 불가
// reference type인 경우 추가, 갱신 등 가능
type User = {
  readonly id: number, 
  username: string
}

const user: User = {
  id: 12837,
  username: 'catgurl'
}
// user.id = 289391283

// 교차 타입(Intersection Type)


type Circle = {
  radius: number
}
type Colorful = {
  color: string
}

type ColorfulCircle = Circle & Colorful

const happyFace: ColorfulCircle = {
  radius: 4,
  color: 'yellow'
}

type Cat = {
  numLives: number,
}
type Dog = {
  breed: string
}

type CatDog = Cat & Dog & {
  age: number
}

const christy: CatDog = {
  numLives: 7,
  breed: 'Husky',
  age: 9
}
```
