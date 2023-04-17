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

```ts
// String Variable With Explicit Annotation
let movieTitle: string = "Amadeus";
movieTitle = "Arrival";
movieTitle = 9; //This results in an error!
movieTitle.toUpperCase();

// Number Variable with explicit annotation
let numCatLives: number = 9;
numCatLives += 1;
numCatLives = "zero"; //Error!

// Explicitly typed boolean variable:
let gameOver: boolean = false;
gameOver = true;
gameOver = "true"; //error!!

// Type Inference
let tvShow = "Olive Kitteridge";
tvShow = "The Other Two";
tvShow = false;

let isFunny = false;
isFunny = true;
isFunny = "asd";

// the any type
let thing: any = "hello"; //This is not a great idea!
thing = 1;
thing = false;
thing();
thing.toUpperCase();

const movies = ["Arrival", "The Thing", "Aliens", "Amadeus"];
let foundMovie: string;

for (let movie of movies) {
  if (movie === "Amadeus") {
    foundMovie = "Amadeus";
  }
}

```

## 함수

---

```ts
// Function parameter type annotations:
const doSomething = (person: string, age: number, isFunny: boolean) => {};

// Return type annotation:
function greet(person: string = "stranger"): string {
  return `Hi there, ${person}!`;
}

function square(num: number): number {
  return num * num;
}

square(3);
greet("Tonya Harding");
doSomething("ChickenFace", 78, true);

// Arrow function:
const add = (x: number, y: number): number => {
  return x + y;
};

// Contextual Type Clues
const colors = ["red", "orange", "yellow"];
colors.map((color) => {
  return color.toUpperCase();
});

// Void
function printTwice(msg: string): void {
  console.log(msg);
  console.log(msg);
}

// Never
function makeError(msg: string): never {
  throw new Error(msg);
}

function gameLoop(): never {
  while (true) {
    console.log("GAME LOOP RUNNING!");
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

## 배열

---

```ts
// String array
const activeUsers: string[] = [];
activeUsers.push("Tony");

// Array of numbers
const ageList: number[] = [45, 56, 13];
ageList[0] = 99;

// Alternate Syntax:
// const bools: Array<boolean> = []
const bools: boolean[] = [];

type Point = {
  x: number;
  y: number;
};

const coords: Point[] = [];
coords.push({ x: 23, y: 8 });

// Multi-dimensional string array
const board: string[][] = [
  ["X", "O", "X"],
  ["X", "O", "X"],
  ["X", "O", "X"],
];

const demo: number[][][] = [[[1]]]

```

## 유니온 타입

---

```ts
// Basic Union Type:
let age: number | string = 21;
age = 23;
age = "24";

type Point = {
  x: number;
  y: number;
};

type Loc = {
  lat: number;
  long: number;
};

// Union type with type aliases
let coordinates: Point | Loc = { x: 1, y: 34 };
coordinates = { lat: 321.213, long: 23.334 };

// Function parameter union type:
function printAge(age: number | string): void {
  console.log(`You are ${age} years old`);
}

function calculateTax(price: number | string, tax: number) {
  if (typeof price === "string") {
    price = parseFloat(price.replace("$", ""));
  }
  return price * tax;
}

// const nums: number[] = [1,2,3,4]
// const stuff: any[] = [1,2,3,4, true, "asdas", {}]

// const stuff: (number | string)[] = [1,2,3, "das"]
// const stuff: number[] | string[] = ["asd", "asd", 1]

// Union Type With Arrays
const coords: (Point | Loc)[] = [];
coords.push({ lat: 321.213, long: 23.334 });
coords.push({ x: 213, y: 43 });

// Literal Types
let zero: 0 = 0;
let mood: "Happy" | "Sad" = "Happy";
mood = "Sad";

type DayOfWeek =
  | "Monday"
  | "Tuesday"
  | "Wednesday"
  | "Thursday"
  | "Friday"
  | "Saturday"
  | "Sunday";

let today: DayOfWeek = "Sunday";

