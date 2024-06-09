## HttpRequest

---

### HTML Form

- Form 태그는 하나 이상의 Widget으로 구성

- action
    - 처리 요청 URL
    - 지정하지않을 시 데이터는 현재 form이 있는 페이지의 URL로 전송

- method
    - 처리 요청 방식
    - GET: Query String이 요청정보 헤더에 포함되어 전달
    - POST: Query String이 요청정보 바디에 포함되어 전달

- enctype
    - POST 방식에서만 유효
    - `application/x-www-form-urlencoded` (default)
    - `multipart/form-data`: 파일 업로드 가능

#### GET

- 요청정보 헤더에 Query String이 담겨 전달되며, URL에 포함된다
    - 기본 URL과 `?`를 통해 구분되며, 각 key-value 쌍들은 `&`들을 통해 구분

- 전달되는 질의 문자열이 노출된다

- 전달되는 질의 문자열 길이에 제한이 있다

#### POST

- 요청정보 바디에 Query String이 담겨 전달된다

- 전달되는 질의 문자열이 노출되지 않는다

- 전달되는 질의 문자열 길이에 제한이 없다

#### File Upload

```html
<form action="" method="POST" enctype="multipart/form-data">
    <input type="file" name="picture">
    <input type="submit" value="전송">
</form>
```

### CSRF Token

- https://docs.djangoproject.com/en/4.2/ref/csrf/

<p align="center">
    <img width="500" alt="csrf" src="https://github.com/zacinthepark/TIL/assets/86648892/21fc4c0a-589f-4f45-9ce8-11267ca39175">
</p>

- CSRF
    - Cross-Site Request Forgery (사이트 간 요청 위조 공격)
    - 사용자가 의도하지 않은 공격

- CsrfViewMiddleware
    - GET 요청 시 csrf token 발급
    - POST 요청 시 csrf token 체크
    - token 체크 오류 시 403 Forbidden 반환
    - settings.py의 `MIDDLEWARE`에서 `django.middleware.csrf.CsrfViewMiddleware`가 담당
    - `{% csrf_token %}` 템플릿 태그를 통해 접근 가능
        - HTML Element에서 `<input type="hidden" name="csrfmiddlewaretoken" value="...">`로 들어가있는 것을 확인할 수 있음

### HttpRequest

- https://docs.djangoproject.com/en/4.2/ref/request-response/#httprequest-objects
- https://docs.djangoproject.com/en/4.2/ref/request-response/#httpresponse-objects

- 클라이언트로부터 전송된 요청정보를 처리하는 객체
    - View의 첫번째 인자로 전달됨

- 요청정보
    - Header
        - 요청 줄
            - `요청방식 URL HTTP 버전`
            - `GET /edu/index.html HTTP/1.1`
        - name
    - Body
        - 요청 바디

#### HttpRequest 속성

| 속성           | 정보                                                                 |
|----------------|----------------------------------------------------------------------|
| path           | 요청된 페이지의 경로 정보 (`/blog/1`)                                |
| method         | 요청 방식 정보 (`GET`, `POST`, ...)                                  |
| GET            | GET 방식으로 전달된 질의 문자열 정보                                 |
| POST           | POST 방식으로 전달된 질의 문자열 정보                                |
| COOKIES        | 현재 요청에서 사용하는 쿠키 정보                                     |
| FILES          | 업로드된 파일 정보                                                   |
| META           | HTTP 요청 정보의 헤더값들을 갖는 딕셔너리                            |
|                | `CONTENT_LENGTH`: 요청 정보 몸체의 길이                              |
|                | `CONTENT_TYPE`: 요청 정보 몸체의 타입                                |
|                | `HTTP_ACCEPT`: 응답에 허용되는 문서 타입                             |
|                | `HTTP_HOST`: 웹 클라이언트의 호스트 헤더 정보                        |
|                | `HTTP_REFERER`: 참조 페이지                                          |
|                | `HTTP_USER_AGENT`: 웹 클라이언트의 정보                              |
|                | `QUERY_STRING`: 질의 문자열                                          |
|                | `REMOTE_ADDR`: 웹 클라이언트의 IP 주소                               |
|                | `REMOTE_HOST`: 웹 클라이언트의 호스트 이름                           |
|                | `REMOTE_USER`: 웹 서버에서 인증한 사용자                             |
|                | `REQUEST_METHOD`: GET, POST 요청 방식                                |
| session        | 현재 웹 클라이언트가 사용하는 세션 객체                              |
| site           | 현재 웹 클라이언트가 사용하는 사이트 객체                            |
| user           | 현재 서비스를 사용하는 사용자 객체                                   |

#### QueryDict, MultiValueDict

- https://docs.djangoproject.com/en/4.2/ref/request-response/#querydict-objects
- https://github.com/django/django/blob/4.2/django/utils/datastructures.py#L43

- MultiValueDict
    - dict type을 상속함
    - 기본적으로 dict는 key의 중복을 허용하지 않음
    - MultiValueDict는 질의 문자열의 정보를 갖는 객체로서 동일 key를 허용함
        - `color=red&color=blue&color=yellow`
    - `request.FILES`의 타입은 MultiValueDict

- QueryDict
    - MultiValueDict를 상속함
    - 수정 불가능한(Immutable) MultiValueDict
    - dict와 MultiValueDict는 수정이 가능함
    - `request.GET`, `request.POST`의 타입은 QueryDict

```html
<form action="" method="post" enctype="multipart/form-data">
    {% csrf_token %}
    ID: <input type="text" name="id"><br>
    PW: <input type="password" name="pwd"><br>
    IMAGE: <input type="file" name="image"><br>
</form>
```

- HttpRequest 정보
    - `type(request)`: `<class 'django.core.handlers.wsgi.WSGIRequest'>`
    - `request.method`: `POST`
    - `request.GET`: `<QueryDict: {}>`
    - `request.POST`: `<QueryDict: {'csrfmiddlewaretoken': ['...'], 'id':['...'], 'pwd':['...']}>`
    - `request.FILES`: `<MultiValueDict: {'image':[<InMemoryUploadedFile: test.jpg(image/jpeg)>]}>`
