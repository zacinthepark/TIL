# Django

---

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

- `python [manage.py](http://manage.py) runserver`
    - url을 `ctrl+클릭` 하면 로켓화면 확인가능
    - 서버종료는 `ctrl+c`

### 프로젝트 구조

<img width="439" alt="dj_6" src="https://user-images.githubusercontent.com/86648892/188303741-32b2ad55-9c0e-4b45-bf61-9fedbfcf3157.png">

- `manage.py`
    - Django 프로젝트 전반에 대한 명령을 내릴 수 있는 파일
    - Django 프로젝트와 다양한 방법으로 상호작용하는 커맨드라인 유틸리티
    - `$ python [manage.py](http://manage.py) <command> [options]`
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
- `$ python [manage.py](http://manage.py) startapp articles`
    - articles라는 앱을 만든다
    - 일반적으로 어플리케이션의 이름은 ‘복수형'으로 작성하는 것을 권장
- `[settings.py](http://settings.py)` 의 `INSTALLED_APPS` 에 추가
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

- browser의 url → `[urls.py](http://urls.py)` → `[views.py](http://views.py)` → `index()`
    - `index(request)` 내의 request 파라미터에 django가 알아서 request를 넣어서 넘겨줌
- HTTP 요청을 수신하고 HTTP 응답을 반환하는 함수 작성
- Template에게 HTTP 응답 서식을 맡김

<img width="998" alt="dj_12" src="https://user-images.githubusercontent.com/86648892/188303748-1570ac25-78dc-41ff-8bce-16d976ca4bc8.png">

- `templates` 디렉토리 생성 및 `index.html` 파일 생성
- `return render(request, 'index.html')`
    - 해당 request에 대하여 index.html파일을 렌더링해줘
    - context는 data라고 생각하자
    - `[settings.py](http://settings.py)` 에 TEMPLATES
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

- `[settings.py](http://settings.py)` 의 DIRS에 추가하여 너 templates 찾을 때 이쪽도 찾아달라고 명령
    - `BASE_DIR` 은 프로젝트 홈 디렉토리를 가리키도록 설정해놓은 값
    - `BASE_DIR / templates`
        - 홈 디렉토리 바로 하위에 있는 templates
        - trailing comma 써주는 습관을 들이자

### BASE_DIR

- `settings.py`
    - `BASE_DIR = Path(__file__).resolve().parent.parent`
    - `[settings.py](http://settings.py)` 에서 특정 경로를 절대경로로 편하게 작성할 수 있도록 Django에서 미리 지정해둔 경로 값
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

- 앱이 많아졌을 때 `[urls.py](http://urls.py)` 를 각 app에 매핑하는 방법
    - app의 view 함수가 많아지면서 사용하는 `path()` 가 많아지고, app 또한 더 많이 작성되기에 프로젝트의 `[urls.py](http://urls.py)` 에서 모두 관리하는 것은 프로젝트 유지보수에 좋지 않음
- `python [manage.py](http://manage.py/) startapp pages`
    - pages 앱 생성
        - `[settings.py](http://settings.py)` → `INSTALLED_APPS` 에 pages 추가
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