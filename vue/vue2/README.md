# Vue 2

- [Vue CDN and Directives](#vue-cdn-and-directives)
- [Vue CLI and Components](#vue-cli-and-components)
- [Vue Lifecycle Hooks and Vuex](#vue-lifecycle-hooks-and-vuex)
- [Vue Router and Navigation Guard](#vue-router-and-navigation-guard)
- [Vue with DRF](#vue-with-drf)

---

# Vue CDN and Directives

- Vue Intro with CDN
- Why Vue
- Vue Instance
- Basic of Syntax
- Vue Advanced

---

# Vue CDN

## 사전 준비 사항

- VSCode Vetur extension 설치
  - 문법 하이라이팅, 자동완성, 디버깅 기능 제공
- Chrome Vue devtools extension 설치 및 설정
  - 크롬 브라우저 개발자 도구에서 vue 디버깅 기능 제공
- Vue CDN
  - [https://v2.vuejs.org/](https://v2.vuejs.org/)
    - Getting Started
      - Installation
        - Development version CDN 복사

<img width="751" alt="vue1" src="https://user-images.githubusercontent.com/86648892/212526791-ab2099e3-ab6f-49a5-b810-1fac1e6d8fc5.png">

## Front-End Development

- Front-End(FE) 개발이란?
  - 사용자에게 보여주는 화면 만들기
- Web App(SPA)을 만들 때 사용하는 도구
  - SPA - Single Page Application

## Web App이란?

- 웹 브라우저에서 실행되는 어플리케이션 소프트웨어
- 개발자 도구 > 디바이스 모드
  - 웹 페이지가 그대로 보이는 것이 아닌 디바이스에 설치된 App처럼 보임
  - 웹 페이지가 디바이스에 맞는 적절한 UX, UI로 표현되는 형태

## SPA(Single Page Application)

- Web App과 함께 자주 등장하는 용어 SPA
- 이전까지는 사용자의 요청에 대해 적절한 페이지 별 template을 반환
- SPA는 서버에서 최초 1장의 HTML만 전달받아 모든 요청에 대응하는 방식
  - 어떻게 한 페이지로 모든 요청에 대응할 수 있을까?
  - **_CSR(Client Side Rendering) 방식_**으로 요청을 처리하기 때문
    - SSR(Server Side Rendering)은 Django와 같은 서버에서 렌더링을 해서 넘겨줌

### [참고] SSR(Server Side Rendering)

<img width="746" alt="vue2" src="https://user-images.githubusercontent.com/86648892/212526788-d21f5d1c-861b-4620-a82c-28157e5a8ebb.png">

- Server가 사용자의 요청에 적합한 HTML을 렌더링하여 제공하는 방식
- 전달받은 새 문서를 보여주기 위해 브라우저는 새로고침을 진행

## CSR(Client Side Rendering)

<img width="767" alt="vue3" src="https://user-images.githubusercontent.com/86648892/212526787-36a6b4bd-9201-4410-a312-24ca2aeddb57.png">

- 최초 한 장의 HTML을 받아오는 것은 동일
  - 단, server로부터 최초로 받아오는 문서는 빈 html 문서
- 각 요청에 대한 대응을 JavaScript를 사용하여 필요한 부분만 다시 렌더링
  1. 필요한 페이지를 서버에 **AJAX**로 요청
  2. 서버는 화면을 그리기 위해 필요한 데이터를 **JSON** 방식으로 전달
  3. JSON 데이터를 JavaScript로 처리 및 DOM 트리에 반영 (렌더링)

### WHY CSR?

1. 모든 HTML 페이지를 서버로부터 받아서 표시하지 않아도 됨
   - 클라이언트-서버 간 통신, 즉 트래픽이 감소
     - 트래픽이 감소한다는 것은 곧 응답 속도가 빨라진다는 것
2. 매번 새 문서를 받아 새로고침하는 것이 아니라 필요한 부분만 고쳐나가므로 각 요청이 끊김없이 진행
   - SNS에서 추천을 누를 때마다 첫 페이지로 돌아간다?
     - 끔찍한 APP!
   - 요청이 자연스럽게 진행이 된다
     - UX 향상
3. BE와 FE의 작업 영역을 명확히 분리할 수 있음
   - 각자 맡은 역할을 명확히 분리한다
     - 협업이 용이해진다

### CSR의 단점?

- 첫 구동 시 필요한 데이터가 많으면 많을수록 최초 작동 시작까지 오랜 시간이 소요
  - Naver, Netflix, Disney+ 등 모바일에 설치된 Web-App을 실행하게 되면 잠깐의 로딩 시간이 필요
- 검색 엔진 최적화(SEO, Search Engine Optimization)가 어려움
  - 서버가 제공하는 것은 텅 빈 HTML
  - 내용을 채우는 것은 AJAX 요청으로 얻은 JSON 데이터로 클라이언트(브라우저)가 진행
- 대체적으로 HTML에 작성된 내용을 기반으로 하는 검색 엔진에 빈 HTML을 공유하는 SPA 서비스가 노출되기는 어려움

### [참고] SEO(Search Engine Optimization)

- google, bing과 같은 검색 엔진 등에 내 서비스나 제품 등이 효율적으로 검색 엔진에 노출되도록 개선하는 과정을 일컫는 작업
- 검색
  - 각 사이트가 운용하는 검색 엔진에 의해 이루어지는 작업
    - 검색 엔진
      - 웹 상에 존재하는 가능한 모든 정보들을 긁어 모으는 방식으로 동작
        - 정보의 대상은 주로 HTML에 작성된 내용
        - JavaScript가 실행된 이후의 결과를 확인하는 과정이 없음
- 최근에는 SPA, 즉 CSR로 구성된 서비스의 비중이 증가
  - SPA 서비스도 검색 대상으로 넓기 위해 JS를 지원하는 방식으로 발전
  - 단, 단순 HTML만을 분석하는 것보다 몇 배의 리소스가 필요한 작업이기에 여전히 CSR의 검색 엔진 최적화 문제가 모두 해결된 것은 아님

### CSR vs SSR

- CSR과 SSR은 흑과 백이 아님
  - 내 서비스에 적합한 렌더링 방식을 적절하게 활용할 수 있어야 함
- SPA 서비스에서도 SSR을 지원하는 Framework도 발전하고 있음 (SPA의 단점을 보완)
  - Vue의 Nuxt.js
  - React의 Next.js
  - Angular Universal 등

## 여러가지 Front-End Framework

<img width="730" alt="vue4" src="https://user-images.githubusercontent.com/86648892/212526786-7c43bbd4-e324-43d2-a2c3-1c1a537ef9fb.png">

- Front-End Framework
  - HTML + CSS + JS를 더 편하게 작업하기위한 툴
    - React, Angular, Svelte, Vue 등
- 더 쉽게 개발하기 위해 사용하는 것
- Github은 이러한 Front-End Framework를 사용하지 않음
  - FE 프레임워크 시장의 변화가 빠르기 때문이라 답변
- 대부분의 기업에서는 생산성과 협업을 위해 Framework를 사용해서 개발

---

# Why Vue?

- 타 프레임워크에 비해 입문자가 시작하기에 좋은 프레임워크
- 구글의 Angular 개발자 출신 Evan You
  - Angular보다 가볍고, 간편하게 사용할 수 있는 프레임워크를 만들기 위해 퇴사
  - 2014년 Vue 발표
- Vue의 구조는 매우 직관적임

## 코드 비교

### Vanila JS

```jsx
<body>
  <div id="app">
    <p id="name">name : </p>
    <input id="inputName" type="text">
  </div>

  <script>
    const name = document.querySelector('#name')
    const input = document.querySelector('#inputName')
    input.addEventListener('input', function (e) {
      name.innerText = 'name : ' + e.target.value
    })
  </script>
</body>
```

### Vue CDN

```jsx
<body>
  <!-- 1) input type의 값이 2) data: message: 값을 변경하고 이 값이 3) p 태그의  {{ message }} 값을 변경 -->
  <!-- View -->
  <div id="app">
    <p id="name">name : {{ message }}</p>
    <input id="inputName" type="text" v-model="message">
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    // CODE HERE
    // View Model
    const app = new Vue({
      el: '#app',
      data: {
        // Model
        message: '',
      }
    })
  </script>
</body>
```

- `<script *src*="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>`
  - Vue CDN 가져오기
- `<input *id*="inputName" *type*="text" *v-model*="message">`
  - `v-model`
    - input에 값을 입력하면 Vue data와 연동되어 반영됨
      - Vanila JS에서는 모든 요소에 각각 innerText를 바꿔줘야하는 작업이 필요했다면
        - 이제는 해당 data 하나와 연동된 요소들에 데이터 변경 사항이 바로 반영됨

### [참고] Vue 2 and Vue 3

- 2022년 2월부터 Vue 프레임워크의 기본 버전에 3으로 전환
- 대체적인 설정들이 Vue 3을 기본으로 적용되어있음
  - 공식문서, CDN, npm 등
- 그러나 여전히 Vue 2가 많이 사용됨
  - legacy code
  - 사용된 기간이 긴 만큼 상대적으로 많은 문서의 양과 참고자료 등
  - 안정성의 측면에서는 아직 Vue 2가 우세한 편

---

# Vue Instance

## MVVM Pattern

<img width="738" alt="vue5" src="https://user-images.githubusercontent.com/86648892/212526785-cc3ac28c-cb73-45dc-b4c0-ba3b182285ac.png">

- 소프트웨어 아키텍쳐 패턴의 일종
- 마크업 언어로 구현하는 그래픽 사용자 인터페이스(**_view_**)의 개발을
  - Back-End(**_model_**)로부터 분리시켜
    - view가 어느 특정한 모델 플랫폼에 종속되지 않도록 함
- View는 우리 눈에 보이는 부분 (DOM)
  - Model은 실제 데이터 (JSON)
    - View Model (Vue)
      - View를 위한 Model
      - View와 연결(binding)되어 Action을 주고받음
      - Model이 변경되면 View Model도 변경되고 바인딩된 View도 변경됨
      - View에서 사용자가 데이터를 변경하면 View Model의 데이터가 변경되고 바인딩된 다른 View도 변경됨
- 즉, Model과 View 사이에서
  - DOM으로부터 이벤트를 듣고
    - Directive를 사용하여 DOM을 조작

## MVVM Pattern 정리

- ViewModel의 핵심은 **_변경사항_**에 대한 **_반응형_**이라는 것
- MVC 패턴에서 Controller를 제외하고 View Model을 넣은 패턴
- View는 Model을 모르고, Model도 View를 모른다
  - DOM은 Data를 모르고, Data도 DOM을 모른다
    - 독립성 증가 및 적은 의존성
- View에서 데이터를 변경하면 View Model의 데이터가 변경되고, 연관된 다른 View도 함께 변경된다

## Vue Instance

```jsx
<body>
  <div id="app">
    {{ message }}
  </div>

  <div>
    {{ message }}
  </div>

  <!-- Vue CDN -->
  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    // CODE HERE
    // 1. Vue instance constructor
    // const vm = new Vue()
    // console.log(vm)

    // 2. el
    const app = new Vue({
      el: '#app',   // element, VM과 HTML의 DOM을 연결해주는 속성 // id가 app인 element를 연결(마운트)하겠다는 뜻

      // 3. data (MVVM의 Model을 담당)
      data: {
        message: 'Hello, Vue!'
      },

      // 4. methods
      methods: {
        print: function () {
          // console.log(this.$data.message)  // 구조상으로는 이렇게 접근하는게 정석 (Vue에 정해진 속성값들에 접근할 때는 구분을 위해 $가 붙음)
          // 편의상 $data는 shorthand로 빼고 접근 가능
          console.log(this.message) // this는 메서드를 호출하는 객체(new Vue()에 해당)
        },
        // this.message의 값을 바꾸는 메서드
        bye: function () {
          this.message = 'Bye, Vue!'
        },
      // arrow function으로 선언하면 this가 app 객체의 상위 스코프인 window를 가리키게 됨
      // 그러므로 호출은 가능하나 Vue 객체의 data를 변경하지는 못함
        // 4-1. arrow function
        arrowBye: () => {
          this.message = 'Arrow Function?'  // window 객체에 message라는 전역 변수를 만든 것이 됨
          console.log(this)
        }
      }
    })
    console.log(app)
  </script>
</body>
```

<img width="668" alt="vue6" src="https://user-images.githubusercontent.com/86648892/212526782-9fcdee9e-26ea-4da0-bbd7-3282ebcd20e6.png">

- Vue Instance는 1개의 객체
  - 아주 많은 속성과 메서드를 이미 가지고 있고
    - 이러한 기능들을 사용하는 것
- `const app = new Vue({})`
  - Vue Instance 생성
- `el`
  - element
  - Vue Instance와 DOM을 mount(연결)하는 옵션
    - **_View와 Model을 연결하는 역할_**
    - HTML **_id 혹은 class_**와 마운트 가능
  - **_Vue Instance와 연결되지 않은 DOM 외부는 Vue의 영향을 받지 않음_**
    - Vue 속성 및 메서드 사용 불가
- `data`
  - Vue Instance의 **_데이터 객체_** 혹은 **_인스턴스 속성_**
  - 데이터 객체는 반드시 기본 객체 **_{ }(Object)_**이어야 함
  - 객체 내부의 아이템들은 value로 모든 타입의 객체를 가질 수 있음
  - 정의된 속성은 **_interpolation {{ }}_**을 통해 view에 렌더링 가능함
  - data의 값들은 `this.dataName` 형태로 접근 가능
- `{{  }}`
  - 선언적 렌더링
  - Vue data를 화면에 렌더링
- `methods`
  - Vue Instance의 method들을 정의하는 곳
  - 메서드를 정의할 때 Arrow Function 사용하지 말 것
    - Arrow Function의 this는 함수가 선언될 때 상위 스코프를 가리킴
      - 즉, this가 Vue 객체의 상위 객체인 window를 가리킴
        - 호출은 문제없이 가능하나 this로 Vue의 data를 변경하지 못함

### [참고] JS constructor (생성자 함수)

- 함수 이름은 반드시 대문자로 시작
- 생성자 함수를 사용할 때는 반드시 `new` 연산자를 사용

```jsx
const member = {
  name: "aiden",
  age: 22,
  sId: 2022311491,
}

const member2 = {
  name: "haley",
  age: 20,
  sId: 2022311492,
}

function Member(name, age, sId) {
  this.name = name
  this.age = age
  this.sId = sId
}

const member3 = new Member("isaac", 21, 2022654321)
```

---

# Basic of Syntax

## Template Syntax

- Vue 2 Guide > Template Syntax 참고
- **_렌더링된 DOM_**을 기본 Vue Instance의 data에 **_선언적으로 바인딩_**할 수 있는 **_HTML 기반 template syntax_**를 사용
  - 렌더링된 DOM
    - 브라우저에 의해 보기 좋게 그려질 HTML 코드
  - HTML 기반 template syntax
    - HTML 코드에 직접 작성할 수 있는 문법 제공
  - 선언적으로 바인딩
    - Vue Instance와 DOM을 연결

```jsx
<body>
  <!-- 1. Text interpolation -->
  <div id="app">
    <p>메시지: {{ msg }}</p>
    <p>HTML 메시지 : {{ rawHTML }}</p>
    <p>HTML 메시지 : <span v-html="rawHTML"></span></p>
    <!-- JS 표현식 자체로 가공하는 것 역시 가능 -->
    <p>{{ msg.split('').reverse().join('') }}</p>
  </div>

  <hr>

  <!-- 2. v-text && v-html -->
  <!-- Directives -->
  <div id="app2">
    <!-- 2-1. v-text & {{}} -->
    <p v-text="message"></p>
    <!-- 같음 (Interpolation 사용)-->
    <p>{{ message }}</p>

    <!-- 2-2. v-html -->
    <p v-html="html"></p>
  </div>

  <hr>

  <!-- 3. v-show && v-if -->
  <!-- v-show는 표현식에 작성된 boolean 값에 따라 해당 태그를 렌더링할지 안할지 결정함, false일시 none으로 DOM에는 존재 -->
  <!-- v-if는 v-show와 비슷하나 false일시 DOM에 존재하지 않게됨 -->
  <div id="app3">
    <p v-show="isActive">보이니? 안보이니?</p>
    <p v-if="isActive">안보이니? 보이니?</p>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    // 1. Text interpolation
    const app = new Vue({
      el: '#app',
      data: {
        msg: 'Text interpolation',
        rawHTML: '<span style="color:red"> 빨간 글씨</span>'
      }
    })

    // 2. v-text && v-html
    const app2 = new Vue({
      el: '#app2',
      data: {
        message: 'Hello!',
        html: '<a href="https://www.google.com">GOOGLE</a>'
      }
    })

    // 3. v-show && v-if
    const app3 = new Vue({
      el: '#app3',
      data: {
        isActive: false
      }
    })
  </script>
</body>
```

<img width="1919" alt="vue7" src="https://user-images.githubusercontent.com/86648892/212526781-2a0832c4-76c2-4592-84d3-6d3e29e7de99.png">

- V-Directive를 통해 컨트롤하거나
- 직접 JS 표현식도 작성 가능

  ```jsx
  <div id="app">
  	<p>{{ msg.split('').reverse().join('') }}</p>
  </div>

  const app = new Vue({
  	el: '#app',
  	data: {
  	  msg: 'Text interpolation',
  	}
  })
  ```

- `v-text`
  - Text Interpolation과 같음
  - `<p *v-text*="message"></p>`
  - `<p>{{ message }}</p>`
- `v-html`
  - HTML 표현식을 연동
  ```jsx
  const app2 = new Vue({
    el: "#app2",
    data: {
      message: "Hello!",
      html: '<a href="https://www.google.com">GOOGLE</a>',
    },
  })
  ```
  - `<p *v-html*="html"></p>`

## Directives

- v-접두사가 있는 특수 속성
  - 여기에는 변수 값을 할당할 수 있음
    - 여기에 들어가는 값은 단순한 문자열이 아니라 JS 표현식이 들어감
      - 역할은 **_표현식의 값_**이 **_변경_**될 때 **_반응적_**으로 DOM에 어떠한 일을 할지 결정함

![vue8](https://user-images.githubusercontent.com/86648892/212526780-9bb4c9fc-e08d-4e55-8f91-edb97c320486.png)

- Name
  - v-directive의 종류
- Argument
  - 인자
- Modifiers
  - 특수 접미사
    - directive에 대한 추가적인 속성값
- Value
  - 자바스크립트의 값

### v-text directive

- Text Interpolation과 함께 가장 기본적인 바인딩 방법
- `{{ }}` 과 동일한 역할

### v-html directive

- HTML 표현식을 연동할 수 있음
- 단, 사용자가 입력하거나 제공하는 컨텐츠에는 절대 사용 금지
  - XSS 공격 참고

### v-show directive

- 표현식에 작성된 값에 따라 element를 보여줄 것인지 결정
  - boolean 값이 변경될 때마다 반응
  - 대상 element의 display 속성을 **_기본 속성과 none_**으로 toggle
  - **_요소 자체는 항상 DOM에 렌더링됨_**
    - 화면에서만 사라졌을 뿐 (display 속성이 변경되었을 뿐)

### v-if directive

- v-show와는 달리 boolean 값이 false일 경우 DOM에서 사라짐
- `v-if v-else-if v-else` 형태로 사용

### v-show and v-if

- `v-show`
  - Expensive initial load, cheap toggle
  - 표현식 결과와 관계없이 렌더링되므로 초기 렌더링에 필요한 비용은 v-if보다 높을 수 있음
  - display 속성 변경으로 표현 여부를 판단하므로 렌더링 후 toggle 비용은 적음
- `v-if`
  - Cheap initial load, expensive toggle
  - 표현식 결과가 false인 경우 렌더링조차 되지 않으므로 초기 렌더링 비용은 v-show보다 낮을 수 있음
  - 단, 표현식 값이 자주 변경되는 경우 잦은 재 렌더링으로 비용이 증가할 수 있음

### v-for

```jsx
<body>
  <!-- 3. v-for -->
  <!-- iterable에 적용 가능 -->
  <!-- 1-1) 문자열 출력 -->
  <div id="app">
    <h2>String</h2>
    <div v-for="char in myStr">
      {{ char }}
    </div>
    <!-- 1-2) 문자열 인덱스까지 출력 -->
    <div v-for="(char, index) in myStr" :key="index">
      <p>{{ index }}번째 문자열 {{ char }}</p>
    </div>

    <!-- 2) 배열 출력 -->
    <h2>Array</h2>
    <div v-for="(item, index) in myArr" :key="`zac-${index}`">
      <p>{{ index }}번째 아이템 {{ item }}</p>
    </div>

    <div v-for="(item, index) in myArr2" :key="`arry-${index}`">
      <p>{{ index }}번째 아이템</p>
      <p>{{ item.name }}</p>
    </div>

    <!-- 3) 객체 출력 -->
    <h2>Object</h2>
    <div v-for="value in myObj">
      <p>{{ value }}</p>
    </div>

    <div v-for="(value, key) in myObj"  :key="key">
      <p>{{ key }} : {{ value }}</p>
    </div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        // 1. String
        myStr: 'Hello, World!',

        // 2-1. Array
        myArr: ['python', 'django', 'vue.js'],

        // 2-2. Array with Object
        myArr2: [
          { id: 1, name: 'python', completed: true},
          { id: 2, name: 'django', completed: true},
          { id: 3, name: 'vue.js', completed: false},
        ],

        // 3. Object
        myObj: {
          name: 'harry',
          age: 27
        },
      }
    })
  </script>
</body>
```

- `for..in..` 형식으로 작성
- 반복한 데이터 타입에 모두 사용 가능

  - 문자열
  - 배열

    - **_특수 속성 key_**
      - 반복이 돌고 있는 주체들이 변경되었을 때 그 값을 보장하기 위해 내부적으로 쓰이는 값
        - 우리가 무엇인가를 하기 위함이 아니라 각각의 v-for가 서로에게 영향을 받지 않고 내부적으로 올바르게 동작하게 하기 위함
      - 다른 v-for와 key가 중복되어서는 안됨
      - Vue가 내부적으로 DOM의 변경사항을 추적할 때 key가 잡혀있으면 더 빠름
        - key를 통해 각각의 element를 구분하기 때문
          <img width="570" alt="vue9" src="https://user-images.githubusercontent.com/86648892/212526779-e42c52d8-03a9-4690-a292-16dd0c610392.png">

  - 객체
    - 순회 시 value가 할당되어 출력
    - 2번째 변수 할당 시 key 출력 가능

### v-on and v-bind directive

```jsx
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .red-text {
      color: red;
    }
    .border-black {
			border: solid 1px black;
		}

    .dark-mode {
      color: white;
      background-color: black
    }

    .white-mode {
      color: black;
      background-color: white;
    }
  </style>
</head>
<body>
  <!-- v-on direcitve: event listener의 역할 -->
  <!-- 어떠한 이벤트가 발생하면(on), 뒤의 JS 연산식을 실행하겠다는 것 -->
  <div id="app">
    <button v-on:click="number++">increase Number</button>
    <p>{{ number }}</p>

    <!-- 메서드 호출 가능 -->
    <button v-on:click="toggleActive">toggle isActive</button>
    <p>{{ isActive }}</p>

    <!-- v-on shortcut 제공 -->
    <!-- 메서드에 인자 전달도 가능 -->
    <button @click="checkActive(isActive)">check isActive</button>
  </div>

  <hr>

    <!-- v-bind directive -->
    <!-- 변수에 바인딩 -->
  <div id="app2">
    <a v-bind:href="url">Go To GOOGLE</a>

    <!-- 클래스 변수명을 넘겨줄 수 있음 -->
    <p v-bind:class="redTextClass">빨간 글씨</p>
    <!-- 객체로 넣어 클래스를 true, false로 넣었다 뺐다 할 수 있음 -->
    <p v-bind:class="{ 'red-text': true }">빨간 글씨</p>
    <!-- 여러 개의 스타일 클래스는 배열로 넣을 수 있음 -->
    <p v-bind:class="[redTextClass, borderBlack]">빨간 글씨, 검은 테두리</p>

    <p :class="theme">상황에 따른 활성화</p>
    <button @click="darkModeToggle">dark Mode {{ isActive }}</button>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        number: 0,
        isActive: false,
      },
      methods: {
        toggleActive: function () {
          this.isActive = !this.isActive
        },

        checkActive: function (check) {
          console.log(check)
        }
      }
    })

    const app2 = new Vue({
      el: '#app2',
      data: {
        url: 'https://www.google.com/',
        redTextClass: 'red-text',
        borderBlack: 'border-black',
        isActive: true,
        theme: 'dark-mode'
      },
      methods: {
        darkModeToggle() {
          this.isActive = !this.isActive
          if (this.isActive) {
            this.theme = 'dark-mode'
          } else {
            this.theme = 'white-mode'
          }
        }
      }
    })
  </script>
</body>
</html>
```

<img width="1912" alt="vue10" src="https://user-images.githubusercontent.com/86648892/212526778-8bce32e3-e0b1-4ba6-a269-b21848ef1b19.png">

### v-on directive

- HTML 요소가 반응하는 이벤트를 붙여주기 위해 사용하는 것이 v-on
  - method를 통한 data 조작도 가능
  - method에 인자를 넘기는 방법은 일반 함수를 호출할 때와 동일한 방식
  - `:` 을 통해 전달된 인자에 따라 특별한 modifiers(수식어)가 있을 수 있음
    - ex) `v-on:keyup.enter`
    - ex) `v-on:submit.prevent`
- `@` shortcut 제공
  - ex) `<button @click="checkActive(isActive)">`

### v-bind directive

- HTML 속성값에 JS 표현식으로 Vue Data를 연결
  - 조건부 바인딩
    - `{ 'class Name': '조건 표현식' }`
    - 삼항 연산자도 가능
  - 다중 바인딩
    - `['JS 표현식', 'JS 표현식', ...]`
- `:` shortcut 제공
  - ex) `<p :class="theme">`

### v-model directive

```jsx
<body>
  <div id="app">
    <!-- v-on을 통한 바인딩 -->
    <h2>1. Input -> Data</h2>
    <h3>{{ myMessage }}</h3>
    <input @input="onInputChange" type="text">
    <hr>

    <!-- v-model을 통한 양방향 바인딩 -->
    <h2>2. Input <-> Data</h2>
    <h3>{{ myMessage2 }}</h3>
    <input v-model="myMessage2" type="text">
    <hr>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        myMessage: '',
        myMessage2: '',
      },
      methods: {
        onInputChange: function (event) {
          this.myMessage = event.target.value
        },
      }
    })
  </script>
</body>
```

- Vue Instance와 DOM의 **_양방향 바인딩_**
- v-on을 통해 이벤트와 연결하는 것 없이 바로 데이터와 연결해주는 것
  - 즉, 데이터에 직접적으로 연결해주는 것
- 한글과 같이 조합형 문자의 경우 입력기 방식으로 인해 v-model의 실시간 양방향 바인딩 적용이 어려움
  - [https://ko.wikipedia.org/wiki/입력기](https://ko.wikipedia.org/wiki/%EC%9E%85%EB%A0%A5%EA%B8%B0)
  - v-on을 통한 이벤트 바인딩 방식으로 대체

---

# Vue Advanced

## computed

- Vue Instance가 가진 options 중 하나
- computed 객체에 정의한 함수를 페이지가 최초로 렌더링될 때 호출하여 계산
  - 계산 결과가 변하기 전까지 함수를 재호출하는 것이 아닌 계산된 값을 반환
- data 속성의 확장이라 이해하자
  - 어떤 data에 가공이 필요한 경우

## methods and computed

### methods

- 호출될 때마다 함수를 실행
- 같은 결과여도 매번 새롭게 계산

### computed

- 함수의 종속 대상의 변화에 따라 계산 여부가 결정됨
- 종속 대상이 변하지 않으면 항상 저장(캐싱)된 값을 반환

```jsx
<body>
  <div id="app">
    <h1>data_01 : {{ number1 }}</h1>
    <h1>data_02 : {{ number2 }}</h1>
    <hr>
    <h1>add_method : {{ add_method() }}</h1>
    <h1>add_method : {{ add_method() }}</h1>
    <h1>add_method : {{ add_method() }}</h1>
    <hr>
    <h1>add_computed : {{ add_computed }}</h1>
    <h1>add_computed : {{ add_computed }}</h1>
    <h1>add_computed : {{ add_computed }}</h1>
    <hr>
    <button v-on:click="dataChange">Change Data</button>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        number1: 100,
        number2: 100
      },
      computed: {
        add_computed: function () {
          console.log('computed 실행됨!')
          return this.number1 + this.number2
        }
      },
      methods: {
        add_method: function () {
          console.log('method 실행됨!')
          return this.number1 + this.number2
        },
        dataChange: function () {
          this.number1 = 200
          this.number2 = 300
        }
      }
    })
  </script>
</body>
```

<img width="1917" alt="vue11" src="https://user-images.githubusercontent.com/86648892/212526777-f1dfb95c-307a-460e-8f68-820b35b97f6b.png">

### computed는 class나 id에 바인딩하여 상황에 따라 변경하고싶을 때 자주 사용

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <style>
      .errorColor {
        color: red;
      }
    </style>
  </head>
  <body>
    <div id="app">
      <h3 :class="errorText">ERROR</h3>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
    <script>
      const app = new Vue({
        el: "#app",
        data: {
          isError: false,
        },
        computed: {
          errorText() {
            return this.isError ? "errorColor" : null
          },
        },
      })
    </script>
  </body>
</html>
```

## watch

- 감시자
  - 특정 데이터의 변화를 감지하는 기능
    - 감시하고 있는 대상이 변경되었을 때 호출됨
      - 첫번째 인자는 현재값, 두번째 인자는 과거값
  - 실행하고자 하는 메서드가 있다면 handler라는 키 값에 문자열 형태로 할당
  - 배열이나 객체를 감시하고 있는 경우
    - `deep: true` 라는 옵션이 필요
      - 배열이나 객체는 데이터가 한 겹 더 안에 있기 때문
- 어떤 데이터가 변경되었을 때
  - 데이터의 가공된 값이 필요하다면
    - computed
  - 단순 값의 가공이 아닌 더 무거운 작업이나 로직이 필요한 경우
    - watch

```jsx
<body>
  <div id="app">
    <h3>Increase number</h3>
    <p>{{ number }}</p>
    <button @click="number++">+</button>
    <hr>

    <h3>Change name</h3>
    <p>{{ name }}</p>
    <input type="text" v-model="name">
    <hr>

    <h3>push myObj</h3>
    <p>{{ myObj }}</p>
    <button @click="itemChange">change Item</button>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        number: 0,
        name: '',
        myObj: {completed: true}
      },
      methods: {
        nameChange: function () {
          console.log('name is changed')
        },

        itemChange: function () {
          this.myObj.completed = !this.myObj.completed
        }
      },
      watch: {
        number: function (val, oldVal) {
          console.log(val, oldVal)
        },

        name: {
          handler: 'nameChange'
        },

        myObj: {
          handler: function (val) {
            console.log(val)
          },
          deep: true
        },
      }
    })
  </script>
</body>
```

<img width="1913" alt="vue12" src="https://user-images.githubusercontent.com/86648892/212526776-0a0ab734-fae3-4af8-b2a0-d64b6f6a9267.png">

## filters

- 텍스트 형식화를 적용할 수 있는 필터
- interpolation 혹은 v-bind를 이용할 때 사용 가능
- JS 표현식 마지막에 `|` (pipe)와 함께 추가되어야 함
- chaining 가능
  - chaining 순서대로 동작

```jsx
<body>
  <div id="app">
    <p>{{ numbers | getOddNums | getUnderTenNums }}</p>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
      },
      filters: {
        // nums 파라미터에 numbers 배열이 들어가면서 동작
        getOddNums: function (nums) {
          const oddNums = nums.filter((num) => {
            return num % 2
          })
          return oddNums
        },

        getUnderTenNums: function (nums) {
          const underTen = nums.filter((num) => {
            return num < 10
          })
          return underTen
        }
      }
    })
  </script>
