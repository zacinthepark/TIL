# Django Practice 1 (Templates, Views, Models, admin account)

### Django Framework를 통한 데이터베이스 활용 및 영화 페이지 구현

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