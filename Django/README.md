# Django

# Django Intro

- Django는 Full-stack Framework이다
    - Full-stack이란 프론트엔드와 백엔드를 합친 것
    - 즉, Django는 프론트와 서버 모두를 개발할 수 있는 프레임워크이다
        - 그러나 현업에서는 백엔드로만 주로 사용된다
    - 프론트엔드로는 자바스크립트 기반 프론트 프레임워크인 Vue.js를 많이 사용한다

### Framework란?

- 서비스 개발에 필요한 기능들을 미리 구현해서 모아놓은 것
- Frame + Work
    - 일정한 뼈대, 틀을 가지고 일하다
    - 제공받은 도구들과 뼈대, 규약을 가지고 무언가를 만드는 일
    - 특정 프로그램을 개발하기 위한 여러 도구들과 규약을 제공하는 것
    - “소프트웨어 프레임워크"는 복잡한 문제를 해결하거나 서술하는데 사용되는 기본 개념 구조
- 장점
    - 잘 사용하면 내가 만들고자 하는 본질(로직)에 집중하여 개발할 수 있음
    - 소프트웨어의 생산성과 품질을 높임

### Web Frameworks

- 2020 Github Stars 기준

<img width="364" alt="dj_1" src="https://user-images.githubusercontent.com/86648892/188303732-f321deca-c770-45eb-9599-74be2cbad55a.png">

<img width="364" alt="dj_2" src="https://user-images.githubusercontent.com/86648892/188303735-49e07db5-23c2-41e1-bca5-fbc7a561243e.png">

- Django의 장점
    - Django는 Python으로 작성된 프레임워크
        - Python이라는 언어의 강력함과 거대한 커뮤니티
    - 수많은 유용한 기능들
    - 검증된 웹 프레임워크
        - 화해, Toss, 두나무, 당근마켓, 요기요 등
            - 유명한 서비스들이 사용한다는 것은 곧 안정적인 서비스가 가능하다는 것

---

## WEB

### WWW(World Wide Web)

- 인터넷이란 전세계에 퍼져있는 거미줄같은 연결망
    - 실제로 해저케이블로 전세계는 연결되어 있음
        - Space X의 “스타링크 프로젝트"는 이러한 유선 연결을 넘어 무선 연결을 추구
- 인터넷을 이용한다는 것은 결국 전세계의 컴퓨터가 연결되어 있는 하나의 인프라를 이용하는 것

## 클라이언트와 서버

<img width="773" alt="dj_3" src="https://user-images.githubusercontent.com/86648892/188303737-89466c50-92bb-40ab-8c60-f802b075c2f9.png">

### 클라이언트

- 웹 사용자의 인터넷에 연결된 장치 (wi-fi에 연결된 컴퓨터 또는 모바일 등)
- Chrome 또는 Firefox와 같은 웹 브라우저
- ***서비스를 요청하는 주체***

### 서버

- 웹 페이지, 사이트 또는 앱을 저장하는 컴퓨터
- 클라이언트가 웹 페이지에 접근하려고할 때
    - 서버에서 클라이언트 컴퓨터로 웹 페이지 데이터를 응답해 사용자의 웹 브라우저에 표시됨
- ***요청에 대해 서비스를 응답하는 주체***

### 클라이언트-서버

- Google 홈페이지에 접속한다는 것은?
    - 클라이언트에서 인터넷에 연결되어 있는 구글 컴퓨터에게
        - Google 홈페이지 html 달라고 요청
            - 구글 컴퓨터는 요청에 따라 인터넷을 통해 html 반환
                - 반환받은 html 파일을 브라우저가 렌더링하여 보여줌
- 결국 어떠한 자원(resource)을 요청(request)하는 것은 클라이언트, 자원을 제공하는 쪽은 서버(server)
- 웹은 클라이언트-서버 구조
    - Django는 서버 구현에 사용됨

---

## Web browser와 Web page

### Web browser?

- 웹에서 **페이지를 찾아 보여주고**, **사용자가 하이퍼링크를 통해 다른 페이지로 이동**할 수 있도록 하는 프로그램
- 웹 페이지 파일을 우리가 보는 화면으로 렌더링(rendering)하는 프로그램

### Web page?

- 웹에 있는 문서로 우리가 보는 화면 하나하나가 웹 페이지

### Web page 종류

- 정적 웹 페이지
    - Static Web Page
    - 있는 그대로를 제공하는 것(served as-is)
    - 한 번 작성된 html 파일의 내용이 변하지 않고 모든 사용자에게 동일한 모습으로 전달되는 것
    - 서버에 미리 저장된 HTML 파일 그대로 전달된 웹 페이지
- 동적 웹 페이지
    - Dynamic Web Page
    - 사용자와 요청에 따라 웹 페이지에 추가적인 수정이 되어 클라이언트에게 전달되는 웹 페이지
        - 웹 페이지의 내용을 바꿔주는 주체가 서버(server)
            - 서버에서 동작하고 있는 프로그램이 웹 페이지를 변경해줌
    - ***사용자의 요청에 따라 적절한 응답을 만들어주는 프로그램***을 만들어야한다!
        - 파일을 처리하고, 데이터베이스와 상호작용
        - 이를 쉽게 할 수 있도록 도와주는 프레임워크가 Django

---

# MTV Design Pattern

## Design Pattern

- Design Pattern이란 자주 사용되는 구조가 있다는 것을 알게 되고, 이를 일반화해서 하나의 공법으로 만들어둔 것
- 소프트웨어에서의 Design Pattern
    - 설계 문제의 처리 과정에서의 유사점을 패턴이라 한다
    - 클라이언트-서버 구조도 소프트웨어 디자인 패턴 중 하나

## Design Pattern의 목적

- 특정 문맥에서 공통적으로 발생하는 문제에 대해 재사용 가능한 해결책 제시
- 프로그래머가 어플리케이션이나 시스템을 디자인할 때 발생하는 공통된 문제들을 해결하는데 형식화된 가장 좋은 관행
- 커뮤니케이션이 간단해짐
    - “우리 이거 클라이언트-서버 구조로 개발하자”
    - 다수의 엔지니어들이 일반화된 패턴으로 소프트웨어 개발을 할 수 있도록 한 규칙, 커뮤니케이션의 효율성을 높이는 기법

---

## MTV Design Pattern

- Model - Template - View
- Django에서의 디자인 패턴
- MVC 디자인 패턴을 기반으로 조금 변형된 패턴

### MVC 디자인 패턴

- Model - View- Controller
- 데이터 및 논리 제어를 구현하는데 널리 사용되는 소프트웨어 디자인 패턴
- 하나의 프로그램을 3가지 역할로 구분한 개발 방법론
    1. Model: 데이터와 관련된 로직을 관리
    2. View: 레이아웃과 화면을 처리
    3. Controller: 명령을 model과 view부분으로 연결

### MVC 디자인 패턴의 목적

- “관심사 분리”
- 더 나은 업무의 분리와 향상된 관리 제공
- 각 부분을 독립적으로 개발할 수 있어, 하나를 수정하고 싶을 때 모두 건들지 않아도 됨
    - 개발 효율성 및 유지보수가 쉬워짐
    - 다수의 멤버로 개발하기 용이함

## MTV 디자인 패턴

<img width="1084" alt="dj_4" src="https://user-images.githubusercontent.com/86648892/188303738-cf774953-b658-492a-950c-445c3ad2600d.png">

### Model

- 데이터와 관련된 로직을 관리
- 프로그램의 ***데이터 구조를 정의***하고, ***데이터베이스의 기록을 관리***

### Template

- 레이아웃과 화면을 처리
- 화면상의 사용자 인터페이스 구조와 레이아웃을 정의

### View

- Model, Template과 관련한 로직을 처리해서 응답을 반환
- 클라이언트의 요청에 대해 처리를 분기하는 역할
    - Request → URL 주소를 보고 어디로(Template) 요청을 보내야할지 판단 → View가 필요한 데이터가 있을 시 Model과 소통 → Model에서 데이터를 가져오고 → 해당 Template으로 보내 화면을 구성하고 → 구성된 화면을 응답으로 클라이언트에게 반환
- 중간처리와 응답반환을 한다고 생각하면 된다

<img width="700" alt="dj_5" src="https://user-images.githubusercontent.com/86648892/188303740-506ea720-0375-42cf-94b8-6b8fbe43791d.png">

---

# Django 환경설정

- ***설치 전 가상환경 설정 및 활성화를 마치고 진행***

## Virtual Environment

### 가상환경 설정

- `python -m venv venv`
    - 가상환경을 만들 것(-m venv)이고 그 이름은 venv
- `source ./venv/Scripts/activate`
    - 가상환경 활성화
    - 맥에서는 venv의 하위 폴더로 bin이 잡혀있는 경우가 있으므로 확인
        - `source venv/bin/activate`
        - 맥 가상환경의 경우 pyenv 사용을 알아보자

## Package

### 패키지 설치

- `$ pip list`
    - 현재 가상환경 내 설치된 모듈 확인
- `$ pip install`
    - `$ pip install django==3.2.13`
        - Django 설치
            - Django와 Django에 필요한 다른 것들도 설치되었음을 확인 가능
        - Django 4.0 릴리즈로 인해 3.2(LTS) 버전을 명시해서 설치
            - LTS(Long Term Support)란 장기 지원 버전으로, 일반적인 경우보다 장기간에 걸쳐 지원하도록 고안된 소프트웨어의 버전
                - 컴퓨터 소프트웨어의 제품 수명주기 관리 정책
                - 배포자는 LTS 확정을 통해 장기적이고 안정적인 지원을 보장함
    - `$ pip install ipython`
    - `$ pip install django-extensions`
        - `settings.py` 의 `INSTALLED_APPS`에 `django_extensions` 추가 필수!
            - 추가할 때 언더바인점 주의

### 패키지 목록 생성

- `pip freeze > requirements.txt`
    - `pip install -r requirements.txt`
        - 현재 있는 `requirements.txt` 파일을 바탕으로 recursive하게 패키지를 다운받아줄 것이다

## Project

### 프로젝트 생성

