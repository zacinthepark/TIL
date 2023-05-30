## JavaScript 기초 문법

---

- Starting JavaScript
- JavaScript 기초 문법
- 함수
- Array와 Object

## Starting JavaScript

---

### JavaScript를 배워야하는 이유

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

### JavaScript의 역사

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

## JavaScript 실행환경 구성

---

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

## JavaScript 기초 문법

---

### 코드 작성법

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

### 변수와 식별자

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

- 선언 (Declaration): 변수를 생성하는 행위 또는 시점
- 할당 (Assignment): 선언된 변수에 값을 저장하는 행위 또는 시점
- 초기화 (Initialization): 선언된 변수에 처음으로 값을 저장하는 행위 또는 시점

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

## 데이터 타입

---

- JavaScript의 모든 값은 특정한 데이터 타입을 가짐
- 크게 **원시 타입(Primitive type)**과 **참조 타입(Reference type)**으로 분류됨

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

## 연산자

---

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

## 조건문

---

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
- `break` 및 `default`문은 “선택적”으로 사용 가능
- `break`문이 없는 경우 `break`문을 만나거나 `default`문을 실행할 때까지 다음 조건문 실행
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

## 반복문

---

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

## 함수

---

- 참조 타입 중 하나로써 function 타입에 속함
- JavaScript에서 함수를 정의하는 방법은 주로 2가지로 구분됨
  - 함수 선언식 (function declaration)
  - 함수 표현식 (function expression)

### 함수의 정의

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

---

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

### Arrow Function

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

## Array와 Object

---

- JavaScript의 데이터 타입 중 참조 타입(reference)에 해당하는 타입은
  - Array와 Object이며
    - 객체라고 말함
- 객체는 속성들의 모음(collection)
  - (참고) 객체 안쪽의 속성들은 메모리에 할당되어있고 해당 객체는 메모리의 시작 주소 값을 가리키고 있는 형태로 이루어져 있다

## 배열(Array)

---

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

### 배열 메서드 기초

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

### 배열 메서드 심화

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

- `array.every(callback(element[, index[, array]]))`
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

## 객체(Object)

---

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

### 객체 관련 문법

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

## JavaScriptON (JavaScript Object Notation)

---

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

### [참고] 배열은 객체다

- 키와 속성들을 담고 있는 참조 타입의 객체 (object)
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

## Practices

---

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
