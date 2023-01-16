# Web

- 웹의 경우 경험을 많이 해보는 것이 중요하다
- 시각적인 부분이 많이 작동하기에 코드 작성 틈틈이 화면을 확인하여 원리를 이해하자

# HTML / CSS

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

---

# Web?

## 웹 사이트의 구성 요소

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

- 웹 사이트는 브라우저를 통해 동작함
    - 브라우저 안에는 HTML 문서를 실행하기 위한 기능들이 들어가 있음
        - .hwp, .doc 등의 파일들이 HTML 문서라면 msword, 한컴오피스 등은 브라우저와 같은 개념
- 브라우저마다 작동 방식이 달라 문제가 생길 때가 있다
    - 파편화
- 이에 대한 해결책으로 웹 표준이 등장함

## 웹 표준

- 웹에서 표준적으로 사용되는 기술이나 규칙
- 크로스 브라우징
    - 어떤 브라우저든 웹 페이지가 동일하게 보이도록 함

<img width="799" alt="html_2" src="https://user-images.githubusercontent.com/86648892/183297274-38e16723-8b56-47b0-891e-9b7e8cec63c6.png">

- W3C는 웹 표준을 만드는 단체
    - 회원사가 많아 결정이 느림
        - 이에 따라 WHATWG가 HTML 5라는 표준을 제안했고, 현재 대세
- [caniuse](https://caniuse.com/)
    - 사용하고 싶은 기술을 검색하면 브라우저 호환성을 확인할 수 있음

---

# 개발환경 설정(Chrome)

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

---

# HTML(Hyper Text Markup Language)

## Hyper Text?

- 참조(하이퍼링크)를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트
- 팀 버너스 리가 기획한 이론
    - 이 문서에서 다른 문서로 즉시 접근할 수 있는 것이 이 세상의 텍스트를 초월한 것과 같다하여 하이퍼 텍스트라 이해하자

## Markup Language

- 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어
- 태그 + 구조!
- ex) HTML, Markdown

<img width="1137" alt="html_3" src="https://user-images.githubusercontent.com/86648892/183297276-2e5ed0e9-ddf2-4b6e-aaeb-20c4481da5f6.png">

## HTML

- 웹 페이지를 작성(구조화)하기 위한 언어
- .html
- HTML 스타일 가이드
    - indent 2칸 (indent가 없어도 문제는 없지만 사실상 해야함)
- HTML이란
    - 태그를 이용하여 구조를 만들고
        - 브라우저로 실행하는 문서
            - **태그, 구조, 브라우저, 문서**

## HTML 기본 구조

- html: 문서의 최상위(root) 요소
    - html 태그로 문서를 열고 닫음
- head: 문서 메타데이터 요소
    - 데이터를 위한 데이터를 메타데이터라 함
    - 문서 제목, 인코딩, 스타일, 외부 파일 로딩 등
    - 일반적으로 브라우저에 나타나지 않는 내용
- body: 문서 본문 요소
    - 실제 화면 구성과 관련된 내용

## head 예시

- `<title>` : 브라우저 상단 타이틀
- `<meta>` : 문서 레벨 메타데이터 요소
- `<link>` : 외부 리소스 연결 요소 (CSS 파일, favicon 등)
- `<script>` : 스크립트 요소 (Javascript 파일 / 코드)
- `<style>` : CSS 직접 작성

<img width="405" alt="html_4" src="https://user-images.githubusercontent.com/86648892/183297278-196527ad-5267-4f90-ac31-f4fcee0822b8.png">

<img width="612" alt="html_5" src="https://user-images.githubusercontent.com/86648892/183297279-5b9dcff5-48fb-4d5a-9300-164e0fac2f96.png">

## head의 또 다른 예시 : Open Graph Protocol

- 메타데이터를 표현하는 새로운 규약
    - HTML 문서의 메타데이터를 통해 문서의 정보를 전달
    - 메타정보에 해당하는 제목, 설명 등을 쓸 수 있도록 정의
    - 메타 property에 설정하면 원하는대로 내용이 나옴
        - 썸네일 같은 것들을 OG protocol을 사용하여 메타데이터 표현함
        - 이런 메타데이터 부분도 실제 개발자들이 다 개발하는 것

<img width="494" alt="html_6" src="https://user-images.githubusercontent.com/86648892/183297282-7b7178ea-65de-40eb-bfca-0f6977c5ab62.png">

## HTML 요소(element)

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

## HTML 속성(attribute)

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

## HTML Global Attribute

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

## HTML 코드 예시

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

## WHY 시맨틱 태그?

- 의미론적 마크업
    - 개발자 및 사용자 뿐만 아니라 검색엔진 등에 의미있는 정보의 그룹을 태그로 표현
    - 단순히 구역을 나누는 것이 뿐만 아니라 ‘의미'를 가지는 태그들을 활용하기 위한 노력
    - 요소의 의미가 명확해지기 때문에 코드의 가독성을 높이고 유지보수를 쉽게 함
    - 검색 엔진 최적(SEO)를 위해서 메타태그, 시맨틱 태그 등을 통한 마크업을 효과적으로 활용해야 함

## 렌더링(Rendering)

- 텍스트로 작성된 코드가 어떻게 웹 사이트가 되는걸까?
- 웹사이트 코드를 사용자가 보게 되는 웹사이트로 바꾸는 과정을 렌더링이라 한다

## DOM(Document Object Model) 트리

- 텍스트 파일인 HTML 문서를 브라우저에서 렌더링하기 위한 구조
    - HTML 문서에 대한 모델을 구성함
    - HTML 문서 내의 각 요소에 접근 / 수정에 필요한 프로퍼티와 메서드를 제공함
- DOM에 따라 잘라서 기억해놨다가 화면에 그리는 느낌이라 생각하면 편하다

<img width="303" alt="html_16" src="https://user-images.githubusercontent.com/86648892/183297297-a42b81ea-73d7-46e5-94bd-311c1851a945.png">

<img width="888" alt="html_17" src="https://user-images.githubusercontent.com/86648892/183297300-e8c4f002-4717-4efc-8257-2ad250879f00.png">

---

# HTML 문서 구조화

## 인라인 / 블록 요소

- HTML 요소는 크게 인라인 / 블록 요소로 나눔
- 인라인 요소는 글자처럼 취급
- 블록 요소는 한 줄 모두 사용
- <태그>내용</태그>로 표현되는 HTML 요소를 분류하자면 인라인, 블록 요소로 구분할 수 있다는 것이다

## 텍스트 요소(Inline)

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

## 그룹 컨텐츠(Block)

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

## form

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

