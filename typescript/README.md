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

- 인터페이스는 object type만 묘사할 수 있음
- 인터페이스는 추가 정의가 가능함
- 인터페이스는 상속이 가능하며, 타입 별칭의 경우 `&`를 사용함

## Typescript 컴파일러

---

### Javascript 컴파일하기

- `tsc --init`
  - tsconfig.json 파일 생성
- `tsc fileName.ts`

### 감시 모드

- `tsc -w` | `tsc --watch`
  - listen for changes and recompile

### 여러 파일 다루기

- `tsc`
  - tsconfig.json이 있는 범위 안에서 컴파일

### 파일 컴파일러 옵션

- Typescript 컴파일에 포함할 모든 파일을 나열

### Include 옵션과 Exclude 옵션

- 컴파일에 포함할 파일을 일일이 나열하기 어려울 경우 사용
- files 옵션이 있을 경우 include는 작동하지 않음
- exclude 옵션은 include 옵션에 포함된 것 중 제외할 것을 명시
- exclude의 기본 옵션에 node_modules도 포함되어 있으며, exclude를 재정의할 시 node_modules도 다시 명시해주자

### Outdir 옵션

- TypeScript가 컴파일된 Javascript 파일을 내보낼 위치를 지정
- src 디렉토리와 같은 특정 디렉토리에 TypeScript 파일을 모아두고, 별도의 디렉토리에 Javascript 파일을 컴파일해두고, 이를 실행
  - 통상적으로 폴더 이름은 dist

### Target 옵션

- TypeScript를 컴파일한 Javascript 버전을 제어
- es6(es2015) 이후부터 화살표 함수 지원

### Strict 옵션

- true로 설정할 시 TypeScript 전체의 타입 검사 추가 규칙, 제약 조건이 활성화됨
- strictNullChecks를 켜고, null될 수 있는 상황인 경우 `string[] | null`과 같이 타입에 명시