- `$ django-admin startproject firstpjt .`
    - `.` 은 현재 디렉토리를 의미하는 것으로 현재 디렉토리 내에 바로 프로젝트 디렉토리를 생성하게 됨
        - 붙이지 않는다면 `firstpjt` 라는 이름의 껍데기 폴더가 생성되고 그 안에 프로젝트 디렉토리가 생성되어 불편함
    - 프로젝트 이름에는 Python이나 Django에서 사용 중인 키워드 및 ‘-’(하이픈) 사용 불가

### 서버 실행

- `python manage.py runserver`
    - url을 `ctrl+클릭` 하면 로켓화면 확인가능
    - 서버종료는 `ctrl+c`

### 프로젝트 구조

<img width="439" alt="dj_6" src="https://user-images.githubusercontent.com/86648892/188303741-32b2ad55-9c0e-4b45-bf61-9fedbfcf3157.png">

- `manage.py`
    - Django 프로젝트 전반에 대한 명령을 내릴 수 있는 파일
    - Django 프로젝트와 다양한 방법으로 상호작용하는 커맨드라인 유틸리티
    - `$ python manage.py <command> [options]`
- `firstpjt`
    - `__init__.py`
        - 패키지로 인식시키는 파일
        - Python에게 이 디렉토리를 하나의 Python 패키지로 다루도록 지시
        - 별도로 추가 코드를 작성하지 않음
    - `asgi.py`
        - Asynchronous Server Gateway Interface
        - Django 애플리케이션이 비동기식 웹 서버와 연결 및 소통하는 것을 도움
        - 추후 배포 시에 사용
    - `settings.py`
        - Django 프로젝트 전반에 대한 설정을 관리
        - `SECRET_KEY` 는 프로젝트 고유 키 값
    - `urls.py`
        - 사이트의 url과 적절한 views의 연결을 지정
        - `urlpatterns` 에 어떤 url이 들어오면 어떤 처리를 하라는 것을 지정
    - `wsgi.py`
        - Web Server Gateway Interface
        - Django 애플리케이션이 웹 서버와 연결 및 소통하는 것을 도움
        - 추후 배포 시에 사용
- `db.sqlite3`
    - 향후 데이터베이스 생성 시 생성됨
    - 데이터베이스
        - 데이터가 들어있는 곳

## Application

### 어플리케이션 생성

- 프로젝트 내에 기능 단위로 여러 개의 앱이 들어갈 수 있다
    - ex) 회원 관련, 게시글 관련, 결제 관련 등등
    - 싱글앱, 멀티앱은 개발방식 선호의 차이
- `$ python manage.py startapp articles`
    - articles라는 앱을 만든다
    - 일반적으로 어플리케이션의 이름은 ‘복수형'으로 작성하는 것을 권장
- `settings.py` 의 `INSTALLED_APPS` 에 추가
    - 참고) third party apps는 `pip install` 해서 받은 것들

### 어플리케이션 구조

<img width="372" alt="dj_7" src="https://user-images.githubusercontent.com/86648892/188303742-c9b71a00-766d-4b85-ac78-45d870ac1cd1.png">

- `admin.py`
    - 관리자용 페이지를 설정하는 곳
- `apps.py`
    - 앱의 정보가 작성된 곳
    - 별도로 추가 코드를 작성하지 않음
- `models.py`
    - 애플리케이션에서 사용하는 Model을 정의하는 곳
    - MTV 패턴의 M에 해당
- `tests.py`
    - 프로젝트의 테스트 코드를 작성하는 곳
- `views.py`
    - view 함수들이 정의되는 곳
    - MTV 패턴의 V에 해당
- `migrations`
    - 데이터베이스 변경 히스토리가 모여있는 곳

### 어플리케이션 등록

<img width="567" alt="dj_8" src="https://user-images.githubusercontent.com/86648892/188303743-da8633ea-d299-4e17-bf30-57f9e7ab564d.png">

- 프로젝트에서 앱을 사용하기 위해서는 반드시 `INSTALLED_APPS` 리스트에 추가해야 함
    - `INSTALLED_APPS`는 Django Installation에 활성화된 모든 앱을 지정하는 문자열 목록
- 반드시 생성 후 등록
    - `INSTALLED_APPS` 에 먼저 작성하고 생성하려면 앱이 생성되지 않음

<img width="509" alt="dj_9" src="https://user-images.githubusercontent.com/86648892/188303744-d3d96988-9fc3-424c-a058-5785353e6d7f.png">

- Local apps - Third party apps - Django apps 순서
    - 해당 순서를 지키지 않아도 당장은 문제가 없으나, 추후 advanced한 내용을 다룰 시를 대비하여 지키는 것을 권장

## Project & Application 정리

### Project

- “collection of apps”
- 프로젝트는 앱의 집합
- 프로젝트에는 여러 앱이 포함될 수 있음
- 앱은 여러 프로젝트에 있을 수 있음

### Application

- 앱은 실제 요청을 처리하고 페이지를 보여주는 등의 역할을 담당
- 일반적으로 앱은 하나의 역할 및 기능 단위로 작성하는 것을 권장함

---

# 요청과 응답

- 설계 순서
    1. url 설계
    2. 그에 맞는 view 설계
    3. model, template 설계

### URLs

<img width="457" alt="dj_10" src="https://user-images.githubusercontent.com/86648892/188303745-71b9698d-1198-4d96-8622-806058623eff.png">

- `path('index/', views.index)`
    - index라는 경로로 들어오면 views에 있는 기능을 수행해주면 된다는 명령
    - `views.index` 를 사용하기 위해 `from articls import views` 필요

### View

<img width="491" alt="dj_11" src="https://user-images.githubusercontent.com/86648892/188303747-52599cb4-44be-4bf7-8c68-42c10296c0ba.png">

- browser의 url → `urls.py` → `views.py` → `index()`
    - `index(request)` 내의 request 파라미터에 django가 알아서 request를 넣어서 넘겨줌
- HTTP 요청을 수신하고 HTTP 응답을 반환하는 함수 작성
- Template에게 HTTP 응답 서식을 맡김

<img width="998" alt="dj_12" src="https://user-images.githubusercontent.com/86648892/188303748-1570ac25-78dc-41ff-8bce-16d976ca4bc8.png">

- `templates` 디렉토리 생성 및 `index.html` 파일 생성
- `return render(request, 'index.html')`
    - 해당 request에 대하여 index.html파일을 렌더링해줘
    - context는 data라고 생각하자
    - `settings.py` 에 TEMPLATES
        - 여기에 `APP_DIRS` 에 `True` 가 기본값으로 설정되어있어 articles 앱 내부의 template을 인식할 수 있음
        - ***그 외 따로 디렉토리를 만들어 인식시켜주고 싶을 경우 `DIRS`에 정의***

### Templates

<img width="481" alt="dj_13" src="https://user-images.githubusercontent.com/86648892/188303749-f15779c7-5b32-40d2-847d-aff5f28ee02f.png">

- 실제 내용을 보여주는데 사용되는 파일
- 파일의 구조나 레이아웃을 정의
- `app_name/templates/`
    - 템플릿 폴더의 이름은 반드시 **templates**라고 지정해야함

### 코드 작성 순서

<img width="1054" alt="dj_14" src="https://user-images.githubusercontent.com/86648892/188303752-ae37cfb7-5802-44f0-b0af-16d3724df1b4.png">

---

## 추가 설정

- `settings.py` 에서 설정

### LANGUAGE_CODE