- <input> 요소의 동작은 type에 따라 달라지므로, 각각의 내용을 숙지할 것
- 지정하지 않을 경우 기본값은 `text`
- [MDN docs input](https://developer.mozilla.org/ko/docs/Web/HTML/Element/Input)

---

## HTML 마크업 예시

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

---

# CSS

- Cascading Styel Sheets
- 선택하고, 스타일을 지정한다
- CSS 구문은 선택자를 통해 스타일을 지정할 HTML 요소를 선택
    - 중괄호 안에서는 속성과 값, 하나의 쌍으로 이루어진 선언을 진행
        - 각 쌍은 선택한 요소의 속성, 속성에 부여할 값을 의미
            - 속성(Property): 어떤 스타일 기능을 변경할지 결정
            - 값(Value): 어떻게 스타일 기능을 변경할지 결정

<img width="812" alt="html_26" src="https://user-images.githubusercontent.com/86648892/183297313-9c8749ef-3df0-4e71-ad25-169e924f7d92.png">

## CSS 정의 방법

- 인라인(inline)
    - html 요소 태그 안에 직접 `<style>` 지정
- 내부 참조(embedding)
    - `<head>`안에
        - `<style>`지정
        - 선택자 사용
- 외부 참조(link file)
    - 분리된 CSS 파일
    - `<head>`안에
        - `<link rel=”stylesheet” hreft=”mystyle.css”>` 와 같이 선언하여 mystyle.css파일 참조하도록 지정

### CSS with 개발자 도구

- Styles: 해당 요소에 선언된 모든 CSS
- Computed: 해당 요소에 최종 계산된 CSS

---

## CSS Selectors

### 선택자(Selector) 유형

- 기본 선택자
    - 전체 선택자, 요소 선택자
    - 클래스 선택자, 아이디 선택자, 속성 선택자
- 결합자(Combinators)
    - 자손 결합자, 자식 결합자
        - 자손
            - 공백
        - 자식
            - `>`
    - 일반 형제 결합자, 인접 형제 결합자
        - 일반 형제 결합자
            - `~`
        - 인접 형제 결합자
            - `+`
- 의사 클래스 / 요소(Pseudo Class)
    - 링크, 동적 의사 클래스
    - 구조적 의사 클래스, 기타 의사 클래스, 의사 엘리먼트, 속성 선택자

### 기본 선택자

- 전체 선택자
    - `*`
- 요소 선택자
    - HTML 태그를 직접 선택
- 클래스(class) 선택자
    - `.`
    - 마침표(.)문자로 시작하며, 해당 클래스가 적용된 항목을 선택
- 아이디(id) 선택자
    - `#`
    - 해당 아이디가 적용된 항목을 선택
    - 일반적으로 하나의 문서에 1번만 사용
    - 여러번 사용해도 동작하지만, 단일 id 사용을 권장

### 예시

```css
<style>
	/* 전체 선택자 */
	* {
			color: red;
	}

	/* 요소 선택자 */
	h2 {
		color: orange;
	}

	h3, h4 {
		font-size: 10px;
	}

	/* 클래스 선택자 */
	.green {
		color: green;
	}

	/* id 선택자 */
	#purple {
		color: purple;
	}

	/* 자식 결합자 */
	.box > p {
		font-size: 30px;
	}

	/* 자손 결합자 */
	.box p {
		color: blue;
	}
</style>
```

```html
<body>
	<!-- .green 적용됨 -->
	<h1 class="green">SSAFY</h1>
  <!-- 전체 선택자 적용됨 -->
  <h2>선택자 연습</h2>
  <div class="green box">
    box contents
    <!-- green이 적용되는 것은 <div>자체임. 지역 목록은 .box p에 의해 파란색, 서울, 강원, 경기는 전체 선택자에 의해 빨강, 인천은 #purple에 의해 보라색 -->
    <div>
      <p>지역 목록</p>
      <ul>
        <li>서울</li>
        <li id="purple">인천</li>
        <li>강원</li>
        <li>경기</li>
      </ul>
    </div>
    <!-- .box p외에도 box 클래스 바로 하위 레벨의 p이므로 .box > p도 적용됨 -->
    <p>lorem + tab : 랜덤한 문자열 자동 생성!</p>
  </div>
  <!-- 전체 선택자 적용 -->
  <h3>HELLO</h3>
  <h4>CSS</h4>
</body>
```

<img width="482" alt="html_27" src="https://user-images.githubusercontent.com/86648892/183297314-bcbd1322-1f61-413e-b918-e1b2fbc2a888.png">

---

## Selectors 심화

### 결합자(Combinators)

- 자손 결합자
    - 공백
    - selector A 하위의 모든 selector B 요소
- 자식 결합자
    - `>`
    - selector A 바로 아래의 selector B 요소
- 일반 형제 결합자
    - `~`
    - selector A의 형제 요소 중 뒤에 오는 selector B 요소를 모두 선택
- 인접 형제 결합자
    - `+`
    - selector A의 형제 요소 중 바로 뒤에 위치하는 selector B 요소를 선택

<img width="1057" alt="html_28" src="https://user-images.githubusercontent.com/86648892/183297315-cf517923-a9f7-4c0c-8887-d98eea927ba8.png">

<img width="1030" alt="html_29" src="https://user-images.githubusercontent.com/86648892/183297316-80d96606-0033-4877-b25b-f72c4303cbd1.png">

<img width="1036" alt="html_30" src="https://user-images.githubusercontent.com/86648892/183297317-fff0bc59-91cd-4faa-b0a2-2671ae28fa74.png">

---

## CSS 적용 우선순위 (cascading order)

### 범위가 좁을수록 강하다

1. 중요도(importance)
    - `!important`
    - 사용시 주의
2. 우선 순위(specificity)
    - 인라인 > id > class, 속성, pseudo-class > 요소, pseudo-element
3. CSS 파일 로딩 순서

```css
h2 {
	color: darkviolet !imporant;
}

p {
	color: orange;
}

.blue {
	color: blue;
}

.green {
	color: green;
}

#red {
	color: red;
}
```

```html
<body>
  <p>1</p>
  <p class="blue">2</p>
  <p class="blue green">3</p>
  <p class="green blue">4</p>
  <p class="blue" id="red">5</p>
  <h2 class="blue" id="red">6</h2>
  <p class="blue" id="red" style="color: yellow;">7</p>
  <h2 class="blue" id="red" style="color: yellow;">8</h2>
</body>

<!-- 1은 p에 의해 오렌지, 2는 .blue에 의해 파랑 -->
<!-- 3과 4는 모두 초록, 동일한 레벨일 경우 뒤에 오는 것 적용 -->
<!-- 6, 8은 !important 선언에 의해 무조건 보라 -->
<!-- 5는 id 우선 적용으로 빨강, 7은 인라인 우선 적용으로 노랑 -->
```

---

## CSS 상속

- CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속
    - 속성(프로퍼티) 중에는 상속이 되는 것과 되지 않는 것들이 있음
    - 상속되는 것
        - text 관련 요소(font, color, text-align), opacity, visibility 등
    - 상속되지 않는 것
        - 여백, 레이아웃과 관련된 것
        - box model 관련 요소(width, height, margin, padding, border, box-sizing, display)
        - position 관련 요소(position, top/right/bottom/left, z-index) 등
- 상속 여부 MDN에서 확인하기

<img width="1107" alt="html_31" src="https://user-images.githubusercontent.com/86648892/183297319-61534e1e-5323-49d4-ac73-1acd8a1afc79.png">

---

## CSS 기본 스타일

### 크기 단위

- `px`
    - 픽셀
    - 모니터 해상도의 한 화소인 픽셀 기준
    - 픽셀의 크기는 변하지 않기에 고정적인 단위
- `%`
    - 백분율 단위
    - 가변적인 레이아웃에서 자주 사용
- `em`
    - 바로 위 부모 요소의 크기에 대한 상대적인 사이즈 지정
- `rem`
    - `root em`의 약자
    - 최상위 요소(html)에 비한 상대적인 사이즈 지정
    - 기본 브라우저 설정 사이즈 16px
    - html tag의 font-size를 base로 함
    - html tag에 font-size가 정의되지 않았다면, 브라우저 기본 설정을 따라감

### 크기 단위 (viewport)

- 보이는 화면을 기준으로 사이즈가 결정됨
- 웹페이지를 방문한 유저의 디바이스 화면을 기준으로 상대적 사이즈 결정
- `vw`, `vh`, `vmin`, `vmax`
    - `vw`는 가로, `vh`는 세로

<img width="1019" alt="html_32" src="https://user-images.githubusercontent.com/86648892/183297320-de2571cd-6789-46b2-a59d-be3258827e94.png">

<img width="804" alt="html_33" src="https://user-images.githubusercontent.com/86648892/183297322-8df2269c-b8a5-46b5-8dd0-ca2d7310bf01.png">

- `px`는 브라우저의 크기를 변경해도 그대로 고정되어있고
- `vw`는 브라우저 가로를 줄였다 늘였다하면 그에 따라 50%를 차지함

### 색상 단위

- 색상 키워드(`background-color: red;` )
    - 대소문자를 구분하지 않음
    - red, blue, black과 같은 특정 색을 직접 글자로 나타냄
- RGB 색상(`background-color: rgb(0, 255, 0);` )
    - 16진수 표기법 혹은 함수형 표기법을 사용해서 특정 색을 표현하는 방식
    - 16진수 표기법
        - `#000000`
    - 함수형 표기법
        - `rgb(0, 0, 0)`
        - `rgba(0, 0, 0, 0.5)`
        - alpha는 투명도
            - 0~1 값 사용
- HSL 색상(`background-color: hsl(0, 100%, 50%);` )
    - 색상, 채도, 명도를 통해 특정 색을 표현하는 방식

### 문서 표현

- 텍스트
    - 서체(font-family), 서체 스타일(font-style, font-weight 등)
    - 자간(letter-spacing), 단어 간격(word-spacing), 행간(line-height) 등
- 컬러(color), 배경(background-image, background-color)
- 기타 HTML 태그별 스타일링
    - 목록(li), 표(table)

---

## CSS Box model

- 모든 HTML 요소는 박스 모델이고
    - 하나의 박스는 4가지 영역으로 구성
        - margin
            - 테두리 바깥의 외부 여백
            - 배경색 지정 불가
            - `margin: auto;` 는 빈 공간을 알아서 margin으로 줌
        - border
            - 테두리
        - padding
            - 테두리 안쪽의 내부 여백
            - 요소에 적용된 배경색, 이밎는 padding까지 적용
        - content
            - 글이나 이미지 등 요소의 실제 내용
- 좌측 상단에서 시작하여
- 위에서 아래 (block)
- 왼쪽에서 오른쪽 (inline)
- 방향으로 쌓인다
- 그리고 이것을 Normal Flow라 부른다

### margin

<img width="540" alt="html_34" src="https://user-images.githubusercontent.com/86648892/183297323-ccf84b25-f80d-448f-a8bd-fcf5a2ea8011.png">

### margin and padding

<img width="554" alt="html_35" src="https://user-images.githubusercontent.com/86648892/183297324-de8ad5cb-b73a-4c45-8d8f-616258c27bd6.png">

### border

<img width="684" alt="html_36" src="https://user-images.githubusercontent.com/86648892/183297325-22ffbf7a-5ffb-4c26-8307-42c49828e8a1.png">

## shorthand 문법

### margin and padding

- 하나만 쓰면
    - 상하좌우
- 둘 쓰면
    - 상하
        - 좌우
- 셋 쓰면
    - 상
        - 좌우
            - 하
- 넷 쓰면
    - 시계방향

<img width="1145" alt="html_37" src="https://user-images.githubusercontent.com/86648892/183297327-62b5f0e8-4f9b-4967-a299-c618e266ba4d.png">

### border

- 한 줄로 표현 가능

<img width="729" alt="html_38" src="https://user-images.githubusercontent.com/86648892/183297329-78d3cb6a-a4cd-4929-9646-caafa13afbef.png">

### box-sizing

- 기본적으로 모든 요소의 box-sizing은 content-box
    - padding을 제외한 순수 contents 영역만을 box로 지정
- 일반적으로 영역을 볼 때 border까지의 너비를 100px로 보는 것을 원함
    - 그 경우 `box-sizing: border-box;` 로 설정

<img width="1160" alt="html_39" src="https://user-images.githubusercontent.com/86648892/183297330-fe4004cd-43c5-43e8-93f4-387350355449.png">

---

## CSS Display

- Display에 따라 크기와 배치가 달라진다
- 네모로 쌓인 박스들을 디스플레이에 따라 배치
- 레이아웃 관련

### 대표적으로 활용되는 display

- `display: block`
    - 줄 바꿈이 일어나는 요소
    - 화면 크기 전체의 가로 폭을 차지
    - 블록 레벨 요소 안에 인라인 레벨 요소 들어갈 수 있음
- `display: inline`
    - 줄 바꿈이 일어나지 않는 행의 일부 요소
    - content 너비만큼 가로 폭을 차지
    - width, height, margin-top, margin-bottom 지정할 수 없음
    - 상하 여백은 `line-height` 로 지정
        - 좌우 수평 정렬은 부모 블록 요소에서 `text-align: center;` 지정
        - 상하 수평 정렬은 `line-height` 값을 부모 블록 높이의 절반 정도 주면 됨
- `display: inline-block`
    - block과 inline 레벨 요소의 특징을 모두 가짐
        - inline처럼 한 줄에 표시할 수 있고
        - block처럼 width, height, margin 속성을 모두 지정할 수 있음
- `display: none`
    - 해당 요소를 화면에 표시하지 않고, 공간조차 부여되지 않음
    - `visibility: hidden`
        - 마찬가지로 화면 표시는 되지 않으나, 공간은 차지한다는 점에서 다름
        - 나중에 보여줄 일이 있으면 hidden, 그럴 일이 없으면 none을 사용
- [MDN docs display](https://developer.mozilla.org/ko/docs/Web/CSS/display)

### 블록 레벨 요소와 인라인 레벨 요소

- 블록
    - div / ul, ol, li / p / hr / form 등
- 인라인
    - span / a / img / input, label / b, em , i , strong 등

<img width="1045" alt="html_40" src="https://user-images.githubusercontent.com/86648892/183297331-69361cd4-5ba1-4f30-a734-a187f25b28b2.png">

- text-align은 블록 요소에만 적용이 가능

<img width="1025" alt="html_41" src="https://user-images.githubusercontent.com/86648892/183297332-a7e408f1-9637-4a64-84f8-a1705ded71c1.png">

<img width="703" alt="html_42" src="https://user-images.githubusercontent.com/86648892/183297336-47031e63-6082-477f-8ce0-0576e9c5b9d6.png">

- 중간에 흰색 공간은 3이 공간을 차지하고 있는 것

---

## CSS Position

- 레이아웃 관련
- 문서 상 요소의 위치를 지정
- static, relative, absolute, fixed, sticky
- static
    - 모든 태그의 기본 값 (기준 위치)
        - Normal Flow를 따름 (좌측 상단)
        - 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치됨
- 좌표 프로퍼티(top, bottom, left, right)를 사용하여 이동 가능
    - relative
    - absolute
    - fixed
    - sticky
- relative: 상대 위치
    - 자기 자신의 static 위치를 기준으로 이동 (normal flow 유지)
    - 레이아웃에서 요소가 차지하는 공간은 static일 때와 같음
- absolute: 절대 위치
    - 요소를 일반적인 문서 흐름에서 제거 후
        - 레이아웃에 공간을 차지하지 않음 (normal flow에서 벗어남)
    - **static이 아닌** 가장 가까이 있는 부모 요소를 기준으로 이동 (없는 경우 브라우저 화면 기준으로 이동)
- fixed: 고정 위치
    - 요소를 일반적인 문서 흐름에서 제거 후
        - 레이아웃에 공간을 차지하지 않음 (normal flow에서 벗어남)
    - 부모 요소와 관계없이 viewport를 기준으로 이동
        - 스크롤 시에도 항상 같은 곳에 위치
- sticky: 스크롤에 따라 static → fixed로 변경
    - 평소엔 static position
        - 스크롤 위치가 임계점에 이르면 fixed position처럼 박스를 화면에 고정할 수 있음

### 예시

- 형에게 `top: 100px; left: 100px;` 을 적용했을 때 absolute와 relative의 차이는?

<img width="424" alt="html_43" src="https://user-images.githubusercontent.com/86648892/183297338-2c70dc32-e7bd-419d-93c3-0506fbf74918.png">

<img width="1030" alt="html_44" src="https://user-images.githubusercontent.com/86648892/183297341-56792d67-2f8b-48f8-9936-6b6be8b245c7.png">

<img width="993" alt="html_45" src="https://user-images.githubusercontent.com/86648892/183297342-cc3fb217-d4ca-4d2a-ad7b-1a590f7c490e.png">

---

## CSS 원칙 정리

- CSS 원칙
    - I : Normal Flow
        - 모든 요소는 박스 모델이고, 좌측상단에 배치
    - II: Display
        - display에 따라 크기와 배치 변경
    - III: Position
        - position에 따라 위치의 기준을 변경
            - relative: 본인의 원래 위치
            - absolute: 특정 부모의 위치
            - fixed: 화면의 위치
            - sticky: 기본적으로 static이지만 스크롤 이동에 따라 fixed로 변경

---

# 추가 정리

### HTML

- HTML 기본 구조를 채워주지 않으면 브라우저가 필요한 부분을 알아서 채워줬음을 알 수 있다
- ‘!’ + tab
    - html 기본 구조 자동완성
- `<meta>` 태그
    - 갖고 있는 데이터에 대한 데이터를 메타데이터라 한다
    - 썸네일같은 것들 작성할 때 사용
- favicon은 웹 브라우저 탭에 작게 들어가있는 아이콘
- HTML 속성
    - 태그 안에 있는 속성명과 속성값
    - id와 class의 역할은 하나의 태그를 지정하는 위한 역할
        - 클래스는 공통된 여러 개의 요소에 어떤 것을 적용할 때 클래스를 부여
            - html 여러군데에 한 번에 적용
        - id는 문서 전체에서 한 개의 고유한 요소를 지정하고 싶을 때 부여
        - 이 룰은 어겨도 되지만 일종의 국룰
    - `data-*`
        - 내가 잠깐 표시하고 싶은 데이터를 저장해놓고 싶을 때
        - Vue.js
- 시맨틱 태그는 필드마다 잘 쓰는 곳이 있고 안 쓰는 곳도 있다
- 검색 엔진 최적화(SEO)
    - 구글의 경우 내부적으로 검색 엔진 봇들이 있음
        - 시맨틱 태그를 통한 마크업의 효과적인 활용은 봇들이 html 파일들을 탐색할 때 효율을 올림
- DOM 트리
    - 중요함
    - 트리는 계층구조를 갖는 자료구조
    - html 태그를 통해 구조를 짜기는 하지만 사실상 그냥 텍스트 파일임
        - 브라우저는 이러한 html 문서를 렌더링하려면 구조를 잡아야 함
        - 선택자를 통해 바꿔줄 수 있는 이유는 브라우저가 DOM 트리를 통해 구조를 기억하고 있기 때문

### HTML 문서 구조화

- 인라인 요소는 딱 그 자리만 차지하는 요소
- 블록 요소는 한 줄을 전부 차지하는 요소
- `<form>` 태그는 사용자로부터 데이터, 인풋을 받기 위한 용도
    - 사용자가 데이터를 서버로 보내는 것이기에 server side와 매우 밀접한 연관이 있다
    - 안에 내용으로 label, input 태그가 쌍으로 들어간다
        - 여러 쌍이 들어갈 수 있음
    - `<label>`
        - label의 `for`와 input의 `id`속성을 일치시켜줘야 함
    - `<input>`
        - name과 value라는 속성을 가짐
        - 웹 브라우저는 type에 정해진 내용을 보고 그에 맞는 형식으로 보여줌
            - html widget이라 검색하면 확인할 수 있음
        - name은 브라우저 입장에서 받는 데이터에 대한 이름
        - required는 입력하지 않으면 못 넘어가는 속성
        - autofocus는 페이지에 들어가자마자 input 들어가는 곳에 커서를 깜빡이게 할 수 있음
        - 유효성 검사는 값이 원하는 형식에 맞는건지 검사하는 것
            - 1차적으로 브라우저에서 검사, 그 다음 프론트엔드 부분에서 검사, 서버에서도 검사
- 서버 요청
    - domain name과 action이 합쳐진 url에 해당하는 서버로 요청이 간다
    - query string에 정보를 담아서 요청하는 것은 GET만 그렇게 한다
        - POST는 안에 내용을 넣어서 보냄
            - 민감정보는 그래서 POST로 요청함

## CSS

- DOM 트리 구조에 따라 상위에 있는 스타일이 폭포처럼 흘러내린다해서 cascading
- 결국 2 steps
    - 선택하고
    - 스타일을 지정한다
- 세미 콜론(;)으로 스타일 속성 구분
- 내부 참조는 html 파일이 길어져서 잘 쓰지 않는다

### CSS Selectors

- 선택자 유형은 기본 선택자와 결합자 수준에서 거의 끝난다
    - 속성 선택자는 `button[type = “submit”] {}` 과 같이 선언할 수 있음
    - 결합자는 공백, ‘>’, ‘+’, ‘~’ 4가지 가 있다
        - 인접 형제 결합자(+)
            - A + B
                - A의 바로 다음이면서 B인 것에 적용
        - 일반 형제 결합자(~)
            - A ~ B
                - A 다음에 오는 형제들 중에서 B를 만족하는 것에 적용
        - 자식 결합자(>)
            - A > B
                - A의 바로 하위 레벨(자식)에 있으면서 B를 만족하는 것에 적용
        - 자손 결합자(공백)
            - A B
                - A의 하위에 있는 레벨(자손)에 있으면서 B를 만족하는 것에 적용
- !important는 css layer가 깊은데 잠깐 띄워야 할 중요한 사항같은 것들 외엔 남발하지 말자
- 개발자 도구의 Styles에 strikethrough가 되어 있는 것은 이런이런 것들이 적용되었는데 그보다 우선순위인 것이 적용된 것이다라는 뜻
- CSS 상속은 자동으로 일어나며 text 관련 요소는 상속, box model 관련 요소는 상속되지 않는다 정도로 생각하자
- 크기 단위에서 em과 rem의 차이는 em은 상속의 영향을 받고, rem은 상속의 영향을 받지 않음
    - rem은 최상위 요소(html)의 사이즈를 기준으로 배수 단위를 가짐
    - 최상위 요소도 `html {}` 과 같이 스타일 지정 가능

### CSS 기본 스타일

- 1vw와 1vh
    - 현재 보고 있는 화면(viewport)의 100분의 1
    - vmin과 vmax는 최대와 최소를 정해주는 것
        - 마찬가지로 100분의 1 단위
        - 항상 내가 보는 화면의 꽉 차는 정사각형?
        
        ```html
        <style>
        .box {
        	height: 100vmin;
        	width: 100vmin:
        </style>
        ```
        
- RGB 색상의 경우 마지막에 투명도 추가 가능

### CSS Box Model

- 웹에서 보고 있는 모든 것은 박스 모델
- 왼쪽 상단에서부터 정렬됨
    - 이것을 Normal Flow라고 함
- 박스 모델을 크게 하는 것과 padding이나 margin을 더 주는 것과는 같게 보일 수도 있으나 엄연히 다르다
- 백그라운드 영역은 padding까지
- box model shorthand 문법
    - `.margin-1 {margin: 10px;}`
        - 전부
    - `.margin-2 {margin: 10px 20px;}`
        - 상하, 좌우
    - `.margin-3 {margin: 10px 20px 30px;}`
        - 나누기 모양
    - `.margin-4 {margin: 10px 20px 30px 40px;}`
        - 시계 방향
- content-box와 border-box 만들면서 비교해볼 것
- box-sizing은 기본적으로 content-box
    - border-box로 하고 싶다면 따로 설정

### CSS Display

- 대표적인 블록 레벨 요소
    - div, p, hr, form
- 대표적인 인라인 레벨 요소
    - span, a, img, input, label, i
- `display: block`, `display: inline` 에 해당하는 각 레벨 요소들은 default로 이 값이 설정되어 있지만, 이 명령을 따로 줄 경우 block처럼 혹은 inline 요소처럼 취급할 수 있음
- `display: none`은 코드에는 있는데, element에 생성도 안됨
    - `visibility: hidden`은 DOM 트리 내부 element에 생성은 되어 공간은 차지하지만, 보이지는 않는 것

### CSS Position

- mdn position으로 확인해보자
- static
    - 기본값
    - normal flow를 따른다는 것
- relative
    - 원래 자리를 차지하고 있고, 그 자리를 기준으로 옮겨간 것
- absolute
    - 부모 요소의 왼쪽 상단을 기준으로 옮겨간 것
    - 원래 자리에선 사라짐 (붕 뜬 느낌)
    - 누가 앞에 오고 뒤로 갈지는 z-index를 활용
    - 부모 중 static이 아닌 것을 기준
        - 부모에 relative를 주지 않으면 브라우저를 기준으로 움직임
- sticky
    - 처음 내가 생성된 위치를 기준으로 해서 화면상에 그대로 stick!

---

# 목차

- CSS Layout
    - float
    - flexbox
    - grid
- bootstrap
    - bootstrap grid system
- Responsive web

---

# CSS Layout

## CSS Layout Techniques

- Display
- Position
- Float (1996)
- Flexbox (2012)
- Grid (2017)
- 기타
    - Responsive Web Design (2010), Media Queries (2012)

---

# Float

- 박스를 왼쪽 혹은 오른쪽으로 이동시켜 텍스트를 포함한 인라인 요소들이 주변을 wrapping하도록 함
- 그 주변을 물 흐르듯이 감싸라는 것
- 요소가 Normal flow를 벗어나도록 함

## Float 속성

- none: 기본값
- left: 요소를 왼쪽으로 띄움
- right: 요소를 오른쪽으로 띄움

<img width="579" alt="html_46" src="https://user-images.githubusercontent.com/86648892/183298287-57c2a123-31eb-4b2c-874d-93f8870c818d.png">

<img width="474" alt="html_47" src="https://user-images.githubusercontent.com/86648892/183298291-96b28ff9-8bc3-4a09-a27d-f93e31f85d7d.png">

---

# Flexbox

- 행과 열 형태로 아이템들을 배치하는 1차원 레이아웃 모델
    - z-index는 차원 간 배치
- display 속성으로 flex를 선언한다는 것은 ‘이제부터 난 축을 기준으로 배치할거야'라는 선언
- 축
    - main axis
        - 기본 direction은 가로(row)
    - cross axis
- Why Flexbox?
    - 이전까지 Normal Flow를 벗어나는 수단은 Float 혹은 Position
    - 수동값 부여없이 수직정렬이나 아이템 간 간격 등을 동일하게 배치하는 것이 어려웠음

## Flexbox 구성 요소

- Flex Container (부모 요소)
    - 부모 요소에 flex를 적용함!
    - flex item들이 놓여있는 영역
    - display 속성을 flex 혹은 inline-flex로 지정
- Flex Item (자식 요소)
    - 컨테이너에 속해있는 컨텐츠(박스)
- `display:flex`
    - flex-container에서 선언
    - 이 객체가 flex-container라 선언하는 것이고
        - 그 바로 아래 레벨이 flex items가 된다
- `display: inline flex`
    - 인라인과 블록의 차이처럼 요소의 테두리가 줄어듬
    - 인라인처럼 사용할 수 있고, 내용물의 크기만큼만 차지

## Flex 속성

- 배치 설정
    - flex-direction
    - flex-wrap
- 공간 나누기
    - justify-content (main axis)
    - align-content (cross axis)
- 정렬
    - align-items (모든 아이템을 cross axis 기준으로)
    - align-self (개별 아이템)

## Flex 속성: flex-direction

- `flex-direction`
    - 요소를 배치할 방향
        - row
        - row-reverse
        - column
        - column-reverse
- 역방향의 경우 HTML 태그 선언 순서와 시각적으로 다르니 유의 (웹 접근성에 영향)

<img width="1205" alt="html_48" src="https://user-images.githubusercontent.com/86648892/183298292-b0952e0f-80f4-41c4-a2e9-c6a1608e232c.png">

## Flex 속성: flex-wrap

- `flex-wrap`
    - 아이템이 컨테이너를 벗어나는 경우의 설정
        - wrap
        - nowrap
            - 기본값
        - wrap-reverse
            - 최신글이 위에 오도록 하고싶을 때와 같은 경우에 사용
            
            <img width="755" alt="html_49" src="https://user-images.githubusercontent.com/86648892/183298295-e837be2d-ca62-4683-94a6-cb021f079c2a.png">
            

## Flex 속성: flex-flow (direction + wrap)

- `flex-flow: row nowrap;`
- direction과 wrap 속성의 shorthand
    - flex-direction과 flex-wrap에 대한 설정을 차례로 작성

## Flex 속성: justify-content

- Main axis를 기준으로 공간 배분

<img width="1173" alt="html_50" src="https://user-images.githubusercontent.com/86648892/183298296-3d0ae692-b0cb-4f89-817e-16405fb589cd.png">

## Flex 속성: align-content

- Cross axis를 기준으로 공간 배분 (아이템이 한 줄로 배치되는 경우 확인할 수 없음)

<img width="999" alt="html_51" src="https://user-images.githubusercontent.com/86648892/183298297-cd548a61-82d5-45f1-8f30-a6d5e5a1508c.png">

## Flex 속성: justify-content & align-content

- 공간 배분
    - flex-start
        - 기본값
        - 아이템들을 axis 시작점으로
    - flex-end
        - 아이템들을 axis 끝 쪽으로
    - center
        - 아이템들을 axis 중앙으로
    - space-between
        - 아이템 사이의 간격을 균일하게 분배
    - space-around
        - 아이템을 둘러싼 영역을 균일하게 분배
    - space-evenly
        - 전체 영역에서 아이템 간 간격을 균일하게 분배

## Flex 속성: align-items

- 모든 아이템을 Cross axis 기준으로 정렬

<img width="1152" alt="html_52" src="https://user-images.githubusercontent.com/86648892/183298298-68296744-f7cb-4fb2-9467-3fe6584927ad.png">

## Flex 속성: align-self

- 개별 아이템을 Cross axis 기준으로 정렬
- 주의! 해당 속성은 컨테이너에 적용하는 것이 아니라 개별 아이템에 적용하는 것

<img width="1172" alt="html_53" src="https://user-images.githubusercontent.com/86648892/183298300-91a2f43f-a0b0-45ba-bd70-812abe8fa8c7.png">

## Flex 속성: align-items & align-self

- Cross axis를 중심으로
    - stretch
        - 기본값
        - 컨테이너를 가득 채움
    - flex-start
        - 위
    - flex-end
        - 아래
    - center
        - 가운데
    - baseline
        - 텍스트 baseline에 기준선을 맞춤

## Flex 기타 속성

- flex-grow
    - 남은 영역을 아이템에 분배
- order
    - 배치 순서
    - 각자의 기본값은 0
    - 그러므로 왼쪽으로 보내고 싶다면 음수의 절댓값이 큰 것이 가장 왼쪽
    - 오른쪽으로 보내고 싶다면 1부터 시작하여 절댓값이 큰 것이 가장 오른쪽

<img width="810" alt="html_54" src="https://user-images.githubusercontent.com/86648892/183298301-47bda5d5-7327-4b45-9c05-5f92a0a4fa36.png">

## Flexbox 활용

### 수직 수평 가운데 정렬

<img width="831" alt="html_55" src="https://user-images.githubusercontent.com/86648892/183298302-e1a802df-9b6c-4c55-bd41-80a3f95b3c91.png">

### 카드 배치

<img width="940" alt="html_56" src="https://user-images.githubusercontent.com/86648892/183298304-ecce7748-2da6-401c-9083-66d04f478adc.png">

---

# Bootstrap

- 정형화된 css 컨텐츠를 편리하게 사용할 수 있도록 모아놓은 것
    - 쉽게 말해 css 코드 덩어리다
- Quickly design and customize
    - UI를 빠르게 빌드할 수 있다
- Responsive
    - 반응형 웹을 편리하게 구현할 수 있다
- Grid System
    - 그리드 시스템의 핵심은 화면을 12칸으로 보고 어떤 식으로 분할할지 선택하는 것
- Prebuilt Components
    - 다양한 component 사용 가능

## CDN via jsDelivr

- Content Delivery(Distribution) Network
    - 컨텐츠(CSS, JS, Image, Text 등)을 효율적으로 전달하기 위해 여러 노드에 가진 네트워크에 데이터를 제공하는 시스템
        - 개별 end-user의 가까운 서버를 통해 빠르게 전달 가능
        - 외부 서버를 활용함으로써 본인 서버의 부하가 적어짐
- import와 비슷한 개념
- CDN via jsDelivr
    - link는 `</head>` 앞에
    - script는 `</body>` 앞에
        - 코드의 실행 속도를 위해

---

# Bootstrap의 기본 원리

## Spacing (margin and padding)

- css는 부트스트랩 개발자들이 만들어놓았기에 클래스 지정만 하면됨
- mt-3
    - m은 property, t는 sides, 3은 size

<img width="749" alt="html_57" src="https://user-images.githubusercontent.com/86648892/183298305-d8649a14-b78f-4709-a4bc-06759f2e0224.png">

<img width="994" alt="html_58" src="https://user-images.githubusercontent.com/86648892/183298308-87707fb6-f813-42b6-a7d8-bd75de7fa254.png">

<img width="919" alt="html_59" src="https://user-images.githubusercontent.com/86648892/183298309-77fcd87b-eb8e-423c-b454-c7c594b39045.png">

- 1은 0.25rem
    - 1rem은 16px
    - rem의 장점은 html 기준으로 바로 적용 가능
    - mx-0
        - 가로 margin을 0으로
    - mx-auto
        - 가로 가운데 정렬
    - py-0
        - 위아래 padding을 0으로

<img width="1083" alt="html_60" src="https://user-images.githubusercontent.com/86648892/183298310-977fde4a-c644-4077-9d6d-7eccd12b8f97.png">

<img width="809" alt="html_61" src="https://user-images.githubusercontent.com/86648892/183298311-13101685-1bf4-4f40-a208-34ddce99c95d.png">

## Color

- 텍스트 컬러, 백그라운드 컬러 모두 적용 가능

<img width="1056" alt="html_62" src="https://user-images.githubusercontent.com/86648892/183298312-215eee19-d84d-4186-8f38-de1f676590ef.png">

<img width="1084" alt="html_63" src="https://user-images.githubusercontent.com/86648892/183298313-087004bb-ba89-49ad-a4af-5cc01f266550.png">

## Text

<img width="850" alt="html_64" src="https://user-images.githubusercontent.com/86648892/183298316-12b6904b-7dd9-4808-8a23-7664c5236e23.png">

## Display

<img width="1095" alt="html_65" src="https://user-images.githubusercontent.com/86648892/183298317-8750b7fc-33c8-428a-a8b2-c8ba407bd5c2.png">

- `d-`
    - `d-inline` 은 inline으로 취급하겠다는 것
    - `d-block` 은 block으로 취급하겠다는 것
    - `d-none`은 코드는 있는데 보이지 않음
        - `d-sm-none d-md-block`
            - 반응형
            - grid system 기준 sm까지는 보이지 않다가 md부터 보임
        - `d-sm-none`
            - 반응형
            - grid system 기준 md까지 보이지 않다가 xl부터 보임

## Position

<img width="589" alt="html_66" src="https://user-images.githubusercontent.com/86648892/183298318-4a824fc0-869f-4381-82b7-df2df617c53b.png">

---

## Bootstrap Components

### Components

- Bootstrap의 다양한 UI 요소를 활용할 수 있음
- 기본 제공된 Components를 변환해서 활용

### Button

- 클릭했을 때 어떤 동작이 일어나도록 하는 요소

<img width="962" alt="html_67" src="https://user-images.githubusercontent.com/86648892/183298319-241cbd9a-95ce-4f0c-9f7f-d0a3f7bb6581.png">

### Dropdowns

- dropdown, dropdown-menu, dropdown-item 클래스를 활요해 옵션 메뉴를 만들 수 있음

<img width="950" alt="html_68" src="https://user-images.githubusercontent.com/86648892/183298320-2c307d76-878f-43bf-9c5c-59a8733c18f6.png">

<img width="1228" alt="html_69" src="https://user-images.githubusercontent.com/86648892/183298323-4233bba7-fa00-409d-8c7a-0ead9f9ab509.png">

### Forms > Form controls

- form-control 클래스를 사용해 <input> 및 <form> 태그를 스타일링할 수 있음

<img width="1046" alt="html_70" src="https://user-images.githubusercontent.com/86648892/183298325-fc4b27ff-b752-4214-8ee6-d0abb6b98e1b.png">

<img width="1176" alt="html_71" src="https://user-images.githubusercontent.com/86648892/183298326-3ae44e94-c54b-4789-b924-8e1889307f77.png">

### Navbar

- navbar 클래스를 활용하면 네비게이션 바를 제작할 수 있음

<img width="1059" alt="html_72" src="https://user-images.githubusercontent.com/86648892/183298328-2d72cf1d-bcd2-4c9d-a9c5-bf2e72048853.png">

<img width="1162" alt="html_73" src="https://user-images.githubusercontent.com/86648892/183298329-745b35c9-e43f-4c1f-a534-0ba6cea93dff.png">

### Carousel

- 콘텐츠(사진)를 순환시키기 위한 슬라이드쇼

<img width="1122" alt="html_74" src="https://user-images.githubusercontent.com/86648892/183298330-305329e6-5dda-40f6-ac3a-f43fe1922f00.png">

### Modal

- 사용자와 상호작용하기 위해 사용하며, 긴급 상황을 알리는데 주로 사용
- 현재 열려있는 페이지 위에 또 다른 레이어를 띄움
- 페이지를 이동하면 자연스럽게 사라짐
    - 팝업은 보통 x를 눌러야 사라지고, modal은 다른 곳을 클릭해도 사라짐
- data-bs-target에 다른 곳에 지정해준 객체의 id를 넣어주어 연결
- 중첩해서 들어가있으면 안됨
    - Modals use `position: fixed`, which can sometimes be a bit particular about its rendering. Whenever possible, place your modal HTML in a top-level position to avoid potential interference from other elements. You’ll likely run into issues when nesting a `.modal` within another fixed element

<img width="1109" alt="html_75" src="https://user-images.githubusercontent.com/86648892/183298331-7bd64685-d208-4249-86b9-82af4762a8dc.png">

<img width="1006" alt="html_76" src="https://user-images.githubusercontent.com/86648892/183298332-44c98ff5-1e8e-4e43-91f1-369b34c466df.png">

### Flexbox in Bootstrap

<img width="647" alt="html_77" src="https://user-images.githubusercontent.com/86648892/183298334-697e30db-3c22-4409-9bd5-caffd1ff225d.png">

### Grid Card

<img width="826" alt="html_78" src="https://user-images.githubusercontent.com/86648892/183298335-b9a472ee-e2c5-44c3-966e-47d0000c7ff6.png">

<img width="1122" alt="html_79" src="https://user-images.githubusercontent.com/86648892/183298337-59517f61-2033-4f01-91a4-09cd09ce6e5c.png">

- 반응형은 `<div *class*="row row-cols-1 row-cols-md-3 g-4">` 덕분에 이루어짐
    - g-4는 gutter를 뜻함
    - 이 div는 grid system상 row에 해당하는데 md이상이 아닌 경우에는 1개의 column을, md이상인 경우 3개의 column을 나타내겠다는 것

### Responsive Web Design

- 다양한 화면 크기를 가진 디바이스들이 등장함에 따라 responsive web design 개념이 등장
- 반응형 웹은 별도의 기술 이름이 아닌 웹 디자인에 대한 접근 방식, 반응형 레이아웃 작성에 도움이 되는 사례들의 모음 등을 기술하는데 사용되는 용어
- 예시
    - Media Queries, Flexbox, Bootstrap Grid System, The viewport meta tag

---

# Bootstrap Grid System

## Grid System

- 요소들의 디자인 및 배치에 도움을 주는 시스템
- 기본 요소
    - Column: 실제 컨텐츠를 포함하는 부분
    - Gutter: 칼럼과 칼럼 사이의 공간 (사이 간격)
    - Container: Column들을 담고 있는 공간

## Bootstrap Grid System

- Bootstrap Grid system은 flexbox로 제작됨
- container, rows, columns로 컨텐츠를 배치하고 정렬
- 반드시 기억할 것
    - 12개의 column
    - 6개의 grid breakpoints

<img width="459" alt="html_80" src="https://user-images.githubusercontent.com/86648892/183298338-4cfbe979-6d06-462d-a520-8c5891c3acca.png">

## Grid system breakpoints

<img width="754" alt="html_81" src="https://user-images.githubusercontent.com/86648892/183298339-9c2a2680-e63e-444c-b219-1ca9836e11a4.png">

<img width="819" alt="html_82" src="https://user-images.githubusercontent.com/86648892/183298340-7be12875-60d6-439b-8e62-2c000f38d879.png">

<img width="1092" alt="html_83" src="https://user-images.githubusercontent.com/86648892/183298341-0efa1414-d8d8-4d77-9a38-bd60143d77d4.png">

<img width="779" alt="html_84" src="https://user-images.githubusercontent.com/86648892/183298342-d142f7ad-644c-4a76-a76d-673c1fd38f6e.png">

<img width="1054" alt="html_85" src="https://user-images.githubusercontent.com/86648892/183298344-faef7e36-66ce-4123-ad19-e59e86499703.png">

<img width="767" alt="html_86" src="https://user-images.githubusercontent.com/86648892/183298345-8bf23303-8f57-4e46-8cbd-6f14e50b72fe.png">

<img width="1089" alt="html_87" src="https://user-images.githubusercontent.com/86648892/183298346-9f162998-d6a2-4678-b565-9c2c8a6ddfad.png">

<img width="832" alt="html_88" src="https://user-images.githubusercontent.com/86648892/183298348-04d636e1-ebdf-4561-a9b6-60dd451a9ace.png">

<img width="1072" alt="html_89" src="https://user-images.githubusercontent.com/86648892/183298350-5bc7b8fd-8500-47c6-8676-2159c34ce904.png">

- div w-100은 텅빈 width 100짜리이므로 줄바꿈의 한 방법
    - 그냥 row 구획을 하나 더 만들어주는게 좋다
- 원하는 비율을 col-숫자로 넣어준다
- 1짜리 13개면 1개가 다음 줄로 넘어간다
    - 12칸이 넘어가는 순간의 객체는 줄바꿈이 되어 넘어감
- offset은 비우고싶을 때 사용
    - `offset-`
    - 왼쪽에 offset을 줌

<img width="995" alt="html_90" src="https://user-images.githubusercontent.com/86648892/183298351-f1aa3398-d051-4af1-bb45-4c16df584438.png">

<img width="704" alt="html_91" src="https://user-images.githubusercontent.com/86648892/183298352-de2aa2f8-78e7-481d-bbc2-8565dcccf740.png">

<img width="783" alt="html_92" src="https://user-images.githubusercontent.com/86648892/183298354-4c89294b-4c42-46b9-9523-e143b2ff7904.png">

<img width="769" alt="html_93" src="https://user-images.githubusercontent.com/86648892/183298355-2311d9bf-aea7-489f-bfcd-a9bb79ff5bd3.png">

---

# 추가 정리

- 레이아웃을 따로 지정하지 않으면 normal flow로 인라인 요소는 좌에서 우로, 블록 요소는 위에서 아래로 배치
- html의 모든 요소는 box model
    - 4가지 영역으로 구성됨
        - content
        - padding
        - border
        - margin
- Display
    - inline, block, none 3가지
    - inline
        - div, form, header, footer 등
    - block
        - a, span 등
    - none
        - display none은 DOM 트리에조차 생성되지 않는 것
        - visibility hidden은 자리는 차지하고 있으나 보이지 않는 것
- padding이 box의 크기에 영향을 주는 경우 box-sizing을 border box로 설정
- margin 한 줄로 표현
    - `margin 0 auto;` 는 위아래 0, 양옆 마진은 알아서 잘 배분
        - 블록 수평 정렬
    - `width ;` 를 화면보다 크게 주면 가로 스크롤이 생김
        - `max-width ;` 로 하면 최대크기 이상으로 가지 않고, 화면이 작아지면 그에 따라 반응형으로 너비 줄어듬
- 블록 안에 인라인 요소를 수평 정렬하고 싶다면 해당 블록의 속성 중 `text-align` 에 center 부여
- DRY에 따라 공통적인 부분이 보인다면 class로 묶어주자
- 아래로 이동
    - 위 마진 부여
    - `position: relative;` `top: ;`
- 수직 정렬을 위해서 `line-height: ;` 속성 사용 가능
- margin이 겹칠 경우 값이 더 큰 것을 줌

---

### box를 통한 positioning 연습

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <link rel="stylesheet" href="box_style.css">
</head>
<body>
  <div id="box-01" class="box"></div>
  <div id="box-02" class="box"></div>
  <div id="box-03" class="box">
    <button>inline elem</button>
  </div>
  <div id="box-04" class="box">
    <div id="box-05" class="box"></div>
  </div>
</body>
</html>
```

```css
.box {
  width: 300px;
  height: 200px;
  border: 2px solid black;
  box-sizing: border-box;
  margin: 10px auto;
}

#box-01 {
  background-color: rgba(131, 211, 184, 80%);
}

#box-02 {
  background-color: rgba(253, 247 ,163, 0.8);
}