```json
{
  "compilerOptions": {
    /* Visit https://aka.ms/tsconfig to read more about this file */

    /* Projects */
    // "incremental": true,                              /* Save .tsbuildinfo files to allow for incremental compilation of projects. */
    // "composite": true,                                /* Enable constraints that allow a TypeScript project to be used with project references. */
    // "tsBuildInfoFile": "./.tsbuildinfo",              /* Specify the path to .tsbuildinfo incremental compilation file. */
    // "disableSourceOfProjectReferenceRedirect": true,  /* Disable preferring source files instead of declaration files when referencing composite projects. */
    // "disableSolutionSearching": true,                 /* Opt a project out of multi-project reference checking when editing. */
    // "disableReferencedProjectLoad": true,             /* Reduce the number of projects loaded automatically by TypeScript. */

    /* Language and Environment */
    "target": "es2016",                                  /* Set the JavaScript language version for emitted JavaScript and include compatible library declarations. */
    // "lib": [],                                        /* Specify a set of bundled library declaration files that describe the target runtime environment. */
    // "jsx": "preserve",                                /* Specify what JSX code is generated. */
    // "experimentalDecorators": true,                   /* Enable experimental support for legacy experimental decorators. */
    // "emitDecoratorMetadata": true,                    /* Emit design-type metadata for decorated declarations in source files. */
    // "jsxFactory": "",                                 /* Specify the JSX factory function used when targeting React JSX emit, e.g. 'React.createElement' or 'h'. */
    // "jsxFragmentFactory": "",                         /* Specify the JSX Fragment reference used for fragments when targeting React JSX emit e.g. 'React.Fragment' or 'Fragment'. */
    // "jsxImportSource": "",                            /* Specify module specifier used to import the JSX factory functions when using 'jsx: react-jsx*'. */
    // "reactNamespace": "",                             /* Specify the object invoked for 'createElement'. This only applies when targeting 'react' JSX emit. */
    // "noLib": true,                                    /* Disable including any library files, including the default lib.d.ts. */
    // "useDefineForClassFields": true,                  /* Emit ECMAScript-standard-compliant class fields. */
    // "moduleDetection": "auto",                        /* Control what method is used to detect module-format JS files. */

    /* Modules */
    "module": "commonjs",                                /* Specify what module code is generated. */
    // "rootDir": "./",                                  /* Specify the root folder within your source files. */
    // "moduleResolution": "node10",                     /* Specify how TypeScript looks up a file from a given module specifier. */
    // "baseUrl": "./",                                  /* Specify the base directory to resolve non-relative module names. */
    // "paths": {},                                      /* Specify a set of entries that re-map imports to additional lookup locations. */
    // "rootDirs": [],                                   /* Allow multiple folders to be treated as one when resolving modules. */
    // "typeRoots": [],                                  /* Specify multiple folders that act like './node_modules/@types'. */
    // "types": [],                                      /* Specify type package names to be included without being referenced in a source file. */
    // "allowUmdGlobalAccess": true,                     /* Allow accessing UMD globals from modules. */
    // "moduleSuffixes": [],                             /* List of file name suffixes to search when resolving a module. */
    // "allowImportingTsExtensions": true,               /* Allow imports to include TypeScript file extensions. Requires '--moduleResolution bundler' and either '--noEmit' or '--emitDeclarationOnly' to be set. */
    // "resolvePackageJsonExports": true,                /* Use the package.json 'exports' field when resolving package imports. */
    // "resolvePackageJsonImports": true,                /* Use the package.json 'imports' field when resolving imports. */
    // "customConditions": [],                           /* Conditions to set in addition to the resolver-specific defaults when resolving imports. */
    // "resolveJsonModule": true,                        /* Enable importing .json files. */
    // "allowArbitraryExtensions": true,                 /* Enable importing files with any extension, provided a declaration file is present. */
    // "noResolve": true,                                /* Disallow 'import's, 'require's or '<reference>'s from expanding the number of files TypeScript should add to a project. */

    /* JavaScript Support */
    // "allowJs": true,                                  /* Allow JavaScript files to be a part of your program. Use the 'checkJS' option to get errors from these files. */
    // "checkJs": true,                                  /* Enable error reporting in type-checked JavaScript files. */
    // "maxNodeModuleJsDepth": 1,                        /* Specify the maximum folder depth used for checking JavaScript files from 'node_modules'. Only applicable with 'allowJs'. */

    /* Emit */
    // "declaration": true,                              /* Generate .d.ts files from TypeScript and JavaScript files in your project. */
    // "declarationMap": true,                           /* Create sourcemaps for d.ts files. */
    // "emitDeclarationOnly": true,                      /* Only output d.ts files and not JavaScript files. */
    // "sourceMap": true,                                /* Create source map files for emitted JavaScript files. */
    // "inlineSourceMap": true,                          /* Include sourcemap files inside the emitted JavaScript. */
    // "outFile": "./",                                  /* Specify a file that bundles all outputs into one JavaScript file. If 'declaration' is true, also designates a file that bundles all .d.ts output. */
    "outDir": "./dist",                                   /* Specify an output folder for all emitted files. */
    // "removeComments": true,                           /* Disable emitting comments. */
    // "noEmit": true,                                   /* Disable emitting files from a compilation. */
    // "importHelpers": true,                            /* Allow importing helper functions from tslib once per project, instead of including them per-file. */
    // "importsNotUsedAsValues": "remove",               /* Specify emit/checking behavior for imports that are only used for types. */
    // "downlevelIteration": true,                       /* Emit more compliant, but verbose and less performant JavaScript for iteration. */
    // "sourceRoot": "",                                 /* Specify the root path for debuggers to find the reference source code. */
    // "mapRoot": "",                                    /* Specify the location where debugger should locate map files instead of generated locations. */
    // "inlineSources": true,                            /* Include source code in the sourcemaps inside the emitted JavaScript. */
    // "emitBOM": true,                                  /* Emit a UTF-8 Byte Order Mark (BOM) in the beginning of output files. */
    // "newLine": "crlf",                                /* Set the newline character for emitting files. */
    // "stripInternal": true,                            /* Disable emitting declarations that have '@internal' in their JSDoc comments. */
    // "noEmitHelpers": true,                            /* Disable generating custom helper functions like '__extends' in compiled output. */
    // "noEmitOnError": true,                            /* Disable emitting files if any type checking errors are reported. */
    // "preserveConstEnums": true,                       /* Disable erasing 'const enum' declarations in generated code. */
    // "declarationDir": "./",                           /* Specify the output directory for generated declaration files. */
    // "preserveValueImports": true,                     /* Preserve unused imported values in the JavaScript output that would otherwise be removed. */

    /* Interop Constraints */
    // "isolatedModules": true,                          /* Ensure that each file can be safely transpiled without relying on other imports. */
    // "verbatimModuleSyntax": true,                     /* Do not transform or elide any imports or exports not marked as type-only, ensuring they are written in the output file's format based on the 'module' setting. */
    // "allowSyntheticDefaultImports": true,             /* Allow 'import x from y' when a module doesn't have a default export. */
    "esModuleInterop": true,                             /* Emit additional JavaScript to ease support for importing CommonJS modules. This enables 'allowSyntheticDefaultImports' for type compatibility. */
    // "preserveSymlinks": true,                         /* Disable resolving symlinks to their realpath. This correlates to the same flag in node. */
    "forceConsistentCasingInFileNames": true,            /* Ensure that casing is correct in imports. */

    /* Type Checking */
    "strict": true,                                      /* Enable all strict type-checking options. */
    // "noImplicitAny": true,                            /* Enable error reporting for expressions and declarations with an implied 'any' type. */
    // "strictNullChecks": true,                         /* When type checking, take into account 'null' and 'undefined'. */
    // "strictFunctionTypes": true,                      /* When assigning functions, check to ensure parameters and the return values are subtype-compatible. */
    // "strictBindCallApply": true,                      /* Check that the arguments for 'bind', 'call', and 'apply' methods match the original function. */
    // "strictPropertyInitialization": true,             /* Check for class properties that are declared but not set in the constructor. */
    // "noImplicitThis": true,                           /* Enable error reporting when 'this' is given the type 'any'. */
    // "useUnknownInCatchVariables": true,               /* Default catch clause variables as 'unknown' instead of 'any'. */
    // "alwaysStrict": true,                             /* Ensure 'use strict' is always emitted. */
    // "noUnusedLocals": true,                           /* Enable error reporting when local variables aren't read. */
    // "noUnusedParameters": true,                       /* Raise an error when a function parameter isn't read. */
    // "exactOptionalPropertyTypes": true,               /* Interpret optional property types as written, rather than adding 'undefined'. */
    // "noImplicitReturns": true,                        /* Enable error reporting for codepaths that do not explicitly return in a function. */
    // "noFallthroughCasesInSwitch": true,               /* Enable error reporting for fallthrough cases in switch statements. */
    // "noUncheckedIndexedAccess": true,                 /* Add 'undefined' to a type when accessed using an index. */
    // "noImplicitOverride": true,                       /* Ensure overriding members in derived classes are marked with an override modifier. */
    // "noPropertyAccessFromIndexSignature": true,       /* Enforces using indexed accessors for keys declared using an indexed type. */
    // "allowUnusedLabels": true,                        /* Disable error reporting for unused labels. */
    // "allowUnreachableCode": true,                     /* Disable error reporting for unreachable code. */

    /* Completeness */
    // "skipDefaultLibCheck": true,                      /* Skip type checking .d.ts files that are included with TypeScript. */
    "skipLibCheck": true                                 /* Skip type checking all .d.ts files. */
  },
  // "files": [
  //   "farmstand.ts",
  //   "index.ts"
  // ]
  "include": ["src"],
  "exclude": ["src/dontTouch.ts", "node_modules"]
}

```