- 모든 사용자에게 제공되는 번역을 결정
- 이 설정이 적용되려면 `USE_I18N` 이 활성화(True)되어 있어야함
- [Unicode Language Identifiers](http://www.i18nguy.com/unicode/language-identifiers.html)

### TIME_ZONE

- 데이터베이스 연결의 시간대를 나타내는 문자열 지정
- `USE_TZ` 가 True이고 이 옵션이 설정된 경우 데이터베이스에서 날짜 시간을 읽으면, UTC 대신 새로 설정한 시간대의 인식 날짜&시간이 반환됨
- `USE_TZ` 가 False인 상태로 이 값을 설정하는 것은 error가 발생하므로 주의
- [List of TZ Database Time Zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)

### USE_I18N

- Django의 번역 시스템을 활성화해야하는지 여부를 지정

### USE_L10N

- 데이터의 지역화된 형식(localized formatting)을 기본적으로 활성화할지 여부를 지정
- True일 경우, Django는 현재 locale의 형식을 사용하여 숫자와 날짜를 표시

### USE_TZ

- datetimes가 기본적으로 시간대를 인식하는지 여부를 지정
- True일 경우 Django는 내부적으로 시간대 인식 날짜 / 시간을 사용

## 유용한 VSCode Extensions

- Django
- Excel Viewer
- SQLite
- Material Icon Theme

---

# Django Template

## Django Template

- Template System의 기본 목표를 숙지하자
    - ***데이터 표현을 제어하는 도구이자 표현에 관련된 로직***
    - Django Template을 이용한 HTML 정적 부분과 동적 컨텐츠 삽입

## DTL(Django Template Language)

- Django template에서 사용하는 built-in template system
    - html 파일을 조금 더 쉽게 만들어주는 Django만의 문법
        - 실무에서는 잘 사용하지 않는다
- 조건, 반복, 변수 치환, 필터 등의 기능을 제공
    - Python처럼 일부 프로그래밍 구조(if, for 등)를 사용할 수 있지만 이것은 ***Python 코드로 실행되는 것이 아님***
    - Django 템플릿 시스템은 단순히 Python이 아닌 HTML에 포함된 것이 아니니 주의
- 프로그래밍적 로직이 아니라 프레젠테이션을 표현하기위한 것임을 명심할 것

## DTL Syntax

### Variable

- `{{ variable }}`
    - 변수명은 영어, 숫자와 밑줄(`_`)의 조합으로 구성될 수 있으나 밑줄로는 시작할 수 없음
        - 공백이나 구두점 문자 또한 사용할 수 없음
    - `.` 을 사용하여 변수 속성에 접근할 수 있음
    - `render()` 의 세번째 인자로 `{'key': value}` 와 같이 딕셔너리 형태로 넘겨주며, 여기서 정의한 key에 해당하는 문자열이 template에서 사용가능한 변수명이 됨
        - `views` 에의 함수 내에서 `models` 로부터 받아온 데이터를 바탕으로 ,보통 `context` 라는 이름으로 딕셔너리를 정의하여 이 정보를 연결된 `templates` 파일에 넘겨줌

### Filters

- `{{ variable|filter }}`
    - 표시할 변수를 수정할 때 사용
    - 예시
        - `{{ name|lower }}`
            - name 변수를 모두 소문자로 출력
    - 60개의 built-in template filters를 제공
    - chained가 가능하며 일부 필터는 인자를 받기도 함
        - `{{ name|truncateworkds:30 }}`

### Tags

- `{% tag %}`
    - 출력 텍스트를 만들거나, 반복 또는 논리를 수행하여 제어 흐름을 만드는 등 변수보다 복잡한 일들을 수행
    - 일부 태그는 시작과 종료 태그가 필요
        - `{% if %} {% endif %}`
    - 약 24개의 built-in template tags를 제공

### Comments

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

---

## Trailing URL Slashes (참고)

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

---

## Template Interitance

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

---

# Sending and Retrieving form data

### `<form></form>`

- form 태그
- WEB에서 사용자 Input을 받는 방법
- `<form target="_blank">`
    - 새 탭에서 열기

## Client & Server Architecture

<img width="522" alt="dj_22" src="https://user-images.githubusercontent.com/86648892/188303762-08c454f8-1b8a-4944-b929-55c18658df79.png">

- 웹은 기본적으로 클라이언트-서버 아키텍처를 사용
    - 클라이언트(일반적으로 웹 브라우저)가 서버에 요청을 보내고, 서버는 클라이언트의 요청에 응답
- 클라이언트 측에서 ***HTML form***은 HTTP 요청을 서버에 보내는 가장 편리한 방법
- 이를 통해 ***사용자는 HTTP 요청에서 전달할 정보를 제공***할 수 있음

## Sending form data (Client)

### HTML <form> element

- 데이터가 전송되는 방법을 정의
- 웹에서 사용자 정보를 입력하는 여러 방식(text, button, submit 등)을 제공하고, ***사용자로부터 할당된 데이터를 서버로 전송***하는 역할을 담당
- “데이터를 어디(action)로 어떤 방식(method)으로 보낼지”
    - 핵심 속성
        - action
        - method

### HTML form’s attributes

1. ***action***
    - 입력 데이터가 전송될 URL을 지정
    - 데이터를 어디로 보낼 것인지 지정하는 것이며 이 값은 반드시 유효한 URL이어야함
    - 만약 이 속성을 지정하지 않으면 데이터는 현재 form이 있는 페이지의 URL로 보내짐
2. ***method***
    - 데이터를 어떻게 보낼 것인지 정의
    - 입력 데이터의 HTTP request methods를 지정
        - HTML form 데이터는 GET, POST 2가지 방법으로만 전송할 수 있음
        - READ 시 `GET`
        - CREATE, UPDATE, DELETE 시 `POST`
    - 정의하지 않을 시 기본값 GET 적용

### HTML <input> element

- 사용자로부터 데이터를 입력받기 위해 사용
- `type` 속성에 따라 동작 방식이 달라짐
    - input 요소의 동작 방식은 type 특성에 따라 현격히 달라지므로 MDN 문서 참고하여 사용
    - 지정하지 않은 경우 기본값은 text
- <label>과 주로 함께 사용하여 label의 `for` 과 input의 `id` 가 연결
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
        - 서버로부터 정보를 ***조회***하는데 사용
            - 즉, 서버에게 리소스를 요청하기 위해 사용
        - ***데이터를 가져올 때만 사용해야함***
        - ***데이터를 서버로 전송할 때 Query String Parameters를 통해 전송***
            - 데이터는 URL에 포함되어 서버로 보내짐

### Query String parameters

- 사용자가 입력 데이터를 전달하는 방법 중 하나
    - URL 주소에 데이터를 파라미터를 통해 넘기는 것
- 앰퍼샌드(`&`)로 연결된 `key=value` 쌍으로 구성되며, 기본 URL과 물음표(`?`)로 구분됨
    - 정해진 주소 이후에 물음표를 쓰는 것으로 Query String이 시작함을 알림
    - `=` 로 key와 value가 구분됨
    - 파라미터가 여러 개일 경우 `&` 를 붙여 여러 개의 파라미터를 넘길 수 있음

## Retrieving the data (Server)

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

---

# Variable Routing

- URL 주소를 변수로 사용하는 것을 의미
    - URL의 일부를 변수로 지정하여 view 함수의 인자로 넘길 수 있음
        - 즉, 변수 값에 따라 하나의 `path()` 에 여러 페이지를 연결시킬 수 있음
- Routing(라우팅)이란 어떤 네트워크 안에서 통신 데이터를 보낼 때 최적의 경로를 선택하는 과정을 뜻함
- `<type: name>`
    - 변수는 `<>` 에 정의하며 view 함수의 인자로 할당됨
    - type이 적혀있지 않다면 str이 기본값
        - str
        - int
        - slug
        - uuid
        - path

<img width="618" alt="dj_27" src="https://user-images.githubusercontent.com/86648892/188303770-8fac5cfd-208c-445f-ad4e-15dc713c4f22.png">

<img width="614" alt="dj_28" src="https://user-images.githubusercontent.com/86648892/188303771-dd92a0d1-2049-45e9-97af-b3d8998fab91.png">

<img width="498" alt="dj_29" src="https://user-images.githubusercontent.com/86648892/188303772-17be78b7-95df-4fd5-a4ba-9e12ebda86cc.png">

---

# App URL Mapping

- 앱이 많아졌을 때 `urls.py` 를 각 app에 매핑하는 방법
    - app의 view 함수가 많아지면서 사용하는 `path()` 가 많아지고, app 또한 더 많이 작성되기에 프로젝트의 `urls.py` 에서 모두 관리하는 것은 프로젝트 유지보수에 좋지 않음
- `python manage.py startapp pages`
    - pages 앱 생성
        - `settings.py` → `INSTALLED_APPS` 에 pages 추가
- `include()` 를 통해 분기 처리
    - `path('articles/', include('articles.urls'))`
        - `articles/` 로 끝나는 것을 보자마자 `include` 내에 있는 것으로 위임

<img width="1077" alt="dj_30" src="https://user-images.githubusercontent.com/86648892/188303773-67782775-c171-4dd4-867d-d8e9b41e586c.png">

<img width="1181" alt="dj_31" src="https://user-images.githubusercontent.com/86648892/188303774-4964b1bb-b41a-40c3-a3df-861afa81aa7b.png">

<img width="864" alt="dj_32" src="https://user-images.githubusercontent.com/86648892/188303775-20940db2-319d-4b7a-8647-a62a22ab5d7f.png">

---

# Naming URL patterns

- 분기된 url 주소를 모두 하나하나 주소를 바꿔줘야 하는가?
- 너무 번거롭다
- 각 url 주소에 이름을 붙여주자

## Naming URL patterns

- `path()` 함수의 `name` 인자 활용
    - 정의된 `name` 은 향후 `{% url ' ' %}` DTL 태그를 활용하여 접근 가능
        - 주어진 URL 패턴 이름 및 선택적 매개 변수와 일치하는 절대경로 주소를 반환
        - 템플릿에 URL을 하드코딩하지 않고도 DRY 원칙을 위반하지 않으면서 링크를 출력

<img width="1144" alt="dj_33" src="https://user-images.githubusercontent.com/86648892/188303776-1993e49d-fc2c-4f50-bfe0-f09fee1501d4.png">

<img width="1169" alt="dj_34" src="https://user-images.githubusercontent.com/86648892/188303778-9e0d4410-9028-4c04-84d1-2a94ce890dcf.png">

---

## Django의 설계 철학 (Templates System)

1. “표현과 로직(view)을 분리”
    - 템플릿 시스템은 표현을 제어하는 도구이자 표현에 관련된 로직일 뿐
        - 즉, 템플릿 시스템은 이러한 기본 목표를 넘어서는 기능을 지원하지 말아야함
2. “중복을 배제”
    - 대다수의 동적 웹사이트는 공통 header, footer, navbar 같은 사이트 공통 디자인 가짐
    - Django 템플릿 시스템은 이러한 요소를 한 곳에 저장하기 쉽게하여 중복코드를 없애야함
    - 템플릿 상속의 기초가 되는 철학

## Framework의 성격

- 독선적(Opinionated)
    - 독선적인 프레임워크들은 어떤 특정 작업을 다루는 ‘올바른 방법'에 대한 분명한 의견(규약)을 가지고 있음
    - 대체로 특정 문제 내에서 빠른 개발 방법을 제시
    - 어떤 작업에 대한 올바른 방법이란 보통 잘 알려져 있고 문서화가 잘 되어있기 때문
    - 하지만 주요 상황을 벗어난 문제에 대해서는 그리 유연하지 못한 해결책을 제시할 수 있음
- 관용적(Unopinionated)
    - 관용적인 프레임워크들은 구성 요소를 한데 붙여서 해결해야 한다거나 심지어 어떤 도구를 써야한다는 ‘올바른 방법'에 대한 제약이 거의 없음
    - 이는 개발자들이 특정 작업을 완수하는데 가장 적절한 도구들을 이용할 수 있는 자유도가 높음
    - 하지만 개발자 스스로 그 도구들을 찾아야한다는 수고가 필요

## Django Framwork의 성격

- ‘다소 독선적’
    - 양쪽 모두에게 최선의 결과를 준다고 강조
- 결국 하고자 하는 말은 현대 개발에 있어서 가장 중요한 것들 중 하나는 ***‘생산성’***
- 프레임워크는 우리가 하는 개발을 방해하기위해 규칙, 제약을 만들어놓은 것이 아님
- 우리가 온전히 만들고자하는 것에만 집중할 수 있게 도와주는 것
- “수레바퀴를 다시 만들지말라”

---

# Namespace

- 이름 중복을 쉽게 구분 및 접근하기 위한 구조 설계
- URL Namespace
    - `articles` 앱과 `pages` 앱에 동일하게 path(`index/` )라는 url이 있다면?
        - `app_name` 및 `path()` 의 `name` 속성으로 해결
- Template Namespace
    - `articles` 앱과 `pages` 앱에 동일하게 `index.html` 이 있다면?
        - 샌드위치 구조로 해결

## URL namespace

- URL namespace를 사용하면 서로 다른 앱에서 동일한 URL 이름을 사용하는 경우에도 이름이 지정된 URL을 고유하게 사용할 수 있음
- `app_name` attribute을 작성해 URL namespace를 설정

<img width="867" alt="dj_35" src="https://user-images.githubusercontent.com/86648892/188497998-0edf4015-89aa-4e73-a3a7-cffcde25faab.png">

- `{% url 'app_name: url_name' %}`
    - app name을url 태그도 바뀌어야 함
        - url 참조는 `:` 연산자를 통해 지정
    - app name을 정의한 순간 url name에 app name을 빼고 호출하면 NoReverseMatch 발생
        - NoReverseMatch 발생하면 url 태그만 찾아보면 된다

<img width="1209" alt="dj_36" src="https://user-images.githubusercontent.com/86648892/188498007-82fbf91f-feb9-40c3-828e-61250b6a18e7.png">

## Template namespace

- Django는 기본적으로 `app_name/templates/` 경로에 있는 templates 파일들만 찾을 수 있으며, `settings.py` 의 INSTALLED_APPS에 작성한 app 순서로 template을 검색 후 렌더링함
    - `settings.py` 의 TEMPLATES 내부 `APP_DIRS: True` 가 해당 경로를 활성화하고 있음
    - 쉽게 말해 등록된 앱들 중 같은 이름의 템플릿이 있을 경우 앱 순서에 따라 먼저 등록된 것을 렌더링
- Django templates의 기본 경로 자체를 변경할 수는 없기에 물리적으로 이름 공간을 만든다
- 하위 디렉토리 경로를 하나 더 줘서 샌드위치 구조로 templates 경로를 재설정
    - `app_name/templates/app_name`

<img width="1151" alt="dj_37" src="https://user-images.githubusercontent.com/86648892/188498013-b999a577-cc83-4e34-a4ba-a6b3e7b96962.png">

---

# Database

- 데이터베이스란 무엇인가?
    - 체계화된 데이터의 모임
    - 검색 및 구조화같은 작업을 보다 쉽게하기 위해 조직화된 데이터를 수집하는 저장 시스템

## Database의 구조

1. ***스키마 (Schema)***
    - 뼈대
    - 데이터베이스에서 자료의 구조, 표현 방법, 관계 등을 정의한 구조
    
    <img width="404" alt="dj_38" src="https://user-images.githubusercontent.com/86648892/188498017-d0daf2cb-5752-425b-ac49-88c12eefc995.png">
    
2. ***테이블 (Table)***
    - 필드(field)와 레코드(record)를 사용해 조직된 데이터 요소들의 집합
        - 필드(field)
            - 속성, 컬럼(Column)
            - 각 필드에는 고유한 데이터 타입이 지정됨
                - INT, TEXT 등
        - 레코드(record)
            - 튜플, 행(Row)
            - 테이블의 데이터는 레코드에 저장됨
                - ex) 4명의 고객정보가 있을 시 레코드는 4개가 존재
    - 관계(Relation)라고도 부름
    
    <img width="780" alt="dj_39" src="https://user-images.githubusercontent.com/86648892/188498020-0db68358-fd0a-49d3-970a-3b65a7712dfe.png">
    