#box-03 {
  text-align: center;
  line-height: 12;
}

#box-04 {
  background-color: rgb(255, 218, 252);
}

#box-05 {
  position: relative;
  top: 50px;
  width: 100px;
  height: 100px;
  background-color: rgb(255, 192, 192);
}
```

<img width="1062" alt="html_94" src="https://user-images.githubusercontent.com/86648892/183298357-04168023-7b45-49b5-9ff2-8517686180b7.png">

---

## web page practice

<img width="1089" alt="html_95" src="https://user-images.githubusercontent.com/86648892/183300044-d27bacf1-7115-4e3d-a16a-8a5d077e8f4e.png">
<img width="950" alt="html_96" src="https://user-images.githubusercontent.com/86648892/183300050-f763570d-f00f-4037-a220-a74a19c2ee31.png">
<img width="1085" alt="html_97" src="https://user-images.githubusercontent.com/86648892/183300053-01d653c9-b54f-4626-8505-d1be52097bce.png">
<img width="1113" alt="html_98" src="https://user-images.githubusercontent.com/86648892/183300055-adf053c1-87c2-41de-b935-5b3a537704d2.png">
<img width="1141" alt="html_99" src="https://user-images.githubusercontent.com/86648892/183300057-0069da65-052b-4811-9cc0-ff52fa84ffc5.png">
<img width="1182" alt="html_100" src="https://user-images.githubusercontent.com/86648892/183300059-4eecc7e7-b2c6-40b1-9cdb-a3110f15ee8c.png">
<img width="1148" alt="html_101" src="https://user-images.githubusercontent.com/86648892/183300060-2b9e5b33-c951-49fe-9dd9-ae52c55f1c83.png">
<img width="853" alt="html_102" src="https://user-images.githubusercontent.com/86648892/183300062-2efff550-0c2d-451d-992a-a3e1da073aa2.png">
<img width="1116" alt="html_103" src="https://user-images.githubusercontent.com/86648892/183300065-9f56db52-3003-4d7d-a322-a580f1748262.png">
<img width="1150" alt="html_104" src="https://user-images.githubusercontent.com/86648892/183300067-36eb6cd1-ffe2-4b5e-95a6-b736921d7c53.png">
<img width="1136" alt="html_105" src="https://user-images.githubusercontent.com/86648892/183300072-a9ba4025-bcf4-4369-a469-231dbb935965.png">

---

## nth-child와 nth-of-type

### 1) 아래의 코드를 작성하고 결과를 확인하시오.
```html
<html>
    <head>
        <title>0801 workshop</title>
        <style>
            #ssafy > p:nth-child(2) {
                color: red;
            }
        </style>
    </head>
    <body>
        <div id="ssafy">
            <h2>어떻게 선택 될까?</h2>
            <p>첫번째 단락</p>
            <p>두번째 단락</p>
            <p>세번째 단락</p>
            <p>네번째 단락</p>
        </div>
    </body>
