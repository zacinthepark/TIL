## MTV 기초

---

- Template
    - [Django Template, DTL Syntax](#django-template)
    - [Sending and Retrieving Form Data](#sending-and-retrieving-form-data)
- Model
    - [Modeling](#modeling)
    - [Migrations](#migrations)
- View
    - [CRUD with view functions](#crud-with-view-functions)


- `templates` 디렉토리 생성 및 `index.html` 파일 생성
- `return render(request, 'index.html')`
    - 해당 request에 대하여 index.html파일을 렌더링해줘
    - context는 data라고 생각하자
    - `settings.py` 에 TEMPLATES
        - 여기에 `APP_DIRS` 에 `True` 가 기본값으로 설정되어있어 articles 앱 내부의 template을 인식할 수 있음
        - **그 외 따로 디렉토리를 만들어 인식시켜주고 싶을 경우 `DIRS`에 정의**

### 3. Templates

- 실제 내용을 보여주는데 사용되는 파일
- 파일의 구조나 레이아웃을 정의
- `app_name/templates/`
    - 템플릿 폴더의 이름은 반드시 **templates**라고 지정해야함

## Django Template

---

- Template System의 기본 목표를 숙지하자
    - **데이터 표현을 제어하는 도구이자 표현에 관련된 로직**
    - Django Template을 이용한 HTML 정적 부분과 동적 컨텐츠 삽입

### DTL(Django Template Language)

- Django template에서 사용하는 built-in template system
    - html 파일을 조금 더 쉽게 만들어주는 Django만의 문법
    - 실무에서는 잘 사용하지 않는다
- 조건, 반복, 변수 치환, 필터 등의 기능을 제공
    - Python처럼 일부 프로그래밍 구조(if, for 등)를 사용할 수 있지만 이것은 **Python 코드로 실행되는 것이 아님**
    - Django 템플릿 시스템은 단순히 Python이 아닌 HTML에 포함된 것이 아니니 주의
- 프로그래밍적 로직이 아니라 프레젠테이션을 표현하기위한 것임을 명심할 것

### DTL Syntax

### 1. Variable

- `{{ variable }}`
    - 변수명은 영어, 숫자와 밑줄(`_`)의 조합으로 구성될 수 있으나 밑줄로는 시작할 수 없음
        - 공백이나 구두점 문자 또한 사용할 수 없음
    - `.` 을 사용하여 변수 속성에 접근할 수 있음
    - `render()` 의 세번째 인자로 `{'key': value}` 와 같이 딕셔너리 형태로 넘겨주며, 여기서 정의한 key에 해당하는 문자열이 template에서 사용가능한 변수명이 됨
        - `views` 에의 함수 내에서 `models` 로부터 받아온 데이터를 바탕으로 ,보통 `context` 라는 이름으로 딕셔너리를 정의하여 이 정보를 연결된 `templates` 파일에 넘겨줌

### 2. Filters

- `{{ variable|filter }}`
    - 표시할 변수를 수정할 때 사용
    - 예시
        - `{{ name|lower }}`
        - name 변수를 모두 소문자로 출력
    - 60개의 built-in template filters를 제공
    - chained가 가능하며 일부 필터는 인자를 받기도 함
        - `{{ name|truncatewords:30 }}`

### 3. Tags

- `{% tag %}`
    - 출력 텍스트를 만들거나, 반복 또는 논리를 수행하여 제어 흐름을 만드는 등 변수보다 복잡한 일들을 수행
    - 일부 태그는 시작과 종료 태그가 필요
        - `{% if %} {% endif %}`
    - 약 24개의 built-in template tags를 제공

### 4. Comments

- `{# #}`
    - Django template에서 라인의 주석을 표현하기 위해 사용
    - 아래처럼 유효하지 않은 템플릿 코드가 포함될 수 있음
        - `{# {% if %} text {% endif %} #}`
- `{% comment %} {% endcomment %}`
    - 여러 줄 주석에 사용

<img width="1231" alt="dj_15" src="https://user-images.githubusercontent.com/86648892/188303753-c3605294-4d31-45b6-a899-d69707ed3392.png">

<img width="1238" alt="dj_16" src="https://user-images.githubusercontent.com/86648892/188303754-60f618fe-f462-488e-aec3-d4033311dffd.png">

<img width="1230" alt="dj_17" src="https://user-images.githubusercontent.com/86648892/188303755-3cd42d50-db74-4d92-9ae9-30a596bbd466.png">

<img width="1222" alt="dj_18" src="https://user-images.githubusercontent.com/86648892/188303756-b66d9a18-7863-4ff4-8cfc-15e3a90be021.png">

<img width="1210" alt="dj_19" src="https://user-images.githubusercontent.com/86648892/188303757-286705a5-69de-4a7f-b99e-f656c588e327.png">

### [참고] Trailing URL Slashes

- Django에서는 trailing slash 옵션이 True
    - Django는 URL 끝에 `/` 가 없다면 자동으로 붙여주는 것이 기본 설정
        - 그래서 모든 주소가 `/` 로 끝나도록 구성되어있음
        - 모든 프레임워크가 이렇게 동작하는 것은 아님
        - 검색 엔진 로봇이나 웹 트래픽 분석 도구에서는 `/` 이 붙은 것과 붙지 않은 것을 다른 페이지로 보며, Django는 URL을 정규화하여 검색 엔진 로봇이 혼동하지 않도록 함
    - url을 적어줄 때 끝에 `/` 를 붙여주자
    - [Trailing URL Slashes?](https://djkeh.github.io/articles/Why-do-we-put-slash-at-the-end-of-URL-kor/)
- 앞에 `/` 는 현재 슬래시가 시작점이라는 의미
    - `/index/` 로 anchoring하면
        - `greetings/index/` 와 같이 현재 url에서 index라는 path를 덧붙여주는 형태로 됨

### 템플릿 상속

- 기본 ‘skeleton’ 템플릿을 만들어
    - 사이트의 모든 공통 요소를 포함하고, 하위 템플릿이 재정의(override)할 수 있는 블록을 정의
    - 코드의 재사용성
- `base.html`
    - base라는 이름의 skeleton 템플릿 작성
    - `base.html` 에서 바뀌어야될 부분은 block으로 구멍을 뚫어줌
    - `base.html` 을 상속받는 템플릿은 `{% extends base.html %}` 을 통해 상속받음을 선언하고, 같은 이름의 block 태그를 선언 뒤, 해당 block 태그 내에 추가할 부분을 작성

<img width="1194" alt="dj_20" src="https://user-images.githubusercontent.com/86648892/188303759-35b15e9c-0146-4f2d-b2ee-54c2f71c0bb6.png">

### 추가 템플릿 경로 추가하기

<img width="1210" alt="dj_21" src="https://user-images.githubusercontent.com/86648892/188303760-b489e68f-b076-4cc7-ab55-d86415d65756.png">

- `settings.py` 의 DIRS에 추가하여 너 templates 찾을 때 이쪽도 찾아달라고 명령
    - `BASE_DIR` 은 프로젝트 홈 디렉토리를 가리키도록 설정해놓은 값
    - `BASE_DIR / templates`
        - 홈 디렉토리 바로 하위에 있는 templates
        - trailing comma 써주는 습관을 들이자

### BASE_DIR

- `settings.py`
    - `BASE_DIR = Path(__file__).resolve().parent.parent`
    - `settings.py` 에서 특정 경로를 절대경로로 편하게 작성할 수 있도록 Django에서 미리 지정해둔 경로 값
    - “객체 지향 파일 시스템 경로”
        - 운영체제별로 파일 경로 표기법이 다르기 때문에 어떤 운영체제에서 실행되더라도 각 운영체제 표기법에 맞게 해석될 수 있도록 하기 위해 사용
        - [Python Docs Pathlib](https://docs.python.org/3/library/pathlib.html)

## Sending and Retrieving form data

---

### `<form></form>`

- form 태그
- WEB에서 사용자 Input을 받는 방법
- `<form target="_blank">`
- 새 탭에서 열기

### Client & Server Architecture

<img width="522" alt="dj_22" src="https://user-images.githubusercontent.com/86648892/188303762-08c454f8-1b8a-4944-b929-55c18658df79.png">

- 웹은 기본적으로 클라이언트-서버 아키텍처를 사용
    - 클라이언트(일반적으로 웹 브라우저)가 서버에 요청을 보내고, 서버는 클라이언트의 요청에 응답
- 클라이언트 측에서 **HTML form**은 HTTP 요청을 서버에 보내는 가장 편리한 방법
- 이를 통해 **사용자는 HTTP 요청에서 전달할 정보를 제공**할 수 있음

### 1. Sending form data (Client)

### HTML `<form>` element

- 데이터가 전송되는 방법을 정의
- 웹에서 사용자 정보를 입력하는 여러 방식(text, button, submit 등)을 제공하고, **사용자로부터 할당된 데이터를 서버로 전송**하는 역할을 담당
- “데이터를 어디(action)로 어떤 방식(method)으로 보낼지”
    - 핵심 속성
        - action
        - method

### HTML form’s attributes

1. **action**

- 입력 데이터가 전송될 URL을 지정
- 데이터를 어디로 보낼 것인지 지정하는 것이며 이 값은 반드시 유효한 URL이어야함
- 만약 이 속성을 지정하지 않으면 데이터는 현재 form이 있는 페이지의 URL로 보내짐

2. **method**

- 데이터를 어떻게 보낼 것인지 정의
- 입력 데이터의 HTTP request methods를 지정
    - HTML form 데이터는 GET, POST 2가지 방법으로만 전송할 수 있음
    - READ 시 `GET`
    - CREATE, UPDATE, DELETE 시 `POST`
- 정의하지 않을 시 기본값 GET 적용

### HTML `<input>` element

- 사용자로부터 데이터를 입력받기 위해 사용
- `type` 속성에 따라 동작 방식이 달라짐
    - input 요소의 동작 방식은 type 특성에 따라 현격히 달라지므로 MDN 문서 참고하여 사용
    - 지정하지 않은 경우 기본값은 text
- `<label>`과 주로 함께 사용하여 label의 `for` 과 input의 `id` 가 연결
- input의 `name` 속성
    - form을 통해 데이터를 제출(submit)했을 때 name 속성에 설정된 값을 서버로 전송하고, 서버는 name 속성에 설정된 값을 통해 사용자가 입력한 데이터 값에 접근할 수 있음
        - 즉, name 속성이 요청 데이터의 key값이 됨
        - GET, POST 방식으로 서버에 전달하는 파라미터(name은 key, value는 value)로 매핑
        - GET 방식에서는 URL에서 `?key=value&key=value/` 형식으로 데이터를 전달

### HTTP request methods

- HTTP
  - HTML 문서와 같은 리소스(데이터, 자원)들을 가져올 수 있도록 해주는 프로토콜(규칙)
  - 웹에서 이루어지는 모든 데이터 교환의 기초
  - HTTP는 주어진 리소스가 수행할 원하는 작업을 나타내는 request methods를 정의
- HTTP request methods
  - 자원에 대한 행위(수행하고자 하는 동작)을 정의
  - GET, POST, PUT, DELETE
  - GET
    - 서버로부터 정보를 **조회**하는데 사용
        - 즉, 서버에게 리소스를 요청하기 위해 사용
    - **데이터를 가져올 때만 사용해야함**
    - **데이터를 서버로 전송할 때 Query String Parameters를 통해 전송**
        - 데이터는 URL에 포함되어 서버로 보내짐

### Query String parameters

- 사용자가 입력 데이터를 전달하는 방법 중 하나
    - URL 주소에 데이터를 파라미터를 통해 넘기는 것
- 앰퍼샌드(`&`)로 연결된 `key=value` 쌍으로 구성되며, 기본 URL과 물음표(`?`)로 구분됨
    - 정해진 주소 이후에 물음표를 쓰는 것으로 Query String이 시작함을 알림
    - `=` 로 key와 value가 구분됨
    - 파라미터가 여러 개일 경우 `&` 를 붙여 여러 개의 파라미터를 넘길 수 있음

### 2. Retrieving the data (Server)

- 데이터 가져오기
- 서버는 클라이언트로 받은 key-value 쌍의 목록과 같은 데이터를 받게됨
- 목록에 접근하는 방법은 사용하는 프레임워크에 따라 다름
- “모든 요청 데이터는 view 함수의 첫번째 인자 request에 들어있다”

<img width="1201" alt="dj_23" src="https://user-images.githubusercontent.com/86648892/188303763-3b08893a-bba8-4423-9926-86eeec9c4769.png">

<img width="1096" alt="dj_24" src="https://user-images.githubusercontent.com/86648892/188303764-44b69b3c-e71f-4a04-bfb6-7f9bde4d8993.png">

<img width="1115" alt="dj_25" src="https://user-images.githubusercontent.com/86648892/188303766-343865cf-56f6-4dea-8b3d-b1bd7a7d71ac.png">

<img width="1215" alt="dj_26" src="https://user-images.githubusercontent.com/86648892/188303769-7bab033d-ccc3-4b3a-8058-90655c952449.png">

### 요청과 응답 객체 흐름 정리

- 페이지가 요청되면 Django는 요청에 대한 메타데이터를 포함하는 HttpRequest object를 생성
- 그리고 해당하는 적절한 view 함수를 로드하고 HttpRequest를 첫번째 인자로 전달
- 마지막으로 view 함수는 HttpResponse object를 반환


### Namespace

### 2. Template namespace

- Django는 기본적으로 `app_name/templates/` 경로에 있는 templates 파일들만 찾을 수 있으며, `settings.py` 의 INSTALLED_APPS에 작성한 app 순서로 template을 검색 후 렌더링함
    - `settings.py` 의 TEMPLATES 내부 `APP_DIRS: True` 가 해당 경로를 활성화하고 있음
    - 쉽게 말해 등록된 앱들 중 같은 이름의 템플릿이 있을 경우 앱 순서에 따라 먼저 등록된 것을 렌더링
- Django templates의 기본 경로 자체를 변경할 수는 없기에 물리적으로 이름 공간을 만든다
- 하위 디렉토리 경로를 하나 더 줘서 샌드위치 구조로 templates 경로를 재설정
    - `app_name/templates/app_name`

<img width="1151" alt="dj_37" src="https://user-images.githubusercontent.com/86648892/188498013-b999a577-cc83-4e34-a4ba-a6b3e7b96962.png">


## Migrations

---

- 작성한 모델의 클래스를 실제 데이터베이스에 반영하는 과정
- `models.py` 에서 작성한 것이 테이블의 스키마라고 할 때, DB에 직접 만들 테이블의 설계도가 migrations 파일들
    - `$ python manage.py makemigrations`
        - 실제로 DB에 옮길 설계도 생성
    - `$ python manage.py migrate`
        - 해당 설계도 파일을 바탕으로 DB에 동기화

### 1. makemigrations

- `$ python manage.py makemigrations`
- 모델을 작성 혹은 변경한 것에 기반한 새로운 migration(설계도, 청사진, 혹은 마이그레이션)을 만들 때 사용
- “테이블을 만들기 위한 설계도를 생성하는 것”

<img width="918" alt="dj_41" src="https://user-images.githubusercontent.com/86648892/188498027-7bf335ed-b7c3-4284-8067-50fae4812ba6.png">

- `migrations/0001_initial.py` 모습
    - “파이썬으로 작성된 최종 설계도”
    - blueprint
    - 아직 DB에 테이블이 생긴 것은 아님

### 2. migrate

- `$ python manage.py migrate`
- “모델과 DB의 동기화”
- makemigrations로 만든 설계도를 실제 `db.sqlite3` DB 파일에 반영하는 과정
    - `db.sqlite3` 라는 파일로서 데이터베이스가 존재
    - migrate되었을 때 여기가 채워짐
    - 확인하기 위해서는 SQLite 확장프로그램 설치

<img width="878" alt="dj_42" src="https://user-images.githubusercontent.com/86648892/188498030-8a64362d-3739-4da3-9492-b437d28b90f6.png">

<img width="680" alt="dj_43" src="https://user-images.githubusercontent.com/86648892/188498032-d887ccc3-e126-4282-945c-c987c8eb34a5.png">

- migration 파일들의 특징은 앞에 숫자 4개가 붙는다
- `0001_initial` 외에 나머지는 무엇인가?
    - settings의 INSTALLED APPS에는 우리가 등록한 앱 외에 기본 내장 앱들이 있다
        - 이 앱들에 대한 설계도도 같이 migrate된 것이다
        - Django를 구동하기 위한 기본 내장 앱에 대한 설계도가 내부적으로 존재함
        - 처음 migrate할 때는 이 설계도를 같이 migrate함

### 기타 명령어

### 1. showmigrations

- `$ python manage.py showmigrations`
    - migrations 파일들이 migrate 됐는지 안됐는지 여부를 확인하는 용도
    - `[x]` 표시가 있으면 migrate가 완료되었음을 의미

### 2. sqlmigrate

- `$ python manage.py sqlmigrate articles 0001`
    - 해당 migrations 파일이 SQL문으로 어떻게 해석될지 미리 확인할 수 있음
    - 앱 이름, 설계도 번호 입력
    - `0001_initial.py` 파일은 파이썬으로 작성되어있는 것으로 이것이 migrate된다는 것은 무엇인가에 의해 DB에 저장되기 위해 SQL문으로 바뀌었다는 것이고, 이를 미리 확인해보기 위함

<img width="839" alt="dj_44" src="https://user-images.githubusercontent.com/86648892/188498034-73ba9285-8cf1-4e30-b506-829bb9eb39f4.png">

### 추가 필드 정의 (추가 migrations)

- `models.py` 에 변경사항이 생긴다면
    - 추가 모델 필드 작성 후 다시 한번 migrations 진행
- 추가 필드를 작성한다는 것은 기존의 테이블에 새로운 컬럼을 추가하는 상황
    - 이미 존재하는 테이블에 새로운 컬럼이 추가되는 상황에는 컬럼들을 빈 값인 상태로 추가할 수 없음
    - 추가되는 칼럼에 대한 기본값을 설정해야함
- 데이터베이스 원칙 중 무결성의 원칙
    - 빈 값을 데이터베이스에 추가할 수 없다
    - 기본값이 NOT NULL

<img width="1084" alt="dj_45" src="https://user-images.githubusercontent.com/86648892/188498035-9165adde-f2ba-4b0d-a6c3-dc2f45caf40b.png">

- (1)은 현재 이 대화에서 입력하는 값을 넣겠다
- (2)는 대화에서 나가서 코드상 default값을 넣어서 다시 makemigrations
- 1이 enter로 해결할 수 있기에 더 편하다
- 0002 설계도 확인
    - `dependencies` 에 0001 initial 설계도가 있음
        - 2번 설계도는 의존성이 있기에 1번 설계도가 있어야 의미가 있는 설계도
        - 만약 `models.py` 에 새로운 class를 생성하고 3번 설계도를 만든다면 다른 테이블이기에 의존성이 없음
- 설계도를 쌓아나가는 이유?
    - 모델이 망가졌을 때 망한 설계도를 버리고 잘 돌아갔던 시점에서 다시 누적하기 위함
- migrate를 통해 다시 반영

### MIGRATIONS 정리

1. `models.py` 변경: 데이터를 **구조화**하고 **조작**하기 위한 도구
2. 설계도 생성 (makemigrations)
3. 설계도 DB 반영 (migrate)

## CRUD with view functions

---

### 고려사항

- `GET` method는 Read(조회)에만 사용
    - `GET` 은 Query String Parameter로 데이터를 보내기에 url을 통해 데이터를 보냄
    - ex) `/articles/create/?title=11&content=22`
- Create(생성), Update(수정), Delete(삭제)과 같이 데이터 조작하는 경우 `POST` method
- 페이지에서 입력을 받아 데이터를 생성한 경우(Create)
    - 생성되었다는 페이지를 따로 render하지 말고 목록 페이지로 redirect
- 개별 게시글 상세 페이지(detail page)의 경우 개별 게시글마다 뷰 함수와 템플릿 파일을 만들 수 없음
    - 글의 번호(pk)를 활용하여 하나의 뷰 함수와 템플릿 파일로 대응
    - Variable Routing 활용

### 요구사항

- 목록을 나타내는 페이지(`index.html`), 새로운 데이터 생성 입력 페이지(`new.html`), 상세정보 페이지(`detail.html`), 정보수정 페이지(`edit.html`)
- 기능 (`views.py`)
    - index 페이지 렌더링
    - new 페이지 렌더링
    - new 페이지에서 받은 데이터 create
        - 그리고 상세정보 페이지로 redirect
    - detail 페이지 렌더링
        - edit 페이지로 이동하는 버튼
        - delete 버튼
    - edit 페이지 렌더링
        - 데이터 update

### `redirect()`

- `from django.shortcuts import redirect`
- 동작 원리 (하기 코드 참고)
    - 클라이언트가 create url로 요청을 보냄
        - create view 함수의 redirect 함수가 302 status code를 응답
        - 응답받은 브라우저는 redirect 인자에 담긴 주소(index)로 사용자를 이동시키기 위해 index url로 Django에 재요청
        - index page를 정상적으로 응답받음 (200 status code)

### HTTP response code

- 클라이언트에게 특정 **HTTP 요청이 성공적으로 완료되었는지 여부**를 알려줌

  - 5개의 응답 그룹

    1. Information responses (1xx)
    2. Successful responses (2xx)
    3. Redirection messages (3xx)
      - 302 Found
      - 해당 상태 코드를 응답받으면 브라우저는 사용자를 해당 URL의 페이지로 이동시킴
    4. Client error response (4xx)
      - 403 Forbidden
        - 서버에 요청이 전달되었지만, 권한때문에 거절되었다는 것을 의미
        - 서버에 요청은 도달했으나 서버가 접근을 거부할 때 반환됨
        - Django 입장에서 작성자가 누구인지 모르기에 함부로 작성할 수 없다는 의미
        - 모델(DB)을 조작하는 것은 단순 조회와 달리 최소한의 신원 확인이 필요
          - 즉, POST 요청을 할 때는 **CSRF Token**이 필요하다
            - **CSRF**
              - Cross-Site-Request-Forgery (사이트 간 요청 위조)
                - 사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여 특정 웹페이지를 보안에 취약하게 하거나 수정, 삭제 등의 작업을 하게 만드는 공격 방법 (2008년 옥션 해킹 사건)
            - **CSRF Token**
              - Security Token 사용 방식
                - 사용자의 데이터에 임의의 난수 값(token)을 부여해 매 요청마다 해당 난수 값을 포함시켜 전송시키도록 함
                - 이후 서버에서 요청을 받을 때마다 전달된 token값이 유효한지 검증
                - 일반적으로 데이터 변경이 가능한 `POST` , `PATCH` , `DELETE` Method 등에 적용
                - Django는 DTL에서 csrf_token 템플릿 태그를 제공 - `{% csrf_token %}` - 템플릿에서 내부 URL로 향하는 `POST` form을 사용하는 경우에 사용 - 해당 태그가 없으면 Django 서버는 요청에 대해 403 forbidden으로 응답 - 외부 URL로 향하는 `POST` form에 대해서는 CSRF 토큰이 유출되어 취약성을 유발할 수 있기에 사용하지 않음 - input type이 hidden으로 작성되며 value는 Django에서 생성한 hash 값으로 설정
                  <img width="1216" alt="dj_58" src="https://user-images.githubusercontent.com/86648892/188498066-84442092-876e-4b23-a2af-3ae4af4bc352.png">
    5. Server error responses (5xx)

- [HTTP CAT](https://http.cat/)
- [HTTP Status Codes](https://developer.mozilla.org/ko/docs/Web/HTTP/Status)

### HTTP request method

- HTTP는 request method를 정의하여
    - 주어진 리소스에 대해 수행하길 원하는 행동을 나타냄
- `GET`
    - 특정 리소스를 가져오도록 요청할 때 사용
    - 반드시 데이터를 가져올 때만 사용
    - DB에 변화를 주지 않음
    - CRUD 중 R 역할을 담당
    - ex) 검색
        - 검색은 서버에 영향을 미치는 것이 아닌 특정 데이터를 조회만 하는 요청
- `POST`
    - 서버로 데이터를 전송할 때 사용
    - 서버에 변경사항을 만듬
    - 리소스를 생성, 변경하기 위해 데이터를 **HTTP body**에 담아 전송
        - 개발자도구 - NETWORK 탭 - Payload 탭의 Form-Data 확인
    - `GET` 의 Query String Parameter와 다르게 **URL로 보내지지 않음**
    - CRUD 중 C, U, D 역할을 담당
    - ex) 로그인

### Code Snippets

<img width="1573" alt="dj_59" src="https://user-images.githubusercontent.com/86648892/188498067-bcb242bb-0f9e-4b7d-bb81-11361579a7a5.png">

### `/templates/base.html`

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx"
      crossorigin="anonymous"
    />
    <title>Document</title>
  </head>
  <body>
    {% block content %} {% endblock content %}

    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa"
      crossorigin="anonymous"
    ></script>
  </body>
</html>
```

### `/pjt02/urls.py`

```python
"""pjt02 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
]
```

### `/articles/models.py`

```python
from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 객체 출력용 메서드
    def __str__(self):
        return self.title
```

### `/articles/urls.py`

```python
from django.urls import path
from . import views

app_name = "articles"
urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
    path('<int:pk>/', views.detail, name="detail"),
    path('<int:pk>/delete/', views.delete, name="delete"),
    path('<int:pk>/edit/', views.edit, name="edit"),
    path('<int:pk>/update/', views.update, name="update"),
]
```

### `/articles/views.py`

```python
from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article(title=title, content=content)
    article.save()

    # detail url에 필요한 파라미터 pk를 같이 넘겨줌
    return redirect('articles:detail', article.pk)

# url로부터 pk를 잘라서 같이 보내줌
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }

    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()

    return redirect('articles:index')

# edit 템플릿을 보여주는 view
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/edit.html', context)

# 실제 데이터 수정
def update(request, pk):
    # 1. pk로 수정할 게시글을 가져온다
    article = Article.objects.get(pk=pk)
    # 2. request에서 사용자가 입력한 title과 content를 가져온다
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    # 3. DB에서 수정할 데이터로 조작한다
    article.save()
    # 4. 모든 조작이 끝나면 어디론가 보낸다
    return redirect('articles:detail', article.pk)
```

### `/articles/templates/articles/index.html`

```html
{% extends 'base.html' %} {% block content %}
<h1>Index 목록</h1>
<a href="{% url 'articles:new' %}">글 작성</a><br />
<hr />
{% for article in articles %}
<p>번호: {{ article.pk }}</p>
{% comment %} 위에 for문으로 들어온 article의 pk값을 적용한 detail이라는 이름의
url로 이동 {% endcomment %}
<a href="{% url 'articles:detail' article.pk %}">제목: {{ article.title }}</a>
<hr />
<br />
{% endfor %} {% endblock content %}
```

### `/articles/templates/articles/new.html`

```html
{% extends 'base.html' %} {% block content %}
<h1>글작성</h1>
<form action="{% url 'articles:create' %}" method="POST">
  {% csrf_token %}
  <label for="title">제목</label>
  <input type="text" name="title" id="title" /><br />

  <label for="content">내용</label>
  <textarea type="text" name="content" id="content"></textarea><br />

  <input type="submit" value="작성" /><br />

  <a href="{% url 'articles:index' %}">글 목록 보기</a>
</form>
{% endblock content %}
```

### `/articles/templates/articles/detail.html`

```html
{% extends 'base.html' %} {% block content %}
<h1>글 상세</h1>
<h3>{{ article.pk }}번째 글</h3>
<hr />
<p>제목: {{ article.title }}</p>
<p>내용: {{ article.content }}</p>
<p>생성시간: {{ article.created_at }}</p>
<p>수정시간: {{ article.updated_at }}</p>
<hr />

{% comment %} 단순히 수정 페이지로 이동하는 것이므로 a태그 사용 {% endcomment %}
<a href="{% url 'articles:edit' article.pk %}">수정</a>
{% comment %} delete url로 이동하면 -> views의 delete 호출 -> delete 함수가
index 페이지로 redirect {% endcomment %}
<form action="{% url 'articles:delete' article.pk %}" method="POST">
  {% csrf_token %}
  <input type="submit" value="삭제" />
</form>
<a href="{% url 'articles:index' %}">글 목록 보기</a>
{% endblock content %}
```

### `/articles/templates/articles/edit.html`

```html
{% extends 'base.html' %} {% block content %}
<h1>글 수정</h1>
<form action="{% url 'articles:update' article.pk %}" method="POST">
  {% csrf_token %}
  <label for="title">제목</label>
  {% comment %} value를 통해 넘겨받은 article의 title 채우기 {% endcomment %}
  <input type="text" name="title" id="title" value="{{article.title}}" /><br />

  <label for="content">내용</label>
  {% comment %} 넘겨받은 article의 content 채우기 {% endcomment %}
  <textarea type="text" name="content" id="content">
{{article.content}}</textarea
  ><br />

  <input type="submit" value="수정" /><br />
</form>
<a href="{% url 'articles:index' %}">글 목록 보기</a>
{% endblock content %}
```

## Admin Site

---

- **Django의 가장 강력한 기능 중 하나인 automatic admin interface**
- “관리자 페이지”
    - 사용자가 아닌 서버의 관리자가 활용하기 위한 페이지
    - 모델 class를 `admin.py` 에 등록하고 관리
    - 레코드 생성 여부 확인에 매우 유용하며 직접 레코드를 삽입할 수도 있음

### admin 계정 생성

- `$ python manage.py createsuperuser`
    - username과 password를 입력해 관리자 계정 생성
    - email은 선택사항이기에 입력하지 않고 enter를 입력하는 것이 가능
    - 비밀번호 생성 시 보안상 터미널에 입력되지 않으니 무시하고 입력을 이어가도록 함

### admin site 로그인

- `/admin/` 을 붙인 url로 접속 후 로그인

### admin에 모델 클래스 등록

- 모델의 record를 보기 위해서는 `admin.py`에 관리하고자 하는 모델 등록 필요

<img width="613" alt="dj_60" src="https://user-images.githubusercontent.com/86648892/188498087-00c8718b-fa96-44d5-8190-5ea3632ebd6b.png">

### 데이터 CRUD in admin

- admin 사이트에서 직접 CRUD 가능

### 정리

- Model
    - Django는 Model을 통해 데이터에 접속하고 관리
- ORM
    - 객체지향 프로그래밍을 이용한 DB 조작
- Migrations
    - 모델에 생긴 변화(필드 추가, 모델 삭제 등)를 DB에 반영하는 방법(과정)
