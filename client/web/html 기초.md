# Web

- 웹의 경우 경험을 많이 해보는 것이 중요하다
- 시각적인 부분이 많이 작동하기에 코드 작성 틈틈이 화면을 확인하여 원리를 이해하자

## HTML / CSS

---

- Web이란?
    - 웹 사이트의 구성 요소
    - 웹 표준과 크로스 브라우징
    - 개발 환경 설정
- HTML
    - HTML 기본구조
    - HTML 문서 구조화
- CSS
    - CSS Selectors
    - CSS 단위
    - CSS Selectors 심화
    - Box Model
    - CSS Display
    - CSS Position

## 웹 사이트의 구성 요소

---

- 웹 사이트란 브라우저를 통해서 접속하는 웹 페이지(문서)들의 모음
- 웹 페이지는 글, 그림, 동영상 등 여러가지 정보를 담고 있으며, 마우스로 클릭하면 다른 웹 페이지로 이동하는 ‘링크'들이 있음
    - ‘링크'를 통해 여러 웹 페이지를 연결한 것을 웹 사이트라고 함

<img width="895" alt="html_1" src="https://user-images.githubusercontent.com/86648892/183297271-36c0afda-5de3-4cec-8b7c-15b463aebeba.png">

- HTML은 구조를 담당
    - 처리나 계산과 같은 동작을 하는건 아니어서 엄밀히 따지면 프로그래밍 언어가 아니다
    - 건물 설계
- CSS는 표현, 그리고 애니메이션과 같은 약간의 동작을 담당
    - 건물 인테리어
- Javascript는 처리, 계산과 같은 동작을 담당
    - 건물 내 엘리베이터, IOT Home

## 브라우저

---

- 웹 사이트는 브라우저를 통해 동작함
    - 브라우저 안에는 HTML 문서를 실행하기 위한 기능들이 들어가 있음
        - .hwp, .doc 등의 파일들이 HTML 문서라면 msword, 한컴오피스 등은 브라우저와 같은 개념
- 브라우저마다 작동 방식이 달라 문제가 생길 때가 있다
    - 파편화
- 이에 대한 해결책으로 웹 표준이 등장함

## 웹 표준

---

- 웹에서 표준적으로 사용되는 기술이나 규칙
- 크로스 브라우징
    - 어떤 브라우저든 웹 페이지가 동일하게 보이도록 함

<img width="799" alt="html_2" src="https://user-images.githubusercontent.com/86648892/183297274-38e16723-8b56-47b0-891e-9b7e8cec63c6.png">

- W3C는 웹 표준을 만드는 단체
    - 회원사가 많아 결정이 느림
        - 이에 따라 WHATWG가 HTML 5라는 표준을 제안했고, 현재 대세
- [caniuse](https://caniuse.com/)
    - 사용하고 싶은 기술을 검색하면 브라우저 호환성을 확인할 수 있음

## 개발환경 설정(Chrome)

---

- VSCode Extensions 추천
    - open in browser
    - auto rename tag
    - highlight matching tag
    - live server
- Chrome 개발자 도구
    - F12 or 우클릭 후 검사
    - Elements
        - DOM 탐색 및 CSS 확인 및 변경
        - Styles
            - 요소에 적용된 CSS 확인
        - Computed
            - 스타일이 계산된 최종 결과
        - Event Listeners
            - 해당 요소에 적용된 이벤트 (Javascript)
    - Sources, Network, Performance, Application, Security, Audits 등

# HTML

## HTML(Hyper Text Markup Language)

---

### Hyper Text?

- 참조(하이퍼링크)를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트
- 팀 버너스 리가 기획한 이론
    - 이 문서에서 다른 문서로 즉시 접근할 수 있는 것이 이 세상의 텍스트를 초월한 것과 같다하여 하이퍼 텍스트라 이해하자

### Markup Language

- 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어
- 태그 + 구조!
- ex) HTML, Markdown