</html>
```
첫번째 단락만 빨갛게 표시됨
### 2) nth-child를 nth-of-type으로 변경하고 결과를 확인하시오.
```html
<html>
    <head>
        <title>0801 workshop</title>
        <style>
            #ssafy > p:nth-of-type(2) {
                color: red;
            }
        </style>
    </head>
    <body>
        <div id="ssafy">
            <h2>어떻게 선택 될까?</h2>
            <p>첫번째 단락</p>
            <p>두번째 단락</p>
            <p>세번째 단락</p>
            <p>네번째 단락</p>
        </div>
    </body>
</html>
```
두번째 단락만 빨갛게 표시됨
### 3) 작성한 코드를 참고하여 nth-child()와 nth-of-type()의 차이점을 작성하시오.
nth-child()는 자식 요소 중 유형을 고려하지 않은 것이며, nth-of-type()은 자식 요소 중 유형을 고려한 순서를 뜻한다. `#ssafy > p:nth-child(2)`는 ssafy라는 id를 가진 태그의 두번째 자식이 p태그이면 해당 태그에 정의된 css를 적용해달라는 것이다. 만약 두번째 자식이 p태그가 아니라면 해당 css는 적용되지 않는다. 반면 `#ssafy > p:nth-of-type(2)`는 ssafy라는 id를 가진 태그의 자식들 중 두번째로 나오는 p태그에 해당 css를 적용해달라는 것이다.

