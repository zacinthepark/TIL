# Vue.js 3

> 하기의 내용들은 Vue 3를 학습하기 위해 사용한 자료이며, 출처는 짐코딩님의 온라인 강의 교안입니다.
>> **[짐코딩 GYM CODING](https://gymcoding.notion.site/Vue-js-3-cd9bb8ec6fec4ba9b388c808caf61880)**

- **준비하기**
  - **[개발환경 구성](#개발환경-구성)**
  - **[Vue란 무엇인가?](#vue란-무엇인가)**
  - **[컴포넌트 이해하기](#컴포넌트-이해하기)**
- **시작하기**
  - **[프로젝트 구성](#프로젝트-구성)**
  - **[ESLint, Prettier](#eslint-prettier)**
  - **[Options API vs Composition API](#options-api-vs-composition-api)**
- **Vue3 Composition API**
  - **[Composition APIs](#composition-apis)**
  - **[Setup Hook](#setup-hook)**
  - **[템플릿 문법 (Template Syntax)](#템플릿-문법-template-syntax)**
  - **[반응형 기초](#반응형-기초)**
  - **[Computed](#computed)**
  - **[클래스와 Style 바인딩](#클래스와-style-바인딩)**
  - **[조건부 렌더링](#조건부-렌더링)**
  - **[목록 렌더링](#목록-렌더링)**
  - **[디렉티브 (directives)](#디렉티브-directives)**
  - **[이벤트 처리](#이벤트-처리)**
  - **[양방향 바인딩](#양방향-바인딩)**
  - **[Watch, WatchEffect](#watch-watcheffect)**
  - **[Dynamic Components](#dynamic-components)**
- **Bootstrap 5**
  - **[Bootstrap 5 설치](#bootstrap-5-설치)**
  - **[프로젝트 만들기](#프로젝트-만들기)**
- **컴포넌트**
  - **[컴포넌트 기초](#컴포넌트-기초)**
  - **[Single-File Component (SFC)](#single-file-component-sfc-1)**
  - **[Props](#props)**
  - **[Events](#events)**
  - **[Non-Prop 속성](#non-prop-속성)**
  - **[Slots](#slots)**
  - **[Provide and Inject](#provide-and-inject)**
  - **[Lifecycle Hooks](#lifecycle-hooks)**
  - **[Template Refs](#template-refs)**
  - **[script setup](#script-setup-1)**
- **Vue-Router**
  - **[Vue-Router란?](#vue-router란)**
  - **[Vue-Router 학습](#vue-router-학습)**
  - **[네비게이션 가드](#네비게이션-가드)**
- **Built-in Components**
  - **[Transition](#transition)**
  - **[TransitionGroup](#transitiongroup)**
  - **[Teleport](#teleport)**
- **재사용성**
  - **[Plugins](#plugins)**
  - **[Custom Directives](#custom-directives)**
  - **[Composables](#composables)**
- **유틸리티**
  - **[toRef, toRefs](#toref-torefs)**
  - **[isRef, unref, isProxy, isReactive, isReadonly](#isref-unref-isproxy-isreactive-isreadonly)**
- **Pinia (Vuex 5)**
  - **[상태관리란?](#상태관리란)**
  - **[Pinia란?](#pinia란)**
  - **[Store 정의](#store-정의)**
  - **[State](#state)**
  - **[Getters](#getters)**
  - **[Actions](#actions)**
  - **[Plugins with Pinia](#plugins-with-pinia)**

# 개발환경 구성

## 크롬 브라우저 설치

---

먼저 HTML/CSS 결과물을 확인 하기 위해서 크롬 브라우저를 설치해 보도록 하겠습니다. 크롬 브라우저는 개발자에게 편리한 다양한 기능을 지원하고 있기 때문에 개발하는 과정에서 편리합니다.

- [크롬 브라우저 설치](https://www.google.co.kr/chrome/?brand=IBEF&gclid=CjwKCAjwz_WGBhA1EiwAUAxIcYR9QVHF878AhQb5i7oQWrsxv9fkePuTxzHlpewgznBosx0VOsW5fRoCSZ4QAvD_BwE&gclsrc=aw.ds)

## Visual Studio Code 설치

---

HTML/CSS 코드를 입력 할 텍스트 에디터 툴인 비주얼 스튜디오 코드 툴을 설치해 보도록 하겠습니다. 여기서 에디터 툴은 쉽게 말하면 메모장이라고 보시면 될 것 같아요.

우리가 정산이나 계산 같은거를 할 때 메모장에 적어놓고 할 수도 있지만! 엑셀로 하면 더 효율적일 거에요! 이렇듯이 HTML/CSS도 메모장으로 코딩할 수 있지만 VSCode와 같은 툴을 이용하면 더 효율적으로 할 수 있습니다.

개발을 위한 툴(도구)! 이라고 보시면 될 것 같아요 😀

- [비주얼 스튜디오 코드 설치](https://code.visualstudio.com/)

## VSCode Plugins 설치

---

HTML/CSS 마크업(코드 입력)을 도와주는 확장 프로그램을 설치해 보도록 하겠습니다! 확장 프로그램은 우리가 **어떤 일**(여기서는 HTML/CSS 코딩)을 **더 효율적으로 작업**할 수 있게 도와줘요!

- `Korean Language Pack`
    
    비주얼 스튜디오 코드 툴을 한국어로 사용할 수 있다.
    
- `Indent-Rainbow`
    
    Tab 영역을 컬러별로 다르게 표시하여 코드라인이 길어 졌을때 읽기 편하게 합니다.
    
- `Auto Rename Tag`
    
    HTML Tag에서 태그 이름을 바꾸면 쌍을 이루는 여는태그 또는 닫는태그 명도 함께 바꿔줍니다.
    
- `CSS Peek`
    
    HTML 문서에서 정의된 CSS를 금방 찾을 수 있도록 도와줌! `ctrl + 클릭` 하면 선언된 곳으로 이동함.
    
- `HTML to CSS autocompletion`
HTML 문서에 선언된 class 명을 .css파일에서 입력할 때 자동완성 기능을 제공합니다.
- `HTML CSS Support`
    
    HTML 문서에서 CSS의 자동완성을 이용할 수 있다.
    
- `Live Server`
    
    HTML 파일 수정 시 새로고침 없이 바로바로 즉각 적용되도록 도와준다.
    
- `ESLint`
    
    코드 검사기로써 에러가 있는지 검사해주는 도구
    
- `Prettier` **사용안함**
    
    코드 포멧터로써 코드를 일관성있고 예쁘게 작성할 수 있도록 도와주는 도구
    

## 설정

---

- `Format On save` **사용안함**

## Vue.js devtools

---

Vue.js 애플리케이션 디버깅을 위한 Chrome 브라우저의 확장 프로그램입니다. (Vue 3 지원 다운로드)

- [Vue.js devtools](https://chrome.google.com/webstore/detail/vuejs-devtools/nhdogjmejiglipccpnnnanhbledajbpd/related)

## Vue.js를 위한 VSCode Plugins

---

- [Volar](https://marketplace.visualstudio.com/items?itemName=johnsoncodehk.volar)
    
    Vue 3용으로 특별히 제작된 언어 지원 플러그인입니다. 
    
    Volar는 Vue 2용 이전 공식 VSCode 확장인 Vetur를 대체합니다. 현재 Vetur가 설치되어 있는 경우 Vue 3 프로젝트에서 비활성화해야 합니다.
    
    [공식홈페이지 참고](https://vuejs.org/guide/typescript/overview.html#ide-support)
    
- [Vue VSCode Snippets](https://marketplace.visualstudio.com/items?itemName=sdras.vue-vscode-snippets)
    
    사용구 코드를 빠르게 타이핑 할 수 있도록 도와주는 플러그인

# Vue란 무엇인가?

## Vue 란?

---

Vue는 User Interface 개발을 위한 자바스크립트 프레임워크 입니다. HTML, CSS, JavaScript를 기반으로 단순 하거나 복잡한 사용자 인터페이스(UI)를 효율적으로 개발하는 데 도움을 줍니다.

우선 빠르게 CDN으로 설치해서 Vue를 경험해보도록 하겠습니다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Hello Vue3</title>
	<script src="https://unpkg.com/vue@next"></script>
</head>
<body>
  <div id="counter">
    <button type="button" v-on:click="counter++">
      Counter: {{ counter }}
    </button>
  </div>
  <script>
    const Counter = {
      data() {
        return {
          counter: 0
        }
      }
    }
    Vue.createApp(Counter).mount('#counter')
  </script>
</body>
</html>
```

위의 예는 Vue의 두 가지 핵심 기능을 보여줍니다.

- **선언적 렌더링**(**Declarative Rendering)** : Vue는 템플릿 구문(`{{ 데이터 }}`)을 활용하여 데이터를 선언적으로 출력(렌더링) 할 수 있도록 합니다.
- **반응성(Reactivity)** : Vue는 JavaScript 상태 변경을 자동으로 추적하고 변경이 발생하면 DOM을 효율적으로 업데이트합니다.

위 예제처럼 Vue를 사용하면 자바스크립트를 사용하는 것보다 빠르게 애플리케이션을 제작할 수 있습니다. 다음은 본격적으로 Vue를 배우기 전에 Vue의 핵심 기능을 빠르게 훓어 보도록 하겠습니다.

## 바인딩(v-bind)

---

템플릿 구문 이외에도 다음과 같은 방법으로 엘리먼트 속성에 **데이터를 바인딩(연결)** 할 수 있습니다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Quickly</title>
  <script src="https://unpkg.com/vue@next"></script>
</head>
<body>
  <div id="app">
    <input type="text" v-bind:placeholder="message">
  </div>
  <script>
    const Counter = {
      data() {
        return {
          message: '텍스트를 입력해주세요'
        }
      }
    }
    Vue.createApp(Counter).mount('#app')
  </script>
</body>
</html>
```

위 예제에서 `v-bind` 속성은 데이터(상태) 속성에 바인딩할 때 사용하는 특수 속성 입니다. 바인딩 된 DOM은 `placeholder` 속성을 Vue 인스턴스의 `message` 속성으로 최신 상태를 유지합니다. (반응형 동작)

그리고 이렇게 `v-` 접두어가 붙은 특수 속성을 **디렉티브(directive)** 라고 합니다.

## 이벤트 핸들링(v-on)

---

사용자가 앱과 상호 작용할 수 있게 하기 위해 `v-on` 디렉티브를 사용하여 Vue 인스턴스의 메소드(methods)를 호출하는 이벤트 리스너를 추가 할 수 있습니다.

```html
<p>{{ message }}</p>
<button type="button" v-on:click="reverseMessage">reverseMessage</button>
```

```jsx
methods: {
  reverseMessage() {
    this.message = this.message
      .split('')
      .reverse()
      .join('')
  }
}
```

이 방법은 직접적으로 DOM(p 엘리먼트)을 건드리지 않고 앱의 상태만 업데이트 합니다. 즉, 모든 DOM의 조작은 Vue에 의해 처리되고 있습니다.

## 양방향 바인딩(v-model)

---

Vue는 양식(`input`, `select` 등)의 입력과 앱의 상태(`data`)를 양방향으로 바인딩하는 `v-model` 디렉티브를 제공합니다.

```html
<p>{{ bindingMessage }}</p>
<input type="text" v-model="bindingMessage" />
```

```jsx
data() {
  return {
    bindingMessage: '파랑색',
  };
},
```

## 조건문

---

엘리먼트 표시여부는 `v-if` 특수 속성(디렉티브)으로 제어할 수 있습니다. 

```html
<p v-if="visible">보이나요?</p>
<button type="button" v-on:click="visible = true">visible</button>
```

```jsx
data() {
  return {
    visible: false,
  };
},
```

## 반복문

---

`v-for`는 배열에서 데이터를 가져와 아이템 목록을 표시하는데 사용할 수 있습니다.

```html
<ul>
  <li v-for="todo in todos">{{ todo }}</li>
</ul>
```

```jsx
data() {
  return {
    todos: ['사과', '딸기', '포도'],
  };
},
```

## 참고

---

- Vue3
    
    [Vue.js - The Progressive JavaScript Framework | Vue.js](https://vuejs.org/)
    
- Vue3 설치 (한글)
    
    [설치방법 | Vue.js](https://v3.ko.vuejs.org/guide/installation.html)

# 컴포넌트 이해하기

## 학습목표

---

이번 시간에는 일반 HTML로 작성된 문서를 Vue로 변환해가며 컴포넌트를 사용하면 어떤점이 좋은지 알아보도록 하겠습니다.

- 컴포넌트란 무엇인가? (What)
- 컴포넌트를 왜 사용하는가? (Why)
- 컴포넌트를 어떻게 사용하는가? (How)
    - `컴포넌트 정의` → `컴포넌트 등록` → `컴포넌트 사용`
- 컴포넌트 시스템이란?

## 컴포넌트 (Component)

---

자바스크립트에서 재사용할 수 있도록 코드를 분리한 파일을 **모듈** 이라고 하는데요. Vue에서도 마찬가지로 **UI(HTML, CSS, JS)를 재사용할 수 있도록 정의한 것** 을 **컴포넌트** 라고합니다.

<aside>
💡 JavaScript 코드를 재사용하는 모듈과 다르게, 컴포넌트는 JavaScript 뿐만아니라 HTML, CSS도 함께 캡슐화하여 재사용이 가능하게 합니다.
</aside>

### 컴포넌트를 사용하는 이유

- 컴포넌트를 사용하면 UI를 재사용 할 수 있습니다.
→ 프론트엔드 개발을 하다보면 JavaScript 뿐만 아니라 HTML, CSS를 반복적으로 사용할 때가 있습니다. 이런경우 컴포넌트로 캡슐화 한 후 필요한 곳에서 사용할 수 있습니다.
- 컴포넌트를 사용하여 UI를 독립적으로 나눔으로써(레이아웃 등) 코드를 클린하게 할 수 있습니다.
→ 프론트엔드 개발을 하다보면 코드가 길어져 유지보수가 힘들 수 있습니다. 이런경우 컴포넌트로 독립적으로 분리함으로써 코드를 클린하게 하여 유지보수를 보다 쉽게할 수 있습니다.

### 컴포넌트 만들기

컴포넌트를 만들고 사용하는 단계를 3가지 단계로 나누고 간단히 설명해보도록 하겠습니다.

`컴포넌트 정의` → `컴포넌트 등록` → `컴포넌트 사용`

## 컴포넌트 정의

---

컴포넌트 **어떤 방법으로 정의** 하느냐에 따라 `문자열 템플릿`, `Single File Component` 두 가지 방법이 있습니다.

### **문자열 템플릿 (string template)**

```jsx
// BookComponent.js 파일
export default {
  data() {
    return {
      subtitle: '도서명'
    }
  },
  template: `
    <article class="book">
      <div class="book__subtitle">{{ subtitle }}</div>
      <div class="book__title">
        HTML 강좌
      </div>
    </article>
  `
}
```

### **Single File Component (SFC)**

자바스크립트로 복잡한 프로젝트를 개발한다면 다음과 같은 어려움이 존재한다.

- **문자열 템플릿**은 가독성이 떨어지고 예쁘지 않습니다.
- `.js` 는 HTML과 JavaScript는 모듈화 할 수있지만 CSS는 빠져있습니다.
- 또 다른 문제점은 [공식문서](https://v3.ko.vuejs.org/guide/single-file-component.html#%E1%84%89%E1%85%A9%E1%84%80%E1%85%A2)에서 확인 가능합니다.

이 모든 문제는를 해결하기 위해 Vue.js는 Webpack, Browserify, Vite와 같은 빌드 도구를 활용하여 `.vue` 확장자를 가진 `Single File Component(SFC)`를 사용합니다.

SFC는 `template`, `script`, `style` 크게 세 가지로 구성되어 있습니다.

```jsx
// BookComponent.vue 파일
<template>
  <article class="book">
    <div class="book__subtitle">{{ subtitle }}</div>
    <div class="book__title">
      HTML 강좌
    </div>
  </article>  
</template>

<script>
export default {
  data() {
    return {
      subtitle: '도서명'
    }
  },
}
</script>

<style scoped>
</style>
```

<aside>
💡 실무에서는 문자열 템플릿 대신 Single File Component를 사용하고 있습니다.

</aside>

### 컴포넌트 등록

컴포넌트를 **어디에서 사용하냐**에 따라 두 가지 등록 방법이 있습니다.

- **전역 등록 (Global Registration)**
    
    `app.component`를 이용해서 컴포넌트를 등록하면, 컴포넌트는 애플리케이션 **전역 등록**이 되어 모든 컴포넌트 인스턴스의 템플릿 내부에서 사용할 수 있습니다.
    
    ```jsx
    const app = createApp({ ... })
    app.component('BookComponent', BookComponent)
    ```
    
- **지역 등록 (Local Registration)**
    
    전역 등록은 보통 이상적이지 않습니다. 예를 들어 Webpack과 같은 빌드 시스템을 사용하는 경우 컴포넌트를 전역 등록 하게 되면 컴포넌트를 사용하지 않더라도 계속해서 최종 빌드에 해당 컴포넌트가 포함되는 것을 의미합니다. 이는 사용자가 다운로드하는 자바스크립트 파일의 크기를 불필요하게 증가시킵니다.
    
    Vue 인스턴스의 `components` 속성 안에 정의 하세요. 그러면 해당 Vue 인스턴스에서 지역 등록된 컴포넌트를 사용할 수 있습니다.
    
    ```jsx
    const app = createApp({
    	components: {
    		BookComponent: BookComponent
    	}
    })
    ```
    

### 컴포넌트 사용

컴포넌트는 `template`에서 사용할 수 있습니다.

```jsx
<BookComponent></BookComponent>
<book-component></book-component> 
```

- `PascalCase`로 등록 된 컴포넌트는 `PascalCase`, `kebab-cased` 둘 다 사용 가능합니다.
- kebab-cased로 등록 된 컴포넌트는 `kebab-cased` 로만 사용 가능합니다.

> **컴포넌트 네이밍 룰**
> 

컴포넌트를 사용할 때 `PascalCased`를 권장합니다. `PascalCased`를 사용하면 다음과 같은 이점이 있습니다.

1. `PascalCased` 이름은 유효한 JavaScript 식별자입니다. 이렇게 하면 JavaScript에서 구성 요소를 더 쉽게 가져오고 등록할 수 있습니다. IDE의 자동 완성 기능도 지원합니다.
2. `<PascalCase />`이것은 템플릿의 기본 HTML 요소가 아닌 Vue 구성 요소라는 것을 더 분명하게 만듭니다. 또한 Vue 구성 요소를 사용자 정의 요소(웹 구성 요소)와 구별합니다.

`SFC`, `string template` 에서 `PascalCase`를 사용 가능하며 `DOM Template`에서는 `kebab-case`를 사용해야 합니다.

[Component Registration | Vue.js](https://vuejs.org/guide/components/registration.html)

## 컴포넌트 시스템

---

컴포넌트 시스템은 Vue의 또 다른 중요한 개념입니다. 이는 작고 독립적이며 재사용할 수 있는 컴포넌트로 구성된 대규모 애플리케이션을 구축할 수 있게 해주는 추상적 개념입니다. 생각해보면 거의 모든 유형의 애플리케이션 인터페이스를 컴포넌트 트리로 추상화할 수 있습니다.

- 작은 의미 재사용 가능한 컴포넌트
- 넓은 의미 모든 Vue 인스턴스는 컴포넌트이다.

쉽게 말해서 Vue는 컴포넌트로 구성된 애플리케이션이다 라고 보셔도 될 만큼 중요하다라는 뜻입니다.

![components](https://user-images.githubusercontent.com/86648892/226257448-685862b8-0d74-4365-a201-ed528c426f7c.png)

# 프로젝트 구성

## Vue 설치방법

---

Vue를 설치할 수 있는 방법은 크게 3가지가 있습니다. 

- 페이지에 **CDN** package로 import 하기
- **npm**을 사용하여 import 하기
- 공식 **CLI**를 사용하여 프로젝트를 scaffold하고, 최신 프론트엔드 워크플로우(예. hot-reload, lint-on-save 등)를 위한 batteries-included build를 제공합니다.

<aside>
💡 scaffold : 개발을 용이하기 시작할 수 있는 발판을 제공해주는 것

**batteries-included** : 외부 라이브러리를 더하지 않아도 기본적으로 제공하는 표준 라이브러리만으로도 시작하는데 문제 없다는 의미로 해석할 수 있습니다.

</aside>

### CDN

프로토타이핑 또는 학습 목적이라면, 아래 코드로 최신 버전을 사용할 수 있습니다.

```html
<script src="https://unpkg.com/vue@next"></script>
<!-- 또는 -->
<script src="https://unpkg.com/vue@3.2.31"></script>
```

### npm

Vue를 사용하여 대규모 애플리케이션을 구축할 때 NPM를 이용한 설치를 권장하고 있습니다. NPM은 Webpack 또는 Browserify와 같은 모듈 번들러와 잘 작동합니다.

```bash
npm install vue@next
```

### Vue CLI

Vue CLI는 웹팩 기반 빌드도구 입니다. 하지만 Vue CLI는 현재 유지관리 모드에 있습니다. 특정 웹팩 기능에 의존하지 않는한 Vite로 새 프로젝트를 시작하는 것이 좋습니다.

Vue CLI를 사용하기 위해서는 `@vue/cli` v4.5 이상의 버전을 설치해야 합니다.

```bash
npm install -g @vue/cli
```

- [Vue CLI에서 Vite로 마이그레이션하는 방법 정보](https://vuejs.org/guide/scaling-up/tooling.html#project-scaffolding)

### Vite

[Vite(비트)](https://github.com/vitejs/vite)는 Vue SFC를 지원하고 매우 가볍고 빠른 빌드 도구입니다. Vue!의 저자이기도 한 Evan You가 만들었습니다!

Vite는 개발 서버를 구동할 때 매우 빠릅니다. 그리고 소스 코드의 변경이 일어났을 때 전체 모듈을 번들링 하는게 아니라 변경된 모듈만 교체하기 때문에 개발을 더욱더 빠르게 진행할 수 있습니다.

그러면 vite로 프로젝트를 구성해 보도록 하겠습니다.

```bash
npm init vue@latest
```

```bash
cd {product name}
npm install
npm run dev
```

이 명령은 공식 Vue 프로젝트 스캐폴딩 도구인 [create-vue 를 설치하고 실행합니다.](https://github.com/vuejs/create-vue)

- Vite에 대해 자세히 알아보려면 [Vite 문서](https://vitejs.dev/)를 확인하세요 .
- Vite 프로젝트에서 Vue 관련 동작을 구성하려면(예: Vue 컴파일러에 옵션 전달) [@vitejs/plugin-vue](https://github.com/vitejs/vite/tree/main/packages/plugin-vue#readme)

## 참고

---

- **Vue Project Scaffolding**

# ESLint, Prettier

## 프로젝트 구조

```bash
├── node_modules
│		└── ...
├── public
│   └── favicon.ico
├── src
│   ├── App.vue
│   ├── assets
│   │   ├── base.css
│   │   └── logo.svg
│   ├── components
│   │   ├── HelloWorld.vue
│   │   ├── TheWelcome.vue
│   │   ├── WelcomeItem.vue
│   │   └── icons
│   │       ├── IconCommunity.vue
│   │       ├── IconDocumentation.vue
│   │       ├── IconEcosystem.vue
│   │       ├── IconSupport.vue
│   │       └── IconTooling.vue
│   └── main.js
├── index.html
├── package-lock.json
├── package.json
├── README.md
└── vite.config.js
```

## 설명

### `vite.config.js`

Vite 명령어로 dev 서버를 실행할 때 프로젝트 루트의 `vite.config.js` 파일 확인을 시도합니다. 그리고 내부에 설정된 값을 참고합니다.

```bash
import { fileURLToPath, URL } from 'url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
})
```

- `alias` : 파일 시스템의 경로에 별칭을 만들 때 사용합니다. 미리 설정된 `‘@’` 기호를 통하여 `‘./src’` 디렉토리에 절대경로로 쉽게 접근할 수 있습니다.

### `package.json`

`npm` 으로 관리하기 위한 프로젝트 정보를 갖고 있는 파일

## ESLint, Prettier

- `ESLint` : [ESLint](https://eslint.org/)는 코드 검사기로 코드에 에러가 있는지 검사해주 도구 입니다.
- `Prettier` : [Prettier](https://prettier.io/)는 코드 포매터로 코드를 일관성있고 예쁘게 정렬해 주는 도구입니다.

현업에서는 대부분 ESLint와 Prettier를 함께 사용하고 있습니다.

### `.eslintrc.cjs`

```jsx
/* eslint-env node */
require("@rushstack/eslint-patch/modern-module-resolution");

module.exports = {
  "root": true,
  "extends": [
    "plugin:vue/vue3-essential",
    "eslint:recommended",
    "@vue/eslint-config-prettier"
  ],
  "env": {
    "vue/setup-compiler-macros": true
  }
}
```

- `plugin:vue/vue3-essential`
    
    [Available rules | eslint-plugin-vue](https://eslint.vuejs.org/rules/#priority-a-essential-error-prevention-for-vue-js-3-x)
    
- `eslint:recommended`
    
    ✔️ 표시된 항목을 자동으로 검사해주는 옵션
    
    [List of available rules](https://eslint.org/docs/rules/)
    
- `@vue/eslint-config-prettier`
    
    불필요한 규칙이나 eslint와 prettier와 출동할 수 있는 규칙을 끄는 출동 방지용 패키지 입니다.
    
    Vue용 [eslint-config-prettier](https://github.com/prettier/eslint-config-prettier)
    
    이 구성은 @vue/cli 및 create-vue 설정에서 사용하도록 특별히 설계되었습니다.
    
    [@vue/eslint-config-prettier](https://www.npmjs.com/package/@vue/eslint-config-prettier)
    

```jsx
/* eslint-env node */
require('@rushstack/eslint-patch/modern-module-resolution');

module.exports = {
	root: true,
	extends: [
		'plugin:vue/vue3-essential',
		'eslint:recommended',
		'@vue/eslint-config-prettier',
	],
	env: {
		'vue/setup-compiler-macros': true,
	},
	rules: {
		'no-console': process.env.NODE_ENV === 'production' ? 'error' : 'off',
		'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off',
		'prettier/prettier': [
			'error',
			{
				singleQuote: true,
				semi: true,
				useTabs: true,
				tabWidth: 2,
				trailingComma: 'all',
				printWidth: 80,
				bracketSpacing: true,
				arrowParens: 'avoid',
				endOfLine: 'auto', // 한줄 추가
			},
		],
	},
};
```

## VSCode 에서 ESLint 기반으로 Format On Save 설정하기

```jsx
// settings.json
{
    "eslint.validate": [
        "javascript",
        "javascriptreact",
        "typescript",
        "typescriptreact",
        // "html",  // 삭제
        "vue",
        "markdown"
    ],
    "editor.codeActionsOnSave": {
        "source.fixAll.eslint": true
    },
    "editor.tabSize": 2,
}
```

- `eslint.validate`
    
    검사해야 하는 언어를 ESLint 확장에 알려줍니다.
    
- `editor.codeActionsOnSave`
    
    VS Code의 저장 이벤트에 대한 훅입니다.
    
- `source.fixAll.eslint`
    
    저장 중인 파일의 문제를 수정하라는 메시지가 표시됩니다.
    

## Rule

## 참고

- **공식 홈페이지 (ko)**
    
    [스타일 가이드 | Vue.js](https://v3.ko.vuejs.org/style-guide/#%E1%84%80%E1%85%B2%E1%84%8E%E1%85%B5%E1%86%A8-%E1%84%87%E1%85%A5%E1%86%B7%E1%84%8C%E1%85%AE)
    
- **공식 홈페이지 (en)**
    
    [Style Guide | Vue.js](https://vuejs.org/style-guide/)
    
- **ESLint VSCode format on save**

# Options API vs Composition API

Vue3에서 애플리케이션을 만들 수 있는 방법은 크게 두 가지가 있습니다. 하나는 Vue2에서 사용해왔던 Options API를 사용하는 방법과 다른 하나는 Vue3에서 새롭게 등장한 Composition API 입니다.

결론적으로 말씀 드리면 Vue2에서는 Options API의 단점을 보완하기 위해 Composition API 등장했으며, Vue3에서는 Composition API 권장하고 있기 때문에 제 수업에서는 Composition API를 기준으로 수업을 진행할 예정입니다.

이번 시간에는 Vue 프레임워크를 처음 경험하신 분들을 위하여 Options API가 어떻게 생겼고 또 Composition API와 어떻게 다른지 또 Composition API란 무엇인지 살펴보도록 하겠습니다.

## Options API vs Composition API 비교

OptionsAPI와 Composition API가 코드상으로 어떠게 다른지 간단히 살펴보도록 하겠습니다.

### Options API

```jsx
<template>
	<div>
		<button @click="increment">Counter: {{ counter }}</button>
	</div>
</template>

<script>
export default {
	data() {
		return {
			counter: 0,
		};
	},
	methods: {
		increment() {
			this.counter++;
		},
	},
	mounted() {
		console.log('애플리케이션이 마운트 되었습니다!');
	},
};
</script>

<style lang="scss" scoped></style>
```

### Composition API

```jsx
<template>
	<div>
		<button>Counter: {{ counter }}</button>
	</div>
</template>

<script>
import { onMounted, ref } from 'vue';

export default {
	setup() {
		const counter = ref(0);

		const increment = () => counter.value++;

		onMounted(() => {
			console.log('애플리케이션이 마운트 되었습니다!');
		});

		return {
			counter,
			increment,
		};
	},
};
</script>

<style lang="scss" scoped></style>
```

- **Options API**는 `data`, `methods`, `mounted` 와 같은 옵션을 사용합니다.
- **Composition API**는 반응형 코드를 작성하는 단일 `setup` 함수가 있습니다.

## Composition API란?

Composition API는 옵션(`data`, `methods`, `...`)을 선언하는 대신 가져온 함수(`ref`, `onMounted`, `...`)를 사용하여 Vue 컴포넌트를 작성할 수 있는 API 세트를 말합니다.

- **Vue3 API Reference**
    
    [API Reference | Vue.js](https://vuejs.org/api/)
    

## [왜 Composition API인가?](https://vuejs.org/guide/extras/composition-api-faq.html#better-logic-reuse)

### Composition API 등장배경

아래 컴포넌트는 **Options API**로 작성되었습니다.

```jsx
export default {
  data() {
    return {
      counter: 0,
      books: [],
    };
  },
  methods: {
    increment() {
      this.counter++;
    },
    addBook(title, author) {
      this.books.push({ title, author });
    },
  },
  computed: {
    firstBook() {
      return this.books[0];
    }
  }
  mounted() {
    console.log('애플리케이션이 마운트 되었습니다!');
  },
};
```

위 Options API 코드를 보면 동일한 논리적 관심사(book, counter)를 처리하는 코드가 파일의 다른 부분에 분산되어 있어 코드를 분석하기가 매우 힘듭니다. 만약 코드가 더 복합하고 길어질 경우 파일을 위아래로 스크롤해야 하기 때문에 더 이해하기 힘든 상황이 옵니다.

또한 특정 논리적 관심사 로직을 유틸로 추출하려는 경우 분산되어 있는 코드조각을 찾아 추출하는 데 상당한 작업이 필요합니다.

다음은 **Composition API**로 작성한 결과입니다.

```jsx
<script setup>
import { onMounted, reactive, ref } from 'vue';

const counter = ref(0);
const increment = () => {
  counter.value++;
};

const books = reactive([]);
const addBook = (title, author) => {
  books.push({ title, author });
};

onMounted(() => {
  console.log('애플리케이션이 마운트 되었습니다!');
});
</script>
```

Composition API를 사용하면 동일한 논리적 관심사 코드가 그룹화 되어 코드를 분석하기도 쉽고 유지보수가 용이해집니다. 또한 논리적 관심사 코드를 외부 유틸 파일로 추출하기가 쉽습니다.

### 코드 재사용성

Composition API의 가장 큰 장점은 **[Composable 함수](https://vuejs.org/guide/reusability/composables.html)** 의 형태로 로직의 재사용이 가능하다는 것입니다. Options API의 기본 로직 재사용 메커니즘인 Mixins의 모든 단점을 해결합니다.

Composition API의 재사용 기능은 계속해서 증가하는 구성 가능한 유틸리티 모음인 [**VueUse**](https://vueuse.org/) 와 같은 인상적인 커뮤니티 프로젝트를 탄생시켰습니다. 또한 **[immutable data](https://vuejs.org/guide/extras/reactivity-in-depth.html#immutable-data)** , **[state machines](https://vuejs.org/guide/extras/reactivity-in-depth.html#state-machines)** , **[RxJS](https://vueuse.org/rxjs/readme.html#vueuse-rxjs)** 와 같은 상태 저장 타사 서비스 또는 라이브러리를 Vue의 **반응성 시스템(Reactivity system)** 에 쉽게 통합하기 위한 깨끗한 메커니즘 역할을 합니다.

- **Compositions API는 Options API가 가지고 있던 2가지 주요 제한 사항을 해결합니다.**
    - **hook** 을 사용하여 관련 **코드 조각을 함께 그룹화** 합니다.
    - **Composables** 을 사용하면 애플리케이션 전체에서 **코드를 매우 쉽게 재사용** 할 수 있습니다.

### TypeScript

### ****Smaller Production Bundle and Less Overhead****

## [Options API와 관계](https://vuejs.org/guide/extras/composition-api-faq.html#does-composition-api-cover-all-use-cases)

### **Composition API로 기존 모든 사용 사례를 커버 가능?**

Composition API를 사용할 때 여전히 필요할 수 있는 몇 가지 옵션(`props`, `emits`, `name` 및 `inheritAttrs`)이 있습니다. `<script setup>`을 사용하는 경우 `inheritAttrs` 옵션이 필요할 수 있는 유일한 옵션입니다.

### 두 API를 함께 사용할 수 있습니까?

네. Options API 구성 요소의 `setup()` 옵션을 통해 Composition API를 사용할 수 있습니다.

그러나 기존 옵션 API 코드베이스가 있는 경우에만 그렇게 하는 것이 좋습니다. (예를 들어 Composition API로 작성된 외부 라이브러리와 통합해야 하는 경우)

### Options API가 deprecated 될 예정인가요?

아니요, 그렇게 할 계획이 없습니다. Options API는 Vue의 필수적인 부분이며 많은 개발자들이 Vue를 좋아하는 이유입니다. 또한 합성 API의 많은 이점은 대규모 프로젝트에서만 나타나고 옵션 API는 복잡도가 낮거나 중간인 많은 시나리오에 대한 확실한 선택으로 남아 있습니다.

## 참고

- Composition API FAQ
    
    [Composition API FAQ | Vue.js](https://vuejs.org/guide/extras/composition-api-faq.html#why-composition-api)
    
- Playground
    
    [Vue SFC Playground](https://sfc.vuejs.org/#eyJBcHAudnVlIjoiPHNjcmlwdD5cbmltcG9ydCB7IHJlZiB9IGZyb20gJ3Z1ZSdcbmV4cG9ydCBkZWZhdWx0IHtcbiAgc2V0dXAoKSB7XG4gICAgY29uc3QgbWVzc2FnZSA9IHJlZignSGVsbG8gV29ybGQhJylcbiAgICBmdW5jdGlvbiByZXZlcnNlTWVzc2FnZSgpIHtcbiAgICAgIG1lc3NhZ2UudmFsdWUgPSBtZXNzYWdlLnZhbHVlLnNwbGl0KCcnKS5yZXZlcnNlKCkuam9pbignJylcbiAgICB9XG4gICAgZnVuY3Rpb24gbm90aWZ5KCkge1xuICAgICAgYWxlcnQoJ25hdmlnYXRpb24gd2FzIHByZXZlbnRlZC4nKVxuICAgIH1cbiAgICByZXR1cm4ge1xuICAgICAgbm90aWZ5LFxuICAgICAgcmV2ZXJzZU1lc3NhZ2UsXG4gICAgICBtZXNzYWdlXG4gICAgfVxuICB9XG59XG48L3NjcmlwdD5cblxuPHRlbXBsYXRlPlxuICA8aDE+e3sgbWVzc2FnZSB9fTwvaDE+XG4gIDxidXR0b24gQGNsaWNrPVwicmV2ZXJzZU1lc3NhZ2VcIj5SZXZlcnNlIE1lc3NhZ2U8L2J1dHRvbj5cbiAgPGJ1dHRvbiBAY2xpY2s9XCJtZXNzYWdlICs9ICchJ1wiPkFwcGVuZCBcIiFcIjwvYnV0dG9uPlxuICA8YSBocmVmPVwiaHR0cHM6Ly92dWVqcy5vcmdcIiBAY2xpY2sucHJldmVudD1cIm5vdGlmeVwiPlxuICAgIEEgbGluayB3aXRoIGUucHJldmVudERlZmF1bHQoKVxuICA8L2E+XG48L3RlbXBsYXRlPlxuXG48c3R5bGU+XG5idXR0b24sIGEge1xuICBkaXNwbGF5OiBibG9jaztcbiAgbWFyZ2luLWJvdHRvbTogMWVtO1xufVxuPC9zdHlsZT4iLCJpbXBvcnQtbWFwLmpzb24iOiJ7XG4gIFwiaW1wb3J0c1wiOiB7XG4gICAgXCJ2dWVcIjogXCJodHRwczovL3NmYy52dWVqcy5vcmcvdnVlLnJ1bnRpbWUuZXNtLWJyb3dzZXIuanNcIlxuICB9XG59IiwiQXBwT3B0aW9uc0FQSS52dWUiOiIifQ==)
    
- API Examples
    
    [Examples | Vue.js](https://vuejs.org/examples/#hello-world)
    
- [v3.ko.vuejs.org](http://v3.ko.vuejs.org) (한글)
    
    [라이프사이클 훅 | Vue.js](https://v3.ko.vuejs.org/api/options-lifecycle-hooks.html)

# Composition APIs

## Composition API

Composition API는 옵션(`data`, `methods`, `...`)을 선언하는 대신 가져온 함수(`ref`, `onMounted`, `...`)를 사용하여 Vue 컴포넌트를 작성할 수 있는 API 세트를 말합니다.

다음은 Composition API에서 각각의 API(`ref`, `onMounted`, `...`)들을 포괄하는 용어 입니다.

- **반응형 API** (**Reactivity API)**
    
    예를 들어 `ref()`, `reactive()`와 같은 API를 사용하여 `reactive state(반응 상태)`, `computed state(계산된 상태)`, `watchers(감시자)`와 같은 것들을 만들 수 있습니다. 
    
- **[라이프 사이클 훅](https://vuejs.org/guide/essentials/lifecycle.html#lifecycle-diagram)** (**Lifecycle Hooks)**
    
    예를 들어 `onMounted()`, `onUnmounted()`와 같은 API를 사용하여 프로그래밍 방식으로 컴포넌트 라이프사이클에 접근할 수 있습니다.
    
    쉽게 말해서 라이프사이클 특정 시점에 이러한 함수로 코드를 삽입할 수 있습니다.
    
- **종속성 주입** (**Dependency Injection)**
    
    예를 들어 `provide()`와 `inject()`는 Reactivity API를 사용하는 동안 Vue의 의존성 주입 시스템을 활용할 수 있게 해줍니다.
    

[API Reference | Vue.js](https://vuejs.org/api/)

## 반응형 API (**Reactivity API)**

반응형 API는 말 그대로 반응하는 데이터와 관련된 API 세트라고 보시면 될 것 같습니다.

예를 들어 `ref()`, `isRef()`

```jsx
<template>
  <div>
    <h2>반응형</h2>
    <p>{{ reactiveMessage }}</p>
    <button v-on:click="addReactiveMesssage">Add message</button>
    <h2>일반</h2>
    <p>{{ normalMessage }}</p>
    <button v-on:click="addNormalMesssage">Add message</button>
  </div>
</template>

<script>
import { isRef, onUpdated, ref } from 'vue';

export default {
  setup() {
    // 반응형 상태 선언
    const reactiveMessage = ref('Reactive Message');
    // 일반 변수 선언
    let normalMessage = 'Normal Message';

    console.log('isRef(reactiveMessage): ', isRef(reactiveMessage)); // true
    console.log('isRef(normalMessage): ', isRef(normalMessage)); // false

    const addReactiveMesssage = () => {
      reactiveMessage.value = reactiveMessage.value + '!';
    };
    const addNormalMesssage = () => {
      normalMessage = normalMessage + '!';
    };

    onUpdated(() => {
      console.log('update component');
    });

    return {
      reactiveMessage,
      normalMessage,
      addReactiveMesssage,
      addNormalMesssage,
    };
  },
};
</script>

<style lang="scss" scoped></style>
```

## 라이프 사이클 훅 (**Lifecycle Hooks)**

### 라이프 사이클

Vue 인스턴스나 컴포넌트가 생성될 때, 미리 사전에 정의된 몇 단계의 과정을 거치게 되는데 이를 **라이프사이클(Lifecycle)** 이라 합니다.

쉽게 말해, Vue 인스턴스가 생성된 후 우리 눈에 보여지고, 사라지기까지의 단계를 말합니다.

Vue 인스턴스는 크게 생성(create)되고, DOM에 부착(mount)되고, 업데이트(update)되며, 없어지는(destroy) 4가지 과정을 거치게 됩니다.

`create` → `mount` → `update` → `destroy`

[Lifecycle Hooks | Vue.js](https://vuejs.org/guide/essentials/lifecycle.html#lifecycle-diagram)

### 라이프사이클 훅

라이프사이클 단계에서 실행되는 함수를 라이프사이클 훅이라고 부른다.

[Composition API: Lifecycle Hooks | Vue.js](https://vuejs.org/api/composition-api-lifecycle.html)

# Setup Hook

## Setup

`setup()` 함수(hook)는 Composition API 사용을 위한 진입점 역할을 합니다.

그리고 `setup` 함수는 컴포넌트 인스턴스가 생성되기 전에 실행됩니다.

- 라이프사이클 이미지
    
    
    ![lifecycle.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7c8e4caa-b9e6-42ca-acc6-df7ea52c91d5/lifecycle.png)
    

## 기본 사용

**반응형 API(Reactivity API)**를 사용하여 반응형 상태를 선언하고 `setup()`에서 객체를 반환하여 `<template>`에 노출할 수 있습니다. 반환된 객체의 속성은 구성 요소 인스턴스에서도 사용할 수 있습니다(다른 옵션이 사용되는 경우):

```jsx
<script>
import { ref } from 'vue'

export default {
  setup() {
    const count = ref(0)

    // 템플릿 및 기타 Options API hook에 노출
    return {
      count
    }
  },
  mounted() {
    console.log(this.count) // 0
  }
}
</script>

<template>
  <button @click="count++">{{ count }}</button>
</template>
```

## Props 접근

`setup` 함수의 첫 번째 매개변수는 `props` 입니다. `props`는 **반응형** 객체입니다.

```jsx
export default {
  props: {
    title: String
  },
  setup(props) {
    console.log(props.title)
  }
}
```

`props` 객체를 구조 분해 할당을 하면 반응성을 잃게 됩니다. 따라서 항상 `props.xxx` 형식으로 `props`에 액세스하는 것이 좋습니다.

**toRef, toRefs**

만약 `props`의 반응성을 유지하면서 구조 분해 할당을 해야 한다면(예: 외부 함수에 prop을 전달해야 하는 경우) `toRefs()` 및 `toRef()` 유틸리티 API를 사용하여 이를 수행할 수 있습니다.

```jsx
import { toRefs, toRef } from 'vue'

export default {
  setup(props) {
    // turn `props` into an object of refs, then destructure
    const { title } = toRefs(props)
    // `title` is a ref that tracks `props.title`
    console.log(title.value)

    // OR, turn a single property on `props` into a ref
    const title = toRef(props, 'title')
  }
}
```

## Setup Context

`setup` 함수에 전달된 두 번째 매개변수는 **Setup Context** 객체입니다. 컨텍스트 객체는 `setup` 함수내에서 유용하게 사용할 수 있는 속성을 갖고 있습니다.

```jsx
export default {
  setup(props, context) {
    // 속성($attrs와 동일한 비반응형 객체)
    console.log(context.attrs)

    // 슬롯($slots에 해당하는 비반응성 개체)
    console.log(context.slots)

    // 이벤트 발생($emit에 해당하는 함수)
    console.log(context.emit)

    // Public한 속성, 함수를 외부에 노출시에 사용
    console.log(context.expose)
  }
}
```

컨텍스트 객체는 반응형이 아니며 안전하게 구조 분해 할당을 할 수 있습니다.

```jsx
export default {
  setup(props, { attrs, slots, emit, expose }) {
    ...
  }
}
```

**attrs, slots**

`attrs`와  `slots`은 컴포넌트 자체가 업데이트될 때 항상 업데이트되는 상태 저장 객체입니다. 이러한 것들은 구조 분해 할당을 피해야 하며 항상 속성을 `attrs.x` 또는 `slot.x`로 접근해야 한다는 것을 의미합니다. 또한 `props`와 달리 `attrs`과 `slots`의 속성은 반응형이지 않습니다. `attrs` 또는 `slots` 변경에 따라 다른 작업을 하려고 하는 경우 `onBeforeUpdate` **라이프사이클 훅** 내에서 수행할 수 있습니다.

### 공공 자산 노출

`expose`은 **[template refs](https://vuejs.org/guide/essentials/template-refs.html#ref-on-component)(템플릿 참조)** 를 통해 상위 컴포넌트에서 컴포넌트의 인스턴스에 접근할 때 노출되는 속성을 명시적으로 제한하는 데 사용할 수 있는 함수입니다.

```jsx
export default {
  setup(props, { expose }) {
    // make the instance "closed" -
    // i.e. do not expose anything to the parent
    expose()

    const publicCount = ref(0)
    const privateCount = ref(0)
    // selectively expose local state
    expose({ count: publicCount })
  }
}
```

## Render 함수 사용

`setup`은 동일한 범위에서 선언된 반응형 상태를 직접 사용할 수 있는 **[render function](https://vuejs.org/guide/extras/render-function.html)** 를 반환할 수도 있습니다.

```jsx
import { h, ref } from 'vue'

export default {
  setup() {
    const count = ref(0)
    return () => h('div', count.value)
  }
}
```

render function을 반환하면 다른 것을 반환할 수 없습니다. 내부적으로는 문제가 되지 않지만 template refs(템플릿 참조)를 통해 이 컴포넌트의 메서드를 상위 컴포넌트에 노출하려는 경우 문제가 될 수 있습니다.

이때 **[expose()](https://vuejs.org/api/composition-api-setup.html#exposing-public-properties)** 를 호출하여 이 문제를 해결할 수 있습니다.

```jsx
import { h, ref } from 'vue'

export default {
  setup(props, { expose }) {
    const count = ref(0)
    const increment = () => ++count.value

    expose({
      increment
    })

    return () => h('div', count.value)
  }
}
```

그러면 template refs(템플릿 참조)를 통해 상위 컴포넌트에서 increment 메서드를 사용할 수 있습니다.

# 템플릿 문법 (Template Syntax)

## 텍스트 보간법

---

데이터 바인딩의 가장 기본형태는 `{{ data }}`(이중 중괄호, 콧수염 괄호)를 사용하는 것입니다. 

- 이중 중괄호를 사용하면 해당 문법은 컴포넌트 인스턴스의 `message` 값으로 대체됩니다.
- `message` 속성이 변경될 때 마다 갱신(반응)됩니다.

```jsx
<template>
  <div>
    <p>문자열 : {{ message }}</p>
  </div>
</template>

<script>
import { ref } from 'vue';

export default {
  setup() {
    const message = ref('안녕하세요');
    return {
      message,
    };
  },
};
</script>

<style lang="scss" scoped></style>
```

`v-once` 디렉티브를 사용하여 데이터가 변경되어도 갱신(반응)되지 않는 일회성 보간을 수행할 수 있습니다.

```html
<p v-once>문자열: {{ message }} </p>
```

## HTML (v-html)

---

이중 중괄호는 데이터를 HTML이 아닌 일반 텍스트로 해석합니다. 실제 HTML을 출력하려면 `v-html` 디렉티브를 사용해야 합니다.

```html
<h2>텍스트: {{ rawHtml }}</h2>
<h2>v-html: <span v-html="rawHtml"></span></h2>
```

> **TIP**

웹사이트에서 임의의 HTML을 동적으로 렌더링하면 **[XSS 취약점 (opens new window)](https://en.wikipedia.org/wiki/Cross-site_scripting)** 으로 쉽게 이어질 수 있고 이는 매우 위험할 소지가 있습니다. HTML 보간법은 반드시 **신뢰할 수 있는 콘텐츠에서만 사용** 하고 **사용자가 제공한 콘텐츠에서는 절대** 사용하면 안 됩니다.
> 

## 속성 바인딩 (v-bind)

---

이중 중괄호는 HTML 속성에 사용할 수 없습니다. 대신 **[v-bind 디렉티브](https://v3.ko.vuejs.org/api/#v-bind)** 를 사용하세요.

```html
<div v-bind:title="dynamicTitle">마우스를 올려보세요.</div>
```

`Boolean 속성` 은 속성 존재 자체가 `참(true)`, `거짓(false)`을 의미하는 속성입니다.

```html
<input type="text" v-bind:disabled="isInputDisabled" />
```

### 단축 표현

`v-bind`는 매우 자주 사용하기 때문에 단축 문법이 있습니다.

```html
<div :title="dynamicTitle">마우스를 올려보세요.</div>
<input type="text" :disabled="isInputDisabled" />
```

`:` 을 사용하여 속성을 바인딩할 수 있습니다. 

### 다중 속성 바인딩

여러 속성을 한번에 바인딩할 수 있습니다.

```jsx
const attrs = {
	id: 'password-id',
	type: 'password',
	placeholder: '비밀번호를 입력해주세요'
}
```

`v-bind`를 **인수 없이 사용** 하여 단일 요소에 바인딩할 수 있습니다.

```jsx
<input v-bind="attrs" />
```

## JavaScript 표현식 사용

Vue에서는 모든 데이터 바인딩 내에서 JavaScript 표현식이 가능합니다.

```jsx
{{ isInputDisabled ? '예' : '아니오' }}
{{ message.split('').reverse().join('') }}
<input type="text" :placeholder="`입력해주세요 ${isInputDisabled}`" />
```

함수도 호출할 수 있습니다.

# 반응형 기초

## 반응형 상태 선언하기

---

JavaScript 객체에서 반응형 상태를 생성하기 위해서는 `reactive()` 함수를 사용할 수 있습니다.

```jsx
import { reactive } from 'vue'

// 반응형 상태
const state = reactive({ count: 0 })
```

컴포넌트 `<template>`에서 반응형 객체를 사용하려면 `setup()`함수에서 **선언하고 리턴** 해야 합니다.

- 반환된 상태는 반응형 객체입니다. 반응형 변환은 "깊습니다”
- 컴포넌트의 `data()`에서 객체를 반환할 때, 이것은 내부적으로 `reactive()`에 의해 반응형으로 만들어집니다.

```jsx
import { reactive } from 'vue'

export default {
  setup() {
    const state = reactive({ count: 0 })

    return {
      state
    }
  }
}
```

```html
<div>{{ state.count }}</div>
```

## ref로 원시값 반응형 데이터 생성하기

---

`reactive()` 함수는 객체타입에만 동작합니다. 그래서 기본타입(number, string, boolean)을 반응형으로 만들고자 할 때  `ref` 메소드를 사용할 수 있습니다.

```jsx
import { ref } from 'vue'

const count = ref(0)
```

`ref` 메서드는 변이가능한(mutable) 객체를 반환합니다. 이 객체 안에는 `value`라는 하나의 속성만 포함하는데요.  `value`값은 `ref()` 메서드에서 매개변수로 받은 값을 갖고 있습니다. 이 객체는 내부의 `value` 값에 대한 반응형 참조(**ref** erence) 역할을 합니다.

```jsx
import { ref } from 'vue'

const count = ref(0)
console.log(count.value) // 0

count.value++
console.log(count.value) // 1
```

### 템플릿에서 사용

템플릿에서 사용할 때는 자동으로 내부 값(`value`)을 풀어내기(Unwrapping) 때문에 `.value`를 추가할 필요없이 사용할 수 있습니다.

```html
<template>
  <div>
    <span>{{ count }}</span>
    <button @click="count ++">카운트 증가</button>
  </div>
</template>

<script>
  import { ref } from 'vue'
  export default {
    setup() {
      const count = ref(0)
      return {
        count
      }
    }
  }
</script>
```

### 반응형 객체의 `ref` Unwarpping

`ref`가 반응형 객체의 속성으로 접근할 때, 자동적으로 내부 값으로 벗겨내서, 일반적인 속성과 마찬가지로 동작합니다. 이때 반응형은 연결되어 있습니다.

```jsx
const count = ref(0)
const state = reactive({
  count
})
count.value++
console.log(count.value) // 1
console.log(state.count) // 1
```

### **배열 및 컬렉션의 참조 Unwarpping**

반응형 객체와 달리 `ref`가 반응형 배열 또는 `Map`과 같은 기본 컬렉션 타입의 요소로 접근될 때 수행되는 래핑 해제가 없습니다.

```jsx
const books = reactive([ref('Vue 3 Guide')])
// need .value here
console.log(books[0].value)

const map = reactive(new Map([['count', ref(0)]]))
// need .value here
console.log(map.get('count').value)
```

## 반응형 상태 구조 분해하기(Destructuring)

큰 반응형 객체의 몇몇 속성을 사용하길 원할 때, 원하는 속성을 얻기 위해 **[ES6 구조 분해 할당](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment)** 을 사용하는 것은 매우 일반적입니다.

```jsx
import { reactive } from 'vue'

const book = reactive({
  author: 'Vue Team',
  year: '2020',
  title: 'Vue 3 Guide',
  description: '당신은 이 책을 지금 바로 읽습니다 ;)',
  price: '무료'
})

let { author, title } = book
```

안타깝게도, 그러한 구조 분해로 두 속성은 반응형을 잃게 될 것 입니다. 이런 경우, 반응형 객체를 일련의 `ref` 들로 변환해야 합니다. 이러한 `ref` 들은 소스 객체에 대한 반응형 연결을 유지합니다.

toRefs, toRef를 사용하면 반응형 객체의 속성과 동기화 됩니다. 그래서 원본 속성을 변경하면 ref 객체가 업데이트되고 그 반대의 경우도 마찬가지 입니다.

```jsx
import { reactive, toRefs } from 'vue'

const book = reactive({
  author: 'Vue Team',
  year: '2020',
  title: 'Vue 3 Guide',
  description: '당신은 지금 바로 이 책을 읽습니다  ;)',
  price: '무료'
})

let { author, title } = toRefs(book)

title.value = 'Vue 3 상세 Guide' // title 이 ref 이므로 .value 를 사용해야 합니다.
console.log(book.title) // 'Vue 3 Detailed Guide'
```

## `readonly`를 이용하여 반응형 객체의 변경 방지

때때로 반응형 객체(`ref`나 `reactive`)의 변화를 추적하기 원하지만, 또한 특정 부분에서는 변화를 막기를 원하기도 합니다. 예를 들어, `Provide/Inject`로 주입된 반응형 객체를 갖고 있을 때, 우리는 그것이 주입된 곳에서는 해당 객체가 변이되는 걸 막고자 할 것입니다. 이렇게 하려면 원래 객체에 대한 읽기 전용 프록시를 생성하십시오.

```jsx
import { reactive, readonly } from 'vue'

const original = reactive({ count: 0 })

const copy = readonly(original)

// 원본이 변이되면 복사본에 의존하는 watch 도 트리거될 것 입니다.
original.count++

// 복사본을 변이하려고 하면 경고와 함께 실패할 것 입니다.
copy.count++ // warning: "Set operation on key 'count' failed: target is readonly."
```

## **[Reactivity Transform](https://vuejs.org/guide/extras/reactivity-transform.html) 실험적인 단계**

`refs`와 함께 `.value`를 사용해야 하는 것은 JavaScript의 언어 제약으로 인한 단점입니다. 그러나 `compile-time transforms`을 사용하면 적절한 위치에 `.value`를 자동으로 추가하여 인체 공학을 개선할 수 있습니다.

Vue는 다음과 같이 이전 “counter” 예제를 작성할 수 있는 `compile-time transforms`을 제공합니다.

```jsx
<script setup>
let count = $ref(0)

function increment() {
  // no need for .value
  count++
}
</script>

<template>
  <button @click="increment">{{ count }}</button>
</template>
```

# Computed

## Computed

---

템플릿 문법(`{{ }}`)은 간단히 사용 하면 매우 편리합니다. 하지만 템플릿 표현식 내 코드가 길어질 경우 가독성이 떨어지고 유지보수가 어려워질 수 있습니다. 예를 들어 아래와 같이 객체가 있는경우:

```jsx
const teacher = reactive({
  name: '짐코딩',
  lectures: [
    'HTML/CSS',
    'JavaScript',
    'Vue3'
  ]
})
```

그리고 `<template>` 에 `author`가 책을 갖고 있는지 없는지 여부를 표시하고 싶습니다.

```html
<p>강의가 존재 합니까?:</p>
<span>{{ teacher.lectures.length > 0 ? 'Yes' : 'No' }}</span>
```

이 시점에서 템플릿 표현식은 복잡해지며 선언적이지 않습니다. 또 이러한 코드를 여러곳에서 반복적으로 사용해야 한다면 더더욱 비효율 적일 것입니다.

이럴때 사용하는 것이 `계산된 속성(computed property)`입니다. 

```jsx
const hasLecture = computed(() => {
  return teacher.lectures.length > 0 ? 'Yes' : 'No'
})
```

```html
<p>강의가 존재 합니까?:</p>
<span>{{ hasLecture }}</span>
```

## Computed vs Method

---

아래와 같이 `메서드`를 활용하면 `computed`와 동일한 효과를 얻을 수 있습니다.

```html
<p>{{ existLecture() }}</p>
```

```jsx
// in component
function existLecture() {
  return teacher.lectures.length > 0 ? 'Yes' : 'No'
}
```

이렇게 `computed`와 메서드는 동일한 결과를 얻을 수 있습니다. 하지만 차이점은 `computed`는 **결과가 캐시된다**는 것입니다. 그리고 `computed` **내 반응형 데이터가 변경된 경우에만 다시 계산**됩니다.

- Computed는 캐쉬됨
- Method는 파라미터가 올 수 있음
- 컴포넌트 랜더링시 computed는 비용이 적게듬
    - [관련](https://kr.vuejs.org/v2/guide/comparison.html)

## Writable Computed

---

Computed는 기본적으로 getter전용입니다. 계산된 속성에 새 값을 할당하려고 하면 런타임 경고가 표시됩니다.  새로운 계산된 속성이 필요한 경우에 getter와 setter를 모두 제공하여 속성을 만들 수 있습니다.

```jsx
import { computed, ref } from 'vue';
export default {
  setup() {
    const firstName = ref('홍');
    const lastName = ref('길동');

    const fullName = computed({
      get() {
        return firstName.value + ' ' + lastName.value;
      },
      set(newValue) {
        [firstName.value, lastName.value] = newValue.split(' ');
      },
    });

    fullName.value = '안녕 하세요';
    return {
      firstName,
      lastName,
      fullName,
    };
  },
};
```

# 클래스와 Style 바인딩

## HTML 클래스 바인딩

---

### 객체 바인딩

클래스를 동적으로 바인딩 하기위해선는 `:class`(`v-bind:class`)를 사용할 수 있습니다.

```html
<div
  class="text"
  :class="{ active: isActive, 'text-danger': hasError }"
></div
```

위 예시처럼 `v-bind:class` 디렉티브는 일반 `class`속성과 공존할 수 있습니다. 그리고 객체를 반환하는 `computed`에 바인딩할 수도 있습니다.

```html
<div class="text" :class="classObject"></div>
```

```jsx
const classObject = computed(() => {
    return {
      active: isActive.value && !hasError.value,
      'text-danger': !isActive.value && hasError.value,
    };
});
```

### 배열에 바인딩

배열에 `:class`를 바인딩하여 클래스 목록을 적용할 수 있습니다.

```jsx
const activeClass = ref('active')
const errorClass = ref('text-danger')
```

```jsx
<div :class="[activeClass, errorClass]"></div>
```

## 인라인 스타일 바인딩

---

HTML style 속성에 객체값을 바인딩할 수 있습니다.

```jsx
const activeColor = ref('red')
const fontSize = ref(30)
```

```html
<div :style="{ color: activeColor, fontSize: fontSize + 'px' }"></div>
```

템플릿이 더 깔끔해지도록 스타일 객체에 직접 바인딩하는 것이 좋습니다.

```jsx
const styleObject = reactive({
  color: 'red',
  fontSize: '13px'
})
```

```html
<div :style="styleObject"></div>
```

### 배열에 바인딩

`:style`은 여러 객체 배열에 바인딩할 수 있습니다.

# 조건부 렌더링

## `v-if`

---

`v-if` 디렉티브는 조건부로 블록을 렌더링 할 때 사용됩니다.

```html
<h1 v-if="visible">Hello Vue3!</h1>
```

## `v-else`

---

`v-else` 디렉티브는 `v-if`가 `거짓(false)`일 때 렌더링 하는 블록입니다.

```html
<h1 v-if="visible">Hello Vue3!</h1>
<h1 v-else>Good bye!</h1>
```

## `v-else-if`

---

`v-else-if`는 이름에서 알 수 있듯이 `v-if`에 대한 ‘else if 블록' 입니다. 여러 조건을 연결할 수 있습니다.

```html
<h1 v-if="type === 'A'">
  A
</h1>
<h1 v-else-if="type === 'B'">
  B
</h1>
<h1 v-else-if="type === 'C'">
  C
</h1>
<h1 v-else>
  Not A/B/C
</h1>
```

## `<template v-if=””>`

---

여러개의 HTML요소를 `v-if` 디렉티브로 연결하고 싶다면 `[<template>](https://developer.mozilla.org/ko/docs/Web/HTML/Element/template)`을 사용할 수 있습니다.

```html
<template v-if="visible">
  <h1>Title</h1>
  <p>Paragraph 1</p>
  <p>Paragraph 2</p>
</template>
```

## `v-show`

---

요소를 조건부로 표시하는 또 다른 옵션은 `v-show` 디렉티브 입니다.

```html
<h1 v-show="show">Title</h1>
	<button @click="show = !show">toggle show</button>
```

## ****`v-if` 대 `v-show`**

---

`v-if`는 "실제(real)"로 렌더링됩니다. 전환 할 때 블록 내부의 컴포넌트들이 제거되고 다시 생성되기 때문입니다.

또한 `v-if`는 **게으릅니다(lazy)**. 초기 렌더링 시, 조건이 거짓(false)이면 아무 작업도 하지 않습니다. 조건부 블록은 조건이 처음으로 참(true)이 될 때까지 렌더링되지 않습니다.

이에 비해 `v-show`는 훨씬 간단합니다. 엘리먼트는 CSS 기반 전환으로 초기 조건과 관계 없이 항상 렌더링됩니다. (역자 주: v-show는 엘리먼트를 DOM에 우선 렌더링하고 조건에 따라 CSS display:block/display:none 속성을 전환합니다.)

일반적으로 `v-if`는 전환 비용이 높은 반면, `v-show`는 초기 렌더링 비용이 높습니다. 그러므로 무언가를 자주 전환해야 한다면 `v-show`를 사용하는 게 좋고, 런타임 시 조건이 변경되지 않는다면 `v-if`를 사용하는 게 더 낫습니다.

## ****`v-if` 와 `v-for`**

---

> **TIP**
`v-if`와 `v-for`를 함께 쓰는 것은 **권장하지 않습니다**. 자세한 내용은 **[스타일 가이드](https://v3.ko.vuejs.org/style-guide/#v-if%E1%84%8B%E1%85%AA-v-for-%E1%84%83%E1%85%A9%E1%86%BC%E1%84%89%E1%85%B5-%E1%84%89%E1%85%A1%E1%84%8B%E1%85%AD%E1%86%BC-%E1%84%91%E1%85%B5%E1%84%92%E1%85%A1%E1%84%80%E1%85%B5-%E1%84%91%E1%85%B5%E1%86%AF%E1%84%89%E1%85%AE)**를 참고하세요.
> 

동일한 엘리먼트에 `v-if`와 `v-for`를 함께 사용할 때, `v-if`가 더 높은 우선순위를 갖습니다. 자세한 내용은 **[리스트 렌더링 가이드](https://v3.ko.vuejs.org/guide/list#v-for-with-v-if)**를 참고하세요.

### 참고

- [Vue2 타일 가이드 (영문)](https://v2.vuejs.org/v2/style-guide/?redirect=true#Avoid-v-if-with-v-for-essential)
- [Vue3 스타일 가이드 (영문)](https://vuejs.org/style-guide/)
- [Vue3 스타일 가이드 (한글)](https://v3-docs.vuejs-korea.org/style-guide/) [2020/1/16 기준 번역 진행중]

# 목록 렌더링

## `v-for`

---

`v-for` 디렉티브를 사용하여 배열인 목록을 렌더링 할 수 있습니다.

```jsx
const items = reactive([
  { id: 1, message: 'Java' },
  { id: 2, message: 'HTML' },
  { id: 3, message: 'CSS' },
  { id: 4, message: 'JavaScript' },
]);
```

```html
<li v-for="(item, index) in items" :key="item.id">
  {{ item.message }}
</li> 
```

- `v-for=”item in items”` 문법을 사용해서 배열에서 항목을 순차적으로 할당합니다.
- `v-for=”(item, index) in items”` 문법을 사용해서 배열 인덱스를 가져올 수 있습니다.
- 항목을 나열할 때 각 `[:key](https://v3.ko.vuejs.org/api/special-attributes.html#key)` 속성에는 고유한 값을 지정해야 합니다. (vue 2.2.0 부터 필수)

## `v-for` 객체

---

`v-for`를 사용하여 객체의 속성을 반복 할 수도 있습니다.

```jsx
const myObject = reactive({
  title: '제목입니다.',
  author: '홍길동',
  publishedAt: '2016-04-10',
});
```

```jsx
<li v-for="(value, key, index) in myObject" :key="key">
	{{ key }} - {{ value }} - {{ index }}
</li>
```

# 디렉티브 (directives)

## 디렉티브 (directives)

---

디렉티브(directives)는 앞에서 말씀드렸던 것처럼 `v-`접두사가 있는 특수 속성입니다. 그리고 디렉티브(directives)는 그대로 직역하면 지시를 뜻 합니다. 즉, 디렉티브(directives)는 기능상에서 중요한 역할인 컴포넌트(또는 DOM 요소)에게 “**~~하게 작동하라”** 하고 지시를 해주는 지시문을 말합니다.

Vue는 여러내장 디렉티브를 제공합니다.

- `v-text`
- `v-html`
- `v-show`
- `v-if`
- `v-else`
- `v-else-if`
- `v-for`
- `v-on` (단축표기 `@`)
- `v-bind` (단축표기 `:`)
- `v-model`
- `v-slot` (단축표기 `#`)
- `v-pre`
- `v-once`
- `v-cloak`
- `v-memo` (`v3.2+`)

[Built-in Directives | Vue.js](https://vuejs.org/api/built-in-directives.html)

[https://v3.ko.vuejs.org/api/directives.html#v-text](https://v3.ko.vuejs.org/api/directives.html#v-text)

## 디렉티브 구성

---

디렉티브는 다음과 같이 구성되어 있습니다.

- `**디렉티브(directives)**` : `v-` 접두사가 있는 특수 속성으로 디렉티브의 `값(value)`이 변경될 때 특정 효과를 반응적으로 DOM에 적용하는 것을 말합니다.
- `**전달인자(Argument)**` : 일부 디렉티브는 디렉티브명 뒤에 콜론(:)으로 표기되는 전달인자를 가질 수 있습니다. 예를 들어, `v-bind` 디렉티브는 반응적으로 HTML 속성을 갱신하는 데 사용합니다.
    - `동적 전달인자` : 대괄호를 사용하여 전달인자를 동적으로 삽입할 수 있습니다.
    `<a v-bind:[attributeName]="url"> ... </a>`
- `**수식어(Modifiers)**` : 수식어는 `점(.)`으로 표시되는 특수 접미사로 디렉티브가 특별한 방식으로 바인딩되어야 함을 나타냅니다.

<img width="1000" alt="directive" src="https://user-images.githubusercontent.com/86648892/226269559-71783f86-10cf-4d74-831f-26349d3e6a15.png">

## 커스텀 디렉티브

---

[Custom Directives](https://www.notion.so/Custom-Directives-784b5372eb0847b0a8fd85f28891d370)

# 이벤트 처리

이벤트 처리는 `v-on`디렉티브로 사용할 수 있습니다. 그리고 `v-on`이벤트는 자주 사용하기 때문에 `@`단축 표현으로 많이 사용됩니다.

```jsx
const counter = ref(0);
```

```html
<div>
  <button @click="counter += 1">counter {{ counter }}</button>
</div>
```

## 메소드 이벤트 핸들러

---

`v-on` 디렉티브에서 메소드를 호출할 수 있습니다. 그리고 이때 매개변수로 `event` 객체를 받습니다.

```jsx
const printEventInfo = (event) => {
  console.log(event.target);
  console.log(event.target.tagName);
};
```

```html
<div>
  <button @click="printEventInfo">printEventInfo</button>
</div>
```

## 이벤트 객체 접근

---

인라인 핸들링에서 `event` 객체에 접근할 수 있습니다. 접근하는 방법는 `$event` 키워드를 사용합니다.

```jsx
const printEventInfo2 = (message, event) => {
  console.log('messsage: ', message);
  console.log(event.target);
  console.log(event.target.tagName);
};
```

```html
<button @click="printEventInfo2('hello world', $event)">
  inline event handler
</button>
```

## 이벤트 수식어(Modifiers)

---

우리는 이벤트를 조작할 때 이벤트 내부에서 `event.preventDefault()` 또는 `event.stopPropagation()` 메서드를 호출할 수 있습니다. 메소드에서 이러한 메소드의 호출은 어렵지 않지만 메소드 안에서 비즈니스 외에 이러한 코드는 비효율적입니다.

이 문제를 해결하기 위해 Vue는 `v-on` 이벤트에 다양한 **이벤트 수식어(Modifiers)**를 제공합니다.

- `.stop` = `e.stopPropagation()`
- `.prevent` = `e.preventDefault()`
- `.capture` = 캡처 모드를 사용할 때 이벤트 리스너를 사용 가능합니다.
- `.self` = 오로지 자기 자신만 호출할 수 있다. 즉, 타깃요소가 `self`일 때 발동된다.
- `.once` = 해당 이벤트는 **한 번만** 실행된다.
- `.passive` = 일반적으로 **[모바일 장치의 성능을 개선](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener#improving_scrolling_performance_with_passive_listeners)** 하기 위해 터치 이벤트 리스너와 함께 사용됩니다 .

```html
<!-- 클릭 이벤트 전파가 중단되었습니다. -->
<a @click.stop="doThis"></a>

<!-- 제출 이벤트가 페이지를 다시 로드하지 않습니다. -->
<form @submit.prevent="onSubmit"></form>

<!-- 수정자는 체이닝이 가능합니다. -->
<a @click.stop.prevent="doThat"></a>

<!-- 단순히 수식어만 사용이 가능합니다. -->
<form @submit.prevent></form>

<!-- 캡처 모드를 사용할 때 이벤트 리스너를 사용 가능합니다.-->
<!--즉, 내부 엘리먼트를 대상으로 하는 이벤트가 해당 엘리먼트에서 처리되기 전에 여기서 처리합니다. -->
<div @click.capture="doThis">...</div>

<!-- event.target이 엘리먼트 자체인 경우에만 트리거를 처리합니다.-->
<!-- 자식 엘리먼트에서는 처리되지 않습니다.-->
<div @click.self="doThat">...</div>

<div @scroll.passive="onScroll">...</div>
```

## 키 수식어

---

키보드 이벤트를 수신할 때 종종 특정 키를 확인해야 하는 경우가 있습니다. 그래서 Vue에서는 `v-on` 또는 `@` 디렉티브에 키 수식어를 제공합니다.

- `.enter`
- `.tab`
- `.delete` (”Delete”와 “Backspace” 키 모두를 수신합니다.)
- `.esc`
- `.space`
- `.up`
- `.down`
- `.left`
- `.right`

```html
<input type="text" @keyup.enter="addTodo" />
```

## 시스템 키 수식어

---

다음 수식어를 사용해 해당 수식어 키가 눌러진 경우에만 마우스 또는 키보드 이벤트 리스너를 트리거 할 수 있습니다.

- `.ctrl`
- `.alt`
- `.shift`
- `.meta` (Mac에서 meta는 command key, Window에서 meta는 윈도우키 입니다, 특정 키보드에서 [조금 다를 수 있음](https://v3.ko.vuejs.org/guide/events.html#%E1%84%89%E1%85%B5%E1%84%89%E1%85%B3%E1%84%90%E1%85%A6%E1%86%B7-%E1%84%89%E1%85%AE%E1%84%89%E1%85%B5%E1%86%A8%E1%84%8B%E1%85%A5-%E1%84%8F%E1%85%B5%E1%84%86%E1%85%A9%E1%86%A8%E1%84%85%E1%85%A9%E1%86%A8))

```html
<!-- 알트 + 엔터 -->
<input @keyup.alt.enter="clear" />

<!-- 컨트롤 + 엔터 -->
<input @keyup.ctrl.enter="send" />

<!-- 컨트롤 + 클릭 -->
<div @click.ctrl="doSomething">Do something</div>
```

## ****`.exact` 수식어**

---

`.exact` 수식어는 정확한 조합이 눌러야하는 것을 요구합니다.

```html
<!-- 아래코드는 Alt 또는 Shift와 함께 눌렀을 때도 실행됩니다.-->
<button @click.ctrl="onClick">A</button>

<!-- 아래코드는 Ctrl키만 눌려져 있을 때 실행됩니다.-->
<button @click.ctrl.exact="onCtrlClick">A</button>

<!-- 아래 코드는 시스템 키가 눌리지 않은 상태인 경우에만 작동합니다.-->
<button @click.exact="onClick">A</button>
```

## 마우스 버튼 수식어

---

- `.left`
- `.right`
- `.middle`

# 양방향 바인딩

## `v-model`

---

프론트엔드에서 입력 양식을 처리할 때 **입력 요소의 상태**와 **자바스크립트의 상태**를 **동기화**해야 하는 경우가 많습니다. `value`를 바인딩하고 `@input`이벤트로 `text`를 변경하는 것은 번거로울 수 있습니다.

```html
<input
  :value="text"
  @input="event => text = event.target.value" />
```

그래서 Vue에서는 이러한 작업은 단순화 하도록 양방향을 바인딩할 수 있는 `v-model`디렉티브를 제공합니다.

```html
<input v-model="text" />
```

## `textarea`

---

- `:value`, `@input`
    
    ```html
    <textarea
      :value="textareaValue"
      @input="(event) => (textareaValue = event.target.value)"
    ></textarea>
    ```
    
- `v-model`
    
    ```html
    <textarea v-model="textareaValue"></textarea>
    ```
    

## `checkbox`, `radio`, `select`

---

`v-model`은 내부적으로 HTML 요소가 어떤 요소냐에 따라 서로 다른 속성(`:value`)과 이벤트(`@input`)를 사용합니다.

- `input type=”text”`와 `textarea`는 `value` 속성과 `input` 이벤트를 사용합니다.
- `checkbox`와 `radio`버튼은 `checked` 속성과 `change` 이벤트를 사용합니다.
- `select` 태그는 `value` 속성과 `change` 이벤트를 사용합니다.

### checkbox

- `:checked`, `@change`
    
    ```html
    <input
      type="checkbox"
      :checked="checkboxValue"
      @change="(event) => (checkboxValue = event.target.checked)"
    />
    ```
    
- `v-model`
    
    ```html
    <input
      type="checkbox"
    	v-model="checkboxValue"
    />
    ```
    

### radio

- `v-model`
    
    ```html
    <label>
      <input type="radio" name="type" value="O" v-model="radioValue" />
      O형
    </label>
    <label>
      <input type="radio" name="type" value="A" v-model="radioValue" />
      A형
    </label>
    ```
    

### select

- `v-model`
    
    ```html
    <select v-model="selectValue">
      <option value="html">HTML 수업</option>
      <option value="css">CSS 수업</option>
      <option value="javascript">JavaScript 수업</option>
    </select>
    ```
    

## `checkbox`

---

하나의 `checkbox`는 단일 `boolean` 값을 가집니다.

```html
<label>
  <input type="checkbox" v-model="checkboxValue" />
  {{ checkboxValue }}
</label>
```

여러개의 `checkbox`는 배열을 바인딩할 수 있습니다.

```html
<div>
  <label>
    <input type="checkbox" v-model="checkboxValues" value="html" />
    HTML
  </label>
  <label>
    <input type="checkbox" v-model="checkboxValues" value="css" />
    CSS
  </label>
  <label>
    <input type="checkbox" v-model="checkboxValues" value="javascript" />
    JavaScript
  </label>
  <p>
    {{ checkboxValues }}
  </p>
</div>
```

### 값 바인딩

단일 `checkbox` 일 때 `boolean`이 아닌 다른 값을 바인딩 하고 싶다면 `true-value`, `false-value` 속성을 사용할 수 있다.

```html
<label>
  <input
    type="checkbox"
    v-model="checkboxYN"
    true-value="Yes"
    false-value="No"
  />
  {{ checkboxYN }}
</label>
```

## `v-model` 수식어(modifiers)

---

### `.lazy`

기본적으로, `v-model`은 각 `input` 이벤트 후 입력과 데이터를 동기화 합니다. (단, **[앞에서 설명](https://v3.ko.vuejs.org/guide/forms.html#vmodel-ime-tip)**한 IME 구성은 제외됩니다.). `lazy` 수식어를 추가하여 `change` 이벤트 이후에 동기화 할 수 있습니다.

```html
<input v-model.lazy="text" />
```

### `.number`

사용자 입력이 자동으로 number 타입으로 형변환 되기를 원하면,  `.number` 수식어를 추가하면 됩니다.

```html
<input v-model.number="text" />
```

### **`.trim`**

사용자가 입력한 내용에서 자동으로 앞뒤 공백을 제거하는 트림처리가 되길 바란다면, `v-model`이 관리하는 input에 `trim` 수식어를 추가하면 됩니다.

```html
<input v-model.trim="text" />
```

# Watch, WatchEffect

## Watch

---

우리는 종종 반응형 상태가 변경 되었을때에 감지하여 다른 작업(api call 등)을 수행해야 하는 경우가 있습니다. 예를 들어 어떠한 상태가 변경 되었을때 DOM을 변경하거나 비동기 작업을해서 다른 상태를 변경하는 것입니다.

Composition API의 `watch` 함수를 사용 하여 반응형 상태가 변경될 때마다 특정 작업을 수행할 수 있습니다.

```jsx
const message = ref('Hello World');

// message 데이터 변경에 
watch(message, (newValue, oldValue) => {
  console.log('newValue: ', newValue);
  console.log('oldValue: ', oldValue);
	// 어떠한 작업을 수행하는 "감시자" 역할을 합니다.
});
```

### Watch Source Type

```jsx
watch(/* Source Type */, (newValue, oldValue) => {});
```

`watch`의 첫 번째 매개변수는 다양한 타입이 될 수 있습니다. `ref`, `reactive`, `computed`, `getter 함수`, `array` 타입일 될 수 있습니다.

```jsx
const x = ref(0)
const y = ref(0)

// single ref
watch(x, (newX) => {
  console.log(`x is ${newX}`)
})

// getter
watch(
  () => x.value + y.value,
  (sum) => {
    console.log(`sum of x + y is: ${sum}`)
  }
)

// array of multiple sources
watch([x, () => y.value], ([newX, newY]) => {
  console.log(`x is ${newX} and y is ${newY}`)
})
```

다음과 같이 반응형 객체의 속성은 볼 수 없습니다.

```jsx
const obj = reactive({ count: 0 });

// 숫자(number)를 전달하기 때문에 작동하지 않습니다.
watch(obj.count, (newValue) => {
	console.log('newValue: ', newValue);
});
```

대신 getter를 사용하세요.

```jsx
const obj = reactive({ count: 0 });
watch(() => obj.count, (newValue) => {
  console.log('newValue: ', newValue);
});
```

## deep option

---

반응형 객체를 직접 `watch()` 하면 암시적으로 깊은 감시자가 생성됩니다. 즉, 속성 뿐만아니라 모든 중첩된 속성에도 트리거 됩니다.

```jsx
const person = reactive({
  name: '홍길동',
  age: 30,
  hobby: '운동',
  obj: {
    count: 0,
  },
});

watch(person, (newValue) => {
  console.log('newValue: ', newValue);
});
```

`getter function`으로 객체를 넘길 경우에는 **`객체의 값`**이 바뀔 경우에만 트리거 됩니다. 즉, 중첩된 속성은 트리거되지 않습니다.

```jsx
watch(
	() => person.obj,
	(newValue) => {
		// 객체의 값이 바뀔 경우에만 트리거 됩니다.
	}
);
```

`deep` 옵션을 사용하면 깊은 감시자로 강제할 수 있습니다.

```jsx
watch(
  () => person.obj,
  (newValue) => {
    console.log('newValue: ', newValue);
  },
  { deep: true }
);
```

<aside>
💡 deep 옵션은 큰 데이터 구조에서 사용할 때 비용이 많이 들 수 있습니다. 필요한 경우에만 사용하고 성능 영향에 주의하십시오.

</aside>

## immediate 즉시실행

---

`immediate` 옵션을 사용하여 최초에 즉시실행 할 수 있다.

```jsx
const message = ref('Hello World!');
const reverseMessage = ref('');

watch(
  message,
  (newValue) => {
    reverseMessage.value = newValue.split('').reverse().join('');
  },
  {
    immediate: true,
  }
);
```

또는 함수를 외부에 선언하여 즉시실행 할 수 있음. (WatchEffect로 하면 더 단순화 할 수 있음)

```jsx
const message = ref('Hello World!');
const reverseMessage = ref('');

const reverseFn = () => {
  reverseMessage.value = message.value.split('').reverse().join('');
};

watch(message, reverseFn);
// 즉시실행
reverseFn();
```

## Computed vs Watch [공식문서](https://v3.ko.vuejs.org/guide/computed.html#computed-%E1%84%89%E1%85%A9%E1%86%A8%E1%84%89%E1%85%A5%E1%86%BC-vs-watch-%E1%84%89%E1%85%A9%E1%86%A8%E1%84%89%E1%85%A5%E1%86%BC)

---

`computed`와 `watch` 둘 다 비슷한 역할을 하고 있습니다.

- **computed**
    
    ```jsx
    const reverseMessage = computed(() =>
      message.value.split('').reverse().join('')
    );
    ```
    
- **watch**
    
    ```jsx
    watch(
      message,
      (newValue) => {
        reverseMessage.value = newValue.split('').reverse().join('');
      }
    );
    ```
    

### 어떻게 사용할 것인가

- **computed**
    
    Vue 인스턴스의 상태(ref, reactive 변수)의 종속 관계를 자동으로 세팅하고자 할 때는 `computed`로 구현하는 것이 좋다.
    
    위 예시 처럼 `reverseMessage`는 `message` 값에 따라 결정되어지는 종속관계에 있다.  이 종속관계 코드가 복잡해지면 `watch`로 구현할 경우 더 복잡해지거나 중복계산 또는 오류를 발생시킬 수 있다.
    
- **watch**
    
    Vue 인트턴스의 상태(ref, reactive 변수)의 변경 시점에 특정 액션(call api, push route 등)을 취하고자 할때 적합하다.
    
    대게의 경우 `computed`로 구현 가능한 것이라면 `watch`가 아니라 `computed`로 구현하는게 대부분 옳다.
    

## WatchEffect

WatchEffect는 콜백 함수 안의 반응성 데이터에 변화가 감지되면 자동으로 반응하여 실행합니다. 그리고 WatchEffect의 코드는 컴포넌트가 생성될 때 즉시 실행됩니다.

```html
watchEffect(async () => {
  const { data } =
							await axios.get(`https://reqres.in/api/users?page=${page.value}`);
  items.value = data.data;
});
```

## `watch` vs `watchEffect`

`watch`와 `watchEffect` 둘 다 관련 작업(api call, push route 등)을 반응적으로 수행할 수 있게 해줍니다. 하지만 주요한 차이점은 관련된 반응형 데이터를 추적하는 방식입니다.

- `watch`명시적으로 관찰된 소스만 추적합니다. 콜백 내에서 액세스한 항목은 추적하지 않습니다. 또한 콜백은 소스가 실제로 변경된 경우에만 트리거됩니다. `watch`종속성 추적을 부작용과 분리하여 콜백이 실행되어야 하는 시기를 보다 정확하게 제어할 수 있습니다.
- `watchEffect`반면에 종속성 추적과 부작용을 한 단계로 결합합니다. 동기 실행 중에 액세스되는 모든 반응 속성을 자동으로 추적합니다. 이것은 더 편리하고 일반적으로 더 간결한 코드를 생성하지만 반응성 종속성을 덜 명시적으로 만듭니다.

# Dynamic Components

## 동적 컴포넌트 (Dynamic Component)

컴포넌트를 동적으로 변경하고 싶을 때 `v-bind:is` 속성을 사용해서 변경할 수 있습니다. 동적 컴포넌트는 탭 인터페이스와 같이 컴포넌트간에 동적으로 전환해야 할 때 유용합니다.

```html
<component :is="currentTabComponent"></component>
```

위 예시에서 `:is` 속성에 전달된 값은 다음 중 하나를 포함할 수 있습니다.

- 등록된 컴포넌트의 문자열 이름 `string`
- 실제 가져온 컴포넌트 객체 `object`


> 💡 `<component :is=”...” />`를 사용하여 여러 컴포넌트간 전환하면 컴포넌트의 마운트가 매번 해제됩니다. 이때 `<KeepAlive> 내장 컴포넌트`를 사용하여 “비활성 컴포넌트"들의 “활성” 상태를 유지할 수 있도록 강제할 수 있습니다.

# Bootstrap 5 설치

## Bootstrap5

Bootstrap는 인기있는 UI Framework입니다. Vue가 JavaScript의 쉽고 빠른 개발을 도와준다면 Bootstrap은 사전에 정의된 CSS를 사용하여 최소한의 노력으로 쉽게 예쁜 HTML Markup을 도와줍니다.

BootstrapVue는 Vue용 Bootstrap이라고 보시면 될 것 같습니다. Vue를 위한 사전에 정의된 다양한 커스텀컴포넌트를 제공합니다. 하지만 이번 시간에는 다음과 같은 이유로 BootstrapVue이 아닌 Bootstrap5를 사용하도록 하겠습니다.

- Vue3를 위한 BootstrapVue는 현재 알파 버전입니다.
- 이번 강좌는 Vue3 문법을 배우는데 목적이 있기 때문에 최소한의 UI만 활용하는 일반 Bootstrap이 더 괜찮을것 같습니다.

## Boostrap5 설치

```bash
npm install bootstrap
```

```jsx
import 'bootstrap/dist/css/bootstrap.min.css';
import { createApp } from 'vue';
import App from './App.vue';

createApp(App).mount('#app');

import 'bootstrap/dist/js/bootstrap.js';
```

## Layout

Bootstrap를 활용하여 Layout을 만들어 보도록 하겠습니다.

### TheNav.vue

```jsx
// src/components/TheNav.vue
<script setup></script>
<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">Navbar</a>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">About</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>
```

### TheView.vue

```jsx
// src/components/TheView.vue
<template>
  <main class="container py-4">Hello World!</main>
</template>
```

### App.vue

```jsx
// src/App.vue
<script setup>
import TheNav from './components/TheNav.vue';
import TheView from './components/TheView.vue';
</script>

<template>
  <TheNav></TheNav>

  <TheView></TheView>
</template>
```

## Bootstrap Icons 설치

1. bootstrap-icons 모듈 설치
    
    ```bash
    npm i bootstrap-icons
    ```
    
2. main.js 에 bootstrap-icons.css 추가
    
    ```jsx
    // main.js
    import 'bootstrap-icons/font/bootstrap-icons.css';
    ```
    
3. `i 태그` 를 활용한 아이콘 적용
    
    ```html
    <template>
    	<i class="bi bi-youtube"></i>
    </template>
    ```
    
    [Bootstrap Icons 바로가기](https://icons.getbootstrap.com/)
    

## 참고

- Vue Style Guide
    
    [Style Guide - Vue.js](https://kr.vuejs.org/v2/style-guide/index.html#%EC%8B%B1%EA%B8%80-%EC%9D%B8%EC%8A%A4%ED%84%B4%EC%8A%A4-%EC%BB%B4%ED%8F%AC%EB%84%8C%ED%8A%B8-%EC%9D%B4%EB%A6%84-%EB%A7%A4%EC%9A%B0-%EC%B6%94%EC%B2%9C%ED%95%A8)
    
- Vue3 프로젝트에 Bootstrap5 설치
    
    [How to install Bootstrap 5 in Vue 3](https://larainfo.com/blogs/how-to-install-bootstrap-5-in-vue-3)
    
- Bootstrap Vue3 (현재 alpha version)
    
    [Introduction | BootstrapVue 3](https://cdmoro.github.io/bootstrap-vue-3/getting-started/#why-bootstrapvue3)
    
- Vuetify3 (Titan Beta)
    
    [The Vuetify roadmap - Vuetify](https://next.vuetifyjs.com/en/introduction/roadmap/)
    
- NPM Package Trands
    
    [bootstrap-vue vs quasar vs vuetify | npm trends](https://www.npmtrends.com/vuetify-vs-bootstrap-vue-vs-quasar)

# 프로젝트 만들기

## 프로젝트 만들기

vue3 기본 프로젝트를 만들어 보겠습니다.

```bash
npm init vue
```

![project1](https://user-images.githubusercontent.com/86648892/226270538-0f75c96c-111c-4bed-a2e1-68eb3f2c350c.png)

위와 같이 **ESLint**와 **Prettier** 설정만 Yes로 설정하고 나머지는 No로 한 후 프로젝트를 생성하도록 하겠습니다.

ESLint, prettier는 좋은 품질의 코드를 작성법을 제공하고, 코드가 일관된 스타일을 준수하도록 만들어주는 도구입니다.

- ESLint : ESLint는 **ES** 와 **Lint**를 합친 것입니다. ES는 Ecma Script의 약어이며, Lint는 에러가 있는 코드에 표시를 달아놓는 것을 의미합니다. 즉, ESLint는 자바스크립트                                                                                                                    문법에서 에러를 표시해주는 툴이다.
- Prettier : Prettier는 Code Formatter이다. 개발자들에게 일관적인 코딩 스타일을 유지할 수 있게 도와주는 툴이다.

> 💡 Vue Router와 상태관리 라이브러리인 Pinia는 필요한 순간에 직접 설치해 보도록 하겠습니다.


그리고 프로젝트 폴더로 진입하여 의존성 모듈을 설치 후 서버를 개발 모드로 실행해 보도록 하겠습니다.

```bash
cd vue3-community
npm install
npm run dev
```

![project2](https://user-images.githubusercontent.com/86648892/226270653-a339e1c5-2228-46f2-a3cd-d03fe57f5605.png)

프로젝트를 실행하면 위와 같이 기본 화면이 잘 나오는 것을 확인할 수 있습니다.

## ESlint, Prettier 설정

`eslintrc.cjs` 파일에 몇가지 `rules`을 추가하겠습니다.

```jsx
/* eslint-env node */
require('@rushstack/eslint-patch/modern-module-resolution');

module.exports = {
  root: true,
  extends: [
    'plugin:vue/vue3-essential',
    'eslint:recommended',
    '@vue/eslint-config-prettier',
  ],
  env: {
    'vue/setup-compiler-macros': true,
  },
	parserOptions: {
		ecmaVersion: '2022',
		sourceType: 'module',
	},
  rules: {
    'prettier/prettier': [
      'error',
      {
        singleQuote: true,
        semi: true,
        tabWidth: 2,
        trailingComma: 'all',
        printWidth: 80,
        bracketSpacing: true,
        arrowParens: 'avoid',
				endOfLine: 'auto', // 한줄 추가
      },
    ],
  },
};
```

Prettier 옵션은 [**공식 홈페이지**](https://prettier.io/docs/en/options.html)에서 확인 할 수 있습니다.

## settings.json 설정

```json
{
	"eslint.validate": [
	    "javascript",
	    "javascriptreact",
	    "typescript",
	    "typescriptreact",
	    // "html",  // 삭제
	    "vue",
	    "markdown"
	],
	"editor.codeActionsOnSave": {
	    "source.fixAll.eslint": true
	},
	"editor.tabSize": 2
}
```

## jsconfig.json 설정

```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "jsx": "preserve",
    "paths": {
      "@/*": ["src/*"]
    }
  },
  "exclude": ["node_modules", "dist"]
}
```

## VSCode 설정

윈도우에서는 `Ctrl + ,(콤마)` 맥에서는 `Cmd + ,(콤마)`를 눌러 설정창에 진입한 후 아래와 같은 설정을 진행해 보도록 하겠습니다.

✅  **Format On Save** 

✅  **Default Formatter**

## 파일 삭제

불필요한 파일을 제거해 보도록 하겠습니다.

```jsx
├── [gymcoding  727]  README.md
├── [gymcoding  337]  index.html
├── [gymcoding 108K]  package-lock.json
├── [gymcoding  548]  package.json
├── [gymcoding   96]  public
│   └── [gymcoding 4.2K]  favicon.ico
├── [gymcoding  192]  src
│   ├── [gymcoding 1.2K]  App.vue
│   ├── [gymcoding  128]  assets
│   │   ├── [gymcoding 2.0K]  base.css
│   │   └── [gymcoding  308]  logo.svg
│   ├── [gymcoding  192]  components
│   │   ├── [gymcoding  651]  HelloWorld.vue
│   │   ├── [gymcoding 3.0K]  TheWelcome.vue
│   │   ├── [gymcoding 1.4K]  WelcomeItem.vue
│   │   └── [gymcoding  224]  icons
│   │       ├── [gymcoding 1.0K]  IconCommunity.vue
│   │       ├── [gymcoding 1.2K]  IconDocumentation.vue
│   │       ├── [gymcoding 1.9K]  IconEcosystem.vue
│   │       ├── [gymcoding  288]  IconSupport.vue
│   │       └── [gymcoding  913]  IconTooling.vue
│   └── [gymcoding   93]  main.js
└── [gymcoding  302]  vite.config.js
```

그리고 App.vue를 다음과 같이 수정해주세요.

# 컴포넌트 기초

## 컴포넌트 정의

---

컴포넌트를 정의하는 방법은 `Single-File Component(SFC)`를 사용하는 방법과  `문자열 템플릿(string template)`으로 정의하는 방법이 있습니다.

- `Single-File Component(SFC)` → 실무에서 일반적으로 사용하는 방법
- `문자열 템플릿(string template)`

### Single-File Component(SFC)

**빌드 도구를 사용할 때** 컴포넌트는 일반적으로 **Single-File Component(SFC)**로 정의할 수 있습니다. SFC는 확장자 `*.vue`를 가진 단일 파일입니다.

```jsx
<template>
  <button @click="counter++">클릭 횟수 {{ counter }}</button>
</template>

<script>
import { ref } from 'vue';

export default {
  setup() {
    const counter = ref(0);
    return {
      counter,
    };
  },
};
</script>

<style></style>
```

### 문자열 템플릿 (string template)

**빌드 도구를 사용하지 않을 때** 컴포넌트는 Vue 옵션인을 포함하는 일반 JavaScript 객체로 정의할 수 있습니다.

```jsx
import { ref } from 'vue/dist/vue.esm-bundler.js';
export default {
  setup() {
    const counter = ref(0);
    return {
      counter,
    };
  },
  template: `
	  <button @click="counter++">클릭 횟수 {{ counter }}</button>
  `,
};
```

> 💡 **vue.esm-bundler.js**
런타임 컴파일러를 포함합니다. 빌드도구(Vite)를 사용하지만 여전히 런타임 문자열 템플릿을 원하는 경우이 옵션(vue.esm-bundler.js)을 사용합니다. 이 파일에 vue의 별칭을 지정하도록 번 들러를 구성해야합니다.

## 컴포넌트 등록

Vue 컴포넌트는 `<template>`안에서 발견 되었을 때 Vue가 구현 위치를 알 수 있도록 **“등록"**을 해야합니다. 그리고 컴포넌트를 등록하는 방법는 **전역(Global)** 및 **지역(Local)** 두 가지가 있습니다.

- **전역 등록(Global Registration)**
- **지역 등록(Local Registration)**

### 전역 등록

우리는 `app.component()` 메서드를 사용하여 **현재 Vue 애플리케이션에서 전역적으로 사용**할 수 있도록 할 수 있습니다.

```jsx
import { createApp } from 'vue';
import App from './App.vue';

import GlobalComponent from './components/GlobalComponent.vue';

const app = createApp(App)
app.component('GlobalComponent', GlobalComponent)
app.mount('#app');
```

`app.component()` 메서드는 다음과 같이 연결(메서드 체인)될 수 있다.

```jsx
app
  .component('ComponentA', ComponentA)
  .component('ComponentB', ComponentB)
  .component('ComponentC', ComponentC)
```

**전역 등록된 컴포넌트는 애플리케이션 어떤 곳에서든 사용 가능하다.**

### 지역 등록

전역 등록은 편리하지만 다음과 같은 몇 가지 단점이 있다.

1. Webpack(또는 Vite)과 같은 빌드 시스템을 사용하는 경우 컴포넌트를 전역 등록하는 것은 **컴포넌트를 사용하지 않더라도 계속해서 최종 빌드에 해당 컴포넌트가 포함**되는 것을 의미합니다. 이는 사용자가 다운로드하는 자바스크립트 파일의 크기를 불필요하게 증가시킵니다.
2. 전역 등록을 계속 하게 되면 애플리케이션의 컴포넌트간 종속 관계를 확인하기 힘듭니다. 상위 컴포넌트, 하위 컴포넌트 구분이 힘들면 유지보수를 하기게 매우 어려워지게 됩니다.

지역 등록된 컴포넌트는 **현재 컴포넌트 영역 안에서만 사용할 수 있습니다.** Vue 컴포넌트 인스턴스의 `components` 옵션을 사용해서 등록할 수 있습니다.

```jsx
// ParentComponent.vue 파일
import ChildComponent from './ChildComponent.vue'

export default {
	components: {
		ChildComponent
	},
	setup() {
		// ...
	}
}
```

`ParentComponent`  컴포넌트에 로컬 등록된 `ChildComponent`는 현재 컴포넌트인 `ParentComponent` 컴포넌트에서만 사용 가능합니다.

## 컴포넌트 사용

등록된 컴포넌트는 `<template>`에서 원하는 만큼 사용할 수 있습니다.

```jsx
<h2>Single-File Component</h2>
<ButtonCounter></ButtonCounter>
<ButtonCounter></ButtonCounter>
<ButtonCounter></ButtonCounter>
```

그리고 **컴포넌트는 사용할 때마다 해당 컴포넌트의 새 인스턴스가 생성**됩니다. 즉, 사용할 때마다 `setup()` 함수 가 실행 된다는 것을 의미합니다.

### PascalCase

Single-File Commponent(SFC)에서는 기본 HTML요소와 구분하기 위해 자식 컴포넌트에 `PascalCase` 이름을 사용하는 것이 좋습니다.

기본 HTML 태그 이름은 대소문자를 수분하지 않지만 Vue SFC는 컴파일된 형식이므로 대소문자 구분 태그 이름을 사용할 수 있습니다. 그리고 `/>` 닫는 태그를 사용할 수도 있습니다.

## 스타일 가이드

[스타일 가이드 | Vue.js](https://v3.ko.vuejs.org/style-guide/#%E1%84%8B%E1%85%AE%E1%84%89%E1%85%A5%E1%86%AB%E1%84%89%E1%85%AE%E1%86%AB%E1%84%8B%E1%85%B1-b-%E1%84%80%E1%85%B2%E1%84%8E%E1%85%B5%E1%86%A8-%E1%84%8C%E1%85%A5%E1%86%A8%E1%84%80%E1%85%B3%E1%86%A8-%E1%84%80%E1%85%AF%E1%86%AB%E1%84%8C%E1%85%A1%E1%86%BC-%E1%84%80%E1%85%A1%E1%84%83%E1%85%A9%E1%86%A8%E1%84%89%E1%85%A5%E1%86%BC-%E1%84%92%E1%85%A3%E1%86%BC%E1%84%89%E1%85%A1%E1%86%BC%E1%84%8B%E1%85%B3%E1%86%AF-%E1%84%8B%E1%85%B1%E1%84%92%E1%85%A1%E1%86%B7)

# Single-File Component (SFC)

## 개요

---

Vue에서 **S**ingle-**F**ile **C**omponent(**SFC**, `*.vue` 파일)는 Vue 컴포넌트의 **템플릿(template), 로직(script), 스타일(style)**을 하나의 파일로 캡슐화하는 특수 파일 형식 입니다. 확장자는 `*.vue`이며 다음은 **SFC**의 예입니다.

```html
<template>
  <p class="greeting">{{ greeting }}</p>
</template>

<script>
export default {
  data() {
    return {
      greeting: 'Hello World!'
    }
  }
}
</script>

<style>
.greeting {
  color: red;
  font-weight: bold;
}
</style>
```

위 예시처럼 Vue SFC는 HTML, CSS, JavaScript의 문법을 유지하면서 확장한 특수 파일입니다.

## 언어 블록

---

### `<template>`

- 각 `*.vue` 파일은 한 번에 최대 하나의 `top-level <template>` 블록을 포함할 수 있습니다.
- 콘텐츠는 추출되어 `@vue/compiler-dom`으로 전달되고, JavaScript 렌더 기능으로 사전 컴파일되고, `render` 옵션으로 내보내어 컴포넌트에 첨부됩니다.

### ****`<script>`****

- 각 `*.vue` 파일은 한 번에 최대 하나의 `<script>` 블록을 포함할 수 있습니다(`<script setup>` 제외).
- 스크립트는 ES 모듈로 실행됩니다.
- `default export`는 일반 객체 또는 `defineComponent`의 반환 값으로 Vue 컴포넌트 옵션 객체여야 합니다.

### ****`<script setup>`****

- 각 `*.vue` 파일은 한 번에 최대 하나의 `<script setup>` 블록을 포함할 수 있습니다(`normal <script>` 제외).
- `<script setup>`은 사전에 처리되어 컴포넌트의 `setup()` 함수로 사용됩니다. **즉, 컴포넌트의 각 인스턴스에 대해 실행됩니다.** `<script setup>`의 최상위 바인딩은 템플릿에 자동으로 노출됩니다. 자세한 내용은 [`<script setup>` 전용 문서](https://vuejs.org/api/sfc-script-setup.html)를 참조하십시오.

### ****`<style>`****

- 단일 `*.vue` 파일에는 여러 `<style>` 태그가 포함될 수 있습니다.
- `<style>` 태그는 현재 컴포넌트에 스타일을 캡슐화하는 데 도움이 되도록 `scoped` 또는 `module` 속성(자세한 내용은 [SFC 스타일 기능](https://vuejs.org/api/sfc-css-features.html) 참조)을 가질 수 있습니다. **캡슐화 모드**가 다른 여러 `<style>` 태그를 동일한 구성 요소에서 혼합할 수 있습니다.

## Custom Blocks

---

프로젝트별 요구사항에 따라 `*.vue` 파일에 **사용자 정의 블록**을 추가할 수 있습니다. 예를 들면 다음과 같은 사용자 정의 블록 예가 있습니다.

- **[Gridsome: `<page-query>`](https://gridsome.org/docs/querying-data/)**
- **[vite-plugin-vue-gql: `<gql>`](https://github.com/wheatjs/vite-plugin-vue-gql)**
- **[vue-i18n: `<i18n>`](https://github.com/intlify/bundle-tools/tree/main/packages/vite-plugin-vue-i18n#i18n-custom-block)**

## 전처리기

---

`<script>`의 `lang`속성을 사용하여 전처리기 언어를 선언할 수 있습니다. 일반적인 경우는 TypeScript를 사용하는 것입니다.

```html
<script lang="ts">
  // use TypeScript
</script>
```

`lang` 속성은 모든 블록에 적용할 수 있습니다. 예를 들어 **SASS**와 **Pug**를 `<style>`과 `<template>`에 적용할 수 있습니다.

```html
<template lang="pug">
p {{ msg }}
</template>

<style lang="scss">
  $primary-color: #333;
  body {
    color: $primary-color;
  }
</style>
```

## Src 가져오기

---

`.vue` 컴포넌트를 여러 파일로 분할하려는 경우 `src` 속성을 사용하여 `language block`에 대한 외부 파일을 가져올 수 있습니다.

```jsx
<template src="./template.html"></template>
<style src="./style.css"></style>
<script src="./script.js"></script>
```

`src`로 가져오는 것은 webpack 모듈 요청과 동일한 경로 확인 규칙을 따릅니다. 즉, 다음을 의미합니다.

상대 경로는 ./로 시작해야 합니다.

npm 종속성에서 리소스를 가져올 수 있습니다.

```jsx
<!-- import a file from the installed "todomvc-app-css" npm package -->
<style src="todomvc-app-css/index.css" />
```

src 가져오기는 사용자 정의 블록에서도 작동합니다. 예:

```jsx
<unit-test src="./unit-test.js">
</unit-test>
```

## CSS 기능

---

### Scoped CSS

`<style>`태그에 `scoped`속성이 있는 경우 해당 CSS는 **현재 컴포넌트의 요소에만** 적용됩니다. 

```html
<template>
  <p class="greeting">greeting</p>
</template>
<style scoped>
.greeting {
  color: red;
  font-weight: bold;
}
</style>
```

원리는 PostCSS 사용하여 아래와 같이 변환 됩니다.

```html
<template>
  <p class="greeting" data-v-7ba5bd90>greeting</p>
</template>
<style scoped>
.greeting[data-v-7ba5bd90] {
  color: red;
  font-weight: bold;
}
</style>
```

### CSS 모듈

`<style module>` 은 CSS 모듈로 컴파일되고, CSS 클래스를 `$style` 객체의 속성으로 노출합니다.

```jsx
<template>
  <p :class="$style.red">This should be red</p>
</template>

<style module>
.red {
  color: red;
}
</style>
```

결과 클래스는 충돌을 피하기 위해 해시되어 CSS 범위를 현재 컴포넌트로만 지정하는 것과 동일한 효과를 얻습니다. [전역 예외](https://github.com/css-modules/css-modules#exceptions) 및 [구성](https://github.com/css-modules/css-modules#composition)과 같은 자세한 내용은 [CSS 모듈 사양](https://github.com/css-modules/css-modules)을 참조하세요.

****Custom Inject Name****

모듈 속성에 값을 제공하여 주입된 클래스 객체의 속성 키를 변경할 수 있습니다.

```jsx
<template>
  <p :class="classes.red">red</p>
</template>

<style module="classes">
.red {
  color: red;
}
</style>
```

**Composition API와 함께 사용**

주입된 클래스는 `useCssModule` API를 통해 `setup()` 및 `<script setup>`에서 접근할 수 있습니다. 사용자 정의 주입 이름이 있는 스타일 모듈 블록의 경우 `useCssModule`은 일치하는 모듈 속성 값을 첫 번째 인수로 허용합니다.

```jsx
import { useCssModule } from 'vue'

// setup() 스코프 내부...
// 기본, 스타일 모듈에 대한 클래스를 반환합니다.
useCssModule()

// 명명된, 스타일 module='classes'에 대한 클래스를 반환합니다.
useCssModule('classes')
```

### ****`v-bind()` in CSS**

SFC `<style>` 태그는 `v-bind` CSS 기능을 사용하여 CSS 값을 동적 구성 요소 상태에 연결하는 것을 지원합니다.

```jsx
<template>
  <div class="text">hello</div>
</template>

<script>
export default {
  data() {
    return {
      color: 'red'
    }
  }
}
</script>

<style>
.text {
  color: v-bind(color);
}
</style>
```

## 참고

---

- Single File Component : Spec
    
    [SFC Syntax Specification | Vue.js](https://vuejs.org/api/sfc-spec.html)
    
- Single File Component : `<script setup>`
    
    [| Vue.js](https://vuejs.org/api/sfc-script-setup.html)
    
- Single File Component : CSS Features

# Props

## Props

블로그를 구축하는 경우 블로그 게시글을 나타내는 컴포넌트가 있다고 가정해 보겠습니다. 이때 모든 블로그 게시글의 UI나 레이아웃은 동일하지만 게시글의 제목, 내용과 같은 데이터는 각각 다릅니다. 그러면 **컴포넌트에 각각 제목이나 내용과 같은 데이터를 전달해야 하는데** 이때 `Props`를 사용하여 컴포넌트로 데이터(속성)를 전달할 수 있습니다.

## Props 란?

`**Props`란? 컴포넌트에 등록할 수 있는 사용자 정의 속성**입니다. 블로그 게시글 컴포넌트에 사용자 정의 속성을 선언하면 이 컴포넌트를 사용하는 부모 컴포넌트에서 데이터(속성)를 전달할 수 있습니다.

## Props 선언

Vue 컴포넌트에는 명시적 `props` 선언이 필요합니다. 왜냐하면 컴포넌트에 전달된 외부 props가 fallthrough 속성으로 처리되어야 함을 알 수 있습니다([다음 섹션](https://vuejs.org/guide/components/attrs.html)에서 설명함).

<aside>
💡 **fallthrough 속성**
props 또는 emits에 명시적으로 선언되지 않은 속성 또는 이벤트

</aside>

### 문자열 배열 선언

컴포넌트에 `props` 옵션을 사용하여 선언할 수 있습니다.

```jsx
// BlogPost.vue
export default {
  props: ['title'],
  setup(props) {
    console.log(props.title)
  }
}
```

### 객체문법 선언

문자열 배열을 사용하여 `props`를 선언하는 것 외에도 객체 문법을 사용하여 속성 타입과 함께 선언할 수도 있습니다.

```jsx
export default {
  props: {
    title: String,
    likes: Number
  },
	setup(props) {
		console.log(props.title)
		console.log(props.likes)
	}
}
```

`props` 선언시 `key`는 속성명이고 `value`는 속성 타입입니다. 더 자세히 선언하고 싶다면 `value`에 고급 옵션인 객체를 선언할 수 있습니다.

```jsx
{
  // Basic type check
  //  (`null` and `undefined` values will allow any type)
  propA: Number,
  // Multiple possible types
  propB: [String, Number],
  // Required string
  propC: {
    type: String,
    required: true
  },
  // Number with a default value
  propD: {
    type: Number,
    default: 100
  },
  // Object with a default value
  propE: {
    type: Object,
    // Object or array defaults must be returned from
    // a factory function
    default() {
      return { message: 'hello' }
    }
  },
  // Custom validator function
  propF: {
    validator(value) {
      // The value must match one of these strings
      return ['success', 'warning', 'danger'].includes(value)
    }
  },
  // Function with a default value
  propG: {
    type: Function,
    // Unlike object or array default, this is not a factory function - this is a function to serve as a default value
    default() {
      return 'Default function'
    }
  }
}
```

- `type` : `String`, `Number`, `Boolean`, `Array`, `Object`, `Date`, `Function`, `Symbol` 모든 기본 생성자 또는 모든 사용자 정의 타입이 올 수 있습니다. (예: `Person`, `Animal`)
    
    그리고 `[Number, String]` 배열을 이용하여 여러개의 타입을 선언할 수 있습니다.
    
- `default` : 속성값이 비어 있거나 `undefined`를 전달 받는 경우 기본값을 선언할 수 있습니다. 그리고 객체 또는 배열 타입인 경우 기본값을 팩토리 함수를 사용하여 반환해야 합니다.
- `required` : 속성이 필수값이라면 `true`로 해서 설정할 수 있습니다.
- `validator` : 속성값의 유효성 검사가 필요할 때 사용할 수 있습니다.

컴포넌트 사용시 `type`, `required`, `validator` 명시된 사항을 위반할 때 개발모드에서 콘솔 경고가 발생됩니다.

## Props 사용

- 선언된 props를 `<template>`에서 바로 사용할 수 있습니다.
    
    ```jsx
    <template>
    	<p>{{ title }}</p>
    </template>
    ```
    
- `setup()` 함수의 첫 번째 매개변수로 props 객체를 받아 사용할 수 있습니다.
    
    ```jsx
    export default {
    	setup(props) {
    		return { };
    	},
    };
    ```
    
- 컴포넌트 인스턴스(this)의 `$props` 객체로 접근할 수 있습니다. **[(Options API)](https://vuejs.org/api/component-instance.html#props)**
    
    ```jsx
    <template>
    	<p>{{ $props }}</p>
    </template>
    <script>
    export default {
    	created() {
    		// 객체로 접근
    		this.$props
    
    		// 
    		this.title
    	}
    };
    </script>
    ```
    

## Props Name Casing

- `props` 선언시에는 camelCase를 사용하여 이름을 선언합니다. 이렇게 하면 속성 키로 사용할 때 따옴표를 사용할 필요가 없고 유효한 JavaScript 식별자이기 때문에 템플릿 표현식에서 직접 참조할 수 있기 때문입니다.
    
    ```jsx
    export default {
    	props: {
    		greetingMessage: String
    	}
    }
    ```
    
    ```html
    <span>{{ greetingMessage }}</span>
    ```
    
- 속성에 값을 전달할 때는 `kebab-case`를 사용하는 것을 [권장](https://vuejs.org/guide/components/props.html#props-declaration)합니다.
    
    ```html
    <MyComponent greeting-message="hello"></MyComponent>
    ```
    

## 객체를 사용하여 다중 속성 전달

객체의 모든 속성을 props로 전달하려는 경우 `v-bind`에 `전달인자(예, v-bind:prop-name)`없이 사용할 수 있습니다.

예를 들어, 다음과 같이 `post`객체가 선언되어 있다고 가정하겠습니다.

```jsx
export default {
	setup() {
		const post = ref({
			id: 1,
			title: 'Learn Vue3'
		})
		return {
			post
		}
	}
}
```

아래 두 가지 전달 방법은 동일합니다.

```html
<!-- 객체를 사용한 다중 속성 전달(전달인자 없음) -->
<BlogPost v-bind="post" />
```

```html
<BlogPost :id="post.id" :title="post.title" />
```

## 단방향 데이터 흐름

모든 `props`는 상위 속성과 하위 속성간에 **단방향 바인딩**으로 형성되어 있습니다. 만약 상위 속성이 업데이트되면 하위 속성도 업데이트되지만 그 반대는 아닙니다. 이러한 성질은 하위 속성 변경 실수로 상위 속성을 변경하여 앱의 데이터 흐름을 이해하기 어렵게 만드는 것을 방지할 수 있습니다.

또한 상위 컴포넌트가 업데이트될 때마다 하위 컴포넌트의 모든 `props`는 최신 상태도 초기화 됩니다. 그렇기 때문에 **자식 컴포넌트 내부에서 `props`를 변경하지 않아야 합니다.**

```jsx
export default {
	props: ['title'],
	setup(props) {
		// ❌ warning, props are readonly!
		props.title = 'changed title';
	}
}
```

**일반적으로 props를 하위 컴포넌트에서 변경하고 싶은 두 가지 경우가 있습니다.**

1. **prop은 초기 값을 전달하는 데 사용됩니다. 자식 컴포넌트에서 속성 값을 로컬 데이터 속성으로 사용 하고자할 때 입니다.** 이 경우 prop을 초기 값으로 사용하는 로컬 변수를 선언하는 것이 가장 좋습니다.
    
    ```jsx
    export default {
    	props: ['initialWidth', 'initialHeight'],
    	setup(props) {
    		// width는 props.initialWidth 값으로 초기화 됩니다.
    		// 향후 props 업데이트의 연결이 끊어집니다.
    		const width = ref(props.initialWidth)
    		const height = ref(props.initialHeight)
    		return {
    			width,
    			height
    		}
    	}
    }
    ```
    
2. **prop**의 값의 변환이 필요할 때 입니다. 이 경우 `computed`를 사용하면 좋습니다. 그리고 상위 속성의 변경을 유지할 수 있습니다.
    
    ```jsx
    export default {
    	props: ['size'],
    	setup(props) {
    		// 향후 props 업데이트의 연결이 유지됩니다.끊어집니다.
    		const rectangleSize = computed(() => props.size.trim().toUpperCase());
    		return {
    			rectangleSize
    		}
    	}
    }
    ```
    

### **객체 / 배열 Props 업데이트**

객체(object)나 배열(array)이 props로 전달되면 자식 컴포넌트에서는 prop 바인딩(값 변경)을 변경할 수 없지만 객체 또는 배열의 중첩 속성은 변경할 수 있습니다. 이것은 JavaScript에서 객체와 배열이 참조 타입(Reference Type)으로 전달되고 Vue가 이러한 변경을 방지하는것은 부당한 비용이 들기 때문입니다.

이러한 변경의 단점은 하위 컴포넌트가 상위 컴포넌트에 명확하지 않은 방식으로 상위 속성 업데이트 하게 되면 잠재적으로 향후 데이터 흐름을 추론하기 어렵게 만든다는 것입니다. 그렇기 때문에 가장 좋은 방법은 부모와 자식이 의도적으로 밀접하게 연관되어 있지 않는한 이러한 변경은 피하는 것입니다. 만약 변경이 필요하다면 자식 컴포넌트에서 `**emit`을 이용하여 부모 컴포넌트가 스스로 변경을 수행할 수 있도록** 이벤트를 내보내야 합니다.

## Boolean Casting

`Boolean`타입의 Props는 특별한 캐스팅 규칙이 있습니다. `<MyComponent>` 가 다음과 같이 선언되어 있습니다.

```jsx
export default {
	props: {
		disabled: Boolean
	}
}
```

`<MyComponent>`는 다음과 같이 사용할 수 있습니다.

```html
<!-- :disabled="true" 전달하는 것과 동일합니다. -->
<MyComponent disabled />

<!-- :disabled="false" 전달하는 것과 동일합니다. -->
<MyComponent />
```

## 반응형을 잃지 않는 구조분해 할당

---

### `toRef`

### `toRefs`

# Events

## Events

자식 컴포넌트에서도 부모 컴포넌트로 데이터를 전달 또는 트리거의 목적으로 이벤트를 내보는것을 말합니다. 그리고 이벤트는 컴포넌트의 `emit` 메서드를 통하여 발생시킬 수 있습니다.

## 이벤트 발생 및 수신

컴포넌트의 `<template>` 블록 안에서 내장 함수 `$emit()`을 사용하여 직접 커스텀한 이벤트를 내보낼 수 있습니다.

```html
<template>
	<button @click="$emit('someEvent')">버튼</button>
</template>
```

그러면 부모 컴포넌트에서 `v-on`(또는 `@`)을 사용하여 이벤트를 수신할 수 있습니다.

```html
<MyComponent @some-event="callFunction" />
```

`.once` 수식어는 컴포넌트 커스텀 이벤트에서도 지원됩니다.

```html
<MyComponent @some-event.once="callFunction" />
```

## 이벤트 파라미터

이벤트와 함께 특정 값을 내보낼 수 있습니다. `$emit` 함수 이벤트명에 추가로 파라미터를 넘길 수 있습니다.

```html
<template>
	<button @click="$emit('someEvent', 'Hello', 'World', '!')">버튼</button>
</template>
```

그런다음 부모 컴포넌트에서 이벤트와 함께 파라미터를 받을 수 있습니다.

```jsx
<template>
	<MyComponent @some-event="callFunction" />
</template>

<script setup>
export default {
	setup() {
		const callFunction = (word1, word2, word3) => {
      alert(word1, word2, word3);
    };
		return {
			callFunction
		}
	}
}
</script>
```

## 이벤트 선언하기

Vue3에서는 `emits` 옵션을 사용하여 이벤트를 선언할 수 있습니다. 이때 이벤트 선언하는 방법은 두 가지 형식으로 선언할 수 있습니다. 

- 문자열 배열 선언
- 객체문법 선언

그리고 JavaScript 코드에서 이벤트를 내보낼 때는 `setup()` 함수의 파라미터로 넘어온 `context.emit()` 메서드를 사용할 수 있습니다.

### 문자열 배열 선언

```jsx
export default {
  emits: ['someEvent'],
  setup(props, context) {
    context.emit('someEvent', 'Hello World!')
  }
}
```

```jsx
export default {
  emits: ['someEvent'],
  setup(props, { emit }) {
    emit('someEvent', 'Hello World!')
  }
}
```

### 객체문법 선언

객체문법으로 선언할 경우 `validation` 로직을 추가할 수 있습니다. 만약 `validation`이 없다면 `null`로 설정하시면 됩니다.

```jsx
export default {
  emits: {
		// 유효성 검사가 없는 이벤트 선언
		someEvent: null,

		// 유효성 검사가 있는 이벤트 선언
		someSubmit: (result) => {
			if (email && password) {
	      return true
	    } else {
	      console.warn('result 값이 비어있습니다!')
	      return false
	    }
		}
	},
  setup(props, context) {
    context.emit('someEvent', 'Hello World!')
  }
}
```

선택 사항이지만 컴포넌트가 작동하는 방식을 더 잘 문서화하기 위해 모든 이벤트를 정의하는 것이 좋습니다. 또한 Vue가 **[Non-Prop 속성](https://vuejs.org/guide/components/attrs.html#v-on-listener-inheritance)** 에서 알려진 리스너를 제외할 수 있습니다 .

## `v-model` 만들기

컴포넌트를 만든 후 해당 컴포넌트에 `v-model`을 적용하려면 `@update:modelValue` 이벤트를 사용하여 `v-model`을 만들 수 있습니다.

일반적으로 기본 HTML 요소인 `<input>` 태그에 `v-model` 은 아래와 같이 사용합니다.

```html
<input v-model="username" />
```

위에 선언된 `v-model`은 아래와 같이 동작합니다.

```html
<input
  :value="username"
  @input="username = $event.target.value"
/>
```

위에 기본 동작 대신 우리가 만든 컴포넌트는 아래와 같이 수행합니다.

```html
<LabelInput
	:modelValue="username"
	@update:modelValue="newValue => username = newValue"
/>
```

이 `<LabelInput>`을 실제로 동작하게 하려면 아래와 같이 컴포넌트를 정의해야 합니다.

- `modelValue` `props`를 `:value` 속성에 바인딩
- `@input` 이벤트에서 새 `@update:modelValue` 이벤트로 내보냅니다.

```html
<template>
  <label>
    {{ label }}
    <input
      type="text"
      :value="modelValue"
      @input="$emit('update:modelValue', $event.target.value)"
    />
  </label>
</template>
<script>
export default {
  props: ['modelValue', 'label'],
  emits: ['update:modelValue'],
};
</script>
```

그리고 아래와 같이 우리가 만든 컴포넌트에 `v-model`을 적용할 수 있습니다.

```html
<LabelInput label="이름" v-model="username" />
```

### Computed 이용하기

컴포넌트 안에서 computed를 사용하여 v-model을 구현할 수 있습니다.

```jsx
<template>
  <label>
    {{ label }}
    <input type="text" v-model="value" />
  </label>
</template>
<script>
import { computed } from 'vue';

export default {
  props: ['modelValue', 'label'],
  emits: ['update:modelValue'],
  setup(props, context) {
    const value = computed({
      get() {
        return props.modelValue;
      },
      set(value) {
        context.emit('update:modelValue', value);
      },
    });
    return {
      value,
    };
  },
};
</script>
```

전달할 수 있습니다. 이럴때  `Emit`을 사용할 수 있습니다.

`<BlogPost>` 컴포넌트를 개발할 때 부모에게 다시 무엇을 전달해야 할 때가 있습니다. 예를 들어 블로그 게시글 폰트 크기를 확대하는 기능이 있다고 가정해 보겠습니다.

```jsx
const postFontSize = ref(1);
```

```html
<div :style="{ fontSize: postFontSize + 'em' }">
	<BlogPost
		v-for="post in posts"
		:key="post.id"
		:title="post.title"
	/>
</div>
```

이제 `<BlogPost>`컴포넌트에서 폰트 크기를 확대할 수 있는 버튼을 추가해 보겠습니다.

```jsx
<template>
  <article>
    <h4>{{ title }}</h4>
    <button @click="$emit('enlarge-text')">크게</button>
  </article>
</template>

<script>
import { toRefs } from 'vue';

export default {
  props: ['title'],
  emits: ['enlarge-text'],
  setup(props) {
    const { title } = toRefs(props);
    return {
      title,
    };
  },
};
</script>

<style></style>
```

자식 컴포넌트에서는 `emits`옵션을 사용하여 이벤트를 선언할 수 있습니다. 그리고 `$emit` 내장 메서드를 호출하여 이벤트를 발생시킬 수 있습니다. 

```html
<div :style="{ fontSize: postFontSize + 'em' }">
  <BlogPost
    v-for="post in posts"
    :key="post.id"
    :title="post.title"
    @enlarge-text="postFontSize += 0.1"
  />
</div>
```

부모 컴포넌트에서는 `v-on`(`@`) 디렉티브를 사용하여 자식 컴포넌트로부터 전달받은 이벤트를 수신할 수 있습니다. `@enlarge-text`로 이벤트를 받아 `postFontSize` 값을 업데이트 했습니다.

### `v-model` 전달인자

기본적으로 `v-model`은 컴포넌트에서 `modelValue` `props`와 `update:modelValue` 이벤트로 사용합니다. 하지만 `전달인자(Arguments)`를 사용하여 이러한 이름을 수정할 수 있습니다.

```html
<BookComponent v-model:title="bookTitle" />
```

이 경우 자식 컴포넌트에서는 `:title`을 속성으로 정의하고 `update:title`로 이벤트를 내보내야 합니다.

```html
<template>
  <article>
    <strong>책 이름</strong> :
    <input
      type="text"
      :value="title"
      @input="$emit('update:title', $event.target.value)"
    />
  </article>
</template>
<script>
export default {
  props: ['title'],
  emits: ['update:title'],
};
</script>
```

### 다중 `v-model` 바인딩

`v-model` `전달인자`를 사용하여 컴포넌트에 여러 `v-model`을 바인딩할 수 있습니다.

```html
<BookComponent
	v-model:title="bookTitle"
	v-model:author="bookAuthor"
/>
```

```html
<template>
  <article>
    <strong>도서명</strong> :
    <input
      type="text"
      :value="title"
      @input="$emit('update:title', $event.target.value)"
    />
    <br />
    <strong>저자</strong> :
    <input
      type="text"
      :value="author"
      @input="$emit('update:author', $event.target.value)"
    />
  </article>
</template>
<script>
export default {
  props: ['title', 'author'],
  emits: ['update:title', 'update:author'],
};
</script>
```

### `v-model` 수식어(Modifiers) 핸들링

필요에 따라 `v-model` `수식어`를 추가할 수 있습니다. 예를 들어 첫 글자를 대문자로 표시하는 `capitalize` 라는 `수식어`를 만들어 보도록 하겠습니다.

```jsx
<CustomInput v-model.capitalize="username"></CustomInput>
```

컴포넌트에 추가된 `수식어`는 `modelModifiers` prop을 통해 컴포넌트에 전달됩니다. 아래 예제에서는 기본값을 빈 객체를 갖는 `modelModifiers` props를 갖는 컴포넌트 입니다.

```jsx
<template>
  <input
    type="text"
    :value="modelValue"
    @input="$emit('update:modelValue', $event.target.value)"
  />
</template>
<script>
export default {
  props: {
    modelValue: String,
    modelModifiers: { default: () => ({}) },
  },
  emits: ['update:modelValue'],
	setup(props, context) {
		// {capitalize: true} 출력
    console.log(props.modelModifiers);
  },
};
</script>
```

컴포넌트의 `modelModifiers` prop에 `capitalize`가 포함되어 있고 이 값은 `true`로 출력되는 것을 확인할 수 있습니다. 왜냐하면 부포 컴포넌트에서 `v-model.capitalize`를 사용했기 때문입니다.

이제 이벤트를 내보내기 전에 문자열 첫 글자를 대문자로 만들면됩니다.

```jsx
<template>
  <input type="text" :value="modelValue" @input="emitValue" />
</template>
<script>
export default {
  props: {
    modelValue: String,
    modelModifiers: { default: () => ({}) },
  },
  emits: ['update:modelValue'],
  setup(props, { emit }) {
    const emitValue = (e) => {
      let value = e.target.value;
      if (props.modelModifiers.capitalize) {
        value = value.charAt(0).toUpperCase() + value.slice(1);
      }
      emit('update:modelValue', value);
    };
    return {
      emitValue,
    };
  },
};
</script>
```

# Non-Prop 속성

## Non-Prop 속성 (fallthrough 속성)

**Non-Prop 속성**은 `props` 또는 `event` 에 명시적으로 선언되지 않은 속성 또는 이벤트 입니다. 예를 들어 `class`, `style`, `id`와 같은 것들이 있습니다.

## 속성 상속

컴포넌트가 단일 루트 요소로 구성되어 있으면 Non-Prop **속성**은 루트 요소의 속성에 자동으로 추가됩니다. 예를 들어 `<MyButton>` 이라는 컴포넌트가 있다고 가정해보겠습니다.

```html
<!-- template of <MyButton> -->
<button>click me</button>
```

그리고 이 컴포넌트를 사용하는 부모 컴포넌트는 다음과 같습니다.

```html
<MyButton class="large" />
```

최종 렌더링된 DOM은 다음과 같습니다.

```html
<button class="large">click me</button>
```

## `class`, `style` 속성 병합

만약 자식 컴포넌트 루트요소에 이미 `class`와 `style`속성이 정의되어 있으면, 부모로 받은 `class`와 `style`속성과 병합 합니다.

```html
<!-- template of <MyButton> -->
<button class="btn">click me</button>
```

최종 병합된 DOM은 다음과 같습니다.

```html
<button class="btn large">click me</button>
```

## `v-on` 이벤트 리스너 상속

`v-on` 이벤트 리스너도 동일하게 상속됩니다.

```html
<MyButton @click="onClick" />
```

- `@click` 리스너는 `<MyButton>`의 컴포넌트 루트요소인 `<button>`요소에 추가됩니다.
- 만약 `<button>`요소에 이미 바인딩된 이벤트가 있다면 이벤트가 추가되어 두 리스너 모두 트리거 됩니다.

## 속성 상속 비활성화

컴포넌트가 자동으로 Non-Prop **속성**을 상속하지 않도록 하려면 컴포넌트의 `inheritAttrs: false` 옵션을 설정할 수 있습니다.

```html
<template>
  <button class="btn" data-link="hello">click me</button>
</template>
<script>
export default {
  inheritAttrs: false,
};
</script>
```

컴포넌트에 Non-Prop **속성**을 비활성화 하는 일반적인 경우는 자식 컴포넌트의 루트요소에 이외의 다른 요소에 Non-Prop **속성**을 적용하고 싶을 때 입니다.

그리고 적용해야 하는 요소에 `<template>`에서 Non-Prop속성에 접근할 수 있는 내장 객체 `$attrs`로 직접 접근할 수 있습니다.

```html
<template>
  <p>Non-Prop 속성: {{ $attrs }}</p>
</template>
```

`$attrs` 객체에는 컴포넌트에 선언되지 않은 모든 속성 `props`, `emits` (예: `class`, `style`, `v-on` 등)을 포함하고 있습니다.

몇 가지 참고 사항:

- `props`와 달리 **Non-Prop 속성**은 JavaScript에서 원래 대소문자를 유지하므로 `foo-bar`와 같은 속성은 `$attrs[’foo-bar’]`로 접근해야 합니다.
- `@click`과 같은 `v-on`리스너는 `$attrs.onClick`과 같이 함수로 접근할 수 있습니다.

### Non-Prop 속성을 특정 요소에 모두 적용하기

`inheritAttrs: false`와 `$attrs`를 이용하면 **Non-Prop 속성**을 특정 요소에 모두 적용할 수 있습니다.

```html
<template>
  <label>
    이름:
    <input type="text" v-bind="$attrs" />
  </label>
</template>
<script>
export default {
  inheritAttrs: false,
};
</script>
```

부모 컴포넌트

```html
<MyInput
  class="my-input"
  placeholder="didj"
  @keyup="onKeyup"
  data-message="Hello World!"
/>
```

<aside>
💡 Vue 3에서 `$listeners` 객체가 제거되었습니다. 모든 리스너는 이제 `$attrs`의 일부가 되었습니다.

</aside>

## Fragments

Vue3에서 컴포넌트는 다중 루트 노드 컴포넌트인 fragments를 공식 지원합니다.

### Vue2.x 문법

2.x에서는 다중 루트 컴포넌트가 지원되지 않았고, 사용자가 실수로 다중 루트 컴포넌트를 만들었을 경우 경고 메세지를 내보냈습니다. 그리고 이 오류를 해결하기 위해 많은 컴포넌트가 단일 `<div>`로 감싸게 됐습니다.

```html
<!-- Layout.vue -->
<template>
  <div>
    <header>...</header>
    <main>...</main>
    <footer>...</footer>
  </div>
</template>
```

### Vue3.x 문법

3.x 에서 컴포넌트는 다중 루트 노드(multiple root node)를 가질 수 있습니다! 하지만, 개발자가 속성을 배포(상속)해야 하는 위치를 명시적으로 정의해야 합니다.

```html
<!-- Layout.vue -->
<template>
  <header>...</header>
  <main v-bind="$attrs">...</main>
  <footer>...</footer>
</template>
```

## 여러 루트노드의 속성 상속

**단일 루트 요소**가 있는 컴포넌트와 달리 **여러 루트 요소**가 있는 컴포넌트에는 자동으로 **Non-Prop 속성**이 상속되지 않습니다. 만약 명시적으로 `$attrs`를 바인딩 하지 않을 경우 런타입 경고가 발생됩니다.

**자식 컴포넌트**

```html
<!-- CustomLayout.vue -->
<template>
  <header></header>
  <main></main>
  <footer></footer>
</template>
```

**부모 컴포넌트**

```html
<CustomLayout id="custom-layout"></CustomLayout>
```

$attrs이 명시적으로 바인딩된 경우 경고가 표시되지 않습니다.

```html
<!-- CustomLayout.vue -->
<template>
  <header></header>
  <main v-bind="$attrs"></main>
  <footer></footer>
</template>
```

## JavaScript에서 Non-Prop 속성 접근

`setup()` 함수의 `context.attrs` 속성으로 노출됩니다 .

```jsx
export default {
  setup(props, context) {
    console.log(context.attrs)
  }
}
```

# Slots

## Slot 이란?

HTML 요소와 마찬가지로 우리가 만든 컴포넌트에 콘텐츠를 전달할 수 있으면 유용합니다. `<FancyButton>` 컴포넌트를 만든 후 콘텐츠를 전달해 보도록 하겠습니다.

```html
<!-- FancyButton.vue -->
<template>
	<button class="fancy-btn">
		<slot></slot>
	</button>
</template>
```

- Style
    
    ```css
    .fancy-btn {
    	color: #fff;
    	background: linear-gradient(315deg, #42d392 25%, #647eff);
    	border: none;
    	padding: 5px 12px;
    	margin: 5px;
    	border-radius: 8px;
    	cursor: pointer;
    }
    ```
    

위에 정의한 컴포넌트를 부모 컴포넌트에서 사용해보겠습니다.

```html
<FancyButton>
	<!-- 슬롯 콘텐츠 -->
	Click!!
</FancyButton>
```

`**<slot>` 요소는 부모 컴포넌트에서 제공하는 콘텐츠를 나타내는 슬롯 콘텐츠 입니다.** 그리고 슬롯은 텍스트 뿐만아니라 HTML요소, 컴포넌트 등 다양한 모든 콘텐츠가 될 수 있습니다.

```html
<FancyButton>
	<!-- 슬롯 콘텐츠 -->
  <span style="color: red">Click me</span>
  <i>!</i>
</FancyButton>
```

<img width="1000" alt="slots" src="https://user-images.githubusercontent.com/86648892/226271889-e5580ead-e4cc-4081-848e-330f4b5c5c27.png">

## ****Fallback Content****

상위 컴포넌트에서 슬롯 콘텐츠가 제공되지 않을때 슬롯에 대한 폴백(기본 콘텐츠)을 지정할 수 있습니다.

```html
<!-- FancyButton.vue -->
<template>
  <button class="btn">
    <slot>Default Click!!</slot>
  </button>
</template>
```

## Named Slots

`<slot>` 요소에 이름을 부여하여 여러개의 `<slot>`을 정의할 수 있습니다.

```html
<!-- BaseCard.vue -->
<template>
  <article>
    <div>
      <slot name="header"></slot>
    </div>
    <div>
      <slot></slot>
    </div>
    <div">
      <slot name="footer"></slot>
    </div>
  </article>
</template>
```

- `<slot>`에 `name`속성을 부여하여 특정 슬롯 콘텐츠가 렌더링 되어야 할 위치를 설정할 수 있습니다.
- `name`이 없는 `<slot>`의 이름은 암시적으로 `default`입니다.

```html
<!-- 부모 컴포넌트 사용 예시 -->
<template>
  <BaseCard>
    <template v-slot:header>제목</template>
    <template v-slot:default>안녕하세요</template>
		<template v-slot:footer>푸터</template>
  </BaseCard>
</template>
```

위 예시처럼 `name`이 부여된 `<slot>`에 콘텐츠를 전달하려면 `v-slot` 디렉티브를 사용하여 전달할 수 있습니다. 그리고 `v-slot:전달인자`를 사용하여 지정한 슬롯 콘텐츠에 전달할 수 있습니다.

`v-slot`은 `#`으로 단축 표현할 수 있습니다.

```html
<!-- 부모 컴포넌트 사용 예시 -->
<template>
  <BaseCard>
    <template #header>제목</template>
    <template #default>안녕하세요</template>
		<template #footer>푸터</template>
  </BaseCard>
</template>
```

그리고 default 슬롯은 암시적으로 처리할 수 있습니다.

```html
<!-- 부모 컴포넌트 사용 예시 -->
<template>
  <BaseCard>
    <template #header>제목</template>
		<!-- 암시적으로 default slot -->
		안녕하세요
		<template #footer>푸터</template>
  </BaseCard>
</template>
```

## Dynamic Slot Named

`v-slot` 디렉티브 전달인자에 데이터를 바인딩하여 동적으로 변경할 수도 있습니다.

```html
<BaseCard>
  <template v-slot:[dynamicSlotName]>
    ...
  </template>

  <!-- with shorthand -->
  <template #[dynamicSlotName]>
    ...
  </template>
</BaseCard>
```

## Render Scope

슬롯 콘텐츠는 상위 컴포넌트에 정의되어 있으므로 상위 컴포넌트의 데이터 영역에 접근은 가능하지만 **하위 컴포넌트의 영역에는 접근할 수 없습니다.**

## Scoped Slots

[Render Scope](https://www.notion.so/Slots-f72f67bf01b449e79358e12cc3a2beee)에서 언급했던 것처럼  슬롯 콘텐츠는 자식 컴포넌트의 데이터에 접근할 수 없습니다.

하지만 **슬롯 콘텐츠**에서 **상위 컴포넌트와 하위 컴포넌트 데이터를 모두 사용**할 수 있다면 우리는 개발할 때 매우 유용합니다.

이러한 방법으로 우리는 자식 컴포넌트에서 `<slot>` 요소를 사용할 때 props를 전달하는 것처럼 속성을 슬롯 콘텐츠에 전달할 수 있습니다.

```html
<!-- MyComponent.vue -->
<template>
  <div>
    <slot :text="greetingMessage" :count="count"></slot>
  </div>
</template>
<script>
import { ref } from 'vue';

export default {
  setup() {
    const greetingMessage = ref('Hello World!');
    const count = ref(1);
    return {
      greetingMessage,
      count,
    };
  },
};
</script>
```

`default` `<slot>`이 **하나 밖에 없는 경우**에는 `v-slot` 디렉티브를 사용하여 `props`를 전달 받을 수 있습니다.

```html
<MyComponent v-slot="slotProps">
  {{ slotProps.text }} {{ slotProps.count }}
</MyComponent>
```

구조분해할당 문법으로 더 사용하기 편리하게 받을 수 있습니다.

```html
<MyComponent v-slot="{ text, count }">
  {{ text }} {{ count }}
</MyComponent>
```

## Named Scoped Slots

이름이 부여된 슬롯도 유사하게 작동합니다. `v-slot:name="slotProps”`

# Provide and Inject

## Prop Drilling

일반적을 부모 컴포넌트에서 자식 컴포넌트로 데이터를 전달해야 할 때 **props**를 사용합니다. 하지만 규모가 큰 컴포넌트 트리가 있고 깊이 중첩된 자손 컴포넌트에 데이터를 전달해야 한다면 해당 자손 컴포넌트와 연관된 모든 자식 컨포넌트에게 동일한 prop을 전달해야 합니다.

<img width="1000" alt="propdrilling1" src="https://user-images.githubusercontent.com/86648892/226272145-5ce9d220-3735-4be4-a01b-ee5050ad2699.png">

`<Root>`에서 `<DeepChild>` 컴포넌트에 데이터를 전달하기 위해서는 `<Footer>` 컴포넌트를 거쳐 데이터를 전달해야 합니. 만약 더 긴 상위 체인이 있으면 더 많은 상위 컴포넌트들이 영향을 받습니다. 이것을 “Prop Drilling”이라고 합니다.

“Prop Drilling” 문제는 Vue3의 `provide`와 `inject`로 해결할 수 있습니다. `provide`와 `inject`를 사용하면 데이터를 제공하는 상위 컴포넌트는 **dependency provider** 역할을 합니다. 그리고 데이터를 받는 하위 컴포넌트는 깊이에 관계 없이 **dependency provider**가 제공하는 종속성(data, function 등)을 주입받을 수 있습니다.

<img width="1000" alt="propdrilling2" src="https://user-images.githubusercontent.com/86648892/226272150-84507be3-e0f9-479e-a8ff-c8762ba54c00.png">

## Provide

하위 컴포넌트 항목에 데이터를 제공하려면 **provider** 역할을 하는 상위 컴포넌트 `setup()` 함수 내부에수 있습니다.

```jsx
import { provide } from 'vue';

export default {
  setup() {
    provide('message', 'hello!');
  },
};
```

`provide()` 함수는 두 개의 파라미터를 받습니다.

- 첫 번째 파라미터는 **주입 키** : ****`문자열` 또는 `Symbol`이 될 수 있습니다. **주입 키**는 하위 컴포넌트에서 주입된 값을 조회하는 데 사용됩니다.
- 두 번째 파라미터는 **제공된 값** : 값은 refs와 같은 반응성 데이터를 포함하여 모든 유형이 될 수 있습니다.

```jsx
import { provide, ref } from 'vue';

export default {
  setup() {
    const message = ref('Hello World!');
    provide('message', message);
    return {
      message,
    };
  },
};
```

반응성 데이터를 사용하면 제곤된 값을 사용하는 하위 컴포넌트가 공급자 컴포넌트에 대한 반응 연결을 설정할 수 있습니다.

## Inject

상위 컴포넌트에서 제공한 데이터를 삽입하려면 하위 컴포넌트 `setup()` 함수 내부에서 `inject()` 함수를 사용할 수 있습니다.

```jsx
import { inject } from 'vue';
export default {
  setup() {
    const message = inject('message');
    const appMessage = inject('appMessage');
    return {
      message,
      appMessage,
    };
  },
};
```

주입된 값이 ref이면 반응성 연결을 유지할 수 있습니다.

### Injection 기본값

만약에 `inject`로 주입된 키가 상위 체인 어디에서든 제공되지 않을경우 런타임 경고가 표시됩니다. 이 때 두 번째 인자로 **기본값(Default Value)**을 설정할 수 있습니다.

```jsx
const defaultMessage = inject('defaultMessage', 'default message');
```

기본값으로 팩토리함수를 제공할 수도 있습니다.

```jsx
const defaultMessage = inject('defaultMessage', () => 'default message');
```

## Reactivity

Provide/Inject를 반응성 데이터로 제공할 때 **가능한 모든 변경을 Provider 내부에서 하는 것이 좋습니다.** 이렇게 Provider 내부에 배치되면 향후 유지관리가 용이합니다.

만약에 injector 내부 컴포넌트에서 반응성 데이터를 변경해야 하는 경우 데이터 변경을 제공하는 함수를 함께 제공하는 것이 좋습니다.

```jsx
// Provider
const message = ref('Hello World!');
const updateMessage = () => {
  message.value = 'world!';
};
provide('message', { message, updateMessage });
```

```jsx
// Injector
const { message, updateMessage } = inject('message');
```

그리고 주입된 컴포넌트에서 제공된 값을 변경할 수 없도록 하려면 `readonly()` 함수를 사용할 수 있습니다.

```jsx
import { provide, readonly, ref } from 'vue';

provide('count', readonly(count));
```

## Symbol 키 사용

대규모 애플리케이션에서 다른 개발자와 함께 작업할 때 잠재적 충돌을 피하기 위해 Symbol 주입 키를 사용하는 것이 가장 좋습니다.

```jsx
// keys.js
export const myInjectionKey = Symbol()
```

```jsx
// in provider component
import { provide } from 'vue'
import { myInjectionKey } from './keys.js'

provide(myInjectionKey, {
  /* data to provide */
})
```

```jsx
// in injector component
import { inject } from 'vue'
import { myInjectionKey } from './keys.js'

const injected = inject(myInjectionKey)
```

## App-level Provide

컴포넌트에서 데이터를 제공하는 것 외에도 App-level에서 제공할 수도 있습니다.

```jsx
import { createApp } from 'vue';
import App from './App.vue';
const app = createApp(App);
app.provide('appMessage', 'Hello app message');
app.mount('#app');
```

### Provide/Inject 사용 예

App-level에서의 Provide는 앱에서 렌더링되는 모든 컴포넌트에서 사용할 수 있습니다. 이것은 [Plugin](https://vuejs.org/guide/reusability/plugins.html)을 작성할 때 유용합니다.

Vue2에서 컴포넌트 인스턴스 객체를 추가할 때 global property에 추가 했으나, Vue3에서 Composition API Setup 함수에서는 컴포넌트 인스턴스에 접근할 수 없다.

이때 대신 Provide/Inject를 사용할 수 있다.

### 참고

[**Vue3 Config Global Properties**](https://vuejs.org/api/application.html#app-config-globalproperties)

# Lifecycle Hooks

각각의 Vue 컴포넌트 인스턴스는 생성되고 소멸될 때 사전에 정의된 몇 단계의 과정을 거치게 되는데 이를 **라이프사이클(lifecycle)**이라 합니다.

**라이프사이클 훅(Lifecycle hooks)은** 라이프사이클 단계에서 사용자가 자신의 코드를 추가할 수 있는 단계별 기능(function)입니다. 

## Lifecycle 다이어그램

다음은 인스턴스 수명 주기에 대한 다이어그램입니다. 지금 진행 중인 모든 것을 완전히 이해할 필요는 없지만 더 많이 배우고 구축함에 따라 유용한 참고 자료가 될 것입니다. 

![lifecycle](https://user-images.githubusercontent.com/86648892/226272841-a9f6fcf4-09bb-4cfc-8e3d-c1c6ad32c1b5.png)

## Lifecycle hooks 등록

컴포넌트가 렌더링을 완료하고 DOM 노드를 만든 후 `onMounted` hooks를 사용하여 코드를 실행할 수 있습니다.

```jsx
import { onMounted } from 'vue';

export default {
  setup() {
    onMounted(() => {
      console.log('컴포넌트 mounted');
    });
  },
};
```

## Lifecycle Hooks

컴포넌트 라이프 사이클의 각 단계에서 실행되는 함수들을 라이프사이클 훅이라고 합니다.

라이프사이클 훅에 접두사 `“on”`을 붙여 컴포넌트의 라이프사이클 훅에서 코드를 실행할 수 있습니다. 아래 표에있는 라이프사이클 훅은 `setup()` 함수 내에서 동기적으로 호출해야 합니다.

다음 표에서 여러 라이프사이클 훅 단계와 `setup()` 함수 내에서 호출하는 방법을 확인할 수 있습니다.

| Options API | setup 내부에서 사용 |
| --- | --- |
| beforeCreate | 필요하지 않음* |
| created | 필요하지 않음* |
| beforeMount | onBeforeMount |
| mounted | onMounted |
| beforeUpdate | onBeforeUpdate |
| updated | onUpdated |
| beforeUnmount | onBeforeUnmount |
| unmounted | onUnmounted |
| errorCaptured | onErrorCaptured |
| renderTracked | onRenderTracked |
| renderTriggered | onRenderTriggered |
| activated | onActivated |
| deactivated | ondeactivated |
| serverprefetch | onserverprefetch |

### 라이프사이클 훅

**`Creation(생성)`** → **`Mounting(장착)`** → **`Updating(수정)`** → **`Destruction(소멸)`**

## Creation

컴포넌트 초기화 단계이며 `Creation Hooks`은 라이프사이클 단계에서 가장 먼저 실행된다. 

- 아직 컴포넌트가 DOM에 추가되기 전이므로 DOM에 접근할 수 없다.
- 서버렌더링에서 지원되는 단계
- 클라이언트나 서버 렌더 단에서 처리해야 할 일이 있으면 이 단계에서 진행

### beforeCreate

컴포넌트 인스턴스가 초기화 될 때 실행됩니다. `data()` 또는 `computed`와 같은 다른 옵션을 처리하기 전에 즉시 호출됩니다.

### created

컴포넌트 인스턴스가 초기화를 완료한 후 호출되는 훅 입니다.

### setup

Composition API의 `setup()` 훅은 Options API 훅 보다 먼저 호출됩니다.

`beforeCreate`와 `created` 라이프사이클 훅은 Options API에서 사용하는 라이프사이클 훅으로 Vue3 Composition API를 활용하여 개발을 진행할 때는 `setup()`함수로 대체할 수 있습니다.

```jsx
export default {
  beforeCreate() {
  },
  created() {
  },
  setup() {
		// coding...
	}
}
```

## Mounting

DOM에 컴포넌트를 삽입하는 단계이다. `onBeforeMount`와 `onMounted`가 있다.

- 서버렌더링에서 지원되지 않는다
- 초기 렌더링 직전에 돔을 변경하고자 한다면 이 단계에서 활용할 수 있다

### onBeforeMount

컴포넌트가 마운트되기 직전에 호출됩니다.

- 대부분의 경우 사용을 권장하지 않는다

### onMounted

컴포넌트가 마운트된 후에 호출됩니다. DOM에 접근할 수 있습니다.

- 모든 자식 컴포넌트가 마운트되었음을 의미합니다.
- 자체 DOM 트리가 생성되어 상위 컴포넌트에 삽입되었음을 의미합니다.

## Updating

컴포넌트에서 사용되는 반응형 데이터가 변경되거나 어떠한 이유로 재렌더링이 발생될 때 호출된다.

- 디버깅이나 프로파일링 등을 위해 컴포넌트 재 렌더링 시점을 알고 싶을 때 사용하면 된다.

### onBeforeUpdate

반응형 상태 변경으로 인해 컴포넌트가 DOM 트리를 업데이트하기 직전에 호출 됩니다.

컴포넌트에서 사용되는 반응형 상태 값이 변해서, DOM에도 그 변화를 적용시켜야 할 때가 있습니다. 이 때, 변화 직전에 호출되는 것이 바로 onBeforeUpdate 훅입니다.

### onUpdated

반응 상태 변경으로 인해 컴포넌트가 DOM 트리를 업데이트한 후에 호출됩니다.

상위 컴포넌트의 `onUpdated`훅은 하위 컴포넌트의 훅 이후에 호출됩니다. (`Child` → `Parent`)

이 훅은 다른 상태 변경으로 인해 발생할 수 있는 컴포넌트의 DOM 업데이트 후에 호출됩니다. 특정 상태 변경 후에 업데이트된 DOM에 액세스해야 하는 경우 대신 `nextTick()`을 사용하십시오.

> **WARNING**
`onUpdated` 훅에서 컴포넌트 상태를 변경하지 마십시오. 그러면 무한 업데이트 루프가 발생할 수 있습니다!
> 

## **Destruction**

해체(소멸)단계 이며 `onBeforeUnmount`와 `onUnmounted`가 있습니다.

### onBeforeUnmount

컴포넌트가 마운트 해제되기 직전에 호출됩니다.

### onUnmounted

컴포넌트가 마운트 해제된 후 호출됩니다.

### ETC

- **[`onErrorCaptured()`](https://vuejs.org/api/composition-api-lifecycle.html#onerrorcaptured)**
- **[`onRenderTracked()`](https://vuejs.org/api/composition-api-lifecycle.html#onrendertracked)**
- **[`onRenderTriggered()`](https://vuejs.org/api/composition-api-lifecycle.html#onrendertriggered)**
- **[`onActivated()`](https://vuejs.org/api/composition-api-lifecycle.html#onactivated)**
- **[`onDeactivated()`](https://vuejs.org/api/composition-api-lifecycle.html#ondeactivated)**
- **[`onServerPrefetch()`](https://vuejs.org/api/composition-api-lifecycle.html#onserverprefetch)**

### Composition API Lifecycle

[Composition API: Lifecycle Hooks | Vue.js](https://vuejs.org/api/composition-api-lifecycle.html)

# Template Refs

Vue의 선언적 렌더링 모델은 대부분의 직접적인 DOM의 작업을 대신 수행합니다. 하지만 때론 기본 DOM요소에 직접 접근해야 하는 경우가 있을 수 있습니다. 이때 `ref` 특수 속성을 사용해서 쉽게 접근할 수 있습니다.

```html
<input type="text" ref="input" />
```

`ref`는 특수 속성입니다. **이 `ref` 특수 속성을 통해 마운트된 DOM 요소 또는 자식 컴포넌트에 대한 참조를 얻을 수 있습니다.** 

## Refs 접근하기

Composition API로 참조를 얻으려면 동일한 이름의 참조를 선언해야 합니다.

- 컴포넌트가 마운트된 후에 접근할 수 있습니다.
- `<template>` 안에서 `input`으로 `Refs`참조에 접근하려는 경우 렌더링되기 전에는 참조가 `null`일 수 있습니다.
- `<template>` 안에서 `$refs` 내장 객체로 `Refs` 참조에 접근할 수 있습니다.

```jsx
<template>
  <input ref="input" type="text" />
	<div>{{ input }}</div>
  <div>{{ $refs.input }}</div>
	<div>{{ input === $refs.input }}</div>
</template>
<script>
import { onMounted, ref } from 'vue';

export default {
  components: {},
  setup() {
    const input = ref(null);

    onMounted(() => {
      input.value.value = 'Hello World!';
      input.value.focus();
    });
    return {
      input,
    };
  },
};
</script>
```

## `v-for` 내부 참조

> v3.2.25 이상에서 동작합니다.
> 

`v-for`내부에서 `ref`가 사용될 때 `ref`는 마운트 후 요소 배열로 채워집니다.

```jsx
<script>
import { ref, onMounted } from 'vue'

export default {
	setup() {
		const list = ref([1, 2, 3])
		
		const itemRefs = ref([])
		
		onMounted(() => console.log(itemRefs.value))
		
		return {
			list,
			itemRefs
		}
	}
}
</script>

<template>
  <ul>
    <li v-for="item in list" ref="itemRefs">
      {{ item }}
    </li>
  </ul>
</template>
```

> ~~현재 v3.2.25 버전에서 버그가 확인됨.~~
> 
> 
> Template Refs는 v-for내부에서 동작하지 않음 **[vuejs/core#5525](https://github.com/vuejs/core/issues/5525)**
> 
> 해결방법 [demo1](https://stackblitz.com/edit/vue3-template-refs-with-function?file=src%2Fcomponents%2FMyList.vue) [demo2](https://stackblitz.com/edit/vue3-template-refs-with-ref-array?file=src/components/MyList.vue)
> 
> **현재 v3.2.31 버전에서 정상작동 확인함.**
> 

## Function Refs

`ref`속성에 문자열 키 대신 함수를 바인딩할 수도 있습니다.

```html
<input :ref="(el) => { /* assign el to a property or ref */ }">
```

## 컴포넌트 Refs

`ref`를 자식 컴포넌트에도 사용할 수 있습니다. `ref`로 자식 컴포넌트에 참조값을 얻게 되면 자식 컴포넌트의 모든 속성과 메서드에 대한 전체를 접근할 수 있습니다.

이러한 경우 부모/자식 컴포넌트간 의존도가 생기기 때문에 이러한 방법은 반드시 필요한 경우에만 사용해야 합니다. 그리고 일반적으로 `ref` 보다 표준 props를 사용하여 부모/자식간 상호작용을 구현해야 합니다.

자식 컴포넌트를 정의해 보겠습니다.

```jsx
// Child.vue
<template>
  <div>Child Component</div>
</template>
<script>
import { ref } from 'vue';

export default {
  setup() {
    const message = ref('Hello Child!');
    const sayHello = () => {
      alert(message.value);
    };
    return {
      message,
      sayHello,
    };
  },
};
</script>
```

부모 컴포넌트에서 자식 컴포넌트의 상태나 메서드에 접근할 수 있습니다.

```jsx
// Child.vue
<template>
  <button @click="child.sayHello()">child.sayHello()</button>
  <Child ref="child"></Child>
</template>

<script>
import { onMounted, ref } from 'vue';
import Child from './components/templateRefs/Child.vue';
export default {
  components: {
    Child,
  },
  setup() {
    const child = ref(null);
    onMounted(() => {
      console.log(child.value.message);
    });
    return { child };
  },
};
</script>
```

## $parent

자식 컴포넌트에서 상위 컴포넌트 참조하기 위해서는 `$parent` 내장객체를 사용할 수 있습니다.

# `<script setup>`

`<script setup>`은 Single-File Component 내에서 Composition API를 사용하기 위한 **syntactic sugar(문법적 설탕)** 입니다.

SFC와 Composition API를 사용하는 경우 `<script setup>`을 [사용하는 것을 권장](https://vuejs.org/api/sfc-script-setup.html#basic-syntax)드립니다. 왜냐하면 일반 `<script>`구문보다 많은 장점을 제공합니다.

- 간결한 문법으로 상용구(boilerplate)를 줄일 수 있음
- 타입스크립트를 사용한 props와 emits 선언 가능 ([공식문서](https://vuejs.org/api/sfc-script-setup.html#typescript-only-features))
- 런타임 성능의 향상(템플릿이 setup 스크립트와 같은 스코프(scope)에 있는 [render 함수](https://v3.vuejs.org/guide/render-function.html)로 컴파일되므로 프록시가 필요없음)
- 더 뛰어난 IDE 타입 추론 성능 (language 서버가 코드로부터 타입을 추론해내는 데 비용이 덜 든다)

<aside>
💡 syntactic sugar는 기능은 그대로인데 읽는 사람을 위해 직관적으로 쉽게 코드를 읽을 수 있게 만든다는 것입니다.

</aside>

## 기본 문법

`<script>` 블록에 `setup` 속성을 추가해서 시작할 수 있습니다.

```html
<script setup>
</script>
```

내부 코드는 컴포넌트의 `setup()` 함수 안의 코드로 컴파일 됩니다.

컴포넌트를 처음 가져올 때 한 번만 실행되는 `일반 <script>`와 달리, `<script setup>`는 컴포넌트의 인스턴스가 생성될 때마다 `<script setup>`내부 코드가 실행됩니다.

### Top-level에 선언

`<script setup>` 내부 최 상위에 선언된 변수, 함수, import 는 `<template>`에서 직접 사용할 수 있습니다.

```html
<script setup>
const msg = 'Hello!'

function log() {
  console.log(msg)
}
</script>

<template>
  <div @click="log">{{ msg }}</div>
	<HelloComponent></HelloComponent>
</template>
```

import 된 자원(Component, Utils 등)도 동일한 방식으로 `<template>`에서 직접 사용할 수 있습니다.

```html
<script setup>
import HelloComponent from './components/HelloComponent.vue'

</script>

<template>
	<HelloComponent></HelloComponent>
</template>
```

## Reactivity

[Reactivity APIs](https://vuejs.org/api/reactivity-core.html)(ref, reactive, computed, watch 등) 를 `<script setup>` 안에서 생성하면 `<template>`에서 직접적으로 사용가능 합니다.

```html
<template>
	<p>{{ message }}</p>
</template>
<script setup>
import { ref } from 'vue';

const message = ref('Hello World!');
</script>
```

## defineProps() & defineEmits()

`defineProps()`와 `defineEmits()` APIs를 `<script setup>` 내에 선언하여 `props`와 `emits`을 사용할 수 있습니다.

```html
<script setup>
const props = defineProps({
  foo: String
})

const emit = defineEmits(['change', 'delete'])
</script>
```

- `defineProps`와 `defineEmits`는 `<script setup>`내부에서만 사용할 수 있는 컴파일러 매크로 입니다. 그렇기 때문에 `import`할 필요가 없으면 `<script setup>`이 처리될 때 컴파일 됩니다.
- `defineProps`는 `props`옵션과 동일한 값을 허용합니다. 그리고 `defineEmits`는 `emits`옵션과 동일한 값을 허용합니다.
- `defineProps`와 `defineEmits`는 전달된 옵션을 기반으로 타입 추론을 제공합니다.
- `defineProps`와 `defineEmits`에 전달된 옵션은 `setup()`에서 `모듈 영역(module scope)`으로 호이스트됩니다. 따라서 옵션은 `setup()` 영역에 선언된 지역 변수를 참조할 수 없습니다. 만약 그렇게 하면 컴파일 오류가 발생합니다.
하지만 `import` 된 옵션은 사용할 수 있습니다. 왜냐하면 `import`도 모듈 영역으로 호이스트 되기 때문입니다.

## ****defineExpose()****

`<script setup>`을 사용하는 컴포넌트는 기본적으로 **Template Refs**나 **$parent**와 같이 컴포넌트간 통신이 닫혀 있습니다.

`<script setup>`을 사용하는 컴포넌트의 내부 데이터나 메서드를 명시적으로 노출하려면 `defineExpose()` 컴파일러 매크로를 사용할 수 있습니다.

```jsx
<script setup>
import { ref } from 'vue'

const a = 1
const b = ref(2)

defineExpose({
  a,
  b
})
</script>
```

expose는 일반 `<script>`에서도 사용할 수 있습니다.

```jsx
export default {
  setup(props, context) {
    // Expose public properties (Function)
    console.log(context.expose)
  }
}
```

## useSlots() & useAttrs()

---

`slots`과 `attrs`는 `<template>` 내부에서 `$slots`와 `$attrs`로 직접 접근해서 사용할 수 있습니다. 만약 `<script setup>` 내부에서 slots과 attrs를 사용하고 싶다면 각각 `useSlots()`, `useAttrs()` helper 메서드를 사용할 수 있습니다.

```jsx
<script setup>
import { useSlots, useAttrs } from 'vue'

const slots = useSlots()
const attrs = useAttrs() // fallthrough 속성 접근하기
</script>
```

`slots`과 `attrs` 는 일반 `<script>`에서도 사용할 수 있습니다.

```jsx
export default {
  setup(props, context) {
    // Attributes (Non-reactive object, equivalent to $attrs)
    console.log(context.attrs)

    // Slots (Non-reactive object, equivalent to $slots)
    console.log(context.slots)
  }
}
```

## `<script>`와 `<script setup>` 함께 사용

---

`<script setup>` 은 `normal <script>` 와 함께 사용할 수 있습니다. 예를 들면 다음과 같은 경우에 `normal <script>`가 필요할 수 있습니다.

- 예를 들어 `<script setup>`에서 표현할 수 없는 inheritAttrs옵션이나 Plugin을 통해 활성화된 Custom 옵션을 사용하고자 할때 `normal <script>`를 함께 선언합니다.
- `named export`를 선언 했을 때 (예: `export const data`)
- 한 번만 실행되어야 하는 로직이 있을 때

```jsx
<script>
// 일반 스크립트, 모듈 범위에서 한 번만 실행
runSideEffectOnce()

// 옵션 선언
export default {
  inheritAttrs: false,
  customOptions: {}
}
</script>

<script setup>
// 각 인스턴스 생성시 setup() 범위에서 실행
</script>
```

## Top-level `await`

---

`<script setup>` 내의 Top-level에서 `await`을 사용할 수 있습니다. 그리고 코드는 `async setup()` 이렇게 컴파일 됩니다.

```html
<script setup>
const post = await fetch(`/api/post/1`).then((r) => r.json())
</script>
```

## `vue/setup-compiler-macros`

---

`defineProps` 및 `defineEmits`와 같은 컴파일러 매크로는 `un-undef` 경고를 생성합니다.

ESLint config 파일에서 컴파일러 매크로 환경을 활성화해야 합니다. 이러한 변수를 전역적으로 노출하지 않으려면 /* 전역 defineProps, defineEmits */를 대신 사용할 수 있습니다.

# Vue-Router란?

## 뷰 라우터 (Vue Router)

뷰 라우터는 Vue.js를 이용하여 싱글 페이지 애플리케이션(SPA)을 구현할 때 사용하는 Vue.js의 공식 라우터 입니다.

[Getting Started | Vue Router](https://router.vuejs.org/guide/)

### **라우터란? (Router)**

라우터라고 하면 일반적으로 네트워크간에 데이터를 전송하는 장치를 말합니다. 뷰에서 말하는 라우터는 쉽게 말해서 URL에 따라 어떤 페이지를 보여줄지 매핑해주는 라이브러리라고 보시면 될 것 같습니다.

예를 들어 “`‘/home’` 경로로 요청이 들어왔을때 `‘Home.vue’` 컴포넌트를 화면에 렌더링 해라!” 라는 역할을 수행하는 라이브러리라고 보시면 될 것 같습니다. 그리고 이때 `‘/home’` → `‘Home.vue’` 이러한 매핑정보를 라우트(Route)라고도 합니다.

### 라우트란? (Route)

어떤 URL에 대해 어떤 페이지를 표시해야 하는지에 대한 정보

## 설치

```bash
npm install vue-router
```

## 시작하기

`HomeView.vue`와 `AboutView.vue`라는 **페이지용 컴포넌트**를 만든후 `‘/’` 경로로 들어왔을 경우 `HomeView.vue` 페이지(컴포넌트)를 렌더링 하고 `‘/about’` 경로로 들어왔을 경우 `AboutView.vue` 페이지(컴포넌트)를 렌더링 하는 실습을 진행해 보도록 하겠습니다.

- `‘/’` → `HomeView.vue`
- `‘/about’` → `AboutView.vue`

### 페이지 컴포넌트 생성

`HomeView.vue`와 `AboutView.vue` 페이지(컴포넌트)를 생성해보도록 하겠습니다.

```jsx
// src/views/HomeView.vue
<script setup></script>
<template>
  <h1>Home Page</h1>
</template>
```

```jsx
// src/views/AboutView.vue
<script setup></script>
<template>
  <h1>About Page</h1>
</template>
```

### 라우트(routes) 정의

먼저 URL 요청에 대해 어떤 페이지(컴포넌트)를 보여줄지에 대한 매핑정보를 정의해보도록 하겠습니다.

```jsx
// src/router/index.js
import HomeView from '@/views/HomeView.vue';
import AboutView from '@/views/AboutView.vue';

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
  },
  {
    path: '/about',
    name: 'about',
    component: AboutView,
  },
];
```

### 라우터(router) 설정

라우터를 설정해보도록 하겠습니다.

```jsx
// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '@/views/HomeView.vue';
import AboutView from '@/views/AboutView.vue';

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
  },
  {
    path: '/about',
    name: 'about',
    component: AboutView,
  },
];
const router = createRouter({
  history: createWebHistory('/'),
  routes,
});

export default router;
```

설정한 라우터 객체를 Vue 인스턴스에 추가해보도록 하겠습니다.

```jsx
import { createApp } from 'vue';

import App from './App.vue';
import router from './router';

createApp(App).use(router).mount('#app');
```

`app.use(router)`를 호출 함으로써 컴포넌트 내부에서 `$router`, `$route` 객체에 접근할 수 있습니다.

## 네비게이션

뷰 라우터를 HTML과 JavaScript로 사용하는 방법에 대해 알아보도록 하겠습니다.

### HTML

```jsx
// src/App.vue
<script setup></script>

<template>
  <nav>
    <Routerlink to="/">Home</Routerlink>
    <span> | </span>
    <RouterLink to="/about">About</RouterLink>
  </nav>
  <main>
    <RouterView></RouterView>
  </main>
</template>
```

- `<RouterLink>`
    
    Vue Router 에서는 페이지를 이동할 때는 일반 `a`태그를 사용하는 대신 **커스텀 컴포넌트인** `<RouterLink>`를 사용하여 다른 페이지 링크를 만들어야 합니다.
    
    이를 통해 **Vue Router는 페이지를 리로딩 하지 않고 URL에 매핑된 페이지를 렌더링**할 수 있습니다.
    
- `<RouterView>`
    
    `<RouterView>`는 URL에 매핑된 컴포넌트를 화면에 표시합니다.
    

### JavaScript

위에서 `router`를 설정할 때 `app.use(router)`를 호출했습니다. 이렇게 호출 함으로써 모든 자식 컴포넌트에 `router`, `route` 같은 객체를 사용할 수 있습니다. 그리고 이러한 객체는 페이지 이동 또는 현재 활성 라우트(경로 매핑)정보 에 접근하는 데 사용할 수 있습니다.

- `router`
    
    라우터 인스턴스로 JavaScript에서 다른 페이지(컴포넌트)로 이동할 수 있다.
    
    - Options API : **this.$router**
    - Composition API : [**useRouter()**](https://router.vuejs.org/api/#userouter)
    - template : $router
- `route`
    
    현재 활성 라우트 정보에 접근할 수 있다. (이 속성은 읽기 전용 입니다.)
    
    - Options API : **this.$route**
    - Composition API : [**useRoute()**](https://router.vuejs.org/api/#useroute)
    - template : $route

```html
<!-- HomeView.vue -->
<script setup>
import { useRoute, useRouter } from 'vue-router';

const router = useRouter();
const route = useRoute();
console.log('route.name: ', route.name);
console.log('route.path: ', route.path);
const goAboutPage = () => router.push('/about');
</script>
<template>
  <h1>Home Page</h1>
  <button @click="goAboutPage">About 페이지로 이동</button>
</template>
```

```html
<!-- AboutView.vue -->
<script setup></script>
<template>
  <h1>About Page</h1>
  <ul>
    <li>$route.name: {{ $route.name }}</li>
    <li>$route.path: {{ $route.path }}</li>
  </ul>
  <button @click="$router.push('/')">Home 페이지로 이동</button>
</template>
```

## components.d.ts

로컬 컴포넌트, 내장 컴포넌트, 기본 HTML 요소 구성 없이 Type-Checking을 사용할 수 있습니다.

전역 컴포넌트의 경우 GlobalComponents 인터페이스를 정의해야 합니다. 예를 들면 다음과 같습니다.

# Vue-Router 학습

## 동적 라우트 매칭

주어진 패턴을 가진 라우트를 동일한 컴포넌트에 매핑해야하는 경우가 자주 있습니다. 예를 들어 **사용자 목록(User List)**은 `/users`와 같은 경로에 매핑되면 되지만 **사용자 상세(User Detail)**는 **사용자 식별자 별로 같은 컴포넌트에 매핑** 되어야 합니다. (예:  `/users/alice`, `/users/emma`, `...` → `UserComponent.vue`)

이럴때 Vue Router에서는 경로에서 동적 세그먼트를 사용하여 해결할 수 있습니다. 이를 `param`이라고 합니다.

```jsx
const User = {
  template: '<div>User</div>',
}

const routes = [
  { path: '/users/:id', component: User },
]
```

이제 `/users/alice`, `/users/emma` URL은 모두 같은 경로(`’/users/:id’`)에 매핑됩니다.

- 동적 세그먼트는 콜론(`:`)으로 표시합니다.
- 그리고 컴포넌트에서 동적 세그먼트의 값은 `$route.params` 필드로 접근할 수 있습니다.

```jsx
const User = {
  template: '<div>User {{ $route.params.id }}</div>',
}
```

동일한 라우트에 여러 동적 세그먼트를 가질 수 있으며, `$route.params` 필드에 매핑됩니다.

| path | URL example | $route.params |
| --- | --- | --- |
| /users/:username | /users/alice | { username: ‘alice’ } |
| /users/:username/posts/:postId | /users/alice/posts/123 | { username: ‘alice’, postId: ‘123’ } |

### `query`, `hash`

`$route.params` 외에도 `$route` 객체는 `$route.query(쿼리스트링)`, `$route.hash(해시태그)` 등과 같은 다른 유용한 정보도 노출합니다.

| URL example | $route |
| --- | --- |
| /users?searchText=love | { params: {...}, hash: '...', query: { searchText: love } } |
| /users/alice#profile | { params: {...}, hash: 'profile', query: { ... } } |

다른 유용한 정보를 더 확인하시려면 [**API Reference**](https://router.vuejs.org/api/#routelocationnormalized)를 참고하세요.

### 404 Not Found Route

일반 파라미터(`:id`)는 슬래쉬(`/`)로 구분된 URL 사이의 문자만 일치시킵니다. 무엇이든 일치시키려면 param 바로 뒤에 괄호 안에 정규식(`regexp`)을 사용할 수 있습니다.

```jsx
const routes = [
  // will match everything and put it under `$route.params.pathMatch`
  { path: '/:pathMatch(.*)*', name: 'NotFound', component: NotFound },
  // will match anything starting with `/user-` and put it under `$route.params.afterUser`
  { path: '/user-:afterUser(.*)', component: UserGeneric },
]
```

## 프로그래밍 방식 네비게이션

`<RouterLink>`를 사용하여 선언적 네비게이션용 anchor 태그를 사용하는 것 외에도 라우터 인스턴스 메소드를 사용하여 프로그래밍 방식으로 이를 수행 할 수 있습니다.

### `router.push`

다른 URL로 이동하려면 `router.push`를 사용할 수 있습니다. 이 메소드는 새로운 항목을 히스토리 스택에 넣기 때문에 사용자가 브라우저의 뒤로 가기 버튼을 클릭하면 이전 URL로 이동하게 됩니다.

이 메소드는 `<RouterLink>`를 클릭 할 때 내부적으로 호출되는 메소드이므로 `<RouterLink :to=”...”>`를 클릭하면 `router.push(...)`를 호출하는 것과 같습니다

| 선언적 방식 | 프로그래밍 방식 |
| --- | --- |
| <RouterLink :to=”...”> | router.push(...) |

```html
<RouterLink :to="..."></RouterLink>
```

`router.push` 파라미터는 문자열 경로 또는 객체가 될 수 있습니다.

```jsx
// 리터럴 문자열 경로
router.push('/users/eduardo')

// 경로가 있는 개체
router.push({ path: '/users/eduardo' })

// 이름을 가지는 라우트
router.push({ name: 'user', params: { username: 'eduardo' } })

// 쿼리와 함께 사용, 결과적으로 /register?plan=private가 됩니다.
router.push({ path: '/register', query: { plan: 'private' } })

// 해시와 함께 사용, 결과적으로 /about#team가 됩니다.
router.push({ path: '/about', hash: '#team' })
```

```jsx
const username = 'eduardo'
// URL을 수동으로 작성할 수 있지만 인코딩을 직접 처리해야 합니다.
router.push(`/user/${username}`) // -> /user/eduardo
// 위와 동일
router.push({ path: `/user/${username}` }) // -> /user/eduardo
// 가능하면 `name`과 `params`를 사용하여 자동 URL 인코딩의 이점을 얻습니다.
router.push({ name: 'user', params: { username } }) // -> /user/eduardo
// `params`는 `path`와 함께 사용할 수 없습니다.
router.push({ path: '/user', params: { username } }) // -> /user
```

### `router.replace`

`router.push`와 같은 역할을 하지만 유일한 차이는 새로운 히스토리 항목에 추가하지 않고 탐색한다는 것입니다. 이름에서 알 수 있듯이 현재 항목을 대체합니다.

| 선언적 방식 | 프로그래밍 방식 |
| --- | --- |
| <router-link :to=”...” replace> | router.replace(...) |

`router.push` 메소드에 `replace: true`속성을 추가하여 동일하게 동작시킬 수 있습니다.

```jsx
router.push({ path: '/home', replace: true })
// equivalent to
router.replace({ path: '/home' })
```

### `router.go(n)`

이 메소드는 `window.history.go(n)`와 비슷하게 히스토리 스택에서 앞으로 또는 뒤로 이동하는 단계를 나타내는 하나의 정수를 매개 변수로 사용합니다.

```jsx
// 한 단계 앞으로 갑니다. history.forward()와 같습니다. history.forward()와 같습니다.
router.go(1)

// 한 단계 뒤로 갑니다. history.back()와 같습니다.
router.go(-1)

// 3 단계 앞으로 갑니다.
router.go(3)

// 지정한 만큼의 기록이 없으면 자동으로 실패 합니다.
router.go(-100)
router.go(100)
```

## ****Params 변경 사항에 반응하기****

매개 변수와 함께 라우트를 사용할 때 주의 해야할 점은 사용자가 `/users/alice`에서 `/users/emma`로 이동할 때 **동일한 컴포넌트 인스턴스가 재사용된다는 것입니다.** 왜냐하면 두 라우트 모두 동일한 컴포넌트를 렌더링하므로 이전 인스턴스를 삭제 한 다음 새 인스턴스를 만드는 것보다 효율적입니다. **그러나 이는 또한 컴포넌트의 라이프 사이클 훅이 호출되지 않음을 의미합니다.**

이렇게 동일한 컴포넌트를 재사용할 때 URL이 변경되게 되면 라이프사이클 훅이 호출되지 않기 때문에 훅에서 하던 일을 할 수 없습니다.

이럴 때는 `Watcher(watch, watchEfffect)` 또는 `beforeRouteUpdate` [**navigation guard**](https://router.vuejs.org/guide/advanced/navigation-guards.html)를 사용하여 `params`와 같은 URL 변경사항에 반응할 수 있습니다.

### watch를 통한 params 반응하기

```jsx
// <script setup>
import { useRoute, watch } from 'vue-router';

const route = useRoute();

watch(
  () => route.params,
  (toParams, previousParams) => {
		// working
  }
);
```

### beforeRouteUpdate

동일한 컴포넌트를 재사용할 때 URL이 변경되는 경우 호출됩니다. 

**Options API**

```jsx
export default {
	beforeRouteUpdate(to, from) {
		// working
		this.userData = await fetchUser(to.params.id)
	}
}
```

**Composition API**

```jsx
// <script setup>
import { onBeforeRouteUpdate } from 'vue-router';
onBeforeRouteUpdate((to, from) => {
  console.log('onBeforeRouteUpdate');
});
```

## 이름을 가지는 라우트 (Named Routes)

Router 인스턴스를 생성할 때 `path`와 함께 `name`을 지정할 수 있습니다. 

```jsx
const routes = [
  {
    path: '/user/:username',
    name: 'user',
    component: User
  }
]
```

이름을 가진 라우트에 링크하려면, 객체를 `router-link` 컴포넌트의 `to` prop로 전달할 수 있습니다.

```jsx
<router-link :to="{ name: 'user', params: { username: 'erina' }}">
  User
</router-link>
```

이것은 `router.push()`와 프로그램적으로 사용되는 것과 정확히 같은 객체입니다.

```jsx
router.push({ name: 'user', params: { username: 'erina' } })
```

두 경우 모두 라우터는 `/user/erina` 경로로 이동합니다.

## 이름을 가지는 뷰 (Named Views)

때로는 여러 개의 뷰(`router-view`)를 중첩하지 않고 동시에 표시해야 하는 경우가 있습니다. 이때 `router-view`에 이름을 지정하여 여러개의 `router-view`를 사용할 수 있습니다. 그리고 이름이 없는 `router-view`는 `default`가 이름으로 주어집니다.

```jsx
<router-view class="view left-sidebar" name="LeftSidebar"></router-view>
<router-view class="view main-content"></router-view>
<router-view class="view right-sidebar" name="RightSidebar"></router-view>
```

뷰는 컴포넌트를 사용하여 렌더링 되므로 여러 뷰에는 동일한 라우트에 대해 여러 컴포넌트가 필요합니다. `components`(s를 붙입니다) 옵션을 사용해야합니다.

```jsx
const router = createRouter({
  history: createWebHashHistory(),
  routes: [
    {
      path: '/',
      components: {
        default: Home,
        // short for LeftSidebar: LeftSidebar
        LeftSidebar,
        // they match the `name` attribute on `<router-view>`
        RightSidebar,
      },
    },
  ],
})
```

## 중첩된 라우트(Nested Routes)

실제 앱 UI는 일반적으로 여러 단계로 중첩 된 컴포넌트로 이루어져 있습니다. URL의 세그먼트가 중첩 된 컴포넌트의 특정 구조와 일치한다는 것은 매우 일반적입니다. 예를 들면 다음과 같습니다.

```jsx
/user/johnny/profile                  /user/johnny/posts
+------------------+                  +-----------------+
| User             |                  | User            |
| +--------------+ |                  | +-------------+ |
| | Profile      | |  +------------>  | | Posts       | |
| |              | |                  | |             | |
| +--------------+ |                  | +-------------+ |
+------------------+                  +-----------------+
```

`vue-router`를 사용하면 중첩 된 라우트 구성을 사용하여이 관계를 표현하는 것이 매우 간단합니다.

```html
<!-- App.vue -->
<div id="app">
	<router-view></router-view>
</div>
```

```html
<!-- User.vue -->
<div class="user">
	<h2>User {{ $route.params.id }}</h2>
</div>
```

```jsx
// router/index.js
const routes = [
  {
    path: '/user/:id',
    component: User,
  },
]
```

`App.vue`에 있는 `<router-view>`는 최상위 `router-view`입니다. 이 `router-view`는 `routes`의 최상위 `path`와 일치하는 컴포넌트(`User.vue`)가 렌더링 됩니다.

그리고 `User.vue` 컴포넌트 내부에 중첩된 `<router-view>`를 선언할 수 있습니다.

```html
<!-- User.vue -->
<div class="user">
	<h2>User {{ $route.params.id }}</h2>
	<router-view></router-view>
</div>
```

그리고 컴포넌트를 이 중첩된 `<router-view>`로 렌더링하려면 `routes` 안의 `children` 옵션을 사용해야 합니다.

```jsx
// router/index.js
const routes = [
  {
    path: '/user/:id',
    component: User,
    children: [
      {
        path: 'profile',
        component: UserProfile,
      },
      {
        path: 'posts',
        component: UserPosts,
      },
    ],
  },
]
```

```html
<!-- UserProfile.vue -->
<div class="user-profile">
	User Profile
</div>
```

```html
<!-- UserPosts.vue -->
<div class="user-posts">
	User Posts
</div>
```

### 참고

- `**/`로 시작하는 중첩 경로는 루트 경로로 처리됩니다. 이를 통해 중첩 URL을 사용하지 않고도 컴포넌트 중첩을 활용할 수 있습니다.**
- 위 routes 설정으로 보면 `/users/alice`로 방문 했을 때 `User 컴포넌트`에 있는 중첩된 `<router-view>`에는 아무것도 렌더링 되지 않습니다.  이러한 경우 빈 중첩 경로를 제공할 수 있습니다.
    
    ```jsx
    const routes = [
      {
        path: '/user/:id',
        component: User,
        children: [
          { path: '', component: UserHome },
    
          // ...other sub routes
        ],
      },
    ]
    ```
    

## 라우트 컴포넌트에 속성 전달

컴포넌트에서 `$route`객체를 사용하면 특정 URL에서만 사용할 수 있게되어 라우트와 강한 결합을 만듭니다. 즉 컴포넌트의 유연성이 제한됩니다. 이러한 결합이 꼭 나쁜 것은 아니지만 `props`옵션으로 이 동작을 분리할 수 있습니다.

컴포넌트와 라우터 속성을 분리하려면 다음과 같이 하십시오.

**라우트에 의존된 컴포넌트**

```jsx
const User = {
  template: '<div>User {{ $route.params.id }}</div>'
}
const routes = [{ path: '/user/:id', component: User }]
```

**라우트 의존도 해제**

```jsx
const User = {
  // make sure to add a prop named exactly like the route param
  props: ['id'],
  template: '<div>User {{ id }}</div>'
}
const routes = [{ path: '/user/:id', component: User, props: true }]
```

이를 통해 어디서나 컴포넌트를 사용할 수 있으므로 컴포넌트 재사용 및 테스트하기가 더 쉽습니다.

### ****Boolean 모드****

`props`를 `true`로 설정하면 `route.params`가 컴포넌트 `props`로 설정됩니다.

### Named views

이름을 가지는 뷰(Named Views)가 있는 경우 각 Named Views에 대한 `props` 옵션 을 정의해야 합니다 .

```jsx
const routes = [
  {
    path: '/user/:id',
    components: { default: User, sidebar: Sidebar },
    props: { default: true, sidebar: false }
  }
]
```

### 객체 모드

`props`가 객체일때 컴포넌트 `props`가 있는 그대로 설정됩니다. `props`가 정적일 때 유용합니다.

```jsx
const routes = [
  {
    path: '/promotion/from-newsletter',
    component: Promotion,
    props: { newsletterPopup: false }
  }
]
```

### 함수 모드

`props`를 반환하는 함수를 만들 수 있습니다. 이를 통해 전달인자를 다른 타입으로 캐스팅하고 적정인 값을 라우트 기반 값과 결합됩니다.

```jsx
const routes = [
  {
    path: '/search',
    component: SearchUser,
    props: route => ({ query: route.query.q })
  }
]
```

## 다양한 history 모드

Router 인스턴스를 생성할 때 `[history](https://router.vuejs.org/api/#history)` 옵션을 사용하면 다양한 history mode 중에서 선택할 수 있습니다.

- Hash - ****[createWebHashHistory()](https://router.vuejs.org/api/#createwebhashhistory)**
- History - ****[createWebHistory()](https://router.vuejs.org/api/#createwebhistory)****
- Memory - ****[createMemoryHistory()](https://router.vuejs.org/api/#creatememoryhistory)****

### Hash 모드

Vue Router를 통해 URL로 페이지를 전환할 때 히스토리 관리 기법를 해시(`#`)형으로 쓸 수 있게 해줍니다.

해시모드는 `[createWebHashHistory()](https://router.vuejs.org/api/#createwebhashhistory)`를 사용하여 생성됩니다.

```jsx
import { createRouter, createWebHashHistory } from 'vue-router'

const router = createRouter({
  history: createWebHashHistory(),
  routes: [
    //...
  ],
})
```

내부적으로 전달되는 실제 URL 앞에 해시 문자(`#`)를 사용합니다. URL의 이 섹션은 서버로 전송되지 않으므로 서버 수준에서 특별한 처리가 필요하지 않습니다. **그러나 그것은 SEO에 나쁜 영향을 미칩니다** . 그게 걱정된다면 HTML5 모드(`createWebHistory()`****)****를 사용하세요.

### History 모드 (HTML5 모드)

Vue Router를 통해 URL로 페이지를 전환할 때 히스토리 관리 기법를 해시(`#`)없이 쓸 수 있게 해줍니다. Web API인 `history.pushState()`를 활용하여 페이지를 다시 로드하지 않고도 URL 탐색을 할 수 있습니다.

HTML5 모드는 `[createWebHistory()](https://router.vuejs.org/api/#createwebhistory)`로 생성되며 권장 모드입니다.

```jsx
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    //...
  ],
})
```

`createWebHistory()`를 사용하면 URL은 “정상"으로 보입니다. 

하지만 여기에 문제가 있습니다. 우리의 앱이 적절한 서버 설정이 없는 단일 페이지 클라이언트 앱이기 때문에 사용자가 직접 `http://oursite.com/user/id`에 접속하면 404 오류가 발생합니다.

걱정하지 않아도됩니다. 문제를 해결하려면 서버에 간단하게 포괄적인 대체 경로를 추가하기만 하면됩니다. URL이 정적 에셋과 일치하지 않으면 앱이 있는 동일한 `index.html`
페이지를 제공해야 합니다.

### 서버 설정 및 주의 사항

서버설정 및 주의 사항은 공식홈페이지를 참고하시는 것을 권장드립니다.

[HTML5 히스토리 모드 | Vue Router](https://v3.router.vuejs.org/kr/guide/essentials/history-mode.html#%E1%84%89%E1%85%A5%E1%84%87%E1%85%A5-%E1%84%89%E1%85%A5%E1%86%AF%E1%84%8C%E1%85%A5%E1%86%BC-%E1%84%8B%E1%85%A8%E1%84%8C%E1%85%A6)

## 참고

- Vue Router v4
    
    [Programmatic Navigation | Vue Router](https://router.vuejs.org/guide/essentials/navigation.html)
    
- Vue Router v3 KR
    
    [중첩된 라우트 | Vue Router](https://v3.router.vuejs.org/kr/guide/essentials/nested-routes.html)
    
- ref vs reactive
    
    [Vue 3 Composition API: ref() vs. reactive()](https://markus.oberlehner.net/blog/vue-3-composition-api-ref-vs-reactive/)

# 네비게이션 가드

## 네비게이션 가드(navigation guard)

이름에서 알 수 있듯이 Vue Router에서 제공하는 네비게이션 가드는 주로 페이지 이동을 리다이렉션 하거나 취소하여 특정 페이지 진입을 보호하는 데 사용됩니다.

라우트 탐색 프로세스에 연결하는 방법에는 **전역**, **라우트별** 또는 **컴포넌트**가 있습니다.

## 전역가드

### Global Before Guards

`router.beforeEach`를 사용하여 전역 가드를 등록할 수 있습니다.

```jsx
const router = createRouter({ ... })

router.beforeEach((to, from) => {
  // ...
  // 네비게이션을 취소하려면 명시적으로 false를 반환합니다.
  return false
})
```

네비게이션이 트리거될 때마다 가드가 작성 순서에 따라 호출되기 전의 모든 경우에 발생합니다. 가드는 비동기식으로 실행 될 수 있으며 네비게이션은 모든 훅이 해결되기 전까지 **보류 중** 으로 간주됩니다.

모든 가드 함수는 두 개의 인수를 받습니다.

- `to`: 라우팅 되는 ****[RouteLocationNormalized](https://router.vuejs.org/api/#routelocationnormalized)** 객체 (라우트 위치 정보를 담고 있는 객체)
- `from`: 라우팅 되기 전의 ****[RouteLocationNormalized](https://router.vuejs.org/api/#routelocationnormalized)** 객체 (라우트 위치 정보를 담고 있는 객체)

그리고 선택적으로 다음 값 중 하나를 반환할 수 있습니다.

- `false`: 현재 라우팅(네비게이션)을 취소합니다.
- A [Route Location](https://router.vuejs.org/api/#routelocationraw): 경로 위치를 반환하여 다른 위치로 리다이렉션할 수 있습니다. 이때 전달될 값은 `router.push()`를 호출할 때와 같은 값을 내보내면 됩니다.

만약 `undefined` 또는 `true`가 반환되면 해당 네비게이션 가드가 검증이 된것으로 판단되어 다음 네비게이션 가드를 수행합니다.

**Optional third argument `next`**

Vue Router의 이전 버전에서는 세 번째 인수 `next`를 사용할 수도 있었는데 이는 일반적인 실수의 원인이었으며 [RFC](https://github.com/vuejs/rfcs/blob/master/active-rfcs/0037-router-return-guards.md#motivation) 를 통해 제거했습니다.

```jsx
// BAD
router.beforeEach((to, from, next) => {
  if (to.name !== 'Login' && !isAuthenticated) next({ name: 'Login' })
  // if the user is not authenticated, `next` is called twice
  next()
})
```

```jsx
// GOOD
router.beforeEach((to, from, next) => {
  if (to.name !== 'Login' && !isAuthenticated) next({ name: 'Login' })
  else next()
})
```

### Global Resolve Guards

`router.beforeResolve`로 글로벌 가드를 등록할 수 있습니다. 이는 `router.beforeEach`와 유사합니다. 모든 컴포넌트 가드와 비동기 라우트 컴포넌트를 불러온 후 네비게이션 가드를 확인하기 전에 호출된다는 차이가 있습니다.

```jsx
router.beforeResolve(async to => {
  if (to.meta.requiresCamera) {
    try {
      await askForCameraPermission()
    } catch (error) {
      if (error instanceof NotAllowedError) {
        // ... 오류를 처리한 다음 탐색을 취소합니다.
        return false
      } else {
        // 예기치 않은 오류, 탐색을 취소하고 오류를 전역 처리기에 전달
        throw error
      }
    }
  }
})
```

데이터를 가져오거나 사용자가 페이지에 들어갈 수 없는 경우 피하고 싶은 다른 작업을 수행하기에 이상적인 장소입니다.

### ****Global After Hooks****

전역 훅을 등록 할 수도 있지만, 가드와 달리 이 훅은 `next` 함수를 얻지 못하며 네비게이션에 영향을 줄 수 없습니다.

```jsx
router.afterEach((to, from) => {
  // ...
})
```

## 라우트 가드

`beforeEnter` 가드를 라우트의 설정 객체에 직접 정의 할 수 있습니다.

```jsx
const routes = [
  {
    path: '/users/:id',
    component: UserDetails,
    beforeEnter: (to, from) => {
      // reject the navigation
      return false
    },
  },
]
```

`beforeEnter`가드는 해당 라우트에 진입할 때만 트리거 됩니다. 그리고 같은 URL이면서 `params`, `query`, `hash`의 변경이 일어났을 때는 트리거 되지 않습니다. 가드는 오직 다른 라우트로 네비게이션 할때만 트리거 됩니다.

`beforeEnter`가드에 함수의 배열을 전달할 수 있습니다. 이것은 다른 라우트에 설정한 가드를 재사용할 때 유용합니다.

```jsx
function removeQueryParams(to) {
  if (Object.keys(to.query).length)
    return { path: to.path, query: {}, hash: to.hash }
}

function removeHash(to) {
  if (to.hash) return { path: to.path, query: to.query, hash: '' }
}

const routes = [
  {
    path: '/users/:id',
    component: UserDetails,
    beforeEnter: [removeQueryParams, removeHash],
  },
  {
    path: '/about',
    component: UserDetails,
    beforeEnter: [removeQueryParams],
  },
]
```

[**route meta fields**](https://router.vuejs.org/guide/advanced/meta.html)와 [**global navigation guards**](https://router.vuejs.org/guide/advanced/navigation-guards.html#global-before-guards)를 사용하여 유사한 동작을 달성할 수 있습니다.

## 컴포넌트 내 가드

마지막으로 라우트 컴포넌트(라우터 구성에 전달되는 컴포넌트) 내부에 라우트 네비게이션 가드를 직접 정의할 수 있습니다.

### Options API 사용

컴포넌트를 라우팅하기 위해 다음 옵션을 추가할 수 있습니다.

- `beforeRouteEnter`
- `beforeRouteUpdate`
- `beforeRouteLeave`

```jsx
const UserDetails = {
  template: `...`,
  beforeRouteEnter(to, from) {
    // 네비게이션 이동이 확정된 후 컴포넌트가 만들어 지기 전에 실행되는 가드입니다.
		// `this` 구성 요소 인스턴스에 대한 액세스 권한이 없습니다.
		// 이 가드가 호출될 때 아직 생성되지 않았기 때문입니다!
  },
  beforeRouteUpdate(to, from) {
		// 이 컴포넌트를 렌더링하는 경로가 변경되면 호출됩니다.
		// 하지만 이 구성 요소는 새 경로에서 재사용됩니다.
		// 예를 들어 `/users/:id` 매개변수가 있는 경로가 주어지면
		// `/users/1`과 `/users/2` 사이를 탐색합니다. 동일한 `UserDetails` 구성요소 인스턴스입니다.
		// 재사용되며, 이 경우 이 후크가 호출됩니다.
		// 이 과정에서 구성 요소가 마운트되기 때문에 탐색 가드는 `this` 구성 요소 인스턴스에 액세스할 수 있습니다.
  },
  beforeRouteLeave(to, from) {
		// 라우트를 떠날 떄 실행되는 가드입니다.
		// 멀리 탐색합니다.
		// `beforeRouteUpdate`와 마찬가지로 `this` 구성 요소 인스턴스에 액세스할 수 있습니다.
  },
}
```

`beforeRouteEnter`가드는 `this`에 대한 액세스 권한이 **없습니다** . 네비게이션이 확인되기 전에 가드가 호출되어 새 입력 구성 요소가 아직 생성되지 않았기 때문입니다.

그러나 콜백을 `next`에 전달하여 인스턴스에 액세스할 수 있습니다. 네비게이션이 확인되면 콜백이 호출되고 컴포넌트 인스턴스가 매개변수로 콜백에 전달됩니다.

```jsx
beforeRouteEnter (to, from, next) {
  next(vm => {
    // access to component public instance via `vm`
  })
}
```

`beforeRouteLeave` **가드**는 일반적으로 사용자가 저장하지 않은 편집으로 경로를 실수로 떠나는 것을 방지하는 데 사용됩니다 . `false`를 반환하여 탐색을 취소할 수 있습니다.

```jsx
beforeRouteLeave (to, from) {
  const answer = window.confirm('정말 떠나시겠습니까? 저장되지 않은 변경 사항이 있습니다!')
  if (!answer) return false
}
```

### Composition API 사용

Composition API에서는 `onBeforeRouteUpdate`와 `onBeforeRouteLeave`를 사용할 수 있습니다.

- `beforeRouteUpdate` → `onBeforeRouteUpdate`
- `beforeRouteLeave` → `onBeforeRouteLeave`

```jsx
import { onBeforeRouteLeave, onBeforeRouteUpdate } from 'vue-router'
import { ref } from 'vue'

export default {
  setup() {
    // same as beforeRouteLeave option with no access to `this`
    onBeforeRouteLeave((to, from) => {
      const answer = window.confirm(
        'Do you really want to leave? you have unsaved changes!'
      )
      // cancel the navigation and stay on the same page
      if (!answer) return false
    })

    const userData = ref()

    // same as beforeRouteUpdate option with no access to `this`
    onBeforeRouteUpdate(async (to, from) => {
      // only fetch the user if the id changed as maybe only the query or the hash changed
      if (to.params.id !== from.params.id) {
        userData.value = await fetchUser(to.params.id)
      }
    })
  },
}
```

## 참고

- Vue Router v4
    
    [Programmatic Navigation | Vue Router](https://router.vuejs.org/guide/essentials/navigation.html)
    
- Vue Router v3 KR
    
    [중첩된 라우트 | Vue Router](https://v3.router.vuejs.org/kr/guide/essentials/nested-routes.html)

# Transition

Vue에서는 Transitions 이나 Animations을 쉽게할 수 있도록 도움을 주는 두 가지 빌드인(내장) 컴포넌트를 제공합니다.

- `<Transition>` : 컴포넌트가 DOM에 나타나고 사라질 때 애니메이션을 적용하기 위해 사용하는 컴포넌트 입니다.
- `<TransitionGroup>` : 컴포넌트가 `v-for` 목록에 삽입, 제거 또는 이동할 때 애니메이션을 적용하기 위해 사용하는 컴포넌트 입니다.

## `<Transition>` 컴포넌트

`<Transition>`은 기본으로 제공되는 컴포넌트 입니다. 즉, 등록하지 않고도 모든 컴포넌트 내 `<template>`안에서 사용할 수 있습니다. `default slot`을 통해 전달된 컴포넌트가 나타나거나(enter) 사라질 때(leave) 애니메이션을 적용하는 데 사용할 수 있습니다. 입장(enter) 또는 퇴장(leave)은 다음 중 하나에 의해 트리거될 수 있습니다.

- `v-if`를 통한 조건부 렌더링
- `v-show`를 통한 조건부 표시
- `<component>` 라는 특수 엘리먼트를 통한 동적 컴포넌트(Dynamic Component) 토글

다음은 가장 기본적인 사용법의 예입니다.

# TransitionGroup

`<TransitionGroup>`은 목록에서 렌더링되는 요소 또는 컴포넌트의 삽입, 제거 및 순서 변경을 애니메이션으로 만들기 위해 설계된 내장 컴포넌트입니다.

[TransitionGroup | Vue.js](https://vuejs.org/guide/built-ins/transition-group.html)

# Teleport

`<Teleport>`는 컴포넌트는 템플릿의 일부분을 외부에 존재하는 다른 DOM 노드로 **'텔레포트(이동)'**할 수 있게 해주는 내장 컴포넌트 입니다.

## `<Teleport>` 사용하기

이동을 원하는 DOM에 다음과 같이 id를 지정할 수 있습니다.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" href="/favicon.ico" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Vite App</title>
  </head>
  <body>
    <div id="app"></div>
    <div id="modal"></div>
    <script type="module" src="/src/main.js"></script>
  </body>
</html>
```

`<Teleport>` 컴포넌트를 활용하여 특정 요소 또는 컴포넌트를 다른 장소(DOM)로 이동할 수 있습니다.

```html
<Teleport to="#modal">
  <PostModal v-model="modal" :item="modalItem"></PostModal>
</Teleport>
```

이렇게 되면 아래와 같은 결과로 렌더링 됩니다.

```html
...
<div id="modal">
  <PostModal v-model="modal" :item="modalItem"></PostModal>
</div>
...
```

# Plugins

## 플러그인

플러그인(Plugin)은 일반적으로 Vue에 전역 수준의 기능을 추가할 때 사용하는 기능을 말합니다. 플러그인에 대해 엄격하게 정의 된 범위는 없습니다. 일반적으로 플러그인이 유용한 시나리오는 다음과 같습니다.

- `app.component()` 메서드를 사용하여 전역 컴포넌트를 등록 하고자 할 때
- `app.directive()` 메서드를 사용하여 커스텀 디렉티브를 등록 하고자 할 때
- `app.provide()`를 사용하여 앱 전체에 리소스(메서드 또는 데이터)를 주입할 때
- 전역 애플리케이션 인스턴스에 속성 또는 메서드를 추가하고자 할 때 `app.config.globalProperties`에 연결하여 추가할 수 있습니다.
- 위의 몇 가지 조합을 수행하는 라이브러리를 설치하고자 할 때 (예: vue-router)

## 플러그인 작성하기

플러그인은 **install() 메서드를 갖고 있는 객체**나 **단순히 설치 함수**로 만들 수 있습니다.

```jsx
// install() 메서드를 갖고 있는 객체
const objPlugin = {
	install(app, options) {
		
	}
}

// 단순히 설치 함수
function funcPlugin(app, options) {

}
```

그리고 작성한 플러그인을 전역 수준의 기능으로 추가할 때는 `app.use()` 메서드를 사용할 수 있습니다.

```jsx
import { createApp } from 'vue';
import router from '@/router';
import { funcPlugin } from './plugins/func';
import { objPlugin } from './plugins/obj';

const app = createApp(App);
app.use(router);
app.use(funcPlugin, { // options });
app.use(objPlugin, { // options });
app.mount('#app');
```

`app.use()` 메소드로 플러그인을 설치하면 플러그인의 매개변수로 `app instance`와 `options` 이 전달됩니다.

```jsx
install: (app, options) => {
	// app.provide, app.component 등 사용할 수 있는 전역 인스턴스
	// app.use(plugin, { options }) 호출 시 전달한 두 번째 파라미터
}
```

## Vue 3 Global component type checking issue

### components.d.ts 등록

- vite-plugin-components 옵션을 사용하여 한번에 체크 가능
    - `ViteComponents()` : 자동 import
    - `globalComponentsDeclaration: true` 옵션 componentd.d.ts 자동 등록

### ****Vue 3 Support - All In One****

- ****[Vue 3 Support - All In One](https://marketplace.visualstudio.com/items?itemName=Wscats.vue) 플러그인 사용**

## 참고

- **Vue3 Plugins 공식문서**
    
    [Plugins | Vue.js](https://vuejs.org/guide/reusability/plugins.html#writing-a-plugin)
    
- **VSCode Volar Plugin**
    - ****Vue Language Features (Volar)****
        
        [Vue Language Features (Volar) - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=Vue.volar)
        
    - ****Vue Volar extension Pack****
        
        [Vue Volar extension Pack - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=MisterJ.vue-volar-extention-pack)
        
- **vite-plugin-components**
    
    [📲 Vite 용 주문형 구성 요소 자동 가져 오기 - wenyanet](https://www.wenyanet.com/opensource/ko/60b92951a4f03f33442a9317.html)
    
    [unplugin-vue-components](https://www.npmjs.com/package/unplugin-vue-components)
    
- Vue3 global components not recognised
    
    [](https://youtrack.jetbrains.com/issue/WEB-48239/Vue-3-global-components-not-recognised)
    
- **global component type PR**
    
    https://github.com/vuejs/core/pull/3399

# Custom Directives

Vue 코어에서 기본으로 제공하는 디렉티브(`v-if` 또는 `v-for`와 같은) 외에도 Vue를 사용하면 직접 커스텀 지렉티브를 만들 수 있습니다.

Vue에서는 [Component](https://vuejs.org/guide/essentials/component-basics.html)와 [Composables](https://vuejs.org/guide/reusability/composables.html) 두 가지 형태의 코드 재사용을 도입했습니다. 컴포넌트는 주요 **빌딩블록을 재사용** 하는 반면 컴포저블은 **stateful logic을 재사용**하는 데 중점을 둡니다. 반면에 커스텀 디렉티브는 주로 일반 요소에 대한 **low-level(저수준) DOM 접근과 관련된 로직을 재사용**하기 위한 것입니다.

## `<script setup>` Directives

---

`<script setup>`에서 `v`접두사로 시작하는 모든 camelCase 변수를 커스텀 디렉티브로 사용할 수 있습니다. 아래 예에서 `vFocus`는 `<template>`에서 `v-focus`로 사용될 수 있습니다.

```jsx
<script setup>
// enables v-focus in templates
const vFocus = {
  mounted: (el) => el.focus()
}
</script>

<template>
  <input v-focus />
</template>
```

`v-focus` 디렉티브는 페이지 로드 시에만 작동하는 것이 아니라 Vue에서 동적으로 요소를 삽입할 때도 작동하기 때문에 `autofocus` 속성보다 더 유용합니다.

## `<script>` Directives

---

일반 `<script>`를 사용하는 경우 `directives` 옵션을 사용하여 커스텀 디렉티브를 등록할 수 있습니다.

```jsx
export default {
  setup() {
    /*...*/
  },
  directives: {
    // enables v-focus in template
    focus: {
      /* ... */
    }
  }
}
```

## Global Directives

---

앱 수준에서 커스텀 디렉티브를 전역적으로 등록하는 것도 일반적입니다.

```jsx
const app = createApp({})

// make v-focus usable in all components
app.directive('focus', {
  /* ... */
})
```

## Directives Hooks

---

디렉티브 정의 객체는 다음과 같은 여러 훅을 사용할 수 있습니다. (모든 훅은 필수가 아닌 선택사항)

```jsx
const myDirective = {
	// 바인딩된 요소의 속성 전에 호출됨
	// 또는 이벤트 리스너가 적용됨
	created(el, binding, vnode, prevVnode) {
	// 인수에 대한 자세한 내용은 아래를 참조하십시오.
	},
	// 요소가 DOM에 삽입되기 직전에 호출됩니다.
	beforeMount() {},
	// 바인딩된 요소의 부모 구성 요소가 있을 때 호출됩니다.
	// 모든 자식이 마운트됩니다.
	mounted() {},
	// 상위 컴포넌트가 업데이트되기 전에 호출됨
	beforeUpdate() {},
	// 상위 컴포넌트 다음에 호출되고
	// 모든 자식이 업데이트되었습니다.
	updated() {},
	// 상위 컴포넌트가 마운트 해제되기 전에 호출됨
	beforeUnmount() {},
	// 상위 컴포넌트가 마운트 해제될 때 호출됩니다.
	unmounted() {}
	}
}
```

### Directives Hooks의 매개변수

디렉티브 훅에는 다음과 같은 매개변수가 전달됩니다.

- `el`: 디렉티브가 바인딩된 요소입니다. DOM을 직접 조작하는 데 사용할 수 있습니다.
- `binding`: 다음 속성을 포함하는 개체입니다.
    - `value`: 지시문에 전달된 값입니다. 예를 들어 `v-my-directive="1 + 1"`에서 값은 `2`입니다.
    - `oldValue`: `beforeUpdate` 및 업데이트에서만 사용할 수 있는 이전 값입니다. 값이 변경되었는지 여부에 관계없이 사용 가능합니다.
    - `arg`: 지시문에 전달된 인수(있는 경우). 예를 들어 `v-my-directive:foo`에서 인수는 `foo`입니다.
    - `modifiers`: 수정자가 있는 경우 수정자를 포함하는 개체입니다. 예를 들어 `v-my-directive.foo.bar`에서 수정자 객체는 `{ foo: true, bar: true }`입니다.
    - `instance`: 지시문이 사용되는 구성 요소의 인스턴스입니다.
    - `dir`: 지시문 정의 개체.
- `vnode`: 바인딩된 요소를 나타내는 기본 VNode.
- `prevNode`: 이전 렌더링에서 바인딩된 요소를 나타내는 VNode. `beforeUpdate` 및 `updated` 후크에서만 사용할 수 있습니다.

예를 들어 다음 디렉티브가 있다고 가정해 보겠습니다.

```jsx
<div v-example:foo.bar="baz">
```

`binding` 매개변수는 다음과 같은 형태의 객체입니다.

```jsx
{
  arg: 'foo',
  modifiers: { bar: true },
  value: /* value of `baz` */,
  oldValue: /* value of `baz` from previous update */
}
```

## 함수로 단축 표현

---

다른 훅(Hook)이 필요 없이 커스텀 디렉티브가 `mounted`와 `updated` 대해 동일한 동작을 갖는 것이 일반적입니다. 이러한 경우 디렉티브를 함수로 정의할 수 있습니다.

```jsx
<div v-color="color"></div>
```

```jsx
app.directive('color', (el, binding) = {
	// 이것은 `mounted`와 `updated` 모두에 대해 호출됩니다.
	el.style.color = binding.value
})
```

## 객체 리터럴

---

디렉티브에 여러 값이 필요한 경우 JavaScript 객체를 전달할 수도 있습니다. 디렉티브는 모든 JavaScript 표현식을 사용할 수 있음을 기억하십시오.

```jsx
<div v-demo="{ color: 'white', text: 'hello!' }"></div>
```

```jsx
app.directive('demo', (el, binding) => {
  console.log(binding.value.color) // => "white"
  console.log(binding.value.text) // => "hello!"
})
```

## 컴포넌트에서 커스텀 디렉티브 사용

---

커스텀 디렉티브가 컴포넌트에서 사용되면 Non-Props 속성과 유사하게 항상 컴포넌트의 루트 노드에 적용됩니다.

```jsx
<MyComponent v-demo="test" />
```

```html
<!-- template of MyComponent -->

<div> <!-- v-demo 디렉티브가 여기에 적용됩니다 -->
  <span>My component content</span>
</div>
```

컴포넌트에는 잠재적으로 둘 이상의 루트 노드가 있을 수 있습니다. 다중 루트 컴포넌트에 커스텀 디렉티브를 적용하면 디렉티브가 무시되고 경고가 발생합니다. **속성과 달리 디렉티브은 `v-bind='$attrs'`를 사용하여 다른 요소에 전달할 수 없습니다.** **일반적으로 컴포넌트에 사용자 지정 지시문을 사용하는 것은 권장되지 않습니다.**

## Vue3 Custom Directives

---

[Custom Directives | Vue.js](https://vuejs.org/guide/reusability/custom-directives.html)

# Composables

## Composable 이란?

Vue 애플리케이션에서 **“Composable”**은 **Vue Composition API를 활용하여 상태 저장 비즈니스 로직을 캡슐화 하고 재사용하는 기능**을 말합니다.

프론트엔드 애플리케이션을 구축할 때 일반적인 로직을 재사용해야 하는 경우가 종종 있습니다. 예를 들어 여러 곳에서 날짜 형식을 지정해야 한다면 우리는 이러한 로직을 재사용 하기 위해서 함수(모듈)로 추출합니다. 이러한 함수는 **상태 비저장 로직을 캡슐화** 한 것입니다. 간단한 Input/Output만 있는 구조 입니다. 이러한 상태 비저장 로직를 재사용하기 위한 많은 라이브러리가 있으며, 예를 들어 **lodash**, **dayjs**와 같은 것들이 있습니다.

하지만 상태 저장 로직은 사용하면서 변경되는 상태 관리가 포함됩니다. 간단한 예는 페이지에서 마우스의 현재 위치를 추적하는 것입니다.

## 마우스 추적 기능 예시

컴포넌트 안에서 직접 Composition API를 사용하여 마우스 추적 기능을 구현하면 다음과 같이 됩니다.

```jsx
<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

const x = ref(0);
const y = ref(0);

function update(event) {
  x.value = event.pageX;
  y.value = event.pageY;
}

onMounted(() => window.addEventListener('mousemove', update));
onUnmounted(() => window.removeEventListener('mousemove', update));
</script>

<template>마우스 위치: {{ x }}, {{ y }}</template>
```

그러나 여러 컴포넌트에서 동일한 로직을 재사용하려면 어떻게 해야 할까요? Composable 함수로 로직을 외부파일로 추출할 수 있습니다.

```jsx
// mouse.js
import { ref, onMounted, onUnmounted } from 'vue';

// Composable 함수명은 'use'로 시작하는게 규칙입니다.
export function useMouse() {
  // Composable에 의해 캡슐화되고 관리되는 상태입니다.
  const x = ref(0);
  const y = ref(0);

  // 상태를 업데이트합니다.
  function update(event) {
    x.value = event.pageX;
    y.value = event.pageY;
  }

  // Composable은 사용중인 컴포넌트 hook 또한 사용할 수 있습니다.
  onMounted(() => window.addEventListener('mousemove', update));
  onUnmounted(() => window.removeEventListener('mousemove', update));

  // 관리 상태를 반환합니다.
  // 상태값는 ref이며 만약 외부에서 해당값을 변경하면 내부의 값도 동기화되어 변경됩니다.
  return { x, y };
}
```

그리고 이러한 Composable 함수는 컴포넌트에서 아래와 같이 사용될 수 있습니다.

```jsx
<script setup>
import { useMouse } from './composables/mouse.js';

const { x, y } = useMouse();
</script>

<template>마우스 위치: {{ x }}, {{ y }}</template>
```

위 예시에서 볼 수 있듯이 핵심 로직은 그대로 유지됩니다. 우리가 해야 할 일은 **핵심 로직을 외부 함수로 추출**하고 컴포넌트에 **노출되어야 하는 상태를 반환**하는 것입니다.

Composable 함수에서는 컴포넌트에서 내부에서 구현 했던것과 마찬가지로 Composable 함수 전체 범위에서 Composition API 기능을 사용할 수 있습니다. 이제 모든 컴포넌트에서 `useMouse()` 기능을 사용할 수 있습니다.

그리고 Composable의 장점은 이러한 **Composable 함수를 중첩**해서 사용할 수 있다는 것입니다. 하나의 Composable 함수는 하나 이상의 다른 Composable 함수를 호출할 수 있습니다. 이를 통해 우리는 작은 로직의 단위를 사용하여 복잡한 로직을 구성할 수 있습니다. 이것은 마치 컴포넌트를 사용하여 전체 애플리케이션을 구성하는 것과 유사합니다. 이렇게 **재사용 로직 단위로 가능하기 때문에 이름이 Composition API** 입니다.

```jsx
// event.js
import { onMounted, onUnmounted } from 'vue';

// 특정 DOM에 이벤트를 등록하는 기능도 Composable 함수로 만들 수 있습니다.
export function useEventListener(target, event, callback) {
  onMounted(() => target.addEventListener(event, callback));
  onUnmounted(() => target.removeEventListener(event, callback));
}
```

`useMouse()`를 사용하여 로직을 단순화 할 수 있습니다.

```jsx
import { ref } from 'vue';
import { useEventListener } from './event';

export function useMouse() {
  const x = ref(0);
  const y = ref(0);

  useEventListener(window, 'mousemove', (event) => {
    x.value = event.pageX;
    y.value = event.pageY;
  });

  return { x, y };
}
```

<aside>
💡 각 컴포넌트 인스턴스에서 `useMouse()` 호출하면 컴포넌트는 서로 간섭하지 않도록 `x`, `y` 상태를 복사하여 생성됩니다. 만약에 컴포넌트간의 상태를 공유하려면 상태관리 API(Vuex, Pinia)를 사용할 수 있습니다.

</aside>

## 비동기 상태 예

`useMouse()` Composable 함수는 파라미터를 사용하지 않았음으로 파라미터를 사용하는 다른 예를 살펴보겠습니다. 비동기 데이터를 가져올 때 성공, 실패 등 다양한 상태를 처리해야 하는 경우가 많습니다.

```jsx
<script setup>
import axios from 'axios';
import { onMounted, ref } from 'vue';

const data = ref(null);
const error = ref(null);

onMounted(() => {
  axios
    .get(`https://reqres.in/api/users?page=1`)
    .then((response) => (data.value = response.data.data))
    .catch((err) => (error.value = err));
});
</script>

<template>
  <div v-if="error">에러 발생!: {{ error.messsage }}</div>
  <div v-else-if="data">
    <ul>
      <li v-for="item in data" :key="item.id">
        {{ item.email }}
      </li>
    </ul>
  </div>
  <div v-else>Loading...</div>
</template>
```

위에서 언급했던 것처럼 데이터를 가져와야 하는 이러한 로직을 반복해서 사용하는 것은 매우 불편할 것입니다. Composable 함수로 추출해 보겠습니다.

```jsx
// fetch.js
import axios from 'axios';
import { ref } from 'vue';

export const useFetch = (url) => {
  const data = ref(null);
  const error = ref(null);

  axios
    .get(url)
    .then((response) => (data.value = response.data.data))
    .catch((err) => (error.value = err));

  return {
    data,
    error,
  };
};
```

이제 컴포넌트에서 가져올 수 있습니다.

```jsx
<script setup>
import { useFetch } from './composables/fetch';

const { data, error } = useFetch('https://reqres.in/api/users?page=1');
</script>

<template>
  <div v-if="error">에러 발생!: {{ error.messsage }}</div>
  <div v-else-if="data">
    <ul>
      <li v-for="item in data" :key="item.id">
        {{ item.email }}
      </li>
    </ul>
  </div>
  <div v-else>Loading...</div>
</template>
```

`useFetch()` Composable 함수는 URL 문자열(string)으로 고정된 데이터를 조회하고 완료됩니다. 다음과 같은 기능을 추가해 보도록 하겠습니다.

- URL이 변경될 때마다 이를 감지(Watch)하여 데이터를 다시 조회함

```jsx
import axios from 'axios';
import { isRef, ref, unref, watchEffect } from 'vue';

export const useFetch = (url) => {
  const data = ref(null);
  const error = ref(null);

  function doFetch() {
    data.value = null;
    error.value = null;
    axios
      .get(unref(url))
      .then((response) => (data.value = response.data.data))
      .catch((err) => (error.value = err));
  }
  if (isRef(url)) {
    watchEffect(doFetch);
  } else {
    doFetch();
  }

  return {
    data,
    error,
  };
};
```

컴포넌트는 다음과 같이 수정하였습니다.

```jsx
<script setup>
import { computed } from '@vue/reactivity';
import { ref } from 'vue';
import { useFetch } from './composables/fetch';
const page = ref(1);
const url = computed(() => 'https://reqres.in/api/users?page=' + page.value);
const { data, error } = useFetch(url);
</script>

<template>
  <div v-if="error">에러 발생!: {{ error.messsage }}</div>
  <div v-else-if="data">
    <ul>
      <li v-for="item in data" :key="item.id">
        {{ item.email }}
      </li>
    </ul>
    <button @click="page = 1">1</button>
    <button @click="page = 2">2</button>
  </div>
  <div v-else>Loading...</div>
</template>
```

## Conventions & Best Practices

### Naming Rule

Composable 함수는 “use”로 시작하는 cacelCase 이름으로 이름을 지정하는 것이 관례입니다.

### Input Arguments

Composable 함수는 반응성에 의존하지 않더라도 ref 파라미터를 입력값으로 받을 수 있습니다. 그렇기 때문에 다른 개발자와 함께 사용하는 Composable 함수를 개발하는 경우 입력 파라미터가 ref인 경우를 처리하는 것이 좋습니다. Utilities Function인 `unref()`를 사용하면 유용합니다.

```jsx
import { unref } from 'vue'

function useFeature(maybeRef) {
	// 만약 mayRef가 실제로 ref라면, 그것의 .value가 반환될 것입니다.
	// 그렇지 않으면, mayRef는 있는 그대로 반환됩니다.
  const value = unref(maybeRef)
}
```

만약 입력이 ref 일 때 반응성 효과가 있는 Composable 함수를 생성하는 경우 `watch()`로 ref를 명시적으로 감시하는지 확인해야 합니다. 또는 `watchEffect()` 내부에서 `unref()`를 호출하여 제대로 추적되고 있는지 확인해야 합니다.

### Return Values

예시에서 보면 Composable 함수에서 `reactive()` 대신 `ref()`를 독점적으로 사용하고 있다는 것을 눈치채셨을 것입니다. Vue에서 권장되는 컨벤션(규칙)은 컴포넌트에서 구조분해 할당으로 재할당 받을 수 있도록 Composable 함수에서 ref 객체를 반환하는 것입니다.

```jsx
// x와 y는 refs 객체입니다.
const { x, y } = useMouse()
```

Composable에서 `reactive` 객체를 반환하면 구조 분해 할당시 내부 상태에 대한 반응성 연결이 끊어지고 `refs`로 반환하면 해당 연결이 유지됩니다.

Composable에서 반환된 상태를 객체 속성으로 사용하려는 경우 반환된 객체를 reactive 랩핑 합니다.

```jsx
const mouse = reactive(useMouse())
// mouse.x는 원본 참조에 연결되어 있습니다.
console.log(mouse.x)
```

### Other Working

Composable 함수에서 다른 작업(DOM 이벤트 리스너 추가 또는 데이터 가져오기)을 수행하는 것은 괜찮지만 다음 규칙에 주의하십시오.

- [**SSR(Server-Side Rendering)**](https://vuejs.org/guide/scaling-up/ssr.html)을 사용하는 애플리케이션에서 작업하는 경우 라이프사이클 훅이 마운트 이후인 곳에서 DOM관련 작업을 수행해야 합니다. (예: `onMounted()`. 이러한 훅은 브라우저에서만 호출되므로 내부 코드가 DOM에 액세스할 수 있는지 확인할 수 있습니다.)
- `onUnmounted()`에서 이벤트관련 리스터를 제거해야 합니다. (예: `useEventListener()`)

### 사용 제한

Composable 함수는 `<script setup>` 또는 `setup()` 훅 내에서 **동기적**으로 호출해야 합니다. 또는 경우에 따라 `onMounted()`와 같은 라이프사이클 훅에서 호출할 수도 있습니다.

# toRef, toRefs

## toRef

반응형 객체의 속성을 하나의 ref 객체로 만들 때 사용된다. 생성된 ref 객체는 원본 반응형 객체의 속성과 동기화 됩니다. 원본 속성을 변경하면 ref 객체가 업데이트되고 그 반대의 경우도 마찬가지 입니다.

```jsx
const state = reactive({
  foo: 1,
  bar: 2
})

const fooRef = toRef(state, 'foo')

// 참조를 변경하면 원본이 업데이트됩니다.
fooRef.value++
console.log(state.foo) // 2

// 원본을 변경하면 ref도 업데이트됩니다.
state.foo++
console.log(fooRef.value) // 3
```

`ref`와 `toRef`는 다릅니다.

```jsx
const fooRef = ref(state.foo)
```

위의 ref 객체(fooRef)는 프리미티브 값을 초기화 값으로 받기 때문에 `state.foo`와 동기화 되지 않습니다.

### ****toRef 활용****

`toRef()`는 Composable 함수에 Props 참조를 전달하려는 경우에 유용합니다.

```jsx
import { toRef } from 'vue'

const props = defineProps(/* ... */)

// `props.foo`를 ref로 변환한 다음
useSomeFeature(toRef(props, 'foo'))
```

`toRef()`가 `props`와 함께 사용 되면 `props`변경에 대한 제한사항이 계족 적용됩니다. ref에 새 값을 할당하려는 시도는 prop을 직접 수정하려는 것과 동일하게 판단되며 허용되지 않습니다.

새 값을 할당하려는 상황이라면 toRef() 대신 `computed(get, set)`를 활용할 수 있습니다.

그리고 toRef는 반응형 객체의 속성이 존재하지 않아도 사용 가능한 ref 객체를 반환합니다.

## toRefs

반응형 객체를 **구조분해 할당 후 반응형을 그대로 유지**하고 싶을 때 사용합니다.

반응형(reactive) 객체를 구조 분해하여 재할당 할 경우 반응형으로 동작하지 않습니다. 이렇게 반응형으로 동작하지 않는것은 매우 당연한 일입니다. (call by value)

```jsx
let position = reactive({
  x: 0,
  y: 0,
});
let { x, y } = position;
x++;
y++;
console.log(x, y);                   // 1 1
console.log(position.x, position.y); // 0 0
```

이때 반응성을 유지하기 위해 reactive 객체의 각각의 속성을 `ref`로 변환해 주는 것이 `toRefs`입니다. `toRefs`를 사용하면 `reactive` 객체 각각의 속성이 `ref` 값으로 변환 됩니다. 그렇기 때문에 구조 분해 할당으로 재할당을 하게 되면 재할당 받은 `ref` 참조 값(예: `x`, `y`)과 `reactive`객체의 속성은 동기화가 됩니다.

```jsx
let position = reactive({
  x: 0,
  y: 0,
});
let { x, y } = toRefs(position);
x.value++;
y.value++;
console.log(x.value, y.value);       // 1 1
console.log(position.x, position.y); // 1 1
```

### toRefs 활용

`toRefs()`는 일반 함수나 Composable 함수에서 Reactive객체를 반환 받는 경우에 유용합니다.

```jsx
function useFeatureX() {
  const state = reactive({
    foo: 1,
    bar: 2
  })

  // ...logic operating on state

  // convert to refs when returning
  return toRefs(state)
}

// can destructure without losing reactivity
const { foo, bar } = useFeatureX()
```

Composable 함수에서 반환값을 `ref`로 반환해야 하는 컨벤션(규칙)이 있습니다. 하지만 Composable 함수 내부에서 reactive 객체를 사용하고 싶을때가 있는데요.

이때 `toRefs()`함수를 사용하여 내부에서 사용한 `reactive`객체를 반환시에 `ref`로 변환할 수 있습니다.

# isRef, unref, isProxy, isReactive, isReadonly

## isRef()

값이 ref 객체인지 확인합니다.

```jsx
if (isRef(foo)) {
	foo.value
}
```

## unref()

매개변수가 ref이면 내부 값(`.value`)을 반환하고 아니면 매개변수 자체를 반환합니다. 이것은 다음 표현식에 대한 syntactic sugar 입니다. `val = isRef(val) ? val.value : val`

```jsx
function useFoo(x) {
	const unwrapped = unref(x)
}
```

## isReactive()

객체가 `reactive()` 또는 `shallowReactive()`에 의해 생성된 프록시인지 확인합니다.

```jsx
const person = reactive({...})
isReactive(person)
```

## isReadonly()

객체가 `readonly()` 또는 `shallowReadonly()`에 의해 생성된 프록시인지 확인합니다.

```jsx
const option = readonly({...});
isReadonly(option)
```

## isProxy()

객체가 `reactive()`, `shallowReactive()`, `readonly()`, `shallowReadonly()`에 의해 생성된 프록시인지 확인합니다.

```jsx
isProxy(person)
isProxy(option)
```

# 상태관리란?

## 상태 관리 패턴이란?

모든 Vue 컴포넌트 인스턴스는 자체적으로 상태를 관리합니다. 간단한 카운터 컴포넌트를 예로 들어 보겠습니다.

```jsx
<script setup>
import { ref } from 'vue'

// state
const count = ref(0)

// actions
function increment() {
  count.value++
}
</script>

<!-- view -->
<template>{{ count }}</template>
```

이 컴포넌트는 다음과 같은 부분으로 구성된 하나의 독립된 단위 입니다.

- **state** - 컴포넌트내에 선언된 상태
- **view** - 상태가 선언적으로 매핑된 템플릿
- **actions** - **view**에서 사용자의 입력에 대한 반응으로 **state**를 변경할 수 있음

컴포넌트의 단방향 데이터 흐름을 간단히 표현해보면 이렇습니다.

<img width="290" alt="stateflow" src="https://user-images.githubusercontent.com/86648892/226276085-a7edad45-f4f4-48d3-bcbb-27a3e49594dd.png">

하지만 컴포넌트간에 공통된 상태를 공유하려면 어떻게 해야 할까요?

1. 공유하고자 하는 상태를 같은 부모 컴포넌트로 두고 **Props**로 전달하는 것입니다.
→ 그러나 이것은 깊은 계층구조를 가진 컴포넌트에서 [Prop Drilling 이라는 문제](https://vuejs.org/guide/components/provide-inject.html#prop-drilling)로 이어질 수 있습니다.
2. Template Refs를 사용해서 부모/자식 인스턴스에 직접 접근하거나 Emits 이벤트를 통해 여러 복사본의 상태를 동기화 하는 것입니다.
→ 이러한 패턴은 유지 관리할 수 없는 코드로 이어집니다. 

더 간단한 해결책은 컴포넌트에서 공유 상태를 추출하여 글로벌 싱글톤으로 관리하는 것입니다. 이러한 글로벌 공통 상태에 대해 모든 컴포넌트는 **“View”** 역할을 하며 컴포넌트 위치에 관계없이 상태에 접근하거나 변경할 수 있습니다.

## Reactivity API를 통한 상태 관리

여러 컴포넌트에서 공유해야 하는 상태가 있는 경우 `reactive()`를 사용하여 반응형 객체를 만든 다음 여러 컴포넌트에서 가져올 수 있습니다.

```jsx
// store.js
import { reactive } from 'vue'

export const store = reactive({
  count: 0
})
```

```jsx
<!-- ComponentA.vue -->
<script setup>
import { store } from './store.js'
</script>

<template>
	<div>From A: {{ store.count }}</div>
</template>
```

```jsx
<!-- ComponentB.vue -->
<script setup>
import { store } from './store.js'
</script>

<template>
	<div>From B: {{ store.count }}</div>
</template>
```

이제 `store` 객체가 변경 될 때마다 `<ComponentA>`와 `<ComponentB>`의 View가 자동으로 업데이트됩니다. 하지만 이러한 코드는 `store`를 가져오는 모든 컴포넌트가 **원하는 대로** 변경할 수 있음을 의미합니다.

```jsx
<template>
  <button @click="store.count++">
    Component B: {{ store.count }}
  </button>
</template>
```

이러한 방법은 로직이 간단하다면 문제없지만 **컴포넌트에 의해 임의로 변경될 수 있는 전역 상태 관리**는 장기적으로 유지하기가 쉽지 않습니다. 상태를 변경하는 로직이 상태 자체 처럼 중앙 집중화 되도록 하려면 작업의 의도를 나태내는 이름으로 `store`객체에 메서드를 정의하는 것이 좋습니다.

```jsx
// store.js
import { reactive } from 'vue'

export const store = reactive({
  count: 0,
  increment() {
    this.count++
  }
})
```

```jsx
<button @click="store.increment()">
	Component B: {{ store.count }}
</button>
```

<aside>
💡 `@click` 핸들러는 괄호와 함께 메서드를 호출합니다. 왜냐하면 inceament 메서드는 컴포넌트 메서드가 아니기 때문에 적절한 `this`컨텍스트로 메소드를 호출하는 데 필요합니다.

</aside>

위 예제에서는 단일 `reactive()` 객체를 저장소로 사용하고 있지만 `ref()` 또는 `computed()`와 같은 다른 [Reactivity APIs](https://vuejs.org/api/reactivity-core.html)를 사용하여 생선된 반응형 `state`를 공유하거나 Composable 함수에서 전역 상태를 반환 할 수도 있습니다.

```jsx
import { ref } from 'vue'

// 모듈 범위에서 생성된 전역 상태
const globalCount = ref(1)

export function useCount() {
  // 컴포넌트 별로 생성된 로컬 상태
  const localCount = ref(1)

  return {
    globalCount,
    localCount
  }
}
```

이처럼 반응형 상태 관리 시스템이 컴포넌트 모델과 분리되어 있기 때문에 Vue를 매우 유연하게 사용할 수 있습니다.

## Pinia

간단한 애플리케이션에서는 위 예시처럼 우리가 수동으로 만든 상태 관리 시스템으로 충분 하지만 대규모 애플리케이션에서는 고려해야 할 사항이 더 많습니다.

- 팀과 협업을 위한 강력한 규칙
- TImeline, in-component, inspection, time-travel debugging을 포함하는 Vue Devtools와 통합
- HMR(Hot Module Replacement)
- 서버사이드 렌더링 지원

Pinia는 위의 모든 것을 구현하는 상태 관리 라이브러리입니다. Vue 핵심 팀에서 유지 관리하며 Vue2, Vue3에서 모두 동작합니다.

기존 사용자들은 Vue의 공식 상태 관리 라이브러리였던 Vuex에 익숙할 수 있습니다. 하지만 이제 Vuex는 이제 유지 관리 모드에 있으며, 동작은 하지만 더 이상 새로운 기능을 개발하지 않습니다. 대신 Pinia가 생태계에서 동일한 역할을 수행하며 새로운 애플리케이션 개발시에는 Pinia를 사용하는 것이 좋습니다.

Pinia는 Vuex5에 대한 핵심 팀의 토론에서 많은 아이디어를 얻어 Vuex의 다음은 어떤 모습일지 연구하는 것으로 시작했습니다. 결국 Pinia는 Vuex5에서 우리가 원하는 대부분을 이미 구현하고 있었고 Pinia를 만들기로 결정했습니다.

Vuex와 비교하여 Pinia는 더 간단한 API를 제공하고 Composition API 스타일의 API를 제공하며 가장 중요한 것은 TypeScript와 함께 사용할 때 견고한 타입 추론을 지원합니다.

# Pinia란?

## 왜 Pinia를 사용해야 하나요?

Pinia는 Vue의 저장소 라이브러리로 컴포너트/페이지 간에 상태를 공유할 수 있습니다. Composition API에 익숙하다면 이미 `export const state = reactive({})` API를 활용하여 Global State를 간단히 만들 수 있을 것입니다. 하지만 이러한 방법은 Single Page Application에 해당하는 방법이며 서버 사이드 렌더링이 되는 경우 애플리케이션이 보안 취약성에 노출시킵니다. 또한 작은 Single Page Application에서도 Pinia를 사용하면 많은 것을 얻을 수 있습니다.

- Devtools 지원
    - mutations, actions를 추적하는 타임라인
    - Store는 사용되는 컴포넌트에 나타납니다.
    - Time travel과 더 쉬운 디버깅
- Hot module replacement
    - 페이지 리로딩 없지 store 수정
    - 개발하는 동안 기존 state 유지
- 플러그인: 플러그인으로 Pinia 기능 확장
- JS 사용자를 위한 적절한 TypeScript 지원 또는 **자동 완성**
- 서버 사이드 렌더링 지원

## Vuex와 비교?

- mutations는 더이상 존재하지 않습니다. 왜냐하면 mutatinos는 필요 이상으로 **장황하게 인식**되었기 때문입니다.
- TypeScript를 지원하기 위해 복잡한 사용자 지정 래퍼를 만들 필요가 없으며 모든 것이 입력되며 API는 TS 타입 추론을 최대한 활용하는 방식으로 설계되었습니다.
- 강력한 autocompletion
- 

## 설치

원하는 패키지 관리자로 설치합니다.

```bash
yarn add pinia
# or with npm
npm install pinia
```

> **Tip**
앱이 Vue 2를 사용하는 경우 구성 `@vue/composition-api`도 설치해야 합니다 . Nuxt를 사용하는 경우 [다음 지침](https://pinia.vuejs.org/ssr/nuxt.html) 을 따라야 합니다 .
> 

만약 Vue CLI를 사용하는 경우 이 **[비공식 플러그인](https://github.com/wobsoriano/vue-cli-plugin-pinia)** 을 대신 사용해 볼 수 있습니다.

pinia를 생성한 후 앱에 전달합니다.

```jsx
import { createPinia } from 'pinia'

app.use(createPinia())
```

## Store란?

Store는 컴포넌트에 포함되지 않은 state 및 비즈니스 로직을 보유하고 있는 엔터티입니다. 즉 전역 상태를 호스팅 합니다. 언제 어디서든 사용 가능한 전역 컴포넌트와 비슷합니다. `state`, `getter`, `action`의 세 가지 개념이 있으며 이러한 개념이 `data`, `computed`, `methods`와 동일하다고 생각할 수 있습니다.

## 언제 Store를 이용해야 하나요?

Store에는 애플리케이션 전체에서 접근할 수 있는 데이터가 포함되어야 합니다. 예를 들어 네비게이션에 표시되는 사용자 정보와 같이 여러 곳에서 사용되는 데이터가 포함됩니다.

반면에 컴포넌트에서 관리될 수 있는 로컬 데이터를 Store에 포함하는 것은 피해야 합니다.

# Store 정의

Store는 `defineStore()`를 사용하여 정의합니다. 그리고 매개변수로 **유니크한 이름**을 전달해야 합니다.

```jsx
import { defineStore } from 'pinia'

// useStore는 useUser, useCart와 같을 수 있습니다.
// 첫 번째 인수는 애플리케이션 전체에서 스토어의 고유 ID입니다.
export const useStore = defineStore('main', {
  // 다른 옵션...
})
```

id라고도 하는 이 이름은 꼭 필요하며 Pinia에서 Store를 devtools에 연결하는 데 사용합니다. 그리고 반환된 함수의 이름은 `use...`로 지정하는 것은 사용법을 관용적으로 만들기 위한 composables 전반에 걸친 규칙입니다.

### Store 사용하기

`setup()` 함수 내부에서 `useStore()`가 호출될 때까지 Store가 생성되지 않기 때문에 Store를 정의하고 있습니다.

```jsx
import { useStore } from '@/stores/counter'

export default {
  setup() {
    const store = useStore()

    return {
      // 템플릿에서 사용하기 위해 전체 스토어 인스턴스를 반환할 수 있습니다.
      store,
    }
  },
}
```

원하는 만큼 Store를 정의할 수 있으며 pinia를 최대한 활용하려면 **각 Store를 다른 파일에 정의해야 합니다.**

Store가 인스턴스화되면 `store`에서 직접 `state`, `getters`, `actions`에 정의된 모든 속성에 액세스할 수 있습니다.

`store`는 `reactive`로 래핑된 객체입니다. 그렇기 때문에 `.value`로 값을 가져오지 않아도 됩니다. 그러나  구조를 분해해서 재할당할 수 없습니다.

```jsx
export default defineComponent({
  setup() {
    const store = useStore()
		// ❌ 이것은 반응성을 깨뜨리기 때문에 작동하지 않습니다.
    const { name, doubleCount } = store

    name // "eduardo"
    doubleCount // 2

    return {
      // 항상 'eduardo'가 될 것입니다.
      name,
      // 항상 2가 될 것입니다
      doubleCount,
      // 이것은 반응적일 것이다
      doubleValue: computed(() => store.doubleCount),
      }
  },
})
```

반응성을 유지하면서 Store에서 속성을 추출하려면 `storeToRefs()`를 사용해야 합니다. 그러면 모든 반응 속성에 대한 참조를 생성합니다. 이것은 `store`의 `state`만 사용하고 `actions`를 호출하지 않을 때 유용합니다. Store 자체에도 바인딩되므로 `store`에서 직접 `actions`를 구조분해 할당할 수 있습니다.

```jsx
import { storeToRefs } from 'pinia'

export default defineComponent({
  setup() {
    const store = useStore()
    // `name`과 `doubleCount`는 반응형 참조입니다.
		// 플러그인에 의해 추가된 속성에 대한 참조도 생성됩니다.
		// 그러나 모든 작업 또는 비반응성(비 참조/반응성) 속성을 건너뜁니다.
    const { name, doubleCount } = storeToRefs(store)
		// increment action은 그냥 추출될 수 있습니다.
    const { increment } = store

    return {
      name,
      doubleCount
      increment,
    }
  },
})
```

# State

`state`는 대부분의 경우 상점의 중심 부분입니다. 그리고 개발자들은 대부분 앱을 나타내는 `state`를 정의하는 것으로 시작합니다. Pinis에서 `state`는 초기 값을 리턴하는 함수로 정의됩니다. 그리고 이러한 `state`는 서버, 클라이언트 모두에서 작동할 수 있습니다.

```jsx
import { defineStore } from 'pinia'

const useStore = defineStore('storeId', {
  // 전체 타입 추론에 권장되는 화살표 함수
  state: () => {
    return {
			// 이 모든 속성은 자동으로 유형이 유추됩니다.
      counter: 0,
      name: 'Eduardo',
      isAdmin: true,
    }
  },
})
```

### `state` 접근하기

기본적으로 `store` 인스턴스를 통해 `state`에 접근하여 직접 읽고 쓸 수 있습니다.

```jsx
const store = useStore()

store.counter++
```

### `state` 초기화

`store`에서 `$reset()` 메서드를 호출하여 상태를 초기 값으로 재설정 할 수 있습니다.

```jsx
const store = useStore()

store.$reset()
```

### `state` 변경하기

`store.counter++`로 `store`를 직접 변경하는 것 외에도 `$patch` 메소드를 호출할 수도 있습니다. `state` 객체의 부분을 매개변수로 전달하여 여러개의 값을 변경할 수 있습니다.

```jsx
store.$patch({
  counter: store.counter + 1,
  name: 'Abalam',
})
```

하지만 객체의 일부 변경으로 배열의 변경을 수행(푸시, 제거, 연결)하려면 적용이 힘들거나 비용이 발생할 수 있습니다. 이때 `$patch` 메서드에 콜백 함수를 전달하여 해결할 수 있습니다.

```jsx
cartStore.$patch((state) => {
  state.items.push({ name: 'shoes', quantity: 1 })
  state.hasChanged = true
})
```

여기서 주요 차이점은 `$patch()`를 사용하면 여러 변경 사항을 devtools의 단일 항목으로 그룹화할 수 있다는 것입니다. `state`와 `$patch()`에 대한 직접적인 변경은 devtools에 나타나며 시간 여행이 가능합니다.(아직 Vue 3에는 없음).

### `state` 교체

`$state`속성을 새 객체로 설정하여 저장소의 전체 상태를 바꿀 수 있습니다 .

```jsx
store.$state = { counter: 666, name: 'Paimon' }
```

pinia 인스턴스의 상태를 변경하여 애플리케이션의 전체 상태를 바꿀 수도 있습니다.

```jsx
pinia.state.value = {}
```

## `state` 구독

Vuex의 `subscribe` 메소드와 유사하게 스토어의 `$subscribe()` 메소드를 통해 상태와 변경 사항을 볼 수 있습니다. 일반 `watch()`보다 `$subscribe()`를 사용하는 이점은 구독이 패치 후에 한 번만 트리거된다는 것입니다(예: 위의 함수 버전을 사용할 때).

```jsx
cartStore.$subscribe((mutation, state) => {
  // 'pinia'에서 { MutationType } 가져오기
  mutation.type // 'direct' | 'patch object' | 'patch function'
  //cartStore.$id와 동일
  mutation.storeId // 'cart'
  // mutation.type === 'patch object'에서만 사용 가능
  mutation.payload // cartStore.$patch()에 전달된 패치 객체

  // 변경될 때마다 전체 상태를 로컬 스토리지에 유지
  localStorage.setItem('cart', JSON.stringify(state))
})
```

기본적으로 `상태구독`은 추가된 컴포넌트에 바인딩됩니다(저장소가 컴포넌트의 `setup()` 내부에 있는 경우). 즉, 컴포넌트가 마운트 해제되면 자동으로 제거됩니다. 컴포넌트가 마운트 해제된 후에도 이를 유지하려면 `{ detached: true }`를 두 번째 인수로 전달하여 현재 컴포넌트에서 상태 구독을 분리합니다.

```jsx
export default {
  setup() {
    const someStore = useSomeStore()

    // this subscription will be kept after the component is unmounted
    someStore.$subscribe(callback, { detached: true })

    // ...
  },
}
```

> **Tip**
`pinia`인스턴스 의 전체 상태를 볼 수 있습니다 .
> 

```jsx
watch(
  pinia.state,
  (state) => {
    // persist the whole state to the local storage whenever it changes
    localStorage.setItem('piniaState', JSON.stringify(state))
  },
  { deep: true }
)
```

## 참고

- Vuex와 다르게 state를 직접 변경할 수 있다.
- Vuex와 다르게 Mutations에 대한 개념이 없어졌다.
    - 결구 개념이 더 단순해지고 구조가 간결해짐.

# State

`state`는 대부분의 경우 상점의 중심 부분입니다. 그리고 개발자들은 대부분 앱을 나타내는 `state`를 정의하는 것으로 시작합니다. Pinis에서 `state`는 초기 값을 리턴하는 함수로 정의됩니다. 그리고 이러한 `state`는 서버, 클라이언트 모두에서 작동할 수 있습니다.

```jsx
import { defineStore } from 'pinia'

const useStore = defineStore('storeId', {
  // 전체 타입 추론에 권장되는 화살표 함수
  state: () => {
    return {
			// 이 모든 속성은 자동으로 유형이 유추됩니다.
      counter: 0,
      name: 'Eduardo',
      isAdmin: true,
    }
  },
})
```

## `state` 접근하기

기본적으로 `store` 인스턴스를 통해 `state`에 접근하여 직접 읽고 쓸 수 있습니다.

```jsx
const store = useStore()

store.counter++
```

## Options API와 사용

### setup() 함수와 함께

```jsx
import { useCounterStore } from '../stores/counterStore'

export default {
  setup() {
    const counterStore = useCounterStore()

    return { counterStore }
  },
  computed: {
    tripleCounter() {
      return this.counterStore.counter * 3
    },
  },
}
```

### setup() 함수 없이

컴포지션 API를 사용하지 않고 `computed`만 사용하는 경우, `mapState()` helper 함수를 사용하여 `state` 속성을 읽기 전용 `computed` 속성으로 매핑할 수 있습니다.

```jsx
import { mapState } from 'pinia'
import { useCounterStore } from '../stores/counterStore'

export default {
  computed: {
    // 구성 요소 내부의 this.counter에 대한 액세스 권한을 부여합니다.
		// store.counter에서 읽는 것과 동일
    ...mapState(useCounterStore, ['counter'])
    // 위와 같지만 this.myOwnName으로 등록
    ...mapState(useCounterStore, {
      myOwnName: 'counter',
      // 스토어에 액세스하는 함수를 작성할 수도 있습니다.
      double: store => store.counter * 2,
      // `this`에 액세스할 수 있지만 올바르게 입력되지 않습니다...
      magicValue(store) {
        return store.someGetter + this.counter + this.double
      },
    }),
  },
}
```

## `state` 초기화

`store`에서 `$reset()` 메서드를 호출하여 상태를 초기 값으로 재설정 할 수 있습니다.

```jsx
const store = useStore()

store.$reset()
```

## `state` 변경하기

`store.counter++`로 `store`를 직접 변경하는 것 외에도 `$patch` 메소드를 호출할 수도 있습니다. `state` 객체의 부분을 매개변수로 전달하여 여러개의 값을 변경할 수 있습니다.

```jsx
store.$patch({
  counter: store.counter + 1,
  name: 'Abalam',
})
```

하지만 객체의 일부 변경으로 배열의 변경을 수행(푸시, 제거, 연결)하려면 적용이 힘들거나 비용이 발생할 수 있습니다. 이때 `$patch` 메서드에 콜백 함수를 전달하여 해결할 수 있습니다.

```jsx
cartStore.$patch((state) => {
  state.items.push({ name: 'shoes', quantity: 1 })
  state.hasChanged = true
})
```

여기서 주요 차이점은 `$patch()`를 사용하면 여러 변경 사항을 devtools의 단일 항목으로 그룹화할 수 있다는 것입니다. `state`와 `$patch()`에 대한 직접적인 변경은 devtools에 나타나며 시간 여행이 가능합니다.(아직 Vue 3에는 없음).

## `state` 교체

`$state`속성을 새 객체로 설정하여 저장소의 전체 상태를 바꿀 수 있습니다 .

```jsx
store.$state = { counter: 666, name: 'Paimon' }
```

pinia 인스턴스의 상태를 변경하여 애플리케이션의 전체 상태를 바꿀 수도 있습니다.

```jsx
pinia.state.value = {}
```

## `state` 구독

Vuex의 `subscribe` 메소드와 유사하게 스토어의 `$subscribe()` 메소드를 통해 상태와 변경 사항을 볼 수 있습니다. 일반 `watch()`보다 `$subscribe()`를 사용하는 이점은 구독이 패치 후에 한 번만 트리거된다는 것입니다(예: 위의 함수 버전을 사용할 때).

```jsx
cartStore.$subscribe((mutation, state) => {
  // 'pinia'에서 { MutationType } 가져오기
  mutation.type // 'direct' | 'patch object' | 'patch function'
  //cartStore.$id와 동일
  mutation.storeId // 'cart'
  // mutation.type === 'patch object'에서만 사용 가능
  mutation.payload // cartStore.$patch()에 전달된 패치 객체

  // 변경될 때마다 전체 상태를 로컬 스토리지에 유지
  localStorage.setItem('cart', JSON.stringify(state))
})
```

기본적으로 `상태구독`은 추가된 컴포넌트에 바인딩됩니다(저장소가 컴포넌트의 `setup()` 내부에 있는 경우). 즉, 컴포넌트가 마운트 해제되면 자동으로 제거됩니다. 컴포넌트가 마운트 해제된 후에도 이를 유지하려면 `{ detached: true }`를 두 번째 인수로 전달하여 현재 컴포넌트에서 상태 구독을 분리합니다.

```jsx
export default {
  setup() {
    const someStore = useSomeStore()

    // this subscription will be kept after the component is unmounted
    someStore.$subscribe(callback, { detached: true })

    // ...
  },
}
```

> **Tip**
`pinia`인스턴스 의 전체 상태를 볼 수 있습니다 .
> 

```jsx
watch(
  pinia.state,
  (state) => {
    // persist the whole state to the local storage whenever it changes
    localStorage.setItem('piniaState', JSON.stringify(state))
  },
  { deep: true }
)
```

# Getters

Getter는 Store 상태에 대한 `computed`와 정확히 동일합니다. `defineStore()`의 `getters` 속성으로 정의할 수 있습니다. 그들은 화살표 함수의 사용을 장려하기 위해 첫 번째 매개변수로 `state`를 받습니다.

```jsx
export const useStore = defineStore('main', {
  state: () => ({
    counter: 0,
  }),
  getters: {
    doubleCount: (state) => state.counter * 2,
  },
})
```

대부분의 경우 `getter`는 `state`에만 의존하지만 `다른 getter`를 사용해야 할 수도 있습니다. 이 때문에 일반 함수를 정의할 때 이를 통해 전체 저장소 인스턴스에 액세스할 수 있지만 리턴 타입의 타입(TypeScript에서)을 정의해야 합니다. 이것은 TypeScript의 알려진 제한으로 인한 것이며 화살표 함수로 정의된 getter나 이것을 사용하지 않는 getter에 영향을 미치지 않습니다.

```jsx
export const useStore = defineStore('main', {
  state: () => ({
    counter: 0,
  }),
  getters: {
    // // 자동으로 리턴 타입을 숫자로 유추합니다.
    doubleCount(state) {
      return state.counter * 2
    },
		// 리턴 타입은 **반드시** 명시적으로 설정되어야 합니다.
    doublePlusOne(): number {
			// 전체 Store에 대한 자동 완성 및 입력 ✨
      return this.doubleCount + 1
    },
  },
})
```

그런 다음 Store 인스턴스에서 직접 getter에 액세스할 수 있습니다.

```jsx
<template>
  <p>Double count is {{ store.doubleCount }}</p>
</template>

<script>
export default {
  setup() {
    const store = useStore()

    return { store }
  },
}
</script>
```

## 다른 getter에 접근

`computed`와 마찬가지로 여러 getters를 결합할 수 있습니다. 이를 통해 다른 getter에 액세스하십시오. TypeScript를 사용하지 않더라도 JSDoc을 사용하여 유형에 대해 IDE에 힌트를 줄 수 있습니다.

```jsx
export const useStore = defineStore('main', {
  state: () => ({
    counter: 0,
  }),
  getters: {
		// `this`를 사용하지 않기 때문에 유형이 자동으로 유추됩니다.
    doubleCount: (state) => state.counter * 2,
    // 여기에 유형을 직접 추가해야 합니다(JS에서 JSDoc 사용). 우리는 또한 할 수 있습니다
		// 이것을 사용하여 getter를 문서화합니다.
		/**
		* 카운터 값 곱하기 2 더하기 1을 반환합니다.
		*
		* @returns {숫자}
		*/
    doubleCountPlusOne() {
			// autocompletion ✨
      return this.doubleCount + 1
    },
  },
})
```

## getter에 매개변수 전달

getter에서 함수를 반환하여 모든 매개변수를 받을 수 있습니다.

```jsx
export const useStore = defineStore('main', {
  getters: {
    getUserById: (state) => {
      return (userId) => state.users.find((user) => user.id === userId)
    },
  },
})
```

컴포넌트에서 사용

```jsx
<script>
export default {
  setup() {
    const store = useStore()

    return { getUserById: store.getUserById }
  },
}
</script>

<template>
  <p>User 2: {{ getUserById(2) }}</p>
</template>
```

이 작업을 수행할 때 getter는 더 이상 캐시되지 않으며 단순히 호출하는 함수입니다. 그러나 getter 자체 내부에 일부 결과를 캐시할 수 있습니다. 이는 드물지만 더 성능이 좋을 것입니다.

```jsx
export const useStore = defineStore('main', {
  getters: {
    getActiveUserById(state) {
      const activeUsers = state.users.filter((user) => user.active)
      return (userId) => activeUsers.find((user) => user.id === userId)
    },
  },
})
```

## 다른 Store getters에 접근

다른 Store getter를 사용하려면 getter 내부에서 직접 사용할 수 있습니다.

```jsx
import { useOtherStore } from './other-store'

export const useStore = defineStore('main', {
  state: () => ({
    // ...
  }),
  getters: {
    otherGetter(state) {
      const otherStore = useOtherStore()
      return state.localData + otherStore.data
    },
  },
})
```

## `setup()` 에서 사용

Store의 속성으로 모든 getter에 직접 접근할 수 있습니다. 

```jsx
export default {
  setup() {
    const store = useStore()

    store.counter = 3
    store.doubleCount // 6
  },
}
```

## Options API에서 사용

### setup() 함수와 사용

```jsx
import { useCounterStore } from '../stores/counterStore'

export default {
  setup() {
    const counterStore = useCounterStore()

    return { counterStore }
  },
  computed: {
    quadrupleCounter() {
      return counterStore.doubleCounter * 2
    },
  },
}
```

### setup() 함수 없이 사용

이전 상태 섹션에서 사용한 것과 동일한 `mapState()`함수를 사용하여 getter에 매핑할 수 있습니다.

# Actions

Actions는 컴포넌트의 메서드와 동일합니다. 그리고 defineStore()의 actions 속성으로 정의할 수 있으며 비즈니스 로직을 정의하는 데 완벽합니다.

```jsx
export const useStore = defineStore('main', {
  state: () => ({
    counter: 0,
  }),
  actions: {
    increment() {
      this.counter++
    },
    randomizeCounter() {
      this.counter = Math.round(100 * Math.random())
    },
  },
})
```

getter와 마찬가지로 Actinos은 전체 타이핑(및 자동 완성 ✨) 지원을 통해 전체 store 인스턴스에 액세스할 수 있습니다. 그들과 달리 Actions는 비동기식일 수 있으며, API 호출이나 다른 Actions까지도 그 안에서 기다릴 수 있습니다! 다음은 Mande를 사용한 예입니다.

```jsx
import { mande } from 'mande'

const api = mande('/api/users')

export const useUsers = defineStore('users', {
  state: () => ({
    userData: null,
    // ...
  }),

  actions: {
    async registerUser(login, password) {
      try {
        this.userData = await api.post({ login, password })
        showTooltip(`Welcome back ${this.userData.name}!`)
      } catch (error) {
        showTooltip(error)
        // let the form component display the error
        return error
      }
    },
  },
})
```

또한 원하는 매개변수를 자유롭게 설정하고 무엇이든 반환할 수 있습니다. Actinos을 호출하면 모든 것이 자동으로 추론됩니다!

Actions은 메서드처럼 호출됩니다.

```jsx
export default defineComponent({
  setup() {
    const main = useMainStore()
		// Store의 메소드로 action 호출
    main.randomizeCounter()

    return {}
  },
})
```

## 다른 Store actions 에 접근하기

다른 Store를 사용하려면 Actions 내에서 직접 사용할 수 있습니다.

```jsx
import { useAuthStore } from './auth-store'

export const useSettingsStore = defineStore('settings', {
  state: () => ({
    preferences: null,
    // ...
  }),
  actions: {
    async fetchUserPreferences() {
      const auth = useAuthStore()
      if (auth.isAuthenticated) {
        this.preferences = await fetchPreferences()
      } else {
        throw new Error('User must be authenticated')
      }
    },
  },
})
```

## setup()과 함께 사용

store의 method로 모든 actions을 직접 호출할 수 있습니다.

```jsx
export default {
  setup() {
    const store = useStore()

    store.randomizeCounter()
  },
}
```

## Options API와 함께 사용

### setup() 함수와 함께

```jsx
import { useCounterStore } from '../stores/counterStore'

export default {
  setup() {
    const counterStore = useCounterStore()

    return { counterStore }
  },
  methods: {
    incrementAndPrint() {
      this.counterStore.increment()
      console.log('New Count:', this.counterStore.count)
    },
  },
}
```

### setup() 함수 없이

Composition API를 전혀 사용하지 않으려면 mapActions() helper 함수를 사용하여 컴포넌트의 메서드로 actions 속성을 매핑할 수 있습니다.

```jsx
import { mapActions } from 'pinia'
import { useCounterStore } from '../stores/counterStore'

export default {
  methods: {
		// 구성 요소 내부의 this.increment()에 대한 액세스를 제공합니다.
		// store.increment()에서 호출하는 것과 동일
    ...mapActions(useCounterStore, ['increment'])
		// 위와 같지만 this.myOwnName()으로 등록
    ...mapActions(useCounterStore, { myOwnName: 'doubleCounter' }),
  },
}
```

## actions 구독

`store.$onAction()`을 사용하여 actions과 결과를 관찰할 수 있습니다. 전달된 콜백은 actions 자체보다 먼저 실행됩니다. 애프터 핸들은 약속하고 작업이 해결된 후 함수를 실행할 수 있도록 합니다. 비슷한 방식으로 onError를 사용하면 액션이 throw되거나 거부되는 경우 함수를 실행할 수 있습니다. 이는 Vue 문서의 이 팁과 유사하게 런타임에 오류를 추적하는 데 유용합니다.

다음은 작업을 실행하기 전과 해결/거부한 후 기록하는 예입니다.

```jsx
const unsubscribe = someStore.$onAction(
  ({
		name, // 액션의 이름
		store, // 인스턴스 저장, `someStore`와 동일
		args, // 액션에 전달된 매개변수의 배열
		after, // 액션이 반환되거나 해결된 후 후크
		onError, // 액션이 throw되거나 거부되면 후크
  }) => {
    // 이 특정 액션 호출을 위한 공유 변수
    const startTime = Date.now()
    // 이것은 `store`에 대한 작업이 실행되기 전에 트리거됩니다.
    console.log(`Start "${name}" with params [${args.join(', ')}].`)

		// 작업이 성공하고 완전히 실행된 후에 트리거됩니다.
		// 반환된 약속을 기다립니다.
    after((result) => {
      console.log(
        `Finished "${name}" after ${
          Date.now() - startTime
        }ms.\nResult: ${result}.`
      )
    })

		// 액션이 거부하는 프라미스를 던지거나 반환하면 트리거됩니다.
    onError((error) => {
      console.warn(
        `Failed "${name}" after ${Date.now() - startTime}ms.\nError: ${error}.`
      )
    })
  }
)

// 리스너를 수동으로 제거
unsubscribe()
```

기본적으로 actions 구독은 추가된 컴포넌트에 바인딩됩니다(저장소가 구성 요소의 setup() 내부에 있는 경우). 즉, 컴포넌트가 마운트 해제되면 자동으로 제거됩니다. 컴포넌트가 마운트 해제된 후에도 이를 유지하려면 true를 두 번째 인수로 전달하여 현재 구성 요소에서 actions 구독을 분리합니다.

# Plugins with Pinia

낮은 수준의 API 덕분에 Pinia Store를 완전히 확장할 수 있습니다.

- Store에 새 속성 추가
- Store을 정의할 때 새로운 옵션 추가
- Store에 새로운 방법 추가
- 기존 메서드 래핑
- actions 변경 또는 취소
- [로컬 스토리지](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage) 와 같은 부작용 구현
- 특정 Store**에만** 적용

플러그인은 `pinia.use()`를 사용하여 pinia 인스턴스에 추가됩니다. 가장 간단한 예는 객체를 반환하여 모든 저장소에 정적 속성을 추가하는 것입니다.

```jsx
import { createPinia } from 'pinia'

// 이 플러그인이 설치된 후 생성되는 모든 저장소에 `secret`이라는 속성을 추가합니다.
// 이것은 다른 파일에 있을 수 있습니다.
function SecretPiniaPlugin() {
  return { secret: 'the cake is a lie' }
}

const pinia = createPinia()
// 플러그인을 pinia에 제공
pinia.use(SecretPiniaPlugin)

// 다른 파일에서
const store = useStore()
store.secret // 'the cake is a lie' 출력
```

이것은 router, modal, toast manager와 같은 전역 객체를 추가하는 데 유용합니다.

## 소개

Pinia 플러그인은 Store 추가할 속성을 선택적으로 반환하는 기능입니다. 그리고 context 매개변수를 받습니다.

```jsx
export function myPiniaPlugin(context) {
	context.pinia // `createPinia()`로 생성된 pinia
	context.app // `createApp()`으로 생성된 현재 앱(Vue 3만 해당)
	context.store // 플러그인이 확장 중인 저장소
	context.options // `defineStore()`에 전달된 저장소를 정의하는 옵션 객체
}
```

이 함수를 `pinia.use()` 를 사용하여 파라미터로 전달합니다.

```jsx
pinia.use(myPiniaPlugin)
```

플러그인은 `pinia`가 `app`에 전달된 후에 생성된 Store에만 적용됩니다.

## Store 확장

플러그인에서 객체를 반환하기만 하면 모든 Store에 속성을 추가할 수 있습니다.

```jsx
pinia.use(() => ({ hello: 'world' }))
```

`store`에서 직접 속성을 설정할 수도 있지만, 가능한 경우 객체를 리턴하여 devtools에서 자동으로 추적할 수 있도록 합니다.

```jsx
pinia.use(({ store }) => {
  store.hello = 'world'
})
```

플러그인에 의해 반환된 모든 속성은 devtools에 의해 자동으로 추적되므로 devtools에서 `hello`를 표시하려면 devtools에서 디버그하려는 경우에만 dev 모드의 `store._customProperties`에 추가해야 합니다.

```jsx
// 위의 예에서
pinia.use(({ store }) => {
  store.hello = 'world'
	// 번들러가 이것을 처리하는지 확인하십시오. webpack 및 vite는 기본적으로 수행해야 합니다.
  if (process.env.NODE_ENV === 'development') {
		// 스토어에서 설정한 키를 추가합니다.
    store._customProperties.add('hello')
  }
})
```

## 새로운 `state` 추가

Store에 새로운 `state` 속성을 추가하거나 hydration 중에 사용할 속성을 추가하려면 두 위치에 추가해야 합니다.

- Store에서 `store.myState`로 액세스할 수 있습니다.
- `store.$state`에서 devtools에서 사용할 수 있고 SSR 동안 직렬화할 수 있습니다.

이렇게 하면 ref 또는 계산된 속성을 공유할 수 있습니다.
