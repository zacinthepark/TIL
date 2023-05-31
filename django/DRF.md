# Django REST Framework and Serializer

- REST API
- Response JSON
- Django REST framework - Single Model
- Django REST framework - N:1 Relation

---


# Response JSON

- JSON 형태로의 서버 응답 변화
  - 페이지 반환이 아닌 JSON 데이터 반환
- 다양한 방법으로 JSON을 응답

### 서버가 응답하는 것

- 서버는 사용자에게 페이지(html)만 응답하는 것이 아니라
  - 다양한 데이터 타입을 응답할 수 있음
    - html을 응답하는 서버를 JSON 데이터를 응답하는 서버로 변환
      - 그렇다면 사용자에게 보여질 화면은 누가 구성?
        - Front-end Framework가 담당

<img width="853" alt="dj_248" src="https://user-images.githubusercontent.com/86648892/212551485-b0094561-b83f-499f-9f99-08eca9dd5a80.png">

<img width="843" alt="dj_249" src="https://user-images.githubusercontent.com/86648892/212551482-ba6add9f-95ab-435a-a0b1-f6ab8867e56d.png">

---

# Response

- 다양한 방법으로 JSON 데이터 응답해보기
  1. HTML 응답
  2. `JsonResponse()` 를 사용한 JSON 응답
  3. **Django Serializer**를 사용한 JSON 응답
  4. **Django REST framework**를 사용한 JSON 응답

## ‘Content-Type’ entity header

- 리소스의 media type(MIME type, content type)을 나타내기 위해 사용됨
- 응답 내에 있는 컨텐츠의 컨텐츠 유형이 실제로 무엇인지 클라이언트에게 알려줌

## Serialization이란?

- “직렬화”
- 데이터 구조나 객체 상태를 동일 혹은 다른 컴퓨터 환경에 저장하고
  - 나중에 재구성할 수 있는 포맷으로 변환하는 과정
    - 즉, 어떠한 언어나 환경에서도 나중에 쉽게 재구성할 수 있는 포맷인 serialized data로 변환하는 과정
      - serialized data란 가공된 데이터로
        - 다른 포맷으로 쉽게 재구성할 수 있는 파일이라는 특징
          - 변환 포맷은 대표적으로 json, xml, yaml이 있으면 json이 가장 보편적으로 쓰임
- Django의 `serialize()` 는 QuerySet 객체 및 Model Instance와 같은 복잡한 데이터를
  - JSON, XML 등의 유형으로 쉽게 변환할 수 있는 Python 데이터 타입으로 만들어줌

<img width="850" alt="dj_250" src="https://user-images.githubusercontent.com/86648892/212551481-fec1e18f-2cc6-4dce-ba28-3b9522727772.png">

<img width="832" alt="dj_251" src="https://user-images.githubusercontent.com/86648892/212551480-75ef0e69-dbac-4f62-8622-3c7ed077041e.png">

## 1. HTML 응답

```python
def article_html(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/article.html', context)
```

```html
<body>
  <h1>Article List</h1>
  <hr>
  <p>
    {% for article in articles %}
      <h2>{{ article.pk }}번 글. {{ article.title }}</h2>
      <p>{{ article.content }}</p>
      <hr>
    {% endfor %}
  </p>
</body>
```

<img width="634" alt="dj_252" src="https://user-images.githubusercontent.com/86648892/212551479-20330f29-bfd9-4587-9d87-e98e1aab0046.png">

## 2. JsonResponse()를 사용한 JSON 응답

- Django가 기본적으로 제공하는 JsonResponse 객체를 활용하여 Python 데이터 타입을 손쉽게 JSON으로 변환하여 응답 가능
- 컬럼을 일일이 정의하여 딕셔너리 생성
- `JsponResponse()`
  - JSON-encoded response를 만드는 클래스
  - `safe` parameter
    - 기본값은 True
    - `JsonResponse()` 에 들어오는 인자가 dictionary가 아니면 `safe=False` 로 설정해야함
      - False로 설정 시 모든 타입의 객체를 serialization 할 수 있음
        - 그렇지 않으면 dictionary 인스턴스만 허용