---
## Bootstrap Components 예제 코드 (Button, Navbar, Pagination 만들기)

### 1.Button 만들기 

##### (a) btn 

##### (b) btn-primary

```html
<button type="submit" class="btn btn-primary" width="40rem;">Submit</button>
```



### 2. NavBar 만들기

##### (a) `light`

##### (b) `navbar-nav`

##### (c) `navbarBreakfast`

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <!-- CSS only -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous">
  <!-- JavaScript Bundle with Popper -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-pprn3073KE6tl6bjs2QrFaJGz5/SUsLqktiwsUTF55Jfv3qYSDhgCecCxMW52nD2" crossorigin="anonymous"></script>
  <title>Document</title>
</head>
<body>
	<nav class="navbar navbar-expand-lg navbar-light bg-light">
		<div class="container-fluid">
			<a class="navbar-brand" href="#">
	      <img src="my_ssafy.png" alt="ssafy" width="70" height="30" class="d-inline-block align-top">
	    </a>
	    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDarkDropdown" 
				aria-controls="navbarNavDarkDropdown" aria-expanded="false" aria-label="Toggle navigation">
	    <span class="navbar-toggler-icon"></span>
		 </button>
			<div class="collapse navbar-collapse" id="navbarNavDropdown">
				<ul class="navbar-nav">
	        <li class="nav-item dropdown">
						<a class="nav-link dropdown-toggle" href="#" id="navbarBreakfast" role="button" data-bs-toggle="dropdown" 
							aria-expanded="false">아침
						</a>
						<ul class="dropdown-menu dropdown-menu-light" aria-labelledby="navbarBreakfast">
							<li><a class="dropdown-item" href="#">오믈렛</a></li>
							<li><a class="dropdown-item" href="#">샌드위치</a></li>
							<li><a class="dropdown-item" href="#">팬케이크</a></li>
							<li><a class="dropdown-item" href="#">김밥</a></li>
							<li><a class="dropdown-item" href="#">주먹밥</a></li>
						</ul>
					</li>
					<li class="nav-item dropdown">
						<a class="nav-link dropdown-toggle" href="#" id="navbarLunch" role="button" data-bs-toggle="dropdown" 
							aria-expanded="false">점심 
						</a>
						<ul class="dropdown-menu dropdown-menu-light" aria-labelledby="navbarLunch">
							<li><a class="dropdown-item" href="#">샐러드</a></li>
							<li><a class="dropdown-item" href="#">떡볶이</a></li>
								<li><a class="dropdown-item" href="#">햄버거</a></li>
						</ul>
					</li>
					<li class="nav-item">
						<a class="nav-link active" href="#">저녁</a>
					</li>
					<li class="nav-item">
						<a class="nav-link disable" href="#">야식</a>
					</li>
				</ul>
			</div>
		</div>
	</nav>
