# INDEX

- [pjt01: Django Framework를 통한 데이터베이스 활용 및 영화 페이지 구현](#pjt01)<br>
- [pjt02: Django Framework를 통한 DB CRUD 및 영화 페이지 구현](#pjt02)<br>
- [pjt03: DRF를 통한 RESTful API 서버 구현](#pjt03)<br>
- [pjt04: 알고리즘을 이용한 영화 서버 및 페이지 구현](#pjt04)<br>
- [pjt05: vue-cli, vuex, router를 활용한 영화 페이지 구현](#pjt05)<br>

---

# pjt01

## Django Framework를 통한 데이터베이스 활용 및 영화 페이지 구현

---

### 요구사항
1. 구현해야될 웹 페이지
- 전체 영화 데이터 조회용 페이지
- 새로운 영화 데이터 생성용 페이지
- 기존 영화 데이터 정보 확인용 페이지
- 기존 영화 데이터 정보 수정용 페이지

2. 기능
- 상기 페이지들을 브라우저를 통해 렌더링
- CRUD 구현
- NEW 페이지를 통해 새로운 영화 데이터 생성 (CREATE)
- EDIT 페이지를 통해 기존 영화 데이터 수정 (UPDATE)
- DELETE 버튼을 통해 기존 영화 데이터 삭제 (DELETE)

---

### 결과 사진
- 반응형 웹페이지를 적용한 경우 2가지씩 첨부

### index.html

![index1](https://user-images.githubusercontent.com/86648892/188090673-ffed7d1b-55a2-40b1-a6fd-8ff50527be09.png)

![index2](https://user-images.githubusercontent.com/86648892/188090663-eaafc0ff-9cb3-4519-b899-7353c972fe92.png)

---

### detail.html

![detail1](https://user-images.githubusercontent.com/86648892/188090653-f9df6472-98b9-48da-b319-c205640fa638.png)

![detail2](https://user-images.githubusercontent.com/86648892/188090600-040edf3b-a232-4c69-848c-26589d5dc56b.png)

---

### new.html

![new1](https://user-images.githubusercontent.com/86648892/188090560-a2d4444c-b274-446c-b726-7fc8764588da.png)

![new2](https://user-images.githubusercontent.com/86648892/188090687-66fd2213-bc00-4a10-a23b-4a2a9dbb4296.png)

---

### edit.html

![edit1](https://user-images.githubusercontent.com/86648892/188090593-34209faa-51ab-4b49-ad00-bacb7d5f62ae.png)

![edit2](https://user-images.githubusercontent.com/86648892/188090591-adf4026a-1532-4993-a324-6038c0955a17.png)

---

### 프로젝트 구조

![code1](https://user-images.githubusercontent.com/86648892/188090678-5ca855de-cd2a-4e19-9abe-5c3b94d918b9.png)

---

## Code Snippets

### /templates/base.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
  <title>Document</title>
  <style>
    h1 {
      font-family: Georgia;
    }
    p {
      font-family: Georgia;
    }
  </style>
</head>
<body>
  
  {% block content %}
  {% endblock content %}

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
</body>
</html>

```
- `font-family`를 내부참조를 통해 정의

---

### /mypjt/urls.py

```python
"""mypjt URL Configuration

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
    path('movies/', include('movies.urls')),
]

```

---

### /movies/urls.py

```python
from django.urls import path
from movies import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
    path('<int:pk>/', views.detail, name="detail"),
    path('<int:pk>/edit/', views.edit, name="edit"),
    path('<int:pk>/update/', views.update, name="update"),
    path('<int:pk>/delete/', views.delete, name="delete"),
]

```

---

### /movies/models.py

```python
from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=20)     # 영화제목
    audience = models.IntegerField()            # 관객 수
    release_date = models.DateField()           # 개봉일
    genre = models.CharField(max_length=30)     # 장르
    score = models.FloatField()                 # 평점
    poster_url = models.TextField()             # 포스터 경로
    description = models.TextField()            # 줄거리

    def __str__(self):
        return self.title

```

- `DateField`, `IntegerField()`, `FloatField` 등 사용해보지 않았던 필드들을 활용해봄
- 입력 시 타입에 맞지 않는 값을 입력했을 때 오류를 반환함을 확인할 수 있었음

---

### /movies/views.py

```python
from django.shortcuts import render, redirect
from movies.models import Movie

# Create your views here.

# 전체 영화 목록 페이지 렌더링
# 전체 영화 데이터 조회 및 index.html 렌더링
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }

    return render(request, 'movies/index.html', context)

# 새로운 영화 생성 페이지 렌더링
# 장르 데이터 제공 및 new.html 렌더링
def new(request):
    return render(request, 'movies/new.html')

# 단일 영화 데이터 저장
# 새로운 영화 데이터 저장 및 detail 페이지로 redirect
def create(request):
    title = request.POST.get('title')
    audience = request.POST.get('audience')
    release_date = request.POST.get('release_date')
    genre = request.POST.get('genre')
    score = request.POST.get('score')
    poster_url = request.POST.get('poster_url')
    description = request.POST.get('description')

    movie = Movie(title=title, audience=audience, release_date=release_date, genre=genre, score=score, poster_url=poster_url, description=description)
    movie.save()

    return redirect('movies:detail', movie.pk)

# 영화 상세 페이지 렌더링
# 단일 영화 데이터 조회 및 detail.html 렌더링
def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie': movie
    }

    return render(request, 'movies/detail.html', context)

# 영화 수정 페이지 렌더링
# 수정 대상 영화 데이터 조회 및 edit.html 렌더링
def edit(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie': movie
    }

    return render(request, 'movies/edit.html', context)

# 단일 영화 데이터 수정
# 영화 데이터 수정 및 detail 페이지로 redirect
def update(request, pk):
    movie = Movie.objects.get(pk=pk)

    movie.title = request.POST.get('title')
    movie.audience = request.POST.get('audience')
    movie.release_date = request.POST.get('release_date')
    movie.genre = request.POST.get('genre')
    movie.score = request.POST.get('score')
    movie.poster_url = request.POST.get('poster_url')
    movie.description = request.POST.get('description')

    movie.save()

    return redirect('movies:detail', movie.pk)

# 단일 영화 데이터 삭제
# 단일 영화 데이터 삭제 및 index 페이지로 redirect
def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()

    return redirect('movies:index')

```

- 각 함수들의 기능은 주석을 통해 참고

---

### /movies/templates/movies/index.html

```html
{% extends 'base.html' %}

{% block content %}

  {% comment %} 1) New 페이지 생성, 가상 로그인 모달 포함한 NavBar {% endcomment %}
  {% comment %} NavBar {% endcomment %}
  <nav class="navbar navbar-expand-md navbar-dark bg-dark my-3">
    <div class="container-fluid">
      <h1 class="fw-bold text-white me-3">MOVIES</h1>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link active" href="{% url 'movies:new' %}">
              <h4 class="mx-3">NEW</h4>
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link active" href="#loginModal" data-bs-toggle="modal" data-bs-target="#exampleModal">
              <h4>LOGIN</h4>
            </a>
          </li>
        </ul>
      </div>
    </div>
  </nav>

  {% comment %} Virtual Modal {% endcomment %}
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

  {% comment %} 2) 포스터 이미지와 영화 정보 리스트 {% endcomment %}
  <div class="container">
    {% for movie in movies %}
    <div class="row p-3">
      <img src="{{movie.poster_url}}" alt="" class="col col-2">
      <div class="col col-6">
        <h4 class="fw-bold">{{movie.title}}</h4>
        <br>
        <p class="fw-semibold">장르: {{movie.genre}}</p>
        <p class="fw-semibold">평점: {{movie.score}}</p>
        <a href="{% url 'movies:detail' movie.pk %}" class="text-decoration-none text-secondary fst-italic fw-bold">[For More Information...]</a>
      </div>
    </div>
    <hr>
    {% endfor %}
  </div>

  {% comment %} 3) footer 설정 {% endcomment %}
  <footer>
    <div class="d-flex fixed-bottom justify-content-center mx-auto">
      <p>DJANGO PJT, by JINWOO PARK</p>
    </div>
  </footer>

{% endblock content %}

```

- 3번 프로젝트 시 활용했던 bootstrap navbar를 활용해봄
- `new.html`로 가는 anchoring text가 이뻐 보이지 않아 navigation bar안에 생성
- LOGIN은 3번 프로젝트 시 작성해봤던 가상의 로그인 modal임 (따로 기능 구현은 안했음)
- 반응형 웹페이지를 통해 일정 사이즈 이하가 되면 dropdown 버튼이 생김
- 본문 내용은 `Movie.objects.all()`을 통해 조회한 기존의 모든 영화 데이터를 반복 순회하여 출력
- For More Information...은 상세 정보로 넘어가는 anchoring text

---

### /movies/templates/movies/detail.html

```html
{% extends 'base.html' %}

{% block content %}
  <nav class="navbar navbar-expand-md navbar-dark bg-dark my-3">

    <div class="container-fluid">
      <h1 class="fw-bold text-white me-4">DETAIL</h1>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link active" href="{% url 'movies:edit' movie.pk %}">
              <h5 class="mx-3">[EDIT details]</h5>
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link active" href="{% url 'movies:index' %}">
              <h5 class="mx-3">[BACK to movies]</h5>
            </a>
          </li>
        </ul>
      </div>
    </div>

  </nav>

  <img src="{{movie.poster_url}}" alt=""><br>
  <h5 class="fw-bold my-3">{{movie.title}}</h5>
  <p class="fw-semibold">Audience: {{movie.audience}}</p>
  <p class="fw-semibold">Release Dates: {{movie.release_date}}</p>
  <p class="fw-semibold">Genre: {{movie.genre}}</p>
  <p class="fw-semibold">Score: {{movie.score}}</p>
  <p class="fw-semibold fst-italic">{{movie.description}}</p>
  <hr>

  <div class="my-2">
    <form action="{% url 'movies:delete' movie.pk %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="DELETE">
    </form>
  </div>

  <footer>
    <div class="d-flex fixed-bottom justify-content-center mx-auto">
      <p>DJANGO PJT, by JINWOO PARK</p>
    </div>
  </footer>
{% endblock content %}

```

- navigation bar의 [EDIT details]는 영화 데이터 수정용 페이지인 `edit.html`을 렌더링하도록 하는 버튼이며, [BACK to movies]는 `index.html`을 렌더링하여 전체 영화 데이터 조회
- DELETE 버튼을 통해 해당 영화 데이터 삭제 가능

---

### /movies/templates/movies/new.html

```html
{% extends 'base.html' %}

{% block content %}
  <nav class="navbar navbar-expand-md navbar-dark bg-dark my-3">

    <div class="container-fluid">
      <h1 class="fw-bold text-white me-1">NEW</h1>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link active" href="{% url 'movies:index' %}">
              <h5 class="mx-3">[BACK to movies]</h5>
            </a>
          </li>
        </ul>
      </div>
    </div>

  </nav>

  {% comment %} create용 POST form {% endcomment %}
  <form action="{% url 'movies:create' %}" method="POST">

    {% csrf_token %}

    <div class = 'my-3'>
      <label for="title" class="me-5">TITLE: </label>
      <input type="text" id="title" name="title">
    </div>

    <div class="my-3">
      <label for="audience" class="me-2">AUDIENCE: </label>
      <input type="text" id="audience" name="audience">
    </div>

    <div class="my-3">
      <label for="release_date" class="me-3">RELEASE_DATE: </label>
      <input type="date" id="release_date" name="release_date" value="연도-월-일">
    </div>

    <div class="my-3">
      <label for="genre" class="me-4">GENRE: </label>
      <select name="genre" id="genre">
        <option value="none" selected disabled>--Select Your Genre--</option>
        <option value="액션">액션</option>
        <option value="스릴러">스릴러</option>
        <option value="로맨스">로맨스</option>
        <option value="판타지">판타지</option>
        <option value="다큐멘터리">다큐멘터리</option>
        <option value="전쟁">전쟁</option>
        <option value="애니메이션">애니메이션</option>
        <option value="코미디">코미디</option>
        <option value="드라마">드라마</option>
        <option value="SF">SF</option>
        <option value="범죄">범죄</option>
        <option value="공포">공포</option>
        <option value="뮤지컬">뮤지컬</option>
      </select>
    </div>

    <div class="my-3">
      <label for="score" class="me-4">SCORE: </label>
      <input type="text" id="score" name="score">
    </div>

    <div class="my-3">
      <label for="poster_url" class="me-3">POSTER_URL: </label>
      <input type="text" id="poster_url" name="poster_url">
    </div>

    <div class="my-3 d-flex align-items-start">
      <label for="description" class="me-3">DESCRIPTION: </label>
      <textarea name="description" id="description" cols="21" rows="3"></textarea>
    </div>

    <input type="submit" value="SUBMIT">

  </form>
  <hr>

  {% comment %} Footer {% endcomment %}
  <footer>
    <div class="d-flex fixed-bottom justify-content-center mx-auto">
      <p>DJANGO PJT, by JINWOO PARK</p>
    </div>
  </footer>
{% endblock content %}

```

- `<form>`태그의 `<input>` 태그 중 date type을 처음 사용해봄
- `<form>`태그의 `<select>` 태그를 처음 사용해봄
- 공식문서를 찾아보면 어려운건 없었음

---

### /movies/templates/movies/edit.html

```html
{% extends 'base.html' %}

{% block content %}
  <nav class="navbar navbar-expand-md navbar-dark bg-dark my-3">

    <div class="container-fluid">
      <h1 class="fw-bold text-white">EDIT</h1>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link active" href="{% url 'movies:index' %}">
              <h5 class="mx-3">[BACK to movies]</h5>
            </a>
          </li>
        </ul>
      </div>
    </div>

  </nav>
  
  <form action="{% url 'movies:update' movie.pk %}" method="POST">

    {% csrf_token %}

    <div class = 'my-3'>
      <label for="title" class="me-5">TITLE: </label>
      <input type="text" id="title" name="title" value="{{movie.title}}">
    </div>

    <div class="my-3">
      <label for="audience" class="me-2">AUDIENCE: </label>
      <input type="text" id="audience" name="audience" value="{{movie.audience}}">
    </div>

    <div class="my-3">
      <label for="release_date" class="me-3">RELEASE_DATE: </label>
      <input type="date" id="release_date" name="release_date" value="{{movie.release_date|date:'Y-m-d'}}">
    </div>

    <div class="my-3">
      <label for="genre" class="me-4">GENRE: </label>
      <select name="genre" id="genre">
        <option value="{{movie.genre}}" selected>{{movie.genre}}</option>
        <option value="액션">액션</option>
        <option value="스릴러">스릴러</option>
        <option value="로맨스">로맨스</option>
        <option value="판타지">판타지</option>
        <option value="다큐멘터리">다큐멘터리</option>
        <option value="전쟁">전쟁</option>
        <option value="애니메이션">애니메이션</option>
        <option value="코미디">코미디</option>
        <option value="드라마">드라마</option>
        <option value="SF">SF</option>
        <option value="범죄">범죄</option>
        <option value="공포">공포</option>
        <option value="뮤지컬">뮤지컬</option>
      </select>
    </div>

    <div class="my-3">
      <label for="score" class="me-4">SCORE: </label>
      <input type="text" id="score" name="score" value="{{movie.score}}">
    </div>

    <div class="my-3">
      <label for="poster_url" class="me-3">POSTER_URL: </label>
      <input type="text" id="poster_url" name="poster_url" value="{{movie.poster_url}}">
    </div>

    <div class="my-3 d-flex align-items-start">
      <label for="description" class="me-3">DESCRIPTION: </label>
      <textarea name="description" id="description" cols="21" rows="3">{{movie.description}}</textarea>
    </div>

    <input type="reset" value="Reset">
    <input type="submit" value="Submit">

  </form>
  <hr>

  <footer>
    <div class="d-flex fixed-bottom justify-content-center mx-auto">
      <p>DJANGO PJT, by JINWOO PARK</p>
    </div>
  </footer>
{% endblock content %}

```

- `new.html`과 거의 유사하지만 해당 영화 데이터가 채워져있는 상태로 출력해줘야하는 것이 관건
- release_date 값을 넣어주는 것을 처음에 조금 헤맸음
- `<input type="date" id="release_date" name="release_date" value="{{movie.release_date|date:'Y-m-d'}}">`를 통해 구현
- genre의 경우 `<option value="{{movie.genre}}" selected>{{movie.genre}}</option>`와 같이 `<select>` 태그의 옵션들 중 해당 영화 인스턴스의 genre를 `selected`로 주어 기본값으로 설정

---

### 개선되어야 할 점

- DELETE 버튼의 위험성이 너무 큰 것 같다. 중간중간 데이터를 딱히 지우고 싶지 않았는데 아무 생각없이 지울뻔한 순간이 몇 번 있었다. DELETE 버튼을 누른다면 정말로 삭제할 것인지 double check하는 팝업 기능을 추가해야할 것 같다.

- 상세정보로 넘어가는 기능을 index page에서 각 영화란의 For More Information...을 누르는 것으로 구현하였는데 막상 만들고보니 직관성이 떨어지는 것 같다. 영화 title에 anchoring하거나, 해당 영화칸 전체를 하나의 버튼처럼(?) anchoring하는 것이 더 직관적일 것 같다.

---

### 후기

- 아직 django 초반이라 모르는 것이지만 지금까지는 재밌다. 구조짜고, 구조 간의 흐름을 읽고 하는 부분이 재밌는 것 같다.

- CSS 오랜만에 다루니 그새 많이 까먹었다. 프로젝트 진행 과정에 있어 django를 통한 모델링이나 기능 구현보다 페이지를 꾸며주는 것에 80% 정도의 시간을 할애한 것 같다.

---

# pjt02

## Django Framework를 통한 DB CRUD 및 영화 페이지 구현

---

- Modeling에 대한 이해
    - `models.py`
    - `forms.py`
- Django Framework를 활용한 CRUD 구현
    - MTV Structure
- Bootstrap 및 CSS 활용한 페이지 꾸미기

---

## 결과 사진

---

### 영화 목록 페이지 (전체 영화 데이터를 조회)
### /movies/index.html

<img width="1343" alt="index" src="https://user-images.githubusercontent.com/86648892/194557989-4e89d0e4-a759-4e05-a081-5098d0c89397.png">

---

### 영화 생성 페이지 (생성 페이지 렌더링 및 새로운 영화 데이터 생성)
### /movies/create.html

<img width="1352" alt="create1" src="https://user-images.githubusercontent.com/86648892/194557963-7517a74e-bb7d-42c8-b3e4-b552bea217a0.png">
<img width="1335" alt="create2" src="https://user-images.githubusercontent.com/86648892/194557969-147125f4-5bba-4f79-9dd6-5f75a1f84faa.png">

---

### 영화 상세정보 페이지 (선택한 영화의 상세정보)
### /movies/detail.html

<img width="1405" alt="detail1" src="https://user-images.githubusercontent.com/86648892/194557972-a38600f9-3995-4b77-bcda-50b01134b285.png">
<img width="1391" alt="detail2" src="https://user-images.githubusercontent.com/86648892/194557988-6bf29749-b4ba-49a1-963e-aac2e09456d0.png">

---

### 영화 정보수정 페이지 (기존 영화 데이터 수정)
### /movies/update.html

<img width="1379" alt="update1" src="https://user-images.githubusercontent.com/86648892/194557996-f2e5fdde-2f3d-4303-8731-9dd1aa3c76b9.png">
<img width="1364" alt="update2" src="https://user-images.githubusercontent.com/86648892/194558000-6063678d-2533-483d-82c9-8a0d4c0a5288.png">

---

## 핵심 코드

---

### /movies/models.py

```python
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=20) # 영화 제목
    audience = models.IntegerField()        # 관객 수
    release_date = models.DateField()       # 개봉일
    genre = models.CharField(max_length=30) # 장르
    score = models.FloatField()             # 평점
    poster_url = models.TextField()         # 포스터 경로
    description = models.TextField()        # 줄거리

    def __str__(self):
        return self.title
```

---

### /movies/forms.py

```python
from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = '__all__'

    # 영화제목 위젯
    title = forms.CharField(
        label='영화 제목',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '제목을 입력하세요.',
                'max_length': 20,
            }
        ),
    )

    # 관객수 위젯
    audience = forms.CharField(
        label='관객 수',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': '관객 수를 입력하세요.',
            }
        ),
    )

    # 개봉일 위젯
    release_date = forms.DateField(
        label='개봉일',
        widget=forms.DateInput(
            format=('%Y-%m-%d'),
            attrs={
                'class': 'form-control',
                'type': 'date',
            }
        ),
    )

    # 장르 위젯
    GENRE = [
        ('Comedy', '코미디'),
        ('Horror', '호러'),
        ('Romance', '로맨스'),
        ('Drama', '드라마'),
        ('Action', '액션'),
        ('SF', 'SF'),
        ('Noir', '느와르'),
    ]
    genre = forms.ChoiceField(
        choices=GENRE,
        label='장르',
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
    )

    # 평점 위젯
    score = forms.CharField(
        label='평점',
        widget=forms.NumberInput(
            attrs={
                'step': 0.5,
                'min': 0,
                'max': 5,
                'class': 'form-control',
                'placeholder': '0점~5점 중 평점을 입력하세요.',
            }
        ),
    )

    # 포스터 경로 위젯
    poster_url = forms.CharField(
        label='포스터 경로',
        initial='https://web.yonsei.ac.kr/_ezaid/board/_skin/albumRecent/3/no_image.gif',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
            }
        ),
    )

    # 줄거리 위젯
    description = forms.CharField(
        label='줄거리',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': '줄거리를 입력하세요.',
            }
        ),
    )
```

---

### /movies/views.py

```python
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_safe, require_POST
from .models import Movie
from .forms import MovieForm


@require_safe
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method=="POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {
        'form': form,
    }
    return render(request, 'movies/create.html', context)


@require_safe
def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)


@require_http_methods(['GET', 'POST'])
def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm(instance=movie)
    context = {
        'form': form,
        'movie': movie,
    }
    return render(request, 'movies/update.html', context)


@require_POST
def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return redirect('movies:index')
```

---

### /movies/index.html

```html
{% extends 'base.html' %}

{% block content %}
<br>
<div>
  <h1 class='text-center' style='font-weight: bolder'>INDEX</h1>
  <a href="{% url 'movies:create' %}">
    <button type="button" class="btn btn-primary">CREATE</button>
  </a>
</div>
<hr>

<div class='row row-cols-1 row-cols-md-5 g-4'>
  {% for movie in movies %}
    <div class='col'>
      <div class='card h-200'>
        <a href="{% url 'movies:detail' movie.pk %}">
          <img src="{{ movie.poster_url }}" class='card-img-top' alt="그림">
        </a>
        <div class='card-body'>
          <h5 class='text-center' style='font-weight: bold'>{{ movie.title }}</h5>
          <h6 class='text-center' style='font-weight: bold'>{{ movie.genre }} / {{ movie.score }}</h6>
        </div>
      </div>
    </div>
  {% endfor %}
</div>
{% endblock content %}
```

---

### /movies/create.html

```html
{% extends 'base.html' %}

{% block content %}
  <h1>CREATE</h1>

  <form action="{% url 'movies:create' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="CREATE" style="background-color:rgb(0, 100, 255)">
  </form>
  <hr>

  <a href="{% url 'movies:index' %}">
    <button type="button" class="btn btn-warning">BACK</button>
  </a>
{% endblock content %}
```

---

### /movies/detail.html

```html
{% extends 'base.html' %}

{% block content %}
  <h1 class='text-center' style="margin:100 auto">DETAIL</h1>
  <hr>

  <div class='container row' style="margin:100 auto;">
    <div class="col-md-5" style="margin:0 auto;">
      <img src="{{ movie.poster_url }}" class="align-items-center" style="width: 30rem;" alt="사진">
      <hr>
      <h4 style='font=weight: bold'> {{ movie.title }}</h4><br>
      <p> Audience : {{ movie.audience }}</p>
      <p> Release Dates : {{ movie.release_date }}</p>
      <p> Genre : {{ movie.genre }}</p>
      <p> Score : {{ movie.score }}</p>
      <p> {{ movie.description }} </p>
      <hr>

      <a href="{% url 'movies:update' movie.pk %}" style="margin:1%;">
        <button type="button" style="background-color:rgb(0, 100, 255)">UPDATE</button>
      </a>
      <form action="{% url 'movies:delete' movie.pk %}" method='POST' style="margin:1%;">
        {% csrf_token %}
        <input type="submit" value="DELETE" style="background-color:rgb(255, 0, 50)">
      </form>
      <hr>

      <a href="{% url 'movies:index' %}" style="margin:1%;;">
        <button type="button" class="btn btn-warning">BACK</button>
      </a>
    </div>
  </div>
{% endblock content %}
```

---

### /movies/update.html

```html
{% extends 'base.html' %}

{% block content %}
  <h1>UPDATE</h1>

  <form action="{% url 'movies:update' movie.pk %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="UPDATE" style="background-color:rgb(0, 100, 255)">
    <input type="reset" value="CANCEL" style="background-color:rgb(0, 100, 255)">
  </form>
  <hr>

  <a href="{% url 'movies:detail' movie.pk %}">
    <button type="button" class="btn btn-warning">BACK</button>
  </a>
{% endblock content %}
```

---

## 후기 및 느낀 점

- 버튼을 구현하는 과정에 있어서 단순히 링크를 이동하는 `<a>` 태그에 `<button>` 태그를 넣어서 버튼 모양을 구현하고, 여기에 bootstrap class를 활용한 버튼 스타일을 구현했다.

- 반면 DB를 건드리게 되는 POST 요청을 수행하는 버튼들의 경우 `<form>` 태그 내의 `<input type="submit">` 태그로 구현했다. POST 요청을 하지 않는 버튼과 달리 bootstrap class를 통해 구현하려고 했을 때는 정상작동하지 않았다.

- ModelForm의 다양한 위젯을 활용해볼 수 있었다. 문서를 조금 더 찾아보자.

- css나 bootstrap 활용이 아직 미숙한 것 같다. 개인적으로 django를 통해 모델링하고, crud하는 과정이 더 재밌게 느껴진다.

- 전체 영화 데이터를 조회하는 목록 페이지의 경우 bootstrap의 card component를 활용하였다.

---

# pjt03

## DRF를 통한 RESTful API 서버 구현

---

- Django REST Framwork를 통한 CRUD 구현
- serializers에 대한 이해
- Postman을 활용한 API 결과 확인

---

### 모델링

```python
from django.db import models

# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateTimeField()
    poster_path = models.TextField()

    actors = models.ManyToManyField(Actor, related_name='movies')

    def __str__(self):
        return self.title


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title
```

---

### URL 구성

#### mypjt/urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('movies.urls')),
]
```

#### movies/urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path('actors/', views.actor_list),
    path('actors/<int:actor_pk>/', views.actor_detail),
    path('movies/', views.movie_list),
    path('movies/<int:movie_pk>/', views.movie_detail),
    path('reviews/', views.review_list),
    path('reviews/<int:review_pk>/', views.review_detail),
    path('movies/<int:movie_pk>/reviews/', views.create_review),
]
```

---

### custom serializer 생성

#### movies/serializers.py

```python
from rest_framework import serializers
from .models import Actor, Movie, Review

class ActorNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('name',)


class MovieTitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title',)


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('title', 'content',)


class ReviewDetailSerializer(serializers.ModelSerializer):
    movie = MovieTitleSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'


class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('title', 'content',)


class MovieSerializer(serializers.ModelSerializer):
    review_set = ReviewSerializer(many=True, read_only=True)
    actors = ActorNameSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'overview',)


class ActorSerializer(serializers.ModelSerializer):
    movies = MovieTitleSerializer(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = '__all__'


class ActorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'
```

---

### view 함수 정의 및 API 요청 결과

#### movies/views.py

```python
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import get_object_or_404, get_list_or_404

from .models import Actor, Movie, Review
from .serializers import ActorListSerializer, ActorSerializer, MovieListSerializer, MovieSerializer, ReviewListSerializer, ReviewDetailSerializer
```

---

#### 전체 배우 목록 제공
![get_actors](https://user-images.githubusercontent.com/86648892/197134623-0042f606-12ee-45c6-ac90-5b7e844b7a53.png)

```python
@api_view(['GET'])
def actor_list(request):
    actors = get_list_or_404(Actor)
    serializer = ActorListSerializer(actors, many=True)
    return Response(serializer.data)

```

#### 단일 배우 정보 제공 (출연 영화 제목 포함)
![get_actor](https://user-images.githubusercontent.com/86648892/197134625-b8fa1d20-c092-4f8c-8445-4b1b7f674941.png)

```python
@api_view(['GET'])
def actor_detail(request, actor_pk):
    actor = get_object_or_404(Actor, pk=actor_pk)
    serializer = ActorSerializer(actor)
    return Response(serializer.data)
```

#### 전체 영화 목록 제공
![get_movies](https://user-images.githubusercontent.com/86648892/197134627-7c93fd3c-2913-4774-89c1-87eccd689028.png)

```python
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)
```

#### 단일 영화 정보 제공 (출연 배우 이름과 리뷰 목록 포함)
![get_movie](https://user-images.githubusercontent.com/86648892/197134605-9820906d-c75b-45e4-b192-b769214b033c.png)

```python
@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)
```

#### 전체 리뷰 목록 제공
![get_reviews](https://user-images.githubusercontent.com/86648892/197134611-60c8f756-6fb9-4bb7-be5d-c237e6582887.png)

```python
@api_view(['GET'])
def review_list(request):
    reviews = get_list_or_404(Review)
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)
```

#### 단일 리뷰 조회 & 수정 & 삭제 (출연 영화 제목 포함)
![get_review](https://user-images.githubusercontent.com/86648892/197134615-b4bba543-43bf-4478-85f8-74a7b1538cd7.png)
![put_review](https://user-images.githubusercontent.com/86648892/197134617-98fbc448-a040-479d-94e9-f9084b935002.png)
![delete_review](https://user-images.githubusercontent.com/86648892/197149436-ac4c6216-0c2c-4334-9223-dffb14246727.png)
5-bc46-fdbef7c0c831.png)

```python
@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    # GET
    if request.method == 'GET':
        serializer = ReviewDetailSerializer(review)
        return Response(serializer.data)

    # PUT
    if request.method == 'PUT':
        serializer = ReviewDetailSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    # DELETE
    if request.method == 'DELETE':
        review.delete()
        data = {
            'delete': f'review {review_pk} is deleted',
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
```

#### 리뷰 생성
![post_review](https://user-images.githubusercontent.com/86648892/197134622-4c5a4568-f519-4f15-bc46-fdbef7c0c831.png)

```python
@api_view(['POST'])
def create_review(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewDetailSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
```

---

### 후기 및 느낀 점

- 모델에서 serializer를 통하여 필요한 정보를 빼오고, CRUD하는 과정에 어느정도 익숙해진 것 같다.

- Django로 template 파일 작성하는 부분이 개인적으로 달갑지 않은 작업이었는데, 이제 하지 않아도 되서 좋다.

- 필요한 정보를 그때 그때 맞게 출력하기 위해 serializer를 계속 새로 정의해주는 작업이 있었는데, 이 방법이 최선인가라는 궁금증이 들었다.

- serializer 내에서 참조하는 모델의 필드명과 동일한 이름의 속성을 정의하면 해당 속성으로 override된다.

---

# pjt04

## 알고리즘을 이용한 영화 서버 및 페이지 구현

---

### 프로젝트 목표

- Django MTV 구조 recap
- Django를 통한 영화 데이터 관리
- Axios를 활용한 AJAX 요청을 통해 좋아요 및 팔로잉 구현
- 페어 프로젝트 경험

---

### 모델링

#### movies/models.py

```python
from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)


class Movie(models.Model):
    genres = models.ManyToManyField(Genre, related_name="movies")
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
```

#### community/models.py

```python
from django.db import models
from django.conf import settings


# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_reviews")
    title = models.CharField(max_length=100)
    movie_title = models.CharField(max_length=50)
    rank = models.IntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE) 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.content
```

#### accounts/models.py

```python
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name="followers")
```

---

### URL 구성

```python

# mypjt/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls')),
    path('community/', include('community.urls')),
    path('accounts/', include('accounts.urls')),
]

# movies/urls.py

from django.contrib import admin
from django.urls import path
from . import views

app_name='movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('recommended/', views.recommended, name='recommended'),
]

# community/urls.py

from django.contrib import admin
from django.urls import path
from . import views

app_name='community'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:review_pk>/', views.detail, name='detail'),
    path('<int:review_pk>/comments/create/', views.create_comment, name='create_comment'),
    path('<int:review_pk>/likes/', views.likes, name='likes'),
]

# accounts/urls.py

from django.contrib import admin
from django.urls import path
from . import views

app_name='accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('<str:username>/', views.profile, name='profile'),
    path('<int:user_pk>/follow/', views.follow, name='follow'),
]
```

---

### View Functions

![movie_index](https://user-images.githubusercontent.com/86648892/199936151-f1092456-4a65-4218-84f4-6650fea52ff5.png)

![movie_detail](https://user-images.githubusercontent.com/86648892/199936163-cfeaf543-473f-4403-9a62-a1b91616642b.png)

![movie_recommend](https://user-images.githubusercontent.com/86648892/199936159-e1b93e79-a8cc-44aa-bb67-415d0b94faa9.png)

#### movies/views.py

```python
from django.shortcuts import render
from django.views.decorators.http import require_safe
from .models import Movie


# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request,'movies/index.html', context)


@require_safe
def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    objects = list(movie.genres.all())
    genres = []
    for genre in objects:
        genres.append(genre.name)
    context = {
        'movie': movie,
        'genres': genres,
    }
    return render(request,'movies/detail.html', context)


@require_safe
def recommended(request):
    movies = Movie.objects.order_by('?')[:10]
    context = {
        'movies': movies,
    }
    return render(request,'movies/recommended.html', context)
```

![review_list](https://user-images.githubusercontent.com/86648892/199936166-ae8f318d-915d-49e7-aa95-65f31a32b402.png)

![review_detail](https://user-images.githubusercontent.com/86648892/199936170-e4f76eae-a34a-4bf1-94ae-abc99dcdc4fe.png)

#### community/views.py

```python
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import ReviewForm, CommentForm
from django.http import JsonResponse


# Create your views here.
@require_safe
def index(request):
    reviews = Review.objects.all()
    context = {
        'reviews' : reviews
    }
    return render(request, 'community/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('community:detail', review.pk)
    else:
        form = ReviewForm()
    context = {
        'form':form,
    }
    return render(request, 'community/create.html', context)


@require_safe
def detail(request,review_pk):
    review = Review.objects.get(pk=review_pk)
    comment_form = CommentForm()
    comments = review.comment_set.all()
    context = {
        'review' : review,
        'comment_form' : comment_form,
        'comments' : comments,
    }
    return render(request, 'community/detail.html', context)


@require_POST
def create_comment(request,review_pk):
    if request.user.is_authenticated:
        review = Review.objects.get(pk=review_pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.review = review
            comment.user = request.user
            comment.save()
        return redirect('community:detail', review.pk)
    return redirect('accounts:login')


@require_POST
def likes(request,review_pk):
    if request.user.is_authenticated:
        review = Review.objects.get(pk=review_pk)
        if review.like_users.filter(pk=request.user.pk).exists():
            review.like_users.remove(request.user)
            is_liked = False
        else:
            review.like_users.add(request.user)
            is_liked = True
        context = {
            'is_liked': is_liked,
            'likes_count': review.like_users.count()
        }
        return JsonResponse(context)
    return redirect('accounts:login')
```

![profile](https://user-images.githubusercontent.com/86648892/199936171-7f501ee9-1a65-4e0f-8879-dd1308e73d27.png)

#### accounts/views.py

```python
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm
from django.http import JsonResponse


# Create your views here.
@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('community:index')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('community:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('community:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'community:index')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)


@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('community:index')


def profile(request, username):
    User = get_user_model()
    person = User.objects.get(username=username)
    context = {
        'person' : person,
    }
    return render(request, 'accounts/profile.html', context)


@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        User = get_user_model()
        me = request.user
        you = User.objects.get(pk=user_pk)
        if me != you:
            if you.followers.filter(pk=me.pk).exists():
                you.followers.remove(me)
                is_followed = True
            else:
                you.followers.add(me)
                is_followed = False
            context = {
                'is_followed': is_followed,
                'followers_count': you.followers.count(),
                'followings_count': you.followings.count(),
            }
            return JsonResponse(context)
        return redirect('accounts:profile', you.username)
    return redirect('accounts:login')
```

---

### 목표에 대한 결과

- Django MTV 구조 recap

  - 모델링부터 시작하여 마이그레이션, URL 구성, 그에 따른 view 함수 구성 및 template 구성 등 전반적인 Django 활용에 대한 복습이 가능했다.

- Django를 통한 영화 데이터 관리

  - fixtures 파일을 통해 쉽게 데이터를 로드하는 법을 다시 한번 연습할 수 있었다.

- Axios를 활용한 AJAX 요청을 통해 좋아요 및 팔로잉 구현

  - 좋아요와 팔로우 기능에 대해 새로운 페이지를 새로고침하는 것에서 벗어나 axios를 통한 비동기 요청 및 JsonResponse 활용을 통해, 페이지의 새로고침없이 LIKE 버튼과 FOLLOW 버튼의 상태 변경 및 좋아요, 팔로워, 팔로잉 숫자 변경이 가능하도록 구현했다.

- 페어 프로젝트 경험

  - driver와 navigator로서의 역할을 모두 수행해본 결과, 어느 한쪽 다 쉬운 역할이 없다고 생각하였다. navigator는 조금 더 상세하게 안내를 하고, drvier로서는 수동적인 태도가 아닌 어느정도 navigator의 호흡에 잘 맞춰야 한다고 느꼈다. 협업이 익숙치 않아 아직 오히려 작업 속도가 더딘 기분이었지만, 익숙해진다면 훨씬 개발하는데 있어 생산성이 높아질 것이며, 부족한 부분도 보완할 수 있다고 생각한다.

---

# pjt05

## vue-cli, vuex, router를 활용한 영화 페이지 구현

---

### 프로젝트 목표

- 영화 정보를 제공하는 SPA 제작
- AJAX 통신과 JSON 구조에 대한 이해
- Vue CLI, Vue Router 플러그인 활용

### API

- [TMDBAPI - Top Rated Movies](https://developers.themoviedb.org/3/movies/get-top-rated-movies)
- [OpenWeatherMapAPI - Current Weather by city name](https://openweathermap.org/current#name)

### 참고 링크

- [Vue CLI Bootstrap 적용하기](https://velog.io/@gillog/Vue.js-Bootstrap-%EC%A0%81%EC%9A%A9%ED%95%98%EA%B8%B0)
- [Vue CLI Bootstrap Card Component 활용](https://carrotweb.tistory.com/174)

### 구현 기능

- 최고 평점 영화 출력 (MovieView)
- 최고 평점 영화 중 랜덤 영화 한 개 출력 (RandomView)
  - OpenWeatherMap으로부터 받아온 현재 날씨도 함께 출력
- 보고싶은 영화 등록 및 삭제 (WatchListView)

---

## MovieView and MovieCard

<img width="1909" alt="MovieView" src="https://user-images.githubusercontent.com/86648892/201368472-9d2b32a4-e1d1-418b-b29c-e42ebf94a4ff.png">

### Code Snippets

#### MovieView.vue

```jsx
<template>
  <div>
    <h1>MovieView</h1>
    <div class="py-5">
      <div class="c">
        <div class="row row-cols-1 row-cols-sm-2 row-cols-md-4">
          <MovieCard
            v-for="movieCard in movieCards"
            :key="movieCard.id"
            :movieCard="movieCard"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import MovieCard from "@/components/MovieCard"

export default {
  name: "MovieView",
  components: {
    MovieCard,
  },
  computed: {
    movieCards() {
      return this.$store.state.movieCards
    },
  },
  created: function () {
    this.$store.dispatch("loadMovieCards")
  },
}
</script>

<style>
.c {
  margin-left: 20px;
  margin-right: 20px;
  text-align: center;
}
</style>
```

#### MovieCard.vue

```jsx
<template>
  <div>
    <div class="col">
      <div class="card h-100 m-3">
        <img :src="posterPath" class="card-img-top" alt="" />
        <div class="card-body">
          <h5 class="text-center" style="font-weight: bold">
            {{ movieCard.title }}
          </h5>
          <div class="card-text">{{ movieCard.overview }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MovieCard",
  props: {
    movieCard: Object,
  },
  computed: {
    posterPath() {
      return "https://image.tmdb.org/t/p/w500" + this.movieCard.poster_path
    },
  },
}
</script>

<style>
.card {
  max-width: 100%;
}
.card-text {
  width: 100%;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 4;
  -webkit-box-orient: vertical;
  text-align: justify;
  text-indent: 7px;
  line-height: 2rem;
}
.card-img-top {
  width: 100%;
  height: 30rem;
  object-fit: cover;
}
</style>
```

- TMDBAPI의 최고 평점 영화들을 axios 요청을 통해 가져온 뒤 Bootstrap Card Component를 활용하여 출력하였다.

- axios 요청을 통해 영화 데이터를 가져오는 것은 수월하게 진행되었으나 v-for directive를 통해 MovieView에서 하위 컴포넌트인 MovieCard로 각 영화 데이터를 넘겨주는 과정에서 각 row마다 3개씩의 영화 카드를 삽입할지에 대해 잠시 막혔었다. 시도 끝에 위와 같이 구현하였다.

---

## RandomView and OpenWeatherMap API

### Code Snippets

#### RandomView.vue

<img width="1915" alt="RandomView" src="https://user-images.githubusercontent.com/86648892/201368489-4e49ad41-010c-4b9b-b9b2-b006f6b7eca5.png">

```jsx
<template>
  <div>
    <h2>오늘의 날씨는 {{ currentWeather }}! 이런 영화 어때요?</h2>
    <div style="width: 50%; width: 315px; margin: auto">
      <button
        class="btn btn-success"
        @click="pickMovie"
        style="display: block; width: 315px"
      >
        PICK
      </button>
      <div class="card h-200" v-if="isSelected">
        <img
          :src="`https://image.tmdb.org/t/p/original${this.movie.poster_path}`"
          class="card-img-top"
        />
        <div class="card-body">
          <h5 class="text-center" style="font-weight: bold; margin: 0px">
            {{ movie.title }}
          </h5>
        </div>
      </div>
    </div>
    <img src="" alt="" />
  </div>
</template>

<script>
import _ from "lodash"

export default {
  name: "RandomView",
  data() {
    return {
      movie: null,
      isSelected: false,
    }
  },
  methods: {
    pickMovie() {
      this.isSelected = true
      const rand_idx = _.random(0, 19)
      const selectedMovie = this.$store.state.movieCards[rand_idx]
      this.movie = selectedMovie
    },
  },
  computed: {
    currentWeather() {
      return this.$store.state.currentWeather
    }
  },
}
</script>

<style></style>
```

- lodash를 통해 랜덤한 영화 추천을 구현하였다. TMDB API 검토 중 poster_path의 끝이 original로 끝나는 url로 요청하면 더 좋은 해상도의 이미지를 가져올 수 있음을 확인하였다.

- OpenWeatherMap API의 현재 날씨 정보를 가져오는 방법을 공식 문서를 통해 확인하여 axios 요청을 통해 현재 날씨 정보의 description 키에 담겨 있는 값을 가져와 함께 출력해주었다. 해당 데이터가 담겨있도록 lifecycle hooks 중 created를 활용하여 App.vue가 생성될 때 해당 데이터를 가져오도록 설정하였다.

---

## WatchListView and WatchListForm and WatchListItem

<img width="1917" alt="WatchListView" src="https://user-images.githubusercontent.com/86648892/201368497-f9db4a1d-217d-473f-ade2-42d1429b0de8.png">

### Code Snippets

#### WatchListView.vue

```jsx
<template>
  <div>
    <WatchListForm />
    <WatchListItem
      v-for="(list, index) in watchList"
      :key="index"
      :list="list"
    />
    <button @click="loadList">저장했던 것 불러오기</button>
  </div>
</template>

<script>
import WatchListForm from "@/components/WatchListForm"
import WatchListItem from "@/components/WatchListItem"

export default {
  name: "WatchListView",
  components: {
    WatchListForm,
    WatchListItem,
  },
  computed: {
    watchList() {
      return this.$store.state.watchList
    },
  },
  methods:{
    loadList(){
      this.$store.dispatch('loadList')
    }
  }
}
</script>
```

#### WatchListForm.vue

```jsx
<template>
  <div class="watchform" style="padding: 35px">
    <h1><label for="title">보고싶은 영화</label></h1>
    <input type="text" id="title" v-model="title" @keyup.enter="addmovie" />
    <button @click="addmovie">add</button>
  </div>
</template>

<script>
export default {
  name: "WatchListForm",
  data() {
    return {
      title: null,
    }
  },
  methods: {
    addmovie() {
      const title = this.title
      if (this.title) {
        this.$store.dispatch("createWatchList", title)
      }
      this.title = null
    },
  },
}
</script>

<style>
.watchform {
  background-color: rgb(228, 242, 253) !important;
}
</style>
```

#### WatchListItem.vue

```jsx
<template>
  <div
    :class="{ 'is-completed': list.isCompleted }"
    style="padding: 10px; border: 0.1px black solid"
  >
    <span @click="updateStatus()">
      {{ list.title }}
    </span>
    <button @click="deleteList">삭제</button>
  </div>
</template>

<script>
export default {
  name: "WatchListItem",
  props: {
    list: Object,
  },
  computed: {
    watchlist() {
      return this.$store.state.WatchList
    },
  },
  methods: {
    updateStatus() {
      this.$store.dispatch("updatedWatchList", this.list)
    },
    deleteList() {
      this.$store.dispatch("deleteList", this.list)
    },
  },
}
</script>

<style>
.is-completed {
  text-decoration: line-through;
  background-color: rgb(238, 238, 238);
}
</style>
```

- WatchListView의 하위 컴포넌트로 보고싶은 영화를 추가할 수 있는 컴포넌트인 WatchListForm과 추가한 영화들을 볼 수 있는 컴포넌트인 WatchListItem을 만들었다.

- Local Storage를 활용하여 기존에 추가했던 영화를 유지할 수 있도록 하였다.

- WatchListItem의 경우 각 영화 아이템들을 style의 border를 통해 구분할 수 있도록 하였고, 이미 본 영화로 처리할 경우 제목에 line-through로 표시하는 것과 함께 해당 셀은 회색으로 변경되도록 처리하였다.

- 사실 이미 본 영화에 대해 line-through style만을 적용하고, 기존에 영화 아이템들을 추가할 때 흰색과 회색을 번갈아가며 주고 싶었는데 원하는대로 잘 진행되지 않아서 위와 같이 하도록 조원들과 타협을 봤다.

---

## 전반적인 후기

- 첫 페어 프로그래밍에는 혼자 작업하는 것에 비해 작업 속도가 더디고, 약간 답답하다는 느낌을 조금은 받았던 것 같다. 하지만 금번 페어 프로그래밍에서는 오히려 협업을 통해 동일 시간 내에 혼자 할 수 없던 작업을 할 수 있다는 것을 느낀 시간이었다. 더불어 함께 해야할 일들을 리스트업하고, 문제를 해결하는 과정에서 즐거움을 느낄 수 있었다.

- vue-cli 활용 및 axios를 통한 API 요청을 연습하고 적용해보면서 더 익숙해질 수 있는 시간이었다.

---