<img width="1137" alt="html_3" src="https://user-images.githubusercontent.com/86648892/183297276-2e5ed0e9-ddf2-4b6e-aaeb-20c4481da5f6.png">

## HTML

---

- 웹 페이지를 작성(구조화)하기 위한 언어
- .html
- HTML 스타일 가이드
    - indent 2칸 (indent가 없어도 문제는 없지만 사실상 해야함)
- HTML이란
    - 태그를 이용하여 구조를 만들고
        - 브라우저로 실행하는 문서
            - **태그, 구조, 브라우저, 문서**

### HTML 기본 구조

- html: 문서의 최상위(root) 요소
    - html 태그로 문서를 열고 닫음
- head: 문서 메타데이터 요소
    - 데이터를 위한 데이터를 메타데이터라 함
    - 문서 제목, 인코딩, 스타일, 외부 파일 로딩 등
    - 일반적으로 브라우저에 나타나지 않는 내용
- body: 문서 본문 요소
    - 실제 화면 구성과 관련된 내용

### head 예시

- `<title>` : 브라우저 상단 타이틀
- `<meta>` : 문서 레벨 메타데이터 요소
- `<link>` : 외부 리소스 연결 요소 (CSS 파일, favicon 등)
- `<script>` : 스크립트 요소 (Javascript 파일 / 코드)
- `<style>` : CSS 직접 작성

<img width="405" alt="html_4" src="https://user-images.githubusercontent.com/86648892/183297278-196527ad-5267-4f90-ac31-f4fcee0822b8.png">

<img width="612" alt="html_5" src="https://user-images.githubusercontent.com/86648892/183297279-5b9dcff5-48fb-4d5a-9300-164e0fac2f96.png">

### head의 또 다른 예시 : Open Graph Protocol

- 메타데이터를 표현하는 새로운 규약
    - HTML 문서의 메타데이터를 통해 문서의 정보를 전달
    - 메타정보에 해당하는 제목, 설명 등을 쓸 수 있도록 정의
    - 메타 property에 설정하면 원하는대로 내용이 나옴
        - 썸네일 같은 것들을 OG protocol을 사용하여 메타데이터 표현함
        - 이런 메타데이터 부분도 실제 개발자들이 다 개발하는 것

<img width="494" alt="html_6" src="https://user-images.githubusercontent.com/86648892/183297282-7b7178ea-65de-40eb-bfca-0f6977c5ab62.png">

### HTML 요소(element)

- HTML 요소 == 태그와 내용

```html
<h1>contents</h1>

<!-- <h1>은 시작 태그, </h1>은 종료 태그 -->
<!-- HTML의 요소는 태그와 내용(contents)으로 구성되어 있다. -->
```

- HTML 요소는 시작 태그와 종료 태그, 그리고 태그 사이에 위치한 내용으로 구성
    - 요소는 태그로 컨텐츠(내용)를 감싸는 것으로 그 정보의 성격과 의미를 정의
    - 내용이 없는 태그들도 존재
        - 닫는 태그가 없음
        - br, hr, img, input, link, meta
- 요소는 중첩(nested)될 수 있음
    - 요소의 중첩을 통해 하나의 문서를 구조화
    - 여는 태그와 닫는 태그의 쌍을 잘 확인!
        - 오류를 반환하는 것이 아닌 그냥 레이아웃이 깨진 상태로 출력
            - 디버깅이 어려움
- 개발자 도구를 통해 원하는 elements를 선택하여 탐색 가능
    - 복잡한 형태의 경우 Elements 탭에서 HTML 구조를 추가 탐색

<img width="824" alt="html_7" src="https://user-images.githubusercontent.com/86648892/183297284-1403b96f-f827-44df-a164-28bacdaf98ec.png">

### HTML 속성(attribute)

```html
<a href="https://google.com"></a>

<!-- 위 코드에서 href는 속성명, "https://google.com"은 속성값 -->
<!-- 태그별로 사용할 수 있는 속성은 다르다 -->
<!-- a는 anchor로 일종의 이동, href는 링크명 -->
<!-- 속성 지정 스타일 가이드는 1)공백없음 2)쌍따옴표 사용 -->
```

