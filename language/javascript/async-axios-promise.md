## JavaScript async and axios and promise

---

- 동기와 비동기
- JavaScript의 비동기 처리
- Axios 라이브러리
- Callback과 Promise
- AJAX

## 동기와 비동기

---

### 동기(Synchronous)

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

### 비동기(Asynchronous)

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

### 비동기(Asynchronous)를 사용하는 이유

### 사용자 경험

- 예를 들어 아주 큰 데이터를 불러온 뒤 실행되는 앱이 있을 때, 동기로 처리한다면 데이터를 모두 불러온 뒤에야 앱의 실행 로직이 수행되므로 사용자들은 마치 앱이 멈춘 것과 같은 경험을 겪게 됨
- 즉, 동기식 처리는 특정 로직이 실행되는동안 다른 로직 실행을 차단하기 때문에 마치 프로그램이 응답하지 않는 듯한 사용자 경험을 만들게 됨
- **비동기로 처리한다면 먼저 처리되는 부분부터 보여줄 수 있으므로**, 사용자 경험에 긍정적인 효과를 볼 수 있음
  - 이와 같은 이유로 많은 웹 기능은 비동기 로직을 사용해서 구현되어있음

## JS의 비동기 처리

---

### JS는 Single Thread 언어

- JavaScript는 한 번에 하나의 일만 수행할 수 있는 **Single Thread** 언어로 동시에 여러 작업을 처리할 수 없음
- 즉, JavaScript는 하나의 작업을 요청한 순서대로 처리할 수 밖에 없음
- 그렇기에 JavaScript의 런타임 환경에서 비동기 처리와 관련한 작업을 진행

### [참고] Thread란?

- 작업을 처리할 때 실제로 작업을 수행하는 주체로
  - multi-thread라면 업무를 수행할 수 있는 주체가 여러 개라는 의미

### JS Runtime

- JavaScript 자체는 Single Thread이므로 비동기 처리를 할 수 있도록 도와주는 환경이 필요
- 특정 언어가 동작할 수 있는 환경을 "런타임(Runtime)"이라함
- JS에서 **비동기와 관련한 작업은 브라우저 또는 Node 환경에서 처리**
  - 브라우저 환경에서의 비동기 동작은 크게 다음의 요소들로 구성됨
    1. JS Engine의 **Call Stack**
    2. **Web API**
    3. **Task Queue**
    4. **Event Loop**

### 브라우저 환경에서의 비동기 처리 동작 방식

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

### 정리

JavaScript는 한 번에 하나의 작업을 수행하는 Single Thread 언어로 동기적 처리를 하지만, 브라우저 환경에서는 Web API에서 처리된 작업이 지속적으로 Task Queue를 거쳐 Event Loop에 의해 Call Stack에 들어와 순차적으로 실행됨으로써 비동기 작업이 가능한 환경이 된다

## Axios 라이브러리

---

### Axios

