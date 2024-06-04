## ORM and Queryset API

---

### Object Relational Mapping

- ORM
    - 객체지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에 데이터를 변환하는 프로그래밍 기술
    - 객체지향 프로그래밍에서 데이터베이스를 연동할 때, 데이터베이스와 객체지향 프로그래밍 언어 간의 호환되지 않는 데이터를 변환하는 프로그래밍 기법

<p align="center">
    <img width="500" alt="dj_46" src="https://user-images.githubusercontent.com/86648892/188498037-a31c3dd8-7e77-4cdb-9514-0debe061338c.png">
</p>

- Django (i speak python) ↔ DB (i speak SQL)
    - Django Framework는 내장된 Django ORM이 있음
    - SQL을 사용하지 않고 데이터베이스를 조작할 수 있게 만들어주는 매개체

- ORM 장점
    - 객체지향 언어로 DB 조작이 가능
    - 객체지향적 접근으로 인한 높은 생산성

- ORM 단점
    - ORM만으로 완전한 서비스를 구현하기 어려운 경우가 있음

### `shell_plus`

- Shell이란 운영체제 상에서 다양한 기능과 서비스를 구현하는 인터페이스를 제공하는 프로그램 (User ↔ Shell ↔ OS)

- Django Shell
    - `pip install django-extensions`
    - `python manage.py shell_plus`
        - django-extension이 제공하는 shell_plus
        - 자주 사용하는 모듈을 자동으로 import
        - 없다면 `python manage.py shell`

- shell 종료 시 `exit()`

### QuerySet API

- ORM이 사용하는 라이브러리 이름
- Django가 기본적으로 ORM을 제공함에 따라 DB를 편하게 조작할 수 있도록 도움

<p align="center">
    <img width="500" alt="queryset_api" src="https://github.com/zacinthepark/TIL/assets/86648892/84d88992-d626-429a-8a68-513712b4d236">
</p>

- objects manager
    - 다양한 Queryset API를 제공
    - Django 모델이 데이터베이스 쿼리 작업을 가능하게 하는 인터페이스
    - Django는 기본적으로 모든 Django 모델 클래스에 대해 objects라는 Manager 객체를 자동으로 추가함

- QuerySet
    - 쿼리를 통해 데이터베이스에게서 전달받은 객체 목록
    - 리스트는 아니지만 리스트와 같은 특성을 가짐
        - iterable
        - index를 통해 접근 가능
    - Django ORM을 통해 만들어진 자료형이며, 필터를 걸거나 정렬 등을 수행할 수 있음

- QuerySet API methods that 'return new querysets'
    - objects manager를 사용하여 *복수의 데이터* 를 가져오는 queryset method를 사용하면 querysets를 반환

- QuerySet API methods that 'do not return querysets'
    - *단일 객체* 반환 시에는 모델의 인스턴스를 반환

### CRUD with QuerySet API

- https://docs.djangoproject.com/en/4.1/ref/models/querysets/
- https://www.w3schools.com/django/django_ref_field_lookups.php

#### 1. READ

<p align="center">
    <img width="600" alt="dj_50" src="https://user-images.githubusercontent.com/86648892/188498051-1b43737c-5ae7-4a91-9254-0d8d431ebe51.png">
</p>

- `all()`
    - `QuerySet` return
    - 전체 데이터 조회

<p align="center">
    <img width="600" alt="dj_51" src="https://user-images.githubusercontent.com/86648892/188498055-4cc49318-6668-4901-908a-22174b97a2a9.png">
</p>


- `get()`
    - 유니크한 데이터, 고유성(uniqueness)을 보장하는 조회에서 사용해야함
        - 대표적으로 primary key
    - 단일 데이터 조회
    - 객체를 찾을 수 없으면 DoesNotExist 예외를 발생시키고, 둘 이상의 객체를 찾으면 MultipleObjectsReturned 예외를 발생시킴

<p align="center">
<img width="600" alt="dj_52" src="https://user-images.githubusercontent.com/86648892/188498056-f5113ac0-6945-491b-a435-6d15582c3979.png">
</p>

