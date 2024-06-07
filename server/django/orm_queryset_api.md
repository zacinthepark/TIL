## ORM and Queryset API

---

### ORM

<p align="center">
    <img width="500" alt="dj_46" src="https://user-images.githubusercontent.com/86648892/188498037-a31c3dd8-7e77-4cdb-9514-0debe061338c.png">
</p>

- Object Relational Mapping
    - 객체지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에 데이터를 변환하는 프로그래밍 기술
    - 객체지향 프로그래밍에서 데이터베이스를 연동할 때, 데이터베이스와 객체지향 프로그래밍 언어 간의 호환되지 않는 데이터를 변환하는 프로그래밍 기법

### QuerySet API

<p align="center">
    <img width="500" alt="queryset_api" src="https://github.com/zacinthepark/TIL/assets/86648892/84d88992-d626-429a-8a68-513712b4d236">
</p>

<p align="center">
    <img width="500" alt="querysets" src="https://github.com/zacinthepark/TIL/assets/86648892/d30b9a82-d32b-4582-973a-dacd3251bf95">
</p>

- https://docs.djangoproject.com/en/4.2/ref/models/querysets/

- 장고에서 제공하는 기본 Manager
    - 장고 모델이 데이터베이스 쿼리 작업을 가능하게 하는 인터페이스
    - `modelName.objects.querySetMethod`

- Manager 이름 변경
    - 모델 클래스 선언 시 `people = models.Manager()`와 같이 Manager 이름 변경 가능

- QuerySet
    - 쿼리를 통해 데이터베이스에게서 전달받은 객체 목록
    - 리스트는 아니지만 리스트와 같은 특성을 가짐
        - iterable
        - index를 통해 접근 가능
    - QuerySet API methods that 'return new querysets'
        - objects manager를 사용하여 *복수의 데이터* 를 가져오는 queryset method를 사용하면 querysets를 반환
    - QuerySet API methods that 'do not return querysets'
        - *단일 객체* 반환 시에는 모델의 인스턴스를 반환

### READ

- `all()`
    - 전체 데이터 조회

- `distinct()`
    - 중복없이 조회

- `values(*fields)`
    - 조회하고자 하는 필드명(컬럼)을 지정
    - 모델 인스턴스가 아닌 지정한 필드에 대한 key-value를 갖는 딕셔너리 요소들을 가진 QuerySet을 반환

- `get(condition)`
    - 조건에 맞는 단일 인스턴스 조회
    - 반드시 하나의 인스턴스가 리턴되어야하므로 pk와 같이 유니크한 데이터를 조회할 때 사용
    - 결과값이 없는 경우 DoesNotExist
    - 결과값이 1개보다 많은 경우 MultipleObjectsReturned

- `order_by(*fields)`
    - 데이터 정렬
    - 오름차순이 기본이며, 필드명에 하이픈을 작성하면 내림차순, 인자로 `?`를 입력하면 랜덤으로 정렬
    - `User.objects.order_by('balance').order_by('-age')`와 같이 체이닝을 할 경우 마지막 호출만 적용됨 (age 기준 내림차순 정렬과 동일)

- `first(), last()`
    - `Employees.objects.order_by('birthdate').first()`

- `filter(condition)`
    - 주어진 조건과 일치하는 객체를 포함하는 QuerySet 반환
    - Field Lookups 활용

- `exclude(condition)`
    - 주어진 조건과 일치하지 않는 객체를 포함하는 QuerySet 반환
    - Field Lookups 활용

- `count()`
    - `Employees.objects.filter(title='IT Manager').count()`

- `exists()`
    - True or False 반환
    - `Customers.objects.filter(country='korea').exists()`

### Field Lookups

- https://www.w3schools.com/django/django_ref_field_lookups.php

- `필드명__lookup명 = 값`

- `__exact`
    - 값이 일치하는 레코드

- `__contains`
    - 값을 포함하는 레코드

- `__in`
    - 리스트와 사용하며 해당 리스트의 원소 중 하나인 경우

- `__gt, __gte, __lt, __lte`
    - 대소 비교

- `__startswith`
    - 해당 값으로 시작하는 경우

- `__endswith`
    - 해당 값으로 끝나는 경우

- `__range=(A, B)`
    - SQL의 BETWEEN A AND B에 해당