</body>
```

---

# Vue Style Guide

- [https://v2.vuejs.org/v2/style-guide/](https://v2.vuejs.org/v2/style-guide/)
- v-for 사용 시 key 사용해주기
- v-for를 사용한 element에 절대 v-if를 사용하지 말기

```html
<body>
  <div id="app">
    <!-- 1. 목록의 항목을 필터링할 때 -->
    <!-- bad 1 -->
    <ul>
      <li v-for="user in users" v-if="user.isActive" :key="user.id">
        {{ user.name }}
      </li>
    </ul>

    <!-- good 1 : computed 속성을 대신 반복하여 해결 -->
    <ul>
      <li v-for="user in activeUsers" :key="user.id">{{ user.name }}</li>
    </ul>

    <!-- 2. 숨김 목록의 렌더링을 피할 때 -->
    <!-- bad 2 -->
    <ul>
      <li v-for="user in users" v-if="shouldShowUsers" :key="user.id">
        {{ user.name }}
      </li>
    </ul>

    <!-- good 2 : v-if를 컨테이너 엘리먼트로 옮기기 -->
    <ul v-if="shouldShowUsers">
      <li v-for="user in users" :key="user.id">{{ user.name }}</li>
    </ul>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: "#app",
      data: {
        users: [
          { id: 1, name: "adam", isActive: false },
          { id: 2, name: "barry", isActive: true },
          { id: 3, name: "cale", isActive: false },
        ],
        shouldShowUsers: true,
      },
      computed: {
        activeUsers: function () {
          return this.users.filter((user) => {
            return user.isActive
          })
        },
      },
    })
  </script>
</body>
```

---

# Vue CDN Practice 1

## Lodash

- [https://lodash.com/docs/4.17.15#random](https://lodash.com/docs/4.17.15#random)
- [https://lodash.com/docs/4.17.15#range](https://lodash.com/docs/4.17.15#range)
- [https://lodash.com/docs/4.17.15#sampleSize](https://lodash.com/docs/4.17.15#sampleSize)

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
  <div id="app">
    <h2>LUNCHBOX</h2>
    <button @click="pickOne">Pick One</button>
    <p>{{ choice }}</p>

    <hr>

    <h2>LOTTO</h2>
    <button @click="getLuckyNumbers">Get Lucky Numbers</button>
    <p v-if="luckyNumbers.length">{{ luckyNumbers }}</p>
  </div>

  <!-- lodash cdn -->
  <script src="https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"></script>
  <!-- vue2 cdn -->
  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        menus: ['국밥', '편백찜', '가락국수', '냉면', '햄버거', '팥죽', '곰탕', '초밥', '설렁탕', '간짜장', '짬뽕'],
        choice: '',
        luckyNumbers: [],
      },
      methods: {
        pickOne: function() {
          const randomIndex = _.random(this.menus.length-1)
          this.choice = this.menus[randomIndex]
        },
        getLuckyNumbers: function() {
          const numbers = _.range(1, 45)
          this.luckyNumbers = _.sampleSize(numbers, 6)
        }
      }
    })
  </script>
</body>
</html>
```

