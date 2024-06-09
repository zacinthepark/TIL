## Generic Display View

---

- https://github.com/django/django/blob/4.2/django/views/generic/list.py
- https://github.com/django/django/blob/4.2/django/views/generic/detail.py

### ListView

- model 속성에 지정된 모델의 모든 인스턴스들을 추출한 후 템플릿에 컨텍스트로 전달하는 Generic View
    - 모델명 속성: model
    - 기본 템플릿명: `앱이름/모델명소문자_list.html`
    - 기본 컨텍스트: `모델명소문자_list` 또는 `object_list`
        - 모델의 모든 인스턴스를 가진 QueryDict 객체

```python
# urls.py
from django.urls import path
from django.views.generic import ListView
from .models import Book

app_name ='book'

urlpatterns = [
    path('', ListView.as_view(model=Book), name='list'),
    ...
]

```

```html
<!-- book/templates/book/book_list.html -->
{% for book in book_list %}
    <a href="{% url 'book:detail' book.id %}"> {{book.title}}</a><br>
{% endfor %}

```

### DetailView

- path 변수로 Primary Key를 전달받아 model 속성에 지정된 모델에서 추출한 후 템플릿에 컨텍스트로 전달하는 Generic View
    - 모델명 속성: model
    - 기본 템플릿명: `앱이름/모델명소문자_detail.html`
    - 기본 컨텍스트: `모델명소문자`
        - 조회하는 모델 인스턴스 객체

```python
# urls.py
from django.urls import path
from django.views.generic import DetailView
from .models import Book

app_name ='book'

urlpatterns = [
    path('detail/<pk>/', DetailView.as_view(model=Book), name='detail'),
    ...
]

```

```python
# models.py
from django.db import models
from django.urls import reverse

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book:list')

```

```html
<!-- book/templates/book/book_detail.html -->
Title: {{book.title}}<br>
Author: {{book.author}}<br>
Publisher: {{book.publisher}}<br>

```
