## Index

---

- [View Decorators](#view-decorators)
- [Custom Form Layout](#custom-form-layout)

## View Decorators

---

View decorators를 활용하여 view 함수를 단단하게 만들어보자

### Decorator

- 기존에 작성된 함수에 기능을 추가하고싶을 때
- 해당 함수를 수정하지 않고 기능을 추가해주는 함수
- 데코레이터 동작 예시

<img width="901" alt="dj_75" src="https://user-images.githubusercontent.com/86648892/189478381-c459b80f-0b8e-41e9-8e8a-590283a86a15.png">

### Allowed HTTP methods

- Django는 다양한 HTTP 기능을 지원하기 위해 view 함수에 적용할 수 있는 데코레이터 제공
    - `from django.views.decorators.http`
        - `import require_http_methods`
            - `@require_http_methods` 시 직접 뒤에 붙인 HTTP request method일 때만 허용
            - ex) `@require_http_methods(['GET', 'POST'])`
        - `import require_safe`
            - `@require_safe` 시 GET 요청일 때만 허용
        - `import require_POST`
            - `@require_POST` 시 POST 요청일 때만 허용
- 일치하지 않는 메서드 요청이라면 **405 Method Not Allowed**를 반환
- `405 Method Not Allowed`: 요청 방법이 서버에게 전달되었으나 사용 불가능한 상태

### 적용

- index
    - 단순 전체 게시글 데이터 조회 (GET)
    - `@require_safe`
- create
    - 새 게시글 생성 페이지 렌더링 요청 (GET), 작성 후 새 게시글 생성 요청 (POST)
    - `@require_http_methods(['GET', 'POST'])`
- update
    - 게시글 수정 페이지 렌더링 요청 (GET), 작성 후 수정된 게시글 인스턴스 저장 요청 (POST)
    - `@require_http_methods(['GET', 'POST'])`
- delete
    - 게시글 DB에서 삭제 요청 (POST)
    - `@require_POST`
    - url로 delete를 시도하면 405 http status code 반환
    <img width="1013" alt="dj_76" src="https://user-images.githubusercontent.com/86648892/189478383-e4ab8b97-9751-4c7d-95a9-98e053d82c35.png">
    - `@require_POST` 작성했으므로 기존에 있던 `if request.method == 'POST':` 필요없음

## Custom Form Layout

---

### 참고 링크

- **subject는 컬럼의 이름**
- [Django Docs - Working with forms (linked to Rendering fields manually](https://docs.djangoproject.com/en/4.1/topics/forms/#rendering-fields-manually)
- [django-bootstrap-v5 Docs](https://django-bootstrap-v5.readthedocs.io/en/latest/)

### 코드 예시 (create.html)

```html
{% extends 'base.html' %} {% load bootstrap5 %} {% block content %}
<h1>CREATE</h1>
<form action="{% url 'articles:create' %}" method="POST">
  {% csrf_token %} {{ form.as_p }}
  <input type="submit" />
</form>
<hr />
<a href="{% url 'articles:index' %}">뒤로가기</a>

<hr />

<h2>수동으로 Form 작성</h2>
<form action="#">
  <div>{{ form.title.errors }} {{ form.title.label_tag }} {{ form.title }}</div>
  <div>
    {{ form.content.errors }} {{ form.content.label_tag }} {{ form.content }}
  </div>
</form>

<hr />

<h2>Looping over the form’s fields</h2>
<form action="#">
  {% for field in form %} {{ field.errors }} {{ field.label_tag }} {{ field }}
  {% endfor %}
</form>

<hr />

<h2>bootstrap v5 라이브러리 사용하기</h2>
<form action="#">
  {% bootstrap_form form %} {% buttons %}
  <button type="submit" class="btn btn-primary">Submit</button>
  {% endbuttons %}
</form>
{% endblock content %}
```

<img width="1318" alt="dj_77" src="https://user-images.githubusercontent.com/86648892/189478385-284b3ec1-89b7-49de-8dbd-e9d5c3ccedf5.png">

<img width="1321" alt="dj_78" src="https://user-images.githubusercontent.com/86648892/189478387-b92345d6-80bb-4462-8095-39eee6e5325c.png">

<img width="1319" alt="dj_79" src="https://user-images.githubusercontent.com/86648892/189478388-6f300af7-185a-454a-96e0-5f6df1fcea36.png">

<img width="1325" alt="dj_80" src="https://user-images.githubusercontent.com/86648892/189478389-2e88b8bf-7d96-4ae6-a7ea-e4ab25cf83eb.png">
