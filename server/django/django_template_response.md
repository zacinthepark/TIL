## Template Response

---

- https://github.com/django/django/blob/main/django/shortcuts.py

- https://docs.djangoproject.com/en/4.2/ref/templates/builtins/

- https://docs.djangoproject.com/en/4.2/howto/custom-template-tags/

### render

- view 함수에서 context와 함께 렌더링할 html 파일을 응답으로 반환
    - `from django.shorcuts import render`
    - `render(HttpRequest, Tempalte, [context])`

- context는 view 함수에서 template으로 전달하는 데이터를 의미
    - key:value 형태의 딕셔너리 타입으로 지정

```python
# urls.py
urlpatterns = [
    ...
    path('greeting/', views.greeting)
]

# views.py
def greeting(request):
    foods = ['apple', 'banana', 'coconut']
    info = {
        'name': 'Alice'
    }
    context = {
        'foods': foods, 
        'info': info
    }
    return render(request, 'greeting.html', context)

# greeting.html
# {{food.0}}
# {{info.name}}

```

### 템플릿 필터

- 공식문서 참조

- `{{값 | 필터}}`
    - `{{값1 | 필터: 값2}}`
    - `{{값1 | 필터1: 값2 | 필터2}}`

```python
# views.py
def test(request):
    var = '''
        Miracles happen to only those who believe in them.
        Think like a man of action and act like man of thought.
        Courage is very important. Like a muscle, it is strengthened by use.
        Life is the art of drawing sufficient conclusions from insufficient premises.
        By doubting we come at the truth.
        A man that has no virtue in himself, ever enview virtue in others.
        When money speaks, the truth keeps silent.
        Better the last smile than the first laughter.
    '''

    return render(request, 'blog/test.html', {'var': var})

```

```html
<!-- blog/test.html -->

{{var}}
<hr>
{{var|linebreaks}}
<hr>
{{var|truncatechars:100}}
<hr>
{{var|truncatewords:50}}

```

```python
# settings.py
LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'

# views.py
from django.utils import timezone

def test(request):
    d1 = timezone.now()
    d2 = timezone.datetime(2001, 3, 19)
    d3 = timezone.datetime(2030, 3, 19)

    return render(request, 'blog/test.html', {'date1': d1, 'date2': d2, 'date3': d3})

```

```html
<!-- blog/test.html -->

{{date1}}<br>
{{date1|date:'Y-m-d'}}<br>
{{date1|time:'P'}}<br>
{{date2|timesince}}<br>
{{date3|timeuntil}}

```

### 템플릿 태그

#### for

```html
<h1>Book List</h1>
{% for book in book_list %}
    <a href="{% url 'book:detail' book.id %}"> {{book.title}}</a><br>
{% endfor %}
<a href="{% url 'book:create' %}">[Register New Book]</a>

```

#### if

```html
{% if score %}
    Score: {{score}}
{% endif %}<br>

{% if score >= 90 %}
    Grade: A
{% elif score >= 80 %}
    Grade: B
{% else %}
    Grade: C
{% endif %}

```

### 템플릿 상속

```html
<!-- layout.html -->

<html>
<head>
    <meta charset="utf-8" />
    <title>{% block title %}{% endblock %}</title>
    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"/>
    <style>
        html {position: relative; min-height: 100%}
        body{margin-bottom: 60px}
        #page-footer{
            position: absolute;
            bottom: 0;
            width:100%;
            height: 60;
            line-height: 60px;
            background-color: #f5f5f5;
        }
    </style>
</head>
<body>
    <nav class="navbar navbar-default">
        <div class="container">
            <div id="navbar" class="collapse navbar-collapse">
                <ul class="nav navbar-nav">
                    <li class="active"><a href="/blog/">Home</a></li>
                    <li><a href="#">About</a></li>
                    <li><a href="#">Contact</a></li>
                </ul>
                <ul class="nav navbar-nav navbar-right">
                    {% if not user.is_authenticated %}
                        <li><a href="{% url 'signup' %}">회원가입</a></li>
                        <li><a href="{% url 'login' %}?next={{request.path}}">로그인</a></li>
                    {% else %}
                        <li><a href="">{{user}}님!</a> </li> 
                        <li><a href="{% url 'profile' %}">내정보</a></li>
                        <li><a href="{% url 'logout' %}?next={{request.path}}">로그아웃</a></li>
                    {% endif %}
                 </ul>
                </div>
        </div>
    </nav>
    <div class="container">
        <div class="row">
            <div class="col-sm-12">
                {% if messages %}
                    <ul>
                        {% for message in messages %}
                            <li>{{ message }}</li>
                        {% endfor %}
                    </ul>
                {% endif %} 

                {% block content %}
                {% endblock %}
            </div>            
        </div>
    </div>
    <div id="page-footer">
        <div class="container">
            <p class="text-muted">
                Copyright © 2020 KINO Data Systems All Right Reserved
            </p>
        </div>
    </div>
</body>
</html>

```

```html
<!-- book_list.html -->

{% extends "layout.html" %}
{% block title %} Book List {% endblock %}
{% block content %}
    <h1>Book List</h1>
    {% for book in book_list %}
        <a href="{% url 'book:detail' book.id %}"> {{book.title}}</a><br>
    {% endfor %}
    <a href="{% url 'book:create' %}">[Register New Book]</a>
{% endblock %}

```
