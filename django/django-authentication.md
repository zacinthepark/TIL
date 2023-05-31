## Index

---

- [Django Authentication System](#django-authentication-system)
- [Substituting Custom User Model](#substituting-custom-user-model)
- [쿠키와 세션](#쿠키와-세션)
- [Authentication in Web Requests](#authentication-in-web-requests)
- [Authentication in User](#authentication-in-user)
- [Limiting access to logged-in users](#limiting-access-to-logged-in-users)
- [패스워드 저장](#추가-패스워드-저장)

## Django Authentication System

---

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

### The Django authentication system

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

### 유저 관리용 accounts 앱 만들기

- 유저 인증과 관련된 앱
    - `$ python manage.py startapp accounts`
        - INSTALLED_APPS에 추가
        - **auth와 관련한 경로나 키워드들은 Django 내부적으로 accounts라는 이름으로 사용하고 있기에 되도록 accounts로 지정하는 것을 권장**
        - 다른 이름으로 설정해도 되지만 나중에 추가 설정을 해야할 일들이 생김
    - url 분리 및 매핑 실행

## Substituting Custom User Model

---

- “Custom User Model”로 **대체**하기
- 기본 User Model을 Custom User Model로 대체할 것을 권장
    - Django에서는 기본적인 인증 시스템과 여러가지 필드가 포함된 User Model을 제공, 대부분의 개발 환경에서는 기본 User Model을 Custom User Model로 대체함
    - 개발자들이 작성하는 일부 프로젝트에서는 Django에서 제공하는 built-in User Model의 기본 인증 요구사항이 적절하지 않을 수 있음
    - ex) 내 서비스의 회원가입 시 username 대신 email을 식별 값으로 사용하는 것이 더 적합한 사이트인 경우, Django의 User Model은 기본적으로 username을 식별 값으로 사용하기 때문에 적합하지 않음
- Django는 현재 프로젝트에서 사용할 User Model을 결정하는 **AUTH_USER_MODEL** 설정 값으로 Default User Model을 재정의(override)할 수 있도록 함
- **첫 migrations를 진행하기 전에 대체 작업을 진행해야함**
    - migrations 과정에서 기본 user model도 포함되기 때문

### `AUTH_USER_MODEL`

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

### Custom User Model 대체 진행 방법

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

### [참고] User 모델 상속 관계

<img width="265" alt="dj_84" src="https://user-images.githubusercontent.com/86648892/189502185-e95cec36-78f9-4131-aaff-9bd51c3de265.png">

### [참고] AbstractUser

- “관리자 권한과 함께 완전한 기능을 가지고 있는 User model을 구현하는 추상 기본클래스”
- Abstract이 붙는 클래스는 테이블에 생성되는 것이 아닌 기본 클래스로서 존재
- **Abstract Base Classes (추상 기본 클래스)**
    - 몇가지 공통 정보를 여러 다른 모델에 넣을 때 사용하는 클래스
    - 데이터베이스 테이블을 만드는데 사용되지 않으며, 대신 다른 모델의 기본클래스로 사용되는 경우 해당 필드가 하위 클래스의 필드에 추가됨
    - [Python Docs - Abstract Base Classes](https://docs.python.org/3/library/abc.html)

### 데이터베이스 초기화

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

### 반드시 User 모델을 대체해야 할까?

- Django는 새 프로젝트를 시작하는 경우 비록 기본 User 모델이 충분하더라도 커스텀 User 모델을 설정하는 것을 **강력하게 권장(highly recommended)**
- 커스텀 User 모델은 **기본 User 모델과 동일하게 작동하면서도 필요한 경우 나중에 맞춤 설정할 수 있기 때문**
- 단, User 모델 대체 작업은 프로젝트의 모든 migrations 혹은 첫 migrate를 실행하기 전에 이 작업을 마쳐야함

## 쿠키와 세션

---

로그인과 로그아웃을 이해하기에 앞서 핵심적인 개념

### HTTP 특징

1. **비연결지향(connectionless)**
    - 연결되어있는 상태가 아니라 요청이 있을 때만 응답을 주고 끝
    - 서버는 요청에 대한 응답을 보낸 후 연결을 끊음
        - ex) 우리가 네이버 메인 페이지를 보고 있을 때 우리는 네이버 서버와 연결되어 있는 것이 아님
        - 네이버 서버는 우리에게 메인 페이지를 응답하고 연결을 끊은 것
2. **무상태(stateless)**
    - 비연결지향에 의해 상태 정보가 유지되지 않음
    - 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며 상태 정보가 유지되지 않음
    - 클라이언트와 서버가 주고받는 메세지들은 서로 완전히 독립적

### 어떻게 로그인 상태를 유지할까?

- HTTP 특성에 의해서 원래는 로그인하고 난 뒤 다른 페이지로 이동하면 로그인 상태가 유지되지 않아야함
  - “쿠키와 세션"으로 로그인 상태를 유지할 수 있음
- 비연결지향에 의해 무상태가 나오고
  - 이를 해결하기 위한 기술이 쿠키와 세션
- **서버와 클라이언트 간 지속적인 상태 유지를 위해 “쿠키와 세션"이 존재**

### 쿠키(Cookie)

- HTTP 쿠키는 “상태가 있는 세션”을 만들도록 해줌

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

### 쿠키 사용 목적

1. 세션 관리(Session Management)
    - 로그인, 아이디 자동완성, 공지 하루 안보기, 팝업 체크, 장바구니 등의 정보 관리
2. 개인화(Personalization)
    - 사용자 선호, 테마 등의 설정
3. 트래킹(Tracking)
    - 사용자 행동을 기록 및 분석
    - 어떤 상품을 많이 봤는지 등

### 쿠키 확인

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

### 세션(Session)

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

### Session in Django

- Django는 **database-backed sessions 저장 방식**을 기본값으로 사용
    - session 정보는 Django DB의 **django_session 테이블**에 저장됨
    - 설정을 통해 다른 저장 방식으로 변경 가능
    - [Django Docs - How to use sessions](https://docs.djangoproject.com/en/4.1/topics/http/sessions/)
- Django는 특정 session id를 포함하는 쿠키를 사용해서 각각의 브라우저와 사이트가 연결된 session을 알아냄
- 사용자에게는 session_key만 줌
    - 사용자에 대한 중요한 정보는 session_data에 담아 서버가 들고있음

## Authentication in Web requests

---

- Django가 제공하는 인증 관련 built-in forms
- 인증은 직접 form을 구현하기 어렵기에 Django에서 로그인, 가입, 비밀번호 변경 등 인증 관련 built-in forms를 제공함
- [Django Docs - Built-in forms](https://docs.djangoproject.com/en/4.1/topics/auth/default/#module-django.contrib.auth.forms)

### 1. Login

- 로그인은 **Session을 Create**하는 과정

### AuthenticationForm

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

### Templates and Context Processors

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

### 2. Logout

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

## Authentication in User

---

### 1. 회원 가입

- 회원가입은 User를 **Create**하는 것이며 **UserCreationForm**이라는 built-in form 사용

### UserCreationForm

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

### Custom user & Built-in auth forms

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

### CustomUserCreationForm()

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

### 2. 회원 탈퇴

- 회원 탈퇴는 DB에서 유저 모델을 **Delete**하는 것

<img width="517" alt="dj_102" src="https://user-images.githubusercontent.com/86648892/189502207-a78c2b8a-583a-465c-80bf-1ee0bc1d89e0.png">

<img width="555" alt="dj_103" src="https://user-images.githubusercontent.com/86648892/189502208-a464a491-710d-4392-be36-37a82514010b.png">

<img width="613" alt="dj_104" src="https://user-images.githubusercontent.com/86648892/189502210-197d028d-adb2-4c93-9b45-dd21558b1c20.png">

### [참고] 탈퇴하면서 해당 유저의 세션 정보도 함께 지우고 싶을 경우

- 순서가 중요 (탈퇴 후 로그아웃)
- `request.user.delete()` -> `auth_logout(request)`
- 로그아웃을 먼저 하면 요청의 객체 정보가 사라져 탈퇴에 필요한 정보가 사라짐

### 3. 회원정보 수정

- 회원정보 수정은 User를 **Update**하는 것이며 **UserChangeForm** built-in form을 사용

### UserChangeForm

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

### 4. 비밀번호 변경

### PasswordChangeForm

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

## Limiting access to logged-in users

---

- 로그인 사용자에 대한 접근 제한하기
- 로그인 사용자에 대해 접근을 제한하는 2가지 방법
    1. `is_authenticated` attribute
    2. `login_required` decorator

### `is_authenticated`

- User model의 속성(attributes) 중 하나
- 사용자가 인증되었는지 여부를 알 수 있는 방법
- 모든 User 인스턴스에 대해 항상 True인 읽기 전용 속성
    - AnonymousUser에 대해서는 항상 False
- 일반적으로 `request.user` 에서 이 속성을 사용
    - `request.user.is_authenticated`
- 권한(permission)과는 관련이 없으며, 사용자가 활성화 상태(active)이거나 유효한 세션(valid session)을 가지고 있는지도 확인하지 않음

<img width="848" alt="dj_114" src="https://user-images.githubusercontent.com/86648892/189502222-52c4c831-f217-4881-a62e-4f5c0f299d32.png">

### `is_authenticated` 적용

- 로그인과 비로그인 상태에서 출력되는 링크를 다르게 설정

<img width="750" alt="dj_115" src="https://user-images.githubusercontent.com/86648892/189502224-e7c19354-43b5-442e-9a64-ac4600f8cb91.png">

- 인증된 사용자만 게시글 작성 링크를 볼 수 있도록 처리
    - 아직 비로그인 상태로도 URL을 직접 입력하면 게시글 작성 페이지로 갈 수 있긴함
    - `login_required` 데코레이터를 향후 활용하여 처리

<img width="886" alt="dj_116" src="https://user-images.githubusercontent.com/86648892/189502225-08a8fb0e-4777-4a1f-bf92-c8c8cff46611.png">

- 인증된 사용자라면 로그인 로직을 수행할 수 없도록 처리

<img width="629" alt="dj_117" src="https://user-images.githubusercontent.com/86648892/189502227-e0e1c5b2-d7b9-49ac-95e5-0b8bb0612c1c.png">

### `login_required`

- `login_required` decorator
- 사용자가 로그인되어 있다면 정상적으로 view 함수 실행
- 로그인하지 않은 사용자의 경우 `settings.py` 의 `LOGIN_URL` 문자열 주소로 redirect
    - `LOGIN_URL`의 기본값은 `/accounts/login/`
    - app 이름을 accounts로 했던 이유 중 하나!
    - `/articles/create/` 로 강제 접속을 시도해보면 로그인 페이지로 리다이렉트 후 `/accounts/login/?next=/articles/create/` url을 확인할 수 있음
    - **인증 성공 시 사용자가 redirect되어야하는 경로는 “next”라는 쿼리 문자열 매개 변수에 저장됨**

### `login_required` 적용

- 로그인 상태에서만 글을 작성, 수정, 삭제할 수 있도록 변경

<img width="760" alt="dj_118" src="https://user-images.githubusercontent.com/86648892/189502228-0c477880-3631-4702-95f7-dc7fc44d07af.png">

### “next” query string parameter

- 로그인이 정상적으로 진행되면 이전에 요청했던 주소로 redirect하기 위해 Django가 제공해주는 쿼리 스트링 파라미터
- 해당 값을 처리할지 말지는 자유이며 별도로 처리해주지 않으면 view에 설정한 redirect 경로로 이동하게됨

<img width="903" alt="dj_119" src="https://user-images.githubusercontent.com/86648892/189502229-8feaee79-3b9c-4e4a-9178-a381bedffa09.png">

<img width="731" alt="dj_120" src="https://user-images.githubusercontent.com/86648892/189502230-b4977862-a594-44da-8606-ce65566161d2.png">

- `/accounts/login/` 과 `/accounts/login/?next=...` 인 경우 2가지를 처리해야 하므로 현재 url로 요청을 보내도록 `action=""` 으로 변경

### `@login_required`와 `@require_POST` 충돌

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

### accounts view 함수에도 이처럼 데코레이터 및 속성값 적용

<img width="913" alt="dj_122" src="https://user-images.githubusercontent.com/86648892/189502232-8c482901-5c4a-4440-a1e0-cee796cb0402.png">

### 정리

- Django Authentication System
    - User 모델 대체하기
- Cookies and Sessions
    - 상태가 있는 세션 구성
- Authentication in Web requests
    - auth built-in form 사용하기
- Authentication in User
    - User Object와 User CRUD

## [추가] 패스워드 저장

---

- [안전한 패스워드 저장](https://d2.naver.com/helloworld/318732)
- [Django Docs - Password management in Django](https://docs.djangoproject.com/en/3.2/topics/auth/passwords/)

### 패스워드 저장 알고리즘

- password는 유저 모델의 필드가 아니다
    - 따로 저장됨
- 비밀번호를 저장할 땐 어떤 방식(알고리즘)을 사용하는가?
    - 단순 텍스트
        - 어불성설
    - 단방향 해쉬 함수의 다이제스트
        - 보완 알고리즘
        - 솔팅(Salting)
        - 키 스트레칭(Key Stretching)

<img width="857" alt="dj_123" src="https://user-images.githubusercontent.com/86648892/189502470-8db20282-1b2b-4d91-a5e4-d644acf53e70.png">

- 솔팅과 키 스트레칭을 바탕으로 한 검증된 Adaptive Key Derivation Function
    - PBKDF2
    - bcrypt
    - scrypt

### 패스워드 저장 in Django

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
