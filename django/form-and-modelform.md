## Index

---

- [Django Form](#django-form)
- [Django ModelForm](#django-modelform)
- [Handling HTTP Requests](#handling-http-requests)
- [View Decorators](#view-decorators)
- [Custom Form Layout](#custom-form-layout)

## Django Form

---

### 참고 링크

- [Django Github - Forms](https://github.com/django/django/blob/main/django/forms/models.py)
- [Django Docs - The Forms API](https://docs.djangoproject.com/en/4.1/ref/forms/api/#django.forms.Form.errors)
- [Django Docs - Form fields (linked to ChoiceField)](https://docs.djangoproject.com/en/4.1/ref/forms/fields/#)
- [Django Docs - Widgets (linked to Selector and checkbox widgets)](https://docs.djangoproject.com/en/4.1/ref/forms/widgets/#selector-and-checkbox-widgets)
- [Django Docs - Coding Style](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/)
- [Django Docs - Working with forms (linked to Rendering fields manually](https://docs.djangoproject.com/en/4.1/topics/forms/#rendering-fields-manually)
- [django-bootstrap-v5 Docs](https://django-bootstrap-v5.readthedocs.io/en/latest/)

### Django Form

- HTML `<input>` 태그를 직접 사용하지 않고 **Django Form**이라는 프레임워크를 통해 사용자로부터 데이터를 받자
- WHY?
    - **유효성 검증**
        - 사용자의 요청 중에는 비정상적인 혹은 악의적인 요청이 있음
        - 사용자가 입력한 데이터가 우리가 원하는 데이터 형식에 맞는지 유효성 검증이 필요
        - 이러한 유효성 검증은 많은 부가적인 것들을 고려해서 구현해야 하는데, 이는 개발 생산성을 늦추고, 쉽지도 않음
        - Django Form은 이 과정에서 과중한 작업과 반복적 코드를 줄여줌으로써 훨씬 쉽게 유효성 검증을 진행할 수 있도록 만듬
    - 유효성 검증 외에도 빠르게 form 작업을 수행할 수 있음

### Form에 대한 Django의 역할

- Form은 Django의 **유효성 검사 도구 중 하나로 외부의 악의적 공격 및 데이터 손상에 대한 중요한 방어 수단**
- Django는 Form과 관련한 유효성 검사를 **단순화하고 자동화**할 수 있는 기능을 제공하여, 개발자가 직접 작성하는 코드보다 더 안전하고 빠르게 수행하는 코드를 작성할 수 있음
    - **개발자가 필요한 핵심 부분만 집중_**할 수 있도록 돕는 프레임워크의 특성

- Django는 Form과 관련한 작업의 3가지 부분을 처리해줌
    1. 렌더링을 위한 데이터 준비 및 재구성
    2. 데이터에 대한 HTML forms 생성
    3. 클라이언트로부터 받은 데이터 수신 및 처리

### Django Form Class

- Form Class
- Django form 관리 시스템의 핵심

### Form Class 선언

- 상속을 통해 선언
    - forms 라이브러리의 Form 클래스를 상속받음
    - Model Class를 models 라이브러리의 Model 클래스를 상속받는 것과 유사

- `forms.py`

    - 앱 폴더에 생성 후 form class 선언
    <img width="616" alt="dj_61" src="https://user-images.githubusercontent.com/86648892/189478360-f3ae2e67-30be-4459-af7e-87f1b885b3de.png">

    - 모델에 관련없이
        - 사용자로부터 무엇을 받을 것인지, 어떤 타입으로 받을지 고려하여 작성
    - form에는 model field와 달리 TextField가 존재하지 않음
    - Form Class를 forms.py에 작성하는 것은 규약은 아니다
        - 파일 이름이 달라도 되고, models.py나 다른 어디에도 작성이 가능하지만 관행적으로 forms.py에 작성하는 것을 권장
    - form class에서 `Charfield()`의 `max_length`는 models와 다르게 필수 인자는 아님
        - 그냥 편리하게 길이 제한을 걸려고 쓰는 용도

### Form Rendering options

- html 파일에서 렌더링 시 views의 함수의 context에 담아 넘겨받은 form을
    - `{{ form.as_p }}` 와 같이 접근하여 사용

- `<label>` & `<input>` 쌍에 대한 3가지 출력 옵션
    1. `as_p()`
        - 각 필드가 단락(`<p>` 태그)으로 감싸져서 렌더링
    2. `as_ul()`
        - 각 필드가 목록 항목(`<li>` 태그)으로 감싸져서 렌더링
        - `<ul>` 태그는 직접 작성해야함
    3. `as_table()`
        - 각 필드가 테이블(`<tr>` 태그) 행으로 감싸져서 렌더링

- 주로 `as_p()` 를 많이 사용함

### Form fields & Widgets

- 그런데 `{{ form }}` 과 같이 한 덩어리로 묶어서 렌더링하면 안에 세부적인 처리를 어떻게 할 것인가에 대한 의문이 생김
- Django의 2가지 HTML input 요소 표현
    1. **Form fields**
        - ex) `forms.CharField()`
        - **입력에 대한 유효성 검사 로직을 처리**
        - 템플릿에서 직접 사용됨
    2. **Widgets**
        - ex) `forms.CharField(widget=forms.Textarea)`
        - 웹 페이지의 **HTML input 요소 렌더링을 담당**
        - 단순히 HTML 렌더링, 출력을 처리하는 것이며 유효성 검증과 아무런 관계가 없음
            - “웹 페이지에서 input element의 단순 raw한 렌더링만을 처리하는 것일 뿐”
        - Widgets은 반드시 form fields에 할당됨
        - form fields의 core field arguments 확인
    - 쉽게 말해 Form fields는 사용자의 입력이 어떠한 입력값이어야하는지 정의하고, 유효한 입력값인지 판단하기 위함이며, Widgets는 input값의 출력을 어떻게 해줄지 세부적으로 조정하기 위함

### 드랍다운을 만들어보자

```python
# articles/forms.py

from django import forms

class ArticleForm(forms.Form):
    NATION_A = 'kr'
    NATION_B = 'ch'
    NATION_C = 'jp'
    NATION_CHOICES = [
        (NATION_A, '한국'),
        (NATION_B, '중국'),
        (NATION_C, '일본'),
    ]
    title = forms.CharField(max_length=10)
    content = forms.CharField(widget=forms.Textarea)
    nation = forms.ChoiceField(choices=NATION_CHOICES)

# NATION_CHOICES = [ ('kr', '한국'), ('ch', '중국'), ('jp', '일본'), ]
# 이렇게 선언하는 것은 동작은 같지만
# Django Style Guide에 어긋난다
# ChoiceField는 <select> 태그, choices의 인자들은 <select> 태그 안의 <option>들로 들어간다
```

- [Django Docs - Widgets (linked to Selector and checkbox widgets)](https://docs.djangoproject.com/en/4.1/ref/forms/widgets/#selector-and-checkbox-widgets)
- [Django Docs - Coding Style](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/)

## Django ModelForm

---

### ModelForm Class

- Model을 기반으로 한 Form Class
- Model을 통해 Form Class를 만들 수 있는 helper class
- 기반으로 하는 모델의 필드를 따로 재정의하지 않아도 됨
- ModelForm은 Form과 똑같은 방식으로 view 함수에서 사용

## ModelForm 선언

- 상속을 통해 선언
    - forms 라이브러리에서 파생된 ModelForm 클래스 상속
    - 정의한 ModelForm 클래스 안에 inner class인 Meta 클래스 선언
    - 어떤 모델을 기반으로 form을 작성할 것인지에 대한 정보를 Meta 클래스에 지정
    <img width="527" alt="dj_62" src="https://user-images.githubusercontent.com/86648892/189478363-35f7863f-a5f7-405b-b9ce-e233243ad3ab.png">

### Meta Class

- ModelForm의 정보를 작성하는 곳
    - model, fields라는 변수명은 정해져 있음

- `model = Article`
    - 참조할 모델
        - 인스턴스가 아닌 참조값
    - 참조하는 모델에 정의된 field 정보를 Form에 적용함
        - input값을 받는 field들
- 어떤 모델을 기반으로 form을 작성할 것인지에 대해 inner class인 Meta 클래스에 지정

- `model = Article`
    - 참조값을 줌 (인스턴스가 아님)
    - 참조값과 반환값

- `fields = '__all__'`
    - 모델의 **입력받아야 할** 모든 필드를 포함
    - 필드 중 사용자가 입력하지 않는 필드는 포함하지 않음
    - ex) `auto_now_add = True` 인 `created_at` 이나 `auto_add = True` 인 `updated_at` 등
    <img width="1086" alt="dj_63" src="https://user-images.githubusercontent.com/86648892/189478364-db5106b4-8175-44b9-a04a-bae25345d820.png">

    - `exclude` 속성을 사용하여 모델에서 포함하지 않을 필드를 지정할 수 있음
        - fields와 exclude를 함께 작성해도 되나 권장하지 않음

### [참고] Meta Data?

**데이터를 표현하기 위한 데이터**

### [참고] 참조값과 반환값

- 언제 참조값을 사용할까?
    - 함수를 호출하지 않고 함수 자체를 그대로 전달하여, 다른 함수에서 “필요한 시점"에 호출하는 경우
    - view 함수의 참조값을 그대로 넘김으로써, path 함수가 내부적으로 해당 view 함수를 “필요한 시점"에 사용하기 위해서
    <img width="756" alt="dj_64" src="https://user-images.githubusercontent.com/86648892/189478365-9bee80ec-525a-4a6e-b7f1-7b5c870ec329.png">

    - 클래스도 마찬가지
        - Article이라는 클래스를 “호출하지 않고(==model을 인스턴스로 만들지 않고)” 작성하는 이유는 ArticleForm이 해당 클래스를 필요한 시점에 사용하기 위함
        - 더불어 이 경우에는 인스턴스가 필요한 것이 아닌, 실제 Article 모델의 참조값을 통해 해당 클래스의 필드나 속성 등을 내부적으로 참조하기 위한 이유도 있음

## ModelForm with view functions (CRUD)

---

### 1. CREATE

<img width="679" alt="dj_65" src="https://user-images.githubusercontent.com/86648892/189478366-3205d78b-db05-486e-890d-40fbf7447101.png">

- `data=request.POST`
    - `BaseModelForm()`의 첫번째 인자는 data임
    - request에 담긴 데이터를 바탕으로 ArticleForm 인스턴스 생성
- 유효성 검사를 통과하면
    - `article = form.save()`
        - ModelForm의 `save()` 는 input 값들을 채운 해당 모델 instance를 반환
        - 상세화면 페이지로 넘어갈 때 해당 모델 인스턴스를 넘겨줘야하므로 article에 할당
    - 이후 상세화면으로 리다이렉트
- 통과하지 못하면
    - 작성 페이지로 리다이렉트

### `is_valid()`

- 유효성 검사를 실행하고, 데이터가 유효한지 여부를 boolean으로 반환
    - `max_length` 등과 같이 모델에 설정해둔 유효성 기준에 따라 판단
    - CharField()에 숫자를 넣으면 안되는것과 같은 기본적인 내장 유효성 검사 외에 추가적으로 유효성 검사 기준 인자를 잘 설계하는 것이 중요
- 데이터 유효성 검사를 보장하기 위한 많은 테스트에 대해 Django는 `is_valid()` 를 제공하여 개발자의 편의를 도움
- `BaseForm()` 에 정의되어 있음

### `is_valid()`의 결과가 False라면?

- `is_valid()` 의 반환 값이 False인 경우 form 인스턴스의 errors 속성에 값이 저장됨
    - 기본적으로는 빈 값
        - 유효성 검증 실패 시 실패한 원인이 딕셔너리 형태로 저장됨
        - `forms.py`에서 정의한 `error_messages` 나 기본적으로 정의된 에러 메세지를 포함한 페이지를 렌더링해줌
    - [참고] 공백과 빈 값은 다르다
        - 빈 값
        - “이 입력란을 작성하세요”
            - Django와 관련없음
            - HTML과 관련있음
                - input 태그의 required라는 속성에 의해 Django에 요청이 가기 전에 이미 막힘
                - 개발자 도구를 통해 required를 지우고 보내면 Django에서 유효성 검사 진행 가능
        - 공백
        - Django에서 에러를 주는 경우

<img width="872" alt="dj_66" src="https://user-images.githubusercontent.com/86648892/189478368-ebc39828-b613-40ad-872c-a8fbd5a9562c.png">

### `form.save()`

- `return self.instance`
- form 인스턴스에 바인딩된 데이터를 통해 데이터베이스 객체를 만들고 저장
- ModelForm의 하위 클래스는 키워드 인자 `instance` 여부를 통해 CREATE, UPDATE 여부를 결정
    - 제공되지 않는 경우 `save()` 는 지정된 모델의 새 인스턴스를 만듬 (CREATE)
    - 제공된 경우 `save()` 는 해당 인스턴스를 수정 (UPDATE)

<img width="478" alt="dj_67" src="https://user-images.githubusercontent.com/86648892/189478369-2bdd9a37-01ab-43fe-9994-a699bb99a01f.png">

### 2. UPDATE

- ModelForm의 인자 instance는 수정 대상이 되는 객체(기존 객체)를 지정
    1. `request.POST`
        - 사용자가 form을 통해 전송한 데이터 (새로운 데이터)
    2. `instance`
        - 수정이 되는 대상
- CREATE에서는
    - `form = ArticleForm(request.POST)`
        - Create 버튼을 통해 들어온 POST 요청에 들어있는 입력 데이터들을 바탕으로 ArticleForm의 모델인 Article의 인스턴스를 반환해 form에 할당
- UPDATE에서는
    - `article = Article.objects.get(pk=pk)`
        - 일단 수정할 인스턴스를 들고온 뒤
    - `form = ArticleForm(request.POST, instance=article)`
        - Update 버튼을 통해 들어온 POST 요청에 들어있는 입력 데이터들을 바탕으로, 위에 할당한 article이라는 인스턴스를 수정한 결과를 form에 할당

<img width="802" alt="dj_68" src="https://user-images.githubusercontent.com/86648892/189478370-050edb5b-0b0a-43a2-8429-11b7e24494c2.png">

<img width="827" alt="dj_69" src="https://user-images.githubusercontent.com/86648892/189478372-4e51086b-53c2-46c5-af64-a606d5be3476.png">

<img width="821" alt="dj_70" src="https://user-images.githubusercontent.com/86648892/189478374-ef4fe4fd-9010-448e-ae80-856289c419a4.png">

### [참고] ModelForm의 인자 구조

<img width="1113" alt="dj_71" src="https://user-images.githubusercontent.com/86648892/189478375-b9809196-81af-43da-a0d5-e99c0aacfedf.png">

### Form & ModelForm 정리

- Form과 ModelForm은 모델을 기반으로 안하냐의 차이
- 누가 더 좋은 것이 아니라 역할이 다른 것
    - **사용자로부터 받는 데이터가 DB에 영향을 미치는가 여부**
    - **로그인은 사용자의 데이터를 받아 인증 과정에서만 사용 후 별도로 DB에 저장하지 않으므로 Form**
    - **회원가입으로 유저 데이터를 추가하거나, 게시판 글 작성처럼 아티클 데이터를 추가하는 경우 ModelForm**

### Form

- 사용자의 입력을 필요로 하며 직접 입력 데이터가 DB 저장에 사용되지 않거나 일부 데이터만 사용될 때
- ex) 로그인
- 사용자의 데이터를 받아 인증 과정에서만 사용 후 별도로 DB에 저장하지 않음

### ModelForm

- 사용자의 입력을 필요로 하며 입력 받은 것을 그대로 DB 필드에 맞춰 저장할 때
- 데이터의 유효성 검사가 끝나면 데이터를 각각 어떤 레코드에 매핑해야할지 이미 알고있기 때문에 곧바로 `save()` 호출이 가능

## Handling HTTP requests

---

- HTTP requests 처리에 따른 view 함수 구조 변화를 구현해보자
    - 하나의 view 함수에서 HTTP request method에 따라 로직이 분리되도록 변경
- new-create, edit-update의 view 함수 역할에는 공동의 목적과 차이점이 있음
    - 공통점
        - new-create는 “생성”
        - edit-update는 “수정”
    - 차이점
        - new, edit는 페이지 렌더링 (GET)
        - create, update는 DB 조작 (POST)

### 1. CREATE

<img width="789" alt="dj_72" src="https://user-images.githubusercontent.com/86648892/189478376-5cd263c9-dc5e-47da-a179-3dcaf38b77f2.png">

- `views.py` 의 new 함수와 create 함수를 create 함수로 통합
    - 불필요해진 new 함수의 url path를 삭제
    - new.html의 이름을 create.html로 변경 후 url path를 변경된 이름으로 수정
    - index.html의 새 게시글 생성 페이지를 렌더링하는 버튼의 링크를 articles의 create url path로 변경
    - 기존 new 함수의 `return render(request, 'articles/new.html', context)` 를 `return render(request, 'articles/create.html', context)` 로 변경
- context의 들여쓰기 위치 주의
    - `if form.is_valid()` 가 False로 평가받았을 때 에러 정보가 담긴 form 인스턴스가 context로 넘어갈 수 있도록 설정
- 분기처리를 할 때 왜 POST를 if의 조건으로 쓸까?
    - DB 조작 관련 코드를 POST일때만 수행한다고 설정할 수 있음
    - if에 GET을 쓰고 else에서 DB 조작 코드를 쓴다면
    - POST외에 다른 request method에 대해서도 DB 조작이 가능한 상태가 되어버림

### 2. UPDATE

CREATE와 동일

<img width="747" alt="dj_73" src="https://user-images.githubusercontent.com/86648892/189478377-cf75d70b-25c8-4aeb-a2be-a9126248b080.png">

### 3. DELETE

POST 요청에 대해서만 삭제가 가능하도록 수정

<img width="849" alt="dj_74" src="https://user-images.githubusercontent.com/86648892/189478379-b35ac0fa-8d13-439b-a6fa-5f70ef8144e8.png">

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

### 정리

- Django Form Class
    - Django 프로젝트의 주요 유효성 검사 도구
    - 공격 및 데이터 손상에 대한 중요한 방어 수단
    - 유효성 검사에 대해 개발자에게 강력한 편의를 제공
- View 함수 구조 변화
    - HTTP requests 처리에 따른 구조 변화