- `__year, __month, __day`
    - 날짜 자료형에서 year, month, day 추출
    - `created__month__gte = 6`과 같이 결합하여 사용 가능

#### AND(&)

- `&` 연산자 사용
    - `Post.objects.filter(region='Asia') & Post.objects.filter(body__contains='발리')`

- 인자로 지정
    - `Post.objects.filter(region='Asia', body__contains='발리')`

- QuerySet 대상으로 작업
    - `qs = Post.objects.filter(region='Asia')`
    - `qs.filter(body__contains='발리')`

- Q 객체 활용
    - `from django.db.models import Q`
    - `Post.objects.filter(Q(region='Asia) & Q(body__contains='발리'))`

#### OR (|)

- `|` 연산자 사용
    - `Post.objects.filter(region='Asia') | Post.objects.filter(body__contains='발리')`

- Q 객체 활용
    - `from django.db.models import Q`
    - `Post.objects.filter(Q(region='Asia) | Q(body__contains='발리'))`
    - `Article.objects.get(Q(title__startswith='Who', Q(created_at=date(2005, 5, 2)) | Q(created_at=date(2005, 5, 6))))`

### GROUPING

- `aggregate()`
    - 집계 함수를 통해 특정 필드 전체의 합, 평균, 개수 등을 계산할 때 사용
    - 딕셔너리 반환
    - `Avg` , `Count` , `Max` , `Min` , `Sum`, ...

- `annotate()`
    - 쿼리의 각 항목에 대한 요약 값을 계산
    - SQL의 `GROUP BY`에 해당
    - '주석을 단다'는 뜻
        - 어떠한 데이터를 조회하면서 추가 정보를 덧붙이는 것
        - 데이터에 존재하는 컬럼이 아니라 계산을 통해서 만들어낸 것
        - 테이블 입장에서는 잠깐 주석이 붙은 것
        - 요약값을 만드는 것이기에 집계 함수와 함께 사용

```python
from django.db.models import Avg, Max, Sum, Count
User.objects.filter(age__gte=30).aggregate(Avg('age'))
# {'age__avg': 37.65909090909091}

User.objects.filter(age__gte=30).aggregate(avg_value=Avg('age'))
# {'avg_value': 37.65909090909091}

User.objects.aggregate(Max('balance'))
# {'balance__max': 1000000}

User.objects.aggregate(Sum('balance'))
# {'balance__sum': 14435040}

User.objects.values('country').annotate(Count('country'))

"""
<QuerySet [
	{'country': '강원도', 'country__count': 14},
	{'country': '경기도', 'country__count': 9},
	{'country': '경상남도', 'country__count': 9},
	...
]>
"""

User.objects.values('country').annotate(num_of_country=Count('country'))

"""
<QuerySet [
	{'country': '강원도', 'num_of_country': 14},
	{'country': '경기도', 'num_of_country': 9},
	{'country': '경상남도', 'num_of_country': 9},
	...
]>
"""

# 한번에 여러 값을 계산해 조회 가능
User.objects.values('country').annotate(Count('country'), avg_balance=Avg('balance'))

# 전체 게시글 조회
# annotate로 각 게시글의 댓글 개수(`number_of_comment`)와 2000-01-01보다 나중에 작성된 댓글의 개수(`pub_date`)를 함께 조회
Article.objects.annotate(
	number_of_comment=Count('comment'),
	pub_date=Count('comment', filter=Q(comment__created_at__lte='2000-01-01'))
)
```

### CREATE

- Model `save()`
    - `article = Article()`
        - `article.title = 'title'`
    - `article = Article(title='title')`
    - `article.save()`

- QuerySet `create()`
    - `Article.objects.create(title='title')`
    - `save()` 필요없음

### UPDATE

- Model `save()`
    - `post = Post.objects.get(title='로라이마')`
    - `post.title = '로라이마 산'`
    - `post.region = 'South America'`
    - `post.save()`

- QuerySet `update()`
    - `qs = Post.objects.filter(title='트롤퉁가')`
    - `qs.update(title='트롤퉁가 전망대', region='Europe')`

### DELETE

- Model `delete()`
    - `post = Post.objects.get(title='로라이마 산')`
    - `post.delete()`

- QuerySet `delete()`
    - `qs = Post.objects.filter(title='트롤퉁가 전망대')`
    - `qs.delete()`
