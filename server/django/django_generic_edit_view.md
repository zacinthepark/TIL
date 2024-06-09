## Generic Edit View

---

- https://github.com/django/django/blob/4.2/django/views/generic/edit.py

### CreateView

- 데이터 추가 기능이 구현된 Generic View로 Django Form을 기반으로 동작
    - model: 필수 속성으로 모델명 지정
    - form_class: Form을 지정하며, 미지정 시 모델 기반으로 ModelForm이 자동으로 생성됨
    - template_name: GET 방식 또는 Form의 유효성 검사 실패 시 응답할 템플릿 지정
    - success_url: POST 방식으로 요청되어 데이터 추가 작업이 완료된 후 이동할 URL을 지정하며, 미지정 시 모델의 `get_absolute_url()` 메서드가 반환하는 URL로 이동
    - fields: 별도의 Form을 지정하지 않고 모델 기반의 ModelForm을 생성하여 사용할 때 Form의 필드로 사용할 모델 필드를 지정
    - 기본 템플릿명: `앱이름/모델명소문자_form.html`
    - 기본 컨텍스트: `form`: form_class 속성에 지정된 또는 모델 기반으로 생성한 Form 객체

- GET 방식으로 요청 시
    - template_name 속성에 지정된 템플릿, 또는 미지정 시 `앱이름/모델명소문자_form.html` 템플릿을 응답
    - 응답된 템플릿은 추가할 데이터를 입력받기 위한 입력 페이지로서 입력 폼은 form 이름의 컨텍스트로 전달된 form_class 속성 또는 모델 기반으로 자동 생성된 Form 객체를 사용해서 작성

- POST 방식으로 요청 시
    - GET 방식 요청으로 응답받은 입력 페이지에서 값을 입력한 후 SUBMIT 버튼을 클릭하면 요청되는 방식
    - POST 방식으로 요청 시 입력받은 값을 Form 객체에 바인딩하고 유효성 검사를 진행
    - 유효성 검사 결과에 따라 다르게 동작
        - 유효성 검사 성공 시: 입력값을 DB에 추가하고 success_url에 지정된 URL로 이동
        - 유효성 검사 실패 시: error message와 함께 입력 페이지로 이동

```python
# urls.py
from django.urls import path
from django.views.generic import *
from .models import Book

app_name ='book'

urlpatterns = [
    path('create/', CreateView.as_view(model=Book, fields='__all__'), name='create'),
    ...
]

```

```html
<!-- book/templates/book/book_form.html -->
{% extends 'layout.html' %}
{% block title %} Book 등록 {% endblock %}
{% block content %}
  <h1>Book 등록</h1>
  <form action="" method="POST">
    {% csrf_token %}
    <table>{{ form.as_table }}</table>
    <input type="submit" value="등록" />
  </form>
{% endblock %}

<!-- book.templates/book/book_list.html -->
<a href="{% url 'book:create' %}">[새 책 등록]</a>

```

### UpdateView

- 데이터를 수정하는 기능이 구현된 Generic View로 기본 속성은 CreateView와 동일

- GET 방식으로 요청 시
    - path 변수로 전달된 Primary Key에 해당하는 모델 인스턴스를 추출하여 Form 객체에 바인딩한 후 template_name 속성에 지정된 템플릿 또는 `앱이름/모델명소문자_form.html` 템플릿을 응답하면서 컨텍스트로 전달
    - 응답된 템플릿의 입력 폼에는 바인딩된 값들이 초기값을 출력됨

- POST 방식으로 요청 시
    - GET 방식 요청으로 응답받은 입력 페이지에서 값을 수정한후 SUBMIT 버튼을 클릭하면 요청되는 방식
    - POST 방식으로 요청 시 입력받은 값을 Form 객체에 바인딩하고 유효성 검사를 진행
    - 유효성 검사 결과에 따라 다르게 동작
        - 유효성 검사 성공 시: 수정된 내용을 DB에 반영하고 success_url에 지정된 URL로 이동
        - 유효성 검사 실패 시: error message와 함께 입력 페이지로 이동

```python
# urls.py
from django.urls import path
from django.views.generic import *
from .models import Book

app_name ='book'

urlpatterns = [
    path('update/<pk>/', UpdateView.as_view(model=Book, fields='__all__'), name='update'),
    ...
]

```

```html
<!-- book/templates/book/book_detail.html -->
{% extends "layout.html" %}
{% block title %} Book 상세보기 {% endblock %}
{% block content %}
    <h1>{{book.title}}</h1>
    제목: {{book.title}} <br>
    저자: {{book.author}} <br>
    출판사: {{book.publisher}} <br>
    <a href="{% url 'book:update' book.id %}">[수정하기]</a>
    <a href="{% url 'book:delete' book.id %}">[삭제하기]</a> 
{% endblock %}

```

### DeleteView

- 데이터 삭제 기능이 구현된 Generic View
    - model: 필수 속성으로 모델명 지정
    - success_url: 필수 속성으로 삭제 작업 후 이동할 URL 지정
    - template_name: 삭제 요청을 확인하는 템플릿 지정
    - 기본 템플릿명: `앱이름/모델명소문자_confirm_delete.html`

- GET 방식으로 요청 시
    - 삭제 작업을 진행할 것인지 여부를 확인하는 `앱이름/모델명소문자_confirm_delete.html` 템플릿을 응답

- POST 방식으로 요청 시
    - 삭제 작업을 진행할 것인지 여부를 확인하는 `앱이름/모델명소문자_confirm_delete.html` 템플릿에서 `[삭제 확인]`을 선택하면 요청되는 방식
    - path 변수로 전달된 Primary Key를 가진 모델 인스턴스를 삭제한 후 success_url 속성에 지정된 페이지로 이동

```python
from django.urls import path, reverse, reverse_lazy
from django.views.generic import *
from .models import Book

app_name ='book'

urlpatterns = [
    # 오류 발생
    # path('delete/<pk>/', DeleteView.as_view(model=Book, success_url=reverse('book:list')), name='delete'),

    # 오류 해결
    path('delete/<pk>/', DeleteView.as_view(model=Book, success_url=reverse_lazy('book:list')), name='delete'),
    ...
]

```

```html
<!-- book/templates/book/book_confirm_delete.html -->
{% extends "layout.html" %}
{% block title %} Post 삭제 {% endblock %}
{% block content %}
    <h1>Book 삭제</h1>
    "{{book}}"을 정말로 삭제하시겠습니까?
    <form action="" method="POST">
        {% csrf_token %}
        <input type="submit" value="네, 삭제합니다">
    </form>
    <a href="{% url 'book:list'%}">아니오, 취소합니다</a>
{% endblock %}

```
