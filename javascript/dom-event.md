## JavaScript DOM and Event

---

- DOM
- Event
- this

## DOM

---

### DOM

- “브라우저에서의 JavaScript”
  - JavaScript는 웹 페이지에서 다양한 기능을 구현하는 스크립트 언어
  - 정적인 정보만 보여주던 웹 페이지를 데이터가 주기적으로 갱신되거나, 사용자와 상호 작용을 하거나, 애니메이션 등이 동작하게 하는 것을 가능하게 함
  - 스크립트 언어(Script Language)란?
    - 기존에 존재하는 응용 소프트웨어를 제어하는 컴퓨터 프로그래밍 언어

### 웹 페이지에서의 JavaScript

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

### 브라우저가 웹 페이지를 불러오는 과정

<img width="549" alt="js37" src="https://user-images.githubusercontent.com/86648892/212543080-ca4e7224-bda4-4cf6-8580-7e121a36c986.png">

- 웹 페이지를 브라우저로 불러오면
  - 브라우저는 코드(HTML, CSS, JavaScript)를 실행 환경(브라우저 탭)에서 실행
  - JavaScript는 **DOM API**를 통해 HTML과 CSS를 동적으로 수정
    - 사용자 인터페이스를 업데이트하는 일에 가장 많이 쓰임

### DOM

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

### DOM에 접근하기

- 모든 웹 브라우저는 스크립트 언어가 손쉽게 웹 페이지의 요소에 접근할 수 있도록 만들기 위해 DOM 구조를 항상 사용
- 우리는 “DOM 주요 객체”들을 활용하여 문서를 조작하거나 특정 요소들을 얻을 수 있음

### DOM의 주요 객체

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

## DOM 조작

---

- Document가 제공하는 기능을 사용해 웹 페이지 문서 조작하기
- DOM 조작 순서
  1. **선택 (Select)**
  2. **조작 (Manipulation)**
     - 생성, 추가, 삭제 등

### 선택 관련 메서드

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

### 조작 관련 메서드

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

### 조작 관련 메서드 (속성 조회 및 설정)

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

## Event

---

- Event란 프로그래밍하고 있는 시스템에서 일어나는 사건(action) 혹은 발생(occurence)으로, 각 이벤트에 대해 조작할 수 있도록 특정 시점을 시스템이 알려주는 것
  - 즉, 웹 페이지에서 어떠한 행동에 대해 여러 사건들이 발생함
    - 예를 들어 사용자가 웹 페이지의 버튼을 클릭하면 클릭에 대한 이벤트가 발생하고, 마우스 오버를 하면 마우스 오버에 대한 이벤트가 발생
      - 해당 이벤트에 대하여 이동을 하거나, 카테고리가 뜨는 등 이벤트를 통해 사건에 대한 결과를 받거나 조작할 수 있음
  - 웹에서는 다양한 Event가 존재
    - 키보드 키 입력, 브라우저 닫기, 데이터 제출, 텍스트 복사 등

### Event Object

- 네트워크 활동이나 사용자와의 상호작용과 같은 사건의 발생을 알리기 위한 객체
- Event 발생
  - 마우스를 클릭하거나 키보드를 누르는 등 사용자 행동으로 발생할 수도 있고
  - 특정 메서드를 호출하여 프로그래밍적으로도 만들어낼 수 있음
- DOM 요소는 Event를 받고 (**”수신”**)
  - 받은 Event를 **“처리”**할 수 있음
  - Event 처리는 주로 addEventListener()라는 Event Handler를 다양한 HTML 요소에 **“부착”**해서 처리함

### Event Handler

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

## Event 취소

---

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

## Event 실습

---

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

## this

---

- 어떠한 object를 가리키는 키워드
  - java에서의 this와 python에서의 self는 인스턴스 자기자신을 가리킴
- JavaScript의 함수는 호출될 때 this를 암묵적으로 전달받음
- JavaScript에서의 this는 일반적인 프로그래밍 언어에서의 this와 조금 다르게 동작
- JavaScript는 **해당 함수 호출 방식에 따라 this에 바인딩되는 객체가 달라짐**
  - 즉, 함수를 선언할 때 this에 객체가 결정되는 것이 아니고
    - 함수를 호출할 때 **함수가 어떻게 호출되었는지에 따라 동적으로 결정됨**

### 전역 문맥에서의 this

- 브라우저의 전역 객체인 window를 가리킴
  - 전역 객체란 모든 객체의 유일한 최상위 객체를 의미
    - `console.log(this)`
      - window

### 함수 문맥에서의 this

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

### 화살표 함수

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

### this 정리

- this는 호출되는 순간에 결정되는 것
  - 즉, 런타임에 결정되는 것
    - addEventListener는 예외
- this가 런타임에 결정되면 장점도 있고 단점도 있음
  - 장점
    - 함수(메서드)를 하나만 만들어서 여러 객체에서 재사용할 수 있다
  - 단점
    - 이런 유연함이 실수로 이어질 수 있다는 것은 단점

## this practice

---

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

### practice_element.html

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

### practice_event.html

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

### practice_scroll.html

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

### practice_this.js

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

## JS Prototype and Constructor

---

- JS에서 일종의 상속을 구현한 개념이라 우선 이해해두자
  - JS는 함수지향형이었으나 개발자들을 끌어들이기 위해 객체지향형 개념들을 구현
- [https://im-developer.tistory.com/98](https://im-developer.tistory.com/98)

### practice_prototype_and_constructor.js

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

## 실습

---

### 새 탭에서 열기

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

### 고정된 todo 출력하기

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

### 카드 출력하기

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

## 실습 advanced

---

### input 필터링 하기

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

### 카드 추가하기

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

### todo 생성하기

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
