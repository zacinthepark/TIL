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

![htm1_1.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/25d1a685-cb7e-4268-b072-fda8824f5fb0/htm1_1.png)

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

![html_2.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/beb37743-e2bc-46f6-9f21-ef6807c04ba2/html_2.png)

- W3C는 웹 표준을 만드는 단체
    - 회원사가 많아 결정이 느림
        - 이에 따라 WHATWG가 HTML 5라는 표준을 제안했고, 현재 대세
- [https://caniuse.com/](https://caniuse.com/)
    - 사용하고 싶은 기술을 검색하면 브라우저 호환성을 확인할 수 있음

---

# 개발환경 설정(Chrome)

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

![html_3.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2a86d8c1-85ad-412a-8a03-877f241470b7/html_3.png)

## HTML

- 웹 페이지를 작성(구조화)하기 위한 언어
- .html
- HTML 스타일 가이드
    - indent 2칸 (indent가 없어도 문제는 없지만 사실상 해야함)
- HTML이란
    - 태그를 이용하여 구조를 만들고
        - 브라우저로 실행하는 문서
            - 태그, 구조, 브라우저, 문서

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

- '<title>' : 브라우저 상단 타이틀
- '<meta>' : 문서 레벨 메타데이터 요소
- '<link>' : 외부 리소스 연결 요소 (CSS 파일, favicon 등)
- '<script>' : 스크립트 요소 (Javascript 파일 / 코드)
- '<style>' : CSS 직접 작성

![html_4.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/78366c7a-e2ac-4053-990a-4b27036cde1c/html_4.png)

![html_5.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f14346a3-5b73-4f88-9b5d-88e6da7ee263/html_5.png)

## head의 또 다른 예시 : Open Graph Protocol

- 메타데이터를 표현하는 새로운 규약
    - HTML 문서의 메타데이터를 통해 문서의 정보를 전달
    - 메타정보에 해당하는 제목, 설명 등을 쓸 수 있도록 정의
    - 메타 property에 설정하면 원하는대로 내용이 나옴
        - 썸네일 같은 것들을 OG protocol을 사용하여 메타데이터 표현함
        - 이런 메타데이터 부분도 실제 개발자들이 다 개발하는 것

![html_6.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/923ccc3d-0c64-4318-891a-c60a04ee1380/html_6.png)

## HTML 요소(element)

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

![html_7.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/30311d5e-107d-4bbd-be64-d7ab35e1ba75/html_7.png)

## HTML 속성(attribute)

```html
<a href = "https://google.com"></a>

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

![html_8.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ab38124d-cb75-4f70-8bc3-effced583866/html_8.png)

## HTML 코드 예시

```html
<!DOCTYPE html>
<html lang = "en">
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

![html_9.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5c98a810-e75e-42d3-b9dd-3d19274b66cd/html_9.png)

## 시맨틱 태그

- HTML 태그가 특정 목적, 역할 및 의미적 가치(semantic value)를 가지는 것
    - 예를 들어 h1 태그는 “이 페이지에서 최상위 제목"인 텍스트를 감싸는 역할(또는 의미)을 나타냄
- Non semantic 요소
    - div, span
        - div : 콘텐츠의 구획을 나타냄
- a, form, table 태그들도 시맨틱 태그로 볼 수 있음
- HTML 5에서는 기존에 단순히 콘텐츠의 구획을 나타내기 위해 사용한 div 태그르 대체하여 사용하기 위해 의미론적 요소를 담은 태그들이 추가됨
- 대표적인 시맨틱 태그 목록
    - header : 문서 전체나 섹션의 헤더(머리말 부분)
    - nav : 내비게이션
    - aside : 사이드에 위치한 공간, 메인 콘텐츠와 관련성이 적은 콘텐츠
    - section : 문서의 일반적인 구분, 컨텐츠의 그룹을 표현
    - article : 문서, 페이지, 사이트 안에서 독립적으로 구분되는 영역
    - footer : 문서 전체나 섹션의 푸터(마지막 부분)
    
    ![html_10.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0740dde6-3c79-4198-bef7-7b0e1cbf55f4/html_10.png)
    
- 왼쪽 오른쪽은 똑같이 작동하더라도 코드를 봤을 때 시맨틱 태그가 의미를 알기 쉬움

![html_11.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/62353d17-cca0-472c-adad-7c1827c2a5c8/html_11.png)

- 구글 뉴스 상단의 메뉴는 Header 태그를 통해서 명확하게 표현하고 있음

![html_12.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1f4128ef-e288-4cbf-ab0e-3718759394f4/html_12.png)

![html_13.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d71355af-c145-482c-a6b6-472a01317c01/html_13.png)

![html_14.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6a24c25c-8cda-4f6c-933c-e1a0f85d8630/html_14.png)

![html_15.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1e8f52fe-18b2-42ce-84ac-b475b875ac0b/html_15.png)

## WHY 시맨틱 태그?

- 의미론적 마크업
    - 개발자 및 사용자 뿐만 아니라 검색엔진 등에 의미있는 정보의 그룹을 태그로 표현
    - 단순히 구역을 나누는 것이 뿐만 아니라 ‘의미'를 가지는 태그들을 활용하기 위한 노력
    - 요소의 의미가 명확해지기 때문에 코드의 가독성을 높이고 유지보수를 쉽게 함
    - 검색 엔진 최적(SEO)를 위해서 메타태그, 시맨틱 태그 등을 통한 마크업을 효과적으로 활용해야 함

## 렌더링(Rendering)

- 텍스트로 작성된 코드가 어떻게 웹 사이트가 되는걸까?
- 웹 사이트 코드를 사용자가 보게 되는 웹 사이트로 바꾸는 과정을 렌더링이라 한다

## DOM(Document Object Model) 트리

- 텍스트 파일인 HTML 문서를 브라우저에서 렌더링하기 위한 구조
    - HTML 문서에 대한 모델을 구성함
    - HTML 문서 내의 각 요소에 접근 / 수정에 필요한 프로퍼티와 메서드를 제공함
- DOM에 따라 잘라서 기억해놨다가 화면에 그리는 느낌이라 생각하면 편하다

![html_16.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2ea8aadc-1c49-46de-9c15-d9a7c9177216/html_16.png)

![html_17.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1804254c-b7f3-4ceb-a5bf-c2a6c18b9298/html_17.png)

# HTML 문서 구조화

## 인라인 / 블록 요소

- HTML 요소는 크게 인라인 / 블록 요소로 나눔
- 인라인 요소는 글자처럼 취급
- 블록 요소는 한 줄 모두 사용
- <태그>내용</태그>로 표현되는 HTML 요소를 분류하자면 인라인, 블록 요소로 구분할 수 있다는 것이다

## 텍스트 요소

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

![html_18.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d395948f-fee0-4d96-983c-4b51fd9f5af2/html_18.png)

## 그룹 컨텐츠

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

![html_19.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/71030760-36e9-4666-918c-b7d4bebee6d8/html_19.png)

- div와 span은 다른 작업을 위한 일종의 투명한 쇼핑백과 같은 것이다

---
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
    - `.margin-1 {}`
        - 전부
    - `.margin-2 {}`
        - 상하, 좌우
    - `.margin-3 {}`
        - 나누기 모양
    - `.margin-4 {}`
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
- sticky
    - 처음 내가 생성된 위치를 기준으로 해서 화면상에 그대로 stick!

---
## Flexbox (Flexible Box!)

- 행과 열 형태로 아이템들을 배치하는 1차원 레이아웃 모델
    - z-index는 차원 간 배치
- 정렬을 하는 느낌
- ie에서 부분지원됨
- `display:flex`
    - flex-container에서 선언
    - 이 객체가 flex-container라 선언하는 것이고
        - 그 바로 아래 레벨이 flex items가 된다
- `display: inline flex`
    - 인라인과 블록의 차이처럼 요소의 테두리가 줄어듬
- 인라인처럼 사용할 수 있고, 내용물의 크기만큼만 차지
- `flex-direction`
    - 요소를 배치할 방향
        - row
        - row-reverse
        - column
        - column-reverse
- main axis라는 꽂이에 레이아웃을 꽂는다고 생각
    - cross axis는 main axis에 수직인 축
- 부모 요소 Flex Container
    - 자식 요소 Flex Item
    - 부모 요소에 Flex를 적용
    - 아이템에 적용하는 것이 아니다

## Flex 속성

- 공간 나누기는 꽂고 남은 공간을 어떻게 나눌 것인가? 배치할 것인가?

### flex-direction

- main axis
- 역방향의 경우 눈으로 보이는 것과 코드 실행 순서가 다를 수 있으니 주의

### flex-wrap

- nowrap은 한 줄안에 크기를 조정해서라도 끼워넣고 싶을 때
    - 기본값
- wrap은 크기 그대로 보장하여 줄바꿈을 통해 끼워넣고 싶을 때
- wrap-reverse는 최신글이 위에 오도록 하고 싶을 때 쓰면 좋을듯

### flex flow

- `flex-flow: row nowrap;`
    - 이처럼 direction과 wrap의 shorthand

### justify-content

- main axis를 기준으로 공간 배분

### align-content

- cross axis를 기준으로 공간 배분
- stretch는 늘리는 것
- 글자들은 baseline을 가짐

### align-self

- 각 아이템들 배치

### 기타 속성

- flex-grow
    - 남은 여백을 grow값이 있는 요소들끼리 나눠가짐
- order
    - 배치 순서
    - 눈에 보이는 순서대로 코드가 실행되지 않아 꼬일 수도 있어서 자주 사용하지 않음

---

# Bootstrap

정형화된 css 컨텐츠를 편리하게 사용할 수 있도록 모아놓은 것

쉽게 말해 css 코드 덩어리다

- UI를 빠르게 빌드할 수 있다
- 반응형 웹을 편리하게 구현할 수 있다
- 그리드 시스템의 핵심은 화면을 12칸으로 보고 어떤 식으로 분할할지 선택하는 것

## CDN

- Content Delivery Network
- import와 비슷한 개념
- CDN via jsDelivr
    - link는 </head> 앞에
    - script는 </body> 앞에
        - 코드의 실행 속도를 위해

## Bootstrap의 기본 원리

### Spacing

- margin
- padding
- css는 부트스트랩 개발자들이 만들어놓았기에 클래스 지정만 하면됨
- mt-3
    - m은 property, t는 sides, 3은 size
- property
    - m - margin
    - p - padding
- sides
    - s - start
        - margin left나 padding left
    - e - end
        - right
    - x - 양 옆
    - y - 위 아래
    - blank - 4방향 전부
- size
    - 0, 1, 2, 3, 4, 5, auto
        - 1은 0.25rem
            - 1rem은 16px
            - rem의 장점은 html 기준으로 바로 적용 가능

### Color

- 텍스트 컬러, 백그라운드 컬러 모두 적용 가능

### Text

- text-decoration-none 많이 사용한다

### Position

### Display

- `d-`
- d-none은 코드는 있는데 보이지 않음
- `d-md-none`
    - 반응형
- `d-sm-none`
    - 반응형

### Components

- Button
- Dropdown
- Navbar
    - 많이 사용함!
    - 구조 살펴보면 d-flex로 배치해놓은거임
- Carousel
    - 회전목마돌듯이 누르면 사진이 넘어가는 UI
- Modal
    - 실수 많이 한다
    - 팝업은 보통 x를 눌러야 사라지고 modal 해당 동작이 아닌 다른 곳을 클릭해도 사라진다는 차이점
    - data-bs-target에 다른 곳에 지정해준 객체의 id를 넣어주면 연결됨!
    - 중첩해서 들어가있으면 안됨
        - Modals use `position: fixed`, which can sometimes be a bit particular about its rendering. Whenever possible, place your modal HTML in a top-level position to avoid potential interference from other elements. You’ll likely run into issues when nesting a `.modal` within another fixed element

### Flexbox in Bootstrap

### Grid Card

- 반응형은 `<div *class*="row row-cols-1 row-cols-md-3 g-4">` 덕분에 이루어짐

---

## Grid System

- 12개의 column
- 6개의 breakpoint
- column 사이의 공간을 gutter라고 함

![스크린샷 2022-08-03 오후 3.32.50.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f7d799f5-ebc9-42af-b9e3-7ce69ed150f2/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2022-08-03_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_3.32.50.png)

- div w-100은 텅빈 width 100짜리이므로 줄바꿈의 한 방법
    - 그냥 row 구획을 하나 더 만들어주는게 좋다
- 원하는 비율을 col-숫자로 넣어준다
- 1짜리 13개면 1개가 다음 줄로 넘어간다
    - 12칸이 넘어가는 순간의 객체는 줄바꿈이 되어 넘어감
- offset은 비우고싶을 때 사용

---

## 추가 정리

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

- [https://flexboxfroggy.com/#ko](https://flexboxfroggy.com/#ko)

---

box를 통한 positioning 연습

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
Bootstrap practice
```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <!-- Bootstrap CSS -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous">
  <!-- Custom CSS -->
  <link rel="stylesheet" href="01_nav_footer.css">
  <link rel="stylesheet" href="03_community.css">
  <title>Community</title>
</head>
<body>
  <!-- 01_nav_footer에서 작성한 Navigation bar & Modal & Footer 코드를 적절한 위치에 사용합니다. -->
  <!-- Navbar -->
  <nav class="navbar navbar-expand-md navbar-dark bg-dark">
    <div class="container-fluid">
      <a href="/02_home.html">
        <img src="/images/logo.png" alt="logo image" height="45">
      </a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link active" href="/02_home.html">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link active" href="/03_community.html">Community</a>
          </li>
          <li class="nav-item">
            <a class="nav-link active" href="#loginModal" data-bs-toggle="modal" data-bs-target="#exampleModal">Login</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
<!-- Modal Info -->
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <div class="mb-1">
          <label for="exampleFormControlInput1" class="form-label fw-bold">Email adress</label>
          <input type="email" class="form-control" id="exampleFormControlInput1">
        </div>
        <h6>We'll never share your email with anyone else.</h6>
        <div class="my-3">
          <label for="exampleFormControlTextarea1" class="form-label fw-bold">Password</label>
          <input type="password" class="form-control" id="exampleFormControlTextarea1">
        </div>
        <div class="form-check mb-3">
          <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
          <label class="form-check-label" for="flexCheckDefault">
            Check me out
          </label>
        </div>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Submit</button>
      </div>
    </div>
  </div>
</div>
  <!-- 03_community.html -->
  <main class="container-fluid w-100 py-3">
    <h1 class="fw-semibold fst-italic fix_left_margin">Community</h1>
    <div class="row fix_left_margin">
      <!-- Aside - 게시판 목록 -->
      <aside class="list-group col col-12 col-lg-2">
        <li class="list-group-item">
          <a href="#" class="text-decoration-none">Boxoffice</a>
        </li>
        <li class="list-group-item">
          <a href="#" class="text-decoration-none">Movies</a>
        </li>
        <li class="list-group-item">
          <a href="#" class="text-decoration-none">Genres</a>
        </li>
        <li class="list-group-item">
          <a href="#" class="text-decoration-none">Actors</a>
        </li>
      </aside>
      <!-- Section - 게시판 -->
      <section class="container col col-12 col-lg-10">
        <div class="d-none d-lg-block">
          <table class="table table-striped">
            <thead class="table-dark">
              <tr>
                <th scope="col">Movie Titles</th>
                <th scope="col">Posts</th>
                <th scope="col">Username</th>
                <th scope="col">Uploaded</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <th scope="row" class="fst-italic">The ShawShank Redemption</th>
                <td>Run!</td>
                <td>Zac</td>
                <td>1 minute ago</td>
              </tr>
              <tr>
                <th scope="row" class="fst-italic">Joker</th>
                <td>Grrrrrrrrrr</td>
                <td>Aiden</td>
                <td>1 minute ago</td>
              </tr>
              <tr>
                <th scope="row" class="fst-italic">Top Gun: Maverick</th>
                <td>Pew</td>
                <td>Jin</td>
                <td>1 minute ago</td>
              </tr>
              <tr>
                <th scope="row" class="fst-italic">500 Days of Summer</th>
                <td>Hi there!</td>
                <td>Katie</td>
                <td>1 minute ago</td>
              </tr>
            </tbody>
          </table>
        </div>
        <div class="d-lg-none">
          <article class="list-group">
            <li class="list-group-item">
              <div>
                <p class="mb-2 fst-italic fw-semibold fs-3">The ShawShank Redemption</p>
                <p class="mb-2 fs-5">Run!</p>
                <div class="mb-1">
                  Zac
                </div>
                <div>
                  <small>1 minute ago</small>
                </div>
              </div>
            </li>
            <li class="list-group-item">
              <div>
                <p class="mb-2 fst-italic fw-semibold fs-3">Joker</p>
                <p class="mb-2 fs-5">Grrrrrrrrrr</p>
                <div class="mb-1">
                  Aiden
                </div>
                <div>
                  <small>1 minute ago</small>
                </div>
              </div>
            </li>
            <li class="list-group-item">
              <div>
                <p class="mb-2 fst-italic fw-semibold fs-3">Top Gun: Maverick</p>
                <p class="mb-2 fs-5">Pew</p>
                <div class="mb-1">
                  Jin
                </div>
                <div>
                  <small>1 minute ago</small>
                </div>
              </div>
            </li>
            <li class="list-group-item">
              <div>
                <p class="mb-2 fst-italic fw-semibold fs-3">500 Days of Summer</p>
                <p class="mb-2 fs-5">Hi there!</p>
                <div class="mb-1">
                  Katie
                </div>
                <div>
                  <small>1 minute ago</small>
                </div>
              </div>
            </li>
          </article>
        </div>
      </section>
    </div>
    <div class="d-flex justify-content-center my-4">
      <nav aria-label="Page navigation example">
        <ul class="pagination">
          <li class="page-item"><a class="page-link" href="#">Previous</a></li>
          <li class="page-item"><a class="page-link" href="#">1</a></li>
          <li class="page-item"><a class="page-link" href="#">2</a></li>
          <li class="page-item"><a class="page-link" href="#">3</a></li>
          <li class="page-item"><a class="page-link" href="#">Next</a></li>
        </ul>
      </nav>
    </div>
  </main>

  <!-- Footer -->
  <footer>
    <div class="d-flex fixed-bottom justify-content-center mx-auto">
      <p>Web-bootstrap PJT, by JINWOO PARK</p>
    </div>
  </footer>
  <!-- Bootstrap JS -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-pprn3073KE6tl6bjs2QrFaJGz5/SUsLqktiwsUTF55Jfv3qYSDhgCecCxMW52nD2" crossorigin="anonymous"></script>
</body>
</html>

```
## Bootstrap practice

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