</body>
</html>
```



### 3. PageNation 만들기

##### (a) - `pagination`

##### (b) - `disabled`

##### (c) - `active`

```html
<nav aria-label="...">
      <ul class="pagination">
          <li class="page-item disabled">
              <a class="page-link" href="#" tabindex="-1" aria-disabled="true">Prev</a>
          </li>
          <li class="page-item active" aria-current="page">
              <a class="page-link" href="#">1</a>
          </li>
          <li class="page-item"><a class="page-link" href="#">2</a></li>
          <li class="page-item"><a class="page-link" href="#">3</a></li>
          <li class="page-item">
              <a class="page-link" href="#">Next</a>
          </li>
      </ul>
  </nav>
```

---

## Web Page Build Practice
<img width="1897" alt="html_106" src="https://user-images.githubusercontent.com/86648892/183303666-a5ac2acc-81d2-4dbc-a026-d465e9358642.png">
<img width="1897" alt="html_107" src="https://user-images.githubusercontent.com/86648892/183303672-37a48639-267a-43f0-8881-c0d4ca6bd025.png">

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="style.css">
  <title>Document</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
</head>
<body>
  <!-- 1. Nav -->
  <nav class="d-flex fixed-top justify-content-between align-items-center bg-dark">
    <a href="#">
      <img src="images/logo.png" alt="Logo Image">
    </a>
    <div>
      <a href="#" class="text-decoration-none text-white me-2">Home</a>
      <a href="#" class="text-decoration-none text-white me-2">Community</a>
      <a href="#" class="text-decoration-none text-white me-2">Login</a>
    </div>
  </nav>

  <!-- 2. Header -->
  <header class="d-flex flex-column justify-content-center align-items-center">
      <h1 class="display-2 text-white fw-bold">Cinema</h1>
      <h1 class="display-2 text-white fw-bold">Community</h1>
      <a href="#" class="btn btn-primary btn-lg my-5">Let's Go</a>
  </header>

  <!-- 3. Section -->
  <section>
    <h2 class="d-flex justify-content-center my-5">Used Skills</h2>
    <article class="d-flex justify-content-evenly">
      <div class="d-flex flex-column align-items-center">
        <img src="images/web.png" alt="Web Image">
        <p>Web</p>
      </div>
      <div class="d-flex flex-column align-items-center">
        <img src="images/html5.png" alt="HTML5 Image">
        <p>HTML5</p>
      </div>
      <div class="d-flex flex-column align-items-center">
        <img src="images/css3.png" alt="CSS3 Image">
        <p>CSS3</p>
      </div>
    </article>
  </section>

  <!-- 4. Footer -->
  <footer class="d-flex fixed-bottom justify-content-center align-items-center bg-primary text-white">
    <p>HTML & CSS project. Created by JINWOO PARK</p>
  </footer>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
</body>
</html>
```