- 출력 확인을 위해 Chrome 확장 프로그램에 JSON Viewer 설치

```python
# 직접 JSON 응답 객체 작성 (JsonResponse())

from django.http.response import JsonResponse

def article_json_1(request):
    articles = Article.objects.all()
    articles_json = []
    # article 데이터 하나씩 딕셔너리 형태로 리스트에 넣음
    for article in articles:
        articles_json.append(
            {
                'id': article.pk,
                'title': article.title,
                'content': article.content,
                'created_at': article.created_at,
                'updated_at': article.updated_at,
            }
        )
    # 만든 딕셔너리 리스트를 JSON으로 변환
    return JsonResponse(articles_json, safe=False)
```

<img width="583" alt="dj_253" src="https://user-images.githubusercontent.com/86648892/212551477-5f824975-dfc4-477d-bad8-8487fc7a28d7.png">

## 3. Django Serializer를 사용한 JSON 응답

- Django 내장 `HttpResponse()` 를 활용한 JSON 응답
- 모델 구조를 기반으로 JSON 데이터를 생성
  - JSON의 모든 필드를 다 작성할 필요 없음

```python
# Django 내장 HttpResponse()와 serializers 활용

from django.http.response import HttpResponse

def article_json_2(request):
    articles = Article.objects.all()
    data = serializers.serialize('json', articles)
    return HttpResponse(data, content_type='application/json')
```

<img width="699" alt="dj_254" src="https://user-images.githubusercontent.com/86648892/212551476-83ac2af1-e096-4d53-910e-c8695ef500ac.png">

## 4. Django REST framework를 사용한 JSON 응답

### Django REST framework (DRF)

- Django에서 Restful API 서버를 쉽게 구축할 수 있도록 도와주는 오픈소스 라이브러리
- Web API 구축을 위한 강력한 toolkit을 제공
- REST framework를 작성하기 위한 여러 기능을 제공
- DRF의 serializer는 Django의 Form 및 ModelForm 클래스와 매우 유사하게 작동
  - DRF에서 일부러 구성을 맞춰둔 것
    - ModelForm과 동일한 일을 하는 것은 아님
      - `serialize()`를 담당