- 속성을 통해 태그의 부가적인 정보를 설정할 수 있음
- 요소는 속성을 가질 수 있으며, 경로나 크기와 같은 추가적인 정보를 제공
- 요소의 시작 태그에 작성
    - 보통 이름과 값이 하나의 쌍으로 존재
- HTML Global Attribute
    - 태그와 상관없이 사용 가능한 속성들도 있음

### HTML Global Attribute

- 모든 HTML 요소가 공통으로 사용할 수 있는 대표적인 속성 (몇몇 요소에는 아무 효과가 없을 수 있음)
    - id : 문서 전체에서 유일한 고유 식별자 지정
    - class: 공백으로 구분된 해당 요소의 클래스의 목록
        - CSS, JS에서 요소를 선택하거나 접근
    - data-* : 페이지에 개인 사용자 정의 데이터를 저장하기 위해 사용
        - 좋아요 기능같은 것들을 만들 때 사용
    - style : inline 스타일
    - title : 요소에 대한 추가 정보 지정
    - tabindex : 요소의 탭 순서

<img width="639" alt="html_8" src="https://user-images.githubusercontent.com/86648892/183297286-f8f18222-24f0-412e-97a4-ae2c00e92159.png">

### HTML 코드 예시

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Document</title>
</head>
<body>
  <!-- 이것은 주석입니다. -->
  <h1>나의 첫번째 HTML</h1>
  <p>이것은 본문입니다.</p>
  <span>이것은 인라인요소</span>
  <a href="https://www.naver.com">네이버로 이동!!</a>
</body>
</html>