- `filter()`
    - `QuerySet` return
    - 지정된 조회 매개 변수와 일치하는 객체를 포함하는 새 QuerySet을 반환
    - 항상 QuerySet으로 반환함
        - 없으면 빈 QuerySet
        - *단일 객체도 QuerySet으로*
    - pk에는 부적합
        - QuerySet으로 주기에 한번 더 벗겨내야하는 불편함
        - 데이터를 조회했는데 없음에도 불구하고 빈 QuerySet을 반환해버림
        - 예외처리가 어려움

- *Field lookups*
    - 조건을 설정하여 조회하는 것
    - SQL WHERE 절의 상세한 조건을 지정하는 방법
    - 특정 레코드에 대한 조건을 설정하는 방법
    - QuerySet 메서드 `filter()`, `exclude()` 및 `get()`에 대한 키워드 인자로 지정됨
    - 문법 규칙
        - 필드명 뒤에 double-underscore 이후 작성함
        - `field__lookuptype=value`

#### 2. CREATE

- 클래스를 통한 인스턴스 생성
    - `article = Article()`
    - `article.title = 'title'`
        - 혹은 `article = Article(title='title')`
    - `article.save()`를 통해 저장

- QuerySet API `create()` 활용
    - `Article.objects.create(title='title')`
    - `save()` 필요없음
        - save 이전에 유효성 검사를 하지 못한다는 단점

- sample code

```html
{% extends 'base.html' %} {% block content %}
<h1>NEW</h1>
<form action="{% url 'articles:create' %}" method="GET">
    <label for="title">Title: </label>
    {% comment %} name은 url querystring에 들어갈 키 명칭 {% endcomment %}
    <input type="text" name="title" id="title" /><br />
    <label for="content">Content: </label>
    <input type="text" name="content" id="content" /><br />
    <input type="submit" />
</form>
<hr />
<a href="{% url 'articles:index' %}">Go Back to Index</a>
{% endblock content %}
```

```python
# new page의 input에서 쏴준 request 속에 데이터가 있다
# 요청에 대한 모든 데이터는 request에 있다
# input에 정의한 name이 key
def create(request):
    # 사용자의 데이터를 받아서 DB에 저장
    # 데이터 받기
    title = request.GET.get('title')
    content = request.GET.get('content')

    # DB에 저장
    # 1
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 2 (왼쪽이 DB의 필드, 오른쪽이 요청에서 받아온 변수)
    article = Article(title=title, content=content)
    article.save()

    # 3
    # Article.objects.create(title=title, content=content)

    return render(request, 'articles/create.html')
```

#### 3. UPDATE

- 수정하고자 하는 인스턴스 객체를 조회 후 반환 값을 저장

- 인스턴스 객체의 인스턴스 변수 값을 새로운 값으로 할당

- `save()` 인스턴스 메서드 호출


### 4. DELETE

- 삭제하고자 하는 인스턴스 객체를 조회 후 반환 값을 저장

- `delete()` 인스턴스 메서드 호출

- pk 1번이 삭제되고 새로 추가되는 항목은 pk 1번에 들어갈까? 끝 순서로 들어갈까?
    - 끝 순서로 들어간다
    - 대부분의 데이터베이스는 삭제된 값을 재사용하지 않는다

### QuerySet API 추가