- [https://www.django-rest-framework.org/](https://www.django-rest-framework.org/)

```python
# settings.py

INSTALLED_APPS = [
    'articles',
    'rest_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

```python
# articles/serializers.py

from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'
```

```python
# articles/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response

# @api_view(['GET'])
@api_view()
def article_json_3(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)
```

<img width="583" alt="dj_255" src="https://user-images.githubusercontent.com/86648892/212551472-813a56ac-3f27-4fd9-b949-0ea82aa34513.png">

- DRF가 자체적으로 JSON 데이터를 담은 DRF 내장 템플릿을 반환
  - `Content-Type: text/html;`
  - 브라우저 상에서만 그런 것이고, 실제 코드에서 프로그래밍적으로 소통할 때는 JSON을 반환

### 직접 requests 라이브러리를 사용하여 JSON 응답 받아보기

- requests 라이브러리 설치
  - `pip install requests`
    - Terminal 화면을 나누어 Django 서버를 켜놓고 파일 실행

```python
# gogo.py

# 요청보낼 때 requests 라이브러리 사용
import requests
from pprint import pprint

response = requests.get('http://127.0.0.1:8000/api/v1/json-3/') # requests가 GET Method로 해당 url에 요청을 보냄
result = response.json()                                        # 응답받은 것을 JSON으로 변환

pprint(result)
# pprint(result[0])
# pprint(result[0].get('title'))
```

<img width="674" alt="dj_256" src="https://user-images.githubusercontent.com/86648892/212551470-938710ff-6204-4371-83eb-9fec1a05b9a0.png">

---

# Django REST framework (Single Model)

- 단일 모델의 data를 Serialization하여 JSON으로 변환하는 방법 학습
- DRF를 활용하여 JSON 데이터를 응답하는 Django 서버 구축

## ModelSerializer

- ModelSerializer 클래스는 모델 필드에 해당하는 필드가 있는 Serializer 클래스를 자동으로 만들 수 있는 shortcut을 제공
  1. Model 정보에 맞춰 자동으로 필드를 생성
  2. serializer에 대한 유효성 검사기를 자동으로 생성
     - 이름도 `is_valid()` 로 같음
     - serialize하기 전 유효성 검사
  3. `.create()` 및 `.update()` 의 간단한 기본 구현이 포함됨
     - 이후 수정이나 생성을 할 때 쓰는 메서드를 기본 구현에 포함하고 있음
- 쿼리셋이나 모델 인스턴스 객체를 넣어주기만 하면 알아서 그 필드에 맞춰서 JSON 데이터를 key-value에 맞춰 생성
- 최대한 Django의 ModelForm과 비슷하게 구현해놓음

### 단일 모델 인스턴스 serialize

- Model Instance 객체 serialize
  - `article = Article.objects.get(pk=1)`
  - `serializer = ArticleListSerializer(article)`
  - `serializer.data`

<img width="624" alt="dj_257" src="https://user-images.githubusercontent.com/86648892/212551468-1508ad08-db57-4cbb-ab78-269e98dec476.png">

### QuerySet 객체 serialize

- QuerySet 객체 serialize
  - 단일 객체 인스턴스 대신 QuerySet 또는 객체 목록을 serialize하려면
    - `many=True` 옵션이 필요함

<img width="774" alt="dj_258" src="https://user-images.githubusercontent.com/86648892/212551467-d3c58515-cc8f-4b8d-a8c2-e6e93c4b40ba.png">

<img width="773" alt="dj_259" src="https://user-images.githubusercontent.com/86648892/212551466-82f16d27-9d5e-45a7-b8f4-67f4f8caf366.png">

---

# Build RESTful API (Article and Comment)

<img width="838" alt="dj_260" src="https://user-images.githubusercontent.com/86648892/212551464-5618e163-34c3-407d-b032-96d68e00749f.png">

- URL은 2개이고, 기능은 7개인 서버를 구현
  - URL이 2개인데 기능이 7개가 가능한 이유는 똑같은 URL이지만 Http Methods로 행동을 정의할 수 있기에 가능

## `api_view` decorator

- DRF에서 `api_view` 데코레이터 작성은 필수
- DRF view 함수가 응답해야하는 HTTP 메서드 목록을 받음
- 기본적으로 GET 메서드만 허용되며 다른 메서드 요청에 대해서는
  - 405 Method Not Allowed로 응답

## raising an exception on invalid data

- serializer의 데이터에 대한 유효성 검사 실행 시 줄 수 있는 옵션
  - 유효하지 않은 데이터에 대해 예외 발생시키기
    - `is_valid()` 는 유효성 검사 오류가 있는 경우 ValidationError 예외를 발생시키는 선택적 `raise_exception` 인자를 사용할 수 있음
      - DRF에서 제공하는 기본 예외 처리기에 의해 자동으로 처리되며 기본적으로 HTTP 400 응답을 반환

## passing additional attributes to `.save()`

- `save()` 메서드는 특정 Serializer 인스턴스를 저장하는 과정에서 추가적인 데이터를 받을 수 있음
- 아래 사진은 `CommentSerializer` 를 통해 Serialize되는 과정에서 Parameter로 넘어온 `article_pk` 에 해당하는 article 객체를 추가적인 데이터를 넘겨 저장

<img width="677" alt="dj_261" src="https://user-images.githubusercontent.com/86648892/212551775-b623c2e4-81a9-4fcf-88a5-e9450185ee1f.png">

## `read_only_fields` 설정

- `read_only_fields` 를 사용해 외래키 필드를 읽기 전용 필드로 설정
- 읽기 전용 필드는 데이터를 전송하는 시점에
  - 해당 필드를 유효성 검사에서 제외시키고 데이터 조회 시에는 출력하도록 함

<img width="593" alt="dj_262" src="https://user-images.githubusercontent.com/86648892/212551774-480fe870-7d69-403a-ad31-0955826d466d.png">

---

# Code Snippets

### `articles/models.py`

```python
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

### `articles/serializers.py`

```python
from rest_framework import serializers  # DRF 패키지에서 serializers 기능을 차용
from .models import Article, Comment    # ModelSerializer에 사용할 모델 import

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',) # 최종적으로 조회는 되나, 유효성 검사에서 제외됨

# 게시글의 목록(게시글들의 QuerySet)을 serialize해서 나눌 것이기에 이름을 ArticleListSerializer로 명명
class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article                         # 해당 모델 정보에 맞춰 자동으로 필드 생성
        # 전체 게시글 목록에서는 생성일, 수정일은 빼고 보여주기
        fields = ('id', 'title', 'content',)    # 어떤 필드를 serialize할지 결정 (사용자에게 최종적으로 JSON에 보여질 것을 결정)

# 단일 게시글에 대한 상세 정보를 제공하는 serializer
# serialize하는 fields가 달라지면 다른 serializer를 만들어줘야함
class ArticleSerializer(serializers.ModelSerializer):
    # article 입장에서 comment는 N이기에 many=True 필요, 또한 유효성 검사에서 제외되어야 함
    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True) # 기존 역참조용 필드를 override
    comment_set = CommentSerializer(many=True, read_only=True)  # 역참조할 시 pk말고 CommentSerializer에서 출력하는 모든 정보 출력 가능
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)    # 새로운 필드 추가

    class Meta:
        model = Article
        fields = '__all__'
```

### `articles/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('articles/<int:article_pk>/comments/', views.comment_create),
]
```

### `articles/views.py`

```python
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import get_object_or_404, get_list_or_404

