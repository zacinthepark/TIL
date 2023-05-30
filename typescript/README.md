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

## Index

---

- [설치 및 설정](#설치-및-설정)
- [타입 애너테이션 기초](#타입-애너테이션-기초)
- [함수](#함수)
- [객체 타입](#객체-타입)
- [배열](#배열)
- [유니온 타입](#유니온-타입)
- [튜플(Tuple)과 Enum](#튜플tuple과-enum)
- [인터페이스](#인터페이스)
- [Typescript 컴파일러](#typescript-컴파일러)
- [DOM and TypeScript](#dom-and-typescript)
- [JavaScript 클래스](#javascript-클래스)
- [TypeScript 클래스](#typescript-클래스)
- [제네릭](#제네릭)
- [Type Narrowing](#type-narrowing)
- [Type Declaration and Third-party Library](#type-declaration-and-third-party-library)
- [모듈](#모듈)
- [Webpack과 TypeScript](#webpack과-typescript)
- [React와 TypeScript](#react와-typescript)

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

## JavaScript 클래스

---

- 클래스와 Type Alias, Interface와의 차이는 클래스는 인스턴스화가 가능하다는 것
- private 속성 `#`은 클래스 정의 안에서만 조작할 수 있도록 하는 것
- `static` 속성은 해당 프로퍼티나 메서드가 클래스 자체에 존재하며 개별 인스턴스에는 없다는 것
- `super()`는 자식 클래스에 생성자를 추가할 때 사용

```js
class Player {
  static description = 'Player In Our Game' // Player.description
  #score = 0  // private property (과거에는 _score와 같이 썼지만 동작을 막지는 않았음)
  #numLives = 10

  constructor(first, last) {
    console.log('IN CONSTRUCTOR!')
    this.first = first
    this.last = last
    this.#secret()
  }

  static randomPlayer() {
    return new Player('Andy', 'Samberg')
  }

  get fullName() {
    return `${this.first} ${this.last}`
  }
  set fullName(newName) {
    const [first, last] = newName.split(' ')
    this.first = first
    this.last = last
  }

  get score() {
    return this.#score
  }
  set score(newScore) {
    if (newScore < 0) {
      throw new Error('Score must be positive!')
    }
    this.#score = newScore
  }

  // getScore() {
  //   return this.#score
  // }
  // updateScore(newScore) {
  //   this.#score = newScore
  // }
  getNumLives() {
    return this.#numLives
  }
  taunt() {
    console.log('BOOYAH!')
  }
  loselife() {
    this.#numLives -= 1
  }
  #secret() {
    console.log('SECRET!')
  }
}

class AdminPlayer extends Player {
  constructor(first, last, powers) {
    super(first, last)
    this.powers = powers
  }

  isAdmin = true
}

const admin = new AdminPlayer('admin', 'mCadmin', ["delete", "restore world"])
console.log('admin: ', admin)

const player1 = new Player('blue', 'steele')
// player1.taunt()
// console.log(player1.first)
// console.log(player1.last)
console.log(player1.fullName)
player1.fullName = 'Amy Adams'
console.log(player1.fullName)

console.log(player1.score)
player1.score = 320
console.log(player1.score)
// console.log(player1.getScore())
// player1.updateScore(28)
// console.log(player1.numLives)
// player1.loselife()
// console.log(player1.numLives)
console.log('player1: ', player1)

const player2 = new Player('charlie', 'brown')
// player2.taunt()
// console.log(player2.first)
// console.log(player2.last)
console.log('player2: ', player2)

```

## TypeScript 클래스

---

- public, private 프로퍼티 설정 가능
- protected 제어자는 상속과 관련된 것으로, private은 해당 클래스 내에서만 접근 가능한 것과 달리 protected는 자식 클래서에서는 접근 가능
- `implements`는 해당 규칙을 준수한다는 것
- `abstract` 클래스는 인스턴스화 할 수 없음
  - 패턴을 정의하고 자식 클래스에서 시행되어야 하는 메서드를 정의하는데 사용
  - `interface`와의 차이점은 interface는 객체의 형태만 설명하는데 반해, abstract 클래스의 경우 그 자체 클래스에서 기능과 데이터를 정의할 수 있음
  - 해당 클래스는 extends할 경우 기능을 상속할 수도 있으며, `abstract`를 불인 부분을 충족시키도록 제약도 거는 것임

```ts
class Player {
  // public readonly first: string
  // public readonly last: string
  // private score: number = 0
  // constructor(first: string, last: string) {
  //   this.first = first
  //   this.last = last
  //   this.secretMethod()
  // }
  constructor(
    public first: string,
    public last: string,
    protected _score: number
  ) {}

  private secretMethod(): void {
    console.log("SECRET METHOD!!");
  }

  get fullName(): string {
    return `${this.first} ${this.last}`;
  }

  get score(): number {
    return this._score;
  }

  set score(newScore: number) {
    if (newScore < 0) {
      throw new Error("Score cannot be negative!");
    }
    this._score = newScore;
  }
}

class SuperPlayer extends Player {
  public isAdmin: boolean = true;
  maxScore() {
    this._score = 99999999;
  }
}

const elton = new Player("Elton", "Steele", 100);
elton.fullName;
// elton.score = "23";

// Classes With Interfaces!
interface Colorful {
  color: string;
}

interface Printable {
  print(): void;
}

class Bike implements Colorful {
  constructor(public color: string) {}
}

class Jacket implements Colorful, Printable {
  constructor(public brand: string, public color: string) {}

  print() {
    console.log(`${this.color} ${this.brand} jacket`);
  }
}

const bike1 = new Bike("red");
const jacket1 = new Jacket("Prada", "black");

abstract class Employee {
  constructor(public first: string, public last: string) {}
  abstract getPay(): number;
  greet() {
    console.log("HELLO!");
  }
}

class FullTimeEmployee extends Employee {
  constructor(first: string, last: string, private salary: number) {
    super(first, last);
  }
  getPay(): number {
    return this.salary;
  }
}

class PartTimeEmployee extends Employee {
  constructor(
    first: string,
    last: string,
    private hourlyRate: number,
    private hoursWorked: number
  ) {
    super(first, last);
  }
  getPay(): number {
    return this.hourlyRate * this.hoursWorked;
  }
}

const betty = new FullTimeEmployee("Betty", "White", 95000);
console.log(betty.getPay());

const bill = new PartTimeEmployee("Bill", "Billerson", 24, 1100);
console.log(bill.getPay());

```

## 제네릭

---

- Built-in Generics
  - `Array<T>` 라는 인터페이스에 다양한 타입 지정 가능
    ```ts
    // const nums: number[] = []
    const nums: Array<number> = []
    const colors: Array<string> = []
    ```
  - 제네릭 함수인 `querySelector`에서 타입을 받아 해당 타입의 요소를 반환해줌
    ```ts
    const inputElement = document.querySelector<HTMLInputElement>('#username')!
    inputElement.value = 'Hacked!'
    ```
- 타입을 특정 타입으로 구현하고 싶지만, 그 타입이 무엇인지 정해놓지 않고자 할 때, 제네릭을 활용할 수 있음
- `.tsx` 파일에서 화살표 함수를 쓰고자 한다면 타입 뒤에 trailing comma를 붙여줘야함
  ```tsx
  // function getRandomElement<T>(list: T[]): T {
  //   const randIdx = Math.floor(Math.random() * list.length);
  //   return list[randIdx];
  // }

  const getRandomElement = <T,>(list: T[]): T => {
    const randIdx = Math.floor(Math.random() * list.length);
    return list[randIdx];
  }
  ```

```ts
// Providing a type to querySelector:
const inputEl = document.querySelector<HTMLInputElement>("#username")!;
console.dir(inputEl);
inputEl.value = "Hacked!";

const btn = document.querySelector<HTMLButtonElement>(".btn")!;

// Without Generics...Lots of Repetition!
function numberIdentity(item: number): number {
  return item;
}
function stringIdentity(item: string): string {
  return item;
}
function booleanIdentity(item: boolean): boolean {
  return item;
}

// function identity(item: any): any{
//   return item;
// }

// With A Generic...Super Reusable!
function identity<T>(item: T): T {
  return item;
}

identity<number>(7);
identity<string>("hello");

function getRandomElement<T>(list: T[]): T {
  const randIdx = Math.floor(Math.random() * list.length);
  return list[randIdx];
}

console.log(getRandomElement<string>(["a", "b", "c"]));
getRandomElement<number>([5, 6, 21, 354, 567, 234, 654]);

// Generic Type Inference
getRandomElement([1, 2, 3, 4]);

// Generics With Constraints:
function merge<T extends object, U extends object>(object1: T, object2: U) {
  return {
    ...object1,
    ...object2,
  };
}

// Type Inference
const comboObj = merge({ name: "colt" }, { pets: ["blue", "elton"] });
console.log(merge({ name: "Colt" }, { num: 9 }));
// Without Type Inference
merge<{ name: string }, { pets: string[] }>(
  { name: "colt" },
  { pets: ["blue", "elton"] }
);

interface Lengthy {
  length: number;
}

// Generics With Custom Constraints:
function printDoubleLength<T extends Lengthy>(thing: T): number {
  return thing.length * 2;
}

// function printDoubleLength(thing: Lengthy): number {
//   return thing.length * 2;
// }

printDoubleLength("asdasd");
printDoubleLength(234); //Not allowed!

// Generics with Default Type
function makeEmptyArray<T = number>(): T[] {
  return [];
}

const nums = makeEmptyArray();
const bools = makeEmptyArray<boolean>();

// A Generic Class Example
interface Song {
  title: string;
  artist: string;
}
interface Video {
  title: string;
  creator: string;
  resolution: string;
}

class Playlist<T> {
  public queue: T[] = [];
  add(el: T) {
    this.queue.push(el);
  }
}

const songs = new Playlist<Song>();
const videos = new Playlist<Video>();

```

## Type Narrowing

---

```ts
// Typeof Narrowing:
// typeof 가드는 string, number, boolean과 같은 원시 타입을 처리하는데 유용함

function triple(value: number | string) {
  if (typeof value === "string") {
    return value.repeat(3);
  }
  return value * 3;
}

const el = document.getElementById("idk");
if (el) {
  el;
} else {
  el;
}

// Truthiness Narrowing:

const printLetters = (word?: string) => {
  if (word) {
    for (let char of word) {
      console.log(char);
    }
  } else {
    console.log("YOU DID NOT PASS IN A WORD!");
  }
};

// EQUALITY NARROWING

function someDemo(x: string | number, y: string | boolean) {
  if (x === y) {
    x.toUpperCase();
  }
}

// IN Operator Narrowing

interface Movie {
  title: string;
  duration: number;
}

interface TVShow {
  title: string;
  numEpisodes: number;
  episodeDuration: number;
}

function getRuntime(media: Movie | TVShow) {
  if ("numEpisodes" in media) {
    return media.numEpisodes * media.episodeDuration;
  }
  return media.duration;
}

console.log(getRuntime({ title: "Amadeus", duration: 140 }));
console.log(
  getRuntime({ title: "Spongebob", numEpisodes: 80, episodeDuration: 30 })
);

// Instanceof Narrowing:

function printFullDate(date: string | Date) {
  if (date instanceof Date) {
    console.log(date.toUTCString());
  } else {
    console.log(new Date(date).toUTCString());
  }
}

// Instanceof Narrowing:

class User {
  constructor(public username: string) {}
}
class Company {
  constructor(public name: string) {}
}

function printName(entity: User | Company) {
  if (entity instanceof User) {
    entity;
  } else {
    entity;
  }
}

// Type Predicates (타입 명제)

interface Cat {
  name: string;
  numLives: number;
}
interface Dog {
  name: string;
  breed: string;
}

// ": pet is dog" --> type predicate
function isCat(animal: Cat | Dog): animal is Cat {
  // as: type casting
  return (animal as Cat).numLives !== undefined;
}

function makeNoise(animal: Cat | Dog): string {
  // pet get passed to isCat above to narrow type
  if (isCat(animal)) {
    animal;
    return "Meow";
  } else {
    animal;
    return "Woof!";
  }
}

// Discriminated Unions (판별 유니온)
// Exhaustiveness Check (소진 검사)와 Never

interface Rooster {
  name: string;
  weight: number;
  age: number;
  kind: "rooster";  // 타입 판별을 쉽게 하기 위하여 literal type property를 추가
}

interface Cow {
  name: string;
  weight: number;
  age: number;
  kind: "cow";
}

interface Pig {
  name: string;
  weight: number;
  age: number;
  kind: "pig";
}

interface Sheep {
  name: string;
  weight: number;
  age: number;
  kind: "sheep";
}

type FarmAnimal = Pig | Rooster | Cow | Sheep;

function getFarmAnimalSound(animal: FarmAnimal) {
  switch (animal.kind) {
    case "pig":
      return "Oink!";
    case "cow":
      return "Moooo!";
    case "rooster":
      return "Cockadoodledoo!";
    case "sheep":
      return "Baaa!";
    default:
      // We should never make it here, if we handled all cases correctly
      //   const shouldNeverGetHere: never = animal;
      //   return shouldNeverGetHere
      const _exhaustiveCheck: never = animal;
      return _exhaustiveCheck;
  }
}

const stevie: Rooster = {
  name: "Stevie Chicks",
  weight: 2,
  age: 1.5,
  kind: "rooster",
};

console.log(getFarmAnimalSound(stevie));

```

## Type Declaration and Third-party Library

---

- `.d.ts` files
  - declaration files contain *only* type information
  - these files don't produce `.js` outputs
- type declaration file이 없는 라이브러리의 경우 `@types/`를 붙여 패키지 설치
  - [DefinitelyTyped](https://github.com/DefinitelyTyped/DefinitelyTyped)
  - `index.d.ts` 파일 확인

```ts
import axios from "axios";
import _ from "lodash";
interface User {
  id: number;
  name: string;
  username: string;
  email: string;
  address: {
    street: string;
    suite: string;
    city: string;
    zipcode: string;
    geo: {
      lat: string;
      lng: string;
    };
  };
  phone: string;
  website: string;
  company: {
    name: string;
    catchPhrase: string;
    bs: string;
  };
}

axios
  .get<User>("https://jsonplaceholder.typicode.com/users/1")
  .then((res) => {
    console.log("WOO!!!");
    printUser(res.data);
  })
  .catch((e) => {
    console.log("ERROR!", e);
  });

axios
  .get<User[]>("https://jsonplaceholder.typicode.com/users")
  .then((res) => {
    console.log("WOO!!!");
    res.data.forEach(printUser);
  })
  .catch((e) => {
    console.log("ERROR!", e);
  });

function printUser(user: User) {
  console.log(user.name);
  console.log(user.email);
  console.log(user.phone);
}

```

## 모듈

---

- Non-modules 작동 방식도 가능하긴 하다
  - 타입스크립트는 `export`하지 않는 파일들에 대해서 모듈이 아닌 스크립트 파일로 인식하며, 스크립트 파일들끼리는 동일한 전역 스코프에 있다고 간주함
  - 이를 자바스크립트로 컴파일했을 때 알맞은 순서대로 스크립트가 실행되도록 개발자가 처리할 것이라 생각하는 것
- module 파일 컴파일 시 옵션을 `CommonJS`로 하면 Node 환경에서는 실행이 되나, 브라우저에서는 에러 발생
  - `tsconfig` 파일에서 `module` 옵션을 `ES6` 등으로 변경
- `<script type="module" src="./dist/index.js"></script>`
- type을 import할 경우
  - `import type { Person }, ... from "./types.js"`
  - `import { type Person, ... } from "./types.js"`

## Webpack과 TypeScript

---

### Webpack 기초구성

- `npm install --save-dev webpack webpack-cli typescript ts-loader`
  - webpack은 모듈 번들러
  - webpack-cli는 webpack의 cli interface
  - typescript를 다시 설치하는 이유는 devDependencies에 타입스크립트를 사용하고 있음을 확실히 보여주기 위해
  - ts-loader는 타입스크립트와 웹팩의 중간자 역할
    - 타입스크립트를 자바스크립트로 컴파일하여 웹팩으로 전달하는 역할
- webpack.config.js 설정
- import 시 .js로 되어있는 부분을 인식하지 못할 수 있으니 .js 제거
- package.json의 scripts에 build 옵션 webpack 설정해주고 빌드
- index.html에 bundle.js를 연결

### 소스 맵 추가하기

- 소스 맵은 단순화되어 있는 번들을 가지고 역매핑을 통해 빌드 전의 상태를 보여줌으로써 번들을 구성하고 있는 코드가 어디서 오는지를 보여줌
- tsconfig.json 파일 내에 sourceMap을 true로 설정
- webpack.config.js 파일 내의 Webpack에게 해당 소스 맵을 추출해 최종 번들에 포함하라고 지시
  - `devtool: 'inline-source-map'`
- 개발자 도구 Sources 탭에서 webpack_ts 확인 가능

### Webpack 개발서버

- `mode: "development"` 옵션 추가
- 이 경우에는 번들 시 경량화되지 않음
- `npm install --save-dev webpack-dev-server`
  - 라이브 서버로 번들링도 백그라운드, 메모리에서 처리
  - 매번 별도의 번들 파일로 만들어 dist에 쓰는 대신 개발 과정 동안 메모리에 번들을 보관
- scripts에 `"serve": "webpack serve"`

### 프로덕션 구성

- 개발용과 프로덕션용 configuration을 구분해보자
- webpack.prod.js라는 별도의 웹팩 설정 파일 생성
  - `mode: "production"`
- scripts에서 `"build": "webpack --config webpack.prod.js"`
- `npm install --save-dev clean-webpack-plugin`
  - webpack 환경설정 파일에 `const { CleanWebpackPlugin } = require("clean-webpack-plugin")`, `plugins: [new CleanWebpackPlugin()]` 추가
  - `filename: "[contenthash]bundle.js"`와 같이 파일 변동사항이 있을 때 다른 번들 파일들이 계속 생겨나게 되는데, clean-webpack-plugin은 빌드용 폴더를 최신 번들만 남기고 정리해줌

## React와 TypeScript

---

### TypeScript로 React 앱 만들기

Create React App
- `npx create-react-app my-app --template typescript`
- `yarn create react-app my-app --template typescript`
- CRA의 Webpack이 tsx의 컴파일을 대신해줌

### props

```tsx
// App.tsx

function App() {
  return (
    <div className="App">
      <Greeter person='Colt' />
      <Greeter person='Blue' />
      <Greeter person='Elton' />
    </div>
  );
}

// Greeter.tsx

import React from 'react'

// 1
function Greeter(props: { person: string }): JSX.Element {
  return <h1>Hello {props.person}!</h1>
}

// 2
interface GreeterProps {
  person: string
}

function Greeter(props: GreeterProps): JSX.Element {
  return <h1>Hello {props.person}!</h1>
}

// 3
interface GreeterProps {
  person: string
}

function Greeter({ person }: GreeterProps): JSX.Element {
  return <h1>Hello {person}!</h1>
}

// React Functional Component의 다른 선언법
// const Greeter: React.FC = () => {
//   return <h1>Hello!</h1>
// }

export default Greeter

```

### useState, useRef

- useState, useRef와 같은 훅들은 제네릭으로 구현되어있음
- useState는 어떤 타입의 자료를 다룰 것인지, useRef는 어떤 타입의 DOM element를 다룰 것인지 지정

```tsx
// App.tsx

import React, {useState} from 'react';
// import Greeter from './components/Greeter';
import ShoppingList from './components/ShoppingList';
import ShoppingListForm from './components/ShoppingListForm';
import Item from './models/items';
import { v4 as getId } from 'uuid';
import './App.css';

function App() {
  const [items, setItems] = useState<Item[]>([])
  const addItem = (product: string, quantity: number) => {
    console.log('MADE IT TO THE APP COMPONENT!')
    setItems([...items, {id: getId(), product: product, quantity: quantity}])
  }
  // const items = [
  //   {id: 1, product: 'Lemon', quantity: 3},
  //   {id: 2, product: 'Chicken Breast', quantity: 2}
  // ]
  return (
    <div>
      <ShoppingList items={items} />
      <ShoppingListForm onAddItem={addItem} />
    </div>
  );
}

export default App;

// ./components/ShoppingList.tsx

import React from "react";
import Item from '../models/items'

interface ShoppingListProps {
  items: Item[]
}

function ShoppingList(props: ShoppingListProps): JSX.Element {
  return (
    <div>
      <h1>Shopping List</h1>
      {props.items && <ul>
        {props.items.map((item) => (
          <li key={item.id}>{item.product} - {item.quantity}</li>
        ))}
      </ul>}
    </div>
  )
}

export default ShoppingList

// ./components/ShoppingListForm.tsx

import React, { useRef } from "react";

interface ShoppingListFormProps {
  onAddItem: (item: string, quantity: number) => void;
}

function ShoppingListForm({ onAddItem }: ShoppingListFormProps): JSX.Element {
  const productInputRef = useRef<HTMLInputElement>(null)
  const quantityInputRef = useRef<HTMLInputElement>(null)

  function handleSubmit(event: React.FormEvent) {
    event.preventDefault()
    const newProduct = productInputRef.current!.value
    const quantity = parseInt(quantityInputRef.current!.value)
    onAddItem(newProduct, quantity)
    productInputRef.current!.value = ''
    quantityInputRef.current!.value = '1'
  }

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" placeholder="Product Name" ref={productInputRef} />
      <input type="number" min={0} ref={quantityInputRef} />
      <button type="submit">Add Item</button>
    </form>
  )
}

export default ShoppingListForm

// ./models/items.ts

export default interface Item {
  id: string,
  product: string,
  quantity: number
}

```