- 데이터베이스는 결국 수많은 테이블들의 모음
    - 사용자들의 회원정보, 게시글 등등의 여러 테이블 모음

## Primary Key (PK)

- 기본 키
- 각 레코드의 고유한 값
- 기술적으로 ***다른 항목과 절대로 중복되어 나타날 수 없는 단일값(unique)***을 가짐
- 데이터베이스 관리 및 테이블 간 관계 설정 시 주요하게 활용됨

## Query

- 데이터를 조회하기 위한 명령어
    - 데이터 처리를 “문의”
- 조건에 맞는 데이터를 추출하거나 조작하는 명령어 (주로 테이블형 자료구조에서)
- 쿼리를 날린다는 곧 데이터베이스를 조작한다는 것

---

# Model

- Django는 웹 어플리케이션의 데이터를 구조화하고 조작하기 위한 모델을 제공함
    - Model을 사용하지 않고는 데이터를 저장할 수 없음
        - Model을 통해 데이터에 접속하고 관리
- 단일한 데이터에 대한 정보를 가짐
- 사용자가 저장하는 데이터들의 필수적인 필드들과 동작들을 포함
- 저장된 데이터베이스의 구조(layout)
- **일반적으로 각각의 모델은 하나의 데이터베이스 테이블에 매핑(mapping)**
    - **모델 클래스 1개 == 데이터베이스 테이블 1개**

<img width="1046" alt="dj_40" src="https://user-images.githubusercontent.com/86648892/188498024-f64a025e-c1a1-43a8-8c29-058eb07120c4.png">

## `models.py`

- 모델 클래스를 작성하는 것은 ***데이터베이스 테이블의 스키마를 정의***하는 것
    - 모델 클래스 == 테이블 스키마
- 장고의 모델과 데이터베이스가 같은 것은 아니다
    - 장고에서 제공하는 모델을 통해 데이터베이스에 간접적으로 소통
    - View에서 1번 데이터 줘 → Model에서 Database한테 1번 데이터 내놔 → 받고 → View로 돌려줌

```python
from django.db import models

# Create your models here.
# 내가 원하는 데이터베이스의 스키마 구조를 정의한 것
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 객체 출력용 메서드
    def __str__(self):
        return self.title
```

- `id` 컬럼은 테이블 생성 시 Django가 자동으로 생성
- 각 모델은 `django.models.Model` 클래스의 서브클래스로 표현됨
    - 즉, 각 모델은 `django.models.Model` 클래스를 상속받음
        - 클래스 상속 기반 형태의 Django 프레임워크 개발
- 클래스 변수명
    - `title`, `content`
        - DB 필드를 나타냄
- 클래스 변수값
    - `models.CharField()` , `models.TextField()`
        - DB 필드의 데이터 타입을 나타냄

## Django Model Field

- Django는 모델 필드를 통해 테이블의 필드(컬럼)에 저장할 데이터 유형을 정의
    - [Django Model Fields](https://docs.djangoproject.com/en/4.1/ref/models/fields/)
- 데이터 유형에 따라 다양한 모델 필드를 제공

### `CharField(max_length=None, **options)`

- 길이의 제한이 있는 문자열을 넣을 때 사용
- `max_length`
    - 필드의 최대 길이(문자)
    - CharField의 필수 인자
    - 데이터베이스와 Django의 유효성 검사에서 활용됨
        - 사용자는 말을 듣지 않는다
            - 유효성 검사가 필요

### `TextField(**options)`

- 글자의 수가 많을 때 사용
- `max_length` 옵션 작성 시 입력 단계에서는 반영되지만, 모델과 데이터베이스 단계에서는 적용되지 않음
    - 실제로 저장될 때 길이에 대한 유효성을 검증하지 않음
    - 쉽게 말해, 의미가 없다

### `DateTimeField()`

- Python의 datetime.datetime 인스턴스로 표시되는 날짜 및 시간을 값으로 사용하는 필드
- `DateField()` 를 상속받는 클래스
- 선택 인자
    - `auto_now_add`
        - 최초 생성 일자 (Useful for creation of timestamps)
        - Django ORM이 최초 insert(테이블에 데이터 입력)시에만 현재 날짜와 시간으로 갱신
            - 테이블에 어떤 값을 최초로 넣을 때
    - `auto_now`
        - 최종 수정 일자 (Useful for “last-modified” timestamps)
        - Django ORM이 save를 할 때마다 현재 날짜와 시간으로 갱신

---

# Migrations

- 작성한 모델의 클래스를 실제 데이터베이스에 반영하는 과정
- `models.py` 에서 작성한 것이 테이블의 스키마라고 할 때, DB에 직접 만들 테이블의 설계도가 migrations 파일들
    - `$ python manage.py makemigrations`
        - 실제로 DB에 옮길 설계도 생성
    - `$ python manage.py migrate`
        - 해당 설계도 파일을 바탕으로 DB에 동기화

## makemigrations

- `$ python manage.py makemigrations`
- 모델을 작성 혹은 변경한 것에 기반한 새로운 migration(설계도, 청사진, 혹은 마이그레이션)을 만들 때 사용
- “테이블을 만들기 위한 설계도를 생성하는 것”

<img width="918" alt="dj_41" src="https://user-images.githubusercontent.com/86648892/188498027-7bf335ed-b7c3-4284-8067-50fae4812ba6.png">

- `migrations/0001_initial.py` 모습
    - “파이썬으로 작성된 최종 설계도”
        - blueprint
        - 아직 DB에 테이블이 생긴 것은 아님

## migrate

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

## 기타 명령어

### showmigrations

- `$ python manage.py showmigrations`
    - migrations 파일들이 migrate 됐는지 안됐는지 여부를 확인하는 용도
    - [X] 표시가 있으면 migrate가 완료되었음을 의미

### sqlmigrate

- `$ python manage.py sqlmigrate articles 0001`
    - 해당 migrations 파일이 SQL문으로 어떻게 해석될지 미리 확인할 수 있음
    - 앱 이름, 설계도 번호 입력
    - `0001_initial.py` 파일은 파이썬으로 작성되어있는 것으로 이것이 migrate된다는 것은 무엇인가에 의해 DB에 저장되기 위해 SQL문으로 바뀌었다는 것이고, 이를 미리 확인해보기 위함

<img width="839" alt="dj_44" src="https://user-images.githubusercontent.com/86648892/188498034-73ba9285-8cf1-4e30-b506-829bb9eb39f4.png">

---

## 추가 필드 정의 (추가 migrations)

- `models.py` 에 변경사항이 생긴다면
    - 추가 모델 필드 작성 후 다시 한번 migrations 진행
- 추가 필드를 작성한다는 것은 기존의 테이블에 새로운 컬럼을 추가하는 상황
    - 이미 존재하는 테이블에 새로운 컬럼이 추가되는 상황에는 컬럼들을 빈 값인 상태로 추가할 수 없음
    - 추가되는 칼럼에 대한 기본값을 설정해야함
- 데이터베이스 원칙 중 무결성의 원칙
    - 빈 값을 데이터베이스에 추가할 수 없다
        - 기본값이 NOT NULL

<img width="1084" alt="dj_45" src="https://user-images.githubusercontent.com/86648892/188498035-9165adde-f2ba-4b0d-a6c3-dc2f45caf40b.png">

- 1)은 현재 이 대화에서 입력하는 값을 넣겠다
- 2)는 대화에서 나가서 코드상 default값을 넣어서 다시 makemigrations
- 1이 enter로 해결할 수 있기에 더 편하다
- 0002 설계도 확인
    - `dependencies` 에 0001 initial 설계도가 있음
        - 2번 설계도는 의존성이 있기에 1번 설계도가 있어야 의미가 있는 설계도
        - 만약 `models.py` 에 새로운 class를 생성하고 3번 설계도를 만든다면 다른 테이블이기에 의존성이 없음