## DOM and TypeScript

---

### package manager 설치
- `npm init -y`
  - package.json 생성

### lite-server 설치 및 커맨드 설정
- `npm install lite-server`
- package.json 파일에 `"scripts": { "start": "lite-server" }` 정의
  - npm start 시 lite-server 실행
  - 자동 새로 고침

### DOM 다루기

- document
  - TypeScript는 document 객체 및 해당 프로퍼티와 메서드를 인지한다
  - 브라우저에서 `console.dir(document)`을 통해 객체를 상세히 확인 가능
  - TypeScript의 경우 Go To Type Definition (형식 정의로 이동)을 통해 더 자세히 확인 가능
- TypeScript의 `lib` 옵션은 기본값이 built-in JS APIs, browser environments (DOM APIs) 등으로 설정되어 있다
- `lib: ["DOM"]`

### TypeScript의 Non-Null 단언 연산자 (Non-Null Assertion Operator)

```ts
const btn = document.getElementById('btn') // 타입은 HTMLElement | null

// 1) 자바스크립트 옵셔널 체이닝으로 해결
// 해당 id의 버튼이 있는 경우에만 동작
btn?.addEventListener('click', function() {
  alert('CLICKED!!!')
})

// 2) 타입스크립트 Non-Null 단언 연산자 활용

const btn = document.getElementById('btn')! // null이 아닐 것이라 단언 (타입은 HTMLElement)
btn.addEventListener('click', function() {
  alert('CLICKED!!!')
})

```

