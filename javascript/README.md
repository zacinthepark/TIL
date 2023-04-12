# JavaScript Basics

- [JavaScript 기초 문법](#javascript-기초-문법)
- [JavaScript DOM and Event](#javascript-dom-and-event)
- [Javascript async and axios and promise](#javascript-async-and-axios-and-promise)

---

# JavaScript 기초 문법

- Starting JavaScript
- JavaScript 기초 문법
- 함수
- Array와 Object

---

# Starting JavaScript

## JavaScript를 배워야하는 이유

### 1. Web 기술의 기반이 되는 언어

- HTML 문서의 콘텐츠를 **동적으로 변경**할 수 있는 언어
- Web이라는 공간에서 채팅, 게임 등 다양한 동작을 할 수 있게된 기반

<img width="687" alt="js1" src="https://user-images.githubusercontent.com/86648892/196928159-d098732a-1c61-4677-bc19-eaa6b906dae0.png">

### 2. 다양한 분야로 확장이 가능한 언어

- JavaScript는 Web을 위해 탄생한 언어로, 초기에는 언어의 특성상 많은 개발자에게 환영받지 못함
- 하지만 버전이 올라가면서 하나의 단단한 언어로 자리매김을 한 언어
- 단순히 Web 조작을 넘어서 서버 프로그래밍, 모바일 서비스, 컴퓨터 응용프로그래밍, 블록체인, 게임 개발 등 **다양한 분야에서 활용이 가능한 언어**가 됨
- 과거에는 단순히 Web Front-end를 위해서만 JavaScript 개발자를 찾았다면 이제는 그 영역이 매우 넓어져 다양한 직군에서 찾는 언어가 됨

### 3. 현재 가장 인기있는 언어

- 언어의 확장성만큼 큰 인기를 얻고 있는 언어

<img width="1533" alt="js2" src="https://user-images.githubusercontent.com/86648892/196928152-b4fb7e1d-ac9c-4ccb-a374-438cb3bdf21c.png">

---

## JavaScript의 역사

### Web Browser의 역할

- JavaScript는 Web을 조작하기위한 언어인만큼 Web Browser와도 깊은 연관관계가 있음
- URL을 통해 Web(WWW)을 탐색함
- `HTML/CSS/JavaScript` 를 이해한 뒤 해석해서 사용자에게 하나의 화면으로 보여줌
- 웹 서비스 이용 시 클라이언트의 역할을 함
- 즉, 웹 페이지 코드를 이해하고, 보여주는 역할을 하는 것이 웹 브라우저

### 웹 브라우저와 스크립트 언어

<img width="869" alt="js3" src="https://user-images.githubusercontent.com/86648892/196928147-1cf5f248-0548-4eeb-a45d-a2669b9493dc.png">

- 이 때까지만 해도 정적 웹 페이지를 단순히 보여주는 용도에 그침
- 웹 브라우저에 탑재해서 웹 페이지를 동적으로 바꿔줄 Script 언어 개발 필요
  - **Script 언어**
    - 소스 코드를 기계어로 바꿔주는 컴파일러없이 바로 실행가능한 언어
    - 속도가 느리다는 단점이 있음
- Netscape에서 약 10일의 개발 기간을 통해 Script 언어인 **Mocha**를 개발
- 이후 **LivsScript**로 이름 변경 후 브라우저에 LivsScript를 해석해주는 Engine을 내장
- 이후 당시 인기있던 JAVA의 명성에 기대보고자 **JavaScript**로 이름 변경

<img width="802" alt="js4" src="https://user-images.githubusercontent.com/86648892/196928144-49fe1f2a-183d-47f3-8448-ffa06240e0bb.png">

- “Netscape가 너무 잘나가는데? 우리도 Web Browser를 만들어보자”
- **JavaScript**를 그대로 복사한 **JScript**라는 언어 제작 후 이를 탑재한 Web Browser인 Internet Explorer 출시
- 이후 **JavaScript**와 **JScript**는 각자의 기능을 추가하기 시작
- 개발자들은 **Netscape Navigator**와 **Internet Explorer** 각각에 대한 코드를 작성해야하는 상황을 맞이하게 됨

<img width="851" alt="js5" src="https://user-images.githubusercontent.com/86648892/196928140-e1839768-51c3-4dd0-abf8-1641a3ebf66b.png">

<img width="842" alt="js6" src="https://user-images.githubusercontent.com/86648892/196928132-c9fc0af4-8f88-4133-b190-d15b21ac8fe7.png">

<img width="842" alt="js7" src="https://user-images.githubusercontent.com/86648892/196928129-0ac8ef09-cc9f-45ee-93b4-bde77b6f996d.png">

<img width="836" alt="js8" src="https://user-images.githubusercontent.com/86648892/196928124-9af1a92c-6482-43eb-a397-4c221c440704.png">

### 정리

- 웹 브라우저는 JavaScript를 해석하는 엔진을 가지고 있음
- 현재의 JavaScript는 이제 시장에서 자리를 잡은 언어이며, 개발에서 큰 축을 담당하는 언어
- 더이상 jQuery등의 라이브러리를 사용할 필요가 없음 (모든 웹 브라우저가 표준안을 따름)
- 특히, Chrome V8의 경우 JavaScript를 번역하는 속도가 매우 빠름
  - 물건인데? Web Browser에서만 사용하지말고 다른 개발에서도 활용해보자!
  - node.js, react.js, electron 등의 내부 엔진으로 사용
    - node.js는 서버 사이드 프로그래밍으로, 브라우저 시장에 갇혀있던 자바스크립트를 밖에서도 실행할 수 있도록 하는 런타임 실행 환경을 만든 프로그램이다
  - 그 결과, back-end, mobile, desktop app 등을 모두 JavaScript로 개발이 가능해짐
- 현재의 JavaScript는 2015 ES6 때 대격변이 일어난 이후의 것으로, ES6 이후의 자료를 볼 것

---

## JavaScript 실행환경 구성

1. Web Browser로 실행하기
   - HTML 파일에 포함시키기
   - 외부 JavaScript 파일 사용하기
   - Web Browser console에서 바로 입력하기
2. Node.js로 실행하기

### Node.js로 실행하기

- JavaScript를 해석하는 웹 브라우저 엔진을 꺼내온 환경으로 터미널에서도 JavaScript를 실행할 수 있음
- npm
  - Node Package Manager
  - JavaScript를 위한 패키지 관리자 (파이썬의 pip)
- 설치 확인
  ```bash
  $ node -v
  $ npm -v
  ```
- JavaScript 파일 실행해보기
  ```bash
  $ node hello.js
  ```

### Node.js 설치 가이드

### Windows

- 다운로드
  - [Node.js Homepage](https://nodejs.org/ko/) 접속 후 LTS 버전 선택
- 설치
  <img width="564" alt="js9" src="https://user-images.githubusercontent.com/86648892/196928120-75f40b37-73fc-496d-885b-fc8824096d13.png">

- 설치 버전 확인 (git bash)
  ```bash
  $ node -v
  v 16.18.0
  ```

### macOS

1. via `NVM` (권장 방법)

   - nvm이란?
     - [Github NVM](https://github.com/nvm-sh/nvm)
     - “node.js의 버전 관리자”
   - 설치

     - 터미널에 작성

     ```bash

     $ curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
     ```

   - 설정 값 입력
     - vscode로 `.zshrc` 열기
     ```bash
     $ code ~/.zshrc
     ```
     - `~/.zshrc` 에 아래 nvm 설정 값을 최하단에 작성 후 저장
     ```bash
     export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
     [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
     ```
     - 터미널에 다음과 같이 입력해 설정 값 적용
     ```bash
     $ source ~/.zshrc
     ```
     - node.js 설치([Node.js Homepage](https://nodejs.org/ko/) 에서 LTS 버전 확인 후 진행)
     ```bash
     $ nvm install 16.18.0
     ```
     - 사용할 버전 선택
     ```bash
     $ nvm use 16.18.0
     ```
     - 터미널에서 설치된 버전 확인
     ```bash
     $ node -v
     v16.18.0
     ```

2. via 공식 홈페이지

   - [Node.js Homepage](https://nodejs.org/ko/) 접속
   - `LTS` 버전 설치 (설치 시기에 따라 버전은 다를 수 있음)
   - 파일 다운로드
   - 설치
   - 설치 후 터미널에서 다음 명령어 실행

   ```bash
   $ sudo chown -R $USER /usr/local/lib/node_modules
   ```

---

# JavaScript 기초 문법

## 코드 작성법

### 세미콜론 (semicolon)

- 자바스크립트는 세미콜론을 선택적으로 사용 가능
- 세미콜론이 없으면 ASI에 의해 자동으로 세미콜론이 삽입됨
  - ASI (Automatic Semicolon Insertion, 자동 세미콜론 삽입 규칙)
- 자바스크립트의 문법 및 개념적 측면에 집중하기 위해 세미콜론을 사용하지 않고 당분간 진행

### 들여쓰기와 코드 블럭

- Python은 4칸 들여쓰기, JavaScript는 2칸 들여쓰기를 사용
- 블럭(block)은 if, for, 함수에서 중괄호 `{ }` 내부를 말함
  - Python은 들여쓰기를 이용해서 코드 블럭을 구분
  - JavaScript는 중괄호 `{ }` 를 사용해 코드 블럭을 구분

<img width="476" alt="js10" src="https://user-images.githubusercontent.com/86648892/196928118-1475dc76-574c-471b-986b-14bf6ad9f7e6.png">

### 코드 스타일 가이드

- 다양한 JavaScript의 코드 스타일 가이드
  - Airbnb JavaScript Style Guide
    - [Airbnb Github Code Style Guide](https://github.com/airbnb/javascript)
  - Google JavaScript Style Guide
  - standardJavaScript
- 코딩 스타일의 핵심은 합의된 원칙과 일관성
- 코드의 품질에 직결되는 중요한 요소
  - 코드의 가독성, 유지보수, 팀원과의 커뮤니케이션 등 개발 과정 전체에 영향을 끼침
- Python에도 PEP8이라는 코드 스타일 가이드가 있었듯, JavaScript에도 코드 스타일 가이드 존재
- 회사마다 여러 코드 스타일 가이드가 존재하는데, 우선 Airbnb Stylel Guide 기반으로 사용할 것
  - 단, 가이드의 일부 항목은 문법 및 개념적 측면에 집중하기 위해 변형해서 사용하는 경우 있음

### 주석

- 한 줄 주석

  - `//`
    <img width="476" alt="js11" src="https://user-images.githubusercontent.com/86648892/196928116-ad6b832a-abd4-444a-8a6c-2f34b809bab2.png">

- 여러 줄 주석
  - `/* */`
    <img width="477" alt="js12" src="https://user-images.githubusercontent.com/86648892/196928109-061d02ad-40f1-4a7f-92d9-eeef891c1ebc.png">

---

## 변수와 식별자

### 식별자 (identifier)

- 식별자는 변수를 구분할 수 있는 변수명을 의미
- 식별자는 반드시 문자, 달러($), 또는 밑줄(\_)로 시작
- 대소문자를 구분하며, 클래스명 외에는 모두 소문자로 시작
- 예약어 사용 불가능
  - ex) for, if, function 등
- 케이스
  <img width="779" alt="js13" src="https://user-images.githubusercontent.com/86648892/196928106-2bf91953-24a7-4614-beae-d783c4a51c94.png">

  - 카멜 케이스 (camelCase, lower-camel-case)

    <img width="386" alt="js14" src="https://user-images.githubusercontent.com/86648892/196928102-544106e7-cf8c-49a9-ac83-c8b6723affb6.png">

- 파스칼 케이스 (PascalCase, upper-camel-case)
  <img width="456" alt="js15" src="https://user-images.githubusercontent.com/86648892/196928098-82a47a39-29a2-4f41-8dff-a0cf07508708.png">

- 대문자 스네이크 케이스 (SNAKE_CASE)
  <img width="427" alt="js16" src="https://user-images.githubusercontent.com/86648892/196928097-bb5e1e27-8359-4445-8c3a-bff943475cac.png">

### 변수

### 변수 선언 키워드

1. `let`
   - 블록 스코프 지역 변수를 선언 (추가로 동시에 값을 초기화)
2. `const`
   - 블록 스코프 읽기 전용 상수를 선언 (추가로 동시에 값을 초기화)
3. `var`
   - 변수를 선언 (추가로 동시에 값을 초기화)

### [참고] 선언, 할당, 초기화

- 선언 (Declaration)
  - 변수를 생성하는 행위 또는 시점
- 할당 (Assignment)
  - 선언된 변수에 값을 저장하는 행위 또는 시점
- 초기화 (Initialization)
  - 선언된 변수에 처음으로 값을 저장하는 행위 또는 시점

```jsx
let foo // 선언
console.log(foo) // undefined

foo = 11 // 할당
console.log(foo) // 11

let bar = 0 // 선언 + 할당
console.log(bar) // 0
```

### [참고] 블록 스코프 (block scope)

- if, for, 함수 등의 중괄호 내부를 가리킴
- 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능

```jsx
let x = 1
if (x === 1) {
  let x = 2
  console.log(x) // 2
}

console.log(x) // 1
```

### 변수 선언 키워드 - let

- `let`
  - 재할당 가능 & 재선언 불가능
    ```jsx
    let number = 10 // 1. 선언 및 초기값 할당
    number = 20 // 2. 재할당
    ```
    ```jsx
    let number = 10 // 1. 선언 및 초기값 할당
    let number = 20 // 2. 재선언 불가능
    ```
  - 블록 스코프를 갖는 지역 변수를 선언, 선언과 동시에 원하는 값으로 초기화할 수 있음

### 변수 선언 키워드 - const

- `const`
  - 재할당 불가능 & 재선언 불가능
    ```jsx
    const number = 10 // 1. 선언 및 초기값 할당
    number = 10 // 2. 재할당 불가능
    ```
    ```jsx
    const number = 10 // 1. 선언 및 초기값 할당
    const number = 20 // 2. 재선언 불가능
    ```
  - **선언 시 반드시 초기값을 설정**해야하며, 이후 값 변경이 불가능
  - let과 동일하게 블록 스코프를 가짐

### 변수 선언 키워드 - var

- `var`
  - 재할당 가능 & 재선언 가능
    - 유지보수 관점에서는 좋지 않음
      - 변수의 트래킹이 매우 어려워짐
  - ES6 이전에 변수를 선언할 때 사용되던 키워드
  - **호이스팅**되는 특성으로 인해 예기치 못한 문제 발생 가능
    - **따라서 ES6 이후부터는 `var` 대신 `const` 와 `let` 을 사용하는 것을 권장**
    - 함수 스코프 (function scope)를 가짐
      - 함수의 중괄호만 스코프를 가지며, if나 for에 대한 중괄호는 영역이 만들어지지 않고 전역 변수로 넘어감
  - 변수 선언 시 `var`, `const`, `let` 키워드 중 하나를 사용하지 않으면 자동으로 `var` 로 선언됨

### [참고] 함수 스코프 (function scope)

- 함수의 중괄호 내부를 가리킴
- 함수 스코프를 가지는 변수는 함수 바깥에서 접근 불가능

```jsx
function foo() {
  var x = 5
  console.log(x) // 5
}

// ReferenceError: x is not defined
console.log(x)
```

### [참고] 호이스팅 (hoisting)

- “끌어올리다”라는 뜻
- 변수를 선언 이전에 참조할 수 있는 현상
- `var` 로 선언된 변수는 선언 이전에 참조할 수 있으며
  - 이러한 현상을 호이스팅이라 함
- 변수 선언 이전의 위치에서 접근 시 `undefined`를 반환

<img width="480" alt="js17" src="https://user-images.githubusercontent.com/86648892/196928093-b5647b47-5d86-4cd2-8eca-fc3b3b989599.png">

- 즉, JavaScript에서 변수들은 실제 실행 시에 코드의 최상단으로 끌어올려지게 되며 (hoisted)

  - 이러한 이유때문에 `var` 로 선언된 변수는 선언 시에 `undefined` 로 값이 초기화되는 과정이 동시에 일어남
    - 반면 `let`, `const` 는 호이스팅이 일어나면 에러를 발생시킴
      <img width="363" alt="js18" src="https://user-images.githubusercontent.com/86648892/196928090-5dd81d94-d7c4-4704-a487-d2c77b800b57.png">

- 변수를 선언하기 전에 접근이 가능한 것은 코드의 논리적인 흐름을 깨뜨리는 행위이며 이러한 것을 방지하기 위해 `let`, `const` 가 추가되었음
  - `var` 는 사용하지 않아야 하는 키워드
    - 다만, 아직까지도 많은 기존의 JavaScript 코드는 ES6 이전의 문법으로 작성되어 있으므로 호이스팅에 대한 이해가 필요

### 변수 선언 정리

<img width="821" alt="js19" src="https://user-images.githubusercontent.com/86648892/196928082-b7fea1a5-6895-4598-9ad7-ae9aaef2f443.png">

- 어디에 변수를 쓰고 상수를 쓸지 결정하는 것은 프로그래머의 몫
- Airbnb 스타일 가이드에서는 기본적으로 `const` 사용을 권장
  - 재할당해야하는 경우만 `let`

---

## 데이터 타입

- JavaScript의 모든 값은 특정한 데이터 타입을 가짐
- 크게 원시 타입(Primitive type)과 참조 타입(Reference type)으로 분류됨

<img width="728" alt="js20" src="https://user-images.githubusercontent.com/86648892/196928075-02cf62fa-1bbb-4577-8c23-7c3659d06686.png">

### Number

- 정수 또는 실수형 숫자를 표현하는 자료형

```jsx
const a = 13
const b = -5
const c = 3.14 // float - 숫자표현
const d = 2.998e8 // 2.998 * 10^8 = 299,800,000
const e = Infinity
const f = -Infinity
const g = NaN // Not a Number를 나타내는 값
```

- `NaN`
  - Not-A-Number(숫자가 아님)을 나타냄
  - `Number.isNaN()` 의 경우 주어진 값의 유형이 Number이고 값이 NaN이면 true, 아니면 false를 반환
    <img width="355" alt="js21" src="https://user-images.githubusercontent.com/86648892/196928074-43dabca9-3891-481e-9314-c48b004ecbb5.png">

    <img width="824" alt="js22" src="https://user-images.githubusercontent.com/86648892/196928068-ab8dfde3-4fd4-42c7-b945-c278cc64c83c.png">

### String

- 문자열을 표현하는 자료형
- 작은 따옴표 또는 큰 따옴표 모두 가능

  ```jsx
  const sentence1 = "Ask and go to the blue" // single quote
  const sentence2 = "Ask and go to the blue" // double quote

  console.log(sentence1)
  console.log(sentence2)
  ```

- 곱셉, 나눗셈, 뺄셈은 안되지만

  - 덧셈을 통해 문자열을 붙일 수 있음

  ```jsx
  const firstName = "Tony"
  const lastName = "Stark"
  const fullName = firstName + lastName

  console.log(fullName) // Tony Stark
  ```

- Quote를 사용하면 선언 시 줄바꿈이 안됨
  - 대신 escape sequence를 사용할 수 있기 때문에 `\n` 을 사용해야함

<img width="573" alt="js23" src="https://user-images.githubusercontent.com/86648892/196928067-9a3594a7-28d3-4b93-ad73-0d9494793b04.png">

- Template Literal을 사용하면 줄바꿈이 되며, 문자열 사이에 변수도 삽입도 가능
  - 백틱
    - 변수 삽입 시 `${변수명}`
  - 단, escape sequence를 사용할 수 없다
    - == Python의 “f-string”

<img width="568" alt="js24" src="https://user-images.githubusercontent.com/86648892/196928063-ce853237-11a4-4041-96e5-991ab34c064a.png">

### Template literals

- 내장된 표현식을 허용하는 문자열 작성 방식
- ES6+ 부터 지원
- Backtick을 이용하며, 여러 줄에 걸쳐 문자열을 정의할 수도 있고
  - JavaScript의 변수를 문자열 안에 바로 연결할 수 있는 이점이 생김
- 표현식을 넣을 수 있는데, 이는 `$ {expression}` 으로 표기

### Empty Value

- 값이 존재하지 않음을 표현하는 값으로 JavaScript에서는 `null` 과 `undefined` 가 존재
- 동일한 역할을 하는 2개의 키워드가 존재하는 이유는 단순한 JavaScript의 설계 실수
- 큰 차이를 두지 말고 interchangeable하게 사용할 수 있도록 권장함
  - 굳이 구분하자면?
  - `null`
    - null 값을 나타내는 특별한 키워드
    - 주로 개발자가 변수의 **값이 없음을 의도적으로 표현**할 때 사용하는 데이터 타입
    ```jsx
    let lastName = null
    console.log(lastName) // null - 의도적으로 값이 없음을 표현
    ```
  - `undefined`
    - 값이 정의되어있지 않음을 표현하는 값
    - 변수 선언 이후 직접 값을 할당하지 않으면 자동으로 할당됨
    - 주로 JS에서 내부적으로 주는 값
    ```jsx
    let firstName // 선언만 하고 할당하지 않음
    console.log(firstName) // undefined
    ```

### null과 undefined

- null과 undefined의 가장 대표적인 차이점은 `typeof` 연산자를 통해 타입을 확인했을 때 나타남

```jsx
typeof null // "object"
typeof undefined // "undefined"
```

- null이 원시타입임에도 불구하고 object로 출력되는 이유는 JavaScript 설계 당시의 버그를 지금까지 해결하지 못한 것
  - 출력상의 버그임
  - 쉽게 해결할 수 없는 이유는 이미 null 타입에 의존성을 갖는 많은 프로그램들이 망가질 수 있기 때문 (하위 호환 유지)

### Boolean

- true와 false
- 참과 거짓을 표현하는 값
- 조건문 또는 반복문에서 유용하게 사용
  - 조건문 또는 반복문에서 boolean이 아닌 데이터 타입은 *자동 형변환 규칙*에 따라 true 또는 false로 변한됨

### ToBoolean Conversions (자동 형변환)

- [ECMAScript ToBoolean](https://tc39.es/ecma262/#sec-toboolean)

<img width="763" alt="js25" src="https://user-images.githubusercontent.com/86648892/196928061-e7eb28d4-38b4-40f7-a9f8-8f546e67f49b.png">

---

## 연산자

### 할당 연산자

- 오른쪽에 있는 피연산자의 평가 결과를 왼쪽 피연산자에 할당하는 연산자
- 다양한 연산에 대한 단축 연산자 지원
- Increment 및 Decrement 연산자

  - Increment
    - `++`
    - 피연산자의 값을 1 증가시키는 연산자
  - Decrement
    - `--`
    - 피연산자의 값을 1 감소시키는 연산자
  - 변수 앞에 오는 경우, 변수를 1 증감시키는 작업을 우선적으로 실행

    - 변수 뒤에 오는 경우, 변수를 1 증감시키는 작업을 해당 라인이 끝난 후 실행
      - 변수 뒤에 쓰는 것을 주로 사용함

    ```jsx
    <script type="text/javascript">
        var num1 = 3;

        document.write(num1 + "<br>");
        document.write((++num1) + "<br>");
        document.write(num1 + "<br>");
        document.write((num1++) + "<br>");
        document.write(num1 + "<br><br>");

        document.write(num1 + "<br>");
        document.write((--num1) + "<br>");
        document.write(num1 + "<br>");
        document.write((num1--) + "<br>");
        document.write(num1 + "<br>");
    </script>

    /*
    3
    4
    4
    4
    5

    5
    4
    4
    4
    3
    */
    ```

  - **`+=` 또는 `-=` 과 같이 더 분명한 표현으로 적을 것을 권장**

```jsx
let c = 0

c += 10
console.log(c) // 10

c -= 3
console.log(c) // 7

c *= 10
console.log(c) // 70

c++
console.log(c) // 71 - c에 1을 더한다 (증감식)

c--
console.log(c) // 70 - c에 1을 뺀다 (증감식)
```

### 비교 연산자

- 피연산자들(숫자, 문자, Boolean 등)을 비교하고
  - 결과값을 boolean으로 반환하는 연산자
- 문자열은 유니코드 값을 사용하며 표준 사전 순서를 기반으로 비교
  - ex) 알파벳끼리 비교할 경우
    - 알파벳 순서상 후순위가 더 크다
    - 소문자가 대문자보다 더 크다

```jsx
3 > 2 // true
3 < 2 // false

"A" < "B" // true
"Z" < "a" // true
"가" < "나" // true
```

### 동등 연산자 (==)

- 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값을 반환
- 비교할 때 **암묵적 타입 변환**을 통해 타입을 일치시킨 후 같은 값인지 비교
- 두 피연산자가 모두 객체일 경우 메모리의 같은 객체를 바라보는지 판별
- **예상치 못한 결과가 발생할 수 있으므로 특별한 경우를 제외하고 사용하지 않음**

```jsx
const a = 1
const b = "1"

console.log(a == b) // true
console.log(a == true) // true

// 자동 형변환 예시
console.log(8 * null) // 0, null은 0
console.log("5" - 1) // 4
console.log("5" + 1) // '51'
console.log("five" * 2) // NaN
```

### 일치 연산자 (===)

- 두 피연산자의 값과 타입이 모두 같은 경우 true를 반환
- 같은 객체를 가리키거나, 같은 타입이면서 같은 값인지를 비교
- 엄격한 비교가 이뤄지며 암묵적 타입 변환이 발생하지 않음
  - 엄격한 비교
    - 두 비교 대상의 타입과 값 모두 같은지 비교하는 방식

```jsx
const a = 1
const b = "1"

console.log(a === b) // false
console.log(a === Number(b)) // true
```

### 논리 연산자

- 3가지 논리 연산자로 구성
  - and
    - `&&`
  - or
    - `||`
  - not
    - `!`
- 단축 평가 지원
  - ex) `false && true`
    - false
  - ex) `true || false`
    - true

```jsx
true && false // false
true && true // true

false || true // true
false || false // false

!true // false

1 && 0 // 0
0 && 1 // 0
4 && 7 // 7

1 || 0 // 1
0 || 1 // 1
4 || 7 // 4
```

### 삼항 연산자 (Ternary Operator)

- 3개의 피연산자를 사용하여 조건에 따라 값을 반환하는 연산자
- 가장 앞의 조건식이 참이면 `:` 앞의 값이 반환되며, 그 반대일 경우 `:` 뒤의 값이 반환되는 연산자
- 삼항 연산자의 결과 값이기 때문에 변수에 할당 가능

```jsx
true ? 1 : 2 // 1
false ? 1 : 2 // 2

const result = Math.PI > 4 ? "Yep" : "Nope"
console.log(result) // Nope
```

---

## 조건문

- `if` statement
  - 조건 표현식의 결과값을 **boolean 타입으로 변환 후 참 / 거짓을 판단**
- `switch` statement
  - 조건 표현식의 결과값이 **어느 값(case)에 해당하는지 판별**
  - 주로 특정 변수의 값에 따라 조건을 분기할 때 활용
    - 조건이 많아질 경우 if문보다 가독성이 나을 수 있음

### if statement

- `if` , `else if` , `else`

  - 조건은 소괄호(condition) 안에 작성
  - 실행할 코드는 중괄호 `{ }` 안에 작성
  - 블록 스코프 생성

  ```jsx
  const name = "manager"

  if (name === "admin") {
    console.log("관리자님 환영합니다.")
  } else if (name === "manager") {
    console.log("매니저님 환영합니다.")
  } else {
    console.log(`${name}님 환영합니다.`)
  }
  ```

### switch statement

- 표현식(expression)의 결과값을 이용한 조건문
- 표현식의 결과값과 case문의 오른쪽 값을 비교
- break 및 default문은 “선택적”으로 사용 가능
- break문이 없는 경우 break문을 만나거나 default문을 실행할 때까지 다음 조건문 실행
- 블록 스코프 생성

```jsx
switch(expression) {
	case 'first value': {
		// do something
		[break]
	}
	case 'second value': {
		// do something
		[break]
	}
	[default: {
		// do something
	}]
}
```

```jsx
const name = "홍길동"

switch (name) {
  case "홍길동": {
    console.log("홍길동님 환영합니다.")
  }
  case "manager": {
    console.log("매니저님 환영합니다.")
  }
  default: {
    console.log(`${name}님 환영합니다.`)
  }
}

// Fall-through
// 3줄 모두 출력됨
```

```jsx
const name = '홍길동'

switch(name) {
	case '홍길동': {
		console.log('홍길동님 환영합니다.')
		[break]
	}
	case 'manager': {
		console.log('매니저님 환영합니다.')
		[break]
	}
	default: {
		console.log(`${name}님 환영합니다.`)
	}
}

// 첫째 줄 출력 후 종료
```

### if / switch

- 조건이 많은 경우 switch문을 통해 가독성 향상을 기대할 수 있음
- 일반적으로 중첩 else if문은 유지보수하기 힘들다는 문제도 있음

<img width="667" alt="js26" src="https://user-images.githubusercontent.com/86648892/196928056-4fda8dfc-8872-42c3-8279-e8f10c9b20d0.png">

---

## 반복문

- `while`
- `for`
- `for...in`
- `for...of`

### while

- 조건문이 참이기만 하면 문장을 계속해서 수행

```jsx
while (조건문) {
  // do something
}
```

```jsx
let i = 0
while (i < 6) {
  console.log(i)
  i += 1
}

// 0, 1, 2, 3, 4, 5
```

### for

- 특정한 조건이 거짓으로 판별될 때까지 반복

```jsx
for ([초기문]; [조건문]; [증감문]) {
  // do something
}
```

```jsx
for (let i = 0; i < 6; i++) {
  console.log(i)
}

// 0, 1, 2, 3, 4, 5

// 1. 반복문 진입 및 변수 i 선언
// 2. 조건문 평가 후 코드 블럭 실행
// 3. 코드 블록 실행 이후 i값 증가

// 2와 3의 반복
```

### for…in (객체 순회)

- 객체(object)의 속성을 순회할 때 사용
- **배열도 순회 가능하지만 인덱스 순으로 순회한다는 보장이 없으므로 권장하지 않음**
- **속성 값(배열에서는 인덱스)을 출력**

```jsx
for (variable in object) {
  statements
}
```

```jsx
const fruits = { a: "apple", b: "banana" }

for (const key in fruits) {
  console.log(key) // a, b
  console.log(fruits[key]) // apple, banana
}
```

### for…of (iterable 순회)

- 반복 가능한 객체를 순회할 때 사용
- 반복 가능한(iterable) 객체의 종류
  - Array, Set, String 등
- **각각의 인덱스에 있는 값을 출력**

```jsx
for (variable of object) {
  statements
}
```

```jsx
const numbers = [0, 1, 2, 3]

for (const number of numbers) {
  console.log(number) // 0, 1, 2, 3
}
```

### for…in과 for…of 차이

- `for...in` 은 속성 이름을 통해 반복
- `for...of` 는 속성 값을 통해 반복

```jsx
const arr = [3, 5, 7]

for (const i in arr) {
  console.log(i) // 0 1 2
}

for (const i of arr) {
  console.log(i) // 3 5 7
}
```

<img width="842" alt="js27" src="https://user-images.githubusercontent.com/86648892/196928054-b44516a7-5be9-43bc-9cda-f8ce5c64e4a2.png">

### [참고] for…in, for…of와 const

- 일반적인 for문 `for (let i = 0; i < arr.length; i++) { ... }` 의 경우에는 최초 정의한 i를 재할당하면서 사용하기 때문에 `const` 를 사용하면 에러 발생
- 다만 `for...in` , `for...of` 의 경우에는 재할당이 아니라, 매 반복 시 해당 변수를 새로 정의하여 사용하므로 에러가 발생하지 않음

### 조건문과 반복문 정리

<img width="823" alt="js28" src="https://user-images.githubusercontent.com/86648892/196928050-79b6bb7d-227d-4bef-af21-2ce937967d02.png">

---

# 함수

- 참조 타입 중 하나로써 function 타입에 속함
- JavaScript에서 함수를 정의하는 방법은 주로 2가지로 구분됨
  - 함수 선언식 (function declaration)
  - 함수 표현식 (function expression)

## 함수의 정의

### 함수 선언식 (Function declaration)

- 일반적인 프로그래밍 언어의 함수 정의 방식

```jsx
function 함수명() {
  // do something
}
```

```jsx
function add(num1, num2) {
  return num1 + num2
}

add(2, 7) // 9
```

### 함수 표현식 (Function expression)

- 표현식 내에서 함수를 정의하는 방식
- 함수 표현식은 함수의 이름을 생략한 익명 함수로 정의 가능

```jsx
변수키워드 함수명 = function () {
	// do something
}
```

```jsx
const sub = function (num1, num2) {
  return num1 - num2
}

sub(7, 2) // 5
```

- 표현식에서 함수 이름을 명시하는 것도 가능
  - 다만 이 경우에는 함수 이름은 호출에 사용되지 못하고 디버깅 용도로 사용됨

```jsx
const mySub = function namedSub(num1, num2) {
  return num1 - num2
}

mySub(1, 2) // -1
namedSub(1, 2) // ReferenceError: namedSub is not defined
```

### 기본 인자(Default arguments)

- 인자 작성 시 `=` 문자 뒤 기본 인자 선언 가능

```jsx
const greeting = function (name = "Anonymous") {
  return `Hi ${name}`
}

greeting() // Hi Anonymous
```

### 매개변수와 인자의 개수 불일치 허용

- 매개변수보다 인자의 개수가 많을 경우

```jsx
const noArgs = function () {
  return 0
}

noArgs(1, 2, 3) // 0

const twoArgs = function (arg1, arg2) {
  return [arg1, arg2]
}

twoArgs(1, 2, 3) // [1, 2]
```

- 매개변수보다 인자의 개수가 적을 경우

```jsx
const threeArgs = function (arg1, arg2, arg3) {
	return [arg1, arg2, arg3]
}

threeArgs() // [undefined, undefined, undefined]
threeArgs(1) // [1, undefined, undefined]
threeArgs(1, 2_ // [1, 2, undefined]
```

### Spread syntax (…)

- “전개 구문”
  - Python의 asterisk를 이용한 가변인자와 유사
- 전개 구문을 사용하면 배열이나 문자열과 같이 반복 가능한 객체를

  - 배열의 경우는 요소, 함수의 경우는 인자로 확장할 수 있음

    1. 배열과의 사용

       ```jsx
       let parts = ["shoulders", "knees"]
       let lyrics = ["head", ...parts, "and", "toes"]

       console.log(lyrics) // ['head', 'shoulders, 'knees', 'and', 'toes']
       ```

    2. 함수와의 사용 (Rest parameters)

       - The rest parameter syntax를 사용하여 정해지지 않은 수의 매개변수를 배열로 받을 수 있음

       ```jsx
       function func(a, b, ...theArgs) {
         // do something
       }
       ```

       ```jsx
       const restOpr = function (arg1, arg2, ...restArgs) {
         return [arg1, arg2, restArgs]
       }

       console.log(restOpr(1, 2, 3, 4, 5)) // [1, 2, [3, 4, 5]]
       console.log(restOpr(1, 2)) // [1, 2, []]
       ```

## 선언식과 표현식

- 선언식 함수와 표현식 함수 모두 타입은 function으로 동일

```jsx
// 함수 표현식
const add = function (args) {}

// 함수 선언식
function sub(args) {}

console.log(typeof add) // function
console.log(typeof sub) // function
```

### 선언식의 Hoisting

- 함수 선언식으로 정의한 함수는 var로 정의한 변수처럼 호이스팅이 발생
- 즉, 함수 호출 이후에 선언해도 동작

```jsx
add(2, 7) // 9

function add(num1, num2) {
  return num1 + num2
}
```

- 반면 함수 표현식으로 선언한 함수는 함수 정의 전에 호출 시 에러 발생
- 함수 표현식으로 정의된 함수는 변수로 평가되어 변수의 scope 규칙을 따름

```jsx
sub(7, 2) // Uncaught ReferenceError: Cannot access 'sub' before initialization

const sub = function (num1, num2) {
  return num1 - num2
}
```

<img width="823" alt="js29" src="https://user-images.githubusercontent.com/86648892/196928046-52bf5a7d-6627-4cc3-8356-d3781e629ac7.png">

## Arrow Function

- “함수를 비교적 간결하게 정의할 수 있는 문법”
- function 키워드와 중괄호를 이용한 구문을 짧게 사용하기 위해 탄생
  - 단계적으로 생략 가능
  1. `function` 키워드 생략 가능
  2. 함수의 **매개변수가 하나뿐**이라면 `( )` 도 생략 가능
  3. 함수의 **내용이 한 줄**이라면 `{ }` 와 `return` 도 생략 가능
- 생략 시 인자와 function body 사이에 `=>` 추가
- 화살표 함수는 **항상 익명 함수**
  - `==` 함수 표현식에서만 사용 가능
- Airbnb Style Guide에서는 1, 3단계만 권장
  - 3단계에서도 인자의 `( )` 는 지우지 않는 것을 권장

<img width="844" alt="js30" src="https://user-images.githubusercontent.com/86648892/196928043-e114daa4-fac1-42e7-8bd5-bded3da93b26.png">

### Arrow Function 응용

<img width="826" alt="js31" src="https://user-images.githubusercontent.com/86648892/196928038-2219d024-d946-4def-b850-2e6da95d8e7e.png">

### 즉시 실행 함수 (IIFE, Immediately Invoked Function Expression)

- 선언과 동시에 실행되는 함수
- 함수의 선언 끝에 `()` 를 추가하여 선언되자마자 실행하는 형태
- `()` 에 값을 넣어 인자로 넘겨줄 수 있음
- 즉시 실행 함수는 선언과 동시에 실행되기 때문에 같은 함수를 다시 호출할 수 없음
- 이러한 특징을 살려 초기화 부분에 많이 사용
- 일회성 함수이므로 익명함수로 사용하는 것이 일반적

```jsx
;(function (num) {
  return num ** 3
})(2)(
  // 8

  (num) => num ** 3
)(2) // 8
```

---

# Array와 Object

- JavaScript의 데이터 타입 중 참조 타입(reference)에 해당하는 타입은
  - Array와 Object이며
    - 객체라고 말함
- 객체는 속성들의 모음(collection)
  - (참고) 객체 안쪽의 속성들은 메모리에 할당되어있고 해당 객체는 메모리의 시작 주소 값을 가리키고 있는 형태로 이루어져 있다

## 배열(Array)

- 키와 속성들을 담고 있는 참조 타입의 객체(object)
- 순서를 보장하는 특징이 있음
- 주로 대괄호를 이용하여 생성하고, 0을 포함한 **양의 정수 인덱스**로 특정 값에 접근 가능
  - 음의 정수 인덱싱 불가
- 배열의 길이는 `array.length` 형태로 접근 가능
  - (참고) 배열의 마지막 원소는 `array.length - 1` 로 접근

```jsx
const numbers = [1, 2, 3, 4, 5]

console.log(numbers[0]) // 1
console.log(numbers[-1]) // undefined
console.log(numbers.length) // 5

const numbers = [1, 2, 3, 4, 5]

console.log(numbers[numbers.length - 1]) // 5
console.log(numbers[numbers.length - 2]) // 4
console.log(numbers[numbers.length - 3]) // 3
console.log(numbers[numbers.length - 4]) // 2
console.log(numbers[numbers.length - 5]) // 1
```

---

## 배열 메서드 기초

<img width="824" alt="js32" src="https://user-images.githubusercontent.com/86648892/196928034-c4c05614-1919-4d01-8b5b-4a119cdbea74.png">

- `array.reverse()`
  - 원본 배열 요소들의 순서를 반대로 정렬
  ```jsx
  const numbers = [1, 2, 3, 4, 5]
  numbers.reverse()
  console.log(numbers) // [5, 4, 3, 2, 1]
  ```
- `array.push()`
  - 배열의 가장 뒤에 요소 추가
- `array.pop()`

  - 배열의 마지막 요소 제거

  ```jsx
  const numbers = [1, 2, 3, 4, 5]

  numbers.push(100)
  console.log(numbers) // [1, 2, 3, 4, 5, 100]

  numbers.pop()
  console.log(numbers) // [1, 2, 3, 4, 5]
  ```

- `array.includes(value)`

  - 배열에 특정 값이 존재하는지 판별 후 참 또는 거짓 반환

  ```jsx
  const numbers = [1, 2, 3, 4, 5]

  console.log(numbers.includes(1)) // true
  console.log(numbers.includes(100)) // false
  ```

- `array.indexOf(value)`

  - 배열에 특정 값이 존재하는지 확인 후 가장 첫번째로 찾은 요소의 인덱스 반환
  - 만약 해당 값이 없을 경우 -1 반환

  ```jsx
  const numbers = [1, 2, 3, 4, 5]
  let result

  result = numbers.indexOf(3)
  console.log(result) // 2

  result = numbers.indexOf(100)
  console.log(result) // -1
  ```

- `array.join([separator])`

  - 배열의 모든 요소를 연결하여 반환
  - separator(구분자)는 선택적으로 지정 가능하며
    - 생략 시 쉼표를 기본값으로 사용

  ```jsx
  const numbers = [1, 2, 3, 4, 5]
  let result

  result = numbers.join()
  console.log(result) // 1, 2, 3, 4, 5

  result = numbers.join("")
  console.log(result) // 12345

  result = numbers.join(" ")
  console.log(result) // 1 2 3 4 5

  result = numbers.join("-")
  console.log(result) // 1-2-3-4-5
  ```

---

## 배열 메서드 심화

### Array Helper Methods

- 배열을 **순회**하며 특정 로직을 수행하는 메서드
- 메서드 호출 시 인자로 **callback 함수**를 받는 것이 특징
  - **callback 함수**: 어떤 함수의 내부에서 실행될 목적으로 인자로 넘겨받는 함수
    - 쉽게 말해 **다른 함수의 파라미터로 들어가는 함수**를 콜백 함수라 한다
      - 콜백 함수는 3가지 매개변수로 구성
        1. element: 배열의 처리할 현재 요소
        2. index: 배열의 처리할 현재 요소의 인덱스
        3. array: 호출한 배열
        4. thisArg: callback을 실행할 때 `this`로 사용할 값

<img width="838" alt="js33" src="https://user-images.githubusercontent.com/86648892/196928030-ddc5fa79-0afa-4f0e-9047-345901f7346b.png">

### [참고] Django로 보는 콜백함수 예시

<img width="574" alt="js34" src="https://user-images.githubusercontent.com/86648892/196928028-b9a8856c-5b82-4717-b36b-a9fc7fdd360f.png">

### forEach

```jsx
array.forEach((element, index, array) => {
  // do something
})
```

- `array.forEach(callback(element[, index[, array]]))`
- 인자로 주어지는 함수(콜백 함수)를 배열의 각 요소에 대해 한 번씩 실행
- 반환값(return) 없음

```jsx
const colors = ["red", "blue", "green"]

// 1. 함수를 따로 표현식으로 정의

printFunc = function (color) {
  console.log(color)
}
colors.forEach(printFunc)

// red
// blue
// green

// 2. 함수 정의를 따로하지 않고 인자로 넣기

colors.forEach(function (color) {
  console.log(color)
})

// 3. Arrow Function 적용

colors.forEach((color) => console.log(color))
```

### map

```jsx
array.map((element, index, array) => {
  // do something
})
```

- `array.map(callback(element[, index[, array]]))`
- 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
- **콜백 함수의 반환값을 요소로 하는 새로운 배열 반환**
- 기존 배열 전체를 다른 형태로 바꿀 때 유용

```jsx
const numbers = [1, 2, 3]

// 1. 함수를 따로 표현식으로 정의

const doubleFunc = function (number) {
  return number * 2
}

const doubleNumbers = numbers.map(doubleFunc)
console.log(doubleNumbers) // [2, 4, 6]

// 2. 함수 정의를 따로하지 않고 인자로 넘기기

const doubleNumbers = numbers.map(function (number) {
  return number * 2
})
console.log(doubleNumbers) // [2, 4, 6]

// 3. Arrow Function 적용

const doubleNumbers = numbers.map((number) => number * 2)
console.log(doubleNumbers) // [2, 4, 6]
```

### filter

```jsx
array.filter((element, index, array) => {
  // do something
})
```

- `array.filter(callback(element[, index[, array]]))
- 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
- **콜백 함수의 반환값이 참인 요소들만 모아서 새로운 배열 반환**
- 기존 배열의 요소들을 필터링할 때 유용

```jsx
const products = [
	{ name: 'cucumber', type: 'vegetable' },
	{ name: 'banana', type: 'fruit' },
	{ name: 'carrot', type: 'vegetable' },
	{ name: 'apple', type: 'fruit' },
]

// 1. 함수를 따로 표현식으로 정의

const fruitFilter = function (product) {
	return product.type === 'fruit'
}

const fruits = products.filter(fruitFilter)

// 2. 함수 정의를 따로하지 않고 인자로 넘기기

const fruits = products.filter(function (product) {
	return product.type ==== 'fruit'
})

// 3. Arrow Function 적용

const fruits = products.filter((product) => product.type === 'fruit')
```

### reduce

```jsx
array.reduce((acc, element, index, array) => {
  // do something
}, initialValue)
```

- `array.reduce(callback(acc, element, [index[, array]])[, initialValue])`
- 인자로 주어지는 함수(콜백 함수)를 배열의 각 요소에 대해 한 번씩 실행해서
  - 하나의 결과 값을 반환
- 즉, 배열을 하나의 값으로 계산하는 동작이 필요할 때 사용
  - 총합, 평균 등
- map, filter 등 여러 배열 메서드 동작을 대부분 대체할 수 있음
- reduce 메서드의 주요 매개변수
  - acc
    - 이전 callback 함수의 반환값이 누적되는 변수
    - reduce의 첫번째 매개변수인 콜백함수의 첫번째 매개변수로 누적된 값이다 (전 단계까지의 결과)
  - initialValue (optional)
    - 최초 callback 함수 호출 시 acc에 할당되는 값, default 값은 배열의 첫번째 값
    - reduce의 두번째 매개변수로 누적될 값의 초기값
      - 지정하지 않을 시 첫번째 요소의 값이 됨
        - **빈 배열의 경우 initialValue를 제공하지 않으면 에러 발생**

```jsx
const tests = [90, 90, 80, 77]

// 총합

const sum = tests.reduce(function (total, x) {
  return total + x
}, 0) // 여기서 0 생략 가능

// Arrow Function 적용

const sum = tests.reduce((total, x) => total + x, 0)

// 평균

const average = tests.reduce((total, x) => total + x, 0) / tests.length
```

<img width="352" alt="js35" src="https://user-images.githubusercontent.com/86648892/196928019-bbb830fe-4764-47f2-99d0-e850e3493959.png">

### find

```jsx
array.find((element, index, array)) {
	// do something
}
```

- `array.find(callback(element[, index[, array]]))`
- 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
- 콜백 함수의 반환 값이 참이면, 조건을 만족하는 첫번째 요소를 반환
- 찾는 값이 배열에 없으면 undefined 반환

```jsx
const avengers = [
  { name: "Tony Stark", age: 45 },
  { name: "Steve Rogers", age: 32 },
  { name: "Thor", age: 40 },
]

const avenger = avengers.find(function (avenger) {
  return avenger.name === "Tony Stark"
})

// Arrow Function 적용

const avenger = avengers.find((avenger) => avenger.name === "Tony Stark")
```

### some

```jsx
array.some((element, index, array) => {
  // do something
})
```

- `array.some(callback(element[, index[, array]]))
- 배열의 **요소 중 하나라도** 주어진 판별 함수를 통과하면 참을 반환
- 모든 요소가 통과하지 못하면 거짓 반환
- **빈 배열은 항상 false 반환**

```jsx
const arr = [1, 2, 3, 4, 5]

const result = arr.some((elem) => elem % 2 === 0) // true
```

### every

```jsx
array.every((element, index, array) => {
  // do something
})
```

- array.every(callback(element[, index[, array]]))
- 배열의 모든 요소가 주어진 판별 함수를 통과하면 참을 반환
- 하나의 요소라도 통과하지 못하면 거짓 반환
- **빈 배열은 항상 true 반환**

```jsx
const arr = [1, 2, 3, 4, 5]

const = result2 = arr.every((elem) => elem % 2 === 0) // false
```

### 배열 순회 비교

```jsx
const chars = ["A", "B", "C", "D"]

// for loop
for (let idx = 0; idx < chars.length; idx++) {
  console.log(idx, chars[idx])
}

/*
0 A
1 B
2 C
3 D
*/

// for ... of
for (const char of chars) {
  console.log(char)
}

/*
A
B
C
D
*/

// forEach
// forEach는 2번째 인자에서 인덱스를 가져올 수 있음
chars.forEach((char, idx) => {
  console.log(idx, char)
})

/*
0 A
1 B
2 C
3 D
*/

chars.forEach((char) => {
  console.log(char)
})

/*
A
B
C
D
*/
```

<img width="477" alt="js36" src="https://user-images.githubusercontent.com/86648892/196927996-31417551-b943-4738-8b5e-1ff6f757e047.png">

---

## 객체(Object)

- 객체는 속성(property)의 집합이며, 중괄호 내부에 key와 value의 쌍으로 표현
- key는 문자열 타입만 가능
  - key 이름에 띄어쓰기 등의 구분자가 있으면 따옴표로 묶어서 표현
- value는 모든 타입(함수 포함)가능
- 객체 요소 접근은 점(.) 또는 대괄호([])로 가능
  - key 이름에 띄어쓰기같은 구분자가 있으면 대괄호 접근만 가능

```jsx
const me = {
  name: "jack",
  phoneNumber: "01012345678",
  "samsung products": {
    buds: "Galaxy Buds pro",
    galaxy: "Galaxy s99",
  },
}

console.log(me.name) // jack
console.log(me.phoneNumber) // 01012345678
console.log(me["samsung products"]) // { buds: 'Galaxy Buds pro', galaxy: 'Galaxy s99' }
console.log(me["samsung products"].buds) // Galaxy Buds pro
```

## 객체 관련 문법

### 객체 관련 ES6 문법 익히기

- ES6에 새로 도입된 문법들로 객체 생성 및 조작에 유용하게 사용 가능
  1. 속성명 축약
  2. 메서드명 축약
  3. 계산된 속성명 사용하기
  4. 구조 분해 할당
  5. 객체 전개 구문(Spread Operator)

### 속성명 축약

- 객체를 정의할 때 key와 할당하는 변수의 이름이 같으면 예시와 같이 축약 가능

```jsx
var books = ["Learning JavaScript", "Learning Python"]
var magazines = ["Vogue", "Science"]

// ES5
var bookShop = {
  books: books,
  magazines: magazines,
}
console.log(bookShop)

/*
{
	books: ['Learning JavaScript', 'Learning Python'],
	magazines: ['Vogue', 'Science']
*/
```

```jsx
const books = ["Learning JavaScript", "Learning Python"]
const magazines = ["Vogue", "Science"]

// ES6+
const bookShop = {
  books,
  magazines,
}
console.log(bookShop)

/*
{
	books: ['Learning JavaScript', 'Learning Python'],
	magazines: ['Vogue', 'Science']
*/
```

### 메서드명 축약

- 메서드 선언 시 function 키워드 생략 가능

```jsx
// ES5
var obj = {
  name: "jack",
  greeting: function () {
    console.log("Hi!")
  },
}

obj.greeting() // Hi!
```

```jsx
// ES6+
const obj = {
  name: "jack",
  greeting() {
    console.log("Hi!")
  },
}

obj.greeting() // Hi!
```

### 계산된 속성 (computed property name)

- 객체를 정의할 때 key의 이름을 표현식을 이용하여 동적으로 생성 가능
  - 아래 코드에서는 `[key]` 부분에 해당
    - 연결된 변수에 따라 key의 이름이 동적으로 변경됨
      - `const key = 'ssafy'` 라면 key에는 ssafy라는 값이 들어가있음

```jsx
const key = "country"
const value = ["한국", "미국", "일본", "중국"]

const myObj = {
  [key]: value,
}

console.log(myObj) // { country: [ '한국', '미국', '일본', '중국' ] }
console.log(myObj.country) // [ '한국', '미국', '일본', '중국' ]
```

### 구조 분해 할당 (destructing assignment)

- 배열 또는 객체를 분해하여 속성을 변수에 쉽게 할당할 수 있는 문법
  - 배열이나 객체를 분해해서
    - 어딘가 할당하는 방식

```jsx
// 구조 분해 할당을 적용하지 않음

const userInformation = {
  name: "ssafy kim",
  userId: "ssafyStudent1234",
  phoneNumber: "010-1234-1234",
  email: "ssafy@ssafy.com",
}

const name = userInformation.name
const userId = userInformation.userId
const phoneNumber = userInformation.phoneNumber
const email = userInformation.email
```

```jsx
// 구조 분해 할당 적용

const userInformation = {
  name: "ssafy kim",
  userId: "ssafyStudent1234",
  phoneNumber: "010-1234-1234",
  email: "ssafy@ssafy.com",
}

const { name } = userInformation
const { userId } = userInformation
const { phoneNumber } = userInformation
const { email } = userInformation

// 여러개도 가능
const { name, userId } = userInformation
```

- 변수에 중괄호를 씌움으로써 점(.)을 통해 접근하는 과정을 생략할 수 있음
  - userInformation이라는 객체를 할당할 때 분해하여
    - 중괄호 안에서 요구하는 것만 넣는 것
- 이름은 맞춰줘야 함
- 여러 개를 구조 분해할 때 편리함

### Spread syntax (…)

- 배열과 마찬가지로 전개구문을 사용하여 객체 내부에서 객체 전개 가능
- 얕은 복사에 활용 가능

```jsx
const obj = { b: 2, c: 3, d: 4 }
const newObj = { a: 1, ...obj, e: 5 }

console.log(newObj) // { a: 1, b: 2, c: 3, d: 4, e: 5 }
```

---

## JavaScriptON (JavaScript Object Notation)

- Key-Value 형태로 이루어진 자료 표기법
- JavaScript의 Object와 유사한 구조를 가지고 있지만 Object는 그 자체로 타입이고
  - JavaScriptON은 형식이 있는 문자열
    - 즉, JSON의 타입은 큰 문자열 덩어리 하나
- **즉, JavaScriptON을 Object로 사용하기 위해서는 변환 작업이 필요**
- 파이썬에서는 JSON을 사용하기 위해 Dictionary로 바꾸는 작업이 필요했다면
  - JavaScript에서는 Object 타입으로 바꾸는 작업이 필요하다

### JavaScriptON 변환

```jsx
const jsonData = {
  coffee: "Americano",
  iceCream: "Cookie and cream",
}
```

```jsx
// Object -> JSON

const objToJson = JSON.stringify(jsonData)
console.log(objToJson) // {"coffee":"Americano","iceCream":"Cookie and cream"}
console.log(typeof objToJson) // string

// JSON -> Object
// Django가 열심히 만든 json data를 Vue.js에서 파싱하여 object로 바꿔 데이터 조작하여 적당한 위치에 배분

const jsonToObj = JSON.parse(objToJson)
console.log(jsonToObj) // { coffee: 'Americano', iceCream: 'Cookie and cream' }
console.log(typeof jsonToObj) // object
```

---

### [참고] 배열은 객체다

- 키와 속성들을 담고 있는 참조 타입의 객체(object)
- 배열은 **인덱스를 키**로 가지며
  - **length 프로퍼티**를 갖는
    - **특수한 객체**

```jsx
Object.getOwnPropertyDescriptors([1, 2, 3])

// [1, 2, 3] 이라는 배열의 실제 모습

/*
{
  '0': { value: 1, writable: true, enumerable: true, configurable: true },
  '1': { value: 2, writable: true, enumerable: true, configurable: true },
  '2': { value: 3, writable: true, enumerable: true, configurable: true },
  length: { value: 3, writable: true, enumerable: false, configurable: false }
}
*/
```

---

## [Practices]

```html
<body>
  <script>
    // 1. 해당 코드를 template string 을 활용하여 리팩토링하시오.
    const name = "Tom"
    const message = `Hi, my name is ${name}`
    console.log(message)

    // 2. 해당 코드를 arrow function 으로 리팩토링하시오.
    // function add(x, y) {
    //   return x + y
    // }
    const arrow1 = (x, y) => x + y
    console.log(arrow1(2, 8))

    // function square(x) {
    //   return x ** 2
    // }
    const arrow2 = (x) => x ** 2
    console.log(arrow2(5))

    // 3. 해당 코드의 메서드 introduce 를 function 키워드 없이 리팩토링하시오.
    // const tom = {
    //   name: 'Tom',
    //   introduce: function () {
    //     console.log('Hi, my name is ' + this.name)
    //   }
    // }

    const tom = {
      name: "Tom",
      introduce() {
        console.log("Hi, my name is " + this.name)
      },
    }
    tom.introduce()

    // 4. 해당 코드를 key, value를 한번씩만 작성하도록 리팩토링하시오.
    const url = "https://test.com"
    const data = { message: "Hello World!" }

    // const request = { url: url, data: data }
    const request = {
      url,
      data,
    }
    console.log(request)
  </script>
</body>
```

```html
<body>
  <script>
    /* 
      1. forEach 메서드를 활용해 모든 사용자들의 이름을 출력하시오.
      2. filter 메서드를 활용해 결혼한 사람들만 모아 marriedUsers 상수에 할당하시오.
      3. find 메서드를 활용해 이름이 'Tom'인 사람만 tom 상수에 할당하시오.
      4. map 메서드를 활용해 모든 사용자에게 isAlive 키를 추가하고 true로 설정한 뒤, newUsers 상수에 할당하시오.
      5. reduce 메서드를 활용해 모든 사용자들의 계좌잔액을 totalBalance 상수에 할당하시오.
    */

    const users = [
      { name: "Jack", age: 31, isMarried: true, balance: 100 },
      { name: "Sarah", age: 22, isMarried: false, balance: 200 },
      { name: "Ash", age: 25, isMarried: true, balance: 300 },
      { name: "Robert", age: 27, isMarried: false, balance: 400 },
      { name: "Tom", age: 35, isMarried: true, balance: 500 },
    ]

    // 1.
    users.forEach((user) => console.log(user.name))

    // 2.
    const marriedUsers = users.filter(
      (marriedUser) => marriedUser.isMarried === true
    )
    for (const marriedUser of marriedUsers) {
      console.log(marriedUser.name)
    }

    // 3.
    const tom = users.find((user) => user.name === "Tom")
    console.log(tom)

    // 4.
    // const newUsers = users.map((user) => user.isAlive = true)
    // console.log(newUsers) // [{0: true}, {1: true}, {2: true}, {3: true}, {4: true}, {length: 5}]가 출력됨 // 기존의 users에 isAlive 속성이 추가되었음

    const newUsers1 = users.map(function (user) {
      return { ...user, isAlive: true }
    })
    console.log(newUsers1)

    const newUsers2 = users.map((user) => {
      user.isAlive = true
      return user
    })
    console.log(newUsers2)

    // 5.
    const totalBalance = users.reduce((total, user) => total + user.balance, 0)
    console.log(totalBalance)
  </script>
</body>
```

```html
<body>
  <script>
    // 1-1. 아래 코드를 object destructuring을 활용해 리팩토링 하시오.
    const savedFile = {
      name: "profile",
      extension: "jpg",
      size: 29930,

      fileSummary() {
        console.log(
          `The file ${this.name}.${this.extension} is size of ${this.size} bytes.`
        )
      },
    }

    // function fileSummary(file) {
    //   console.log(`The file ${file.name}.${file.extension} is size of ${file.size} bytes.`)
    // }

    savedFile.fileSummary()

    // 1-2. 아래 코드를 object destructuring을 활용해 리팩토링 하시오.
    const data = {
      username: "myName",
      password: "myPassword",
      email: "my@mail.com",
    }

    // a) 기존 방법 (직접 접근)
    // const username = data.username
    // const password = data.password
    // const email = data.email

    // b) 객체 분해하여 해당 키값 요소만 변수에 할당
    // const { username } = data
    // const { password } = data
    // const { email } = data
    // console.log(username, password, email)

    // c) 한번에 묶어서 변수에 할당
    const { username, password, email } = data
    console.log(username, password, email)

    // 2. Rest operator를 활용해 아래 코드를 리팩토링 하시오.

    // function addNumbers(a, b, c, d, e) {
    //   const numbers = [a, b, c, d, e];
    //   return numbers.reduce((sum, number) => {
    //     return sum + number
    //   }, 0)
    // }

    function addNumbers(...numbers) {
      return numbers.reduce((sum, number) => {
        return sum + number
      }, 0)
    }

    console.log(addNumbers(1, 2)) // 3
    console.log(addNumbers(1, 2, 3, 4, 5)) // 15

    // 3-1. Spread operator를 활용해 아래 코드를 리팩토링 하시오.
    const defaultColors = ["red", "green", "blue"]
    const favoriteColors = ["navy", "black", "gold", "white"]

    // .concat() 활용
    // const palette = defaultColors.concat(favoriteColors);
    // console.log(palette)

    // Spread operator 활용
    const palette = [...defaultColors, ...favoriteColors]
    console.log(palette)

    // 3-2. Spread operator를 활용해 아래 코드를 리팩토링 하시오.

    // Object.assign(target, ...sources) 활용
    const info1 = { name: "Tom", age: 30 }
    const info2 = { isMarried: true, balance: 3000 }
    // const fullInfo = Object.assign(info1, info2)

    // Spread operator 활용
    const fullInfo = { ...info1, ...info2 }
    console.log(fullInfo)
  </script>
</body>
```

```jsx
/*
  전기버스
  - A도시는 전기버스를 운행하려고 한다. 전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서, 중간에 충전기가 설치된 정류장을 만들기로 했다.
  - 버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.
  - 충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.
  - 만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다. 출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.

  <입력>
    [
      3,   => 최대한 이동할 수 있는 정류장 수
      10,  => 종점 정류장 번호
      5,   => 설치된 충전기의 개수
      [1, 3, 5, 7, 9]  => 충전기가 설치된 정류장 번호
    ]

  <출력>
    현재 아래 주어진 입력에 따른 출력은
      3
      0
      4
    이다.
*/

// 입력
const inputs = [
  [3, 10, 5, [1, 3, 5, 7, 9]], // 3
  [3, 10, 5, [1, 3, 7, 8, 9]], // 0
  [5, 20, 5, [4, 7, 9, 14, 17]], // 4
  [10, 20, 5, [4, 7, 9, 14, 17]], // 2 (추가 실험용 테케)
]

// 정답 풀이
function solution(K, N, M, chargers) {
  candidates = [0, ...chargers, N]
  let start = 0
  let ans = 0
  for (let i = 1; i < candidates.length; i++) {
    // 충전소 간 거리가 K보다 큰 경우는 이동 불가
    if (candidates[i] - candidates[i - 1] > K) {
      ans = 0
      break
    }
    // 시작지점에서 갈 수 있는 만큼 가고, 못가는 경우에 도달했을 때는 바로 전 충전소 지점에서 충전, 충전 횟수 1 증가
    if (candidates[i] - candidates[start] > K) {
      start = i - 1
      ans++
    }
  }
  return ans
}

// 정답 출력
for (const input of inputs) {
  console.log(solution(...input))
}
```

```jsx
// 회문 판별 함수
function isPalindrome(str) {
  // split을 통해 str -> array // reverse를 통해 array 뒤집고, join을 통해 array -> str
  const words = str.split(" ")
  const str1 = words.join("")
  const str2 = str1.split("").reverse().join("")
  if (str1 === str2) {
    return true
  } else {
    return false
  }
}

// 출력
console.log(
  isPalindrome("a santa at nasa"), // true
  isPalindrome("google") // false
)
```

```jsx
// 별 찍기

for (let i=1; i <= 5; i++) {
  let ans = ''
  for (let j=1; j <= 5-i; j++) {
      ans += ' '
  }
  for (let j=1; j <= i*2-1; j++) {
      ans += '*'
  }
  console.log(ans)
}

/*

    *
   ***
  *****
 *******
*********

/*
```

```jsx
// 별 찍기 (repeat 사용)

for (let i=1; i<=9; i+=2) {
  console.log(' '.repeat((9-i)/2) + '*'.repeat(i))
}

/*

    *
   ***
  *****
 *******
*********

/*
```

---

# JavaScript DOM and Event

- DOM
- Event
- this

---

# DOM

- “브라우저에서의 JavaScript”
  - JavaScript는 웹 페이지에서 다양한 기능을 구현하는 스크립트 언어
  - 정적인 정보만 보여주던 웹 페이지를 데이터가 주기적으로 갱신되거나, 사용자와 상호 작용을 하거나, 애니메이션 등이 동작하게 하는 것을 가능하게 함
  - 스크립트 언어(Script Language)란?
    - 기존에 존재하는 응용 소프트웨어를 제어하는 컴퓨터 프로그래밍 언어

## 웹 페이지에서의 JavaScript

- JavaScript는 프로그래밍 언어로서의 역할도 가능하지만 클라이언트 사이드 JavaScript 언어 위에 올라가있는 기능들은 더 다양함
  - API라고 불리는 이 기능들은 JavaScript 코드에서 사용할 수 있는 것들을 더 무궁무진하게 만들어줌
  - 해당 API는 크게 2개의 범주로 분류
    1. Broswer APIs
       - 웹 브라우저에 내장된 API
         - 웹 브라우저가 현재 컴퓨터 환경에 관한 데이터를 제공하거나, 오디오를 재생하는 등 여러가지 유용하고 복잡한 일을 수행할 수 있게함
         - JavaScript로 Browser API들을 사용해서 여러가지 기능을 사용할 수 있음
       - **DOM API**
       - Geolocation API
         - 지리정보 관련 API
       - WebGL
         - 그래픽 관련 API
       - etc
    2. Third Party APIs
       - 브라우저에 탑재되지 않은 API
       - 웹에서 직접 코드와 정보를 찾아야함
       - Google Map API, Kakao Login API 등

## 브라우저가 웹 페이지를 불러오는 과정

<img width="549" alt="js37" src="https://user-images.githubusercontent.com/86648892/212543080-ca4e7224-bda4-4cf6-8580-7e121a36c986.png">

- 웹 페이지를 브라우저로 불러오면
  - 브라우저는 코드(HTML, CSS, JavaScript)를 실행 환경(브라우저 탭)에서 실행
  - JavaScript는 **DOM API**를 통해 HTML과 CSS를 동적으로 수정
    - 사용자 인터페이스를 업데이트하는 일에 가장 많이 쓰임

## DOM

<img width="577" alt="js38" src="https://user-images.githubusercontent.com/86648892/212543079-0325fc8a-2328-4ca2-be56-383e7cfacc8c.png">

- “문서 객체 모델”
  - Document Object Model
  - 문서를 논리 트리로 표현
- HTML 문서를 구조화하여 객체(Object)로 취급
  - 프로그래밍 언어가 DOM 구조에 접근할 수 있는 방법을 제공
    - 문서 구조, 스타일, 내용 등을 쉽게 변경할 수 있게 도움
    - HTML 콘텐츠를 추가, 제거, 변경하고, 동적으로 페이지에 스타일을 추가하는 등 HTML과 CSS를 조작할 수 있음
    - 단순한 속성 접근, 메서드 활용 뿐만 아니라 프로그래밍 언어적 특성을 활용한 조작이 가능함
- 정리
  - 브라우저에서 문서에 접근하여 조작하는 방법
    - 웹 페이지라는 문서를
      - DOM API를 통해 객체 구조 생성
        - JS를 통해 DOM 수정
  - 웹 페이지는 일종의 문서(document)
    - 이 문서는 웹 브라우저를 통해 그 내용이 해석되어 웹 브라우저 화면에 나타나거나 HTML 코드 자체로 나타나기도 함
      - DOM은 동일한 문서를 표현하고, 저장하고, 조작하는 방법을 제공
        - DOM은 **웹 페이지의 객체 지향 표현**이며
          - JS와 같은 스크립트 언어를 이용해 DOM을 수정할 수 있음

## DOM에 접근하기

- 모든 웹 브라우저는 스크립트 언어가 손쉽게 웹 페이지의 요소에 접근할 수 있도록 만들기 위해 DOM 구조를 항상 사용
- 우리는 “DOM 주요 객체”들을 활용하여 문서를 조작하거나 특정 요소들을 얻을 수 있음

## DOM의 주요 객체

- `window`
- `document`
- navigator, location, history, screen 등

### window object

<img width="749" alt="js39" src="https://user-images.githubusercontent.com/86648892/212543078-705ca74a-bd41-4e06-80de-e4161298d5a1.png">

- DOM을 표현하는 창
- 가장 최상위 객체
  - 작성 시 생략 가능
- 하나의 탭이 하나의 윈도우
- DOM에서 제공하는 모든 클래스의 위에 있는 클래스
- 일반적으로 접근할 때 window는 생략함
- window의 메서드 예시
  - 새 탭 열기
    <img width="582" alt="js40" src="https://user-images.githubusercontent.com/86648892/212543077-b6b826e4-1b2f-40e4-b4c3-d879fff044a3.png">

    - 경고 대화 상자 표시

    <img width="583" alt="js41" src="https://user-images.githubusercontent.com/86648892/212543076-f4e46b54-ae42-402f-b31b-083b8d4cfb95.png">

    - 인쇄 대화 상자 표시

    <img width="582" alt="js42" src="https://user-images.githubusercontent.com/86648892/212543075-d483897d-4902-4709-a3a4-9845ec13cb26.png">

### document object

<img width="650" alt="js43" src="https://user-images.githubusercontent.com/86648892/212543074-3f4d2bfc-2ce3-42d3-8905-e5f24164fa13.png">

- HTML 문서의 진입점
- 브라우저가 불러온 웹 페이지
- 페이지 컨텐츠의 진입점 역할을 하며, `<body>` 등과 같은 수많은 다른 요소들을 포함하고 있음
- document의 속성 예시
  - 현재 문서의 제목
    - HTML의 `<title>` 값
      - `document.title`
        - 현재 탭에 나타나는 title 값 확인 가능
        - 제목 수정
          - `document.title = 'JavaScript'`
- document는 window의 속성이다
  - `window.document`
    - `#document` 출력 확인 가능

### [참고] 파싱(Parsing)

<img width="1448" alt="js44" src="https://user-images.githubusercontent.com/86648892/212543071-a690d766-a520-44bc-8fdb-1bfad17a5801.png">

- 구문 분석 및 해석
- 브라우저가 문자열을 해석 → DOM Tree로 만드는 과정

---

# DOM 조작

- Document가 제공하는 기능을 사용해 웹 페이지 문서 조작하기
- DOM 조작 순서
  1. **선택 (Select)**
  2. **조작 (Manipulation)**
     - 생성, 추가, 삭제 등

## 선택 관련 메서드

- `document.querySelector(selector)`
  - 단일 선택
    - 제공한 선택자와 일치하는 element 한 개 선택
  - 첫번째 객체 반환
    - 제공한 CSS selector를 만족하는 첫번째 객체를 반환
  - 없다면 null 반환
- `document.querySelectorAll(selector)`
  - 여러 개 선택
    - 제공한 선택자와 일치하는 여러 element 선택
    - 매칭할 하나 이상의 selector를 포함하는 유효한 CSS selector를 인자(문자열)로 받음
  - 제공한 CSS selector를 만족하는 **NodeList**를 반환

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <h1 id="title">DOM 조작</h1>
    <p class="text">querySelector</p>
    <p class="text">querySelectorAll</p>
    <ul>
      <li>Javascript</li>
      <li>Python</li>
    </ul>

    <script>
      console.log(document.querySelector("#title"))
      console.log(document.querySelectorAll(".text"))

      console.log(document.querySelector(".text"))
      console.log(document.querySelectorAll("body > ul > li"))

      liTags = document.querySelectorAll("body > ul > li")
      liTags.forEach((element) => {
        console.log(element)
      })
    </script>
  </body>
</html>
```

<img width="1918" alt="js45" src="https://user-images.githubusercontent.com/86648892/212543070-59ff5dde-d9cf-4eab-9715-96d7e19646e1.png">

### [참고] NodeList

- index로만 각 항목에 접근 가능
- 배열의 forEach 메서드 및 다양한 배열 메서드 사용 가능
- `querySelectorAll()에 의해 반환되는 NodeList는 DOM의 변경사항을 실시간으로 반영하지 않음
  - 실시간으로 반영되지 않는다는 것이 안좋다는 뜻은 아님
    - 라이브 콜렉션과 정적 콜렉션
      - querySelectorAll()은 정적 노드리스트를 반환
      - [https://developer.mozilla.org/ko/docs/Web/API/NodeList](https://developer.mozilla.org/ko/docs/Web/API/NodeList)

## 조작 관련 메서드

- `document.createElement(tagName)`
  - 태그를 만드는 것
  - 작성한 tagName의 HTML 요소를 생성하여 반환
- `Node.innerText`
  - 태그 안의 내용
  - Node 객체와 그 자손의 텍스트 컨텐츠(DOMString)를 표현 (해당 요소 내부의 raw text)
  - 사람이 읽을 수 있는 요소만 남김
    - 즉, 줄 바꿈을 인식하고 숨겨진 내용을 무시하는 등 최종적으로 스타일링이 적용된 모습으로 표현됨
- `Node.appendChild()`
  - 한 Node를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입
  - 한번에 오직 하나의 Node만 추가할 수 있음
  - 추가된 Node 객체를 반환
  - 만약 주어진 Node가 이미 문서에 존재하는 다른 Node를 참조한다면 현재 위치에서 새로운 위치로 이동
- `Node.removeChild()`
  - DOM에서 자식 Node를 제거
  - 제거된 Node를 반환

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <div></div>

    <script>
      // 태그 생성
      const h1Tag = document.createElement("h1")

      // 태그안에 컨텐츠를 작성하고
      h1Tag.innerText = "DOM 조작"

      // 부모 div 태그를 가져와서
      const div = document.querySelector("div")

      // div 태그의 자식 요소로 추가
      div.appendChild(h1Tag)

      // div의 h1 요소 삭제
      div.removeChild(h1Tag)
    </script>
  </body>
</html>
```

## 조작 관련 메서드 (속성 조회 및 설정)

- `Element.getAttribute(attributeName)`
  - 해당 요소의 지정된 값(문자열)을 반환
  - 인자(attributeName)는 값을 얻고자 하는 속성의 이름
- `Element.setAttribute(name, value)`
  - 지정된 요소의 값을 설정
  - 속성이 이미 존재하면 값을 갱신
    - 존재하지 않으면 지정된 이름과 값으로 새 속성을 추가

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <style>
      .red {
        color: red;
      }
      .blue {
        color: blue;
      }
    </style>
  </head>
  <body>
    <h1 class="red">안녕하세요</h1>
    <div></div>

    <script>
      const aTag = document.createElement("a")
      aTag.setAttribute("href", "https://google.com")
      aTag.innerText = "구글"

      const divTag = document.querySelector("div")
      divTag.appendChild(aTag)

      const h1Tag = document.querySelector("h1")
      h1Tag.classList.toggle("blue")

      // remove, add를 통해 클래스 속성 추가 및 제거 가능
      // h1Tag.classList.remove('red')
      // h1Tag.classList.add('blue')
    </script>
  </body>
</html>
```

<img width="1916" alt="js46" src="https://user-images.githubusercontent.com/86648892/212543067-e589d8ec-13ba-4e93-894a-11ddc85b4635.png">

### [참고] Element.classList

- [https://developer.mozilla.org/ko/docs/Web/API/Element/classList](https://developer.mozilla.org/ko/docs/Web/API/Element/classList)

---

# Event

- Event란 프로그래밍하고 있는 시스템에서 일어나는 사건(action) 혹은 발생(occurence)으로, 각 이벤트에 대해 조작할 수 있도록 특정 시점을 시스템이 알려주는 것
  - 즉, 웹 페이지에서 어떠한 행동에 대해 여러 사건들이 발생함
    - 예를 들어 사용자가 웹 페이지의 버튼을 클릭하면 클릭에 대한 이벤트가 발생하고, 마우스 오버를 하면 마우스 오버에 대한 이벤트가 발생
      - 해당 이벤트에 대하여 이동을 하거나, 카테고리가 뜨는 등 이벤트를 통해 사건에 대한 결과를 받거나 조작할 수 있음
  - 웹에서는 다양한 Event가 존재
    - 키보드 키 입력, 브라우저 닫기, 데이터 제출, 텍스트 복사 등

## Event Object

- 네트워크 활동이나 사용자와의 상호작용과 같은 사건의 발생을 알리기 위한 객체
- Event 발생
  - 마우스를 클릭하거나 키보드를 누르는 등 사용자 행동으로 발생할 수도 있고
  - 특정 메서드를 호출하여 프로그래밍적으로도 만들어낼 수 있음
- DOM 요소는 Event를 받고 (**”수신”**)
  - 받은 Event를 **“처리”**할 수 있음
  - Event 처리는 주로 addEventListener()라는 Event Handler를 다양한 HTML 요소에 **“부착”**해서 처리함

## Event Handler

<img width="820" alt="js47" src="https://user-images.githubusercontent.com/86648892/212543066-a21af82c-6b51-473f-a846-75de433a4da1.png">

- `EventTarget.addEventListener(type, listener[, options])`
  - 지정한 Event가 대상에 전달될 때마다 호출할 함수를 설정
    - EventTarget
      - Event를 지원하는 모든 객체(Element, Document, Window 등)를
        - 대상(EventTarget)으로 지정 가능
    - type
      - 반응할 Event 유형을 나타내는 대소문자 구분 문자열
      - 대표 이벤트
        - input, click, submit 등
        - [https://developer.mozilla.org/en-US/docs/Web/Events](https://developer.mozilla.org/en-US/docs/Web/Events)
    - listener
      - 콜백 함수
        - 해당 타입의 이벤트가 들어올 시 할 행동
      - 지정된 타입의 Event를 수신할 객체
        - JavaScript function 객체(콜백 함수)이어야함
          - 콜백 함수는 발생한 Event의 데이터를 가진 Event 객체를 유일한 매개변수로 받음

### click event

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <button id="btn">버튼</button>
    <p id="counter">0</p>

    <script>
      const btn = document.querySelector("#btn")
      let countNum = 0

      // Event Handler 작성
      btn.addEventListener("click", function (event) {
        // console.log(event)
        const pTag = document.querySelector("#counter")
        countNum += 1
        pTag.innerText = countNum
      })
    </script>
  </body>
</html>
```

<img width="1913" alt="js48" src="https://user-images.githubusercontent.com/86648892/212543064-245aba88-991d-412d-8080-c3e0be9ab0f4.png">

### input event

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <input type="text" id="text-input" />
    <p></p>
    <script>
      // input 태그 안에 넣는 값을 실시간으로 출력하기
      // 1. input 선택
      const inputTag = document.querySelector("#text-input")
      // 2. Event Handler 부착
      inputTag.addEventListener("input", function (event) {
        // console.log(event)
        // console.log(event.target.value)
        const pTag = document.querySelector("p")
        pTag.innerText = event.target.value
      })
    </script>
  </body>
</html>
```

<img width="1912" alt="js49" src="https://user-images.githubusercontent.com/86648892/212543063-42fbd2d2-d0c6-4a04-ae63-e18ec47d7539.png">

### click and input event

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <style>
      .blue {
        color: blue;
      }
    </style>
  </head>
  <body>
    <h1></h1>
    <button id="btn">클릭</button>
    <input type="text" />

    <script>
      const btn = document.querySelector("#btn")
      btn.addEventListener("click", function (event) {
        const h1Tag = document.querySelector("h1")
        h1Tag.classList.toggle("blue")
      })

      const inputTag = document.querySelector("input")
      inputTag.addEventListener("input", function (event) {
        const h1Tag = document.querySelector("h1")
        h1Tag.innerText = event.target.value
      })
    </script>
  </body>
</html>
```

<img width="1913" alt="js50" src="https://user-images.githubusercontent.com/86648892/212543061-e9c234d4-e709-43a0-8684-d04d5018ebf3.png">

---

## Event 취소

### `event.preventDefault()`

- 현재 Event의 기본 동작을 중단
- HTML 요소의 기본 동작을 작동하지 않게 막음
- HTML 요소의 기본 동작 예시
  - a tag
    - 클릭 시 특정 주소로 이동
      - a 태그를 눌러도 href 링크로 이동하지 않게 하고 싶을 경우
  - form tag
    - form 데이터 전송
      - form 안에 submit 역할을 하는 버튼을 눌러도 창을 새로 실행하지 않게 하고 싶을 경우 (submit은 작동됨)

### prevent copy

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <div>
      <h1>정말 중요한 내용</h1>
    </div>

    <script>
      const h1Tag = document.querySelector("h1")
      h1Tag.addEventListener("copy", function (event) {
        // 복사 이벤트를 방지
        event.preventDefault()
        alert("복사할 수 없습니다!")
      })
    </script>
  </body>
</html>
```

<img width="1913" alt="js51" src="https://user-images.githubusercontent.com/86648892/212543060-eac419ba-6650-490c-8f4d-5393fef5d0e2.png">

---

## Event 실습

### lotto

- 버튼을 클릭하면 랜덤 로또 번호 6개를 출력하기
- **lodash**
  - 모듈성, 성능 및 추가 기능을 제공하는 JavaScript 유틸리티 라이브러리
  - array, object 등 자료구조를 다룰 때 사용하는 유용하고 간편한 유틸리티 함수들을 제공
  - 예시
    - reverse, sortBy, range, random 등
  - [https://lodash.com/docs/4.17.15](https://lodash.com/docs/4.17.15)

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>프로젝트</title>
    <style>
      /* 스타일은 수정하지 않습니다. */
      .ball {
        width: 10rem;
        height: 10rem;
        margin: 0.5rem;
        border-radius: 50%;
        text-align: center;
        line-height: 10rem;
        font-size: xx-large;
        font-weight: bold;
        color: white;
      }
      .ball-container {
        display: flex;
      }
    </style>
  </head>
  <body>
    <h1>로또 추천 번호</h1>
    <button id="lotto-btn">행운 번호 받기</button>
    <div id="result"></div>

    <script src="https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"></script>
    <script>
      const btn = document.querySelector("#lotto-btn")
      btn.addEventListener("click", function (event) {
        // 공이 들어갈 컨테이너 생성
        const ballContainer = document.createElement("div")
        ballContainer.classList.add("ball-container")

        // 랜덤한 숫자 6개 생성 (lodash 라이브러리 메서드 사용)
        const numbers = _.sampleSize(_.range(1, 46), 6)
        console.log(numbers)

        // 공 만들기
        numbers.forEach((number) => {
          const ball = document.createElement("div")
          ball.innerText = number
          ball.classList.add("ball")
          ball.style.backgroundColor = "crimson"
          ballContainer.appendChild(ball)
        })

        // 공 컨테이너를 결과 영역의 자식으로 넣기
        const resultDiv = document.querySelector("#result")
        resultDiv.appendChild(ballContainer)
      })
    </script>
  </body>
</html>
```

<img width="1914" alt="js52" src="https://user-images.githubusercontent.com/86648892/212543059-ad1e3e0d-6d47-472b-9771-a644acbf2b83.png">

### todo (create, read 기능만 구현)

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <form action="#">
      <input type="text" class="inputData" />
      <input type="submit" value="Add" />
    </form>
    <ul></ul>

    <script>
      const formTag = document.querySelector("form")

      const addTodo = function (event) {
        // console.log(event)
        // 기본 form 태그 동작 방지
        event.preventDefault()

        const inputTag = document.querySelector(".inputData")
        const data = inputTag.value

        // 문자열 메서드 .trim()은 양쪽 공백 제거
        if (data.trim()) {
          const liTag = document.createElement("li")
          liTag.innerText = data

          const ulTag = document.querySelector("ul")
          ulTag.appendChild(liTag)

          // 입력값 제출 후 input 내에 값이 남아있지 않도록 리셋
          event.target.reset()
        } else {
          alert("내용을 입력하세요!")
        }
      }

      formTag.addEventListener("submit", addTodo)
    </script>
  </body>
</html>
```

<img width="1913" alt="js53" src="https://user-images.githubusercontent.com/86648892/212543057-53336080-615b-4a2f-b216-5f824cdc0b1f.png">

---

# this

- 어떠한 object를 가리키는 키워드
  - java에서의 this와 python에서의 self는 인스턴스 자기자신을 가리킴
- JavaScript의 함수는 호출될 때 this를 암묵적으로 전달받음
- JavaScript에서의 this는 일반적인 프로그래밍 언어에서의 this와 조금 다르게 동작
- JavaScript는 **해당 함수 호출 방식에 따라 this에 바인딩되는 객체가 달라짐**
  - 즉, 함수를 선언할 때 this에 객체가 결정되는 것이 아니고
    - 함수를 호출할 때 **함수가 어떻게 호출되었는지에 따라 동적으로 결정됨**

## 전역 문맥에서의 this

- 브라우저의 전역 객체인 window를 가리킴
  - 전역 객체란 모든 객체의 유일한 최상위 객체를 의미
    - `console.log(this)`
      - window

## 함수 문맥에서의 this

- 함수의 this 키워드는 다른 언어와 조금 다르게 동작
  - this의 값은 함수를 호출한 방법에 의해 결정됨
  - 함수 내부에서 this의 값은 함수를 호출한 방법에 의해 좌우됨
- 단순 호출
- Method
- Nested

### 단순 호출

<img width="564" alt="js54" src="https://user-images.githubusercontent.com/86648892/212543055-d2a39fe0-c5b0-4648-88bb-051c8878dc25.png">

- 전역 객체를 가리킴
- 전역은 브라우저에서는 window, Node.js는 global을 의미함

### Method (Function in Object, 객체의 메서드로서)

<img width="564" alt="js55" src="https://user-images.githubusercontent.com/86648892/212543054-9bf0067b-1180-41fa-a900-23142ffff41c.png">

- 메서드로 선언하고 호출한다면
  - 객체의 메서드이므로 해당 객체가 바인딩

### Nested (function keyword)

<img width="745" alt="js56" src="https://user-images.githubusercontent.com/86648892/212543053-c700625a-459a-4f58-be25-e8072a8fe48d.png">

- 해당 콜백 함수는 메서드로 호출된 것이 아니라 스스로 호출된 것이기에 전역 객체 window를 가리킴
- 이를 해결하기 위한 수단이 “화살표 함수”
  - **Arrow Function은 한 단계 상위의 문맥을 가리킴**

### Nested (Arrow Function)

<img width="726" alt="js57" src="https://user-images.githubusercontent.com/86648892/212543051-4c3b20d2-beac-434c-9400-976f1d27d9d1.png">

- Arrow Function에서 this는 자신을 감싼 정적 범위
  - 즉, 자신보다 한 단계 상위 문맥
  - 자동으로 한 단계 상위 scope의 context를 바인딩

## 화살표 함수

- 화살표 함수는 호출의 위치와 상관없이 상위 스코프를 가리킴
  - Lexcial scope this
    - **Lexical scope?**
      - 함수를 어디서 호출하는지가 아니라 **어디에 선언**하였는지에 따라 결정
        - Static scope라고도 하며 대부분의 프로그래밍 언어에서 따르는 방식
          - 따라서 함수 내의 함수 상황에서 화살표 함수를 쓰는 것을 권장

### this와 addEventListener

- 하지만
  - addEventListener에서의 콜백 함수는 특별하게 function 키워드의 경우 addEventListener를 호출한 대상(event.target)을 뜻함
    - 화살표 함수는 상위 스코프를 지칭하기에 addEventListener에서는 window 객체가 바인딩됨
  - addEventListener의 콜백 함수는 function 키워드를 사용하자

## this 정리

- this는 호출되는 순간에 결정되는 것
  - 즉, 런타임에 결정되는 것
    - addEventListener는 예외
- this가 런타임에 결정되면 장점도 있고 단점도 있음
  - 장점
    - 함수(메서드)를 하나만 만들어서 여러 객체에서 재사용할 수 있다
  - 단점
    - 이런 유연함이 실수로 이어질 수 있다는 것은 단점

## this practice

```jsx
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <button id="function">function</button>
  <button id="arrow">arrow function</button>

  <script>
    // 1. 단순 호출
    const myFunc = function () {
      console.log(this)
    }
    myFunc()

    // 2. Method
    const myObj1 = {
      data: 1,
      myFunc() {
        console.log(this)
        console.log(this.data)
      }
    }
    myObj1.myFunc()

    // 3-1. Nested (function)
    const myObj2 = {
      numbers: [1],
      myFunc() {
        console.log(this) // myObj
        this.numbers.forEach(function (number) {
          console.log(number) // 1
          console.log(this) // window
        })
      }
    }
    myObj2.myFunc()

    // 3-2. Nested (arrow function)
    const myObj3 = {
      numbers: [1],
      myFunc() {
        console.log(this) // myObj
        this.numbers.forEach((number) => {
          console.log(number) // 1
          console.log(this) // myObj
        })
      }
    }
    myObj3.myFunc()

    // this와 addEventListener
    const functionButton = document.querySelector('#function')
    const arrowButton = document.querySelector('#arrow')

    functionButton.addEventListener('click', function(event) {
      console.log(this) // <button id="function">function</button>
    })

    arrowButton.addEventListener('click', event => {
      console.log(this) // window
    })
  </script>
</body>
</html>
```

<img width="1915" alt="js58" src="https://user-images.githubusercontent.com/86648892/212543049-516304ad-4081-455a-8d4e-cd2ffb9714b4.png">

---

## practice_element.html

```jsx
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h3>요일</h3>
  <ul id="day">
    <li>월요일</li>
    <li>화요일</li>
    <li>수요일</li>
    <li>목요일</li>
    <li>금요일</li>
  </ul>

  <script>
    // 요소 만들기
    const sunday = document.createElement('li')
    const saturday = document.createElement('li')
    const startP = document.createElement('p')
    const endP = document.createElement('p')
    // 요소 꾸미기
    sunday.innerText = '일요일'
    saturday.innerText = '토요일'
    startP.innerText = 'START'
    endP.innerText = 'END'
    // 요소 배치하기
    // prepend, append, before, after
    const day = document.querySelector('#day')
    // 자식으로서 앞뒤에 추가
    day.prepend(sunday)
    day.append(saturday)
    // 형제로서 앞뒤에 추가
    day.before(startP)
    day.after(endP)

    // 월요일 삭제하기
    // const mon = document.querySelector('#day > li:nth-child(2)')
    const mon = day.children[1]
    mon.remove()

    // 일요일을 토요일 다음으로 이동
    // const sun = day.children[0]
    const sun = day.firstChild
    day.append(sun)
  </script>
</body>
</html>
```

<img width="1916" alt="js59" src="https://user-images.githubusercontent.com/86648892/212543048-e5eff9f3-1ed5-4110-8083-aa53921b3475.png">

---

## practice_event.html

```css
.box {
  width: 30px;
  height: 30px;
  display: inline-block;
  margin: 10px auto;
}

.red {
  background-color: red;
}

.blue {
  background-color: blue;
}

.green {
  background-color: green;
}
```

```jsx
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="1025_style.css">
  <title>JavaScript Practice</title>
</head>
<body>
  <div id="number">0</div>
  <button id="minus">-</button>
  <button id="plus">+</button>

  <div>
    <div class="box red"></div>
    <div class="box blue"></div>
    <div class="box green"></div>
  </div>

  <script>
    // 1. 버튼을 누르면 숫자 1씩 증가 및 감소
    let number = document.querySelector("#number")
    const minusBtn = document.querySelector('#minus')
    const plusBtn = document.querySelector('#plus')

    plusBtn.addEventListener('click', function (event) {
      // number.innerText = parseInt(number.innerText) + 1
      number.innerText++
    })
    minusBtn.addEventListener('click', function (event) {
      // number.innerText = parseInt(number.innerText) - 1
      number.innerText--
    })

    //2. 상자를 클릭하면 해당 색으로 글자 색 변경
    const box = document.querySelectorAll('.box')

    box.forEach((element) => {
      element.addEventListener('click', function (event) {
        number.setAttribute('style', `color: ${event.target.classList[1]}`)
      })
    })

    // 3. 상자를 마우스오버하면 해당 색으로 글자 색 변경
    document.querySelector('.red')
      .addEventListener('mouseover', function() {
        number.style.color = 'red'
      })

    document.querySelector('.blue')
    .addEventListener('mouseover', function() {
      number.style.color = 'blue'
    })

    document.querySelector('.green')
      .addEventListener('mouseover', function() {
        number.style.color = 'green'
    })

  </script>
</body>
</html>
```

<img width="1916" alt="js60" src="https://user-images.githubusercontent.com/86648892/212543046-2636e48e-03e1-462e-8ed6-c012c65a639b.png">

---

## practice_scroll.html

```jsx
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>lorem</h1>
  <div>
    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusantium quod, eaque blanditiis optio commodi temporibus facere fugit deleniti neque, deserunt corporis id tempore reiciendis cumque eos ipsam iste ratione vero molestias. Laborum, adipisci. Necessitatibus consequatur, mollitia ratione nihil dolores, iste possimus error enim impedit placeat eaque eius. Cumque numquam culpa officia sapiente provident voluptas ad, debitis suscipit, laudantium temporibus id consequatur excepturi nesciunt minima qui adipisci. Qui tempora voluptate minus. Quibusdam omnis mollitia nihil hic incidunt blanditiis libero, voluptates a voluptate ullam delectus tempore fugit sed obcaecati quos harum nisi, doloremque deserunt inventore consequuntur quaerat distinctio corporis repellendus. Maiores, dolore provident ut voluptatem cum sit aliquid tenetur sequi ea ullam commodi, obcaecati perspiciatis neque praesentium reprehenderit hic saepe veniam facilis sunt exercitationem libero enim reiciendis, ipsa amet? Deserunt, omnis beatae magni itaque distinctio quisquam quia ea aspernatur! Libero non natus impedit ipsam reprehenderit nobis aliquid accusantium officia laborum, repellat mollitia officiis vel tempore laboriosam, possimus corrupti! Numquam, quibusdam. Nemo deleniti nobis error omnis rerum dolore iste magni veritatis deserunt accusantium! Quidem necessitatibus ducimus corrupti esse expedita beatae ea voluptatibus ullam suscipit enim architecto, dolores nobis, ipsum ratione nulla dolorem eum commodi dolor saepe! Voluptates dicta adipisci consequuntur ducimus, quidem velit earum sunt error quasi facilis aliquam accusamus temporibus perspiciatis? Veniam ipsa laboriosam iste minima quis eveniet voluptas, corrupti accusantium adipisci, aliquid consectetur enim ipsam praesentium accusamus eos et repellendus alias placeat obcaecati nam! Aut, praesentium rerum maxime reprehenderit fuga ab ipsa sint adipisci, laudantium dignissimos nihil eaque veniam tenetur ex et esse consectetur asperiores quaerat incidunt cupiditate! Consectetur autem dolorum minus sapiente architecto tempore eum iste molestias sed! Asperiores ratione deleniti non. Quae, consequatur atque. Natus qui labore reiciendis deserunt beatae impedit sed, omnis aliquam iusto aperiam facilis mollitia a nobis molestias cum laborum distinctio ad repellendus quia enim. Nobis excepturi, cumque molestiae minima ut in ea, quibusdam facilis nihil vero molestias dolore, sapiente dolorum repellendus suscipit! Porro et magni voluptas, delectus tempore culpa at atque quaerat, maiores cum excepturi ratione eligendi officia sed a reprehenderit saepe accusantium. Facilis expedita nulla quae in eligendi amet omnis atque aperiam. Reprehenderit, at provident harum incidunt quibusdam placeat aspernatur aperiam quod voluptas molestias laudantium! In recusandae labore officia nobis possimus impedit, tempora laboriosam illo ut veritatis non consequatur odit ab amet eum deleniti quaerat sed. Deleniti aut aspernatur animi, enim totam dolorem vero quae commodi odio consectetur. In, pariatur sit nihil incidunt, quis corporis dolorum, officiis laborum eum aspernatur porro recusandae totam maxime itaque amet. Dignissimos beatae voluptates quibusdam doloremque earum nostrum distinctio tempore officiis incidunt laborum. Et ullam hic expedita possimus ratione iste, sequi, architecto impedit perferendis, corporis ad? Explicabo distinctio eius laboriosam autem qui eveniet asperiores, amet quidem iusto dolore doloribus alias, adipisci voluptate vero illo. Facere necessitatibus quidem perspiciatis ullam nobis, ducimus nostrum vitae, quis voluptates consequuntur atque sunt magni voluptatibus nesciunt deserunt aliquid magnam recusandae dicta sed facilis at quos inventore porro cum. Explicabo molestiae, at, cupiditate, eos quas error deleniti repellendus ducimus voluptatum fugiat laborum non sequi possimus ratione perferendis assumenda sunt laboriosam consequatur nobis sed. Nulla, eum? Mollitia, saepe nisi eius, consequuntur maxime aut officia iste perspiciatis inventore sint laudantium voluptates! Dignissimos ipsum consequatur eveniet nihil vel placeat officia recusandae, quibusdam quod, harum veritatis deleniti sapiente a minus dolorem dolores, cupiditate nulla obcaecati est. Quod culpa laborum libero laboriosam similique quo esse. Architecto saepe incidunt tempora iure, aut, voluptas, quae veniam culpa autem et possimus pariatur? Molestiae eveniet quae, eos illum error molestias obcaecati nulla? Non maiores deserunt blanditiis vitae quasi. Aspernatur labore voluptatum laborum deleniti illo nisi ut velit eligendi impedit hic rem totam iste perspiciatis, atque quae numquam quis tempore itaque sint doloribus aperiam. Mollitia laboriosam natus officia eius sint corrupti ea accusantium dolore nobis! Fugiat error aspernatur, dolorem accusantium ea eius ducimus, aliquam explicabo veritatis, illo vero? Fugit sed quos recusandae error aut inventore incidunt placeat vero nam exercitationem, provident consectetur unde obcaecati tempore deserunt suscipit ea earum. Corporis eaque ipsam facilis. Unde atque excepturi debitis non dolor consequuntur animi accusantium accusamus nulla perspiciatis minus temporibus quam sunt molestiae culpa nam, vero illo? Perspiciatis, blanditiis alias illum vitae consectetur, ullam, magnam ipsa nisi dignissimos laboriosam nesciunt ea ut. Aut facilis, amet ipsum soluta laborum, repellat pariatur maxime reiciendis animi natus, odit in vitae necessitatibus perferendis. Ab voluptates itaque autem esse fuga odit et facere. Libero eum perferendis vel dolorem possimus optio cum consectetur assumenda nesciunt officiis voluptatibus amet ipsam, rerum ducimus consequatur itaque voluptate excepturi facere quo nisi animi iusto hic eveniet. Culpa, reiciendis minus. Porro non vero doloremque ut magnam enim, ipsa, in commodi esse facilis molestias sint sunt provident tempore, eum dolorum alias at sapiente. Nihil iure quaerat magni error eos provident veniam possimus doloremque hic. Quam itaque harum animi alias eveniet hic qui! Ad nisi quisquam dicta ipsa distinctio, sed exercitationem recusandae excepturi ipsum dolorum illo voluptate aliquam ratione suscipit magni repellat impedit, fugit deserunt, adipisci cumque autem explicabo? Earum veritatis sunt perferendis, eligendi a mollitia ea ab officia at voluptatem. Perferendis doloribus quibusdam assumenda nihil corporis illo nesciunt laboriosam recusandae omnis fugit? Et exercitationem praesentium neque cumque ipsum dolor quod maiores voluptatem, ea unde temporibus corporis a adipisci quisquam tempora distinctio necessitatibus eos! Aliquam molestias iusto libero quis laudantium odio quas cum natus sunt accusamus inventore nisi architecto, numquam quibusdam doloremque modi, velit perferendis fugit porro explicabo quasi, dignissimos et minima? Delectus vitae provident perferendis cumque dolorem alias numquam incidunt, molestias, quos at dolorum voluptatem aliquid, qui tempora dolores doloribus quae? Deleniti pariatur ab distinctio asperiores, reprehenderit officia nesciunt odio, eaque obcaecati assumenda magni non voluptate aspernatur sed placeat ex, nobis modi adipisci repellat minima in voluptatum accusantium necessitatibus. Quia eum voluptate blanditiis dolor tenetur, quae magni architecto qui maiores. Distinctio dignissimos incidunt ratione delectus, culpa repellat nostrum voluptate dolores porro eius, placeat ipsum vitae laboriosam nam molestias nulla nemo sit corrupti illum dolore natus nesciunt similique aliquid expedita? Modi architecto mollitia cum porro, aliquam itaque tenetur recusandae, accusantium nobis enim blanditiis dolorum voluptatem placeat corporis, expedita nesciunt voluptates repellat.
  </div>

  <script>
    const loremDiv = document.querySelector('div')
    let cnt = 0
    function printEvent(event) {
      console.log(event)
      console.log(window.scrollY)             // 현재 수직으로 몇 픽셀만큼 스크롤되었는지 반환
      console.log(window.innerHeight)         // 현재 보고있는 화면의 높이 (window의 content area)
      console.log(document.body.scrollHeight) // 스크롤시키지 않았을 때 전체높이
      if (document.body.scrollHeight*0.95 <= window.innerHeight + window.scrollY) {
        cnt += 1
        const newText = `\nNew Text! ${cnt}`
        loremDiv.innerText += newText
      }
    }
    window.addEventListener('scroll', printEvent)
  </script>
</body>
</html>
```

<img width="1918" alt="js61" src="https://user-images.githubusercontent.com/86648892/212543042-9f34ffd6-6994-44e8-a514-8d2a0c54db93.png">

---

## practice_this.js

```jsx
const myPrice1 = {
  exchangeRate: 1432,
  prices: [10, 50, 100],

  printPrices: function () {
    this.prices.forEach(
      function (price) {
        // (1) this가 myPrice를 가리킴
        console.log(price * this.exchangeRate) // (2) this는 콜백함수의 것으로 최상위 객체인 window를 가리킴
      }.bind(this) // (3) 2이 문제를 해결하기 위해 사용
    )
  },
}

const myPrice2 = {
  exchangeRate: 1432,
  prices: [10, 50, 100],

  printPrices: function () {
    this.prices.forEach((price) => {
      // arrow function에 .bind(this)가 내포되어 있음
      console.log(price * this.exchangeRate)
    })
  },
}

myPrice1.printPrices()
/*
14320
71600
143200
*/
myPrice2.printPrices()
/*
14320
71600
143200
*/

const obj = {
  a: 1,
  test1: function () {
    console.log(this.a) // 1
  },
  test2: () => {
    console.log(this.a) // undefined
    console.log(this) // window
  },
}

obj.test1()
obj.test2()
```

---

## JS Prototype and Constructor

- JS에서 일종의 상속을 구현한 개념이라 우선 이해해두자
  - JS는 함수지향형이었으나 개발자들을 끌어들이기 위해 객체지향형 개념들을 구현
- [https://im-developer.tistory.com/98](https://im-developer.tistory.com/98)

## practice_prototype_and_constructor.js

```jsx
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
let myDog = new Dog("우유", 4)
myDog.attack()
let myCat = new Cat("키티", 3)
myCat.attack()

// (3) .__proto__

let bird = {
  name: "새",
  age: 2,
  attack: function () {
    console.log(`${this.name} 짹짹!`)
  },
}

let cutebirdy = {
  name: "참새",
  age: 4,
}

// 인스턴스의 prototype 속성 추가 (.__proto__)
cutebirdy.__proto__ = bird

console.log(bird.name) // 새
console.log(typeof bird) // object
bird.attack() // 새 짹짹!
cutebirdy.attack() // 참새 짹짹!
```

---

# 실습

## 새 탭에서 열기

```jsx
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .text-decoration-none {
      text-decoration: none;
    }
  </style>
</head>

<body>
  <a id="anchor" href="">GOOGLE</a>
  <script>
    /*
      JavaScript 코드만을 활용하여 a#anchor 요소를 아래와 같이 수정합니다.
        1) a 태그에 text-decoration-none 클래스를 추가합니다.
        2) a 태그의 href 속성은 https://google.com/ 입니다.
        3) a 태그의 target 속성은 _blank 입니다. (새 탭에서 열기)
    */
    const anchorTag = document.querySelector('#anchor')
    anchorTag.classList.add('text-decoration-none')
    anchorTag.href = 'https://google.com/'
    anchorTag.setAttribute('target', '_blank')
  </script>
</body>

</html>
```

<img width="1917" alt="js62" src="https://user-images.githubusercontent.com/86648892/212543040-70758c07-a4d9-4da8-a784-2f7334e2ca56.png">

## 고정된 todo 출력하기

```jsx
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>

<body>
  <div id="app"></div>
  <script>
    // div#app 요소 선택
    const app = document.querySelector('#app')
    // h1 태그를 createElement 로 생성
    const title = document.createElement('h1')
    // 생성한 h1태그의 내용을 '오늘의 Todo' 로 설정
    title.innerText = '오늘의 Todo'
    // ul, li 태그들을 생성 및 내용 추가
    const ulTag = document.createElement('ul')
    todos = ['양치하기', '공부하기', '휴식하기']
    todos.forEach((todo) => {
      const liTag = document.createElement('li')
      liTag.innerText = todo
      ulTag.appendChild(liTag)
    })
    // 각 태그들을 적절하기 div#app 요소에 자식요소로 추가. (#app > ul > li)
    app.appendChild(title)
    app.appendChild(ulTag)
  </script>
</body>

</html>
```

<img width="1913" alt="js63" src="https://user-images.githubusercontent.com/86648892/212543037-32bfa0de-eded-4120-be54-109c1349ed1b.png">

## 카드 출력하기

```jsx
<!DOCTYPE html>
<html lang="en">

<head>
  <title>Document</title>
  <!-- CSS only -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
</head>

<body>
  <div class="container">
    <section id="cardsSection" class="row">
      <!-- 카드 예시 -->
      <article class="col-4">
        <div class="card m-1">
          <div class="card-body">
            <h5 class="card-title">Example</h5>
            <p class="card-text">This is a card example.</p>
          </div>
        </div>
      </article>
      <!-- 카드 예시 -->
    </section>
  </div>

  <script>
    // section#cardSection에 예시와 같은 카드를 생성하여 추가하는 코드를 작성하시오.
    const cardsSection = document.querySelector('#cardsSection')

    function createCard(title, content) {
      // 여기에 카드를 작성하시오.
      const article = document.createElement('article')
      article.classList.add('col-4')

      const card = document.createElement('div')
      card.classList.add('card', 'm-1')

      const cardBody = document.createElement('div')
      cardBody.classList.add('card-body')

      const cardTitle = document.createElement('h5')
      cardTitle.classList.add('card-title')
      cardTitle.innerText = title

      const cardContent = document.createElement('p')
      cardContent.classList.add('card-text')
      cardContent.innerText = content

      cardBody.append(cardTitle, cardContent)
      card.appendChild(cardBody)
      article.appendChild(card)

      return article
    }

    // 카드 생성
    const newCard = createCard('Hello', 'World')

    // DOM에 추가
    cardsSection.appendChild(newCard)
  </script>
</body>

</html>
```

<img width="1918" alt="js64" src="https://user-images.githubusercontent.com/86648892/212543033-e53a0a8a-f44c-4a6b-9ac1-cefdbd43569a.png">

---

# 실습 advanced

## input 필터링 하기

```jsx
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>

<body>
  <div>
    Input: <input id="userInput" type="text" autofocus>
  </div>
  <div>
    Output: <span id="output"></span>
  </div>

  <script>
    /*
      현재 코드에서는 input#userInput에 입력한 내용이 그대로 span#output에 출력된다.
      아래 이미지를 참고하여 badWords에 포함된 단어가 사용자 입력에 포함되어 있을 경우,
      span#output에서 해당 단어를 '**' 로 바꿔 출력하도록 filterMessage 함수를 완성하시오.
      replaceAll 메서드를 검색 후 활용할 수 있습니다.
    */
    const badWords = ['바보', '멍청', '메롱',]
    const userInput = document.querySelector('#userInput')
    const output = document.querySelector('#output')

    function filterMessage(event) {
      // event.target은 이벤트가 발생한 대상 객체, 이 경우에 event.target은 userInput이며, 해당 타겟의 value는 output의 innerText에서 확인 가능
      let filteredInput = event.target.value
      // badWords에 포함된 단어가 입력될 경우, '**'으로 변환하여 output에 출력
      for (word of badWords) {
        filteredInput = filteredInput.replaceAll(word, '**')  // 입력한 값을 검사하여 badWords의 word와 매칭되는 것이 있을 시 **으로 변경
        // console.log(word)
        // console.log(filteredInput)
      }
      output.innerText = filteredInput
    }
      // output 출력 갱신
    userInput.addEventListener('input', filterMessage)
  </script>
</body>

</html>
```

<img width="1917" alt="js65" src="https://user-images.githubusercontent.com/86648892/212543030-1659e84a-5790-4c8c-88d3-7fbecf70008c.png">

## 카드 추가하기

```jsx
<!DOCTYPE html>
<html lang="en">

<head>
  <title>Document</title>
  <!-- CSS only -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
</head>

<body>
  <div class="container">

    <form id="form" class="my-3">
      <div class="mb-3">
        <input type="text" class="form-control" id="title" placeholder="New">
      </div>
      <div class="mb-3">
        <textarea class="form-control" id="content" rows="3" placeholder="Card"></textarea>
      </div>
      <div class="d-grid gap-2">
        <button class="btn btn-primary">add</button>
      </div>
    </form>

    <section id="cardsSection" class="row">
      <!-- 카드가 추가되는 부분 -->
    </section>

  </div>

  <script>
    /*
      사용자가 form 에 title과 content를 입력하고 submit하면, 예시와 같은 카드를 생성하여 div#cardSection에 추가하는 코드를 작성하시오.
      카드가 생성되면 기존에 입력된 input과 textarea의 내용은 삭제되어야 합니다.
    */
    const form = document.querySelector('#form')
    const titleInput = document.querySelector('#title')
    const contentInput = document.querySelector('#content')
    const cardsSection = document.querySelector('#cardsSection')

    form.addEventListener('submit', function (event) {
      event.preventDefault()
      const article = document.createElement('article')
      article.classList.add('col-4')

      const card = document.createElement('div')
      card.classList.add('card', 'm-1')

      const cardBody = document.createElement('div')
      cardBody.classList.add('card-body')

      const cardTitle = document.createElement('h5')
      cardTitle.classList.add('card-title')
      cardTitle.innerText = titleInput.value

      const cardText = document.createElement('p')
      cardText.classList.add('card-text')
      cardText.innerText = contentInput.value

      cardBody.append(cardTitle, cardText)
      card.appendChild(cardBody)
      article.appendChild(card)
      cardsSection.appendChild(article)

      event.target.reset()
    })
  </script>
</body>

</html>
```

<img width="1913" alt="js66" src="https://user-images.githubusercontent.com/86648892/212543027-7e3cfae5-40d6-4bd5-b7bf-6d87b009edab.png">

## todo 생성하기

```jsx
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>

<body>
  <form action="/todos/">
    <input type="text">
    <button>Add</button>
  </form>
  <ul></ul>

  <script>
    /*
    1. form에서 submit 이벤트 발생 시 input에 작성된 값 todo로 추가
    2. todo 추가 후 input value 값 초기화
    3. 빈 값인 데이터 입력 방지 및 알림창 출력
    */
    const form = document.querySelector('form')
    const todoInput = document.querySelector('input')
    const todos = document.querySelector('ul')

    form.addEventListener('submit', function (event) {
      event.preventDefault()
      const liTag = document.createElement('li')
      // 빈 값일 경우 입력 방지 및 알림창 출력
      if (todoInput.value) {
        liTag.innerText = todoInput.value
        todos.appendChild(liTag)
      } else {
        alert('내용을 입력하세요!')
      }
      // 추가 후 form 초기화를 통한 todoInput의 value 초기화
      event.target.reset()
    })
  </script>
</body>

</html>
```

<img width="1914" alt="js67" src="https://user-images.githubusercontent.com/86648892/212543025-060d9735-5837-4fb2-8c6f-5fb6df1898f5.png">

---

# JavaScript async and axios and promise

- 동기와 비동기
- JavaScript의 비동기 처리
- Axios 라이브러리
- Callback과 Promise
- AJAX

---

# 동기와 비동기

## 동기(Synchronous)

- 모든 일을 순서대로 하나씩 처리하는 것
- 순서대로 처리한다는 것은
  - 이전 작업이 끝나면 다음 작업을 시작한다는 것
- 요청과 응답을 동기식으로 처리한다면?
  - 요청을 보내고 응답이 올 때까지 기다렸다가 다음 로직을 처리
    - 아래 코드는 확인을 누르기 전까지 p태그는 보이지 않음

```jsx
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <button>버튼</button>
  <script>
    const btn = document.querySelector('button')
    btn.addEventListener('click', () => {
      alert('you clicked me!')
      const pElem = document.createElement('p')
      pElem.innerText = 'p Element'
      document.body.appendChild(pElem)
    })
  </script>
</body>
</html>
```

## 비동기(Asynchronous)

- 작업을 시작한 후 **결과를 기다리지 않고** 다음 작업을 처리하는 것
  - 병렬적 수행
- 시간이 필요한 작업들은 요청을 보낸 뒤 응답이 빨리 오는 작업부터 처리
- ex) Gmail에서 메일 전송을 누르면 목록 화면으로 전환되지만 실제로 메일을 보내는 작업은 병렬적으로 뒤에서 처리됨

```jsx
function slowRequest(callBack) {
  console.log("1. 오래 걸리는 작업 시작 ...")
  setTimeout(function () {
    callBack()
  }, 3000)
}

function myCallBack() {
  console.log("2. 콜백함수 실행됨")
}

slowRequest(myCallBack)
console.log("3. 다른 작업 실행")

/*
1. 오래 걸리는 작업 시작 ...
3. 다른 작업 실행
2. 콜백함수 실행됨
*/
```

## 비동기(Asynchronous)를 사용하는 이유

### 사용자 경험

- 예를 들어 아주 큰 데이터를 불러온 뒤 실행되는 앱이 있을 때, 동기로 처리한다면 데이터를 모두 불러온 뒤에야 앱의 실행 로직이 수행되므로 사용자들은 마치 앱이 멈춘 것과 같은 경험을 겪게 됨
- 즉, 동기식 처리는 특정 로직이 실행되는동안 다른 로직 실행을 차단하기 때문에 마치 프로그램이 응답하지 않는 듯한 사용자 경험을 만들게 됨
- **비동기로 처리한다면 먼저 처리되는 부분부터 보여줄 수 있으므로**, 사용자 경험에 긍정적인 효과를 볼 수 있음
  - 이와 같은 이유로 많은 웹 기능은 비동기 로직을 사용해서 구현되어있음

---

# JS의 비동기 처리

## JS는 Single Thread 언어

- JavaScript는 한 번에 하나의 일만 수행할 수 있는 **Single Thread** 언어로 동시에 여러 작업을 처리할 수 없음
- 즉, JavaScript는 하나의 작업을 요청한 순서대로 처리할 수 밖에 없음
- 그렇기에 JavaScript의 런타임 환경에서 비동기 처리와 관련한 작업을 진행

### [참고] Thread란?

- 작업을 처리할 때 실제로 작업을 수행하는 주체로
  - multi-thread라면 업무를 수행할 수 있는 주체가 여러 개라는 의미

## JS Runtime

- JavaScript 자체는 Single Thread이므로 비동기 처리를 할 수 있도록 도와주는 환경이 필요
- 특정 언어가 동작할 수 있는 환경을 "런타임(Runtime)"이라함
- JS에서 **비동기와 관련한 작업은 브라우저 또는 Node 환경에서 처리**
  - 브라우저 환경에서의 비동기 동작은 크게 다음의 요소들로 구성됨
    1. JS Engine의 **Call Stack**
    2. **Web API**
    3. **Task Queue**
    4. **Event Loop**

## 브라우저 환경에서의 비동기 처리 동작 방식

- 브라우저 환경에서 JS의 비동기는 아래와 같이 처리된다
  1. 모든 작업은 **Call Stack**(LIFO)으로 들어간 후 처리된다
  2. 오래 걸리는 작업이 **Call Stack**으로 들어오면 **Web API**로 보내서 처리하도록 한다
  3. Web API에서 처리가 끝난 작업들은 **Task Queue**(FIFO)에 순서대로 들어간다
  4. **Event Loop**가 **Call Stack**이 비어있는 것을 체크하고, **Task Queue**에서 가장 오래된 작업을 **Call Stack**으로 보낸다

### Call Stack

- 요청이 들어올 때마다 순차적으로 처리하는 Stack
  - LIFO
- 기본적인 JS의 Single Thread 작업 처리

### Web API

- JS 엔진이 아닌 브라우저에서 제공하는 runtime 환경으로 시간이 소요되는 작업을 처리
  - setTimeout, DOM Event, AJAX 요청 등

### Task Queue

- 비동기 처리된 Callback 함수가 대기하는 Queue
  - FIFO

### Event Loop

- Call Stack과 Task Queue를 지속적으로 모니터링
- Call Stack이 비어있는지 확인 후 비어있다면 Task Queue에서 대기 중인 오래된 작업을 Call Stack으로 Push

### 비동기 처리 예시 (setTimeout)

<img width="864" alt="js68" src="https://user-images.githubusercontent.com/86648892/212543672-f4b8e5c8-35fe-4ee2-8531-091e75364cd4.png">

- setTimeout 뒤에 붙는 숫자는 Web API에서의 처리 지연 시간을 의미하는 것이다
  - 즉, 0초를 주더라도 Web API로 넘어간다

```jsx
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <script>
    console.log('Hi')

    setTimeout(function () {
      console.log('SSAFY')
    }, 3000)

    console.log('Bye')
  </script>
</body>
</html>
```

## 정리

JavaScript는 한 번에 하나의 작업을 수행하는 Single Thread 언어로 동기적 처리를 하지만, 브라우저 환경에서는 Web API에서 처리된 작업이 지속적으로 Task Queue를 거쳐 Event Loop에 의해 Call Stack에 들어와 순차적으로 실행됨으로써 비동기 작업이 가능한 환경이 된다

---

# Axios 라이브러리

## Axios

- JS의 HTTP 웹 통신을 위한 라이브러리
- 확장 가능한 인터페이스와 쉽게 사용할 수 있는 비동기 통신 기능을 제공
- node 환경은 npm을 이용해서 설치 후 사용할 수 있고, browser 환경은 CDN을 이용해서 사용할 수 있음
- Axios 공식문서 및 Github
  - [https://axios-http.com/kr/docs/intro](https://axios-http.com/kr/docs/intro)
  - [https://github.com/axios/axios](https://github.com/axios/axios)
- `axios` 라는 객체를 통해 어디론가 요청을 보냄
  - Python에서는 `requests` 라이브러리 활용

## Axios 기본 구조

- get, post 등 여러 method 사용 가능
- `.then` 을 이용해서 요청이 성공했을 때 수행할 로직을 작성
- `.catch` 를 이용해서 요청이 실패했을 때 수행할 로직을 작성

### 고양이 사진 가져오기

- The Cat API 활용
  - [https://api.thecatapi.com/v1/images/search](https://api.thecatapi.com/v1/images/search))
  - 이미지를 요청해서 가져오는 작업을 비동기로 처리
- Python으로 요청해보기 (동기)

```python
import requests

print('고양이는 야옹')      # 1

cat_image_search_url = 'https://api.thecatapi.com/v1/images/search'
response = requests.get(cat_image_search_url)

if response.status_code == 200:
    print(response.json())  # 2
else:
    print('실패했다옹')

print('야옹야옹')           # 3

'''
고양이는 야옹
[{'id': '200', 'url': 'https://cdn2.thecatapi.com/images/200.jpg', 'width': 960, 'height': 720}]
야옹야옹
'''
```

- Axios로 요청해보기 (비동기)

<img width="574" alt="js69" src="https://user-images.githubusercontent.com/86648892/212543773-88017469-5050-4e1e-997a-ea035ee22649.png">

<img width="439" alt="js70" src="https://user-images.githubusercontent.com/86648892/212543772-d9b795ff-fd36-4b45-84f8-45606ea13613.png">

- 동기식 코드(Python)는 위에서부터 순서대로 처리가 되기에 첫번째 print가 출력되고 이미지를 가져오는 처리를 기다렸다가 다음 print가 출력되는 반면
- 비동기식 코드(JavaScript)는 바로 처리가 가능한 작업(console.log)은 바로 처리하고, 오래 걸리는 작업인 이미지를 요청하고 가져오는 일은 요청을 보내놓고 기다리지 않고 다음 코드로 진행 후 완료가 된 시점에 결과 출력이 진행됨

### 고양이 사진 가져오기 (완성)

1. 버튼을 누르면
2. 고양이 이미지를 요청하고
3. 요청이 처리되어 응답이 오면
4. 처리된 response에 있는 url을 img 태그에 넣어서 보여주기

```jsx
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <button>야옹아 이리온</button>

  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
    console.log('고양이는 야옹')
    const catImageSearchURL = 'https://api.thecatapi.com/v1/images/search'
    const btn = document.querySelector('button')

    btn.addEventListener('click', function () {
      axios.get(catImageSearchURL)
        .then((response) => {
          // console.log(response.data[0].url)
          imgElem = document.createElement('img')
          imgElem.setAttribute('src', response.data[0].url)
          document.body.appendChild(imgElem)
        })
        .catch((response) => {
          console.log('실패했다옹')
        })
        console.log('야옹야옹')
    })
  </script>
</body>
</html>
```

- 버튼을 누르면 `console.log` 가 먼저 출력되고 이미지 요청을 보낸다
- 버튼을 여러번 누르면 먼저 로딩되는 이미지부터 나오는 것을 볼 수 있다

## 정리

- axios는 비동기로 데이터 통신을 가능하게 하는 라이브러리
- 같은 방식으로 우리가 배운 Django REST API로 요청을 보내서 데이터를 받아온 후 처리할 수 있음

---

# Callback과 Promise

## 비동기 처리의 단점

- 비동기 처리의 핵심은 Web API로 들어오는 순서가 아니라
  - **작업이 완료되는 순서에 따라 처리**한다는 것
    - 개발자 입장에서 코드의 실행 순서가 불명확하다는 단점
      - **실행 결과를 예상하면서 코드를 작성할 수 없음**
- 이를 해결하기 위해 Callback 함수 사용

---

# Callback Function(콜백 함수)

## 콜백 함수란?

- **다른 함수의 인자로 전달되는 함수**를 콜백 함수라 한다
- 비동기에만 사용되는 함수가 아니며 동기, 비동기 상관없이 사용 가능
- 시간이 걸리는 **비동기 작업이 완료된 후 실행할 작업을 명시하는데 사용**되는 콜백 함수를 **비동기 콜백(asynchronous callback)**이라 부름

## 콜백 함수를 사용하는 이유

- 명시적인 호출이 아닌 특정한 조건 혹은 행동에 의해 호출되도록 작성할 수 있음
- “요청이 들어오면”, “이벤트가 발생하면”, “데이터를 받아오면” 등의 조건으로 이후 로직을 제어할 수 있음
- **비동기 처리를 순차적으로 동작할 수 있게함**
- 비동기 처리를 위해서는 콜백 함수의 형태가 반드시 필요함

## 콜백 지옥(Callback Hell)

- 콜백 함수는 연쇄적으로 발생하는 비동기 작업을 순차적으로 동작할 수 있게함
- 보통 어떤 기능의 실행 결과를 받아서 다른 기능을 수행하기위해 많이 사용하는데, 이 과정을 작성하다보면 비슷한 패턴이 계속 발생하게됨
- 비동기 처리를 위한 콜백을 작성할 때 마주하는 문제를 Callback Hell이라 하며, 그 때의 코드 작성 형태가 마치 피라미드와 같다해서 “Pyramid of Doom”이라고도 부름

<img width="879" alt="js71" src="https://user-images.githubusercontent.com/86648892/212543944-7a739850-130e-460e-a85e-36136877fcbb.png">

## 정리

- 콜백 함수는 비동기 작업을 순차적으로 실행할 수 있게 하는 반드시 필요한 로직
- 비동기 코드를 작성하다보면 콜백 함수로 인한 콜백 지옥은 반드시 나타나는 문제
  - 코드의 가독성을 해치고
  - 유지 보수가 어려워짐

---

# Promise(프로미스)

## Promise

- Callback Hell 문제를 해결하기 위해 등장한 비동기 처리를 위한 객체
- “작업이 끝나면 실행 시켜줄게”라는 약속(promise)
- 비동기 처리를 위한 객체
- **비동기 작업의 완료 또는 실패를 나타내는 객체**
- Promise 기반의 클라이언트가 **Axios** 라이브러리
  - `axios.get()` 은 프로미스 객체
  - “Promise based HTTP client for the browser and node.js”
  - 성공에 대한 약속 `.then()`
  - 실패에 대한 약속 `.catch()`
  - `.finally()` 는 성공과 실패 여부 관계없이 실행되는 로직

### then(callback)

- 요청한 작업이 성공하면 callback 실행
- callback은 **이전 작업의 성공 결과를 인자로 전달받음**
  - 즉, 앞에서 성공한 데이터를 담은 프로미스 객체가 들어옴

### catch(callback)

- `then()` 이 하나라도 실패하면 callback 실행
  - then은 chaining이 가능함
- callback은 이전 작업의 실패 객체를 인자로 전달받음
  - 실패한 정보를 가진 프로미스 객체가 들어옴

### then and catch

- then과 catch 모두 항상 promise 객체를 반환
  - 즉, 계속해서 **chaining을 할 수 있음**
  - chaining하기 위해서는 이전 then에서 `return`이 반드시 있어야 하며 이를 통해 Promise 객체를 반환해줘야 한다
- **axios로 처리한 비동기 로직이 항상 promise 객체를 반환**
- promise 방식은 비동기 처리를 일반적으로 위에서 아래로 적는 방식처럼 코드를 작성할 수 있음

<img width="577" alt="js72" src="https://user-images.githubusercontent.com/86648892/212543942-49542117-7349-4a8d-916d-be8a4e684be6.png">

<img width="323" alt="js73" src="https://user-images.githubusercontent.com/86648892/212543941-96178dba-8dbc-423a-bc87-2dedecf6d1f6.png">

```jsx
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
    const URL = 'https://jsonplaceholder.typicode.com/todos/1/'
    // 1. Axios
    // 1-1. Axios의 return 값은 Promise
    const myPromise = axios.get(URL)
    // console.log(myPromise) // Promise Object

    myPromise
      .then(response => {
        // console.log(response)
        return response.data
      })


    // 1-2. chaining
    axios.get(URL)
      .then(response => {
        console.log(response)
        return response.data
      })
      .then(response => {
        console.log(response)
        return response.title
      })
      .then(response => {
        console.log(response)
      })
      .catch(error => {
        console.log(error)
      })

    // 1-3. 다른 표기법(권장)
    axios({
      method: 'get',
      url: URL,
    })
      .then(response => {
        console.log(response)
        return response.data
      })
      .then(response => {
        console.log(response)
        return response.title
      })
      .then(response => {
        console.log(response)
      })
      .catch(error => {
        console.log(error)
      })
  </script>
</body>
</html>
```

## Promise가 보장하는 것 (vs 비동기 콜백)

- 비동기 콜백 작성 스타일과 달리 Promise가 보장하는 특징

1. callback 함수는 JavaScript의 Event Loop가 현재 실행 중인 Call Stack을 완료하기 이전에는 절대 호출되지 않음
   - Promise callback 함수는 Event Queue에 배치되는 엄격한 순서로 호출됨
2. 비동기 작업이 성공하거나 실패한 뒤에 `.then()` 메서드를 이용하여 추가한 경우에도 1번과 똑같이 동작
3. `.then()` 을 여러번 사용하여 여러개의 callback 함수를 추가할 수 있음 (Chaining)
   - 각각의 callback은 주어진 순서대로 하나하나 실행하게 된다
   - Chaining은 Promise의 가장 뛰어난 장점

---

## Axios and Promise Practice (Cat API and Dog API)

```jsx
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <button>야옹아 이리온</button>
  <button id="dog-btn">멍멍아 이리온</button>

  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
    // console.log('고양이는 야옹')
    const catImageSearchURL = 'https://api.thecatapi.com/v1/images/search'
    const btn = document.querySelector('button')

    const dogImageSearchURL = 'https://dog.ceo/api/breeds/image/random'
    const dogBtn = document.querySelector('#dog-btn')

    dogBtn.addEventListener('click', function (event) {
      axios({
        method: 'get',
        url: dogImageSearchURL
      })
        .then((response) => {
          console.log(response.data.message)
          const imgSrc = response.data.message
          return imgSrc
        })
        .then((imgSrc) => {
          const imgTag = document.createElement('img')
          imgTag.setAttribute('src', imgSrc)
          document.body.appendChild(imgTag)
        })
        .catch((error) => {
          console.log(error)
        })
    })

    // Promise 객체를 리턴하는 axios 라이브러리
    // console.log(axios.get(catImageSearchURL))

    btn.addEventListener('click', function () {
      // 권장 표기 방식
      axios({
        method: 'get',
        url: catImageSearchURL,
      })
        .then((response) => {
          // console.log(response.data[0].url)
          imgElem = document.createElement('img')
          return imgElem
        })
        .then((imgElem) => {
          imgElem.setAttribute('src', response.data[0].url)
          document.body.appendChild(imgElem)
        })
        .catch((error) => {
          console.log('실패했다옹')
        })
        console.log('야옹야옹')

      // 일반 표기 방식
      axios.get(catImageSearchURL)
        .then((response) => {
          // console.log(response.data[0].url)
          imgElem = document.createElement('img')
          return imgElem
        })
        .then((imgElem) => {
          imgElem.setAttribute('src', response.data[0].url)
          document.body.appendChild(imgElem)
        })
        .catch((error) => {
          console.log('실패했다옹')
        })
        // console.log('야옹야옹')
    })
  </script>
</body>
</html>
```

---

# AJAX

## AJAX란?

- **비동기 통신을 이용하면 화면 전체를 새로고침하지 않아도 서버로 요청을 보내고, 데이터를 받아 화면의 일부분만 업데이트 가능**
- 이러한 “비동기 통신 웹 개발 기술”을 Asynchronous Javascript And XML(AJAX)라 한다
- AJAX의 특징
  1. **페이지 새로고침없이** 서버에 요청
  2. 서버로부터 **응답(데이터)을 받아** 작업을 수행
- 이러한 비동기 웹 통신을 위한 라이브러리 중 하나가 Axios

---

# 비동기(Async) 적용하기

- 기존에는 form을 통해 요청을 보내고
  - HTML 파일을 다시 받아서 새로고침했음
- 더 이상 **form을 통해 요청을 보내지 않고**
  - **제출 양식만을 구성해놓고 해당 제출 양식과 이벤트에 axios를 붙여서**
    - 실질적으로 **요청을 보내는 것은 axios**
      - 이를 통해 HTML 파일을 다시 받아서 새로고침하는 것이 아니라 **필요한 데이터만 받음**
- HTML 파일에서 UI 구현
  - HTML 요소 중 업데이트가 필요한 부분에 대해 **axios가 서버에 데이터 요청**
    - view 함수에서 html 파일을 주는 것 (새로고침)이 아니라
      - 업데이트가 필요한 부분에 대한 정보만 제공 (**JsonResponse**)
        - **이걸 axios의 response에서 받아서**
          - **JS를 통해 HTML 내 요소들을 업데이트**
- JS와 Django의 문법 영역을 구분할 것
  - JavaScript가 데이터를 가져올 수 있는 부분은
    - **HTML 파일 내의 DOM 트리 내에 있거나**
    - **유저가 요청한 정보에 있거나**

---

## 팔로우 (follow) 비동기 적용

- 각각의 템플릿에서 script 코드를 작성하기 위한 block tag 영역 작성

<img width="838" alt="js74" src="https://user-images.githubusercontent.com/86648892/212543940-30fd6a08-bbef-486b-ab35-506d65b91360.png">

- axios CDN 작성

<img width="839" alt="js75" src="https://user-images.githubusercontent.com/86648892/212543937-48922846-5c53-4d8b-b7ca-c4f40b280757.png">

- form 요소 선택을 위해 id 속성 지정 및 선택
- 불필요해진 action과 method 속성은 삭제
  - 요청은 axios로 대체되기 때문

<img width="766" alt="js76" src="https://user-images.githubusercontent.com/86648892/212543935-09bff82a-83f2-4803-bd4c-00101d84eaa5.png">

<img width="765" alt="js77" src="https://user-images.githubusercontent.com/86648892/212543934-86d60073-ebfb-4e01-a914-4f0d090d0c9d.png">

- form 요소에 이벤트 핸들러 작성 및 submit 이벤트 취소

<img width="766" alt="js78" src="https://user-images.githubusercontent.com/86648892/212543933-1e55f598-5e82-4f34-9624-2c7cd80d6c0c.png">

- axios 요청 준비

<img width="767" alt="js79" src="https://user-images.githubusercontent.com/86648892/212543932-75a892fa-b69a-4463-b417-d8d4a1a4a515.png">

- **url에 작성할 user pk 가져오기 (HTML → JS)**

<img width="763" alt="js80" src="https://user-images.githubusercontent.com/86648892/212543931-565bebd4-b9e7-491e-9545-75446b24f556.png">

<img width="766" alt="js81" src="https://user-images.githubusercontent.com/86648892/212543930-658b9806-dcc4-417f-bc4a-4749a87a7717.png">

### `data-*attributes`

<img width="765" alt="js82" src="https://user-images.githubusercontent.com/86648892/212543928-d9873836-f8de-4f05-8dea-cd006af743e8.png">

- 사용자 지정 데이터 특성을 만들어 임의의 데이터를 HTML과 DOM 사이에서 교환할 수 있는 방법
- 모든 사용자 지정 테이터는 dataset 속성을 통해 사용할 수 있음
- `data-test-value`라는 이름의 특성을 지정했다면
  - JS에서는 `element.dataset.testValue`로 접근할 수 있음
- 속성명 작성 시 주의사항
  - 대소문자 여부에 상관없이 xml로 시작하면 안됨
  - 세미콜론을 포함해서는 안됨
  - 대문자를 포함해서는 안됨
- [https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/data-\*](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/data-*)

<img width="765" alt="js83" src="https://user-images.githubusercontent.com/86648892/212543927-3ddcd929-5782-4193-a8b9-866e46964632.png">

- **hidden 타입으로 숨겨져있는 csrf 값을 가진 input 태그 선택**

<img width="657" alt="js84" src="https://user-images.githubusercontent.com/86648892/212543926-658e70b0-036e-474e-ba8c-211957026654.png">

<img width="765" alt="js85" src="https://user-images.githubusercontent.com/86648892/212543925-112b6776-5688-4c2f-82b3-2d951a2b4c8c.png">

- **AJAX로 csrftoken 보내기**

<img width="767" alt="js86" src="https://user-images.githubusercontent.com/86648892/212543921-03db3217-74e7-443d-8bfc-f5dc50e24acf.png">

- 팔로우 버튼을 토글하기 위해서는 현재 팔로우가 된 상태인지 여부 확인 필요
  - axios 요청을 통해 받는 response 객체를 활용해 view 함수를 통해서 팔로우 여부를 파악할 수 있는 변수를 담아 JSON 타입으로 응답하기
- 팔로우 여부를 확인하기 위한 is_followed 변수 작성 및 JSON 응답

<img width="768" alt="js87" src="https://user-images.githubusercontent.com/86648892/212543918-74de0429-1baf-4dd0-9b75-94fe528353bf.png">

- view 함수에서 응답한 is_followed를 사용해 버튼 토글하기

<img width="767" alt="js88" src="https://user-images.githubusercontent.com/86648892/212543917-623b611d-7e59-44b2-aa1c-734a0e99fde8.png">

- 네트워크 요청 결과 확인
  - 개발자 도구 - Network

<img width="669" alt="js89" src="https://user-images.githubusercontent.com/86648892/212543916-5bdbbbbd-8582-4cf7-baf4-0107155db056.png">

<img width="625" alt="js90" src="https://user-images.githubusercontent.com/86648892/212543915-32ed6039-f93f-4220-956e-39ea1bf13914.png">

### [참고] XHR

- “XMLHttpRequest”
- AJAX 요청을 생성하는 JavaScript API
- XHR의 메서드로 브라우저와 서버 간 네트워크 요청을 전송할 수 있음
- **Axios는 손쉽게 XHR을 보내고 응답 결과를 Promise 객체로 반환해주는 라이브러리**

### 팔로워와 팔로잉 수 비동기 적용

- span 태그와 id 속성 작성

<img width="797" alt="js91" src="https://user-images.githubusercontent.com/86648892/212543914-4a8998ac-1e42-4398-b6bc-73538bddfb7d.png">

<img width="766" alt="js92" src="https://user-images.githubusercontent.com/86648892/212543913-a3a867dc-681b-457e-b513-cd2e9b8cb9a8.png">

- 팔로워와 팔로잉 인원 수 연산은 view 함수에서 진행하여 결과를 응답으로 전달

<img width="768" alt="js93" src="https://user-images.githubusercontent.com/86648892/212543912-b4f61905-b733-464d-a2ba-902f3b46038f.png">

- view 함수에서 응답한 연산 결과를 사용해 각 태그의 인원 수 값 변경

<img width="765" alt="js94" src="https://user-images.githubusercontent.com/86648892/212543910-a3afe8c2-f206-49fa-af60-0e16ba6ffb5b.png">

---

# Follows and Likes 비동기 적용 최종 코드

## Follows

### `accounts/profile.html`

```jsx
{% extends 'base.html' %}

{% block content %}
  <h1>{{ person.username }}님의 프로필</h1>
  <div>
    팔로워 : <span id="followers-count">{{ person.followers.all|length }}</span>  /
    팔로잉 : <span id="followings-count">{{ person.followings.all|length }}</span>
  </div>

  {% if request.user != person %}
    <div>
      <form id="follow-form" data-user-id="{{ person.pk }}">
        {% csrf_token %}
        {% if request.user in person.followers.all %}
          <input type="submit" value="언팔로우">
        {% else %}
          <input type="submit" value="팔로우">
        {% endif %}
      </form>
    <div>
  {% endif %}

  <h2>{{ person.username }}이 작성한 모든 게시글</h2>
  {% for article in person.article_set.all %}
    <div>{{ article.title }}</div>
  {% endfor %}

  <hr>

  <h2>{{ person.username }}이 작성한 모든 댓글</h2>
  {% for comment in person.comment_set.all %}
    <div>{{ comment.content }}</div>
  {% endfor %}

  <hr>

  <h2>{{ person.username }}이 좋아요 한 모든 게시글</h2>
  {% for article in person.like_articles.all %}
    <div>{{ article.title }}</div>
  {% endfor %}

  <a href="{% url 'articles:index' %}">back</a>
{% endblock content %}

{% block script %}
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
    const form = document.querySelector('#follow-form')
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
    form.addEventListener('submit', function (event) {
      event.preventDefault()
      const userId = event.target.dataset.userId
      axios({
        method: 'post',
        url: `/accounts/${userId}/follow/`,
        headers: {'X-CSRFToken': csrftoken,}
      })
        .then((response) => {
          // console.log(response)
          // Follow 버튼 토글 (새로고침 없이)
          const isFollowed = response.data.is_followed
          const followBtn = document.querySelector('#follow-form > input[type=submit]')
          if (isFollowed === true) {
            followBtn.value = '언팔로우'
          } else {
            followBtn.value = '팔로우'
          }
          // 팔로워 및 팔로잉 수 변경 (새로고침 없이)
          const followersCountTag = document.querySelector('#followers-count')
          const followingsCountTag = document.querySelector('#followings-count')
          const followersCount = response.data.followers_count
          const followingsCount = response.data.followings_count
          followersCountTag.innerText = followersCount
          followingsCountTag.innerText = followingsCount
        })
        .catch((error) => {
          console.log(error.response)
        })
    })
  </script>
{% endblock script %}
```

### `accounts/views.py`

```python
from django.http import JsonResponse

@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        User = get_user_model()
        me = request.user
        you = User.objects.get(pk=user_pk)
        if me != you:
            if you.followers.filter(pk=me.pk).exists():
                you.followers.remove(me)
                is_followed = False
            else:
                you.followers.add(me)
                is_followed = True
            context = {
                'is_followed': is_followed,
                'followers_count': you.followers.count(),
                'followings_count': you.followings.count(),
            }
            return JsonResponse(context)
        return redirect('accounts:profile', you.username)
    return redirect('accounts:login')
```

## Likes

- 좋아요 비동기 적용은 팔로우와 동일한 흐름 + `forEach()` + `querySelectorAll()`
- index 페이지 각 게시글에 좋아요 버튼이 있기 때문

### `articles/index.html`

```jsx
{% extends 'base.html' %}

{% block content %}
  <h1>Articles</h1>
  {% if request.user.is_authenticated %}
    <a href="{% url 'articles:create' %}">CREATE</a>
  {% endif %}
  <hr>
  {% for article in articles %}
    <p>
      <b>작성자 : <a href="{% url 'accounts:profile' article.user %}">{{ article.user }}</a></b>
    </p>
    <p>글 번호 : {{ article.pk }}</p>
    <p>제목 : {{ article.title }}</p>
    <p>내용 : {{ article.content }}</p>
    <div>
      <form class="like-forms" data-article-id="{{ article.pk }}">
        {% csrf_token %}
        {% if request.user in article.like_users.all %}
          <input type="submit" value="좋아요 취소" id="like-{{ article.pk }}">
        {% else %}
          <input type="submit" value="좋아요" id="like-{{ article.pk }}">
        {% endif %}
      </form>
    </div>
    <a href="{% url 'articles:detail' article.pk %}">상세 페이지</a>
    <hr>
  {% endfor %}
{% endblock content %}

{% block script %}
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
    const forms = document.querySelectorAll('.like-forms')
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
    // 모든 게시글들의 좋아요 버튼에 대하여 submit이 일어날 경우 axios 요청 설정
    forms.forEach((form) => {
      form.addEventListener('submit', function (event) {
        event.preventDefault()
        const articleId = event.target.dataset.articleId
        axios({
          method: 'post',
          url: `/articles/${articleId}/likes/`,
          headers: {'X-CSRFToken': csrftoken},
        })
          .then((response) => {
            // console.log(response)
            // 좋아요 버튼 토글 (새로고침 없이)
            const isLiked = response.data.is_liked
            const likeBtn = document.querySelector(`#like-${articleId}`)
            if (isLiked === true) {
              likeBtn.value = '좋아요 취소'
            } else {
              likeBtn.value = '좋아요'
            }
          })
          .catch((error) => {
            console.log(error.response)
          })
      })
    })
  </script>
{% endblock script %}
```

### `articles/views.py`

```python
from django.http import JsonResponse

@require_POST
def likes(request, article_pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=article_pk)
        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)
            is_liked = False
        else:
            article.like_users.add(request.user)
            is_liked = True
        context = {
            'is_liked': is_liked,
        }
        return JsonResponse(context)
    return redirect('accounts:login')
```

---

## 왜 비동기(Asynchronous) 방식이 필요할까

- “human-centered design with UX”
  - “인간 중심으로 설계된 사용자 경험”
  - 실제 AJAX라는 용어를 처음 논문에서 사용한 Jesse James Garrett이 AJAX를 소개하며 강조한 한 마디

---

## Follow and Like 추가 구현 코드

- Follow
  - Unfollow와 Follow 버튼의 색깔 변경
- Like
  - 해당 게시글 좋아요 개수 표시
  - font awesome을 통해 좋아요 버튼 하트 모양으로 구현

### `accounts/profile.html`

```jsx
{% extends 'base.html' %}

{% block content %}
  <h1>{{ person.username }}의 프로필 페이지</h1>
  {% with followings=person.followings.all followers=person.followers.all %}
    <div>
      팔로잉 수: <span id="followings-count">{{ followings|length }}</span>
      팔로워 수: <span id="followers-count">{{ followers|length }}</span>
    </div>
    {% if user != person %}
      <div>
        <form id="follow-form" data-user-id="{{ person.pk }}">
          {% csrf_token %}
          {% if user in followers %}
            <input type="submit" value="Unfollow" class="text-danger">
          {% else %}
            <input type="submit" value="Follow" class="text-primary">
          {% endif %}
        </form>
      </div>
    {% endif %}
  {% endwith %}

  <hr>

  <h2>{{ person.username }}가 작성한 게시글</h2>
  {% for article in person.article_set.all %}
    <div>{{ article.title }}</div>
  {% endfor %}

  <hr>

  <h2>{{ person.username }}가 작성한 댓글</h2>
  {% for comment in person.comment_set.all %}
    <div>{{ comment.content }}</div>
  {% endfor %}

  <hr>

  <h2>{{ person.username }}가 좋아요를 누른 게시글</h2>
  {% for article in person.like_articles.all %}
    <div>{{ article.title }}</div>
  {% endfor %}

  <a href="{% url 'articles:index' %}">[back]</a>

{% endblock content %}

{% block script %}
  <script>
    const form = document.querySelector('#follow-form')
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
    form.addEventListener('submit', function (event) {
      event.preventDefault()
      const userId = event.target.dataset.userId
      axios({
        method: 'post',
        url: `/accounts/${userId}/follow/`,
        headers: {'X-CSRFToken': csrftoken},
      })
        .then((response) => {
          console.log(response)
          const isFollowed = response.data.is_followed
          const followersCount = response.data.followers_count
          const followingsCount = response.data.followings_count

          const followBtn = document.querySelector('#follow-form > input[type=submit]')
          const followingsCountTag = document.querySelector('#followings-count')
          const followersCountTag = document.querySelector('#followers-count')

          if (isFollowed === true) {
            followBtn.value = 'Unfollow'
            // followBtn.style.color = 'red'
            followBtn.classList.toggle('text-danger')
            followBtn.classList.toggle('text-primary')
          } else {
            followBtn.value = 'Follow'
            // followBtn.style.color = 'blue'
            followBtn.classList.toggle('text-primary')
            followBtn.classList.toggle('text-danger')
          }

          followingsCountTag.innerText = followingsCount
          followersCountTag.innerText = followersCount
        })
    })
  </script>
{% endblock script %}
```

### `accounts/views.py`

```python
from django.http import JsonResponse

@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        User = get_user_model()
        me = request.user
        you = get_object_or_404(User, pk=user_pk)
        if me != you:
            if you.followers.filter(pk=me.pk).exists():
                you.followers.remove(me)
                is_followed = False
            else:
                you.followers.add(me)
                is_followed = True
            context = {
                'is_followed': is_followed,
                'followers_count': you.followers.count(),
                'followings_count': you.followings.count(),
            }
            return JsonResponse(context)
        return redirect('accounts:profile', you.username)
    return redirect('accounts:login')
```

### `articles/index.html`

```jsx
{% extends 'base.html' %}

{% block content %}
  <h1>Articles</h1>
  {% if request.user.is_authenticated %}
    <a href="{% url 'articles:create' %}">[CREATE]</a>
  {% else %}
    <a href="{% url 'accounts:login' %}">[새 글을 작성하려면 로그인하세요.]</a>
  {% endif %}
  <hr>
  {% for article in articles %}
    <p>작성자 :
      <a href="{% url 'accounts:profile' article.user.username %}">{{ article.user }}</a>
    </p>
    <p>글 번호 : {{ article.pk }}</p>
    <p>글 제목 : {{ article.title }}</p>
    <p>글 내용 : {{ article.content }}</p>
    <div>
      <form class="like-form" data-article-id="{{ article.pk }}">
        {% csrf_token %}
        {% if user in article.like_users.all %}
          <button id="like-{{ article.pk }}" type="submit" class="btn btn-lg default" style="font-size: 25px; color: red; border: none">
            <i class="fa-solid fa-heart" id="heart-{{ article.pk }}"></i>
          </button>
        {% else %}
          <button id="like-{{ article.pk }}" type="submit" class="btn btn-lg default" style="font-size: 25px; color: red; border: none">
            <i class="fa-regular fa-heart" id="heart-{{ article.pk }}"></i>
          </button>
        {% endif %}
      </form>
      <p>
        <span id="like-count-{{ article.pk }}">
          {{ article.like_users.all|length }}
        </span>
        명이 이 글을 좋아합니다.
      </p>
    </div>
    <a href="{% url 'articles:detail' article.pk %}">[DETAIL]</a>
    <hr>
  {% endfor %}
{% endblock content %}

{% block script %}
  <script>
    const forms = document.querySelectorAll('.like-form')
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

    forms.forEach((form) => {
      form.addEventListener('submit', function (event) {
        event.preventDefault()
        const articleId = event.target.dataset.articleId
        axios({
          method: 'post',
          url: `/articles/${articleId}/likes/`,
          headers: {'X-CSRFToken': csrftoken},
        })
          .then((response) => {
            // console.log(response)
            const isLiked = response.data.is_liked
            const likeCounts = response.data.like_counts
            // const likeBtn = document.querySelector(`#like-${articleId}`)
            const likeCountTag = document.querySelector(`#like-count-${articleId}`)
            const heart = document.querySelector(`#heart-${articleId}`)

            if (isLiked === true) {
              heart.classList.remove('fa-regular')
              heart.classList.add('fa-solid')
            } else {
              heart.classList.remove('fa-solid')
              heart.classList.add('fa-regular')
            }

            likeCountTag.innerText = likeCounts
          })
          .catch((error) => {
            console.log(error.response)
          })
      })
    })
  </script>
{% endblock script %}
```

### `articles/views.py`

```python
from django.http import JsonResponse

@require_POST
def likes(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)
            is_liked = False
            like_counts = article.like_users.count()
        else:
            article.like_users.add(request.user)
            is_liked = True
            like_counts = article.like_users.count()
        context = {
            'is_liked': is_liked,
            'like_counts': like_counts,
        }
        return JsonResponse(context)
    return redirect('accounts:login')
```

---