- JS의 HTTP 웹 통신을 위한 라이브러리
- 확장 가능한 인터페이스와 쉽게 사용할 수 있는 비동기 통신 기능을 제공
- node 환경은 npm을 이용해서 설치 후 사용할 수 있고, browser 환경은 CDN을 이용해서 사용할 수 있음
- Axios 공식문서 및 Github
  - [https://axios-http.com/kr/docs/intro](https://axios-http.com/kr/docs/intro)
  - [https://github.com/axios/axios](https://github.com/axios/axios)
- `axios` 라는 객체를 통해 어디론가 요청을 보냄
  - Python에서는 `requests` 라이브러리 활용

### Axios 기본 구조

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

### 정리

- axios는 비동기로 데이터 통신을 가능하게 하는 라이브러리
- 같은 방식으로 우리가 배운 Django REST API로 요청을 보내서 데이터를 받아온 후 처리할 수 있음

## Callback과 Promise

---

### 비동기 처리의 단점

- 비동기 처리의 핵심은 Web API로 들어오는 순서가 아니라
  - **작업이 완료되는 순서에 따라 처리**한다는 것
    - 개발자 입장에서 코드의 실행 순서가 불명확하다는 단점
      - **실행 결과를 예상하면서 코드를 작성할 수 없음**
- 이를 해결하기 위해 Callback 함수 사용

### 콜백 함수란?

- **다른 함수의 인자로 전달되는 함수**를 콜백 함수라 한다
- 비동기에만 사용되는 함수가 아니며 동기, 비동기 상관없이 사용 가능
- 시간이 걸리는 **비동기 작업이 완료된 후 실행할 작업을 명시하는데 사용**되는 콜백 함수를 **비동기 콜백(asynchronous callback)**이라 부름

### 콜백 함수를 사용하는 이유

- 명시적인 호출이 아닌 특정한 조건 혹은 행동에 의해 호출되도록 작성할 수 있음
- “요청이 들어오면”, “이벤트가 발생하면”, “데이터를 받아오면” 등의 조건으로 이후 로직을 제어할 수 있음
- **비동기 처리를 순차적으로 동작할 수 있게함**
- 비동기 처리를 위해서는 콜백 함수의 형태가 반드시 필요함

### 콜백 지옥(Callback Hell)

- 콜백 함수는 연쇄적으로 발생하는 비동기 작업을 순차적으로 동작할 수 있게함
- 보통 어떤 기능의 실행 결과를 받아서 다른 기능을 수행하기위해 많이 사용하는데, 이 과정을 작성하다보면 비슷한 패턴이 계속 발생하게됨
- 비동기 처리를 위한 콜백을 작성할 때 마주하는 문제를 Callback Hell이라 하며, 그 때의 코드 작성 형태가 마치 피라미드와 같다해서 “Pyramid of Doom”이라고도 부름

<img width="879" alt="js71" src="https://user-images.githubusercontent.com/86648892/212543944-7a739850-130e-460e-a85e-36136877fcbb.png">

### 정리

- 콜백 함수는 비동기 작업을 순차적으로 실행할 수 있게 하는 반드시 필요한 로직
- 비동기 코드를 작성하다보면 콜백 함수로 인한 콜백 지옥은 반드시 나타나는 문제
  - 코드의 가독성을 해치고
  - 유지 보수가 어려워짐

## Promise(프로미스)

---

### Promise

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

### Promise가 보장하는 것 (vs 비동기 콜백)

- 비동기 콜백 작성 스타일과 달리 Promise가 보장하는 특징

1. callback 함수는 JavaScript의 Event Loop가 현재 실행 중인 Call Stack을 완료하기 이전에는 절대 호출되지 않음
   - Promise callback 함수는 Event Queue에 배치되는 엄격한 순서로 호출됨
2. 비동기 작업이 성공하거나 실패한 뒤에 `.then()` 메서드를 이용하여 추가한 경우에도 1번과 똑같이 동작
3. `.then()` 을 여러번 사용하여 여러개의 callback 함수를 추가할 수 있음 (Chaining)
   - 각각의 callback은 주어진 순서대로 하나하나 실행하게 된다
   - Chaining은 Promise의 가장 뛰어난 장점

## Axios and Promise Practice (Cat API and Dog API)

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

## AJAX

---

### AJAX란?

- **비동기 통신을 이용하면 화면 전체를 새로고침하지 않아도 서버로 요청을 보내고, 데이터를 받아 화면의 일부분만 업데이트 가능**
- 이러한 “비동기 통신 웹 개발 기술”을 Asynchronous Javascript And XML(AJAX)라 한다
- AJAX의 특징
  1. **페이지 새로고침없이** 서버에 요청
  2. 서버로부터 **응답(데이터)을 받아** 작업을 수행
- 이러한 비동기 웹 통신을 위한 라이브러리 중 하나가 Axios

### 비동기(Async) 적용하기

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

### 왜 비동기(Asynchronous) 방식이 필요할까

- “human-centered design with UX”
- “인간 중심으로 설계된 사용자 경험”
- 실제 AJAX라는 용어를 처음 논문에서 사용한 Jesse James Garrett이 AJAX를 소개하며 강조한 한 마디

## 팔로우 (follow) 비동기 적용

---

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

## Follows and Likes 비동기 적용 최종 코드

---

### Follows

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

### Likes

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

## Follow and Like 추가 구현 코드

---

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