- 설계도를 쌓아나가는 이유?
    - 모델이 망가졌을 때 망한 설계도를 버리고 잘 돌아갔던 시점에서 다시 누적하기 위함
- migrate를 통해 다시 반영

---

## MIGRATIONS 정리

1. `models.py` 변경
    - 데이터를 ***구조화***하고 ***조작***하기 위한 도구
2. 설계도 생성 (makemigrations)
3. 설계도 DB 반영 (migrate)

---

# ORM

## 그런데 설계도는 어떻게, 누가 해석할까?

- Django(i speak python) —> DB(i speak SQL)
- 중간에 SQL 언어로 번역해주는 친구가 필요함

## ORM

- Object-Relational-Mapping
- Django Framework는 내장된 Django ORM이 있음
    - 한 마디로 SQL을 사용하지 않고 데이터베이스를 조작할 수 있게 만들어주는 매개체
- 객체지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에 데이터를 변환하는 프로그래밍 기술
    - 객체지향 프로그래밍에서 데이터베이스를 연동할 때, 데이터베이스와 객체지향 프로그래밍 언어 간의 호환되지 않는 데이터를 변환하는 프로그래밍 기법

<img width="1125" alt="dj_46" src="https://user-images.githubusercontent.com/86648892/188498037-a31c3dd8-7e77-4cdb-9514-0debe061338c.png">

## ORM 장단점

### 장점

- SQL을 잘 알지 못해도 객체지향 언어로 DB 조작이 가능
- 객체지향적 접근으로 인한 높은 생산성
    - “생산성”
        - 현시대 개발의 키워드

### 단점

- ORM만으로 완전한 서비스를 구현하기 어려운 경우가 있음

---

## [참고] Shell이란?

- 운영체제 상에서 다양한 기능과 서비스를 구현하는 인터페이스를 제공하는 프로그램
- 셸(껍데기)은 사용자와 운영체제 내부 사이의 인터페이스를 감싸는 층이기 때문에 그러한 이름이 붙음
- “사용자" ↔ 셸 ↔ ”운영체제”
- 코드 테스트할 때 유용
- python shell 실행 명령어
    - git bash (windows)
        - `$ python -i`
    - zsh (macOS)
        - `$ python`
- django shell
    - `$ pip install django-extensions`
    - `$ python manage.py shell_plus`
        - django-extension이 제공하는 shell_plus
        - 자주 사용하는 모듈을 자동으로 import해줌
        - 없다면 `$ python manage.py shell`
- shell 종료 시 `exit()`

<img width="1005" alt="dj_47" src="https://user-images.githubusercontent.com/86648892/188498039-8d7305fb-bd82-4429-9ba9-992c4a42d811.png">

---

# QUERYSET API

- ORM이 사용하는 라이브러리 이름
- Django가 기본적으로 ORM을 제공함에 따라 DB를 편하게 조작할 수 있도록 도움
- Model을 만들면 Django는 객체들을 만들고, 읽고, 수정하고, 지울 수 있는 (CRUD) DB API를 자동으로 만듬

<img width="905" alt="dj_48" src="https://user-images.githubusercontent.com/86648892/188498044-f5c93166-6381-4f9d-819b-411813e21a8e.png">

- `Article.objects.all()`
    - 전체 데이터를 조회하는 ORM 코드
        - DB에게 전체 데이터 다 내놓으라고 하는 것
        - 결과가 QuerySet이라는 객체로 나옴
- Queryset API 부분에서 CRUD

## objects manager

- 다양한 Queryset API를 제공해주는 친구
    - “DB를 Python class로 조작할 수 있도록 여러 메서드를 제공하는 manager”
- Django 모델이 데이터베이스 쿼리 작업을 가능하게 하는 인터페이스
- Django는 기본적으로 모든 Django 모델 클래스에 대해 objects라는 Manager 객체를 자동으로 추가함
- 이 Manager(objects)를 통해 특정 데이터를 조작(메서드)할 수 있음

## Query

- 데이터베이스에 날리는 요청
    - “쿼리문을 작성한다”
        - 원하는 데이터를 얻기 위해 데이터베이스에 요청을 보낼 코드를 작성한다
- 이에 대한 응답으로 QuerySet이라는 자료형이 돌아옴
- Client → python(query) → ORM → SQL → Database → SQL → ORM → python(QuerySet)

## QuerySet

- 데이터베이스에게서 전달받은 객체 목록 (데이터 모음)
    - 리스트는 아니지만 리스트와 같은 특성을 가짐
        - iterable함
        - index로 접근 가능
- Django ORM을 통해 만들어진 자료형이며, 필터를 걸거나 정렬 등을 수행할 수 있음
- “objects” manager를 사용하여 ***복수의 데이터***를 가져오는 queryset method를 사용할 때 반환되는 객체
    - ***단일한 객체 반환 시에는 모델의 인스턴스를 반환***

<img width="1169" alt="dj_49" src="https://user-images.githubusercontent.com/86648892/188498047-fe72b8ae-57af-44e7-b7a4-5ffb2bb8276d.png">

---

# QuerySet API를 활용한 CRUD 구현

## CRUD

- Create, Read, Update, Delete
    - 생성, 조회, 수정, 삭제
- 대부분의 컴퓨터 소프트웨어가 가지는 기본적인 데이터 처리 기능 4가지를 지칭

## CREATE

### 데이터 객체 생성 방법

1. `article = Article()`
    - 클래스를 통한 인스턴스 생성
        - `article.title = 'x'`
            - 클래스 변수명과 같은 이름의 인스턴스 변수를 생성 후 값 할당
                - `article.save()`
                    - 인스턴스로 save 메서드 호출
                        - `article.save()` 해야 DB에 등록됨
2. `article = Article(title = 'x')`
    - `article.save()`
3. `Article.objects.create(title = ‘x’)`
    - QuerySet API 중 `create()` 메서드 활용
        - `save()` 필요없음
            - save 이전에 유효성 검사를 하지 못하므로 좋은 것은 아니다

### `.save()`

- “Saving object”
- 객체를 데이터베이스에 저장함
- 데이터 생성 시 save를 호출하기 전에는 객체의 id값은 None
    - id 값은 Django가 아니라 데이터베이스에서 계산되기 때문
- 단순히 모델 클래스를 통해 인스턴스를 생성하는 것은 DB에 영향을 미치지 않기 때문에 반드시 save를 호출해야 테이블에 레코드가 생성됨

### 예시 코드

```html
{% extends 'base.html' %}

{% block content %}
  <h1>NEW</h1>
  <form action="{% url 'articles:create' %}" method='GET'>
    <label for="title">Title: </label>
    {% comment %} name은 url querystring에 들어갈 키 명칭 {% endcomment %}
    <input type="text" name="title" id="title"><br>
    <label for="content">Content: </label>
    <input type="text" name="content" id="content"><br>
    <input type="submit">
  </form>
  <hr>
  <a href="{% url 'articles:index' %}">Go Back to Index</a>
{% endblock content %}
```

```python
# new page의 input에서 쏴준 request 속에 데이터가 있다
# 요청에 대한 모든 데이터는 request에 있다
# input에 정의한 name이 key
def create(request):
    # 사용자의 데이터를 받아서 DB에 저장
    # 데이터 받기
    title = request.GET.get('title')
    content = request.GET.get('content')

    # DB에 저장
    #1
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    #2 (왼쪽이 DB의 필드, 오른쪽이 요청에서 받아온 변수)
    article = Article(title=title, content=content)
    article.save()

    # #3
    # Article.objects.create(title=title, content=content)

    return render(request, 'articles/create.html')
```

## READ

- 데이터 조회
    - QuerySet API methods that “return new querysets”
    - QuerySet API methods that “do not return querysets”

### `all()`

- QuerySet return
- 전체 데이터 조회

<img width="1096" alt="dj_50" src="https://user-images.githubusercontent.com/86648892/188498051-1b43737c-5ae7-4a91-9254-0d8d431ebe51.png">

### `get()`

- 유니크한 데이터, 고유성(uniqueness)을 보장하는 조회에서 사용해야함
    - 대표적으로 primary key
- 단일 데이터 조회
- 객체를 찾을 수 없으면 DoesNotExist 예외를 발생시키고, 둘 이상의 객체를 찾으면 MultipleObjectsReturned 예외를 발생시킴

<img width="970" alt="dj_51" src="https://user-images.githubusercontent.com/86648892/188498055-4cc49318-6668-4901-908a-22174b97a2a9.png">

### `filter()`

- QuerySet return
- 지정된 조회 매개 변수와 일치하는 객체를 포함하는 새 QuerySet을 반환
- 항상 QuerySet으로 반환함
    - 없으면 빈 QuerySet
    - 단일 객체도 QuerySet으로
- pk에는 부적합
    - QuerySet으로 주기에 한번 더 벗겨내야하는 불편함
    - 데이터를 조회했는데 없음에도 불구하고 빈 QuerySet을 반환해버림
        - 예외처리가 어려움