```

<img width="707" alt="html_9" src="https://user-images.githubusercontent.com/86648892/183297289-d166855c-9295-41ba-a529-4e0cb0957372.png">

## 시맨틱 태그

---

- HTML 태그가 특정 목적, 역할 및 의미적 가치(semantic value)를 가지는 것
    - 예를 들어 h1 태그는 “이 페이지에서 최상위 제목"인 텍스트를 감싸는 역할(또는 의미)을 나타냄
- Non semantic 요소
    - div, span
        - div : 콘텐츠의 구획을 나타냄(블록 요소)
        - span: 인라인 요소
- a, form, table 태그들도 시맨틱 태그로 볼 수 있음
- HTML 5에서는 기존에 단순히 콘텐츠의 구획을 나타내기 위해 사용한 div 태그르 대체하여 사용하기 위해 의미론적 요소를 담은 태그들이 추가됨
- 대표적인 시맨틱 태그 목록
    - header : 문서 전체나 섹션의 헤더(머리말 부분)
    - nav : 내비게이션
    - aside : 사이드에 위치한 공간, 메인 콘텐츠와 관련성이 적은 콘텐츠
    - section : 문서의 일반적인 구분, 컨텐츠의 그룹을 표현
    - article : 문서, 페이지, 사이트 안에서 독립적으로 구분되는 영역
    - footer : 문서 전체나 섹션의 푸터(마지막 부분)
    
    <img width="421" alt="html_10" src="https://user-images.githubusercontent.com/86648892/183297290-0f74f310-0813-4db2-8068-f8b60b3c1f65.png">
    
- 왼쪽 오른쪽은 똑같이 작동하더라도 코드를 봤을 때 시맨틱 태그가 의미를 알기 쉬움

<img width="807" alt="html_11" src="https://user-images.githubusercontent.com/86648892/183297291-038b78d8-587c-4beb-8f86-a8753f515a5d.png">

- 구글 뉴스 상단의 메뉴는 Header 태그를 통해서 명확하게 표현하고 있음

<img width="662" alt="html_12" src="https://user-images.githubusercontent.com/86648892/183297292-4f639c8a-ba17-411f-8bec-78ed6a0e0274.png">

<img width="816" alt="html_13" src="https://user-images.githubusercontent.com/86648892/183297293-ba2669de-2d9e-4b09-b677-0c0371792508.png">

<img width="858" alt="html_14" src="https://user-images.githubusercontent.com/86648892/183297295-4110f3f4-df5e-4e3b-9c4a-6b8f7be89ffc.png">

<img width="892" alt="html_15" src="https://user-images.githubusercontent.com/86648892/183297296-ea5e241d-7912-4a43-88e3-892e49fcc35e.png">

### WHY 시맨틱 태그?

- 의미론적 마크업
    - 개발자 및 사용자 뿐만 아니라 검색엔진 등에 의미있는 정보의 그룹을 태그로 표현
    - 단순히 구역을 나누는 것이 뿐만 아니라 ‘의미'를 가지는 태그들을 활용하기 위한 노력
    - 요소의 의미가 명확해지기 때문에 코드의 가독성을 높이고 유지보수를 쉽게 함
    - 검색 엔진 최적(SEO)를 위해서 메타태그, 시맨틱 태그 등을 통한 마크업을 효과적으로 활용해야 함

## 렌더링(Rendering)

---

- 텍스트로 작성된 코드가 어떻게 웹 사이트가 되는걸까?
- 웹사이트 코드를 사용자가 보게 되는 웹사이트로 바꾸는 과정을 렌더링이라 한다

## DOM(Document Object Model) 트리

---

- 텍스트 파일인 HTML 문서를 브라우저에서 렌더링하기 위한 구조
    - HTML 문서에 대한 모델을 구성함
    - HTML 문서 내의 각 요소에 접근 / 수정에 필요한 프로퍼티와 메서드를 제공함
- DOM에 따라 잘라서 기억해놨다가 화면에 그리는 느낌이라 생각하면 편하다

<img width="303" alt="html_16" src="https://user-images.githubusercontent.com/86648892/183297297-a42b81ea-73d7-46e5-94bd-311c1851a945.png">

<img width="888" alt="html_17" src="https://user-images.githubusercontent.com/86648892/183297300-e8c4f002-4717-4efc-8257-2ad250879f00.png">

## HTML 문서 구조화

---

### 인라인 / 블록 요소

- HTML 요소는 크게 인라인 / 블록 요소로 나눔
- 인라인 요소는 글자처럼 취급
- 블록 요소는 한 줄 모두 사용
- `<태그>내용</태그>`로 표현되는 HTML 요소를 분류하자면 인라인, 블록 요소로 구분할 수 있다는 것이다

### 텍스트 요소(Inline)

```html
<!-- 태그 -->
<!-- 설명 -->

<a></a>
<!-- href 속성을 활용하여 다른 URL로 연결하는 하이퍼링크 생성 -->

<b></b>
<strong></strong>
<!-- 굵은 글씨 요소 -->
<!-- 중요한 강조하고자 하는 요소(보통 굵은 글씨로 표현) -->

<i></i>
<em></em>
<!-- 기울임 글씨 요소 -->
<!-- 중요한 강조하고자 하는 요소(보통 기울임 글씨로 표현) -->

<br>
<!-- 텍스트 내에 줄 바꿈 생성 -->
<!-- 브라우저에서 enter를 친 것 같은 효과 -->

<img>
<!-- src 속성을 활용하여 이미지 표현 -->

<span></span>
<!-- 의미없는 인라인 컨테이너 -->
```

<img width="541" alt="html_18" src="https://user-images.githubusercontent.com/86648892/183297302-2cb61fe9-a928-4672-aa73-2e09fd05610a.png">

### 그룹 컨텐츠(Block)

```html
<!-- 태그 -->
<!-- 설명 -->

<p></p>
<!-- 하나의 문단(paragraph) -->

<hr>
<!-- 문단 레벨 요소에서의 주제의 분리를 의미하며 수평선으로 표현됨 (A Horizontal Rule) -->

<ol></ol>
<ul></ul>
<!-- 순서가 있는 리스트(ordered) -->
<!-- 순서가 없는 리스트(unordered) -->

