## MTV 기초

---

- Template
    - [Sending and Retrieving Form Data](#sending-and-retrieving-form-data)
- View
    - [CRUD with view functions](#crud-with-view-functions)

## Django Template

---

### DTL Syntax

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