### 타입 단언

- 타입스크립트에 직접 타입을 설정
```ts
let mystery: unknown = 'Hello World!'
const numChars = (mystery as string).length // undefined이지만 런타임 이전을 관여하는 타입스크립트에서는 문제 없음

```
- DOM으로 타입 단언하기
```ts
const btn = document.getElementById("btn")! as HTMLButtonElement
const input = document.getElementById("todoinput")! as HTMLInputElement

btn.addEventListener('click', function() {
  alert(input.value)
  input.value = ''
})

```

### 이벤트 다루기

```ts
const form = document.querySelector('form')!

// 이런 식으로 콜백으로 부른 경우 타입스크립트는 context clues를 활용하여 e의 타입이 SubmitEvent임을 안다
form.addEventListener('submit', function(e) {
  e.preventDefault()
  console.log('SUBMITTED!')
})

// 그러나 따로 분리하면 e의 타입을 추론하지 못한다 (타입 명시 필요)
function handleSubmit(e: SubmitEvent) {
  e.preventDefault()
  console.log('SUBMITTED!')
}

form.addEventListener('submit', handleSubmit)

```

### Todo List 만들기

```ts
interface Todo {
  text: string;
  completed: boolean;
}

const btn = document.getElementById("btn")! as HTMLButtonElement; //Type assertion
const input = document.getElementById("todoinput")! as HTMLInputElement;
const form = document.querySelector("form")!;
const list = document.getElementById("todolist")!;

const todos: Todo[] = readTodos();
todos.forEach(createTodo);

// Load todos from local storage
function readTodos(): Todo[] {
  const todosJSON = localStorage.getItem("todos");
  if (todosJSON === null) return [];
  return JSON.parse(todosJSON);
}

// Save todos to local storage
function saveTodos() {
  localStorage.setItem("todos", JSON.stringify(todos));
}

function handleSubmit(e: SubmitEvent) {
  e.preventDefault();
  const newTodo: Todo = {
    text: input.value,
    completed: false,
  };
  createTodo(newTodo);
  todos.push(newTodo);

  saveTodos();
  input.value = "";
}

// DOM에 todo li 추가
function createTodo(todo: Todo) {
  const newLI = document.createElement("li");
  const checkbox = document.createElement("input");
  checkbox.type = "checkbox";
  checkbox.checked = todo.completed;

  checkbox.addEventListener("change", function () {
    todo.completed = checkbox.checked;
    saveTodos();
  });

  newLI.append(todo.text);
  newLI.append(checkbox);
  list.append(newLI);
}

form.addEventListener("submit", handleSubmit);

```