from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer

# @api_view()는 기본값이 GET만 허용
@api_view(['GET', 'POST'])
def article_list(request):
    # 전체 게시글 조회
    if request.method == 'GET':
        # articles = Article.objects.all()
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    # 게시글 작성
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)   # ArticleSerializer를 사용한 이유는 게시글이 생성됐을 때 전체 필드를 출력하는 JSON을 사용하고 싶어서 사용
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    # 단일 게시글 조회
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    # 단일 게시글 삭제
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # 단일 게시글 수정
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)  # ModelForm과 다르게 앞쪽에 인스턴스가 들어감
        # serializer = ArticleSerializer(instance=article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['GET'])
def comment_list(request):
    # 댓글 목록 조회
    if request.method == 'GET':
        # comments = Comment.objects.all()
        comments = get_list_or_404(Comment)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    # comment = Comment.objects.get(pk=comment_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    # 특정 댓글 조회
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    # 특정 댓글 삭제
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # 특정 댓글 수정
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

# 단일 댓글 데이터 생성
@api_view(['POST'])
def comment_create(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):   # 아래줄에서 article이 들어가기 전 유효성 검사 진행 (read_only_fields 설정 필요)
            serializer.save(article=article)        # 외래키 삽입 (ModelForm과 달리 commit=False를 사용하지 않음)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