<img width="1099" alt="dj_52" src="https://user-images.githubusercontent.com/86648892/188498056-f5113ac0-6945-491b-a435-6d15582c3979.png">

### Field lookups

- 조건을 설정하여 조회하는 것
- 특정 레코드에 대한 조건을 설정하는 방법
- QuerySet method `filter()`, `exclude()` 및 `get()` 에 대한 키워드 인자로 지정됨
- [QuerySet methods](https://docs.djangoproject.com/en/4.1/ref/models/querysets/)

<img width="646" alt="dj_53" src="https://user-images.githubusercontent.com/86648892/188498058-8983af76-f9ab-4a0c-96b1-7381fa010b66.png">

## UPDATE

- update 과정
    - 수정하고자 하는 인스턴스 객체를 조회 후 반환 값을 저장
        - 인스턴스 객체의 인스턴스 변수 값을 새로운 값으로 할당
            - `save()` 인스턴스 메서드 호출

<img width="613" alt="dj_54" src="https://user-images.githubusercontent.com/86648892/188498060-96aa0d6c-9d99-44ec-a405-cd02270908ed.png">

## DELETE

- 삭제하고자 하는 인스턴스 객체를 조회 후 반환 값을 저장
    - `delete()` 인스턴스 메서드 호출

<img width="622" alt="dj_55" src="https://user-images.githubusercontent.com/86648892/188498061-ccfe2eed-b555-413c-9c94-6672c600c4b9.png">

- 그렇다면 pk 1번이 삭제되고 새로 추가되는 항목은 pk 1번에 들어갈까? 끝 순서로 들어갈까?
    - 끝 순서로 들어간다
- 대부분의 데이터베이스는 삭제된 값을 재사용하지 않는다

## 출력 참고

<img width="614" alt="dj_56" src="https://user-images.githubusercontent.com/86648892/188498063-8fe75887-df99-4b42-92c8-5be7bec33a23.png">

<img width="1515" alt="dj_57" src="https://user-images.githubusercontent.com/86648892/188498065-4d337d1c-05ff-4e01-8715-e8496a0dd9aa.png">

- migrations?
    - DB에 영향을 끼치는 변경이 아니기에 새롭게 생성할 migrations가 없다!

---

# CRUD with view functions

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
                    - 즉, POST 요청을 할 때는 ***CSRF Token***이 필요하다
                        - ***CSRF***
                            - Cross-Site-Request-Forgery (사이트 간 요청 위조)
                                - 사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여 특정 웹페이지를 보안에 취약하게 하거나 수정, 삭제 등의 작업을 하게 만드는 공격 방법 (2008년 옥션 해킹 사건)
                        - ***CSRF Token***
                            - Security Token 사용 방식
                                - 사용자의 데이터에 임의의 난수 값(token)을 부여해 매 요청마다 해당 난수 값을 포함시켜 전송시키도록 함
                                - 이후 서버에서 요청을 받을 때마다 전달된 token값이 유효한지 검증
                                - 일반적으로 데이터 변경이 가능한 `POST` , `PATCH` , `DELETE` Method 등에 적용
                                - Django는 DTL에서 csrf_token 템플릿 태그를 제공
                                    - `{% csrf_token %}`
                                        - 템플릿에서 내부 URL로 향하는 `POST` form을 사용하는 경우에 사용
                                            - 해당 태그가 없으면 Django 서버는 요청에 대해 403 forbidden으로 응답
                                            - 외부 URL로 향하는 `POST` form에 대해서는 CSRF 토큰이 유출되어 취약성을 유발할 수 있기에 사용하지 않음
                                    - input type이 hidden으로 작성되며 value는 Django에서 생성한 hash 값으로 설정
                        
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
    - 리소스를 생성, 변경하기 위해 데이터를 ***HTTP body***에 담아 전송
        - 개발자도구 - NETWORK 탭 - Payload 탭의 Form-Data 확인
    - `GET` 의 Query String Parameter와 다르게 ***URL로 보내지지 않음***
    - CRUD 중 C, U, D 역할을 담당
    - ex) 로그인

---

## Code Snippets

<img width="1573" alt="dj_59" src="https://user-images.githubusercontent.com/86648892/188498067-bcb242bb-0f9e-4b7d-bb81-11361579a7a5.png">

### `/templates/base.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
  <title>Document</title>
</head>
<body>
  
  {% block content %}
  {% endblock content %}

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
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
{% extends 'base.html' %}

{% block content %}
  <h1>Index 목록</h1>
  <a href="{% url 'articles:new' %}">글 작성</a><br>
  <hr>
  {% for article in articles %}
    <p>번호: {{ article.pk }}</p>
    {% comment %} 위에 for문으로 들어온 article의 pk값을 적용한 detail이라는 이름의 url로 이동 {% endcomment %}
    <a href="{% url 'articles:detail' article.pk %}">제목: {{ article.title }}</a>
    <hr>
    <br>
  {% endfor %}
{% endblock content %}
```

### `/articles/templates/articles/new.html`

```html
{% extends 'base.html' %}

{% block content %}
  <h1>글작성</h1>
  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    <label for="title">제목</label>
    <input type="text" name="title" id="title"><br>

    <label for="content">내용</label>
    <textarea type="text" name="content" id="content"></textarea><br>

    <input type="submit" value="작성"><br>

    <a href="{% url 'articles:index' %}">글 목록 보기</a>
  </form>
{% endblock content %}
```

### `/articles/templates/articles/detail.html`

```html
{% extends 'base.html' %}

{% block content %}
  <h1>글 상세</h1>
  <h3>{{ article.pk }}번째 글</h3>
  <hr>
  <p>제목: {{ article.title }}</p>
  <p>내용: {{ article.content }}</p>
  <p>생성시간: {{ article.created_at }}</p>
  <p>수정시간: {{ article.updated_at }}</p>
  <hr>

  {% comment %} 단순히 수정 페이지로 이동하는 것이므로 a태그 사용 {% endcomment %}
  <a href="{% url 'articles:edit' article.pk %}">수정</a>
  {% comment %} delete url로 이동하면 -> views의 delete 호출 -> delete 함수가 index 페이지로 redirect {% endcomment %}
  <form action="{% url 'articles:delete' article.pk %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="삭제">
  </form>
  <a href="{% url 'articles:index' %}">글 목록 보기</a>
{% endblock content %}
```

### `/articles/templates/articles/edit.html`

```html
{% extends 'base.html' %}

{% block content %}
  <h1>글 수정</h1>
  <form action="{% url 'articles:update' article.pk %}" method="POST">
    {% csrf_token %}
    <label for="title">제목</label>
    {% comment %} value를 통해 넘겨받은 article의 title 채우기 {% endcomment %}
    <input type="text" name="title" id="title" value="{{article.title}}"><br>

    <label for="content">내용</label>
    {% comment %} 넘겨받은 article의 content 채우기 {% endcomment %}
    <textarea type="text" name="content" id="content">{{article.content}}</textarea><br>

    <input type="submit" value="수정"><br>
  </form>
  <a href="{% url 'articles:index' %}">글 목록 보기</a>
{% endblock content %}
```

---

# Admin Site

- ***Django의 가장 강력한 기능 중 하나인 automatic admin interface***
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

---

## 정리

- Model
    - Django는 Model을 통해 데이터에 접속하고 관리
- ORM
    - 객체지향 프로그래밍을 이용한 DB 조작
- Migrations
    - 모델에 생긴 변화(필드 추가, 모델 삭제 등)를 DB에 반영하는 방법(과정)
- HTTP request & response
    - 요청의 행동을 표현하는 HTTP request method
    - 요청에 대한 성공 여부 응답을 숫자로 표현하는 HTTP response status codes

---

# Django Form

### 참고 링크

- [Django Github - Forms](https://github.com/django/django/blob/main/django/forms/models.py)
- [Django Docs - The Forms API](https://docs.djangoproject.com/en/4.1/ref/forms/api/#django.forms.Form.errors)
- [Django Docs - Form fields (linked to ChoiceField)](https://docs.djangoproject.com/en/4.1/ref/forms/fields/#)
- [Django Docs - Widgets (linked to Selector and checkbox widgets)](https://docs.djangoproject.com/en/4.1/ref/forms/widgets/#selector-and-checkbox-widgets)
- [Django Docs - Coding Style](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/)
- [Django Docs - Working with forms (linked to Rendering fields manually](https://docs.djangoproject.com/en/4.1/topics/forms/#rendering-fields-manually)
- [django-bootstrap-v5 Docs](https://django-bootstrap-v5.readthedocs.io/en/latest/)

## Django Form

- HTML `<input>` 태그를 직접 사용하지 않고 ***Django Form***이라는 프레임워크를 통해 사용자로부터 데이터를 받자
- WHY?
    - ***유효성 검증***
        - 사용자의 요청 중에는 비정상적인 혹은 악의적인 요청이 있음
        - 사용자가 입력한 데이터가 우리가 원하는 데이터 형식에 맞는지 유효성 검증이 필요
            - 이러한 유효성 검증은 많은 부가적인 것들을 고려해서 구현해야 하는데, 이는 개발 생산성을 늦추고, 쉽지도 않음
                - Django Form은 이 과정에서 과중한 작업과 반복적 코드를 줄여줌으로써 훨씬 쉽게 유효성 검증을 진행할 수 있도록 만듬
    - 유효성 검증 외에도 빠르게 form 작업을 수행할 수 있음

### Form에 대한 Django의 역할

- Form은 Django의 ***유효성 검사 도구 중 하나로 외부의 악의적 공격 및 데이터 손상에 대한 중요한 방어 수단***
- Django는 Form과 관련한 유효성 검사를 ***단순화하고 자동화***할 수 있는 기능을 제공하여, 개발자가 직접 작성하는 코드보다 더 안전하고 빠르게 수행하는 코드를 작성할 수 있음
    - ***개발자가 필요한 핵심 부분만 집중***할 수 있도록 돕는 프레임워크의 특성
- Django는 Form과 관련한 작업의 3가지 부분을 처리해줌
    1. 렌더링을 위한 데이터 준비 및 재구성
    2. 데이터에 대한 HTML forms 생성
    3. 클라이언트로부터 받은 데이터 수신 및 처리

---

# Django Form Class

- Form Class
    - Django form 관리 시스템의 핵심

## Form Class 선언

- 상속을 통해 선언
    - forms 라이브러리의 Form 클래스를 상속받음
        - Model Class를 models 라이브러리의 Model 클래스를 상속받는 것과 유사
- `forms.py`
    - 앱 폴더에 생성 후 form class 선언
    
    <img width="616" alt="dj_61" src="https://user-images.githubusercontent.com/86648892/189478360-f3ae2e67-30be-4459-af7e-87f1b885b3de.png">
    
    - 모델에 관련없이
        - 사용자로부터 무엇을 받을 것인지, 어떤 타입으로 받을지 고려하여 작성
    - form에는 model field와 달리 TextField가 존재하지 않음
    - Form Class를 forms.py에 작성하는 것은 규약은 아니다
        - 파일 이름이 달라도 되고, models.py나 다른 어디에도 작성이 가능하지만 관행적으로 forms.py에 작성하는 것을 권장
    - form class에서 `Charfield()`의 `max_length`는 models와 다르게 필수 인자는 아님
        - 그냥 편리하게 길이 제한을 걸려고 쓰는 용도

## Form Rendering options

- html 파일에서 렌더링 시 views의 함수의 context에 담아 넘겨받은 form을
    - `{{ form.as_p }}` 와 같이 접근하여 사용
- `<label>` & `<input>` 쌍에 대한 3가지 출력 옵션
    1. `as_p()`
        - 각 필드가 단락(`<p>` 태그)으로 감싸져서 렌더링
    2. `as_ul()`
        - 각 필드가 목록 항목(`<li>` 태그)으로 감싸져서 렌더링
        - `<ul>` 태그는 직접 작성해야함
    3. `as_table()`
        - 각 필드가 테이블(`<tr>` 태그) 행으로 감싸져서 렌더링
- 주로 `as_p()` 를 많이 사용함

## Form fields & Widgets

- 그런데 `{{ form }}` 과 같이 한 덩어리로 묶어서 렌더링하면 안에 세부적인 처리를 어떻게 할 것인가에 대한 의문이 생김
- Django의 2가지 HTML input 요소 표현
    1. ***Form fields***
        - ex) `forms.CharField()`
        - ***입력에 대한 유효성 검사 로직을 처리***
        - 템플릿에서 직접 사용됨
    2. ***Widgets***
        - ex) `forms.CharField(widget=forms.Textarea)`
        - 웹 페이지의 ***HTML input 요소 렌더링을 담당***
            - 단순히 HTML 렌더링, 출력을 처리하는 것이며 유효성 검증과 아무런 관계가 없음
                - “웹 페이지에서 input element의 단순 raw한 렌더링만을 처리하는 것일 뿐”
        - Widgets은 반드시 form fields에 할당됨
            - form fields의 core field arguments 확인
    - 쉽게 말해 Form fields는 사용자의 입력이 어떠한 입력값이어야하는지 정의하고, 유효한 입력값인지 판단하기 위함이며, Widgets는 input값의 출력을 어떻게 해줄지 세부적으로 조정하기 위함

### 드랍다운을 만들어보자

```python
# articles/forms.py

