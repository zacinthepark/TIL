## MTV 기초

---

- View
    - [CRUD with view functions](#crud-with-view-functions)

## CRUD with view functions

---

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