---

## Web Page Build Practice 2

```css
@import url('https://fonts.googleapis.com/css2?family=Merienda+One&family=Nunito:wght@200;300;400;500;600&display=swap');

/* 스크롤을 부드럽게 설정합니다. */
html{
  scroll-behavior: smooth;
}

/* 기본 글꼴 설정 */
body {
  font-family: 'Nunito', sans-serif;
  /* 창 크기가 줄어도 최소 1280px의 너비를 유지합니다. 
  디바이스의 화면 크기가 더 작다면 스크롤이 생성됩니다. */
  min-width: 1280px;
  color: #333333;
}

/*내비게이션 바 */
.nav-bar {
  display: flex;
  /* 서비스명과 메뉴 버튼이 서로 멀어지게 합니다. */
  justify-content: space-between;
  align-items: center;
  /* 내비게이션 바는 상단에 붙어 있습니다. */
  position: sticky;
  top: 0;
  left: 0;
  right: 0;
  height: 2rem;
  padding: 1rem 2rem; 
  /* sticky를 사용하는 경우 배경색을 지정해줘야 합니다. */
  background-color: white;
  height: 48px;
}

.service-name {
  font-size: large;
  font-family: 'Merienda One';
  margin-bottom: 0;
}

.nav-menu a {
  text-decoration: none;
  color: black;
  margin-left: 1rem;
}

/* 호버 시 색상 변화 */
.nav-menu a:hover {
  color: #5F98D1;
}

.banner {
  background: url(../assets/apparel.jpeg);
  background-repeat: no-repeat;
  background-size: cover;
  height: 600px;
}

/* 상단 이동 버튼 */
.pageup-btn {
  position: fixed;
  right: 1rem;
  bottom: 1rem;
  background: url(../assets/up-arrow.png);
  width: 2rem;
  height: 2rem;
  background-repeat: no-repeat;
  background-size: cover;
}

/* 본문 영역 */
.container {
  width: 1280px;
  margin-left: auto;
  margin-right: auto;
}

/* 본문의 한 영역을 담당합니다. */
.section {
  display: flex;
  padding: 0 3rem;
  margin: 3rem 0;
}

/* 각각의 타이틀입니다. */
.section-title {
  text-align: center;
  font-family: 'Merienda One';
  font-size: xx-large;
  margin-bottom: 0;
}

/* 제목과 콘텐츠의 세로 배치 */
.about {
  display: flex;
  flex-direction: column;
  padding-left: 2rem;
  padding-right: 2rem;
}

.section-description {
  font-size: large;
  margin-top: 1rem;
  line-height: 2rem;
}

/* 이미지의 크기 및 테두리 깎기. */
.info-img {
  width: 500px;
  border-radius: 1rem;
}

.contact-wrap {
  justify-content: space-around;
}

/* colmn 배치로 inline 요소들이 세로로 쌓이도록 조정합니다. */
.contact-form {
  display: flex;
  flex-direction: column;
  font-size: large;
  border: .2rem solid #333333;
  padding: 1rem;
}

.form-label {
  margin: 0.8rem 0;
}

.contact-form input {
  width: 400px;
  height: 2rem;
  padding: 0.5rem;
  border: 0.05rem solid #333333;
}

/* 버튼 호버 시 색상 변화 및 위치 조정. */
.form-button {
  width: 100px;
  margin: 1.5rem auto auto auto;
  background: none;
  cursor: pointer;
  border: 0.05rem solid #333;
}

.contact-form button:hover {
  background-color: #5F98D1;
}

.contact-img {
  width: 400px;
  height: 100%;
}

/* More 영역 */
.icon-wrap {
  display: flex;
  justify-content: space-evenly;
}

/* 이미지, 타이틀, 콘텐츠가 세로로 쌓이도록 조정합니다. */
.icon-box {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.icon {
  width: 64px;
  height: 64px;
}

.icon-text {
  margin-top: 1rem;
}

/* 푸터 영역 */
.footer-content {
  margin-top: 3rem;
  /* 위 테두리 선 긋기. */
  border-top: 0.1rem solid #333333;
  padding: 1rem;
  font-size: large;
  text-align: center;
}

/* PRODUCT PAGE */
.product-title {
  font-family: 'Merienda One';
  font-size: x-large;
  border-bottom: 0.1rem solid #333333;
  padding-bottom: 0.5rem;
  margin-bottom: 0;
}

.card-columns {
  display: flex;
  /* wrap 속성을 주어 넘치면 다음 줄로 가게끔 설정. */
  flex-wrap: wrap;
}

/* 각각의 카드 내부는 세로로 레이아웃 됩니다. */
.card {
  display: flex;
  flex-direction: column;
  /* 한 줄에 3개씩 배치되도록 조정 */
  margin: 1%;
  width: 31%;
  height: 350px;
  border: 0.05rem solid black;  
}

.card-img {
  padding: 0.5rem;
  width: 100%;
  height: 150px;
}

.card-title {
  margin-top: 0.5rem;
  text-align: center;
  font-size: large;
  font-weight: bold;
}

.card-content {
  padding: 0.5rem;
  line-height: 1.5rem;
}
```

<img width="1900" alt="html_108" src="https://user-images.githubusercontent.com/86648892/183304249-701bd497-80e0-46f9-8fa9-9f76eaf25aec.png">
<img width="1898" alt="html_109" src="https://user-images.githubusercontent.com/86648892/183304251-3d40638c-ca4c-417d-9808-2f817d0f6d74.png">
<img width="1904" alt="html_110" src="https://user-images.githubusercontent.com/86648892/183304252-6368e8e2-3fff-471a-b548-c7976b7c0ecc.png">

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="css/reset.css">
  <link rel="stylesheet" href="css/style.css">
  <title>SSAFY APPAREL</title>
</head>
<body>
  <!-- 네비게이션 영역 -->
  <nav class="nav-bar" id="nav-bar">
    <h1 class="service-name">SSAFY APPAREL</h1>
    <div class="nav-menu">
      <a href="index.html">HOME</a>
      <a href="products.html">PRODUCTS</a>
    </div>
  </nav>
  <!-- 이미지 배너 -->
  <div class="banner" id="banner"></div>

  <!-- 오른쪽 하단의 상단 이동 버튼 -->
  <a href="#banner" class="pageup-btn"></a>

  <!-- 본문 영역 -->
  <div class="container">
    <!-- About Our Company -->
    <div class="section">
      <img src="./assets/apparel2.jpeg" alt="apparel2" class="info-img">
      <article class="about">
        <h2 class="section-title">About Our Company</h2>
        <p class="section-description">Lorem ipsum dolor sit amet consectetur adipisicing elit. Eaque deleniti facilis recusandae non aspernatur nam rerum repellat reiciendis inventore iste, molestiae necessitatibus, voluptas nulla, quibusdam ducimus atque aliquid adipisci minus!
        Recusandae debitis velit reprehenderit praesentium repellendus modi est, blanditiis neque consequatur in libero rerum saepe voluptatibus sit at ducimus suscipit consectetur eum incidunt nostrum aut vel, laborum quis temporibus. Tempore!</p>
      </article>
    </div>

    <!-- Contacts -->
    <h2 class="section-title">Contact Us</h2>
    <div class="section contact-wrap">
      <form class="contact-form">
        <label for="username" class="form-label">Username</label>
        <input type="text" id="username" placeholder="Username" required>
        <label for="email" class="form-label">Email</label>
        <input type="email" placeholder="Email" required>
        <button class="form-button">Send</button>
      </form>
      <img class="contact-img" src="assets/contact.jpg" alt="contact">
    </div>

    <!-- More -->
    <h2 class="section-title">More</h2>
    <div class="section icon-wrap">
      <div class="icon-box">
        <img src="./assets/email.png" alt="icon" class="icon">
        <span class="icon-text">Email Address</span>
        <span class="icon-text">ssafy@ssafy.com</span>
      </div>
      <div class="icon-box">
        <img src="./assets/telephone.png" alt="icon" class="icon">
        <span class="icon-text">Phone Number</span>
        <span class="icon-text">010-1234-5678</span>
      </div>
      <div class="icon-box">
        <img src="./assets/location.png" alt="icon" class="icon">
        <span class="icon-text">Location</span>
        <span class="icon-text">서울특별시 역삼동</span>
      </div>
      <div class="icon-box">
        <img src="./assets/clock.png" alt="icon" class="icon">
        <span class="icon-text">Working Hours</span>
        <span class="icon-text">9am ~ 6pm</span>
      </div>
    </div>
  </div>

  <!-- 푸터 영역 -->
  <footer class="container">
    <div class="footer-content">
      <span>© Copyright 2022 By SSAFY | All Rights Reserved</span>
    </div>
  </footer>