from django import forms

class ArticleForm(forms.Form):
    NATION_A = 'kr'
    NATION_B = 'ch'
    NATION_C = 'jp'
    NATION_CHOICES = [
        (NATION_A, '한국'),
        (NATION_B, '중국'),
        (NATION_C, '일본'),
    ]
    title = forms.CharField(max_length=10)
    content = forms.CharField(widget=forms.Textarea)
    nation = forms.ChoiceField(choices=NATION_CHOICES)

# NATION_CHOICES = [ ('kr', '한국'), ('ch', '중국'), ('jp', '일본'), ]
# 이렇게 선언하는 것은 동작은 같지만
# Django Style Guide에 어긋난다
# ChoiceField는 <select> 태그, choices의 인자들은 <select> 태그 안의 <option>들로 들어간다
```

- [Django Docs - Widgets (linked to Selector and checkbox widgets)](https://docs.djangoproject.com/en/4.1/ref/forms/widgets/#selector-and-checkbox-widgets)
- [Django Docs - Coding Style](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/)

---

# Django ModelForm

## ModelForm Class

- Model을 기반으로 한 Form Class
- Model을 통해 Form Class를 만들 수 있는 helper class
    - 기반으로 하는 모델의 필드를 따로 재정의하지 않아도 됨
- ModelForm은 Form과 똑같은 방식으로 view 함수에서 사용

## ModelForm 선언

- 상속을 통해 선언
    - forms 라이브러리에서 파생된 ModelForm 클래스 상속
    - 정의한 ModelForm 클래스 안에 inner class인 Meta 클래스 선언
        - 어떤 모델을 기반으로 form을 작성할 것인지에 대한 정보를 Meta 클래스에 지정
    
    <img width="527" alt="dj_62" src="https://user-images.githubusercontent.com/86648892/189478363-35f7863f-a5f7-405b-b9ce-e233243ad3ab.png">

### Meta Class

- ModelForm의 정보를 작성하는 곳
    - model, fields라는 변수명은 정해져 있음
- `model = Article`
    - 참조할 모델
        - 인스턴스가 아닌 참조값
    - 참조하는 모델에 정의된 field 정보를 Form에 적용함
        - input값을 받는 field들
- 어떤 모델을 기반으로 form을 작성할 것인지에 대해 inner class인 Meta 클래스에 지정
    - `model = Article`
        - 참조값을 줌 (인스턴스가 아님)
        - 참조값과 반환값
    - `fields = '__all__'`
        - 모델의 ***입력받아야 할*** 모든 필드를 포함
        - 필드 중 사용자가 입력하지 않는 필드는 포함하지 않음
            - ex) `auto_now_add = True` 인 `created_at` 이나 `auto_add = True` 인 `updated_at` 등
    
    <img width="1086" alt="dj_63" src="https://user-images.githubusercontent.com/86648892/189478364-db5106b4-8175-44b9-a04a-bae25345d820.png">
    
    - `exclude` 속성을 사용하여 모델에서 포함하지 않을 필드를 지정할 수 있음
        - fields와 exclude를 함께 작성해도 되나 권장하지 않음

### [참고] Meta Data?

- 데이터를 표현하기 위한 데이터

### [참고] 참조값과 반환값

- 언제 참조값을 사용할까?
    - 함수를 호출하지 않고 함수 자체를 그대로 전달하여, 다른 함수에서 “필요한 시점"에 호출하는 경우
        - view 함수의 참조값을 그대로 넘김으로써, path 함수가 내부적으로 해당 view 함수를 “필요한 시점"에 사용하기 위해서
        
        <img width="756" alt="dj_64" src="https://user-images.githubusercontent.com/86648892/189478365-9bee80ec-525a-4a6e-b7f1-7b5c870ec329.png">
        
    - 클래스도 마찬가지
        - Article이라는 클래스를 “호출하지 않고(==model을 인스턴스로 만들지 않고)” 작성하는 이유는 ArticleForm이 해당 클래스를 필요한 시점에 사용하기 위함
        - 더불어 이 경우에는 인스턴스가 필요한 것이 아닌, 실제 Article 모델의 참조값을 통해 해당 클래스의 필드나 속성 등을 내부적으로 참조하기 위한 이유도 있음

---

# ModelForm with view functions (CRUD)

## CREATE

<img width="679" alt="dj_65" src="https://user-images.githubusercontent.com/86648892/189478366-3205d78b-db05-486e-890d-40fbf7447101.png">

- `data=request.POST`
    - `BaseModelForm()`의 첫번째 인자는 data임
    - request에 담긴 데이터를 바탕으로 ArticleForm 인스턴스 생성
- 유효성 검사를 통과하면
    - `article = form.save()`
        - ModelForm의 `save()` 는 input 값들을 채운 해당 모델 instance를 반환
        - 상세화면 페이지로 넘어갈 때 해당 모델 인스턴스를 넘겨줘야하므로 article에 할당
    - 이후 상세화면으로 리다이렉트
- 통과하지 못하면
    - 작성 페이지로 리다이렉트

### `is_valid()`

- 유효성 검사를 실행하고, 데이터가 유효한지 여부를 boolean으로 반환
    - `max_length` 등과 같이 모델에 설정해둔 유효성 기준에 따라 판단
        - CharField()에 숫자를 넣으면 안되는것과 같은 기본적인 내장 유효성 검사 외에 추가적으로 유효성 검사 기준 인자를 잘 설계하는 것이 중요
- 데이터 유효성 검사를 보장하기 위한 많은 테스트에 대해 Django는 `is_valid()` 를 제공하여 개발자의 편의를 도움
- `BaseForm()` 에 정의되어 있음

### is_valid()의 결과가 False라면?

- `is_valid()` 의 반환 값이 False인 경우 form 인스턴스의 errors 속성에 값이 저장됨
    - 기본적으로는 빈 값
        - 유효성 검증 실패 시 실패한 원인이 딕셔너리 형태로 저장됨
            - `forms.py`에서 정의한 `error_messages` 나 기본적으로 정의된 에러 메세지를 포함한 페이지를 렌더링해줌
    - [참고] 공백과 빈 값은 다르다
        - 빈 값
            - “이 입력란을 작성하세요”
                - Django와 관련없음
                    - HTML과 관련있음
                        - input 태그의 required라는 속성에 의해 Django에 요청이 가기 전에 이미 막힘
                            - 개발자 도구를 통해 required를 지우고 보내면 Django에서 유효성 검사 진행 가능
        - 공백
            - Django에서 에러를 주는 경우

<img width="872" alt="dj_66" src="https://user-images.githubusercontent.com/86648892/189478368-ebc39828-b613-40ad-872c-a8fbd5a9562c.png">

### `form.save()`

- `return self.instance`
- form 인스턴스에 바인딩된 데이터를 통해 데이터베이스 객체를 만들고 저장
- ModelForm의 하위 클래스는 키워드 인자 `instance` 여부를 통해 CREATE, UPDATE 여부를 결정
    - 제공되지 않는 경우 `save()` 는 지정된 모델의 새 인스턴스를 만듬 (CREATE)
    - 제공된 경우 `save()` 는 해당 인스턴스를 수정 (UPDATE)

<img width="478" alt="dj_67" src="https://user-images.githubusercontent.com/86648892/189478369-2bdd9a37-01ab-43fe-9994-a699bb99a01f.png">

---

## UPDATE

- ModelForm의 인자 instance는 수정 대상이 되는 객체(기존 객체)를 지정
    1. `request.POST`
        - 사용자가 form을 통해 전송한 데이터 (새로운 데이터)
    2. `instance`
        - 수정이 되는 대상
- CREATE에서는
    - `form = ArticleForm(request.POST)`
        - Create 버튼을 통해 들어온 POST 요청에 들어있는 입력 데이터들을 바탕으로 ArticleForm의 모델인 Article의 인스턴스를 반환해 form에 할당
- UPDATE에서는
    - `article = Article.objects.get(pk=pk)`
        - 일단 수정할 인스턴스를 들고온 뒤
    - `form = ArticleForm(request.POST, instance=article)`
        - Update 버튼을 통해 들어온 POST 요청에 들어있는 입력 데이터들을 바탕으로, 위에 할당한 article이라는 인스턴스를 수정한 결과를 form에 할당

<img width="802" alt="dj_68" src="https://user-images.githubusercontent.com/86648892/189478370-050edb5b-0b0a-43a2-8429-11b7e24494c2.png">

<img width="827" alt="dj_69" src="https://user-images.githubusercontent.com/86648892/189478372-4e51086b-53c2-46c5-af64-a606d5be3476.png">

<img width="821" alt="dj_70" src="https://user-images.githubusercontent.com/86648892/189478374-ef4fe4fd-9010-448e-ae80-856289c419a4.png">

### [참고] ModelForm의 인자 구조

<img width="1113" alt="dj_71" src="https://user-images.githubusercontent.com/86648892/189478375-b9809196-81af-43da-a0d5-e99c0aacfedf.png">

---

## Form & ModelForm

- Form과 ModelForm은 모델을 기반으로 안하냐의 차이
- 누가 더 좋은 것이 아니라 역할이 다른 것
    - ***사용자로부터 받는 데이터가 DB에 영향을 미치는가 여부***
        - ***로그인은 사용자의 데이터를 받아 인증 과정에서만 사용 후 별도로 DB에 저장하지 않으므로 Form***
        - ***회원가입으로 유저 데이터를 추가하거나, 게시판 글 작성처럼 아티클 데이터를 추가하는 경우 ModelForm***

### Form

- 사용자의 입력을 필요로 하며 직접 입력 데이터가 DB 저장에 사용되지 않거나 일부 데이터만 사용될 때
    - ex) 로그인
        - 사용자의 데이터를 받아 인증 과정에서만 사용 후 별도로 DB에 저장하지 않음

### ModelForm

- 사용자의 입력을 필요로 하며 입력 받은 것을 그대로 DB 필드에 맞춰 저장할 때
- 데이터의 유효성 검사가 끝나면 데이터를 각각 어떤 레코드에 매핑해야할지 이미 알고있기 때문에 곧바로 `save()` 호출이 가능

---

# Handling HTTP requests

- HTTP requests 처리에 따른 view 함수 구조 변화를 구현해보자
    - 하나의 view 함수에서 HTTP request method에 따라 로직이 분리되도록 변경
- new-create, edit-update의 view 함수 역할에는 공동의 목적과 차이점이 있음
    - 공통점
        - new-create는 “생성”
        - edit-update는 “수정”
    - 차이점
        - new, edit는 페이지 렌더링 (GET)
        - create, update는 DB 조작 (POST)

## CREATE

<img width="789" alt="dj_72" src="https://user-images.githubusercontent.com/86648892/189478376-5cd263c9-dc5e-47da-a179-3dcaf38b77f2.png">

- `views.py` 의 new 함수와 create 함수를 create 함수로 통합
    - 불필요해진 new 함수의 url path를 삭제
        - new.html의 이름을 create.html로 변경 후 url path를 변경된 이름으로 수정
            - index.html의 새 게시글 생성 페이지를 렌더링하는 버튼의 링크를 articles의 create url path로 변경
                - 기존 new 함수의 `return render(request, 'articles/new.html', context)` 를 `return render(request, 'articles/create.html', context)` 로 변경
- context의 들여쓰기 위치 주의
    - `if form.is_valid()` 가 False로 평가받았을 때 에러 정보가 담긴 form 인스턴스가 context로 넘어갈 수 있도록 설정
- 분기처리를 할 때 왜 POST를 if의 조건으로 쓸까?
    - DB 조작 관련 코드를 POST일때만 수행한다고 설정할 수 있음
    - if에 GET을 쓰고 else에서 DB 조작 코드를 쓴다면
        - POST외에 다른 request method에 대해서도 DB 조작이 가능한 상태가 되어버림

## UPDATE

- CREATE와 동일

<img width="747" alt="dj_73" src="https://user-images.githubusercontent.com/86648892/189478377-cf75d70b-25c8-4aeb-a2be-a9126248b080.png">

## DELETE

- POST 요청에 대해서만 삭제가 가능하도록 수정

<img width="849" alt="dj_74" src="https://user-images.githubusercontent.com/86648892/189478379-b35ac0fa-8d13-439b-a6fa-5f70ef8144e8.png">

---

# View Decorators

- View decorators를 활용하여 view 함수를 단단하게 만들어보자

## Decorator

- 기존에 작성된 함수에 기능을 추가하고싶을 때
    - 해당 함수를 수정하지 않고 기능을 추가해주는 함수
- 데코레이터 동작 예시
    - 
    
    <img width="901" alt="dj_75" src="https://user-images.githubusercontent.com/86648892/189478381-c459b80f-0b8e-41e9-8e8a-590283a86a15.png">
    

## Allowed HTTP methods

- Django는 다양한 HTTP 기능을 지원하기 위해 view 함수에 적용할 수 있는 데코레이터 제공
    - `from django.views.decorators.http`
        - `import require_http_methods`
            - `@require_http_methods` 시 직접 뒤에 붙인 HTTP request method일 때만 허용
                - ex) `@require_http_methods(['GET', 'POST'])`
        - `import require_safe`
            - `@require_safe` 시 GET 요청일 때만 허용
        - `import require_POST`
            - `@require_POST` 시 POST 요청일 때만 허용
- 일치하지 않는 메서드 요청이라면 ***405 Method Not Allowed***를 반환
    - 405 Method Not Allowed
        - 요청 방법이 서버에게 전달되었으나 사용 불가능한 상태

## 적용

- index
    - 단순 전체 게시글 데이터 조회 (GET)
        - `@require_safe`
- create
    - 새 게시글 생성 페이지 렌더링 요청 (GET), 작성 후 새 게시글 생성 요청 (POST)
        - `@require_http_methods(['GET', 'POST'])`
- update
    - 게시글 수정 페이지 렌더링 요청 (GET), 작성 후 수정된 게시글 인스턴스 저장 요청 (POST)
        - `@require_http_methods(['GET', 'POST'])`
- delete
    - 게시글 DB에서 삭제 요청 (POST)
        - `@require_POST`
            - url로 delete를 시도하면 405 http status code 반환
    
    <img width="1013" alt="dj_76" src="https://user-images.githubusercontent.com/86648892/189478383-e4ab8b97-9751-4c7d-95a9-98e053d82c35.png">
    
    - `@require_POST` 작성했으므로 기존에 있던 `if request.method == 'POST':` 필요없음

---

# Custom Form Layout

### 참고 링크

- [Django Docs - Working with forms (linked to Rendering fields manually](https://docs.djangoproject.com/en/4.1/topics/forms/#rendering-fields-manually)
    - **subject는 컬럼의 이름**
- [django-bootstrap-v5 Docs](https://django-bootstrap-v5.readthedocs.io/en/latest/)

### 코드 예시 (create.html)

```html
{% extends 'base.html' %}
{% load bootstrap5 %}

