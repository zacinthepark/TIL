# Database Basics and Django

- [Django](#django)
- [Django N:1 Relationship](#django-n1-relationship)
- [Django M:N Relationship](#django-mn-relationship)
- [Django REST Framework and Serializer](#django-rest-framework-and-serializer)


# The Django authentication system

### 참고 링크

- [Django Github - built-in auth models](https://github.com/django/django/blob/main/django/contrib/auth/models.py)
- [Django Github - builit-in auth forms](https://github.com/django/django/blob/main/django/contrib/auth/forms.py)
- [Django Docs - Built-in forms](https://docs.djangoproject.com/en/4.1/topics/auth/default/#module-django.contrib.auth.forms)
- [Django Github - global_settings.py](https://github.com/sebleier/django/blob/master/django/conf/global_settings.py)
- [Django Docs - Substituting a custom User model](https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#substituting-a-custom-user-model)
- [Python Docs - Abstract Base Classes](https://docs.python.org/3/library/abc.html)
- [Django Docs - How to use sessions](https://docs.djangoproject.com/en/4.1/topics/http/sessions/)
- [Django Docs - Built-in template context processors](https://docs.djangoproject.com/en/4.1/ref/templates/api/#built-in-template-context-processors)
- [Django Docs - User model Fields](https://docs.djangoproject.com/en/4.1/ref/contrib/auth/#fields)
- [Django Docs - Password management in Django](https://docs.djangoproject.com/en/3.2/topics/auth/passwords/)

## The Django authentication system

- Django authentication system(인증 시스템)은 인증(Authentication)과 권한(Authorization) 부여를 함께 제공(처리)하며, 이러한 기능을 일반적으로 인증 시스템이라함
- 필수 구성은 `settings.py` 에 이미 포함되어 있으며 INSTALLED_APPS에서 확인 가능
  - built-in app
    - `django.contrib.auth`
      - Django에서는 admin, staff, 일반 user가 있음
- Authentication(인증)
  - 신원 확인
  - 사용자가 자신이 누구인지 확인하는 것
- Authorization(권한)
  - 권한 부여
  - 인증된 사용자가 수행할 수 있는 작업을 결정

## 유저 관리용 accounts 앱 만들기

- 유저 인증과 관련된 앱
  - `$ python manage.py startapp accounts`
    - INSTALLED_APPS에 추가
    - **auth와 관련한 경로나 키워드들은 Django 내부적으로 accounts라는 이름으로 사용하고 있기에 되도록 accounts로 지정하는 것을 권장**
    - 다른 이름으로 설정해도 되지만 나중에 추가 설정을 해야할 일들이 생김
  - url 분리 및 매핑 실행

---

# Substituting a custom User model

- “Custom User Model”로 **대체**하기
- 기본 User Model을 Custom User Model로 대체할 것을 권장
  - Django에서는 기본적인 인증 시스템과 여러가지 필드가 포함된 User Model을 제공, 대부분의 개발 환경에서는 기본 User Model을 Custom User Model로 대체함
    - 개발자들이 작성하는 일부 프로젝트에서는 Django에서 제공하는 built-in User Model의 기본 인증 요구사항이 적절하지 않을 수 있음
      - ex) 내 서비스의 회원가입 시 username 대신 email을 식별 값으로 사용하는 것이 더 적합한 사이트인 경우, Django의 User Model은 기본적으로 username을 식별 값으로 사용하기 때문에 적합하지 않음
- Django는 현재 프로젝트에서 사용할 User Model을 결정하는 **AUTH_USER_MODEL** 설정 값으로 Default User Model을 재정의(override)할 수 있도록 함
- **첫 migrations를 진행하기 전에 대체 작업을 진행해야함**
  - migrations 과정에서 기본 user model도 포함되기 때문

## `AUTH_USER_MODEL`

- 프로젝트에서 User를 나타낼 때 사용하는 모델
  - auth 앱의 User 클래스라는 뜻
    - `django.contrib.auth`
      - Django의 contrib 모듈 안에 있는 auth
- 프로젝트가 진행되는동안 (모델을 만들고 마이그레이션한 후) 변경할 수 없음
  - 프로젝트 시작 시 설정하기 위한 것이며, 참조하는 모델은 첫번째 마이그레이션에서 사용할 수 있어야함
    - 즉, 첫번째 마이그레이션 이전에 확정지어야하는 값
- settings의 로드 구조
  - `settings.py` 에 기본값으로 `AUTH_USER_MODEL = 'auth.User'` 을 가지고 있음
    - AUTH_USER_MODEL은 `settings.py` 에 보이지 않는데 어디에 기본값이 작성되어 있는걸까?
      - 우리가 작성하는 `settings.py` 는 `global_settings.py` 를 상속받아 재정의하는 파일
        - [Django Github - global_settings.py](https://github.com/sebleier/django/blob/master/django/conf/global_settings.py)

## Custom User Model 대체 진행 방법

- 공식문서 참고
  - [Django Docs - Substituting a custom User model](https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#substituting-a-custom-user-model)

1. Custom User Model 작성

   - AbstractUser를 상속받는 커스텀 User 클래스 작성
     - 기존 User 클래스도 AbstractUser를 상속받기 때문에 커스텀 User 클래스도 완전히 같은 모습을 가지게 됨
       <img width="1110" alt="dj_81" src="https://user-images.githubusercontent.com/86648892/189502176-31307fca-dcfc-425c-9302-80eb5f310082.png">

2. Django 프로젝트에서 User를 나타내는데 사용하는 모델을 방금 생성한 커스텀 User 모델로 저장

<img width="616" alt="dj_82" src="https://user-images.githubusercontent.com/86648892/189502179-71ee98f1-23e4-4192-bb76-3d2be6c9e938.png">

3. `admin.py` 에 커스텀 User 모델을 등록

   - 기존 User 모델이 아니기 때문에 등록하지 않으면 admin site에 출력되지 않음

   <img width="614" alt="dj_83" src="https://user-images.githubusercontent.com/86648892/189502180-c81ecf0b-eb74-4e84-9247-e8f3c16b482d.png">

## [참고] User 모델 상속 관계

<img width="265" alt="dj_84" src="https://user-images.githubusercontent.com/86648892/189502185-e95cec36-78f9-4131-aaff-9bd51c3de265.png">

## [참고] AbstractUser

- “관리자 권한과 함께 완전한 기능을 가지고 있는 User model을 구현하는 추상 기본클래스”
  - Abstract이 붙는 클래스는 테이블에 생성되는 것이 아닌 기본 클래스로서 존재
- **Abstract Base Classes (추상 기본 클래스)**
  - 몇가지 공통 정보를 여러 다른 모델에 넣을 때 사용하는 클래스
  - 데이터베이스 테이블을 만드는데 사용되지 않으며, 대신 다른 모델의 기본클래스로 사용되는 경우 해당 필드가 하위 클래스의 필드에 추가됨
  - [Python Docs - Abstract Base Classes](https://docs.python.org/3/library/abc.html)

## 데이터베이스 초기화

- 프로젝트 중간에 AUTH_USER_MODEL을 변경하는 것은 모델 관계에 영향을 미치기에 더 어려운 작업이 필요
  - 예를 들어 변경사항이 자동으로 수행될 수 없기에 DB 스키마를 직접 수정하고, 이전 사용자 테이블에서 데이터를 이동하고, 일부 마이그레이션을 수동으로 다시 적용해야 하는 등
    - 결론은 **프로젝트 처음에 진행하자**
- 프로젝트 중간이라면?
  - 데이터베이스 초기화 후 진행
    1. migrations 파일 삭제
       - migrations 폴더 및 `__init__.py` 는 삭제하지 않음
       - 번호가 붙은 파일만 삭제
    2. db.sqlite3 삭제
    3. migrations 진행
       - makemigrations
       - migrate
- 이제 auth_user 테이블이 아니라 accounts_user 테이블을 사용하게 됨

## 반드시 User 모델을 대체해야 할까?

- Django는 새 프로젝트를 시작하는 경우 비록 기본 User 모델이 충분하더라도 커스텀 User 모델을 설정하는 것을 **강력하게 권장(highly recommended)**
- 커스텀 User 모델은 **기본 User 모델과 동일하게 작동하면서도 필요한 경우 나중에 맞춤 설정할 수 있기 때문**
  - 단, User 모델 대체 작업은 프로젝트의 모든 migrations 혹은 첫 migrate를 실행하기 전에 이 작업을 마쳐야함

---

# HTTP Cookies

- 로그인과 로그아웃을 이해하기에 앞서 핵심적인 개념

## HTTP

- Hyper Text Transefer Protocol
  - 웹상에서 데이터를 주고받는 약속
- 웹(WWW)에서 이루어지는 모든 데이터 교환의 기초
- HTML 문서와 같은 리소스들을 가져올 수 있도록 해주는 프로토콜(규칙, 규약)
- 클라이언트-서버 프로토콜이라고도 부름

## 요청과 응답

- **요청(requests)**
  - 클라이언트(브라우저)에 의해 전송되는 메세지
- **응답(response)**
  - 서버에서 응답으로 전송되는 메세지

## HTTP 특징

1. **비연결지향(connectionless)**
   - 연결되어있는 상태가 아니라 요청이 있을 때만 응답을 주고 끝
   - 서버는 요청에 대한 응답을 보낸 후 연결을 끊음
     - ex) 우리가 네이버 메인 페이지를 보고 있을 때 우리는 네이버 서버와 연결되어 있는 것이 아님
       - 네이버 서버는 우리에게 메인 페이지를 응답하고 연결을 끊은 것
2. **무상태(stateless)**
   - 비연결지향에 의해 상태 정보가 유지되지 않음
   - 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며 상태 정보가 유지되지 않음
   - 클라이언트와 서버가 주고받는 메세지들은 서로 완전히 독립적

## 어떻게 로그인 상태를 유지할까?

- HTTP 특성에 의해서 원래는 로그인하고 난 뒤 다른 페이지로 이동하면 로그인 상태가 유지되지 않아야함
  - “쿠키와 세션"으로 로그인 상태를 유지할 수 있음
- 비연결지향에 의해 무상태가 나오고
  - 이를 해결하기 위한 기술이 쿠키와 세션
- **서버와 클라이언트 간 지속적인 상태 유지를 위해 “쿠키와 세션"이 존재**

# 쿠키(Cookie)

- HTTP 쿠키는 “상태가 있는 세션”을 만들도록 해줌

## 개념

- 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각이다
  - 쉽게 말해 브라우저에서 했던 행동을 저장해놓을 수 있는 곳
    - KEY-VALUE 형태로 저장
- 사용자가 웹사이트를 방문할 경우 해당 웹사이트의 서버를 통해 사용자의 컴퓨터에 설치되는 작은 기록 정보 파일
  1. 브라우저(클라이언트)는 쿠키를 로컬에 KEY-VALUE의 데이터 형식으로 저장
  2. 이렇게 쿠키를 저장해 놓았다가, **동일한 서버에 재요청 시 저장된 쿠키를 함께 전송**
- 쿠키는 두 요청이 동일한 브라우저에서 들어왔는지 아닌지를 판단할 때 주로 사용됨
  - 이를 이용해 사용자의 로그인 상태를 유지할 수 있음
    - 쿠키에 “나 로그인된 사용자야"라는 정보를 담아 매 요청마다 서버에 전송하는 것
  - 상태가 없는(stateless) HTTP 프로토콜에서 상태 정보를 기억시켜주기 때문
- 즉, 웹 페이지에 접속하면 웹 페이지를 응답한 서버로부터 쿠키를 받아 브라우저에 저장하고, 클라이언트가 같은 서버에 재요청 시마다 요청과 함께 저장해둔 쿠키도 함께 전송

<img width="1176" alt="dj_85" src="https://user-images.githubusercontent.com/86648892/189502186-1f8fd6e9-96f0-409a-b32c-1e969f5c9022.png">

## 쿠키 사용 목적

1. 세션 관리(Session Management)
   - 로그인, 아이디 자동완성, 공지 하루 안보기, 팝업 체크, 장바구니 등의 정보 관리
2. 개인화(Personalization)
   - 사용자 선호, 테마 등의 설정
3. 트래킹(Tracking)
   - 사용자 행동을 기록 및 분석
     - 어떤 상품을 많이 봤는지 등

## 쿠키 확인

- 개발자도구 - Network 탭

<img width="647" alt="dj_86" src="https://user-images.githubusercontent.com/86648892/189502187-073710a1-dd7b-474a-96a3-c3214d9a2f02.png">

- 서버는 Set-Cookie 응답 헤더를 브라우저에게 전송
  - 이 헤더를 통해 클라이언트에게 쿠키를 저장하라고 전달

<img width="697" alt="dj_87" src="https://user-images.githubusercontent.com/86648892/189502189-634de91f-41be-4202-b8f9-149678e5e125.png">

- 브라우저 역시 서버로 전송되는 모든 요청에 Cookie HTTP 헤더를 사용해 서버로 이전에 저장했던 모든 쿠키들을 함께 전송
  - 위 예시는 쿠팡 장바구니 정보를 저장
- 개발자도구 - Application 탭 - Cookies
  - 저장되어 있는 쿠키 확인

<img width="755" alt="dj_88" src="https://user-images.githubusercontent.com/86648892/189502190-f6e16994-6d70-4ddd-ab06-192f4982cf6b.png">

- 쿠키를 지우면(우측 클릭 - Clear) 상태가 유지되지 않는 것을 확인할 수 있음

# 세션(Session)

- 사이트와 특정 브라우저 사이의 “state(상태)”를 유지시키는 것
- 클라이언트가 서버에 접속하면
  - 서버가 특정 session id를 발급하고, 클라이언트는 session id를 쿠키에 저장
    - 클라이언트가 다시 동일한 서버에 접속하면 요청과 함께 쿠키(session id가 저장된)를 서버에 전달
      - 쿠키는 요청 때마다 서버에 함께 전송되므로 서버에서 session id를 확인해 알맞은 로직을 처리
- session id는 세션을 구별하기위해 필요하며, 쿠키에는 session id만 저장

### 쿠키 Lifetime(수명)

1. **Session cookie**
   - 현재 세션(current session)이 종료되면 삭제됨
   - 브라우저 종료와 함께 세션이 삭제됨
2. **Persistent cookies**
   - Expires 속성에 지정된 날짜 혹은 Max-Age 속성에 지정된 기간이 지나면 삭제됨

## Session in Django

- Django는 **database-backed sessions 저장 방식**을 기본값으로 사용
  - session 정보는 Django DB의 **django_session 테이블**에 저장됨
  - 설정을 통해 다른 저장 방식으로 변경 가능
    - [Django Docs - How to use sessions](https://docs.djangoproject.com/en/4.1/topics/http/sessions/)
- Django는 특정 session id를 포함하는 쿠키를 사용해서 각각의 브라우저와 사이트가 연결된 session을 알아냄
- 사용자에게는 session_key만 줌
  - 사용자에 대한 중요한 정보는 session_data에 담아 서버가 들고있음

---

# Authentication in Web requests

- Django가 제공하는 인증 관련 built-in forms
  - 인증은 직접 form을 구현하기 어렵기에 Django에서 로그인, 가입, 비밀번호 변경 등 인증 관련 built-in forms를 제공함
    - [Django Docs - Built-in forms](https://docs.djangoproject.com/en/4.1/topics/auth/default/#module-django.contrib.auth.forms)

# Login

- 로그인은 **Session을 Create**하는 과정

## AuthenticationForm

- 로그인을 위한 built-in form
  - 로그인하고자 하는 사용자 정보를 입력받음
  - 기본적으로 username과 password를 받아 데이터가 유효한지 검증

### 로그인 구현

- 로그인 로직
  - ID와 PW를 비교하여 일치하는지 확인하고
    - 일치한다면 session을 생성하고
      - 해당 sessionid를 돌려주고 쿠키에 담음
  - 이것을 AuthenticationForm을 통해 쉽게 구현
- 로그인 페이지 구현
  - 페이지 렌더링
    - GET
  - 인증
    - POST
- `AuthenticationForm()`
  - `class AuthenticationForm(forms.Form)`
    - request를 첫번째 인자로 취함
    - Form을 상속받음
      - 인증에만 쓰이고 DB를 다루는 것은 아니기에 ModelForm일 필요없음

<img width="500" alt="dj_89" src="https://user-images.githubusercontent.com/86648892/189502191-2590ffef-2ee7-4f72-acd4-41b9cb0f5f35.png">

<img width="617" alt="dj_90" src="https://user-images.githubusercontent.com/86648892/189502193-9b534508-c8a6-4ca0-b606-09644b3aadfc.png">

- `from django.contrib.auth.forms import AuthenticationForm`
- `login()`
  - `login(request, user, backend=None)`
    - 인증된 사용자를 로그인시키는 로직으로 view 함수에서 사용
      - 입력된 데이터 판단 → 현재 세션에 데이터를 입력 → 로그인
    - 현재 세션에 연결하려는 인증된 사용자가 있는 경우 사용
    - HttpRequest 객체와 User 객체가 필요
  - views 함수의 login 함수와 이름 중복을 피하기 위해 `import login as auth_login`
  - `get_user()`
    - AuthenticationFrom의 인스턴스 메서드
    - 유효성 검사를 통과했을 경우 로그인한 사용자 객체를 반환

### 세션 데이터 확인

- 로그인 후 개발자 도구와 DB에서 Django로부터 발급받은 세션 확인
  - django_session 테이블에서 확인
  - 브라우저의 개발자도구 - Application - Cookies에서 확인

## Templates and Context Processors

- 템플릿에서 인증 관련 데이터 출력

<img width="614" alt="dj_91" src="https://user-images.githubusercontent.com/86648892/189502194-162af42e-cad5-409e-acfd-336f7e405eaa.png">

- context 데이터가 없는데 user 변수를 어떻게 사용할 수 있을까?

  - `settings.py`의 **context processors** 설정값 때문
  - `context_processors`

    - 템플릿이 렌더링될 때 호출 가능한 컨텍스트 데이터 목록

      - 작성된 컨텍스트 데이터는 기본적으로 템플릿에서 사용가능한 변수로 포함됨
      - 즉, Django에서 자주 사용하는 데이터 목록을 미리 템플릿에 로드해둔 것
        <img width="584" alt="dj_92" src="https://user-images.githubusercontent.com/86648892/189502195-14fe5b93-697e-4b49-a95e-b4adcab57e4d.png">

      - user 변수를 담당하는 프로세서는 `django.contrib.auth.context_processors.auth`
        - [Django Docs - Built-in template context processors](https://docs.djangoproject.com/en/4.1/ref/templates/api/#built-in-template-context-processors)
      - `user` 의 경우 인증된 사용자라면 `User()` 클래스 인스턴스로 출력, 인증되지 않은 사용자라면 `AnonymousUser()` 클래스 인스턴스로 출력

# Logout

- 로그아웃은 **Session을 Delete**하는 과정
  - 클라이언트(sessionid)와 서버에 있는 세션 정보를 삭제
  - 유저 정보 삭제가 아님
    - 유저 정보 삭제는 회원탈퇴
- `logout(request)`
  - HttpRequest 객체를 인자로 받고 반환값이 없음
  - 사용자가 로그인하지 않은 경우 오류를 발생시키지 않음
  - 2가지 일 처리
    1. 현재 요청에 대한 session data를 DB에서 삭제
    2. 클라이언트의 쿠키에서도 sessionid를 삭제
    - 이는 다른 사람이 동일한 웹 브라우저를 사용하여 로그인하고, 이전 사용자의 세션 데이터에 액세스하는 것을 방지하기 위함

<img width="1191" alt="dj_93" src="https://user-images.githubusercontent.com/86648892/189502196-6fab2e54-ee7b-4276-a1ee-1a0f3c70f572.png">

---

# 회원 가입

- 회원가입은 User를 **Create**하는 것이며 **UserCreationForm**이라는 built-in form 사용

## UserCreationForm

- 주어진 username과 password로 권한이 없는 새 user를 생성하는 ModelForm
- 3개의 필드를 가짐
  1. username (from the user model)
  2. password1
  3. password2
- `signup()`
  - 회원가입 페이지를 렌더링할 페이지 생성
  - 새로운 유저 모델 생성

<img width="533" alt="dj_94" src="https://user-images.githubusercontent.com/86648892/189502197-aa0c7e9c-2804-4e80-a0f4-d32cfe32b174.png">

<img width="634" alt="dj_95" src="https://user-images.githubusercontent.com/86648892/189502198-f99cdf80-c22a-4169-bbd4-c40ef035a204.png">

<img width="718" alt="dj_96" src="https://user-images.githubusercontent.com/86648892/189502199-c47a2024-7c9b-4cff-af36-9f3b709db91a.png">

### 에러 페이지 확인

<img width="945" alt="dj_97" src="https://user-images.githubusercontent.com/86648892/189502201-697a1e10-a251-44f4-a6f4-60ab7d861edd.png">

- `UserCreationForm()`은 ModelForm으로 우리가 대체한 커스텀 유저 모델이 아닌 기존 유저 모델을 바탕으로 작성된 클래스
  - built-in User model인 ‘auth.User’를 바탕으로 만들어짐
    - class Meta에 `model = User` 로 적혀있음
    - 상속을 통해 Meta 정보를 바꿔줘야 한다
      - accounts의 `forms.py`에서 `CustomUserCreationForm()` 생성

# Custom user & Built-in auth forms

- 기존 User 모델을 참조하는 Form인지 여부

### AbstractBaseUser의 모든 subclass와 호환되는 forms

- User 모델을 대체하더라도 커스텀하지 않아도 되는 Form 클래스
  1. AuthenticationForm
  2. SetPasswordForm
  3. PasswordChangeForm
  4. AdminPasswordChangeForm
- 기존 User 모델을 참조하는 Form이 아님

### 커스텀 유저 모델을 사용하려면 다시 작성하거나 확장해야하는 forms

1. UserCreationForm
   - 회원가입
2. UserChangeForm
   - 회원정보수정

- 두 form 모두 `class Meta: model = User` 가 등록된 form이기에 반드시 커스텀(확장)해야함

## CustomUserCreationForm()

<img width="849" alt="dj_98" src="https://user-images.githubusercontent.com/86648892/189502202-81532ad9-5622-4759-87b1-2fd7d1ec9be6.png">

### `get_user_model()`

- **현재 프로젝트에서 활성화된 사용자 모델(active user model)**을 반환
- 직접 커스텀 유저 모델을 import해서 참조할 수도 있으나
  - Django는 User 클래스를 직접 참조하는 대신 `get_user_model()` 을 사용해 참조해야한다고 강조함
- 직접 참조하지 않는 이유
  - 예를 들어 기존 User 모델이 아닌 User 모델을 커스텀한 상황에서는 커스텀 User 모델을 자동으로 반환해주기 때문

<img width="724" alt="dj_99" src="https://user-images.githubusercontent.com/86648892/189502203-a09403a1-1f7e-45a1-8dbe-5c1a2244957b.png">

<img width="749" alt="dj_100" src="https://user-images.githubusercontent.com/86648892/189502204-ced07494-fb5e-40e4-a3d4-a34f1106cf1e.png">

### [참고] UserCreationForm의 save()

- user를 반환함

<img width="771" alt="dj_101" src="https://user-images.githubusercontent.com/86648892/189502205-7cade324-21f5-4fc1-b2f9-7ee5dff4b131.png">

# 회원 탈퇴

- 회원 탈퇴는 DB에서 유저 모델을 **Delete**하는 것

<img width="517" alt="dj_102" src="https://user-images.githubusercontent.com/86648892/189502207-a78c2b8a-583a-465c-80bf-1ee0bc1d89e0.png">

<img width="555" alt="dj_103" src="https://user-images.githubusercontent.com/86648892/189502208-a464a491-710d-4392-be36-37a82514010b.png">

<img width="613" alt="dj_104" src="https://user-images.githubusercontent.com/86648892/189502210-197d028d-adb2-4c93-9b45-dd21558b1c20.png">

### [참고] 탈퇴하면서 해당 유저의 세션 정보도 함께 지우고 싶을 경우

- 순서가 중요
- `request.user.delete()`
  - 탈퇴
  - `auth_logout(request)`
    - 로그아웃
- 로그아웃을 먼저 하면 요청의 객체 정보가 사라져 탈퇴에 필요한 정보가 사라짐

# 회원정보 수정

- 회원정보 수정은 User를 **Update**하는 것이며 **UserChangeForm** built-in form을 사용

## UserChangeForm

- 사용자의 정보 및 권한을 변경하기 위해 admin 인터페이스에서 사용되는 ModelForm
  - admin 페이지에서 이미 쓰고있는 것을 사용자에게도 보여주자는 것
- UserChangeForm 또한 ModelForm이기에 instance 인자 설정
- CustomUserCreationForm과 같이 CustomUserChangeForm 사용
- 유저 모델을 다루기에 ModelForm
- admin 인터페이스에서 사용됨 (admin 페이지)
- admin 페이지에서 이미 쓰고있는 것을 사용자에게도 보여주자

<img width="537" alt="dj_105" src="https://user-images.githubusercontent.com/86648892/189502211-4aef9f08-8bef-455d-bc0c-9e948fa21bd8.png">

<img width="539" alt="dj_106" src="https://user-images.githubusercontent.com/86648892/189502212-960971b6-de62-4ccb-a1d8-d59d5f88f271.png">

<img width="742" alt="dj_107" src="https://user-images.githubusercontent.com/86648892/189502213-ddfcbbe1-35e2-438f-8596-d9f2527a733f.png">

<img width="839" alt="dj_108" src="https://user-images.githubusercontent.com/86648892/189502214-f08ca6d0-d437-44b5-8c54-a592b92236c6.png">

<img width="510" alt="dj_109" src="https://user-images.githubusercontent.com/86648892/189502216-3b29a597-dc96-49ee-bb2d-7b2690e96ccb.png">

### UserChangeForm의 필드 변경

<img width="935" alt="dj_110" src="https://user-images.githubusercontent.com/86648892/189502217-c94ae010-58e0-4ee5-b75a-7b3414479ae6.png">

- 필드 설정을 하지 않을 시 일반 사용자가 접근해서는 안될 정보들(fields)까지 모두 수정이 가능해짐
  - admin 인터페이스에서 사용되는 ModelForm이기 때문
- 따라서 UserChangeForm을 상속받아 작성해둔 서브클래스 CustomUserChangeForm에서 접근 가능한 필드를 조정
- User 모델의 fields명은 migrations 파일이나 공식문서에서 확인
  - [Django Docs - User model Fields](https://docs.djangoproject.com/en/4.1/ref/contrib/auth/#fields)

---

# 비밀번호 변경

## PasswordChangeForm

- 사용자가 비밀번호를 변경할 수 있도록 하는 Form
- 이전 비밀번호를 입력하여 비밀번호를 변경할 수 있도록 함
- 이전 비밀번호를 입력하지 않고 비밀번호를 설정할 수 있는 SetPasswordForm을 상속받는 서브클래스
- Django에서 내부적으로 폼을 누르면 `/accounts/password/` 로 보냄
  - 여기에 맞춰서 url 설정
- `from django.contrib.auth.forms import PasswordChangeForm`

<img width="556" alt="dj_111" src="https://user-images.githubusercontent.com/86648892/189502218-10a11997-5813-4e5b-ab4b-57568dc13253.png">

<img width="557" alt="dj_112" src="https://user-images.githubusercontent.com/86648892/189502219-575582e1-4298-4d56-b250-79e680baf093.png">

<img width="804" alt="dj_113" src="https://user-images.githubusercontent.com/86648892/189502220-0a84a68e-e24e-4735-982a-4e534dcdcace.png">

### 암호 변경 시 세션 무효화 방지

- 비밀번호 변경이 성공적으로 진행되면 로그아웃됨
  - 비밀번호가 변경되면 기존 세션과의 회원 인증 정보가 일치하지 않아서 로그인 상태가 유지되지 못함
  - 비밀번호는 잘 변경되었으나 비밀번호가 변경되면서 기존 세션과의 회원 인증 정보가 일치하지않기 때문
  - 기존 세션과의 싱크업 과정이 필요함
    - `update_session_auth_hash(request, user)`

### `update_session_auth_hash(request, user)`

- 현재 요청(current request)과 새 session data가 파생될 업데이트된 user 객체를 가져오고, session data를 적절하게 업데이트
- 암호가 변경되어도 로그아웃되지 않도록 새로운 password의 session data로 session을 업데이트

---

# Limiting access to logged-in users

- 로그인 사용자에 대한 접근 제한하기
- 로그인 사용자에 대해 접근을 제한하는 2가지 방법
  1. `is_authenticated` attribute
  2. `login_required` decorator

## is_authenticated

- User model의 속성(attributes) 중 하나
- 사용자가 인증되었는지 여부를 알 수 있는 방법
- 모든 User 인스턴스에 대해 항상 True인 읽기 전용 속성
  - AnonymousUser에 대해서는 항상 False
- 일반적으로 `request.user` 에서 이 속성을 사용
  - `request.user.is_authenticated`
- 권한(permission)과는 관련이 없으며, 사용자가 활성화 상태(active)이거나 유효한 세션(valid session)을 가지고 있는지도 확인하지 않음

<img width="848" alt="dj_114" src="https://user-images.githubusercontent.com/86648892/189502222-52c4c831-f217-4881-a62e-4f5c0f299d32.png">

### is_authenticated 적용

- 로그인과 비로그인 상태에서 출력되는 링크를 다르게 설정

<img width="750" alt="dj_115" src="https://user-images.githubusercontent.com/86648892/189502224-e7c19354-43b5-442e-9a64-ac4600f8cb91.png">

- 인증된 사용자만 게시글 작성 링크를 볼 수 있도록 처리
  - 아직 비로그인 상태로도 URL을 직접 입력하면 게시글 작성 페이지로 갈 수 있긴함
    - `login_required` 데코레이터를 향후 활용하여 처리

<img width="886" alt="dj_116" src="https://user-images.githubusercontent.com/86648892/189502225-08a8fb0e-4777-4a1f-bf92-c8c8cff46611.png">

- 인증된 사용자라면 로그인 로직을 수행할 수 없도록 처리

<img width="629" alt="dj_117" src="https://user-images.githubusercontent.com/86648892/189502227-e0e1c5b2-d7b9-49ac-95e5-0b8bb0612c1c.png">

## login_required

- login_required decorator
- 사용자가 로그인되어 있다면 정상적으로 view 함수 실행
- 로그인하지 않은 사용자의 경우 `settings.py` 의 `LOGIN_URL` 문자열 주소로 redirect
  - `LOGIN_URL`의 기본값은 `/accounts/login/`
  - app 이름을 accounts로 했던 이유 중 하나!
  - `/articles/create/` 로 강제 접속을 시도해보면 로그인 페이지로 리다이렉트 후 `/accounts/login/?next=/articles/create/` url을 확인할 수 있음
    - **인증 성공 시 사용자가 redirect되어야하는 경로는 “next”라는 쿼리 문자열 매개 변수에 저장됨**

### login_required 적용

- 로그인 상태에서만 글을 작성, 수정, 삭제할 수 있도록 변경

<img width="760" alt="dj_118" src="https://user-images.githubusercontent.com/86648892/189502228-0c477880-3631-4702-95f7-dc7fc44d07af.png">

### “next” query string parameter

- 로그인이 정상적으로 진행되면 이전에 요청했던 주소로 redirect하기 위해 Django가 제공해주는 쿼리 스트링 파라미터
- 해당 값을 처리할지 말지는 자유이며 별도로 처리해주지 않으면 view에 설정한 redirect 경로로 이동하게됨

<img width="903" alt="dj_119" src="https://user-images.githubusercontent.com/86648892/189502229-8feaee79-3b9c-4e4a-9178-a381bedffa09.png">

<img width="731" alt="dj_120" src="https://user-images.githubusercontent.com/86648892/189502230-b4977862-a594-44da-8606-ce65566161d2.png">

- `/accounts/login/` 과 `/accounts/login/?next=...` 인 경우 2가지를 처리해야 하므로 현재 url로 요청을 보내도록 `action=""` 으로 변경

---

### `@login_required` 와 `@require_POST` 충돌

- `@login_required` 는 GET request method를 처리할 수 있는 view 함수에서만 사용
- 게시글 삭제(delete) 함수 예시
  - 원래는 게시글 삭제 버튼 누르면 해당 url로 POST 요청하여 삭제
  - 비로그인 상태로 detail 페이지에서 게시글 삭제 시도
    - login_required에 의해 로그인 페이지로 리다이렉트
      - `http://127.0.0.1:8000/accounts/login/?next=/articles/1/delete/`
      - 로그인 완료하면
        - 더이상 버튼에 의한 POST 요청이 아닌 해당 url을 통해 GET 요청으로 변함
        - require_POST와 충돌
          - 405(Method Not Allowed) status code
- 2가지 문제가 발생
  1. redirect 과정에서 POST 요청 데이터의 손실
  2. redirect로 인한 요청은 GET 요청 메서드로만 요청됨
- POST method만 허용하는 delete같은 함수는 내부에서 `is_authenticated` 속성을 통해 처리

<img width="667" alt="dj_121" src="https://user-images.githubusercontent.com/86648892/189502231-94a64121-3512-43cf-9f60-b94e0957a3a6.png">

---

### accounts view 함수에도 이처럼 데코레이터 및 속성값 적용

<img width="913" alt="dj_122" src="https://user-images.githubusercontent.com/86648892/189502232-8c482901-5c4a-4440-a1e0-cee796cb0402.png">

---

## 정리

- The Django authentication system
  - User 모델 대체하기
- HTTP Cookies
  - 상태가 있는 세션 구성
- Authentication in Web requests
  - auth built-in form 사용하기
- Authentication in User
  - User Object와 User CRUD

---

# [추가] 패스워드 저장

- [안전한 패스워드 저장](https://d2.naver.com/helloworld/318732)
- [Django Docs - Password management in Django](https://docs.djangoproject.com/en/3.2/topics/auth/passwords/)

## 패스워드 저장 알고리즘

- password는 유저 모델의 필드가 아니다
  - 따로 저장됨
- 비밀번호를 저장할 땐 어떤 방식(알고리즘)을 사용하는가?
  - 단순 텍스트
    - 말도 안됨
  - 단방향 해쉬 함수의 다이제스트
    - 보완 알고리즘
      - 솔팅(Salting)
      - 키 스트레칭(Key Stretching)

<img width="857" alt="dj_123" src="https://user-images.githubusercontent.com/86648892/189502470-8db20282-1b2b-4d91-a5e4-d644acf53e70.png">

- 솔팅과 키 스트레칭을 바탕으로 한 검증된 Adaptive Key Derivation Function
  - PBKDF2
  - bcrypt
  - scrypt

## 패스워드 저장 in Django

Django는 비밀번호 저장을 위해 salting과 key stretching을 바탕으로 한 adaptive key derivation function 중 PBKDF2를 기본으로 채택하고 있다.

- User 객체의 password 속성에 부여되는 비밀번호 값은 `<algorithm>$<iterations>$<salt>$<hash>` 포맷의 문자열이다.
- 이러한 저장값을 생성하기 위해 사용하는 해쉬 함수는 Django의 `PASSWORD_HASHERS`를 통해 설정되며, 기본 코드는 다음과 같다.

```python
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]
```

- Django는 `PASSWORD_HASHERS`의 첫번째 값, 즉 `settings.PASSWORD_HASHERS[0]`을 참조하여 암호 저장 알고리즘을 채택한다.
- 위 코드의 경우 PBKDF2 방식으로 저장은 하지만, 암호 검사 시 PBKDF2SHA1, argon2, bcrypt 방식도 지원함을 뜻한다.

---

# Django N:1 Relationship

- A-many-to-one-relationship
- N : 1 (Comment - Article)
- N : 1 (Article - User)
- N : 1 (Comment - User)

---

# A-many-to-one-relationship

- 관계형 데이터베이스에서의 외래키 속성을 사용해 모델간 N:1 관계 설정하기
- 외래 키(ForeignKey)를 사용하여 RDB의 테이블 간 관계를 만들 수 있음
  - 관계(Relationship)란?
    - 테이블 간의 상호작용을 기반으로 설정되는 여러 테이블 간의 논리적인 연결

### 테이블 간 관계 예시

<img width="1176" alt="dj_124" src="https://user-images.githubusercontent.com/86648892/212546968-e41f595f-7e34-4ab4-8970-35446e7ecceb.png">

## RDB에서의 관계

1. `1:1`
   - One-to-one relationships
   - 한 테이블의 레코드 하나가 다른 테이블의 레코드 단 한 개와 관련된 경우
2. `N:1`
   - Many-to-one relationships
   - 한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 한 개와 관련된 경우
   - 기준 테이블에 따라 1:N, One-to-many relationships라고도 함
3. `M:N`
   - Many-to-many relationships
   - 한 테이블의 0개 이상의 레코드가 다른 테이블의 0개 이상의 레코드와 관련된 경우
   - 양쪽 모두에서 N:1 관계를 가짐

## Django Relationship Fields

1. `OneToOneField()`
   - A one-to-one relationship
2. `ForeignKey()`
   - A many-to-one relationship
3. `ManyToManyField()`
   - A-many-to-many relationship

---

## Foreign Key

- 외래 키 (외부 키)
- 관계형 데이터베이스에서 다른 테이블의 행을 식별할 수 있는 키
- 참조되는 테이블의 기본 키(Primary Key)를 가리킴
- 참조하는 테이블의 행 1개의 값은, 참조되는 측 테이블의 행 값에 대응됨
  - 즉, 참조하는 테이블의 행에는, 참조되는 테이블에 나타나지 않는 값을 포함할 수 없음
- 참조하는 테이블 행 여러 개가, 참조되는 테이블의 동일한 행을 참조할 수 있음
- **부모 테이블의 유일한 값을 참조**
  - **참조 무결성**
  - **외래 키의 값이 반드시 부모 테이블의 Primary Key일 필요는 없지만 유일한 값이어야 함**

### [참고] 참조 무결성

- 데이터베이스 관계 모델에서 관련된 2개의 테이블 간의 일관성을 말함
- 외래 키가 선언된 테이블의 외래 키 속성(열)의 값은 그 테이블의 부모가 되는 테이블의 기본 키 값으로 존재해야 함

## `ForeignKey(to, on_delete, **options)`

- A many-to-one relationship을 담당하는 Django의 모델 필드 클래스
- Django 모델에서 관계형 데이터베이스의 외래 키 속성을 담당
- 2개의 필수 위치 인자가 필요
  1. **참조하는 model class**
  2. `***on_delete` 옵션
     - 외래 키가 참조하는 객체가 사라졌을 때, 외래 키를 가진 객체를 어떻게 처리할지 정의
     - 데이터 무결성을 위해 매우 중요한 설정
     - `on_delete` 옵션 값
       - `CASCADE`
         - 부모 객체(참조된 개체)가 삭제되었을 때 이를 참조하는 객체도 삭제
       - `PROJECT`
         - 참조하는 객체가 있다면 참조되는 해당 객체를 못지우도록 설정
       - `SET_NULL`
         - 부모 객체가 삭제되었을 때 참조하는 객체의 값을 NULL로 설정
       - `SET_DEFAULT`
         - 부모 객체가 삭제되었을 때 참조하는 객체의 값을 설정한 기본값으로 대체

### [참고] 데이터 무결성 (Data Integrity)

- 데이터의 정확성과 일관성을 유지하고 보증하는 것
- 데이터베이스나 RDBMS의 중요한 기능
- 무결성 제한의 유형
  1. 개체 무결성 (Entity Integrity)
  2. 참조 무결성 (Referential Integrity)
  3. 범위 무결성 (Domain Integrity)

---

## Related Manager (관계 모델 참조)

- Related manager는 N:1 혹은 M:N 관계에서 사용가능한 문맥(context)
- Django는 모델 간 N:1 혹은 M:N 관계가 설정되면 `역참조` 할 때에 사용할 수 있는 manager를 생성
  - 이전에 모델 생성 시 `objects` 라는 매니저를 통해 queryset api를 사용했던 것처럼
    - Related manager를 통해 queryset api를 사용할 수 있게 됨
- N:1 관계에서 생성되늰 Related manager 이름은 참조하는 **“모델명_set”** 이름 규칙으로 만들어짐
  - `ForeignKey()` 설정 시 `related_name` 옵션을 통해 역참조 시 사용할 매니저 이름을 설정 가능
    - 작성 후 migration 과정 필요
    - 설정 시 기존의 `modelName_set` 은 더이상 사용할 수 없고, 대체됨

## 역참조

- 나를 참조하는 테이블(나를 외래 키로 지정한)을 참조하는 것
  - 본인을 외래 키로 참조 중인 다른 테이블에 접근하는 것
  - N:1에서는 1이 N을 참조하는 상황

<img width="1163" alt="dj_125" src="https://user-images.githubusercontent.com/86648892/212546967-3acdd5b9-c4b5-45df-81b3-a240c8f7b9e0.png">

<img width="1090" alt="dj_126" src="https://user-images.githubusercontent.com/86648892/212546965-bef1a122-25cb-402b-9978-f9f6229b8a2c.png">

---

# Referencing the User Model

## Django에서 User 모델을 참조하는 2가지 방법

1. `settings.AUTH_USER_MODEL`
   - 문자열을 반환
     - 반환값은 ‘accounts.User’ (문자열)
   - User 모델에 대한 외래 키 또는 M:N 관계를 정의할 때 사용
   - **`models.py`의 모델 필드에서 User 모델을 참조할 때 사용**
     - 장고 내부적인 동작순서에 따라 아직 유저 객체가 생성되지 않은 시점에서 `models.py` 가 임시로 참조할 수 있도록 문자열을 주는 것
2. `get_user_model()`
   - 객체를 반환
     - 반환값은 User Object (객체)
   - 현재 활성화(Active)된 User 모델을 반환
     - 커스터마이징한 User 모델이 있을 경우는 Custom User 모델, 그렇지 않으면 User를 반환
   - **`models.py` 가 아닌 다른 모든 곳에서 유저 모델을 참조할 때 사용**

---

# N : 1 (Comment - Article)

- Comment(N) - Article(1)
- Comment 모델과 Article 모델 간 관계 설정
- “0개 이상의 댓글은 1개의 게시글에 작성될 수 있음”

<img width="1068" alt="dj_127" src="https://user-images.githubusercontent.com/86648892/212546962-d8c3df94-0bf4-4c13-bfdb-d6fd8085367e.png">

## Comment 모델 정의

<img width="815" alt="dj_128" src="https://user-images.githubusercontent.com/86648892/212546960-57b2b1a5-8516-432e-9a8d-45ab168403dd.png">

- 외래 키 필드는 ForeignKey 클래스를 작성하는 위치와 관계없이 필드의 마지막에 작성됨
- `ForeignKey()` 클래스의 인스턴스 이름은 참조하는 모델 클래스 이름의 단수형(소문자)으로 작성하는 것을 권장
  - migration 과정 진행
    <img width="1068" alt="dj_129" src="https://user-images.githubusercontent.com/86648892/212546959-901cce13-1e0e-4a21-a31b-9f54c93ea9f8.png">

<img width="1046" alt="dj_130" src="https://user-images.githubusercontent.com/86648892/212546958-c2b7c241-b9cd-45dc-ac8c-5f55dd9a790f.png">

<img width="1031" alt="dj_131" src="https://user-images.githubusercontent.com/86648892/212546957-46ab927b-8bec-4c80-8105-3f5b87e3b176.png">

<img width="1025" alt="dj_132" src="https://user-images.githubusercontent.com/86648892/212546956-631d339f-286c-46c0-8803-82cb36939db4.png">

<img width="1030" alt="dj_133" src="https://user-images.githubusercontent.com/86648892/212546954-72bf657e-4e90-41c1-a457-54af27b340aa.png">

---

# Comment CRUD 구현

## CREATE

- CommentForm 작성
  - 외래 키 필드는 사용자로부터 받는 입력이 아니므로 출력에서 제외
- 기존의 ArticleForm 클래스의 인스턴스명을 `form` 으로 작성했기에 헷갈리지 않도록 `comment_form` 으로 작성
- 출력에서 제외된 외래 키의 경우 url에서 `variable routing` 을 활용하여 받아온 pk값을 활용
- `***save(commit=False)` 옵션 활용\*\*\*
  - “Create, but don’t save the new instance”
    - 아직 데이터베이스에 저장되지 않은 인스턴스를 반환
    - 저장하기 전에 객체에 대한 사용자 지정 처리를 수행할 때 유용하게 사용
  - commit 옵션을 활용해 DB에 저장되기 전 comment 객체에 article 객체 저장하기

<img width="605" alt="dj_134" src="https://user-images.githubusercontent.com/86648892/212546952-62aaed63-6e6e-4ff6-85b5-38d784e89232.png">

<img width="717" alt="dj_135" src="https://user-images.githubusercontent.com/86648892/212546951-b6de9101-d9b6-453f-adf5-d7b8a86426fa.png">

<img width="562" alt="dj_136" src="https://user-images.githubusercontent.com/86648892/212546950-d099bacf-1862-4ca7-ae28-804bd4e9e0cb.png">

<img width="560" alt="dj_137" src="https://user-images.githubusercontent.com/86648892/212546949-40d98ce4-ba67-4f74-9161-cdcac7eaadf2.png">

---

## READ

- 작성한 댓글 목록 출력하기
- 특정 article에 있는 모든 댓글을 가져온 후 context에 추가
- detail 템플릿에서 댓글 목록 출력하기

<img width="723" alt="dj_138" src="https://user-images.githubusercontent.com/86648892/212546948-e64c7719-527d-4ca0-afc1-0359ff91df7a.png">

<img width="723" alt="dj_139" src="https://user-images.githubusercontent.com/86648892/212546947-f749bcae-b663-4ff8-9837-1911b56d5c8e.png">

## DELETE

- 댓글 삭제 구현하기
- 댓글을 삭제할 수 있는 버튼을 각각의 댓글 옆에 출력될 수 있도록 함

<img width="1154" alt="dj_140" src="https://user-images.githubusercontent.com/86648892/212546945-88fc2e31-b48e-4e90-aa17-e7f68412c031.png">

<img width="710" alt="dj_141" src="https://user-images.githubusercontent.com/86648892/212546943-ddfed818-4ea8-4950-bc36-8d2cd3f195dc.png">

<img width="1026" alt="dj_142" src="https://user-images.githubusercontent.com/86648892/212546939-04c8bad3-623c-4dd1-8a41-c3ee25b536c2.png">

## UPDATE

- 댓글 수정은 구현하지 않음
  - 댓글 수정을 구현할 경우 게시글 수정 페이지가 필요했던 것처럼 댓글 수정 페이지가 필요
  - 하지만 일반적으로 댓글 수정은 수정 페이지로의 이동없이 현재 페이지를 유지한 상태로 댓글 작성 Form 부분만 변경되어 수정할 수 있도록 함
  - 이처럼 페이지의 일부 내용만 업데이트하는 것은 JavaScript의 영역이기 때문에 JavaScript를 학습한 후 별도로 진행

---

## DTL(Django Template Language)과 QuerySet API를 활용한 추가 댓글 구현 사항

### 댓글 개수 출력하기

<img width="768" alt="dj_143" src="https://user-images.githubusercontent.com/86648892/212546934-3a161a94-3fe7-4288-b76d-273c8d44e032.png">

<img width="951" alt="dj_144" src="https://user-images.githubusercontent.com/86648892/212546930-87135284-fbee-403e-9cbd-5b38dccb1970.png">

### 댓글이 없는 경우 대체 컨텐츠 출력하기

<img width="1162" alt="dj_145" src="https://user-images.githubusercontent.com/86648892/212546925-90d84a12-d382-4864-998d-a70c5ef51533.png">

---

# N : 1 (Article - User)

- Article(N) - User(1)
- Article 모델과 User 모델 간 관계 설정
- “0개 이상의 게시글은 1개의 회원에 의해 작성될 수 있음”
- Article 모델에 User 모델을 참조하는 외래 키 작성
  - migration 진행

<img width="1072" alt="dj_146" src="https://user-images.githubusercontent.com/86648892/212546924-3268cef1-0d14-4b05-8023-2b8c66154396.png">

<img width="1091" alt="dj_147" src="https://user-images.githubusercontent.com/86648892/212546923-3aefe3fb-9fc7-4c86-807d-93d3518bf9b5.png">

<img width="1071" alt="dj_148" src="https://user-images.githubusercontent.com/86648892/212546920-b2fa8f66-0adf-4aa7-a90c-3d00e0cd2514.png">

- 기본적으로 모든 컬럼은 `NOT NULL` 제약조건이 있기에 데이터가 없이는 새로 추가되는 외래 키 필드 user_id가 생성되지 않음
- 기본값을 어떻게 작성할지 선택
- 1을 입력하고 Enter 진행

<img width="1069" alt="dj_149" src="https://user-images.githubusercontent.com/86648892/212546918-e7f98d17-cd34-40b1-9b31-0e5d59031a9e.png">

- articel의 user_id에 어떤 데이터를 넣을 것인지 직접 입력
- 1 입력 후 Enter 진행
- 기존에 작성된 게시글은 모두 1번 회원이 작성한 것으로 처리됨

---

# Article CRUD 구현

## CREATE

- 인증된 회원의 게시글 작성 구현하기
- 작성하기 전 로그인을 먼저 진행한 상태로 진행
- ArticleForm의 출력 필드 수정
  - 사용자로부터 키를 받아오는 것이 아닌 `save(commit=False)` 를 통해 request를 보내는 사용자의 정보를 저장

<img width="606" alt="dj_150" src="https://user-images.githubusercontent.com/86648892/212546914-cfa7d769-9db6-4eab-9f8a-444612069e17.png">

<img width="773" alt="dj_151" src="https://user-images.githubusercontent.com/86648892/212547213-17588ae1-d352-44ef-8c48-cbad2e457c2e.png">

## DELETE

- 이제 게시글에 작성자 정보가 함께 들어있기 때문에 현재 삭제를 요청하려는 사람과 게시글을 작성한 사람을 비교하여 본인의 게시글만 삭제할 수 있도록 함

<img width="723" alt="dj_152" src="https://user-images.githubusercontent.com/86648892/212547212-bacff37d-662c-41d1-b0e3-9b65c8badd5c.png">

## UPDATE

- 수정도 마찬가지로 수정을 요청하려는 사람과 게시글을 작성한 사람을 비교하여 본인의 게시글만 수정할 수 있도록 함
- 추가로 해당 게시글의 작성자가 아니라면, 수정 및 삭제 버튼을 출력하지 않도록 함

<img width="1046" alt="dj_153" src="https://user-images.githubusercontent.com/86648892/212547210-53984eb4-101a-4134-88ce-34cd100daa68.png">

<img width="928" alt="dj_154" src="https://user-images.githubusercontent.com/86648892/212547209-9fb5da4f-bfe3-401d-ba3e-aea72c348d30.png">

## READ

- 게시글 작성자 출력
  - index 템플릿과 detail 템플릿에서 각 게시글의 작성자 출력

<img width="670" alt="dj_155" src="https://user-images.githubusercontent.com/86648892/212547208-01f2ca1f-a5c7-4856-97b5-0d94f03432da.png">

<img width="483" alt="dj_156" src="https://user-images.githubusercontent.com/86648892/212547207-22992f2a-e007-4a67-a636-aad3e22ef4bc.png">

---

# N : 1 (Comment - User)

- Comment(N) - User(1)
- Comment 모델과 User 모델 간 관계 설정
- “0개 이상의 댓글은 1개의 회원에 의해 작성될 수 있음”
- Comment는 Article의 id, User의 id 2개의 ForeignKey를 가지게 됨
- 마찬가지로 migration 진행 및 NOT NULL 제약조건 해결 진행

<img width="1068" alt="dj_157" src="https://user-images.githubusercontent.com/86648892/212547204-5f5d654c-0de0-4569-924a-ba206e4df450.png">

<img width="1066" alt="dj_158" src="https://user-images.githubusercontent.com/86648892/212547202-5c51c9c7-b939-4bc1-a150-dece6c8f0cb5.png">

<img width="1073" alt="dj_159" src="https://user-images.githubusercontent.com/86648892/212547201-6ac030da-782e-4528-9ea9-5c4253c97556.png">

<img width="1069" alt="dj_160" src="https://user-images.githubusercontent.com/86648892/212547199-efc96456-2a57-4a9e-8362-5c45dcef9ccb.png">

---

# Comment CRUD 구현

## CREATE

- 인증된 회원의 댓글 작성 구현하기
- 작성하기 전 로그인을 먼저 진행한 상태로 진행
- CommentForm 출력 필드 수정
  - 사용자로부터 키를 받아오는 것이 아닌 `save(commit=False)` 를 통해 request를 보내는 사용자의 정보를 저장

<img width="607" alt="dj_161" src="https://user-images.githubusercontent.com/86648892/212547198-c074ae3f-5e7c-4759-abea-f024bd10d5a1.png">

<img width="778" alt="dj_162" src="https://user-images.githubusercontent.com/86648892/212547194-7b900712-8877-4e48-a699-aa6439763405.png">

## READ

- detail 템플릿에서 각 게시글의 작성자 출력

<img width="1023" alt="dj_163" src="https://user-images.githubusercontent.com/86648892/212547192-01df4af7-fb52-4973-827b-88026c1c5e3b.png">

## DELETE

- 이제 댓글에는 작성자 정보가 함께 들어있기 때문에 현재 삭제를 요청하려는 사람과 댓글을 작성한 사람을 비교하여 본인의 댓글만 삭제할 수 있도록 함
- 추가로 해당 댓글의 작성자가 아니라면, 삭제 버튼을 출력하지 않도록 함

<img width="776" alt="dj_164" src="https://user-images.githubusercontent.com/86648892/212547191-323eab57-2704-46a4-a23c-6913167a69c2.png">

<img width="1038" alt="dj_165" src="https://user-images.githubusercontent.com/86648892/212547190-433cc569-cf5a-43d7-9e71-0d8a95c019ae.png">

---

## 인증된 사용자에 대한 접근 제한하기

- `is_authenticated`
- `View Decorators`

### 인증된 사용자인 경우만 댓글 작성 및 삭제하기

<img width="923" alt="dj_166" src="https://user-images.githubusercontent.com/86648892/212547189-abb6d252-8fac-4cee-a595-0535c1deecce.png">

<img width="847" alt="dj_167" src="https://user-images.githubusercontent.com/86648892/212547186-bfeeaba8-ce4a-419e-8a9f-6daa54e6a986.png">

### 비인증 사용자는 CommentForm을 볼 수 없도록 하기

<img width="1035" alt="dj_168" src="https://user-images.githubusercontent.com/86648892/212547185-f65b0425-d54d-4624-b1fb-59d395f87102.png">

---

## 정리

- 다대일 관계 (A many-to-one relationship)
  - Foreign Key
  - Django Relationship Fields
  - Related Manager
  - Referencing the User Model
- N : 1 모델 관계 설정
  - Comment - Article
  - Article - User
  - Comment - User
- 작성 과정
  - models에서 참조 키를 설정
  - forms에서 필드를 가리기
  - view 함수에서 동작을 처리
  - html에서 조건에 따라 출력 여부 설정

---

## 참고 [Django Coding Style Guide about Imports]

- import와 관련한 coding style guide
  - [https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/#imports](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/#imports)
  - isort 사용
    - **`$** python -m pip install "isort >= 5.1.0"`
    - **`$** isort .`
      - `$ isort accounts/views.py`
- 띄어쓰기, 좌우 공백
- camelCase말고 언더바 사용

---

# Django M:N Relationship

- Many to many relationship
- M:N (Article-User)
  - Like
- M:N (User-User)
  - Follow
- Fixtures

---

# Many-to-many relationship practice (patients-doctors)

### target and source model?

- target model
  - 관계 필드를 가지지 않은 모델
  - N:1에서는 1에 해당
- source model
  - 관계 필드를 가진 모델
  - N:1에서는 N에 해당

### `models.py`

```python
from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'

class Patient(models.Model):
    # doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)  # [1] 1명의 의사 - N명의 환자인 경우 (한계: 동일한 환자가 여러 의사에게 예약을 받는 경우를 구현하기 어려움)
    # [3] M:N 필드 (중개모델을 Django에서 알아서 생성해줌)
    doctors = models.ManyToManyField(Doctor, related_name='patients', through='Reservation')
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'

# [2] 중개모델 작성 (예약을 단위로 기록)
# class Reservation(models.Model):
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'

# [3-1] ManyToManyField의 extra data 작성 (through argument와 연결)
class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptom = models.TextField()
    reserved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'
```

### 정리

- M:N 관계로 맺어진 두 테이블에는 변화가 없음
- Django의 ManyToManyField는 중개 테이블을 자동으로 생성함
- Django의 ManyToManyField는 M:N 관계를 맺는 두 모델 어디에 위치해도 상관 없음
  - 대신 필드 작성 위치에 따라 참조와 역참조 방향을 주의할 것
- N:1은 완전한 종속의 관계였지만 M:N은 의사에게 진찰받는 환자, 환자를 진찰하는 의사의 2가지 형태로 모두 표현이 가능한 것

---

# `ManyToManyField(to, **options)`

## ManyToManyField란

- 다대다 관계 설정 시 사용하는 모델 필드
- 하나의 필수 위치인자가 필요
  - M:N 관계로 설정할 모델 클래스
- 모델 필드의 RelatedManager를 사용하여 관련 개체를 추가, 제거, 혹은 만들 수 있음
  - `add()` , `remove()` , `create()` , `clear()` …

## 데이터베이스에서의 표현

- Django는 다대다 관계를 나타내는 중개 테이블을 생성
- ManyToManyField는 중개 테이블에 별도 생성되는 것이며 기존 모델 테이블에 컬럼이 추가되지 않음
  - 중개 테이블 이름은 **appname_ManyToManyField를 포함한 modelname_ManyToManyFieldname**
    - ex) `articles_article_like_users`
    - `db_table` arguments를 사용하여 중개 테이블의 이름을 변경할 수도 있음
  - 중개 테이블의 컬럼 이름
    - source model과 target model이 다른 경우
      - id
      - **<containing_model>\_id**
        - 참조하는 모델 이름
      - **<other_model>\_id**
        - 역참조하는 모델 이름
    - 동일한 모델의 관계인 경우
      - id
      - **from\_<model>\_id**
      - **to\_<model>\_id**

## ManyToManyField Arguments

1. `related_name`
2. `through`
3. `symmetrical`

- blank=True
  - db의 유효성 검사와 관련없음 (값이 있어야함)
    - 사용자가 입력할 때 blank를 허용하는 것

### `related_name` argument

- target model이 source model을 참조할 때 사용할 manager name
- ForeignKey의 related_name과 동일

### `through` argument

- 중개 테이블을 수동으로 지정하려는 경우 `through` 옵션을 사용하여 사용하려는 중개 테이블을 나타내는 Django 모델을 지정할 수 있음
- 가장 일반적인 용도는 중개 테이블에 extra data를 추가하여 다대다 관계와 연결하려는 경우
- ManyToManyField를 조회할 때 해당 중개 테이블을 ‘통해서’ 조회를 하겠다는 뜻
- ManyToManyField에 자동으로 생성하는 것을 이제는 through 테이블로 대체하겠다는 뜻
- 예약을 주체로 예약을 생성하는 것도 가능하지만
  - 환자 혹은 의사를 주체로 관계를 추가하는 것이 더 합리적
- `add()` 시 `through_defaults={'key': 'value'}` argument 필요
  - `through_defaults` 값에 딕셔너리 타입으로 입력
  - ex) `patient2.doctors.add(doctor1, through_defaults={'symptom': 'flu'})`

### `symmetrical` argument

- 기본값은 True
- **ManyToManyField가 동일한 모델(on self)을 가리키는 정의**에서만 사용
- 재귀 참조 (self 참조)
  <img width="833" alt="dj_169" src="https://user-images.githubusercontent.com/86648892/212547774-196ab395-d15f-464b-b960-1a30529cb380.png">

- `symmetrical=True` 일 경우
  - set 매니저를 추가하지 않음
  - source 모델의 인스턴스가 target 모델의 인스턴스를 참조하면
    - 자동으로 target 모델 인스턴스도 source 모델 인스턴스를 참조하도록 함 (대칭)
      - 쉽게 말해 1-2의 관계가 추가된다면, 2-1의 관계도 추가됨
  - 대칭을 원하지 않는 경우 `False` 로 설정

## ManyToManyField Related Manager

- N:1 혹은 M:N 관계에서 사용 가능한 문맥(context)
- Django는 모델 간 N:1 혹은 M:N 관계가 설정되면 역참조 시에 사용할 수 있는 manager를 생성
  - 모델 생성 시 obejcts라는 매니저를 통해 queryset api를 사용했던 것처럼 related manager를 통해 queryset api 사용 가능
- N:1, M:N 관계에 따라 다르게 사용 및 동작됨
  - N:1
    - target 모델 객체만 사용 가능
  - M:N
    - 관련된 두 객체 모두 사용 가능
- 메서드 종류
  - `add()` , `remove()` , `create()` , `clear()` , `set()` …

## Methods (ManyToManyField)

### `add()`

- “지정된 객체를 관련 객체 집합에 추가”
- 이미 존재하는 관계에 사용하면 관계가 복제되지 않음
- 모델 인스턴스, 필드 값(PK)을 인자로 허용

### `remove()`

- “관련 객체 집합에서 지정된 모델 개체를 제거”
- 내부적으로 `QuerySet.delete()` 를 사용하여 관계가 삭제됨
- 모델 인스턴스, 필드 값(PK)을 인자로 허용

## 중개 테이블 필드 생성 규칙

<img width="962" alt="dj_170" src="https://user-images.githubusercontent.com/86648892/212547771-e43b0d22-2295-4120-afc2-2fee1e39623e.png">

---

# M:N (Article-User)

- Article과 User의 M:N 관계 설정을 통한 좋아요 기능 구현하기

## Like 기능 구현하기

### 모델 관계 설정

<img width="968" alt="dj_171" src="https://user-images.githubusercontent.com/86648892/212547769-a727db36-6b1a-4798-9eb6-89078f77aa32.png">

- `like_users` 필드 생성 시 자동으로 역참조에는 `.article_set` 매니저가 생성됨
- 그러나 이전 N:1 (Aritcle-User) 관계에서 이미 해당 매니저를 사용 중
  - `user.article_set.all()`
    - 해당 유저가 작성한 모든 게시글 조회
  - **user가 작성한 글들(`user.article_set`)과 user가 좋아요를 누른 글(`user.article_set`)을 구분할 수 없게 됨**
  - 이런 경우 user와 관계된 ForeignKey 혹은 ManyToManyField 중 하나에 `related_name` 을 작성해야 함

<img width="1022" alt="dj_172" src="https://user-images.githubusercontent.com/86648892/212547765-07fbe386-c6af-4cdb-bb0c-3257d092b1d8.png">

- 생성된 중개 테이블 확인

<img width="485" alt="dj_173" src="https://user-images.githubusercontent.com/86648892/212547761-5dcf4b86-f09a-4cfa-bfd5-94886cd7c232.png">

<img width="1000" alt="dj_174" src="https://user-images.githubusercontent.com/86648892/212547757-9fa18eb3-8299-436d-82c5-96f30988daf6.png">

### LIKE 구현

### url과 view 함수 설정

<img width="586" alt="dj_175" src="https://user-images.githubusercontent.com/86648892/212547755-78740740-e653-4bb4-9518-f4e233613d38.png">

<img width="590" alt="dj_176" src="https://user-images.githubusercontent.com/86648892/212547751-e2de49dd-ce83-4c3a-a12e-f7347a7fd8bc.png">

### `.exists()`

- QuerySet에 결과가 포함되어 있으면 True를 반환하고 그렇지 않으면 False를 반환
- 특히 큰 QuerySet에 있는 특정 개체의 존재와 관련된 검색에 유용

### index 템플릿에서 각 게시글에 좋아요 버튼 출력하기

<img width="810" alt="dj_177" src="https://user-images.githubusercontent.com/86648892/212547747-ec70756d-eb73-4ce1-b563-f299d8d9cbdf.png">

### 데코레이터 및 is_authenticated 추가

<img width="825" alt="dj_178" src="https://user-images.githubusercontent.com/86648892/212547743-6d270f89-6121-48c2-8358-92f30092ed1b.png">

---

# M:N (User-User)

- User 자기 자신과의 M:N 관계 설정을 통한 팔로우 기능 구현하기

## Profile 구현

- 자연스러운 follow 흐름을 위한 프로필 페이지를 먼저 작성

### url 및 view 함수 작성

- urlpatterns는 위에서부터 매칭한다
  - 만약 `path(’<str:username>/’, views.profile, name=’profile’),` 를 맨 위에 작성해버리면 그 아래에 있는 login, logout, signup 등 모든 문자열 시작 url들이 죽어버린다

<img width="895" alt="dj_179" src="https://user-images.githubusercontent.com/86648892/212547738-b4ed5f5d-525f-400e-a073-d81f2ac7deb6.png">

<img width="894" alt="dj_180" src="https://user-images.githubusercontent.com/86648892/212547736-853d38ea-5ce4-40ee-a771-782407629a39.png">

### profile 템플릿 작성

<img width="498" alt="dj_181" src="https://user-images.githubusercontent.com/86648892/212547731-c4abdd82-0efa-43de-b5b6-73b6a588e3bc.png">

<img width="553" alt="dj_182" src="https://user-images.githubusercontent.com/86648892/212547727-b3db06a2-a500-448e-9b71-cfa3eed85c31.png">

### profile 템플릿으로 이동할 수 있는 하이퍼링크 작성

<img width="1069" alt="dj_183" src="https://user-images.githubusercontent.com/86648892/212547722-d4e0b25b-6a59-40fc-a703-3f6241d41e61.png">

<img width="1065" alt="dj_184" src="https://user-images.githubusercontent.com/86648892/212547719-8524bedc-cb15-4f51-8c47-8fb9467add67.png">

---

## Follow 구현

### 모델 관계 설정

<img width="1092" alt="dj_185" src="https://user-images.githubusercontent.com/86648892/212547715-1457bffd-f9bf-4463-8f14-1082f398c070.png">

- 참조할 때 이름은 followings
  - followings 당하는 입장에서 역참조는 followers
- migration 진행
- 생성된 중개 테이블 확인
  <img width="574" alt="dj_186" src="https://user-images.githubusercontent.com/86648892/212547713-0728164b-2e05-4426-9a7d-9e87d65a02eb.png">

### url 및 view 함수 작성

<img width="897" alt="dj_187" src="https://user-images.githubusercontent.com/86648892/212547709-a8143bf5-526c-4991-ae33-2f3b5330f74d.png">

<img width="893" alt="dj_188" src="https://user-images.githubusercontent.com/86648892/212547704-186239f6-6034-497c-be86-040912fb44ec.png">

### 프로필 유저의 팔로잉, 팔로워 수 & 팔로워, 언팔로우 버튼 작성

<img width="931" alt="dj_189" src="https://user-images.githubusercontent.com/86648892/212547701-312080a9-efc5-4d96-9aef-774960b70c0f.png">

### 데코레이터 및 is_authenticated 추가

<img width="830" alt="dj_190" src="https://user-images.githubusercontent.com/86648892/212547697-71d002b3-cb8d-4f5f-8dec-64974165e521.png">

---


# Django REST Framework and Serializer

- REST API
- Response JSON
- Django REST framework - Single Model
- Django REST framework - N:1 Relation

---



# Response JSON

- JSON 형태로의 서버 응답 변화
  - 페이지 반환이 아닌 JSON 데이터 반환
- 다양한 방법으로 JSON을 응답

### 서버가 응답하는 것

- 서버는 사용자에게 페이지(html)만 응답하는 것이 아니라
  - 다양한 데이터 타입을 응답할 수 있음
    - html을 응답하는 서버를 JSON 데이터를 응답하는 서버로 변환
      - 그렇다면 사용자에게 보여질 화면은 누가 구성?
        - Front-end Framework가 담당

<img width="853" alt="dj_248" src="https://user-images.githubusercontent.com/86648892/212551485-b0094561-b83f-499f-9f99-08eca9dd5a80.png">

<img width="843" alt="dj_249" src="https://user-images.githubusercontent.com/86648892/212551482-ba6add9f-95ab-435a-a0b1-f6ab8867e56d.png">

---

# Response

- 다양한 방법으로 JSON 데이터 응답해보기
  1. HTML 응답
  2. `JsonResponse()` 를 사용한 JSON 응답
  3. **Django Serializer**를 사용한 JSON 응답
  4. **Django REST framework**를 사용한 JSON 응답

## ‘Content-Type’ entity header

- 리소스의 media type(MIME type, content type)을 나타내기 위해 사용됨
- 응답 내에 있는 컨텐츠의 컨텐츠 유형이 실제로 무엇인지 클라이언트에게 알려줌

## Serialization이란?

- “직렬화”
- 데이터 구조나 객체 상태를 동일 혹은 다른 컴퓨터 환경에 저장하고
  - 나중에 재구성할 수 있는 포맷으로 변환하는 과정
    - 즉, 어떠한 언어나 환경에서도 나중에 쉽게 재구성할 수 있는 포맷인 serialized data로 변환하는 과정
      - serialized data란 가공된 데이터로
        - 다른 포맷으로 쉽게 재구성할 수 있는 파일이라는 특징
          - 변환 포맷은 대표적으로 json, xml, yaml이 있으면 json이 가장 보편적으로 쓰임
- Django의 `serialize()` 는 QuerySet 객체 및 Model Instance와 같은 복잡한 데이터를
  - JSON, XML 등의 유형으로 쉽게 변환할 수 있는 Python 데이터 타입으로 만들어줌

<img width="850" alt="dj_250" src="https://user-images.githubusercontent.com/86648892/212551481-fec1e18f-2cc6-4dce-ba28-3b9522727772.png">

<img width="832" alt="dj_251" src="https://user-images.githubusercontent.com/86648892/212551480-75ef0e69-dbac-4f62-8622-3c7ed077041e.png">

## 1. HTML 응답

```python
def article_html(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/article.html', context)
```

```html
<body>
  <h1>Article List</h1>
  <hr>
  <p>
    {% for article in articles %}
      <h2>{{ article.pk }}번 글. {{ article.title }}</h2>
      <p>{{ article.content }}</p>
      <hr>
    {% endfor %}
  </p>
</body>
```

<img width="634" alt="dj_252" src="https://user-images.githubusercontent.com/86648892/212551479-20330f29-bfd9-4587-9d87-e98e1aab0046.png">

## 2. JsonResponse()를 사용한 JSON 응답

- Django가 기본적으로 제공하는 JsonResponse 객체를 활용하여 Python 데이터 타입을 손쉽게 JSON으로 변환하여 응답 가능
- 컬럼을 일일이 정의하여 딕셔너리 생성
- `JsponResponse()`
  - JSON-encoded response를 만드는 클래스
  - `safe` parameter
    - 기본값은 True
    - `JsonResponse()` 에 들어오는 인자가 dictionary가 아니면 `safe=False` 로 설정해야함
      - False로 설정 시 모든 타입의 객체를 serialization 할 수 있음
        - 그렇지 않으면 dictionary 인스턴스만 허용
- 출력 확인을 위해 Chrome 확장 프로그램에 JSON Viewer 설치

```python
# 직접 JSON 응답 객체 작성 (JsonResponse())

from django.http.response import JsonResponse

def article_json_1(request):
    articles = Article.objects.all()
    articles_json = []
    # article 데이터 하나씩 딕셔너리 형태로 리스트에 넣음
    for article in articles:
        articles_json.append(
            {
                'id': article.pk,
                'title': article.title,
                'content': article.content,
                'created_at': article.created_at,
                'updated_at': article.updated_at,
            }
        )
    # 만든 딕셔너리 리스트를 JSON으로 변환
    return JsonResponse(articles_json, safe=False)
```

<img width="583" alt="dj_253" src="https://user-images.githubusercontent.com/86648892/212551477-5f824975-dfc4-477d-bad8-8487fc7a28d7.png">

## 3. Django Serializer를 사용한 JSON 응답

- Django 내장 `HttpResponse()` 를 활용한 JSON 응답
- 모델 구조를 기반으로 JSON 데이터를 생성
  - JSON의 모든 필드를 다 작성할 필요 없음

```python
# Django 내장 HttpResponse()와 serializers 활용

from django.http.response import HttpResponse

def article_json_2(request):
    articles = Article.objects.all()
    data = serializers.serialize('json', articles)
    return HttpResponse(data, content_type='application/json')
```

<img width="699" alt="dj_254" src="https://user-images.githubusercontent.com/86648892/212551476-83ac2af1-e096-4d53-910e-c8695ef500ac.png">

## 4. Django REST framework를 사용한 JSON 응답

### Django REST framework (DRF)

- Django에서 Restful API 서버를 쉽게 구축할 수 있도록 도와주는 오픈소스 라이브러리
- Web API 구축을 위한 강력한 toolkit을 제공
- REST framework를 작성하기 위한 여러 기능을 제공
- DRF의 serializer는 Django의 Form 및 ModelForm 클래스와 매우 유사하게 작동
  - DRF에서 일부러 구성을 맞춰둔 것
    - ModelForm과 동일한 일을 하는 것은 아님
      - `serialize()`를 담당
- [https://www.django-rest-framework.org/](https://www.django-rest-framework.org/)

```python
# settings.py

INSTALLED_APPS = [
    'articles',
    'rest_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

```python
# articles/serializers.py

from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'
```

```python
# articles/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response

# @api_view(['GET'])
@api_view()
def article_json_3(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)
```

<img width="583" alt="dj_255" src="https://user-images.githubusercontent.com/86648892/212551472-813a56ac-3f27-4fd9-b949-0ea82aa34513.png">

- DRF가 자체적으로 JSON 데이터를 담은 DRF 내장 템플릿을 반환
  - `Content-Type: text/html;`
  - 브라우저 상에서만 그런 것이고, 실제 코드에서 프로그래밍적으로 소통할 때는 JSON을 반환

### 직접 requests 라이브러리를 사용하여 JSON 응답 받아보기

- requests 라이브러리 설치
  - `pip install requests`
    - Terminal 화면을 나누어 Django 서버를 켜놓고 파일 실행

```python
# gogo.py

# 요청보낼 때 requests 라이브러리 사용
import requests
from pprint import pprint

response = requests.get('http://127.0.0.1:8000/api/v1/json-3/') # requests가 GET Method로 해당 url에 요청을 보냄
result = response.json()                                        # 응답받은 것을 JSON으로 변환

pprint(result)
# pprint(result[0])
# pprint(result[0].get('title'))
```

<img width="674" alt="dj_256" src="https://user-images.githubusercontent.com/86648892/212551470-938710ff-6204-4371-83eb-9fec1a05b9a0.png">

---

# Django REST framework (Single Model)

- 단일 모델의 data를 Serialization하여 JSON으로 변환하는 방법 학습
- DRF를 활용하여 JSON 데이터를 응답하는 Django 서버 구축

## ModelSerializer

- ModelSerializer 클래스는 모델 필드에 해당하는 필드가 있는 Serializer 클래스를 자동으로 만들 수 있는 shortcut을 제공
  1. Model 정보에 맞춰 자동으로 필드를 생성
  2. serializer에 대한 유효성 검사기를 자동으로 생성
     - 이름도 `is_valid()` 로 같음
     - serialize하기 전 유효성 검사
  3. `.create()` 및 `.update()` 의 간단한 기본 구현이 포함됨
     - 이후 수정이나 생성을 할 때 쓰는 메서드를 기본 구현에 포함하고 있음
- 쿼리셋이나 모델 인스턴스 객체를 넣어주기만 하면 알아서 그 필드에 맞춰서 JSON 데이터를 key-value에 맞춰 생성
- 최대한 Django의 ModelForm과 비슷하게 구현해놓음

### 단일 모델 인스턴스 serialize

- Model Instance 객체 serialize
  - `article = Article.objects.get(pk=1)`
  - `serializer = ArticleListSerializer(article)`
  - `serializer.data`

<img width="624" alt="dj_257" src="https://user-images.githubusercontent.com/86648892/212551468-1508ad08-db57-4cbb-ab78-269e98dec476.png">

### QuerySet 객체 serialize

- QuerySet 객체 serialize
  - 단일 객체 인스턴스 대신 QuerySet 또는 객체 목록을 serialize하려면
    - `many=True` 옵션이 필요함

<img width="774" alt="dj_258" src="https://user-images.githubusercontent.com/86648892/212551467-d3c58515-cc8f-4b8d-a8c2-e6e93c4b40ba.png">

<img width="773" alt="dj_259" src="https://user-images.githubusercontent.com/86648892/212551466-82f16d27-9d5e-45a7-b8f4-67f4f8caf366.png">

---

# Build RESTful API (Article and Comment)

<img width="838" alt="dj_260" src="https://user-images.githubusercontent.com/86648892/212551464-5618e163-34c3-407d-b032-96d68e00749f.png">

- URL은 2개이고, 기능은 7개인 서버를 구현
  - URL이 2개인데 기능이 7개가 가능한 이유는 똑같은 URL이지만 Http Methods로 행동을 정의할 수 있기에 가능

## `api_view` decorator

- DRF에서 `api_view` 데코레이터 작성은 필수
- DRF view 함수가 응답해야하는 HTTP 메서드 목록을 받음
- 기본적으로 GET 메서드만 허용되며 다른 메서드 요청에 대해서는
  - 405 Method Not Allowed로 응답

## raising an exception on invalid data

- serializer의 데이터에 대한 유효성 검사 실행 시 줄 수 있는 옵션
  - 유효하지 않은 데이터에 대해 예외 발생시키기
    - `is_valid()` 는 유효성 검사 오류가 있는 경우 ValidationError 예외를 발생시키는 선택적 `raise_exception` 인자를 사용할 수 있음
      - DRF에서 제공하는 기본 예외 처리기에 의해 자동으로 처리되며 기본적으로 HTTP 400 응답을 반환

## passing additional attributes to `.save()`

- `save()` 메서드는 특정 Serializer 인스턴스를 저장하는 과정에서 추가적인 데이터를 받을 수 있음
- 아래 사진은 `CommentSerializer` 를 통해 Serialize되는 과정에서 Parameter로 넘어온 `article_pk` 에 해당하는 article 객체를 추가적인 데이터를 넘겨 저장

<img width="677" alt="dj_261" src="https://user-images.githubusercontent.com/86648892/212551775-b623c2e4-81a9-4fcf-88a5-e9450185ee1f.png">

## `read_only_fields` 설정

- `read_only_fields` 를 사용해 외래키 필드를 읽기 전용 필드로 설정
- 읽기 전용 필드는 데이터를 전송하는 시점에
  - 해당 필드를 유효성 검사에서 제외시키고 데이터 조회 시에는 출력하도록 함

<img width="593" alt="dj_262" src="https://user-images.githubusercontent.com/86648892/212551774-480fe870-7d69-403a-ad31-0955826d466d.png">

---

# Code Snippets

### `articles/models.py`

```python
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

### `articles/serializers.py`

```python
from rest_framework import serializers  # DRF 패키지에서 serializers 기능을 차용
from .models import Article, Comment    # ModelSerializer에 사용할 모델 import

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',) # 최종적으로 조회는 되나, 유효성 검사에서 제외됨

# 게시글의 목록(게시글들의 QuerySet)을 serialize해서 나눌 것이기에 이름을 ArticleListSerializer로 명명
class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article                         # 해당 모델 정보에 맞춰 자동으로 필드 생성
        # 전체 게시글 목록에서는 생성일, 수정일은 빼고 보여주기
        fields = ('id', 'title', 'content',)    # 어떤 필드를 serialize할지 결정 (사용자에게 최종적으로 JSON에 보여질 것을 결정)

# 단일 게시글에 대한 상세 정보를 제공하는 serializer
# serialize하는 fields가 달라지면 다른 serializer를 만들어줘야함
class ArticleSerializer(serializers.ModelSerializer):
    # article 입장에서 comment는 N이기에 many=True 필요, 또한 유효성 검사에서 제외되어야 함
    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True) # 기존 역참조용 필드를 override
    comment_set = CommentSerializer(many=True, read_only=True)  # 역참조할 시 pk말고 CommentSerializer에서 출력하는 모든 정보 출력 가능
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)    # 새로운 필드 추가

    class Meta:
        model = Article
        fields = '__all__'
```

### `articles/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('articles/<int:article_pk>/comments/', views.comment_create),
]
```

### `articles/views.py`

```python
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import get_object_or_404, get_list_or_404

from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer

# @api_view()는 기본값이 GET만 허용
@api_view(['GET', 'POST'])
def article_list(request):
    # 전체 게시글 조회
    if request.method == 'GET':
        # articles = Article.objects.all()
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    # 게시글 작성
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)   # ArticleSerializer를 사용한 이유는 게시글이 생성됐을 때 전체 필드를 출력하는 JSON을 사용하고 싶어서 사용
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    # 단일 게시글 조회
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    # 단일 게시글 삭제
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # 단일 게시글 수정
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)  # ModelForm과 다르게 앞쪽에 인스턴스가 들어감
        # serializer = ArticleSerializer(instance=article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['GET'])
def comment_list(request):
    # 댓글 목록 조회
    if request.method == 'GET':
        # comments = Comment.objects.all()
        comments = get_list_or_404(Comment)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    # comment = Comment.objects.get(pk=comment_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    # 특정 댓글 조회
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    # 특정 댓글 삭제
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # 특정 댓글 수정
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

# 단일 댓글 데이터 생성
@api_view(['POST'])
def comment_create(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):   # 아래줄에서 article이 들어가기 전 유효성 검사 진행 (read_only_fields 설정 필요)
            serializer.save(article=article)        # 외래키 삽입 (ModelForm과 달리 commit=False를 사용하지 않음)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
```

## GET (List)

### 게시글 데이터 목록 조회하기

<img width="1491" alt="dj_263" src="https://user-images.githubusercontent.com/86648892/212551772-a2d86c82-2186-4340-af6b-3e07d9e87d79.png">

## GET - Detail

### 단일 게시글 데이터 조회하기

<img width="1496" alt="dj_264" src="https://user-images.githubusercontent.com/86648892/212551771-ef86a807-6c56-4845-bf1e-007f47679da0.png">

## POST

### 게시글 데이터 생성하기

<img width="1371" alt="dj_265" src="https://user-images.githubusercontent.com/86648892/212551770-ba13e92b-c337-4375-adc3-ccea7a3df854.png">

- 요청에 대한 데이터 생성이 성공했을 경우 201 Created 상태 코드를 응답하고 실패했을 경우는 400 Bad request를 응답
  - `from rest_framework import status`
    - `return Response(serializer.data, status=status.HTTP_201_CREATED`
    - `return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST`
      - `if serializer.is_valid(raise_exception=True):` 와 같이 raise exception option을 주면 더이상 400을 따로 설정하지 않아도 됨

## DELETE

### 게시글 데이터 삭제하기

<img width="1328" alt="dj_266" src="https://user-images.githubusercontent.com/86648892/212551768-293984e0-9b5e-4a0e-a6c7-a9242b6081c7.png">

- 요청에 대한 데이터 삭제가 성공했을 경우는 204 No Content 상태 코드 응답
  - API는 반드시 요청에 대한 결과를 정확한 상태 코드로 전달해야 한다
    - 그래야 소통이 가능하다

## PUT

### 게시글 데이터 수정하기

<img width="1322" alt="dj_267" src="https://user-images.githubusercontent.com/86648892/212551767-3cad5381-a10f-403d-8154-407ea8d40efe.png">

- 요청에 대한 데이터 수정이 성공했을 경우는 200 OK 상태 코드 응답

---

# Django REST framework (N:1 Relation)

- N:1 관계에서의 모델 data를 Serialization하여 JSON으로 변환하는 방법 학습
- Serializer의 필드를 정의하는 것은 모델을 바탕으로 한 JSON 데이터에 추가적으로 덧붙이고 싶은 정보가 있을 때 정의한다고 생각하자
  - 역참조를 하는 related manager의 이름으로 필드를 정의하면
    - serializer에 역참조하는 데이터들을 넣어주는 로직을 쓰지 않아도 알아서 인식하여 넣어주는 것 뿐
      - 예시
        - `comment_set = CommentSerializer(many=True, read_only=True)`
        - `comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)`

## GET (List)

### 댓글 데이터 목록 조회하기

<img width="1507" alt="dj_268" src="https://user-images.githubusercontent.com/86648892/212551766-cf212aa2-56c7-4983-bb27-9b101886a18e.png">

## GET (Detail)

### 단일 댓글 데이터 조회하기

<img width="1502" alt="dj_269" src="https://user-images.githubusercontent.com/86648892/212551765-4739720f-47c9-450f-8d90-5051d993dded.png">

### POST

### 단일 댓글 데이터 생성하기

<img width="1325" alt="dj_270" src="https://user-images.githubusercontent.com/86648892/212551763-dbba2a11-3285-4084-898f-ce2e66b3d52c.png">

- CommentSerializer에서 article field의 데이터는 사용자로부터 입력받는 것이 아니므로
  - CommentSerializer에서 article은 read only field로 설정

### DELETE & PUT

### 댓글 데이터 삭제 및 수정 구현하기

<img width="1254" alt="dj_271" src="https://user-images.githubusercontent.com/86648892/212551761-fae71e32-bb35-4851-b62c-7cdcbfe8b700.png">

<img width="1261" alt="dj_272" src="https://user-images.githubusercontent.com/86648892/212551760-812c213a-d12d-403b-8e72-e94389278b85.png">

---

# N:1 역참조 데이터 조회

1. 특정 게시글에 작성된 댓글 목록 출력하기
   - **기존 필드 override**
2. 특정 게시글에 작성된 댓글의 개수 출력하기
   - **새로운 필드 추가**

## 특정 게시글에 작성된 댓글 목록 출력하기

### 기존 필드 Override (역참조 덮어씌우기)

1. **PrimaryKeyRelatedField()**
   - `comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)`

<img width="1455" alt="dj_273" src="https://user-images.githubusercontent.com/86648892/212551759-a42410eb-4376-4f4e-af99-3b14a21e9b5b.png">

1. **Nested Relationships**
   - `comment_set = CommentSerializer(many=True, read_only=True)`
     - 역참조 시 pk말고 CommentSerializer에서 출력하는 모든 정보 출력 가능

<img width="1259" alt="dj_274" src="https://user-images.githubusercontent.com/86648892/212551756-1ac50631-3d57-4b27-8bbe-99cb5334cdda.png">

## 특정 게시글에 작성된 댓글의 개수 출력하기

### 새로운 필드 추가

- `comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)`
  - `source`
    - serializers field’s argument
    - 필드를 채우는데 사용할 속성의 이름
    - 점 표기법(dotted notation)을 사용하여 속성을 탐색할 수 있음
    - source에 ORM 명령어 작성
      - `article.comment_set.count()`
        - ArticleSerializer 안이므로 article 생략, 문자열 안이어서 끝 괄호 생략
  - comment_count와 같이 변수명은 정의하고싶은 것으로 정의
  - 숫자를 다룰 것이므로 `IntegerField()`
  - 유효성 검사를 통과해야하므로 `read_only`는 True

<img width="1352" alt="dj_275" src="https://user-images.githubusercontent.com/86648892/212551753-1aeae757-f7dc-4138-b159-9d66aeae495b.png">

### [주의] 읽기 전용 필드 지정 이슈

- 기존에 물리적으로 존재했던 필드는 `read_only_fields` 지정 가능
- override되거나 추가된 필드의 경우에는 `read_only_fields`에 추가할 수 없음
- `read_only_fields` 에 지정하는 것들은 DB→클라이언트로 조회만 가능하고, 클라인어트→DB로 조작은 불가한 필드를 설정하는 것

<img width="715" alt="dj_276" src="https://user-images.githubusercontent.com/86648892/212551750-097f9c7d-a213-4a5f-aac8-4966a7afe5e0.png">

---

# Django shortcuts functions

- `django.shortcuts` 패키지는 개발에 도움될 수 있는 여러 함수와 클래스를 제공
- 제공되는 shortcuts 목록
  - `render()` , `redirect()` , `get_object_or_404()` , `get_list_or_404()`
    - `get()` 대신 `get_object_or_404()`
    - `all()` 대신 `get_list_or_404()`
  - [https://docs.djangoproject.com/en/4.1/topics/http/shortcuts/](https://docs.djangoproject.com/en/4.1/topics/http/shortcuts/)

## `get_object_or_404()`

- `objects.get()` 과 같은 코드의 경우 해당 pk의 값이 없거나, 혹은 2개 이상인 경우 모두 예외가 발생함
  - `objects.get()` 의 경우 코드 진행이 더 이상 이루어지지 않고
    - Django는 500 status를 반환함
- `get_object_or_404()` 의 경우 예외 발생 시 404 status와 함께 코드 진행 가능
  - 해당 객체가 없을 때 DoesNotExist 예외 대신 Http404를 raise함

<img width="607" alt="dj_277" src="https://user-images.githubusercontent.com/86648892/212551749-c2eee230-4f90-4015-9464-621c6b75a604.png">

## `get_list_or_404()`

- 빈 쿼리셋을 주는 것이 아닌 404 status를 반환

<img width="629" alt="dj_278" src="https://user-images.githubusercontent.com/86648892/212551747-4b59ae5c-47ac-46cc-8a32-c584fed83dc9.png">

## WHY?

- API 서버의 기본은 정확한 상태 코드를 반환하여 클라이언트와 소통하는 것
- 클라이언트 입장에서 “서버에 오류가 발생하여 요청을 수행할 수 없다(500)”라는 원인이 정확하지 않은 에러를 마주하기보다는, 서버가 적절한 예외 처리를 하고 클라이언트에게 올바른 에러를 전달하는 것 또한 중요한 요소

---

### [추가] SerializerMethodField

- [SerializerMethodField](https://www.django-rest-framework.org/api-guide/fields/#serializermethodfield)
- [SerializerMethodField로 모델에서 변형된 JSON을 내려주기](https://eunjin3786.tistory.com/m/268)
- [APIView, api_view란?](https://hangjastar.tistory.com/m/203)

---