```

## 튜플(Tuple)과 Enum

---

Tuples are arrays of fixed lengths and ordered with specific types
Enums allow us to define a set of named constants

```ts
// These are NOT tuples:
// const stuff: (string | number)[] = [1,'asd', 'asdasd', 'asdasd', 2]
// const color: number[] = [23,45,234,234]

// This is a tuple!
const color: [number, number, number] = [255, 0, 45];

type HTTPResponse = [number, string];

const goodRes: HTTPResponse = [200, "OK"];

// typescript는 정의된 것과 다른 동작에 대해 오류를 표시하지만, 튜플 정의 후 push, pop 동작에는 관여하지 않음 (한계)
// goodRes.push(123)
// goodRes.pop()

// An array of tuples:
const responses: HTTPResponse[] = [
  [404, "Not Found"],
  [200, "OK"],
];

// Enum Example:
// 관례상 대문자로 많이 정의함
enum OrderStatus {
  PENDING,
  SHIPPED,
  DELIVERED,
  RETURNED,
}
const myStatus = OrderStatus.DELIVERED;

function isDelivered(status: OrderStatus) {
  return status === OrderStatus.DELIVERED;
}

isDelivered(OrderStatus.RETURNED);

// String Enum:
// rawValue 지정 가능
enum ArrowKeys {
  UP = "up",
  DOWN = "down",
  LEFT = "left",
  RIGHT = "right",
}

```

<img width="1891" alt="스크린샷 2023-04-17 오후 10 52 53" src="https://user-images.githubusercontent.com/86648892/232504963-c2479977-7d0f-435c-8aba-ee922d5d6578.png">

<img width="1855" alt="스크린샷 2023-04-17 오후 10 53 08" src="https://user-images.githubusercontent.com/86648892/232504947-afbab0ef-80f3-4525-aa16-cea268371340.png">

## 인터페이스

---

Describe the shape of objects (only objects)

```ts
// Point as a TYPE ALIAS
// type Point = {
//     x: number,
//     y: number
// }

// const pt: Point = {x: 213, y:12}

// Point using an INTERFACE:
interface Point {
  x: number;
  y: number;
}

const pt: Point = { x: 123, y: 1234 };

interface Person {
  readonly id: number;
  first: string;
  last: string;
  nickname?: string;
  // sayHi: () => string;
  sayHi(): string;
}

const thomas: Person = {
  first: "Thomas",
  last: "Hardy",
  nickname: "Tom",
  id: 21837,
  sayHi: () => {
    return "Hello!";
  },
};

thomas.first = "kasjdh";
// thomas.id = 238974;

interface Product {
  name: string;
  price: number;
  applyDiscount(discount: number): number;
}

const shoes: Product = {
  name: "Blue Suede Shoes",
  price: 100,
  applyDiscount(amount: number) {
    const newPrice = this.price * (1 - amount);
    this.price = newPrice;
    return this.price;
  },
};

console.log(shoes.applyDiscount(0.4));

// Re-opening an interface:
// type 선언은 이와 같은 추가 선언이 불가함
interface Dog {
  name: string;
  age: number;
}

interface Dog {
  breed: string;
  bark(): string;
}

const elton: Dog = {
  name: "Elton",
  age: 0.5,
  breed: "Australian Shepherd",
  bark() {
    return "WOOF WOOF!";
  },
};

// 인터페이스 상속 기능
// Extending an interface:
interface ServiceDog extends Dog {
  job: "drug sniffer" | "bomb" | "guide dog";
}

const chewy: ServiceDog = {
  name: "Chewy",
  age: 4.5,
  breed: "Lab",
  bark() {
    return "Bark!";
  },
  job: "guide dog",
};

interface Human {
  name: string;
}

interface Employee {
  readonly id: number;
  email: string;
}

// Extending multiple interfaces
interface Engineer extends Human, Employee {
  level: string;
  languages: string[];
}

const pierre: Engineer = {
  name: "Pierre",
  id: 123897,
  email: "pierre@gmail.com",
  level: "senior",
  languages: ["JS", "Python"],
};

```

### Interface vs Type Alias