<pre></pre>
<!-- HTML에 작성한 내용 그대로 표현 -->
<!-- 보통 고정폭 글꼴이 사용되고 공백문자를 유지 -->

<blockquote></blockquote>
<!-- 텍스트가 긴 인용문 -->
<!-- 주로 들여쓰기를 한 것으로 표현됨 -->

<div></div>
<!-- 의미없는 블록 레벨 컨테이너 -->
```

<img width="538" alt="html_19" src="https://user-images.githubusercontent.com/86648892/183297303-e38757d0-9c97-48a8-8bbd-1d555595d1a4.png">

- div와 span은 다른 작업을 위한 일종의 투명한 쇼핑백과 같은 것이다

### form

- `<form>`은 정보(데이터)를 서버에 제출하기 위해 사용하는 태그
    - 즉, 사용자가 브라우저를 통해 서버에 데이터를 전송하고 싶을 때 사용
- `<form>` 기본 속성
    - action: form을 처리할 서버의 URL(데이터를 보낼 곳)
    - method: form을 제출할 때 사용할 HTTP 메서드(GET or POST)
    - enctype: method가 post인 경우 데이터의 유형
        - application/x-www-form-urlencoded: 기본값
        - multipart/form-data: 파일 전송 시(input type이 file인 경우)
        - text/plain: HTML 5 디버깅용(잘 사용되지 않음)
- form안에 input 태그들을 넣어서 입력을 받는다
- input 태그는 label 태그와 함께 사용
    - input 태그에 대한 상세한 설명을 label에 붙임
    - input의 `id`와 label의 `for` 연결
    - form의 action은 URL path parameter에 추가되는 내용 input의 name, value 쌍은 query string에 들어가는 내용이라 생각하자

<img width="768" alt="html_20" src="https://user-images.githubusercontent.com/86648892/183297305-ce34aabe-f525-412d-af6e-2066017d4f85.png">

### input

- 다양한 타입을 가지는 입력 데이터 유형과 위젯이 제공됨
- `<input>` 대표 속성
    - name: form control에 적용되는 이름 (이름 / 값 페어로 전송됨)
    - value: form control에 적용되는 값 (이름 / 값 페어로 전송됨)
    - required, readonly, autofocus, autocomplete, disabled 등

### input label

- label을 클릭하여 input 자체의 초점을 맞추거나 활성화시킬 수 있음
    - 사용자는 선택할 수 있는 영역이 늘어나 웹 / 모바일(터치) 환경에서 편하게 사용할 수 있음
    - label과 input 입력의 관계가 시각적 뿐만 아니라 화면리더기에서도 label을 읽어 쉽게 내용을 확인할 수 있도록 함
- `<input>`에 id 속성을, `<label>`에는 for 속성을 활용하여 상호 연관을 시킴

### input 유형 (입력)

- 입력 타입별로 HTML 기본 검증 및 추가 속성 활용이 가능
    - text: 일반 텍스트 입력
    - password: 입력 시 값이 보이지 않고 문자를 특수기호’*’로 표현
    - email: 이메일 형식이 아닌 경우 form 제출 불가
    - number: min, max, step 속성을 활용하여 숫자 범위 설정 가능
    - file: accept 속성을 활용하여 파일 타입 지정 가능
    
    <img width="376" alt="html_21" src="https://user-images.githubusercontent.com/86648892/183297306-442aca48-1248-4364-bf41-e2bf44d52ef3.png">
    

### input 유형 (항목 중 선택)

- checkbox, radio
- 일반적으로 label 태그와 함께 사용하여 선택 항목을 작성함
- 동일 항목에 대해서는 name을 지정하고 선택된 항목에 대한 value를 지정해야함
    - checkbox: 다중 선택
    - radio: 단일 선택

### input 유형 (기타)

- picker
    - color: color picker
    - date: date picker
- hidden input을 활용하여 사용자 입력을 받지 않고 서버에 전송되어야 하는 값을 설정
    - hidden: 사용자에게 보이지 않는 input

<img width="262" alt="html_22" src="https://user-images.githubusercontent.com/86648892/183297307-217b953f-9fff-4def-9a15-6bfa4fdd1dc2.png">

### input 유형 (종합)

- `<input>` 요소의 동작은 type에 따라 달라지므로, 각각의 내용을 숙지할 것
- 지정하지 않을 경우 기본값은 `text`
- [MDN docs input](https://developer.mozilla.org/ko/docs/Web/HTML/Element/Input)

## HTML 마크업 예시

---

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>Form 활용 실습</h1>
    <form action="">
      <!-- autofocus 및 label 확인 -->
      <!-- autofocus는 브라우저 실행 시 커서가 해당 부분에 자동 설정 -->
      <div class="input-group">
        <label for="username">아이디</label>
      </div>
      <input type="text" name="username" id="username" autofocus>

      <!-- disabled 및 value 확인 -->
      <!-- disabled는 해당 input 입력 불가 상태, value는 기본으로 들어가있는 값 -->
      <div class="input-group">
        <label for="name">이름</label>
      </div>
      <input type="text" name="name" value="홍길동" id="name" disabled>

      <!-- label 확인 -->
      <!-- checked는 기본적으로 체크되어있는 상태로 설정 -->
      <div class="input-group">
        <label for="agreement">개인정보 수집에 동의합니다.</label>
      </div>
      <input type="checkbox" name="agreement" id="agreement" checked>
      <div class="input-group">
        <label>최종 제출을 확인합니다.</label>
      </div>
      <input type="checkbox">
    </form>
    <!-- 제출 버튼 -->
    <input type="submit" value="제출">
</body>
</html>
```