- [User CRUD](#user-crud)
- [Sorting Data](#sorting-data)
- [Filtering Data](#filtering-data)
- [Grouping Data](#grouping-data-aggregation)
- [Improve Query](#improve-query)

### User CRUD

#### 모든 user 레코드 조회

- `User.objects.all()`

#### 101번 user 레코드 조회

- `User.objects.get(pk=101)`

#### 101번 user 레코드의 last_name을 ‘김’으로 수정

- `user = User.objects.get(pk=101)`
- `user.last_name = '김'`
- `user.save()`

#### 101번 user 레코드 삭제

- `user = User.objects.get(pk=101)`
- `user.delete()`

#### 전체 인원 수 조회

1. `User.objects.count()`
2. `len(User.objects.all())`

### Sorting Data

#### 나이가 어린 순으로 이름과 나이 조회

- `User.objects.order_by('age').values('first_name', 'age')`
    - `.order_by(*fields)`
        - QuerySet의 정렬을 재정의
        - 기본적으로 오름차순으로 정렬하며
        - *필드명에 하이픈을 작성하면 내림차순으로 정렬*
        - *인자로 (`?`)를 입력하면 랜덤으로 정렬*

    - order_by 주의사항
        - `User.objects.order_by('balance').order_by('-age')`
            - 이와 같이 작성할 경우 앞의 호출은 모두 지워지고 마지막 호출만 적용됨
            - `User.objects.order_by('-age')` 와 같음

    - `.values(*fields, **expressions)`
        - 모델 인스턴스가 아닌 딕셔너리 요소들을 가진 QuerySet을 반환
        - `*fields` 는 선택인자이며, 조회하고자 하는 필드명을 가변인자로 받음
        - 필드를 지정하면 각 딕셔너리에는 지정한 필드에 대한 key와 value만을 출력
        - 입력하지 않을 경우 각 딕셔너리에는 레코드의 모든 필드에 대한 key와 value를 출력

#### 이름과 나이를 나이가 많은 순서대로 조회

- `User.objects.order_by('-age').values('first_name', 'age')`

#### 이름, 나이, 계좌 잔고를 나이가 어린순으로, 만약 같은 나이라면 계좌 잔고가 많은 순으로 정렬해서 조회

- `User.objects.order_by('age', '-balance').values('first_name', 'age', 'balance')`

### Filtering Data

#### 중복없이 모든 지역 조회

- `User.objects.distinct().values('country')`

#### 지역 순으로 오름차순 정렬하여 중복없이 모든 지역 조회

- `User.objects.distict().values('country').order_by('country')`

#### 이름과 지역 중복없이 모든 이름과 지역 조회

- `User.objects.distinct().values('first_name', 'country')`

#### 이름과 지역 중복없이 오름차순 정렬하여 모든 이름과 지역 조회

- `User.objects.distinct().values('first_name', 'country').order_by('country')`

#### 나이가 30살인 사람들의 이름 조회

- `User.objects.filter(age=30).values('first_name')`

#### 나이가 30살 이상인 사람들의 이름과 나이 조회

- `User.objects.filter(age__gte=30).values(’first_name’, ‘age’)`

#### 나이가 30살 이상이고 계좌 잔고가 50만원 초과인 사람들의 이름, 나이, 계좌 잔고 조회

- `User.objects.filter(age__gte=30, balance__gt=500000).values(’first_name’, ‘age’, ‘balance’)`

#### 이름에 ‘호’가 포함되는 사람들의 이름과 성 조회

- `User.objects.filter(first_name__contains='호').values('first_name', 'last_name')`

#### 핸드폰 번호가 011로 시작하는 사람들의 이름과 핸드폰 번호 조회

- `User.objects.filter(phone__startswith='011-').values('first_name', 'phone')`
    - SQL에서의 `%` 와일드카드와 같음
    - `_`(underscore)는 별도로 정규 표현식을 사용해야함

#### 이름이 ‘준’으로 끝나는 사람들의 이름 조회

- `User.objects.filter(first_name__endswith='준').values('first_name')`

#### 경기도 혹은 강원도에 사는 사람들의 이름과 지역 조회

- `User.objects.filter(country__in=['경기도', ‘강원도’]).values(’first_name’, ‘country’)`

#### 경기도 혹은 강원도에 살지 않는 사람들의 이름과 지역 조회

- `User.objects.exclude(country__in=['경기도', '강원도']).values('first_name', 'country')`
    - `exclude(**kwargs)`
        - 주어진 매개변수와 일치하지 않는 객체를 포함하는 QuerySet 반환

#### 나이가 가장 어린 10명의 이름과 나이 조회

- `User.objects.order_by('age').values('first_name', 'age')[:10]`

#### 나이가 30이거나 성이 김씨인 사람들 조회

```python
from django.db.models import Q
User.objects.filter(Q(age=30) | Q(last_name='김'))
```

> Q object: 필터링 시 복잡한 쿼리를 실행해야하는 경우 Q 객체가 필요함<br>
https://docs.djangoproject.com/en/4.1/topics/db/queries/#complex-lookups-with-q-objects

```python
from django.db.models import Q
Q(question__startswith='What')

# & 및 | 를 사용하여 Q 객체를 결합할 수 있음
Q(question__startswith='Who') | Q(question__startswith='What')

# 조회를 하면서 여러 Q 객체를 제공할 수도 있음
Article.objects.get(
    Q(title__startswith='Who', Q(created_at=date(2005, 5, 2)) | Q(created_at=date(2005, 5, 6)))
)
```

### Grouping Data (Aggregation)

- `aggregate()`
    - https://docs.djangoproject.com/en/4.1/topics/db/aggregation/#
    - 전체 QuerySet에 대한 값을 계산
    - 특정 필드 전체의 합, 평균, 개수 등을 계산할 때 사용
    - *딕셔너리* 를 반환
    - Aggregate Functions: `Avg` , `Count` , `Max` , `Min` , `Sum`, ...

- `annotate()`
    - 쿼리의 각 항목에 대한 요약 값을 계산
    - SQL의 `GROUP BY` 에 해당
    - '주석을 단다'라는 뜻
        - 어떠한 데이터를 조회하면서 추가 정보를 덧붙이는 것
        - 데이터에 존재하는 컬럼이 아니라 계산을 통해서 만들어낸 것
        - 테이블 입장에서는 잠깐 주석이 붙은 것
        - 요약값을 만드는 것이기에 Aggregate Functions와 함께 사용

#### 나이가 30살 이상인 사람들의 평균 나이 조회

```python
from django.db.models import Avg
User.objects.filter(age__gte=30).aggregate(Avg('age'))
# {'age__avg': 37.65909090909091}

# 딕셔너리 key 값을 수정 가능
User.objects.filter(age__gte=30).aggregate(avg_value=Avg('age'))
# {'avg_value': 37.65909090909091}
```

#### 가장 높은 계좌 잔액 조회

```python
from django.db.models import Max
User.objects.aggregate(Max('balance'))
# {'balance__max': 1000000}
```

#### 모든 계좌 잔액 총액 조회

```python
from django.db.models import Sum
User.objects.aggregate(Sum('balance'))
# {'balance__sum': 14435040}
```

#### 각 지역별로 몇명씩 살고 있는지 조회

```python
from django.db.models import Count
User.objects.values('country').annotate(Count('country'))

"""
<QuerySet [
	{'country': '강원도', 'country__count': 14},
	{'country': '경기도', 'country__count': 9},
	{'country': '경상남도', 'country__count': 9},
	...
]>
"""

# aggregate와 마찬가지로 딕셔너리의 key 값을 변경 가능

from django.db.models import Count
User.objects.values('country').annotate(num_of_country=Count('country'))

"""
<QuerySet [
	{'country': '강원도', 'num_of_country': 14},
	{'country': '경기도', 'num_of_country': 9},
	{'country': '경상남도', 'num_of_country': 9},
	...
]>
"""
```

#### 각 지역별로 몇명씩 살고 있는지 + 지역별 계좌 잔액 평균 조회

```python
# 한번에 여러 값을 계산해 조회 가능
User.objects.values('country').annotate(Count('country'), avg_balance=Avg('balance'))
```

#### 각 성씨가 몇명씩 있는지 조회

- `User.objects.values('last_name').annotate(Count('last_name'))`

#### 게시글 댓글 조회

```python
# Comment-Article의 관계가 N:1인 경우
# 전체 게시글을 조회하면서
# annotate로 각 게시글의 댓글 개수(`number_of_comment`)와 2000-01-01보다 나중에 작성된 댓글의 개수(`pub_date`)를 함께 조회하는 것

Article.objects.annotate(
	number_of_comment=Count('comment'),
	pub_date=Count('comment', filter=Q(comment__created_at__lte='2000-01-01'))
)
```

### Improve Query

- 데이터 조회 시 subquery를 줄일 수 있는 방향성을 고민
    - Django가 DB를 히트하는 수를 줄이는 것이 목표
    - ORM의 lazy한 특성으로 인해 데이터를 가져올 때 DB를 실제로 히트하는 것이 아닌, for문 등 실제로 필요할 때 DB를 히트함
    - main query를 보내는 시점에 N:1 관계에있는, N번 히트해야할 데이터를 미리 가져온다면 향후 subquery를 줄일 수 있을 것

- `annotate`, `select_related`, `prefetched_related` 등 활용

```python
# views.py

from django.shortcuts import render
from .models import Article, Comment
from django.db.models import Count

# Create your views here.
def index_1(request):
    # articles = Article.objects.order_by('-pk')
    articles = Article.objects.annotate(Count('comment')).order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index_1.html', context)

def index_2(request):
    # articles = Article.objects.order_by('-pk')
    articles = Article.objects.select_related('user').order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index_2.html', context)

def index_3(request):
    # articles = Article.objects.order_by('-pk')
    articles = Article.objects.prefetch_related('comment_set').order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index_3.html', context)

from django.db.models import Prefetch

def index_4(request):
    # articles = Article.objects.order_by('-pk')
    # articles = Article.objects.prefetch_related('comment_set').order_by('-pk')
    articles = Article.objects.prefetch_related(
        Prefetch('comment_set', queryset=Comment.objects.select_related('user'))
    ).order_by('-pk')

    context = {
        'articles': articles,
    }
    return render(request, 'articles/index_4.html', context)
```

```html
<!-- index_1.html -->

{% extends 'base.html' %} {% block content %}
<h1>Articles</h1>
{% for article in articles %}
<p>제목 : {{ article.title }}</p>
{% comment %}
<p>댓글개수 : {{ article.comment_set.count }}</p>
{% endcomment %}
<p>댓글개수 : {{ article.comment__count }}</p>
<hr />
{% endfor %} {% endblock content %}
```

```html
<!-- index_2.html -->

{% extends 'base.html' %} {% block content %}
<h1>Articles</h1>
{% for article in articles %}
<h3>작성자 : {{ article.user.username }}</h3>
<p>제목 : {{ article.title }}</p>
<hr />
{% endfor %} {% endblock content %}
```

```html
<!-- index_3.html -->

{% extends 'base.html' %} {% block content %}
<h1>Articles</h1>
{% for article in articles %}
<p>제목 : {{ article.title }}</p>
<p>댓글 목록</p>
{% for comment in article.comment_set.all %}
<p>{{ comment.content }}</p>
{% endfor %}
<hr />
{% endfor %} {% endblock content %}
```

```html
<!-- index_4.html -->

{% extends 'base.html' %} {% block content %}
<h1>Articles</h1>
{% for article in articles %}
<p>제목 : {{ article.title }}</p>
<p>댓글 목록</p>
{% for comment in article.comment_set.all %}
<p>{{ comment.user.username }} : {{ comment.content }}</p>
{% endfor %}
<hr />
{% endfor %} {% endblock content %}
```

- `annotate()`
    - `articles = Article.objects.annotate(Count('comment')).order_by('-pk')`
    - `{{ article.comment__count }}`
        - 게시글을 가져올 때 댓글 개수까지 카운팅한 값을 한번에 가져오는 것으로 개선 가능

- `select_related()`
    - 1:1 또는 N:1 참조 관계에서 쿼리 개선
    - `articles = Article.objects.select_related('user').order_by('-pk')`
        - 각 게시글마다 user를 참조하고 있음
        - 원래는 article 전체를 다 가져오는 것에서 그쳤는데
        - article을 가져오면서 article이 참조하고 있는 user id값도 처음 한번에 다 들고와서 중복적인 쿼리 요청을 1번으로 줄임

- `prefetched_prelated()`
    - M:N 또는 N:1 역참조 관계에서 쿼리 개선
    - `articles = Article.objects.prefetch_related(’comment_set’).order_by(’-pk’)`
        - 게시글 전체를 가져오면서 거기에 묶여있는 댓글 정보들도 한번에 다 들고옴

```python
articles = Articles.objects.prefetch_related(
    Prefetch('comment_set', queryset=Comment.objects.select_related('user'))
).order_by('-pk')
```

- 기존 상황
    - 게시글 출력하면서 댓글 목록 출력
    - 댓글 출력하면서 각 댓글의 작성자를 출력
    - 100번의 쿼리

- 개선 상황
    - 댓글을 가져오면서 유저를 한번에 붙이고
    - 게시글을 가져오면서 댓글을 한번에 붙여서 가져옴
    - 2번의 쿼리로 개선