{% block content %}
  <h1>CREATE</h1>
  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
  <hr>
  <a href="{% url 'articles:index' %}">뒤로가기</a>

  <hr>

  <h2>수동으로 Form 작성</h2>
  <form action="#">
    <div>
      {{ form.title.errors }}
      {{ form.title.label_tag }}
      {{ form.title }}
    </div>
    <div>
      {{ form.content.errors }}
      {{ form.content.label_tag }}
      {{ form.content }}
    </div>
  </form>

  <hr>

  <h2>Looping over the form’s fields</h2>
  <form action="#">
    {% for field in form %}
      {{ field.errors }}
      {{ field.label_tag }}
      {{ field }}
    {% endfor %}
  </form>

  <hr>

  <h2>bootstrap v5 라이브러리 사용하기</h2>
  <form action="#">
    {% bootstrap_form form %}
    {% buttons %}
      <button type="submit" class="btn btn-primary">Submit</button>
    {% endbuttons %}
  </form>
{% endblock content %}
```

<img width="1318" alt="dj_77" src="https://user-images.githubusercontent.com/86648892/189478385-284b3ec1-89b7-49de-8dbd-e9d5c3ccedf5.png">

<img width="1321" alt="dj_78" src="https://user-images.githubusercontent.com/86648892/189478387-b92345d6-80bb-4462-8095-39eee6e5325c.png">

<img width="1319" alt="dj_79" src="https://user-images.githubusercontent.com/86648892/189478388-6f300af7-185a-454a-96e0-5f6df1fcea36.png">

<img width="1325" alt="dj_80" src="https://user-images.githubusercontent.com/86648892/189478389-2e88b8bf-7d96-4ae6-a7ea-e4ab25cf83eb.png">

---

## 정리

- Django Form Class
    - Django 프로젝트의 주요 유효성 검사 도구
    - 공격 및 데이터 손상에 대한 중요한 방어 수단
    - 유효성 검사에 대해 개발자에게 강력한 편의를 제공
- View 함수 구조 변화
    - HTTP requests 처리에 따른 구조 변화

---