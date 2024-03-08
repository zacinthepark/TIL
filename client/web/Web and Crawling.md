# Web and Crawling

## Server & Client Architecture

- Client
    - Request: Browser를 사용하여 Server에 데이터를 요청

- Server
    - Response: Client의 Browser에서 데이터를 요청하면 요청에 따라 데이터를 Client로 전송

- Browser의 역할: 1. request를 보내 response를 받음 2. rendering
    - 클라이언트에서 URL을 통해 request를 보내면 Server는 WAS에서 이를 처리하여 html, text, img, json data 등 다양한 response를 보낸다
    - 웹 크롤링은 이러한 request를 보내는 과정을 코드화하여 동작시키는 것이라 이해할 수 있다
    - python에서는 `requests` 패키지가 있음

## URL (Uniform Resource Locator)

![url](https://github.com/zacinthepark/TIL/assets/86648892/315ee7d3-2ce9-40bf-9172-cf9f55fc76e5)

- Protocol: 규칙 ('한글'이라는 규칙을 통해 소통하는 것과 비슷한 맥락)

- Domain: DNS를 통해 IP 주소를 획득하고, 해당 서버로 요청이 이동할 수 있음
    - Primary Domain
    - Sub Domain

- Port: IP로는 서버 컴퓨터까지 찾아갈 수 있는데, 서버 안의 WAS, DBS와 같은 application에 접속할 때 필요한 식별자
    - HTTP 표준 프로토콜에서 http는 80, https는 443이 기본 포트이며, 생략 가능

- Path: 서버 컴퓨터 안에도 경로가 있다

- Page (File): 경로 안의 파일

- `?` 앞부분은 파일, 뒷부분은 Data

- Query: 클라이언트에서 웹 서버 쪽으로 보내는 추가적인 Data
    - `&` 기호로 구분되는 key-value 쌍 목록
    - 서버는 리소스를 응답하기 전 이러한 파라미터를 사용하여 추가 작업을 수행할 수 있음

- Fragment: 브라우저를 컨트롤하기 위한 부분
    - 리소스 내부 일종의 '북마크'로, 브라우저의 해당 북마크 지점에 있는 컨텐츠 표시
        - e.g. HTML 문서에서 브라우저는 앵커가 정의한 지점으로 스크롤함
    - fragment identifier라 부르는 `#` 이후 부분은 서버에 전송되지 않음
        - e.g. `https://docs.djangoproject.com/en/3.2/intro/install/#quick-install-guide` 요청에서 `#quick-install-guide`는 서버에 전달되지 않고 브라우저에게 해당 지점으로 이동할 수 있도록 함

## HTTP Request Methods

- Get
    - URL에 Query 포함
    - Query(데이터) 노출, 전송 가능 데이터 작음

- Post
    - Body에 Query 포함
    - Query(데이터) 비노출, 전송 가능 데이터 많음

## HTTP Status Code

- Client와 Server가 데이터를 주고 받은 결과 정보

- 2xx : Success
- 3xx : Redirect
- 4xx : Request Error
- 5xx : Server Error

## Cookie, Session, Cache

- Cookie
    - Client의 Browser에 저장하는 문자열 데이터
    - 사용 예시 : 로그인 정보, 내가 봤던 상품 정보, 팝업 다시보지 않음 등

- Session
    - Client의 Browser와 Server의 연결 정보
    - 사용 예시 : 자동 로그인

- Cache
    - Client, Server의 RAM(메모리)에 저장하는 데이터
    - RAM에 데이터를 저장하면 데이터 입출력이 빠름

## Web Language & Framework

- Client (Frontend)
    - HTML
    - CSS : Bootstrap, Semantic UI, Materialize, Material Design Lite
    - Javascript : React.js, Vue.js, Angular, jQuery

- Server (Backend)
    - Python : Django, Flask, FastAPI
    - Java : Spring
    - Ruby : Rails
    - Scala : Play
    - Javascript : Express(Node.js)

## Scraping & Crawling

- Scraping
    - 특정 데이터를 수집하는 작업

- Crawling
    - 웹 서비스의 여러 페이지를 이동하며 데이터를 수집하는 작업
    - spider, web crawler, bot 용어 사용
    - 구글 봇은 검색 기능에 사용되며, 사용자가 입력 검색어에 대하여 크롤링하여 결과를 반환

## Internet

- 컴퓨터로 연결하여 TCP/IP 프로토콜을 이요하여 정보를 주고 받는 컴퓨터 네트워크
- 해저케이블을 사용하여 전세계 컴퓨터에 접속
- 무선 인터넷은 매체(media)를 주파수 사용

## OSI 7 Layer

![osi_7_1](https://github.com/zacinthepark/TIL/assets/86648892/ec59942d-95c2-4cf3-8fa5-11f4596ca53b)

![osi_7_2](https://github.com/zacinthepark/TIL/assets/86648892/38050632-89be-4585-8645-f7c94aef8c36)

- Open System Interconnection Reference Model

- 국제표준화기구(OSI)에서 개발한 모델로 컴퓨터 네트워크 프로토콜 디자인과 통신을 계층으로 나누어 설명

- Layer가 낮을수록 페이로드 증가

## Web Crawling

- 웹 페이지에서 데이터를 수집하는 방법에 대해서 학습

## 웹 크롤링 방법

### 웹 페이지의 종류

- 정적인 페이지 : 웹 브라우저에 화면이 한번 뜨면 이벤트에 의한 화면의 변경이 없는 페이지
- 동적인 페이지 : 웹 브라우저에 화면이 뜨고 이벤트가 발생하면 서버에서 데이터를 가져와 화면을 변경하는 페이지

### requests 이용

- 받아오는 문자열에 따라 두 가지 방법으로 구분
    - **json 문자열**로 받아서 파싱하는 방법 : 주로 **동적 페이지 크롤링** 할 때 사용
    - **html 문자열**로 받아서 파싱하는 방법 : 주로 **정적 페이지 크롤링** 할 때 사용

### selenium 이용

- 브라우저를 직접 열어서 데이터를 받는 방법

### 크롤링 방법에 따른 속도

- requests json > requests html > selenium