---

# Vue CDN Practice 2

- [https://wormwlrm.github.io/2018/12/29/Understanding-Vue-Lifecycle-hooks.html](https://wormwlrm.github.io/2018/12/29/Understanding-Vue-Lifecycle-hooks.html)
- [https://wormwlrm.github.io/2018/12/29/Understanding-Vue-Lifecycle-hooks.html](https://wormwlrm.github.io/2018/12/29/Understanding-Vue-Lifecycle-hooks.html)
- [https://hianna.tistory.com/697](https://hianna.tistory.com/697)

```jsx
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Random Cat Image</title>
  <style>
    img {
      width: 500px;
      height: 500px;
    }
  </style>
</head>
<body>
  <!-- View -->
  <div id="app">
    <h1>Cat Image</h1>
    <div v-if="imgSrc">
      <img :src="imgSrc" alt="cat image">
    </div>
    <button @click="getCatImage">Get Cat</button>
  </div>

  <!-- axios -->
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <!-- vue.js -->
  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        imgSrc: null,
      },
      methods: {
        getCatImage: function() {
          const API_URL = "https://api.thecatapi.com/v1/images/search"
          axios({
            method: 'get',
            url: API_URL,
          })
            .then((response) => {
              // console.log(response.data[0].url)
              this.imgSrc = response.data[0].url
            })
        }
      },
      created: function() {       // Vue Life Cycle을 활용하여 Vue 인스턴스가 초기화될 때 API 서버로 요청을 보내 이미지 불러옴
        this.getCatImage()
      },
      updated: function() {
        console.log(this.imgSrc)  // Vue Life Cylce을 활용하여 이미지 리소스가 업데이트될 때 콘솔창에 이미지 리소스 출력
      },
    })
  </script>
</body>
</html>
```

---

# Vue CDN Practice 3

```jsx
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>To-Do List</title>

  <style>
    .completed {
      text-decoration: line-through;
      color: gray;
    }
  </style>
</head>
<body>
  <!-- View -->
  <div id="app">
    <select v-model="status">
      <option value="all">전체</option>
      <option value="inProgress">진행중</option>
      <option value="completed">완료</option>
    </select>
    <input v-model="content" @keyup.enter="addToDo" type="text">
    <button @click="addToDo">+</button>

    <br>

    <ul>
      <li v-for="todo in todoListByStatus" :key="todo.date">
        <input type="checkbox" :checked="todo.completed" @click="toggleToDo(todo)">
        <span :class="{ completed: todo.completed }">{{ todo.content }}</span>
      </li>
    </ul>

    <button @click="deleteCompleted">완료된 할 일 지우기</button>
  </div>

  <!-- vue.js -->
  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    // 세션 간 ToDoList 데이터 보존 위해 localStorage 활용
    const storageKey = "todoListApp"
    const todoStorage = {
      // getItem(key, value)
      load: function() {
        return JSON.parse(localStorage.getItem(storageKey)) || []
      },
      // setItem(key, value)
      save: function(todoList) {
        localStorage.setItem(storageKey, JSON.stringify(todoList))
      }
    }

    // Vue Instance
    const app = new Vue({
      el: '#app',
      data: {
        content: '',
        todoList: todoStorage.load(),
        status: 'all',
      },
      methods: {
        // 할 일 목록에 추가
        addToDo: function() {
          // 추가할 todo 데이터 정의
          const todo = {
            content: this.content,
            completed: false,
            date: new Date().getTime(), // 현재 Unix 타임 기준(.getTime()) Date 객체 생성(new Date())
          }
          // 추가 및 content 초기화
          if (this.content) {           // 한글 입력일 경우 빈 문자열을 content로 담은 todo 객체가 하나 더 생기는 것을 방지
            this.todoList.push(todo)
          }
          this.content = ''
        },
        // 완료 여부 변경
        toggleToDo: function(todo) {
          todo.completed = !todo.completed
        },
        // 완료한 일 삭제 (완료되지 않은 일만 필터링)
        deleteCompleted: function() {
          this.todoList = this.todoList.filter((todo) => !todo.completed)
        },
      },
      computed: {
        todoListByStatus: function() {
          return this.todoList.filter((todo) => {
            if (this.status === 'inProgress') {
              return !todo.completed
            }
            if (this.status === 'completed') {
              return todo.completed
            }
            return true
          })
        },
      },
      watch: {
        todoList: {
          handler: function(todoList) {
            todoStorage.save(todoList)
          },
          deep: true,
        }
      }
    })
  </script>
</body>
</html>
```

---

# Vue CDN Practice 4

```jsx
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>yes or no</title>
</head>
<body>
  <div id="watch-example">
    <p>
      yes / no 질문을 물어보세요:
      <input v-model="question" type="text">
    </p>
    <p>{{ answer }}</p>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    const watchExampleVM = new Vue({
      el: '#watch-example',
      data: {
        question: '',
        answer: '질문을 하기 전까지는 대답할 수 없습니다.'
      },
      methods: {
        getAnswer: function() {
          if (this.question.indexOf('?') === -1) {
            this.answer = '질문에 물음표를 작성해주세요 :)'
            return
          }

          this.answer = '생각중...'
          const vm = this

          axios.get('https://yesno.wtf/api')
            .then(function (response) {
              vm.answer = _.capitalize(response.data.answer)
            })
            .catch(function (error) {
              vm.answer = 'API 요청에 오류가 있습니다. ' + error
            })
        }
      },
      created: function() {
        // _.debounce(func, [wait=0], [options={}])
        // creates a debounced function
        /*
        _.debounce는 lodash가 제공하는 기능으로, 특히 시간이 많이 소요되는 작업을 실행할 수 있는 빈도를 제한
        이 경우에는 yesno.wtf/api에 액세스하는 빈도를 제한하고, 사용자가 ajax 요청을 하기 전에 타이핑을 완전히 마칠 때까지 기다리길 바란다
        _.debounce 함수, 혹은 이와 유사한 _.throttle에 대한 추가 정보는 https://lodash.com/docs#debounce
        */
        this.debouncedGetAnswer = _.debounce(this.getAnswer, 500)
      },
      watch: {
        // 질문이 변경될 때마다 해당 기능 실행
        question: function() {
          this.answer = '입력을 기다리는 중...'
          this.debouncedGetAnswer()
        }
      }
    })
  </script>
</body>
</html>
```

---

# Vue CLI and Components

- Vue CLI
- SFC
- Pass Props & Emit Events

---

# Node.js

- JS는 브라우저를 조작하는 유일한 언어
  - 하지만 브라우저 밖에서는 구동할 수 없었음
- JS를 구동하기 위한 런타임 환경인 Node.js로 인해 브라우저가 아닌 환경에서도 구동할 수 있게됨
  - Chrome V8 엔진을 제공하여 여러 OS 환경에서 실행할 수 있는 환경을 제공
  - 브라우저만 조작 가능했으나, Server-Side-Programming 또한 가능해짐

## NPM (Node Package Manager)

- JS 패키지 관리자
  - Python에 pip가 있다면 Node.js에는 npm
  - pip와 마찬가지로 다양한 의존성 패키지를 관리
- Node.js의 기본 패키지 관리자
- Node.js 설치 시 함께 설치됨

---

# Vue CLI

- Vue 개발을 위한 표준 도구
- 프로젝트의 구성을 도와주는 역할
- 확장 플러그인, GUI, Babel 등 다양한 tool 제공
- 브라우저 환경이 아닌 단독적인 런타임 환경에서 실행

## 설치 및 시작

- 설치
  - `npm install -g @vue/cli`
- 프로젝트 생성
  - vscode terminal에서 진행
  - `vue create vue-cli`
  - version은 Vue 2 선택
- 프로젝트 디렉토리로 이동
  - `cd vue-cli`
- 프로젝트 실행
  - `npm run serve`
- 이미 있는 프로젝트를 받아왔다면?
  - package-lock.json이 있는 위치에서 `npm install`
    - 해당 프로젝트의 package-lock.json에 따라 node_modules를 설치해줌

## Vue CLI 프로젝트 구조

<img width="796" alt="vue13" src="https://user-images.githubusercontent.com/86648892/212527153-578970e0-68ed-4e39-a04a-7b666d872e0a.png">

## node_modules

- 프로젝트 환경을 담당
- node.js 환경의 여러 의존성 모듈
- python의 venv와 비슷한 역할
  - 따라서 .gitignore에 넣어주어야 하며, Vue 프로젝트를 생성하면 자동으로 추가됨

### node_modules - babel

<img width="1410" alt="vue14" src="https://user-images.githubusercontent.com/86648892/212527151-b5b23636-11fd-41a7-ad2a-d390c2304e0a.png">

- “JavaScript compiler”
- JS ES6+ 코드를 구버전으로 번역 및 변환해주는 도구
- JS의 파편화, 표준화의 영향으로 작성된 코드의 스펙트럼이 매우 다양
  - 최신 문법을 사용해도 브라우저의 버전 별로 동작하지 않는 상황이 발생
  - 버전에 따른 같은 의미의 다른 코드를 작성하는 등의 대응이 필요해졌고, 이러한 문제를 해결하기 위한 도구
  - 원시 코드(최신 버전)를 목적 코드(구 버전)으로 옮기는 번역기가 등장하면서 더이상 코드가 특정 브라우저에서 동작하지 않는 상황에 대해 크게 고민하지 않을 수 있음

### node_modules - webpack

<img width="701" alt="vue15" src="https://user-images.githubusercontent.com/86648892/212527150-f59ad5f5-dc4c-4e59-b9f5-9bfb909cd09e.png">

<img width="317" alt="vue16" src="https://user-images.githubusercontent.com/86648892/212527148-a3169d37-c36b-4be4-858b-15baba9b3767.png">

- “static module bundler”
- 모듈 간의 의존성 문제를 해결하기 위한 도구
- 프로젝트에 필요한 모든 모듈을 매핑하고 내부적으로 종속성 그래프를 빌드함
- Webpack은 모듈 간의 의존성 문제를 해결하기 위해 등장
  - Module 의존성 문제?
    - 모듈의 수가 많아지고 라이브러리 혹은 모듈 간의 의존성(연결성)이 깊어지면서 특정한 곳에서 발생한 문제가 어떤 모듈 간의 문제인지 파악하기 어려움
      - Module?
        - 개발하는 어플리케이션의 크기가 커지고 복잡해지면 파일 하나에 모든 기능을 담기가 어려워짐
        - 따라서 자연스럽게 파일을 여러 개로 분리하여 관리를 하게 되었고, 이 때 분리된 파일 각각이 모듈(module), 즉 js 파일 하나가 하나의 모듈
        - 모듈은 대개 기능 단위로 분리하며, 클래스 하나 혹은 특정한 목적을 가진 복수의 함수로 구성된 라이브러리 하나로 구성됨
        - 여러 모듈 시스템
          - ESM(ECMA Script Module), AMD, CommonJS, UMD
- Bundler
  - 모듈 의존성 문제를 해결해주는 작업이 Bundling
  - Webpack은 다양한 Bundler 중 하나
  - 모듈들을 하나로 묶어주고 묶인 파일은 하나(혹은 여러 개)로 만들어짐
  - Bundling된 결과물은 개별 모듈의 실행 순서에 영향을 받지 않고 동작하게됨
  - snowpack, parcel, rollup.js 등 webpack 이외에도 다양한 모듈 번들러 존재

### Vue CLI는 Babel, Webpack에 대한 초기 설정이 자동으로 되어 있음

### package.json

- 프로젝트의 종속성 목록과 지원되는 브라우저에 대한 구성 옵션을 포함

### package-lock.json

- node_modules에 설치되는 모듈과 관련된 모든 의존성을 설정 및 관리
- 협업 및 배포 환경에서 정확히 동일한 종속성을 설치하도록 보장하는 표현
- 사용할 패키지의 버전을 고정
- 개발 과정 간의 의존성 패키지 충돌 방지
- python의 requirements.txt 역할

### favicon

- 서버를 켰을 때 브라우저 탭에 나오는 아이콘

### `public/index.html`

<img width="384" alt="vue17" src="https://user-images.githubusercontent.com/86648892/212527147-12a715d0-fcae-4ec2-a80c-9b4d7c9b0e41.png">

- Vue 앱의 뼈대가 되는 html 파일
  - CSR
    - 페이지 하나만 받고 클라이언트가 그려나감
      - `<div id=”app”></div>` 부분이 루트 컴포넌트
        - 여기가 Vue와 연결된 것
          - App.Vue가 여기에 렌더링되는 것

## `src/`

- `src/assets`
  - 정적 파일을 저장하는 디렉토리
- `src/components`
  - 하위 컴포넌트들이 위치
- `src/App.vue`
  - 최상위 컴포넌트
  - `public/index.html` 과 연결됨
- `src/main.js`
  - webpack이 빌드를 시작할 때 가장 먼저 불러오는 entry point
  - `public/index.html` 과 `src/App.vue` 를 연결시키는 작업이 이루어지는 곳
  - Vue 전역에서 활용할 모듈을 등록할 수 있는 파일

---

# SFC

## Component

<img width="786" alt="vue18" src="https://user-images.githubusercontent.com/86648892/212527146-44425cbf-3428-4c8e-ba3e-aa45e40c0cde.png">

- UI를 독립적이고 재사용 가능한 조각들로 나눈 것
  - 기능별로 분화한 코드 조각
- CS에서는 다시 사용할 수 있는 범용성을 위해 개발된 소프트웨어 구성 요소를 의미
- 하나의 app을 구성할 때 중첩된 컴포넌트들의 tree로 구성하는 것이 보편적임
  - HTML에서는 body tag를 root node로 하는 tree 구조라면
    - Vue에서는 `src/App.vue` 를 root node로 하는 tree 구조
- 컴포넌트는 유지보수를 쉽게 만들어주며, 재사용성의 측면에서도 매우 강력한 기능을 제공

## component in Vue

- Vue에서의 component
  - 이름이 있는 재사용 가능한 Vue Instance
    - `const app = new Vue()` 에서 app은 하나의 컴포넌트

## SFC (Single File Component)

- 하나의 `.vue` 파일이 하나의 Vue instance이고, 하나의 컴포넌트이다
- Vue Instance를 기능 단위로 작성하는 것이 핵심
- 컴포넌트 기반 개발의 핵심 기능

---

# Vue Component

- 웹을 구성하는 3가지 언어의 코드가 하나의 파일 안에 작성된다
  - template(HTML)
    - HTML의 body 부분
    - 눈으로 보여지는 요소 작성
    - 다른 컴포넌트를 HTML 요소처럼 추가 가능
  - script(JavaScript)
    - JS 코드가 작성되는 곳
    - 컴포넌트 정보, 데이터, 메서드 등 vue 인스턴스를 구성하는 대부분이 작성됨
  - style(CSS)
    - CSS가 작성되며 컴포넌트의 스타일을 담당
- root component는 `App.vue`
- 이 `App.vue`를 `public/index.html` 과 연결
- `public/index.html` 페이지 하나에 계속 그려나가는 것
  - 이것이 SPA

## component 등록

### component 생성

- `src/components/` 안에 생성
- script에 이름 등록
  - name을 등록해줘야 상위 컴포넌트가 인식할 수 있음
- template에 요소 추가
  - template 태그는 단순히 HTML과 관련된 것이라는 영역 표시에 불과
    - 그 안에 최상위 태그를 추가해줘야함
      - 추가해준 태그부터 렌더링됨

### component 등록 3단계

1. 불러오기

   - `import {instance name} from {위치}`
   - import 경로에서 `@` 는 src를 의미
   - 확장자가 .vue이면 생략 가능

   <img width="491" alt="vue19" src="https://user-images.githubusercontent.com/86648892/212527145-25703ce0-3f67-44dd-92a6-5c76e97c59ee.png">

2. 등록하기

<img width="519" alt="vue20" src="https://user-images.githubusercontent.com/86648892/212527143-904f331c-70ba-4420-b19d-6ddecf150252.png">

3. 보여주기

<img width="476" alt="vue21" src="https://user-images.githubusercontent.com/86648892/212527142-0f9989bd-d151-4b63-937a-66710f02a60d.png">

---

# Pass Props & Emit Events

## Data in components

- 동적 웹페이지에서는 데이터가 필요
- 한 페이지에서 여러 컴포넌트들이 데이터를 공유해야함
- 서로 어떻게 데이터를 공유하는가?
  - 필요한 컴포넌트들끼리 데이터를 주고받을까?
    - 데이터를 흐름을 파악하기 힘들다
    - 개발 속도가 저하된다
    - 유지보수 난이도가 증가한다
  - 컴포넌트는 부모-자식 관계를 가지고 있으므로 부모-자식 관계만 데이터를 주고받게 하자
    - 데이터의 흐름 파악이 용이
    - 유지보수가 쉬워짐
    - 부모 → 자식
      - pass props
    - 자식 → 부모
      - emit events

## Pass Props

- [https://v2.vuejs.org/v2/guide/components-props.html#Prop-Validation](https://v2.vuejs.org/v2/guide/components-props.html#Prop-Validation)
- 요소의 속성(property)을 사용하여 데이터 전달
  - `prop-data-name="value"` 형태로 데이터 전달
    - kebab-case로 이름을 지어 전달
      - HTML 속성명은 대소문자를 구분하지 않기 때문
  - 정적인 데이터를 전달하는 경우를 static props라 함
- props는 부모(상위) 컴포넌트 정보를 전달하기 위한 사용자 지정 특성
- 자식(하위) 컴포넌트는 props 옵션을 사용하여 수신하는 props를 명시적으로 선언해야 함
  - 전달받은 props를 type과 함께 명시
  - 받을 때는 전달한 이름을 camelCase로 받음
    - 부모 템플릿(html)에서 kebab-case로 넘긴 변수를 자식의 스크립트(vue)에서 자동으로 camelCase로 변환하여 인식함

### Dynamic Props

<img width="768" alt="vue22" src="https://user-images.githubusercontent.com/86648892/212527141-b5560792-6d75-4cf0-90ce-7333ddd2399d.png">

<img width="787" alt="vue23" src="https://user-images.githubusercontent.com/86648892/212527140-fd235403-454c-4153-b376-66ae87b6b888.png">

- v-bind로 묶여있는 `""` 안의 구문은 JS의 구문
  - `<SomeComponent num-props="1"/>`
    - static props로 string으로서의 “1”을 전달
  - `<SomeComponent :num-props="1"/>`
    - dynamic props로 숫자로서의 1을 전달

### 컴포넌트의 data 함수

- 각 vue 인스턴스는 같은 data 객체를 공유하므로 새로운 data 객체를 반환(return)하여 사용해야 한다
- [https://v2.vuejs.org/v2/guide/components.html#data-Must-Be-a-Function](https://v2.vuejs.org/v2/guide/components.html#data-Must-Be-a-Function)

### 단방향 데이터 흐름

- 모든 props는 부모에서 자식으로
  - 즉, 아래로 단방향 바인딩을 형성
- 부모 속성이 업데이트되면 자식으로 흐르지만 반대 방향은 아님
  - 부모 컴포넌트가 업데이트될 때마다 자식 컴포넌트의 모든 prop들이 최신값으로 새로고침됨
- 목적
  - 하위 컴포넌트가 실수로 상위 컴포넌트 상태를 변경하여 앱의 데이터 흐름을 이해하기 힘들게 만드는 것을 방지
  - 하위 컴포넌트에서 prop을 변경하려고 시도해서는 안되며 그렇게 하면 Vue는 콘솔에서 경고를 출력함

## Emit Event

- 자식 컴포넌트에서 부모 컴포넌트로 데이터를 전달할 때는 이벤트를 발생시킴
- 이벤트에 담아서 간접적으로 부모가 청취할 수 있도록 하는 방식
  1. 데이터를 이벤트 리스너의 콜백함수의 인자로 전달
  2. 상위 컴포넌트는 해당 이벤트를 통해 데이터를 받음

### `$emit`

- `$emit` 메서드를 통해 부모 컴포넌트에 이벤트를 발생
  - `$emit('event-name')` 형식으로 사용하며 부모 컴포넌트에 event-name이라는 이벤트가 발생했다는 것을 알림
  - 마치 사용자가 마우스 클릭을 하면 click 이벤트가 발생하는 것처럼 `$emit('event-name)` 가 실행되면 event-name 이벤트가 발생하는 것
- `$`
  - JS는 변수에 `_`, `$` 두 개의 특수문자를 사용 가능
    - 기존에 사용하던 변수, 메서드들과 겹치지 않게 하기 위해 Vue는 `$emit` 를 이벤트 전달을 위한 방식으로 채택

<img width="879" alt="vue24" src="https://user-images.githubusercontent.com/86648892/212527138-a6c4784e-3dd7-4809-9afc-291440f5ce30.png">

<img width="872" alt="vue25" src="https://user-images.githubusercontent.com/86648892/212527137-ce290e31-6ce2-48d5-88ab-42ae9d69bee4.png">

<img width="876" alt="vue26" src="https://user-images.githubusercontent.com/86648892/212527136-f407d61b-d22b-46a5-8b18-7b8444c499f0.png">

### Emit Event 흐름

1. 자식 컴포넌트에 있는 버튼 클릭 이벤트를 청취하여 연결된 핸들러 함수(ChildToParent) 호출
2. 호출된 함수에서 `$emit` 을 통해 부모 컴포넌트에 이벤트(child-to-parent)를 발생
   - 이벤트에 데이터(child data)를 함께 전달
3. 부모 컴포넌트는 자식 컴포넌트의 이벤트(child-to-parent)를 청취하여 연결된 핸들러 함수(parentGetEvent)를 호출
   - 함수의 인자로 전달된 데이터(child data)가 포함되어 있음
4. 호출된 함수에서 `console.log` 실행

### Emit with Dynamic Data

- pass props와 마찬가지로 동적인 데이터도 전달 가능

<img width="858" alt="vue27" src="https://user-images.githubusercontent.com/86648892/212527135-c140048b-5892-4cd6-835e-80091a16fd34.png">

<img width="869" alt="vue28" src="https://user-images.githubusercontent.com/86648892/212527133-ded67077-1376-40ec-a671-c6949b236b24.png">

<img width="749" alt="vue29" src="https://user-images.githubusercontent.com/86648892/212527132-8ca04fc3-ec7a-4cd4-afc1-5b5ed53aa22f.png">

### Emit with Dynamic Data 흐름

1. 자식 컴포넌트에 있는 keyup.enter 이벤트를 청취하여 연결된 핸들러 함수(ChildInput) 호출
2. 호출된 함수에서 `$emit` 을 통해 부모 컴포넌트에 이벤트(child-input)를 발생
   - 이벤트에 v-model로 바인딩된 입력받은 데이터를 전달
3. 상위 컴포넌트는 자식 컴포넌트의 이벤트(child-input)를 청취하여 연결된 핸들러 함수(getDynamicData) 호출
   - 함수의 인자로 전달된 데이터가 포함되어있음
4. 호출된 함수에서 `console.log` 실행

## Emit Event 정리

- 자식 컴포넌트에서 부모 컴포넌트로 이벤트를 발생시킴
  - 이벤트에 데이터를 담아 전달 가능
- 부모 컴포넌트에서 자식 컴포넌트의 이벤트를 청취
  - 전달받은 데이터는 이벤트 핸들러 함수의 인자로 사용

## pass props and emit event 컨벤션

- HTML 요소에서 사용할 때는 kebab-case
- JS에서 사용할 때는 camelCase
- props
  - 상위→하위 흐름에서 HTML 요소로 내려줌
    - kebab-case
  - 하위에서 받을 때 JS에서 받음
    - camelCase
- emit
  - emit 이벤트를 발생시키면 HTML 요소가 이벤트를 청취함
    - kebab-case
  - 메서드, 변수명 등은 JS에서 사용함
    - camelCase

---

# Props and Emit Practice

<img width="737" alt="vue30" src="https://user-images.githubusercontent.com/86648892/212527131-15dc26f5-e50f-42b4-909c-8a4a050b1c10.png">

## App.vue

```jsx
<template>
  <div id="app">
    <h1>App</h1>
    <input type="text" @input="onAppInput">
    <!-- <p>appData: {{appInputData}}</p> -->
    <p>parentData: {{ parentInputData }}</p>
    <p>childData: {{ childInputData }}</p>
    <app-parent :app-input-data="appInputData" @on-parent-input="getParentInput" @on-child-input="getChildInput"></app-parent>
  </div>
</template>

<script>
import AppParent from './components/AppParent.vue'

export default {
  name: 'App',
  components: {
    AppParent,
  },
  data: function() {
    return {
      appInputData: null,
      parentInputData: null,
      childInputData: null,
    }
  },
  methods: {
    onAppInput(event) {
      this.appInputData = event.target.value
    },
    getParentInput(parentInputData) {
      this.parentInputData = parentInputData
    },
    getChildInput(childInputData) {
      this.childInputData = childInputData
    },
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
```

## AppParent.vue

```jsx
<template>
  <div>
    <h1>AppParent</h1>
    <input type="text" @input="onParentInput">
    <!-- <p>parentData: {{ parentInputData }}</p> -->
    <p>appData: {{ appInputData }}</p>
    <p>childData: {{ childInputData }}</p>
    <app-child :app-input-data="appInputData" :parent-input-data="parentInputData" @on-child-input="getChildInput"></app-child>
  </div>
</template>

<script>
import AppChild from './AppChild.vue'

export default {
  name: 'AppParent',
  components: {
    AppChild,
  },
  props: {
    appInputData: String,
  },
  data: function() {
    return {
      parentInputData: null,
      childInputData: null,
    }
  },
  methods: {
    onParentInput(event) {
      this.parentInputData = event.target.value
      this.$emit('on-parent-input', this.parentInputData)
    },
    getChildInput(childInputData) {
      this.childInputData = childInputData
      this.$emit('on-child-input', this.childInputData)
    },
  }
}
</script>

<style>
</style>
```

## AppChild.vue

```jsx
<template>
  <div>
    <h1>AppChild</h1>
    <input type="text" @input="onChildInput">
    <p>appData: {{ appInputData }}</p>
    <p>parentData {{ parentInputData }}</p>
    <p>childData: {{ childInputData }}</p>
  </div>
</template>

<script>
export default {
  name: 'AppChild',
  props: {
    appInputData: String,
    parentInputData: String,
  },
  data: function() {
    return {
      childInputData: null,
    }
  },
  methods: {
    onChildInput(event) {
      this.childInputData = event.target.value
      this.$emit('on-child-input', this.childInputData)
    },
  }
}
</script>

<style>
</style>
```

---

# Vue Lifecycle Hooks and Vuex

- Vuex
- Lifecycle Hooks
- Todo with Vuex

---

# Vuex

- 상태 관리(State Management)란 무엇인가?
- Vuex는 무엇이고 왜 필요한가?
- Vuex 기본 문법

# State Management (상태 관리)

- 상태(State)란?
  - 현재에 대한 정보(data)
- Web Application에서의 상태는 어떻게 표현할까?
  - 현재 App이 가지고 있는 Data로 표현할 수 있음
- 우리는 여러 개의 component를 조합해서 하나의 App을 만듬
  - 각 컴포넌트는 독립적이기에 각각의 상태(data)를 가짐
    - 하지만 컴포넌트들은 모여 하나의 App을 구성하기에
      - 여러 개의 component가 같은 상태(data)를 유지할 필요가 있음
        - 상태 관리(State Management)가 필요!

## Pass Props & Emit Event

![vue31](https://user-images.githubusercontent.com/86648892/212527451-26316ece-4c0a-4d84-a9a3-c5bdc375f172.png)

- Props와 Event를 통한 상태 관리
  - 컴포넌트의 깊이가 너무 깊어지면 데이터의 전달이 어려워질 수 있다는 한계
  - 공통의 상태를 유지해야 하는 컴포넌트가 많아지면 데이터 전달 구조가 복잡해지는 한계
    - 중앙 저장소를 만들자!

## Centralized Store

![vue32](https://user-images.githubusercontent.com/86648892/212527450-02e43667-a279-4110-aa53-1950782bd74d.png)

- 중앙 저장소(store)에 데이터를 모아서 상태 관리
- 각 component는 중앙 저장소의 데이터를 사용
- component의 계층에 상관없이 중앙 저장소에 접근해서 데이터를 얻거나 변경할 수 있음
- 중앙 저장소의 데이터가 변경되면 각각의 component는 해당 데이터의 변화에 반응하여 새로 변경된 데이터를 반영함
- 규모가 크거나 컴포넌트 중첩이 깊은 프로젝트의 관리가 매우 편리

## Vuex

- “state management pattern + Library” for vue.js
  - 상태 관리 패턴 + 라이브러리
- 중앙 저장소를 통해 상태 관리를 할 수 있도록 하는 라이브러리
- 데이터가 예측 가능한 방식으로만 변경될 수 있도록 하는 규칙을 설정하며
  - Vue의 반응성을 효율적으로 사용하는 상태 관리 기능을 제공
- Vue의 공식 도구로써 다양한 기능을 제공

---

# Vuex Project

```bash
$ vue create vuex-app // Vue 프로젝트 생성
$ cd vuex-app // 디렉토리 이동
$ vue add vuex // Vue CLI를 통해 vuex plugin 적용
```

![vue33](https://user-images.githubusercontent.com/86648892/212527449-ddcb169e-d8c0-4855-866e-86d0e261aca5.png)

![vue34](https://user-images.githubusercontent.com/86648892/212527448-f08854e4-8a4d-42cb-99a0-7d9a447611ff.png)

## 1. State

- vue 인스턴스의 data에 해당
- 중앙에서 관리하는 모든 상태 정보
- 개별 component는 state에서 데이터를 가져와서 사용
  - 개별 component가 관리하던 data를 중앙 저장소(Vuex Store의 state)에서 관리하게 됨
- state의 데이터가 변화하면 해당 데이터를 사용(공유)하는 component도 자동으로 다시 렌더링
- `$store.state` 로 state 데이터에 접근

![vue35](https://user-images.githubusercontent.com/86648892/212527447-1c2d7738-e744-4e77-b508-d626e572945a.png)

## 2. Mutations

- 실제로 state를 변경하는 유일한 방법
- vue 인스턴스의 methods에 해당하지만 Mutations에서 호출되는 핸들러(handler) 함수는 반드시 동기적이어야 함
  - 비동기 로직으로 mutations를 사용해서 state를 변경하는 경우, state의 변화의 시기를 특정할 수 없기 때문
- 첫번째 인자로 `state` 를 받으며, component 혹은 Actions에서 `commit()` 메서드로 호출됨

## 3. Actions

- mutations의 역할 외의 역할들을 담당
- mutations와 비슷하지만 비동기 작업을 포함할 수 있다는 차이가 있음
- state를 직접 변경하지 않고 `commit()` 메서드로 mutations를 호출해서 state를 변경함
- `context` 객체를 인자로 받으며, 이 객체를 통해 store.js의 모든 요소와 메서드에 접근할 수 있음
  - 즉, state를 직접 변경할 수 있지만 하지 않아야 함
- component에서 `dispatch()` 메서드에 의해 호출됨

## 4. Getters

- vue 인스턴스의 computed에 해당
- state를 활용하여 계산된 값을 얻고자 할 때 사용
  - state의 원본 데이터를 건들지 않고 계산된 값을 얻을 수 있음
- computed와 마찬가지로 getters의 결과는 캐시(cache)되며, 종속된 값이 변경된 경우에만 재계산됨
- getters에서 계산된 값은 state에 영향을 미치지 않음
- 첫번째 인자로 state, 두번째 인자로 getter를 받음
  - state를 기반으로 값을 계산, 추가로 다른 getters가 만든 값도 사용하는 경우도 있음

## 모든 데이터를 Vuex에서 관리해야 할까?

- Vuex를 사용한다고 해서 모든 데이터를 state에 넣어야 하는 것은 아님
- Vuex에서도 여전히 pass props, emit event를 사용하여 상태를 관리할 수 있음
- 개발 환경에 따라 적절하게 사용하는 것이 필요함

## 정리

- `state`
  - 중앙에서 관리하는 **모든 상태 정보**
- `mutations`
  - **state를 변경**하기 위한 methods
- `actions`
  - **비동기 작업이 포함될 수 있는 (외부 API와의 소통 등)** methods
  - state를 변경하는 것 외의 모든 로직 진행
- `getters`
  - state를 활용해 **계산한 새로운 변수 값**
- component에서 데이터를 조작하기 위한 데이터의 흐름
  - component ⇒ (actions) ⇒ mutations ⇒ state
- component에서 데이터를 사용하기 위한 데이터의 흐름
  - state ⇒ (getters) ⇒ component

## Vuex 실습

---

### 시작하기 전 - Object method shorthand

- 이제부터는 객체 메서드 축약형을 사용할 것

![vue36](https://user-images.githubusercontent.com/86648892/212527445-58136c03-f5d1-49ed-94d6-0e3f22b1f421.png)

### `src/store/index.js`

- vuex의 핵심 컨셉 4가지
  - `state`
  - `getters`
  - `mutations`
  - `actions`
    ![vue37](https://user-images.githubusercontent.com/86648892/212527444-3355ab47-8733-4c44-9287-edcef0a7c0b5.png)

### state

![vue38](https://user-images.githubusercontent.com/86648892/212527443-61705da4-e52b-4983-80aa-5cbe5b9a9404.png)

- 중앙에서 관리하는 모든 상태 정보
- `$store.state`로 접근 가능
- store의 state에 message 데이터 정의

![vue39](https://user-images.githubusercontent.com/86648892/212527442-3a08e9fa-c732-47bc-a45d-6108ddb3e32b.png)

- component에서 state 사용

![vue40](https://user-images.githubusercontent.com/86648892/212527441-1c8b8f3b-ce11-4d2e-9869-7f26b0e5a709.png)

- `$store.state`로 바로 접근하기 보다 `computed` 에 정의 후 접근하는 것을 권장

![vue41](https://user-images.githubusercontent.com/86648892/212527440-20cafb0f-484b-4bce-9c0c-a51f8665e49c.png)

- Vue 개발자 도구에서의 Vuex
- 관리 화면을 Vuex로 변경
- 관리되고 있는 state 확인 가능

### actions

- state를 변경할 수 있는 **mutations 호출**
- component에서 `**dispatch()`에 의해 호출됨\*\*
- `dipatch(A, B)`
  - A : 호출하고자 하는 actions 함수
  - B : 넘겨주는 데이터(payload)
    ![vue42](https://user-images.githubusercontent.com/86648892/212527439-12bd1d61-3359-4bd9-af63-b7bf27c51bd0.png)
- actions에 정의된 changeMessage 함수에 데이터 전달하기
- component에서 actions는 `dispatch()`에 의해 호출됨

![vue43](https://user-images.githubusercontent.com/86648892/212527437-d8a8f94c-2514-4d19-b0c7-a9619fcc16b1.png)

- actions의 첫번째 인자는 `context`
  - context는 store의 전반적인 속성을 모두 가지고 있으므로 `context.state`와 `context.getters`를 통해 mutations를 호출하는 것이 모두 가능
  - `dispatch()`를 사용해 다른 actions도 호출할 수 있음
  - **단, actions에서 state를 직접 조작하는 것은 삼가야 함**
- actions의 두번째 인자는 `payload`
  - 넘겨준 데이터를 받아서 사용

### mutations

![vue44](https://user-images.githubusercontent.com/86648892/212527436-449ad8b0-779f-400b-a2bf-626d0d72bcc3.png)

- **actions에서 `commit()`을 통해 mutations 호출하기**
- mutations는 state를 변경하는 유일한 방법
- component 또는 actions에서 `**commit()`에 의해 호출됨\*\*
- `commit(A, B)`
  - A : 호출하고자 하는 mutations 함수
  - B : payload
    ![vue45](https://user-images.githubusercontent.com/86648892/212527435-142d19b0-010b-4f68-b425-4b94c25d7413.png)
- **mutations 함수 작성하기**
- mutations는 state를 변경하는 유일한 방법
- mutations 함수의
  - 첫번째 인자는 `state`
  - 두번째 인자는 `payload`

### getters

![vue46](https://user-images.githubusercontent.com/86648892/212527433-7c1625b4-a9d7-4f9d-94f7-b8906d74bb00.png)

- **getters 사용해 보기**
- **getters는 state를 활용한 새로운 변수**
- getters 함수의
  - 첫번째 인자는 `state`
  - 두번째 인자는 `getters`

![vue47](https://user-images.githubusercontent.com/86648892/212527432-1dabd6e3-0ef3-4ab5-a0ec-8956b3a693d5.png)

- **getters의 다른 함수 사용해보기**

![vue48](https://user-images.githubusercontent.com/86648892/212527430-9abb96ec-c674-4b15-9bab-267aff0116f5.png)

- **getters 출력하기**
- getters 역시 state와 마찬가지로 computed에 정의해서 사용하는 것을 권장

![vue49](https://user-images.githubusercontent.com/86648892/212527429-bcb4247b-476e-4090-8ca0-b2dbd1608bea.png)

---

# Lifecycle Hooks

- 각 Vue 인스턴스는 생성과 소멸의 과정 중 단계별 초기화 과정을 거침
  - Vue 인스턴스가 생성된 경우, 인스턴스를 DOM에 마운트하는 경우, 데이터가 변경되어 DOM를 업데이트하는 경우 등
- 각 단계가 트리거가 되어 특정 로직을 실행할 수 있음
- 이를 Lifecycle Hooks이라고 함

![vue50](https://user-images.githubusercontent.com/86648892/212527428-add37e99-6d47-4eb6-835a-0b0ce3e35ea8.png)

## Lifecycle Hooks 맛보기

![vue51](https://user-images.githubusercontent.com/86648892/212527427-22b56368-6753-49a2-a1a7-12af4dfa2594.png)

![vue52](https://user-images.githubusercontent.com/86648892/212527426-9c8d134c-0b52-4285-a63e-310cefa34b83.png)

![vue53](https://user-images.githubusercontent.com/86648892/212527425-f2dd9621-bb6b-4ab3-af45-c3b937cc4cbc.png)

## created

- Vue instance가 생성된 후 호출됨
- data, computed 등의 설정이 완료된 상태
- 서버에서 받은 데이터를 vue instance의 data에 할당하는 로직을 구현하기 적함
- 단, mount되지 않아 요소에 접근할 수 없음

![vue54](https://user-images.githubusercontent.com/86648892/212527423-5b101ad9-f41b-4e59-a30e-d83e7635ee6b.png)

- JavaScript에서 학습한 Dog API 활용 실습의 경우
  - 버튼을 누르면 강아지 사진을 보여줌
- 버튼을 누르지 않아도 첫 실행 시 기본 사진이 출력되도록 하고 싶다면?
  - ⇒ created 함수에 강아지 사진을 가져오는 함수를 추가
    ![vue55](https://user-images.githubusercontent.com/86648892/212527422-43436c5c-203b-416b-9b0d-eef71aa914f4.png)

## mounted

- Vue instance가 요소에 mount된 후 호출됨
- mount된 요소를 조작할 수 있음

![vue56](https://user-images.githubusercontent.com/86648892/212527421-343598e4-3777-4a1d-ae6a-f1d70e93e482.png)

- `created`의 경우, mount 되기 전이기 때문에 DOM에 접근할 수 없으므로 동작하지 않음
- mounted는 주석 처리

![vue57](https://user-images.githubusercontent.com/86648892/212527420-2ebad463-2166-41f7-a8c6-e5976da4af1b.png)

## updated

- 데이터가 변경되어 DOM에 변화를 줄 때 호출됨

![vue58](https://user-images.githubusercontent.com/86648892/212527419-ecce5479-20d8-4874-9fb4-a622c1b6046b.png)

## Lifecycle Hooks 특징

- instance마다 각각의 Lifecycle을 가지고 있음

![vue59](https://user-images.githubusercontent.com/86648892/212527418-7b693bcc-221b-46cd-afbc-7a44c4a1f587.png)

- Lifecycle Hooks는 컴포넌트별로 정의할 수 있음
- 현재 해당 프로젝트는 `App.vue` 생성 ⇒ `ChildComponent` 생성 ⇒ `ChildComponent` 부착 ⇒ `App.vue` 부착 ⇒ `ChildComponent` 업데이트 순으로 동작한 것

![vue60](https://user-images.githubusercontent.com/86648892/212527417-c0c517d2-36ea-40d8-a043-085e61575747.png)

- 부모 컴포넌트의 mounted hook이 실행되었다고 해서 자식이 mount된 것이 아니고, 부모 컴포넌트가 updated hook이 실행되었다고 해서 자식이 updated된 것이 아님
- 부착 여부가 부모-자식 관계에 따라 순서를 가지고 있지 않은 것
- **instance마다 각각의 Lifecycle을 가지고 있기 때문**

---

# Simple Todo App with Vuex

- Vuex를 사용한 Todo 프로젝트 만들기
- 구현 기능
  - Todo CRUD
  - Todo 개수 계산
    - 전체 Todo
    - 완료된 Todo
    - 미완료된 Todo

## CRUD

### READ Todo

- store에 임의의 todo 데이터 생성
  - TodoList에서 computed로 받아오기
    - 해당 데이터 props로 TodoListItem에 내려주기

### CREATE Todo

- TodoForm에서 createTodo
  - actions에서 Todo 생성
    - mutations에서 만들어진 Todo를 state에 push

### Delete Todo

- 지울 todo에 대한 정보를 넘겨줘야함

### Update Todo

- isCompleted 값을 true와 false로 toggle

## Components

### App.vue

```jsx
<template>
  <div id="app">
    <h1>Todo List</h1>
    <h2>모든 Todo 개수: {{ allTodosCount }}</h2>
    <h2>완료된 Todo 개수: {{ completedTodosCount }}</h2>
    <h2>미완료된 Todo 개수: {{ unCompletedTodosCount }}</h2>
    <TodoList/>
    <TodoForm/>
    <!-- <button @click="loadTodos">Todo 불러오기</button> -->
  </div>
</template>

<script>
import TodoList from '@/components/TodoList'
import TodoForm from '@/components/TodoForm'

export default {
  name: 'App',
  components: {
    TodoList,
    TodoForm,
  },
  computed: {
    allTodosCount() {
      return this.$store.getters.allTodosCount
    },
    completedTodosCount() {
      return this.$store.getters.completedTodosCount
    },
    unCompletedTodosCount() {
      return this.$store.getters.unCompletedTodosCount
    }
  },
  methods: {
    loadTodos() {
      this.$store.dispatch('loadTodos')
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
```

### TodoForm.vue

```jsx
<template>
  <div>
    <input
      type="text"
      v-model.trim="todoTitle"
      @keyup.enter="createTodo"
    >
  </div>
</template>

<script>
export default {
  name:'TodoForm',
  data() {
    return {
      todoTitle: null,
    }
  },
  methods: {
    createTodo() {
      // console.log(this.todoTitle)
      if (this.todoTitle) {
        this.$store.dispatch('createTodo', this.todoTitle)
      }
      this.todoTitle = null
    }
  }
}
</script>

<style>
</style>
```

### TodoList.vue

```jsx
<template>
  <div>
    <TodoListItem
      v-for="(todo, index) in todos"
      :key="index"
      :todo="todo"
    />
  </div>
</template>

<script>
import TodoListItem from '@/components/TodoListItem'

export default {
  name: 'TodoList',
  components: {
    TodoListItem,
  },
  computed: {
    todos() {
      return this.$store.state.todos
    }
  },
}
</script>

<style>
</style>
```

### TodoListItem.vue

```jsx
<template>
  <div>
    <span
      @click="updateTodoStatus"
      :class="{ 'is-completed': todo.isCompleted }"
    >
      {{ todo.title }}
    </span>
    <button @click="deleteTodo">Delete</button>
  </div>
</template>

<script>
export default {
  name: 'TodoListItem',
  props: {
    todo: Object,
  },
  methods: {
    deleteTodo() {
      // console.log('삭제 메서드 호출!!')
      this.$store.dispatch('deleteTodo', this.todo)
      // this.$store.commit('DELETE_TODO', this.todo)
    },
    updateTodoStatus() {
      this.$store.dispatch('updateTodoStatus', this.todo)
    },
  }
}
</script>

<style>
  .is-completed {
    text-decoration: line-through;
  }
</style>
```

### `store/index.js`

```jsx
import Vue from "vue"
import Vuex from "vuex"
import createPersistedState from "vuex-persistedstate"

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    todos: [],
  },
  getters: {
    allTodosCount(state) {
      return state.todos.length
    },
    completedTodosCount(state) {
      // 1. 완료된 투두만 모아놓은 새로운 배열을 생성
      const completedTodos = state.todos.filter((todo) => {
        return todo.isCompleted === true
      })
      // 2. 그 새로운 배열의 길이를 반환
      return completedTodos.length
    },
    unCompletedTodosCount(state, getters) {
      return getters.allTodosCount - getters.completedTodosCount
    },
  },
  mutations: {
    CREATE_TODO(state, todoItem) {
      state.todos.push(todoItem)
    },
    DELETE_TODO(state, todoItem) {
      const index = state.todos.indexOf(todoItem)
      state.todos.splice(index, 1)
    },
    UPDATE_TODO_STATUS(state, todoItem) {
      console.log(todoItem)
      // todos 배열에서 선택된 todo의 is_completed값만 토글한 후
      // 업데이트 된 todos 배열로 되어야 함

      // made by 승태
      // const index = state.todos.indexOf(todoItem)
      // state.todos[index].isCompleted = !state.todos[index].isCompleted

      state.todos = state.todos.map((todo) => {
        if (todo === todoItem) {
          todo.isCompleted = !todo.isCompleted
        }
        return todo
      })
    },
    // LOAD_TODOS(state) {
    //   const localStorageTodos = localStorage.getItem('todos')
    //   const parsedTodos = JSON.parse(localStorageTodos)
    //   // console.log(parsedTodos)
    //   state.todos = parsedTodos
    // },
  },
  actions: {
    createTodo(context, todoTitle) {
      // Todo 객체 만들기
      const todoItem = {
        title: todoTitle,
        isCompleted: false,
      }
      // console.log(todoItem)
      context.commit("CREATE_TODO", todoItem)
      // context.dispatch('saveTodosToLocalStorage')
    },
    deleteTodo(context, todoItem) {
      context.commit("DELETE_TODO", todoItem)
      // context.dispatch('saveTodosToLocalStorage')
    },
    updateTodoStatus(context, todoItem) {
      context.commit("UPDATE_TODO_STATUS", todoItem)
      // context.dispatch('saveTodosToLocalStorage')
    },
    // saveTodosToLocalStorage(context) {
    //   const jsonTodos = JSON.stringify(context.state.todos)
    //   localStorage.setItem('todos', jsonTodos)
    // },
    // loadTodos(context) {
    //   context.commit('LOAD_TODOS')
    // }
  },
  modules: {},
})
```

---

# Local Storage

- 브라우저의 Local Storage에 데이터를 저장하여 브라우저를 종료하고 다시 실행해도 데이터가 보존될 수 있도록 하기
- vuex-persistedstate 라이브러리를 활용하여 편리하게 데이터를 보존해보기

## Window.localStorage

- 브라우저에서 제공하는 저장공간 중 하나인 Local Storage에 관련된 속성
- 만료되지 않고 브라우저를 종료하고 다시 실행해도 데이터가 보존됨
- 데이터가 문자열 형태로 저장됨
- 관련 메서드
  - `setItem(key, value)`
    - key, value 형태로 데이터 저장
  - `getItem(key)`
    - key에 해당하는 데이터 조회

## Local Storage 실습

![vue61](https://user-images.githubusercontent.com/86648892/212527416-b083d4da-193d-46f9-a170-a3df4974d972.png)

- todos 배열을 Local Storage에 저장하기
- 데이터가 문자열 형태로 저장되어야 하기 때문에 `JSON.stringify()` 를 사용해 문자열로 변환해주는 과정 필요
- state를 변경하는 작업이 아니기 때문에 mutations가 아닌 actions에 작성

![vue62](https://user-images.githubusercontent.com/86648892/212527415-91358843-afdd-41a7-a457-6506f753ec52.png)

- todo 생성, 삭제, 수정 시에 모두 saveTodosToLocalStorage action 메서드

![vue63](https://user-images.githubusercontent.com/86648892/212527414-2de83623-2ba1-4d20-8a5f-7f619e699185.png)

- 개발자도구 → Application → Storage → Local Storage에서 todos가 저장된 것을 확인
- 하지만 아직 Local Storage에 있는 todo 목록을 불러오는 것이 아니기 때문에 페이지 새로고침 이후 목록이 모두 사라짐
- 불러오기 버튼을 누르면 Local Storage에 저장된 데이터를 가져오도록 할 것
  1. 불러오기 버튼 작성
     ![vue64](https://user-images.githubusercontent.com/86648892/212527413-0f213d6b-dabf-4af3-92bc-7bcddac43c9d.png)
  1. loadTodos 메서드 작성
     ![vue65](https://user-images.githubusercontent.com/86648892/212527410-85942a30-5ec9-42c2-b59e-9eda31ef4ae8.png)
  1. loadTodos action 메서드 작성
     ![vue66](https://user-images.githubusercontent.com/86648892/212527409-5fbde067-49dd-4fa0-947a-6b702e1fe726.png)
  1. LOAD_TODOS mutation 메서드 작성
  - 문자열 데이터를 다시 object 타입으로 변환
    - `JSON.parse()` 하여 저장
      ![vue67](https://user-images.githubusercontent.com/86648892/212527408-1c805960-6db2-4752-93c9-fa680dacfaf0.png)

### 동작 확인

![vue68](https://user-images.githubusercontent.com/86648892/212527407-a210e5c0-3698-4940-af44-9b65238247f9.png)

---

## vuex-persistedstate

- Vuex state를 자동으로 브라우저의 Local Storage에 저장해주는 라이브러리 중 하나
- 페이지가 새로고침 되어도 Vuex state를 유지시킴
- Local Storage에 저장된 data를 자동으로 state로 불러옴
- 설치
  - `npm i vuex-persistedstate`
- 적용

  ```jsx
  // index.js

  import createPersistedState from 'vuex-persistedstate'

  Vue.use(Vuex)

  export default new Vuex.Store({
  	plugins: [
  		createPersistedState(),
  	],
  	...
  })
  ```

- 이전에 작성한 Local Storage 관련 코드를 모두 주석 처리하기
  - App.vue
    - 불러오기 버튼
    - loadTodos 메서드
  - index.js
    - LOAD_TODOS mutation 메서드
    - saveTodosToLocalStorage action 메서드
    - loadTodos action 메서드
    - context.dispatch(’saveTodosToLocalStorage’) 코드
- 이제는 불러오기 버튼 없이 자동으로 저장된 데이터를 불러올 수 있음
  ![vue69](https://user-images.githubusercontent.com/86648892/212527406-bce545af-d5d0-418b-b4b0-7a69af739429.png)

---

# Vue Router and Navigation Guard

- Vue Router
- Navigation Guard
- Articles app with Vue

---

# Vue Router

## Routing

- 네트워크에서 경로를 선택하는 프로세스
- 웹 서비스에서의 라우팅
  - 유저가 방문한 URL에 대해 적절한 결과를 응답하는 것
    - ex) `/articles/index/` 에 접근하면 articles의 index에 대한 결과를 보내줌
- 해당 url에 방문했을 때
  - 어디로 보내줄 것인가?
- Vue에서는 url 대신 route라고 불러준다

## Routing in SSR

- Server가 모든 라우팅을 통제
  - `return render`
  - `return redirect`
- URL로 요청이 들어오면 응답으로 완성된 HTML 제공
  - Django로 보낸 요청의 응답 HTML은 완성본인 상태였음
- 결론적으로, Routing(URL)에 대한 결정권을 서버가 가짐

## Routing in SPA and CSR

- 서버는 하나의 HTML(index.html)만을 제공
- 이후에 모든 동작은 하나의 HTML 문서 위에서 JavaScript 코드를 활용
  - DOM을 그리는데 필요한 추가적인 데이터가 있다면 axios와 같은 AJAX 요청을 보낼 수 있는 도구를 사용하여 데이터를 가져오고 처리
- 즉, **하나의 URL만 가질 수 있음**

## Why routing?

- 그럼 도작에 따라 URL이 반드시 바뀌어야 하는가?
  - 그렇지는 않으나
    - 유저의 사용성 관점에서는 필요함
- Routing이 없다면
  - 유저가 URL을 통한 페이지의 변화를 감지할 수 없음
  - 페이지가 무엇을 렌더링 중인지에 대한 상태를 알 수 없음
    - 새로고침 시 처음 페이지로 돌아감
    - 링크를 공유할 시 처음 페이지만 공유 가능
  - 브라우저의 뒤로가기 기능을 사용할 수 없음

## Vue Router

- Vue 공식 라우터
- SPA 상에서 라우팅을 쉽게 개발할 수 있는 기능을 제공
- 라우트(routes)에 컴포넌트를 매핑한 후
  - 어떤 URL에서 렌더링할지 알려줌
    - 즉, SPA를 MPA처럼 URL을 이동하면서 사용 가능
    - SPA의 단점 중 하나인 **“URL이 변경되지 않는다”**를 해결
      - 마치 페이지가 여러 개인 것같은 착각을 일으킴
- [참고] MPA (Multiple Page Application)
  - 여러 개의 페이지로 구성된 어플리케이션
  - SSR 방식으로 렌더링

### Vue Router 시작하기

- 기존에 프로젝트를 진행하고 있던 도중에 router를 추가하게 되면 App.vue를 덮어쓰므로 필요한 경우 명령을 실행하기 전에 파일을 백업해두어야 함

```bash
$ vue create vue-router-app // Vue 프로젝트 생성
$ cd vue-router-app         // 디렉토리 이동
$ vue add router            // Vue CLI를 통해 router plugin 적용

? Use history mode for router? (Requires proper server setup for index fallback in production)
// Y 선택
```

### History Mode

- URL을 기록하여 뒤로가기가 가능하도록 함
- 브라우저의 History API를 활용한 방식
  - 새로고침 없이 URL 이동 기록을 남길 수 있음
- 우리에게 익숙한 URL 구조로 사용 가능
  - ex) `http://localhost:8080/index`
- [참고] History mode를 사용하지 않으면 Default 값인 hash mode로 설정됨
  - ‘#’을 통해 URL을 구분하는 방식
  - ex) `http://localhost:8080#index`

![vue70](https://user-images.githubusercontent.com/86648892/212530171-c47de1ae-60f7-455b-b4e0-1dc9fd7f9394.png)

![vue71](https://user-images.githubusercontent.com/86648892/212530183-360a5003-cf7a-4adf-931e-f9ec0b06c354.png)

- `router/index.js` 생성
- `views` 폴더 생성

<img width="867" alt="vue72" src="https://user-images.githubusercontent.com/86648892/212530240-8a8c7b54-52ca-4f90-8638-ff04178c0e84.png">

## router-link

- a 태그와 비슷한 기능
  - URL을 이동시킴
    - routes에 등록된 컴포넌트와 매핑됨
    - 히스토리 모드에서 router-link는 클릭 이벤트를 차단하여 a 태그와 달리 브라우저가 페이지를 다시 로드하지 않도록 함
      - a 태그의 기본 이벤트가 차단되어 있음
- 목표 경로는 `to` 속성으로 지정됨
- 기능에 맞게 HTML에서 a 태그로 rendering되지만, 필요에 따라 다른 태그로 바꿀 수 있음

<img width="827" alt="vue73" src="https://user-images.githubusercontent.com/86648892/212530236-6d90934f-a689-4c5f-aba1-2c08ef91e7f1.png">

## router-view

- 주어진 URL에 대해 일치하는 컴포넌트를 렌더링하는 컴포넌트
- 실제 컴포넌트가 DOM에 부착되어 보이는 자리를 의미
- router-link를 클릭하면 routes에 매핑된 컴포넌트를 렌더링
- Django에서의 block tag와 비슷함
  - App.vue는 base.html의 역할
  - router-view는 block 태그로 감싼 부분

<img width="569" alt="vue74" src="https://user-images.githubusercontent.com/86648892/212530234-ec4eed59-cf12-4308-87c7-770d1b820585.png">

## `src/router/index.js`

- 라우터에 관련된 정보 및 설정이 작성되는 곳
- Django에서의 urls.py에 해당
- routes에 URL와 컴포넌트를 매핑

<img width="483" alt="vue75" src="https://user-images.githubusercontent.com/86648892/212530231-b1d4fedd-d4f0-4fcf-8ddb-5a647fa5d320.png">

## `src/Views`

- router-view에 들어갈 component 작성
- 기존에 컴포넌트를 작성하던 곳은 components 폴더 뿐이었지만 이제 두 폴더로 나뉘어짐
- 각 폴더 안의 .vue 파일들이 기능적으로 다른 것은 아님
  - 경로만 다를 뿐이다
- 폴더별 컴포넌트 배치는 다음과 같이 진행 (규약은 아님)
  - `views/`
    - routes에 매핑되는 컴포넌트, 즉 `<router-view>` 의 위치에 렌더링되는 컴포넌트를 모아두는 폴더
    - 다른 컴포넌트와 구분하기 위해 View로 끝나도록 만드는 것을 권장
      - ex) App 컴포넌트 내부의 AboutView, HomeView 컴포넌트
  - `components/`
    - routes에 매핑된 컴포넌트의 하위 컴포넌트를 모아두는 폴더
      - ex) HomeView 컴포넌트 내부의 HelloWorld 컴포넌트

---

# Vue Router 실습

### 주소를 이동하는 2가지 방법

1. 선언적 방식 navigation
2. 프로그래밍 방식 navigation

## 선언적 방식 네비게이션

- router-link의 `to` 속성으로 주소 전달
  - routes에 등록된 주소와 매핑된 컴포넌트로 이동
    <img width="470" alt="vue76" src="https://user-images.githubusercontent.com/86648892/212530228-5ebd1036-10aa-4423-8b7c-fb31ca414d0b.png">
- Named Routes
  - 이름을 가지는 routes - Django에서 path 함수의 name 인자의 활용과 같은 방식 - 동적인 값을 사용하기 때문에 v-bind를 사용해야 정상적으로 작동
    <img width="275" alt="vue77" src="https://user-images.githubusercontent.com/86648892/212530225-4deb8c58-c874-4f5a-a9a4-d6a361adcf53.png">
    <img width="586" alt="vue78" src="https://user-images.githubusercontent.com/86648892/212530224-71878f55-cfb9-4b7a-afd8-d9c572265319.png">

## 프로그래밍 방식 네비게이션

- Vue 인스턴스 내부에서 라우터 인스턴스에 `$router` 로 접근할 수 있음
- 다른 URL로 이동하려면 `this.$router.push` 를 사용
  - router의 history stack에 이동할 URL을 넣는(push) 방식
  - history stack에 기록이 남기 때문에 사용자가 브라우저의 뒤로 가기 버튼을 클릭하면 이전 URL로 이동할 수 있음
- 결국 `<router-link :to="...">` 를 클릭하는 것과 `$router.push(...)` 를 호출하는 것은 같은 동작

<img width="473" alt="vue79" src="https://user-images.githubusercontent.com/86648892/212530223-f897290f-61f6-4cd6-9ca0-26c7258c6b0b.png">

### Dynamic Route Matching

- 동적 인자 전달
  - URL의 특정 값을 변수처럼 사용할 수 있음
    - ex) Django에서의 variable routing
    - `$route.params` 로 변수에 접근 가능 - 다만 HTML에서 직접 사용하기 보다는 data에 넣어서 사용하는 것을 권장
      <img width="372" alt="vue80" src="https://user-images.githubusercontent.com/86648892/212530222-201f2070-afec-41c3-82b2-c8f4e543da10.png">

<img width="505" alt="vue81" src="https://user-images.githubusercontent.com/86648892/212530221-2a7d5f01-e364-41b7-860c-9fbceca567ef.png">

- Dynamic Route Matching (선언적 방식 네비게이션)
  <img width="839" alt="vue82" src="https://user-images.githubusercontent.com/86648892/212530219-1c780d66-7f49-4588-90a1-6fc8b4ffe729.png">
- Dynamic Route Matching (프로그래밍 방식 네비게이션)
  <img width="1513" alt="vue83" src="https://user-images.githubusercontent.com/86648892/212530218-98452790-9a4a-4706-b7c1-9aab78d00841.png">

### lazy-loading

- 모든 파일을 한 번에 로드하려고 하면 모든 것을 다 읽는 시간이 매우 오래 걸림
- 미리 로드를 하지 않고 특정 라우트에 방문할 때 매핑된 컴포넌트의 코드를 로드하는 방식을 활용할 수 있음
  - 모든 파일을 한 번에 로드하지 않아도 되기 때문에 최초에 로드하는 시간이 빨라짐
  - 당장 사용하지 않을 컴포넌트는 먼저 로드하지 않는 것이 핵심

<img width="1473" alt="vue84" src="https://user-images.githubusercontent.com/86648892/212530217-e34140e7-ea15-4112-900a-8bc4480ab115.png">

---

# Navigation Guard

- Vue router를 통해 특정 URL에 접근할 때 다른 URL로 리다이렉트하거나 해당 URL로의 접근을 막는 방법
  - ex) 사용자의 인증 정보가 없으면 특정 페이지에 접근하지 못하게 함
- 전역 가드
  - 어플리케이션 전역에서 동작
- 라우터 가드
  - 특정 URL에서만 동작
- 컴포넌트 가드
  - 라우터 컴포넌트 안에 정의

---

## 전역 가드

### Global Before Guard

- **다른 url 주소로 이동**할 때 항상 실행
- `router/index.js`
  - `router.beforeEach()` 를 사용하여 설정
- 콜백 함수의 값으로 다음과 같이 3개의 인자를 받음
  - `to`
    - 이동할 URL 정보가 담긴 Route 객체
  - `from`
    - 현재 URL 정보가 담긴 Route 객체
  - `next`
    - 지정한 URL로 이동하기 위해 호출하는 함수
      - 콜백 함수 내부에서 반드시 한 번만 호출되어야 함
      - 기본적으로 `to` 에 해당하는 URL로 이동
- URL이 변경되어 화면이 전환되기 전 `router.beforeEach()` 가 호출됨
  - 화면이 전환되지 않고 대기 상태가 됨
- 변경된 URL로 라우팅하기 위해서는 `next()` 를 호출해줘야 함
  - `next()` 가 호출되기 전까지 화면이 전환되지 않음

### 로그인 여부에 따른 라우팅 처리

- Login이 되어있지 않다면 Login 페이지로 이동하는 기능 추가

<img width="821" alt="vue85" src="https://user-images.githubusercontent.com/86648892/212530528-92046731-7ac5-4cb2-a0a0-135e61412a24.png">

- LoginView에 대한 라우터 링크 추가

<img width="838" alt="vue86" src="https://user-images.githubusercontent.com/86648892/212530526-6e592ffd-2213-4704-96bc-d5af7c427e13.png">

- HelloView에 로그인을 해야만 접근할 수 있도록 만들어 보기
- 로그인 여부에 대한 임시 변수 생성
- 로그인이 필요한 페이지를 저장
  - 로그인이 필요한 페이지들의 이름(라우터에 등록한 name)을 작성
- 앞으로 이동할 페이지(to)가 로그이 필요한 사이튼인지 확인

<img width="377" alt="vue87" src="https://user-images.githubusercontent.com/86648892/212530524-586c9c69-0075-464b-a698-1f2eef94d15b.png">

- isAuthRequired 값에 따라 로그인이 필요한 페이지이고 로그인이 되어있지 않으면
  - Login 페이지로 이동
- 그렇지 않으면
  - 기존 루트로 이동
- `next()` 인자가 없을 경우 to로 이동
  - `next()` 가 한 번만 호출되도록 유의

<img width="376" alt="vue88" src="https://user-images.githubusercontent.com/86648892/212530523-c9635987-7fce-48bf-9371-03c62e43fe74.png">

<img width="823" alt="vue89" src="https://user-images.githubusercontent.com/86648892/212530522-c0db1b9e-818a-4298-8eb4-6b1790f949da.png">

<img width="845" alt="vue90" src="https://user-images.githubusercontent.com/86648892/212530520-4aad859c-f171-4f99-b650-5600506c069d.png">

<img width="839" alt="vue91" src="https://user-images.githubusercontent.com/86648892/212530518-eed1f60d-6ad1-48b6-98af-0f915b614e65.png">

<img width="843" alt="vue92" src="https://user-images.githubusercontent.com/86648892/212530517-ff790be2-0bc6-469d-9ce5-8c289f621cbd.png">

<img width="856" alt="vue93" src="https://user-images.githubusercontent.com/86648892/212530516-6cf7bd54-6abe-4004-8fe9-06f7d22515e4.png">

---

## 라우터 가드

- 전체 route가 아닌 특정 route에 대해서만 가드를 설정하고 싶을 때 사용
- `beforeEnter()`
  - route에 진입했을 때 실행됨
  - 라우터를 등록한 위치에 추가
  - 단, 매개변수, 쿼리, 해시 값이 변경될 때는 실행되지 않고 다른 경로에서 탐색할 때만 실행됨
  - 콜백 함수는 to, from, next를 인자로 받음

### 로그인 여부에 따른 라우팅 처리

- 이미 로그인 되어있는 경우 HomeView로 이동하기
- 기존 전역 가드 실습코드는 주석처리

<img width="1446" alt="vue94" src="https://user-images.githubusercontent.com/86648892/212530515-c4f351e7-9af4-46fd-bf79-12fd42ec678b.png">

<img width="1380" alt="vue95" src="https://user-images.githubusercontent.com/86648892/212530514-764ce8c4-26b3-4663-ae91-7bf548fe65a5.png">

- Login을 제외한 다른 페이지로 이동하면 라우터 가드를 따로 설정해주지 않았기 때문에 라우터 가드가 동작하지 않음
- 이런 식으로 특정 라우트만 따로 가드를 하고 싶은 경우에는 라우터 가드를 사용
- `isLoggedIn = false` 로 변경하면 Login 페이지로 정상 이동 가능

---

## 컴포넌트 가드

- 특정 컴포넌트 내에서 가드를 지정하고 싶을 때 사용
- `beforeRouteUpdate()`
  - 해당 컴포넌트를 렌더링하는 경로가 변경될 때 실행

### Params 변화 감지

- about에서 jun에게 인사하는 페이지로 이동

<img width="712" alt="vue96" src="https://user-images.githubusercontent.com/86648892/212530513-52989a40-dcba-4ac3-95cf-8553525a79b3.png">

- navbar에 있는 Hello를 눌러 harry에게 인사하는 페이지로 이동
  - URL은 변하지만 페이지는 변화하지 않음

<img width="714" alt="vue97" src="https://user-images.githubusercontent.com/86648892/212530511-9935146a-503d-488c-b0f0-d30cd094b17a.png">

- 변화하지 않는 이유
  - 컴포넌트가 재사용되었기 때문
  - 기존 컴포넌트를 지우고 새로 만드는 것보다 효율적
    - 단, lifecycle hook이 호출되지 않음
    - 따라서 `$route.params` 에 있는 데이터를 새로 가져오지 않음
- `beforeRouteUpdate()` 를 사용해서 처리
  - userName을 이동할 params에 있는 userName으로 재할당

<img width="475" alt="vue98" src="https://user-images.githubusercontent.com/86648892/212530510-fb58aabe-1703-407b-983b-9977ee9a26f5.png">

---

## 404 Not Found

### 요청한 리소스가 존재하지 않는 경우

- 모든 경로에 대해서 404 page로 redirect 시키기
  - 기존에 명시한 경로가 아닌 모든 경로가 404 page로 redirect됨
  - 이 때, routes의 최하단부에 작성해야함

<img width="476" alt="vue99" src="https://user-images.githubusercontent.com/86648892/212530508-6954df7a-071e-41fa-8797-01b048c8e1a5.png">

### 형식은 유효하지만 특정 리소스를 찾을 수 없는 경우

- 데이터가 없음을 명시
- 404 page로 이동
- Dog API(https://dog.ceo/dog-api/)를 참고하여 실습

<img width="871" alt="vue100" src="https://user-images.githubusercontent.com/86648892/212530507-e60e397e-b893-4dd4-ab2a-572799043026.png">

<img width="1508" alt="vue101" src="https://user-images.githubusercontent.com/86648892/212530506-b858c939-6e75-48e5-ba7b-612ddc2e614c.png">

<img width="1276" alt="vue102" src="https://user-images.githubusercontent.com/86648892/212530502-93b5580a-bc9c-4b82-80cc-97d264e8feda.png">

<img width="1372" alt="vue103" src="https://user-images.githubusercontent.com/86648892/212530501-2c637c7f-760b-4f44-bf82-034ebb26870e.png">

<img width="1381" alt="vue104" src="https://user-images.githubusercontent.com/86648892/212530500-faebf75a-0f7b-414b-8f7f-72d6abf359b8.png">

<img width="1314" alt="vue105" src="https://user-images.githubusercontent.com/86648892/212530498-691ab9ca-0ed5-4fd9-89d0-a0d2557469be.png">

<img width="1374" alt="vue106" src="https://user-images.githubusercontent.com/86648892/212530497-851c9bb2-8077-4343-abba-ef63319cf0c4.png">

<img width="1272" alt="vue107" src="https://user-images.githubusercontent.com/86648892/212530495-74ededf9-82ac-4fb0-9da1-3b96ebd4341f.png">

---

# Articles with Vue

## 프로젝트 시작

```bash
$ vue create articles
$ cd articles
$ vue add vuex
$ vue add router
```

<img width="394" alt="vue108" src="https://user-images.githubusercontent.com/86648892/212530492-7ece8131-c80e-4bf6-9fa6-8bff1b7ac629.png">

## `router/index.js`

```jsx
import Vue from "vue"
import VueRouter from "vue-router"
import IndexView from "../views/IndexView.vue"
import CreateView from "../views/CreateView.vue"
import DetailView from "../views/DetailView.vue"
import NotFound404 from "../views/NotFound404.vue"

Vue.use(VueRouter)

const routes = [
  {
    path: "/",
    name: "index",
    component: IndexView,
  },
  {
    path: "/create",
    name: "create",
    component: CreateView,
  },
  {
    path: "/404-not-found",
    name: "NotFound404",
    component: NotFound404,
  },
  {
    path: "/:id",
    name: "detail",
    component: DetailView,
  },
  {
    path: "*",
    redirect: { name: "NotFound404" },
  },
]

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
})

export default router
```

## `store/index.js`

```jsx
import Vue from "vue"
import Vuex from "vuex"

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    article_id: 3,
    articles: [
      {
        id: 1,
        title: "title1",
        content: "content1",
        createdAt: new Date().getTime(),
      },
      {
        id: 2,
        title: "title2",
        content: "content2",
        createdAt: new Date().getTime(),
      },
    ],
  },
  getters: {},
  mutations: {
    CREATE_ARTICLE(state, article) {
      state.articles.push(article)
      state.article_id = state.article_id + 1
    },
    DELETE_ARTICLE(state, article_id) {
      state.articles = state.articles.filter((article) => {
        return !(article.id === article_id)
      })
    },
  },
  actions: {
    createArticle(context, payload) {
      const article = {
        id: context.state.article_id,
        title: payload.title,
        content: payload.content,
        createdAt: new Date().getTime(),
      }
      context.commit("CREATE_ARTICLE", article)
    },
  },
  modules: {},
})
```

## views

### App.vue

```jsx
<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
```

### IndexView.vue

```jsx
<template>
  <div>
    <h1>Articles</h1>
    <router-link :to="{ name: 'create' }">Create Article</router-link>
    <ArticleItem
      v-for="article in articles"
      :key="article.id"
      :article=article
    />
  </div>
</template>

<script>
import ArticleItem from "@/components/ArticleItem"

export default {
  name: 'IndexView',
  components: {
    ArticleItem,
  },
  computed: {
    articles() {
      return this.$store.state.articles
    }
  }
}
</script>

<style>
</style>
```

### CreateView.vue

```jsx
<template>
  <div>
    <h1>Create Article</h1>
    <form @submit.prevent="createArticle">
      <input type="text" v-model.trim="title" /><br />
      <textarea v-model.trim="content"></textarea>
      <input type="submit" />
    </form>
    <router-link :to="{ name: 'index' }">BACK</router-link>
  </div>
</template>

<script>
export default {
  name: "CreateView",
  data() {
    return {
      title: null,
      content: null,
    }
  },
  methods: {
    createArticle() {
      const title = this.title
      const content = this.content
      if (!title) {
        alert("Enter a title!")
      } else if (!content) {
        alert("Enter a content!")
      } else {
        const payload = {
          title,
          content,
        }
        this.$store.dispatch("createArticle", payload)
        this.$router.push({ name: "index" })
      }
    },
  },
}
</script>

<style></style>
```

### DetailView.vue

```jsx
<template>
  <div>
    <h1>Detail</h1>
    <p>Number: {{ article?.id }}</p>
    <p>Title: {{ article?.title }}</p>
    <p>Content: {{ article?.content }}</p>
    <!-- <p>Created At: {{ article?.createdAt }}</p> -->
    <p>Created At: {{ articleCreatedAt }}</p>
    <button @click="deleteArticle">DELETE</button><br />
    <router-link :to="{ name: 'index' }">BACK</router-link>
  </div>
</template>

<script>
export default {
  name: "DetailView",
  data() {
    return {
      article: null,
    }
  },
  computed: {
    articles() {
      return this.$store.state.articles
    },
    articleCreatedAt() {
      const article = this.article
      const createdAt = new Date(article?.createdAt).toLocaleString()
      return createdAt
    },
  },
  methods: {
    getArticleById(id) {
      // const id = this.$route.params.id
      for (const article of this.articles) {
        if (article.id === Number(id)) {
          this.article = article
          break
        }
      }
      if (this.article === null) {
        this.$router.push({ name: "NotFound404" })
      }
    },
    deleteArticle() {
      this.$store.commit("DELETE_ARTICLE", this.article.id)
      this.$router.push({ name: "index" })
    },
  },
  created() {
    this.getArticleById(this.$route.params.id)
  },
}
</script>

<style></style>
```

### NotFound404.vue

```jsx
<template>
  <div>
    <h1>404 Not Found</h1>
  </div>
</template>

<script>
export default {
  name: "NotFound404",
}
</script>

<style></style>
```

## components

### ArticleItem.vue

```jsx
<template>
  <!-- @click="goDetail" -->
  <div @click="goDetail(article.id)">
    <p>Number: {{ article.id }}</p>
    <p>Title: {{ article.title }}</p>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'ArticleItem',
  props: {
    article: Object,
  },
  methods: {
    // goDetail() {
    //   this.$router.push({ name: 'detail', params: {id: `${this.article.id}` }})
    // },
    goDetail(id) {
      this.$router.push({ name: 'detail', params: {id} })
    }
  }
}
</script>

<style>
</style>
```

---

# Vue with DRF

- Vue with DRF
- CORS
- DRF Auth System
- DRF Auth with Vue
- DRF spectacular

---

# Vue with DRF

- Server와 Client의 통신 방법 이해하기
- CORS 이슈 이해하고 해결하기
- DRF Auth System 이해하기
- Vue와 API server 통신하기

---

# Server and Client

## Server

- 클라이언트에게 **_정보_**와 **_서비스_**를 제공하는 컴퓨터 시스템
- 서비스 전체를 제공
  - Django Web Service
    ![vue109](https://user-images.githubusercontent.com/86648892/212540524-91a346a5-577c-4c84-b6f1-48a959910128.png)
    - Django를 통해 전달받은 HTML에는 하나의 웹 페이지를 구성할 수 있는 모든 데이터가 포함
    - 서버에서 모든 내용을 렌더링하여 하나의 HTML 파일로 제공
    - 정보를 포함한 web 서비스를 구성하는 모든 내용을 서버 측에서 제공
- 정보를 제공
  ![vue110](https://user-images.githubusercontent.com/86648892/212540523-73fa4dcb-33c4-4af9-b863-ada4c3e3b7d0.png)
  - DRF API Service
  - Django를 통해 관리하는 정보만을 클라이언트에 제공
  - DRF를 사용하여 JSON으로 변환

## Client

- **_Server가 제공하는 서비스에 적절한 요청_**을 통해 **_Server로부터 반환받은 응답을 사용자에게 표현_**하는 기능을 가진 프로그램 혹은 시스템
- Server가 제공하는 서비스에 적절한 요청
  - Server가 정의한 방식대로 요청 인자를 넘겨 요청
  - Server는 정상적인 요청에 적합한 응답 제공
- Server로부터 반환받은 응답을 사용자에게 표현
  ![vue111](https://user-images.githubusercontent.com/86648892/212540521-3ca1d832-288b-4b6c-be11-4f0152de55e6.png)
  - 사용자의 요청에 적합한 data를 server에 요청하여 응답받은 결과로 **_적절한 화면을 구성_**

## 정리

- Server는 정보와 서비스를 제공
  - DB와 통신하며 데이터를 CRUD하는 것을 담당
  - 요청을 보낸 Client에게 정상적인 요청이었다면 처리한 결과를 응답
- Client는 사용자의 정보 요청을 처리, server에게 응답받은 정보를 표현
  - Server에게 정보(데이터)를 요청
  - 응답받은 정보를 가공하여 화면에 표현

---

# Vue with DRF 사전작업

![vue112](https://user-images.githubusercontent.com/86648892/212540519-ee476041-65f2-4fea-868d-7d8870bb48ca.png)

- 컴포넌트 구성
- fixtures를 통한 loaddata
  ```bash
  $ python manage.py migrate
  $ python manage.py loaddata articles.json comments.json
  ```
- npm을 통한 패키지 설치
  ```bash
  $ npm install
  $ npm run serve
  ```

---

# CORS (Cross-Origin Resource Sharing)

![vue113](https://user-images.githubusercontent.com/86648892/212540518-b4874294-62fe-4857-b831-7e299e0d75be.png)

![vue114](https://user-images.githubusercontent.com/86648892/212540517-dbaf9f7b-12ee-406f-8244-b978df2d857a.png)

- 현재 Django 서버는 8000번 포트를, Vue 서버는 8080 포트를 사용
- Server에서는 200 상태 코드를 반환하였으나 Client Console에서는 Error를 확인
  - 데이터를 확인할 수 없는 이유
    - CORS policy에 의해 blocked되었기 때문

## What Happened?

- 브라우저가 요청을 보내고 서버의 응답이 브라우저에 도착
  - Server의 log는 200(정상) 반환
    - 즉, Server는 정상적으로 응답했지만 브라우저가 막은 것
- 보안상의 이유로 브라우저는 **_동일 출처 정책(SOP)_**에 의해 다른 출처의 리소스와 상호작용하는 것을 제한함

### SOP (Same Origin Policy)

- “동일 출처 정책”
- 불러온 문서나 스크립트가 **_다른 출처_**에서 가져온 리소스와 상호작용하는 것을 제한하는 보안 방식
- 잠재적으로 해로울 수 있는 문서를 분리함으로써 공격받을 수 있는 경로를 줄임
- [https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy)

### Origin (출처)

- URL의 Protocol, Host, Port를 모두 포함하여 출처라 부름
- Same Origin
  - Protocol, Host, Port 세 영역이 일치하는 경우에만 동일 출처로 인정
    ![vue115](https://user-images.githubusercontent.com/86648892/212540516-e66d8461-66ae-4a41-9d10-f64e72eeb072.png)
    ![vue116](https://user-images.githubusercontent.com/86648892/212540513-5dd6182f-ac34-4eac-b99c-0bfcd3378b47.png)

### CORS (교차 출처 리소스 공유)

- 추가 **_HTTP Header_**를 사용하여
  - 특정 출처에서 실행 중인 웹 어플리케이션이 **_다른 출처의 자원에 접근할 수 있는 권한_**을 부여하도록 **_브라우저에 알려주는_** 체제
    - 어떤 출처에서 자신의 컨텐츠를 불러갈 수 있는지 **_서버에 지정_**할 수 있는 방법
- 리소스가 자신의 출처와 다를 때 교차 출처 HTTP 요청을 실행
  - 만약 다른 출처의 리소스를 가져오기 위해서는 이를 제공하는 서버가 브라우저에게 **_다른 출처지만 접근해도 된다는 사실을 알려야 함_**
  - “교차 출처 리소스 공유 정책 (CORS policy)”

### CORS policy (교차 출처 리소스 공유 정책)

- 다른 출처에서 온 리소스를 공유하는 것에 대한 정책
- CORS policy에 위배되는 경우 브라우저에서 해당 응답 결과를 사용하지 않음
  - Server에서 응답을 주더라도 브라우저에서 거절
- 다른 출처의 리소스를 불러오려면 그 출처에서 올바른 CORS header를 포함한 응답을 반환해야 한다
- [https://developer.mozilla.org/ko/docs/Web/HTTP/CORS](https://developer.mozilla.org/ko/docs/Web/HTTP/CORS)

## How to set CORS

- CORS 표준에 의해 추가된 HTTP Response Header를 통해 이를 통제 가능
- HTTP Response Header 예시
  - **Access-Control-Allow-Origin**
    - 단일 출처를 지정하여 브라우저가 해당 출처가 리소스에 접근하도록 허용
  - Access-Control-Allow-Credentials
  - Access-Control-Allow-Headers
  - Access-Control-Allow-Methods

### django-cors-headers library

- [https://github.com/adamchainz/django-cors-headers](https://github.com/adamchainz/django-cors-headers)
- **응답에 CORS header를 추가**해주는 라이브러리
- 다른 출처에서 Django 어플리케이션에 대한 브라우저 내 요청을 허용함
- `pip install django-cors-headers`
  - `pip freeze > requirements.txt`
    - `INSTALLED_APPS` 에 `'corsheaders'` 추가
    - `MIDDLEWARE` 에 `'corsheaders.middleware.CorsMiddleware'` 추가
      - 위치는 `'django.middleware.common.CommonMiddleware'` 위에 쓰는 것을 권장
      - CorsMiddleware는 가능한 CommonMiddleware보다 먼저 정의되어야 함
    - `CORS_ALLOWED_ORIGINS` 에 교차 출처 자원 공유를 허용할 Domain 등록
      - 만약 모든 Origin을 허용하고자 한다면 `CORS_ALLOWED_ALL_ORIGINS = True` - 권장하지는 않음
        ![vue117](https://user-images.githubusercontent.com/86648892/212540512-9e32c5bb-ccb3-4a96-8013-2d04996d7e01.png)
    - 응답에 Access-Control-Allow-Origin 헤더가 있는 것을 확인
      ![vue118](https://user-images.githubusercontent.com/86648892/212540510-8929569b-6f06-46a0-ab87-320b4b0b7108.png)

---

# DRF Auth System

## Authentication and Authorization

### Authentication

- 인증, 입증
- 자신이라고 주장하는 사용자가 누구인지 확인하는 행위
- 모든 보안 프로세스의 첫 단계
- 즉, 내가 누구인지를 확인하는 과정
- 401 Unauthorized
  - 비록 HTTP 표준에서는 “미승인(unauthorized)”을 명확히 하고 있지만, 의미상 이 응답은 “비인증(unauthenticated)”을 의미

### Authorization

- 사용자에게 특정 리소스 또는 기능에 대한 액세스 권한을 부여하는 과정 및 절차
- 보안 환경에서 권한 부여는 항상 인증이 먼저 필요함
  - 사용자는 조직에 대한 액세스 권한을 부여받기 전에 먼저 자신의 ID가 진짜인지 먼저 확인해야함
- 서류의 등급, 웹 페이지에서 글을 조회, 삭제, 수정할 수 있는 방법, 제한 구역
  - 인증이 되었어도 모든 권한을 부여받는 것은 아님
- 403 Forbidden
  - 401과 다른 점은 서버는 클라이언트가 누구인지 알고 있음

### Authentication and Authorization work together

- 회원가입 후, 로그인 시 서비스를 이용할 수 있는 권한 생성
  - 인증 이후에 권한이 따라오는 경우가 많음
- 단, 모든 인증을 거쳐도 권한이 동일하게 부여되는 것은 아님
  - Django에서 로그인을 했더라도 다른 사람의 글까지 수정 및 삭제가 가능하진 않음
- 세션, 토큰, 제3자를 활용하는 등의 다양한 인증 방식이 존재

### 인증 여부 확인 방법

- DRF 공식문서에서 제안하는 인증 절차 방법
  - [https://www.django-rest-framework.org/api-guide/authentication/](https://www.django-rest-framework.org/api-guide/authentication/)

<img width="622" alt="vue119" src="https://user-images.githubusercontent.com/86648892/212540509-4d49070a-4693-4c85-aa53-ef6aad941376.png">

- BasicAuthentication, SessionAuthentication?
- settings.py에 작성하여야 할 설정
  - “기본적인 인증 절차를 어떠한 방식으로 둘 것이냐”를 설정하는 것
  - 예시의 2가지 방법 외에도 각 Framework마다 다양한 인증 방식이 있음
- 이번에 사용할 방법은 DRF가 기본으로 제공해주는 인증 방식 중 하나인 TokenAuthentication
- 모든 상황에 대한 인증 방식을 정의하는 것이므로, 각 요청에 따라 다른 인증 방식을 거치고자 한다면 다른 방식이 필요
- view 함수마다 (각 요청마다) 다른 인증 방식을 설정하고자 한다면 decorator 활용

<img width="602" alt="vue120" src="https://user-images.githubusercontent.com/86648892/212540507-43ae6eb8-82d4-44fb-83ab-1a01b5200833.png">

- [참고] permission_classes
  - 권한 관련 설정
  - 권한 역시 특정 view 함수마다 다른 접근 권한을 요구할 수 있음

### 다양한 인증 방식

- BasicAuthentication
  - 가장 기본적인 수준의 인증 방식
  - 테스트에 적합
- SessionAuthentication
  - Django에서 사용하였던 session 기반의 인증 시스템
  - DRF와 Django의 session 인증 방식은 보안적 측면을 구성하는 방법에 차이가 있음
- RemoteUserAuthentication
  - Django의 Remote user 방식을 사용할 때 활용하는 인증 방식
- TokenAuthentication
  - 매우 간단하게 구현할 수 있음
  - 기본적인 보안 기능 제공
  - 다양한 외부 패키지가 있음
- settings.py에서 `DEFAULT_AUTHENTICATION_CLASSES` 를 정의
  - TokenAuthentication 인증 방식을 사용할 것임을 명시

### TokenAuthentication 사용 방법

- INSTALLED_APPS에 `rest_framework.authtoken` 등록

<img width="705" alt="vue121" src="https://user-images.githubusercontent.com/86648892/212540506-791d1b72-2240-4e28-b4e7-9ec75cb467f7.png">

- 각 User마다 고유 Token 생성

<img width="702" alt="vue122" src="https://user-images.githubusercontent.com/86648892/212540504-26b5cf1a-31f4-4ce4-b76e-f13281db01ec.png">

- 생성한 Token을 각 User에게 발급
  - User는 발급받은 Token을 요청과 함께 전송
  - Token을 통해 User 인증 및 권한 확인
- Token 발급 방법

<img width="474" alt="vue123" src="https://user-images.githubusercontent.com/86648892/212540501-74f24065-5ab2-45ff-9bfb-0925fa486909.png">

- User는 발급받은 Token을 headers에 담아 요청과 함께 전송
  - 단, 반드시 Token 문자열 함께 삽입
    - 삽입해야할 문자열은 각 인증 방식마다 다름
      - ex) Bearer, Auth, JWT 등
  - 주의) Token 문자열과 발급받은 실제 Token 사이를 ‘ ‘(공백)으로 구분
- Authorization HTTP headers 작성 방법

<img width="758" alt="vue124" src="https://user-images.githubusercontent.com/86648892/212540500-1aacb091-bfb3-4028-ae44-1a6786911d68.png">

### 토큰 생성 및 관리 문제점

- 기본 제공 방식에서 고려하여야 할 사항들
  1. Token 생성 시점
  2. 생성한 Token 관리 방법
  3. User와 관련된 각종 기능 관리 방법
     - 회원가입
     - 로그인
     - 회원정보 수정
     - 비밀번호 변경 등

---

# dj-rest-auth

- Token을 생성하기 위해 사용할 라이브러리
- 회원가입, 인증(소셜미디어 인증 포함), 비밀번호 재설정, 사용자 세부 정보 검색, 회원정보 수정 등을 위한 REST API end point 제공
- 주의) django-rest-auth는 더 이상 업데이트를 지원하지 않음 `dj-rest-auth` 사용

<img width="680" alt="vue125" src="https://user-images.githubusercontent.com/86648892/212540498-02713905-32c5-4990-9d6d-26c2b29c1f4d.png">

## dj-rest-auth 사용 방법

1. 패키지 설치
2. App 등록
3. url 등록

<img width="635" alt="vue126" src="https://user-images.githubusercontent.com/86648892/212540492-c7194a98-2053-4a6f-8d05-5b963586f9d5.png">

## dj-rest-auth 사용하기

- auth.User를 accounts.User로 변경
  - auth.User로 설정된 DB 제거

<img width="376" alt="vue127" src="https://user-images.githubusercontent.com/86648892/212531361-22fa7503-f1eb-4541-8766-a00a873c1ade.png">

- dj-rest-auth 설치
  - `pip install dj-rest-auth`
    - `pip freeze > requirements.txt`
- `settings.py` 설정

<img width="475" alt="vue128" src="https://user-images.githubusercontent.com/86648892/212531359-eb6dfbec-a6cd-462b-8ead-b312eb14a6b5.png">

- migrate
  - `python manage.py migrate`
- urlpatterns 작성
  - `/accounts/` 로 이동
    - 회원가입 기능 없음
      - 회원가입은 토큰을 생성하는 것
        - 기본적으로 생성된 url은 인증된 회원을 대상으로 하는 기능들
        - 공식문서 확인
          - Registration (optional)
            - `pip install 'dj-rest-auth[with_social]'`
          - Social Authentication (optional)
            - 다른 소셜 계정들로 로그인 가능

<img width="526" alt="vue129" src="https://user-images.githubusercontent.com/86648892/212531357-b6543ffe-f1db-4586-b74f-6ed757315879.png">

![vue130](https://user-images.githubusercontent.com/86648892/212531356-ff1af6bb-5760-41a4-b702-2c5b2f113cbf.png)

### Registration

<img width="1441" alt="vue131" src="https://user-images.githubusercontent.com/86648892/212531354-1cfc079a-ad12-4674-8d7d-a649779ced8b.png">

<img width="1474" alt="vue132" src="https://user-images.githubusercontent.com/86648892/212531353-6a4d088e-3b76-404a-ba7b-85c58e184fdd.png">

<img width="1451" alt="vue133" src="https://user-images.githubusercontent.com/86648892/212531352-46df68ec-4937-43a9-9d1e-eb61ceb2da4f.png">

<img width="1453" alt="vue134" src="https://user-images.githubusercontent.com/86648892/212531351-08d7a812-09b6-4815-8f7d-8748902e7d77.png">

### Signup and Login

<img width="1462" alt="vue135" src="https://user-images.githubusercontent.com/86648892/212531350-7306f6cd-0bdf-405c-bf6f-cf448d12ed4b.png">

### Password Change

<img width="1463" alt="vue136" src="https://user-images.githubusercontent.com/86648892/212531349-634628ac-f16c-43d0-8425-74f7c9bfd04f.png">

<img width="1096" alt="vue137" src="https://user-images.githubusercontent.com/86648892/212531348-60bded9c-46a2-4c72-8115-c0d44eab0e6f.png">

<img width="1251" alt="vue138" src="https://user-images.githubusercontent.com/86648892/212531347-a772fa7f-c515-4372-bd25-0a1960d8baed.png">

<img width="1193" alt="vue139" src="https://user-images.githubusercontent.com/86648892/212531345-31a75f4a-f966-4bc6-b915-98ba686a811a.png">

<img width="1391" alt="vue140" src="https://user-images.githubusercontent.com/86648892/212531344-e23dc2f1-06f1-48fb-a5c0-98be052c24a2.png">

---

## Permission Setting

<img width="1329" alt="vue141" src="https://user-images.githubusercontent.com/86648892/212531342-1845425f-17c4-4b9b-b2ad-d835530d53d1.png">

<img width="1401" alt="vue142" src="https://user-images.githubusercontent.com/86648892/212531341-1e0528c0-9369-4a17-a12e-95a30c8ead1b.png">

<img width="1152" alt="vue143" src="https://user-images.githubusercontent.com/86648892/212531340-6834fa16-c9a4-4b60-8d5d-4ee24e3a077a.png">

### Article List Read

<img width="1479" alt="vue144" src="https://user-images.githubusercontent.com/86648892/212531339-f03102e2-96f3-4980-9084-1fc8522c5da2.png">

<img width="1238" alt="vue145" src="https://user-images.githubusercontent.com/86648892/212531338-e23fc57d-2f26-4c5f-a6c3-ffecfd8fcab6.png">

### Article Create

<img width="1503" alt="vue146" src="https://user-images.githubusercontent.com/86648892/212531336-0346247c-0f66-402a-9f20-800e0d78e313.png">

<img width="1207" alt="vue147" src="https://user-images.githubusercontent.com/86648892/212531335-4925f468-171b-413c-97d6-1a56ec9e0efe.png">

### Article Detail Read

<img width="1251" alt="vue148" src="https://user-images.githubusercontent.com/86648892/212531333-a8f23c70-17ab-48a5-8071-968bb4144d19.png">

---

## 정리

1. 인증 방법 설정
   - `DEFAULT_AUTHENTICATION_CLASSES`
2. 권한 설정하기
   - `DEFAULT_PERMISSION_CLASSES`
3. 인증 방법, 권한 세부 설정도 가능
   - `@authentication_classes`
   - `@permission_classes`
4. 인증 방법은 다양한 방법이 있으므로 내 서비스에 적합한 방식을 선택

---

# DRF Auth with Vue

### 인증과 권한에 대한 요청을 Vue가 담당

### SignUp Request

<img width="1463" alt="vue149" src="https://user-images.githubusercontent.com/86648892/212531332-e3138476-8560-4e29-a207-cb17a31dfe79.png">

<img width="1439" alt="vue150" src="https://user-images.githubusercontent.com/86648892/212531330-1384ae7c-8ce3-482b-9319-59a80962feff.png">

<img width="1350" alt="vue151" src="https://user-images.githubusercontent.com/86648892/212531329-c7e5b3f5-1929-4ace-9a2d-5353729cd0c0.png">

<img width="1216" alt="vue152" src="https://user-images.githubusercontent.com/86648892/212531327-94399b30-61e5-489e-a263-e3219d944ce3.png">

- 회원가입을 완료 시 응답 받을 정보 Token을 store에서 관리할 수 있도록 actions를 활용하여 요청 후, state에 저장할 로직 작성
  - 회원가입이나 로그인 후 얻을 수 있는 Token은 server 구성 방식에 따라 매 요청마다 요구할 수 있으므로, 다양한 컴포넌트에서 쉽게 접근할 수 있도록 중앙 상태 저장소인 vuex에서 관리

<img width="1466" alt="vue153" src="https://user-images.githubusercontent.com/86648892/212531326-97067d86-85a4-4417-9411-e45938211b9d.png">

<img width="1469" alt="vue154" src="https://user-images.githubusercontent.com/86648892/212531325-964c9fed-7f52-46b8-98cc-69452116dc80.png">

<img width="1476" alt="vue155" src="https://user-images.githubusercontent.com/86648892/212531324-b67857a8-cdab-4ef5-8d1c-484e2bbcdaa0.png">

<img width="1470" alt="vue156" src="https://user-images.githubusercontent.com/86648892/212531323-f565888a-5deb-442e-bca4-45b2ea11bd99.png">

### 토큰 관리

- 게시물 전체 조회와 달리, 인증 요청의 응답으로 받은 Token은 매번 요청하기 어려움

  - 비밀번호를 항상 보관하고 있을 수는 없음
  - localStorage에 Token 저장을 위해 vuex-persistedstate 활용

    - `npm install vuex-persistedstate`
      <img width="581" alt="vue157" src="https://user-images.githubusercontent.com/86648892/212531321-094b226b-6008-4c18-a941-a98f787271b5.png">

      - User 인증 정보를 localStorage에 저장해도 되는가?
        - 안전한 방법으로 볼 수는 없음
        - 따라서, vuex-persistedstate는 아래의 2가지 방법을 제공
          1. 쿠키를 사용하여 관리
          2. 로컬 저장소를 난독화하여 관리
      - 실습 편의를 위해 localStorage를 사용할 예정

### Login Request

<img width="1479" alt="vue158" src="https://user-images.githubusercontent.com/86648892/212531318-108aaef9-9b52-4226-b0cb-369a73d5a10c.png">

<img width="1440" alt="vue159" src="https://user-images.githubusercontent.com/86648892/212531317-3795288f-9c5e-46d1-960d-f895f0cafe78.png">

<img width="1325" alt="vue160" src="https://user-images.githubusercontent.com/86648892/212531316-7b684498-4513-4292-9c32-236f566a9b57.png">

<img width="1408" alt="vue161" src="https://user-images.githubusercontent.com/86648892/212531315-9c30c665-b6e4-4b5e-b3c3-149045ada130.png">

- signUp과 다른 점은 password1, password2가 password로 바뀐 것 뿐이다
- 요청을 보내고 응답을 받은 Token을 state에 저장하는 것까지도 동일
  - mutations가 처리해야 하는 업무가 동일
  - `SIGN_UP` mutations를 `SAVE_TOKEN` mutations로 대체 가능

<img width="1458" alt="vue162" src="https://user-images.githubusercontent.com/86648892/212531312-77f0b534-8546-49ec-b072-dbaeb397f0c0.png">

<img width="1487" alt="vue163" src="https://user-images.githubusercontent.com/86648892/212531310-5a575316-0a1d-45ab-8188-04df96d643f9.png">

<img width="1470" alt="vue164" src="https://user-images.githubusercontent.com/86648892/212531309-3eab35e8-a4ca-4894-98af-2283cfe0c564.png">

<img width="1488" alt="vue165" src="https://user-images.githubusercontent.com/86648892/212531308-a8471870-7bc5-4302-95bf-63832ed65c65.png">

### IsAuthenticated in Vue

- 회원가입, 로그인 요청에 대한 처리 후 state에 저장된 Toekn을 직접 확인하기 전까지 인증 여부 확인 불가
- 인증되지 않았을 시 게시글 정보를 확인할 수 없으나 이유를 알 수 없음
  - 로그인 여부를 확인할 수 있는 수단이 없음

<img width="1461" alt="vue166" src="https://user-images.githubusercontent.com/86648892/212531306-39a78914-01dd-4b67-ba63-01f1f06f62d5.png">

<img width="1445" alt="vue167" src="https://user-images.githubusercontent.com/86648892/212531304-a448d9f2-fdd3-4c60-834e-4b3e1a9b046b.png">

<img width="1453" alt="vue168" src="https://user-images.githubusercontent.com/86648892/212531303-879d72f3-ed18-45b4-a778-2cbb333c0412.png">

<img width="1488" alt="vue169" src="https://user-images.githubusercontent.com/86648892/212531302-b3a3bf46-b056-4721-8712-52b756dd9c01.png">

### 로그인 후 Articles에서는?

- 인증은 받았지만 게시글 조회 시 인증 정보를 담아 보내고 있지 않음
  <img width="1209" alt="vue170" src="https://user-images.githubusercontent.com/86648892/212531300-c9391c4e-6a1e-4092-bb56-724ca549e5fe.png">
  - 원인
    - 로그인은 했으나 Django에서는 로그인한 것으로 인식하지 못함
      - 발급받은 Token을 요청으로 보내지 않았기 때문

### Request with Token

- 인증 여부를 확인하기 위한 Token이 준비되었으니
- headers HTTP에 Token을 담아 요청을 보내면 된다

<img width="1496" alt="vue171" src="https://user-images.githubusercontent.com/86648892/212531298-ae09932d-5267-476a-a57a-1ae2a4e93943.png">

<img width="1303" alt="vue172" src="https://user-images.githubusercontent.com/86648892/212531296-90dfb248-03e3-46c6-a605-378030aefd2a.png">

<img width="1486" alt="vue173" src="https://user-images.githubusercontent.com/86648892/212531295-e97b999f-a7b1-4046-b333-a9aeaee17475.png">

<img width="1292" alt="vue174" src="https://user-images.githubusercontent.com/86648892/212531293-c8d232e3-84ef-4841-88f8-4866c4465a1f.png">

<img width="1495" alt="vue175" src="https://user-images.githubusercontent.com/86648892/212531291-6cf2e3cf-0052-4745-9309-f577037b401f.png">

<img width="1141" alt="vue176" src="https://user-images.githubusercontent.com/86648892/212531290-9914c27a-33ed-4c4b-a0a1-8eb46ad55e6d.png">

<img width="1444" alt="vue177" src="https://user-images.githubusercontent.com/86648892/212531289-88a70c9f-15fb-4be9-8749-45431225901c.png">

<img width="1341" alt="vue178" src="https://user-images.githubusercontent.com/86648892/212531288-eecc5100-b7ca-4bb0-99ae-560061d6b5df.png">

<img width="1421" alt="vue179" src="https://user-images.githubusercontent.com/86648892/212531287-98efe4d4-684d-4b7e-b215-ec055b82b5cb.png">

<img width="1431" alt="vue180" src="https://user-images.githubusercontent.com/86648892/212531286-7d73a7cf-cdfe-43c0-bb73-968e642a4bd7.png">

<img width="1457" alt="vue181" src="https://user-images.githubusercontent.com/86648892/212531284-3b2d91a5-ef70-4a8f-8d19-8d61a69d6280.png">

---

# swagger

- 스웨거(Swagger)는 개발자가 REST 웹 서비스를 설계, 빌드, 문서화, 소비하는 일을 도와주는 오픈 소스 소프트웨어 프레임워크
  - 즉, API를 설계하고 문서화 하는데 도움을 주는 라이브러리

<img width="512" alt="vue182" src="https://user-images.githubusercontent.com/86648892/212531282-6e45f422-815f-44ed-85fe-72c3e3e8af4d.png">

---

# drf-spectacular

### 다양한 DRF API

- 스웨어(Swagger)를 생성할 수 있도록 도움을 주는 라이브러리
- 과거에는 다양한 라이브러리가 있었으나 OpenAPI Specification이 3.0으로 업데이트되며 새 버전을 지원하지 않는 라이브러리들이 있으니 사용시 유의

### drf-spectacular

- Open API 3.0을 지원하는 DRF API OpenAPI 생성기
- 지속적인 업데이트와 관리로 최신 Django, DRF 버전 지원

<img width="925" alt="vue183" src="https://user-images.githubusercontent.com/86648892/212531281-056c2274-9e0e-4cc2-994e-2f9f5d026b1e.png">

<img width="1307" alt="vue184" src="https://user-images.githubusercontent.com/86648892/212531280-a903b9ee-cd2c-40f9-b96c-468cc714e2b4.png">

<img width="1348" alt="vue185" src="https://user-images.githubusercontent.com/86648892/212531278-390ab818-aa77-4f24-9ba8-54f9f4e60672.png">

<img width="1403" alt="vue186" src="https://user-images.githubusercontent.com/86648892/212531275-8ce2fe0f-d7e4-4a5f-a812-0145263cabf9.png">

---