<img width="262" alt="html_23" src="https://user-images.githubusercontent.com/86648892/183297308-3ab6f19a-366b-4d81-ad36-a872865048ae.png">

```html
<div>
 <p>checkbox</p>
 <input type="checkbox" id="html" name="language" value="html" checked>
 <label for="html">HTML</label>
 <input type="checkbox" id="python" name="language" value="python" checked>
 <label for="python">Python</label>
 <input type="checkbox" id="java" name="language" value="java">
 <label for="java">Java</label>
  <hr>
</div>
```

<img width="365" alt="html_24" src="https://user-images.githubusercontent.com/86648892/183297310-5b7052ed-228b-406a-827e-c2f5f3a8a57d.png">

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <header>
    <a href="https://www.ssafy.com">
      <img src="ssafy.png" alt="main img" width="300">
    </a>
    <h1>SSAFY 학생 건강설문</h1>
  </header>
  <section>
    <form action="#">
      <div>
        <label for="name">이름을 기재해주세요.</label><br>
        <input type="text" id="name" name="name" autofocus>
      </div>
      <!-- required는 반드시 값을 선택해야 넘어갈 수 있음 -->
      <div>
        <label for="region">지역을 선택해주세요.</label><br>
        <select name="region" id="region" required>
          <option value="">선택</option>
          <option value="서울">서울</option>
          <option value="대전">대전</option>
          <option value="광주">광주</option>
          <option value="구미">구미</option>
          <option value="강원" disabled>강원</option>
        </select>
      </div>
      <div>
        <p>오늘의 체온을 선택해주세요.</p>
        <input type="radio" name="body-heat" id="normal" value="normal" checked>
        <label for="normal">37도 미만</label><br>
        <input type="radio" name="body-heat" id="warning" value="warning">
        <label for="warning">37도 이상</label>
      </div>
      <input type="submit" value="제출">
    </form>
  </section>
  <footer>
    Google 설문지를 통해 비밀번호를 제출하지 마시오.
  </footer>
</body>
</html>
```

<img width="357" alt="html_25" src="https://user-images.githubusercontent.com/86648892/183297312-ef6d7ed3-942e-4d35-b7fb-ee5398c6f6bb.png">