```

## GET (List)

### 게시글 데이터 목록 조회하기

<img width="1491" alt="dj_263" src="https://user-images.githubusercontent.com/86648892/212551772-a2d86c82-2186-4340-af6b-3e07d9e87d79.png">

## GET - Detail

### 단일 게시글 데이터 조회하기

<img width="1496" alt="dj_264" src="https://user-images.githubusercontent.com/86648892/212551771-ef86a807-6c56-4845-bf1e-007f47679da0.png">

## POST

### 게시글 데이터 생성하기

<img width="1371" alt="dj_265" src="https://user-images.githubusercontent.com/86648892/212551770-ba13e92b-c337-4375-adc3-ccea7a3df854.png">

- 요청에 대한 데이터 생성이 성공했을 경우 201 Created 상태 코드를 응답하고 실패했을 경우는 400 Bad request를 응답
  - `from rest_framework import status`
    - `return Response(serializer.data, status=status.HTTP_201_CREATED`
    - `return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST`
      - `if serializer.is_valid(raise_exception=True):` 와 같이 raise exception option을 주면 더이상 400을 따로 설정하지 않아도 됨

## DELETE

### 게시글 데이터 삭제하기

<img width="1328" alt="dj_266" src="https://user-images.githubusercontent.com/86648892/212551768-293984e0-9b5e-4a0e-a6c7-a9242b6081c7.png">

- 요청에 대한 데이터 삭제가 성공했을 경우는 204 No Content 상태 코드 응답
  - API는 반드시 요청에 대한 결과를 정확한 상태 코드로 전달해야 한다
    - 그래야 소통이 가능하다

## PUT

### 게시글 데이터 수정하기

<img width="1322" alt="dj_267" src="https://user-images.githubusercontent.com/86648892/212551767-3cad5381-a10f-403d-8154-407ea8d40efe.png">

- 요청에 대한 데이터 수정이 성공했을 경우는 200 OK 상태 코드 응답

---

# Django REST framework (N:1 Relation)

- N:1 관계에서의 모델 data를 Serialization하여 JSON으로 변환하는 방법 학습
- Serializer의 필드를 정의하는 것은 모델을 바탕으로 한 JSON 데이터에 추가적으로 덧붙이고 싶은 정보가 있을 때 정의한다고 생각하자
  - 역참조를 하는 related manager의 이름으로 필드를 정의하면
    - serializer에 역참조하는 데이터들을 넣어주는 로직을 쓰지 않아도 알아서 인식하여 넣어주는 것 뿐
      - 예시
        - `comment_set = CommentSerializer(many=True, read_only=True)`
        - `comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)`

## GET (List)

### 댓글 데이터 목록 조회하기

<img width="1507" alt="dj_268" src="https://user-images.githubusercontent.com/86648892/212551766-cf212aa2-56c7-4983-bb27-9b101886a18e.png">

## GET (Detail)

### 단일 댓글 데이터 조회하기

<img width="1502" alt="dj_269" src="https://user-images.githubusercontent.com/86648892/212551765-4739720f-47c9-450f-8d90-5051d993dded.png">

### POST

### 단일 댓글 데이터 생성하기

<img width="1325" alt="dj_270" src="https://user-images.githubusercontent.com/86648892/212551763-dbba2a11-3285-4084-898f-ce2e66b3d52c.png">

- CommentSerializer에서 article field의 데이터는 사용자로부터 입력받는 것이 아니므로
  - CommentSerializer에서 article은 read only field로 설정

### DELETE & PUT

### 댓글 데이터 삭제 및 수정 구현하기

<img width="1254" alt="dj_271" src="https://user-images.githubusercontent.com/86648892/212551761-fae71e32-bb35-4851-b62c-7cdcbfe8b700.png">

<img width="1261" alt="dj_272" src="https://user-images.githubusercontent.com/86648892/212551760-812c213a-d12d-403b-8e72-e94389278b85.png">

---

# N:1 역참조 데이터 조회

1. 특정 게시글에 작성된 댓글 목록 출력하기
   - **기존 필드 override**
2. 특정 게시글에 작성된 댓글의 개수 출력하기
   - **새로운 필드 추가**

## 특정 게시글에 작성된 댓글 목록 출력하기

### 기존 필드 Override (역참조 덮어씌우기)

1. **PrimaryKeyRelatedField()**
   - `comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)`

<img width="1455" alt="dj_273" src="https://user-images.githubusercontent.com/86648892/212551759-a42410eb-4376-4f4e-af99-3b14a21e9b5b.png">

1. **Nested Relationships**
   - `comment_set = CommentSerializer(many=True, read_only=True)`
     - 역참조 시 pk말고 CommentSerializer에서 출력하는 모든 정보 출력 가능

<img width="1259" alt="dj_274" src="https://user-images.githubusercontent.com/86648892/212551756-1ac50631-3d57-4b27-8bbe-99cb5334cdda.png">

## 특정 게시글에 작성된 댓글의 개수 출력하기

### 새로운 필드 추가

- `comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)`
  - `source`
    - serializers field’s argument
    - 필드를 채우는데 사용할 속성의 이름
    - 점 표기법(dotted notation)을 사용하여 속성을 탐색할 수 있음
    - source에 ORM 명령어 작성
      - `article.comment_set.count()`
        - ArticleSerializer 안이므로 article 생략, 문자열 안이어서 끝 괄호 생략
  - comment_count와 같이 변수명은 정의하고싶은 것으로 정의
  - 숫자를 다룰 것이므로 `IntegerField()`
  - 유효성 검사를 통과해야하므로 `read_only`는 True

<img width="1352" alt="dj_275" src="https://user-images.githubusercontent.com/86648892/212551753-1aeae757-f7dc-4138-b159-9d66aeae495b.png">

### [주의] 읽기 전용 필드 지정 이슈

- 기존에 물리적으로 존재했던 필드는 `read_only_fields` 지정 가능
- override되거나 추가된 필드의 경우에는 `read_only_fields`에 추가할 수 없음
- `read_only_fields` 에 지정하는 것들은 DB→클라이언트로 조회만 가능하고, 클라인어트→DB로 조작은 불가한 필드를 설정하는 것

<img width="715" alt="dj_276" src="https://user-images.githubusercontent.com/86648892/212551750-097f9c7d-a213-4a5f-aac8-4966a7afe5e0.png">

---

# Django shortcuts functions

- `django.shortcuts` 패키지는 개발에 도움될 수 있는 여러 함수와 클래스를 제공
- 제공되는 shortcuts 목록
  - `render()` , `redirect()` , `get_object_or_404()` , `get_list_or_404()`
    - `get()` 대신 `get_object_or_404()`
    - `all()` 대신 `get_list_or_404()`
  - [https://docs.djangoproject.com/en/4.1/topics/http/shortcuts/](https://docs.djangoproject.com/en/4.1/topics/http/shortcuts/)

## `get_object_or_404()`

- `objects.get()` 과 같은 코드의 경우 해당 pk의 값이 없거나, 혹은 2개 이상인 경우 모두 예외가 발생함
  - `objects.get()` 의 경우 코드 진행이 더 이상 이루어지지 않고
    - Django는 500 status를 반환함
- `get_object_or_404()` 의 경우 예외 발생 시 404 status와 함께 코드 진행 가능
  - 해당 객체가 없을 때 DoesNotExist 예외 대신 Http404를 raise함

<img width="607" alt="dj_277" src="https://user-images.githubusercontent.com/86648892/212551749-c2eee230-4f90-4015-9464-621c6b75a604.png">

## `get_list_or_404()`

- 빈 쿼리셋을 주는 것이 아닌 404 status를 반환

<img width="629" alt="dj_278" src="https://user-images.githubusercontent.com/86648892/212551747-4b59ae5c-47ac-46cc-8a32-c584fed83dc9.png">

## WHY?

- API 서버의 기본은 정확한 상태 코드를 반환하여 클라이언트와 소통하는 것
- 클라이언트 입장에서 “서버에 오류가 발생하여 요청을 수행할 수 없다(500)”라는 원인이 정확하지 않은 에러를 마주하기보다는, 서버가 적절한 예외 처리를 하고 클라이언트에게 올바른 에러를 전달하는 것 또한 중요한 요소

---

### [추가] SerializerMethodField

- [SerializerMethodField](https://www.django-rest-framework.org/api-guide/fields/#serializermethodfield)
- [SerializerMethodField로 모델에서 변형된 JSON을 내려주기](https://eunjin3786.tistory.com/m/268)
- [APIView, api_view란?](https://hangjastar.tistory.com/m/203)