</body>
</html>
```

<img width="1900" alt="html_111" src="https://user-images.githubusercontent.com/86648892/183304314-b88af945-baac-4c09-b5aa-097d9117633f.png">
<img width="1900" alt="html_112" src="https://user-images.githubusercontent.com/86648892/183304325-79598149-a224-49f6-8487-88ed984452d6.png">

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="css/reset.css">
  <link rel="stylesheet" href="css/style.css">
  <title>SSAFY APPAREL</title>
</head>
<body>
  <!-- 네비게이션 영역 -->
  <nav class="nav-bar">
    <h1 class="service-name">SSAFY APPAREL</h1>
    <div class="nav-menu">
      <a href="index.html">HOME</a>
      <a href="products.html">PRODUCTS</a>
    </div>
  </nav>
</header>

  <!-- 제품 영역 -->
  <div class="container">
    <div class="section">
      <h2 class="product-title">Our Products</h2>
    </div>
    <div class="section card-columns">
      <div class="card">
        <img src="assets/t-shirt.jpg" class="card-img">
        <span class="card-title">T-shirts</span>
        <span class="card-content">Lorem ipsum dolor sit amet consectetur adipisicing elit. Similique temporibus nihil cupiditate non porro, nesciunt, natus delectus, aliquam rerum quisquam animi ipsa quaerat aspernatur ea a? Fugit odio deleniti nemo?</span>
      </div>
      <div class="card">
        <img src="assets/coats.jpg" class="card-img">
        <span class="card-title">Coats</span>
        <span class="card-content">Lorem ipsum dolor sit amet consectetur adipisicing elit. Similique temporibus nihil cupiditate non porro, nesciunt, natus delectus, aliquam rerum quisquam animi ipsa quaerat aspernatur ea a? Fugit odio deleniti nemo?</span>
      </div>
      <div class="card">
        <img src="assets/jeans.jpg" class="card-img">
        <span class="card-title">Jeans</span>
        <span class="card-content">Lorem ipsum dolor sit amet consectetur adipisicing elit. Similique temporibus nihil cupiditate non porro, nesciunt, natus delectus, aliquam rerum quisquam animi ipsa quaerat aspernatur ea a? Fugit odio deleniti nemo?</span>
      </div>
      <div class="card">
        <img src="assets/shoes.jpg" class="card-img">
        <span class="card-title">Shoes</span>
        <span class="card-content">Lorem ipsum dolor sit amet consectetur adipisicing elit. Similique temporibus nihil cupiditate non porro, nesciunt, natus delectus, aliquam rerum quisquam animi ipsa quaerat aspernatur ea a? Fugit odio deleniti nemo?</span>
      </div>
      <div class="card">
        <img src="assets/suits.jpg" class="card-img">
        <span class="card-title">Suits</span>
        <span class="card-content">Lorem ipsum dolor sit amet consectetur adipisicing elit. Similique temporibus nihil cupiditate non porro, nesciunt, natus delectus, aliquam rerum quisquam animi ipsa quaerat aspernatur ea a? Fugit odio deleniti nemo?</span>
      </div>
      <div class="card">
        <img src="assets/accesories.jpg" class="card-img">
        <span class="card-title">Accessories</span>
        <span class="card-content">Lorem ipsum dolor sit amet consectetur adipisicing elit. Similique temporibus nihil cupiditate non porro, nesciunt, natus delectus, aliquam rerum quisquam animi ipsa quaerat aspernatur ea a? Fugit odio deleniti nemo?</span>
      </div>
    </div>
  </div>

   <!-- 푸터 영역 -->
   <footer class="container">
    <div class="footer-content">
      <span>© Copyright 2022 By SSAFY | All Rights Reserved</span>
    </div>
  </footer>
</body>
</html>
```

---

## Grid Breakpoint Practice

<img width="1319" alt="html_113" src="https://user-images.githubusercontent.com/86648892/183305234-10b33cbe-6363-43b2-ae3f-0b7837995e61.png">

```html

<!-- 01_grid.html -->

<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="style.css">
  <title>01_grid</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
</head>
<body>
  <div class="container">
    <div class="row">
      <div class="col">
        <h1>Bootstrap Grid System 1</h1>
      </div>
    </div>

    <!-- 1. -->
    <div class="row">
      <div class="item col-4">
        <p>4</p>
      </div>
      <div class="item col-4">
        <p>4</p>
      </div>
      <div class="item col-4">
        <p>4</p>
      </div>
    </div>

    <!-- 2. -->
    <div class="row">
      <div class="item col-6">
        <p>6</p>
      </div>
      <div class="item col-6">
        <p>6</p>
      </div> 
    </div>

    <!-- 3. -->
    <div class="row">
      <div class="item col-3">
        <p>3</p>
      </div>
      <div class="item col-6">
        <p>6</p>
      </div>
      <div class="item col-3">
        <p>3</p>
      </div>
    </div> 

    <!-- 4. -->
    <div class="row">
      <div class="item col-2">
        <p>2</p>
      </div>
      <div class="item col-9">
        <p>9</p>
      </div>
      <div class="item col-1">
        <p>1</p>
      </div> 
    </div>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
</body>
</html>

```

<img width="1318" alt="html_114" src="https://user-images.githubusercontent.com/86648892/183305236-7a8baba2-c1a7-4a69-a439-c3ebaac64fa3.png">

```html

<!-- 02_grid.html -->

<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="style.css">
  <title>02_grid</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
</head>
<body>
  <div class="container">
    <div class="row">
      <div class="col">
        <h1>Bootstrap Grid System 2</h1>
      </div>
    </div>

    <!-- 1. -->
    <div class="row">
      <div class="item col-4 col-sm-2">
        <p>576px 미만 4 <br> 576px 이상 2</p>
      </div>
      <div class="item col-4 col-sm-5">
        <p>576px 미만 4 <br> 576px 이상 5</p>
      </div>
      <div class="item col-4 col-sm-5">
        <p>576px 미만 4 <br> 576px 이상 5</p>
      </div>
    </div>

    <!-- 2. -->
    <div class="row">
      <div class="item col-1 col-md-2">
        <p>768px 미만 1 <br> 768px 이상 2</p>
      </div>
      <div class="item col-3 col-md-3">
        <p>768px 미만 3 <br> 768px 이상 3</p>
      </div>
      <div class="item col-4 col-md-3">
        <p>768px 미만 4 <br> 768px 이상 3</p>
      </div>
      <div class="item col-1 col-md-2">
        <p>768px 미만 1 <br> 768px 이상 2</p>
      </div>
      <div class="item col-3 col-md-2">
        <p>768px 미만 3 <br> 768px 이상 2</p>
      </div>
    </div>

    <!-- 3. -->
    <div class="row">
      <div class="item col-4 col-sm-3 col-md-6">
        <p>576px 미만 4 <br> 768px 미만 3 <br> 768px 이상 6</p>
      </div>
      <div class="item col-6  col-sm-3 col-md-6">
        <p>576px 미만 6 <br> 768px 미만 3 <br> 768px 이상 6</p>
      </div>
      <div class="item col-2 col-sm-6 col-md-12">
        <p>576px 미만 2 <br> 768px 미만 6 <br> 768px 이상 12</p>
      </div>
    </div>

    <!-- 4. -->
    <div class="row">
      <div class="item col-12 col-md-4 col-xl-2">
        <p>768px 미만 12 <br> 768px 이상 4 <br> 1200px 이상 2</p>
      </div>
      <div class="item col-12 col-md-4 col-xl-2">
        <p>768px 미만 12 <br> 768px 이상 4 <br> 1200px 이상 2</p>
      </div>
      <div class="item col-12 col-md-4 col-xl-12">
        <p>768px 미만 12 <br> 768px 이상 4 <br> 1200px 이상 12</p>
      </div>
    </div>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
</body>
</html>

```

<img width="1138" alt="html_115" src="https://user-images.githubusercontent.com/86648892/183305243-00568a73-7e59-47ce-ae30-cc97be4869ca.png">

```html

<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="style.css">
  <title>03_grid</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
</head>
<body>
  <div class="container">
    <div class="row">
      <div class="col">
        <h1>Bootstrap Grid System 3</h1>
      </div>
    </div>

    <!-- 1. -->
    <div class="row">
      <div class="item col-4 col-md-4">
        <p>item1</p>
      </div>
      <div class="item col-8 col-md-4 offset-md-4">
        <p>item2</p>
      </div>
    </div>

    <!-- 2. -->
    <div class="row">
      <div class="item col-4 col-md-4 offset-md-4 col-lg-5 offset-lg-7">
        <p>item1</p>
      </div>
      <div class="item col-4 offset-4 col-md-4 offset-md-0 col-lg-8 offset-lg-2">
      <!-- <div class="item col-4 offset-4 col-md-4 col-lg-8 offset-lg-2"> -->
        <!-- 위 line에 offset-md-0을 주는 이유는 offset-4가 선언되어있기에 md의 경우 다른 offset을 부여하고 싶다면 offset-md-0과 같이 새로 선언해줘야함 -->
        <p>item2</p>
      </div>
    </div>
    
    <!-- 3. -->
    <div class="row">
      <div class="item col-12 col-md-3 col-lg-3">
        item1
      </div>
      <div class="item col-12 col-md-9 col-lg-9">
        <div class="row">
          <div class="item col-6 col-md-6 col-lg-3">item2</div>
          <div class="item col-6 col-md-6 col-lg-3">item3</div>
          <div class="item col-6 col-md-6 col-lg-3">item4</div>
          <div class="item col-6 col-md-6 col-lg-3">item5</div>
        </div>
      </div>
    </div>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
</body>
</html>

```

---

# CHECK THESE SITES!
- [CSS Diner](https://flukeout.github.io/)
- [Flexbox Froggy](https://flexboxfroggy.com/#ko)
- [CSS Layout 정리](https://ko.learnlayout.com/display.html)
- [Grid System 정리](https://roseee.tistory.com/entry/Bootstrap-%EA%B7%B8%EB%A6%AC%EB%93%9C-%EC%8B%9C%EC%8A%A4%ED%85%9C-Grid-System)
- [Emmet Cheatsheet](https://docs.emmet.io/cheat-sheet/)