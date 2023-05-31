## Django M:N Relationship

---

- [Many to many relationship](#many-to-many-relationship)
- [ManyToManyField](#manytomanyfieldto-options)
- [M : N (Article-User) (Likes)](#m--n-article-user)
- [M : N (User-User) (Follows)](#m--n-user-user)

## Many-to-many relationship

---

### target and source model

1. target model
- 관계 필드를 가지지 않은 모델
- N:1에서는 1에 해당

2. source model
- 관계 필드를 가진 모델
- N:1에서는 N에 해당

### `models.py`

```python
from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'

class Patient(models.Model):
    # doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)  # [1] 1명의 의사 - N명의 환자인 경우 (한계: 동일한 환자가 여러 의사에게 예약을 받는 경우를 구현하기 어려움)
    # [3] M:N 필드 (중개모델을 Django에서 알아서 생성해줌)
    doctors = models.ManyToManyField(Doctor, related_name='patients', through='Reservation')
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'

# [2] 중개모델 작성 (예약을 단위로 기록)
# class Reservation(models.Model):
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'

# [3-1] ManyToManyField의 extra data 작성 (through argument와 연결)
class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptom = models.TextField()
    reserved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'
```

### 정리

- M:N 관계로 맺어진 두 테이블에는 변화가 없음
- Django의 ManyToManyField는 중개 테이블을 자동으로 생성함
- Django의 ManyToManyField는 M:N 관계를 맺는 두 모델 어디에 위치해도 상관 없음
- 대신 필드 작성 위치에 따라 참조와 역참조 방향을 주의할 것
- N:1은 완전한 종속의 관계였지만 M:N은 의사에게 진찰받는 환자, 환자를 진찰하는 의사의 2가지 형태로 모두 표현이 가능한 것

## `ManyToManyField(to, **options)`

---

### ManyToManyField란

- 다대다 관계 설정 시 사용하는 모델 필드
- 하나의 필수 위치인자가 필요
- M:N 관계로 설정할 모델 클래스
- 모델 필드의 RelatedManager를 사용하여 관련 개체를 추가, 제거, 혹은 만들 수 있음
- `add()` , `remove()` , `create()` , `clear()` …

### 데이터베이스에서의 표현

- Django는 다대다 관계를 나타내는 중개 테이블을 생성
- ManyToManyField는 중개 테이블에 별도 생성되는 것이며 기존 모델 테이블에 컬럼이 추가되지 않음
- 중개 테이블 이름은 **appname_ManyToManyField를 포함한 modelname_ManyToManyFieldname**
  - ex) `articles_article_like_users`
  - `db_table` arguments를 사용하여 중개 테이블의 이름을 변경할 수도 있음
- 중개 테이블의 컬럼 이름
  - source model과 target model이 다른 경우
    - id
    - **<containing_model>\_id**
      - 참조하는 모델 이름
    - **<other_model>\_id**
      - 역참조하는 모델 이름
  - 동일한 모델의 관계인 경우
    - id
    - **from\_<model>\_id**
    - **to\_<model>\_id**

### ManyToManyField Arguments

1. `related_name`
2. `through`
3. `symmetrical`

- `blank=True`
  - db의 유효성 검사와 관련없음 (값이 있어야함)
  - 사용자가 입력할 때 blank를 허용하는 것

### 1. `related_name` argument

- target model이 source model을 참조할 때 사용할 manager name
- ForeignKey의 `related_name`과 동일

### 2. `through` argument

- 중개 테이블을 수동으로 지정하려는 경우 `through` 옵션을 사용하여 사용하려는 중개 테이블을 나타내는 Django 모델을 지정할 수 있음
- 가장 일반적인 용도는 중개 테이블에 extra data를 추가하여 다대다 관계와 연결하려는 경우
- ManyToManyField를 조회할 때 해당 중개 테이블을 ‘통해서’ 조회를 하겠다는 뜻
- ManyToManyField에 자동으로 생성하는 것을 이제는 through 테이블로 대체하겠다는 뜻
- 예약을 주체로 예약을 생성하는 것도 가능하지만
  - 환자 혹은 의사를 주체로 관계를 추가하는 것이 더 합리적
- `add()` 시 `through_defaults={'key': 'value'}` argument 필요
  - `through_defaults` 값에 딕셔너리 타입으로 입력
  - ex) `patient2.doctors.add(doctor1, through_defaults={'symptom': 'flu'})`

### 3. `symmetrical` argument

- 기본값은 True
- **ManyToManyField가 동일한 모델(on self)을 가리키는 정의**에서만 사용
- 재귀 참조 (self 참조)

<img width="833" alt="dj_169" src="https://user-images.githubusercontent.com/86648892/212547774-196ab395-d15f-464b-b960-1a30529cb380.png">

- `symmetrical=True` 일 경우
  - set 매니저를 추가하지 않음
  - source 모델의 인스턴스가 target 모델의 인스턴스를 참조하면
    - 자동으로 target 모델 인스턴스도 source 모델 인스턴스를 참조하도록 함 (대칭)
    - 쉽게 말해 1-2의 관계가 추가된다면, 2-1의 관계도 추가됨
  - 대칭을 원하지 않는 경우 `False` 로 설정

### ManyToManyField Related Manager

- N:1 혹은 M:N 관계에서 사용 가능한 문맥(context)
- Django는 모델 간 N:1 혹은 M:N 관계가 설정되면 역참조 시에 사용할 수 있는 manager를 생성
  - 모델 생성 시 obejcts라는 매니저를 통해 queryset api를 사용했던 것처럼 related manager를 통해 queryset api 사용 가능
- N:1, M:N 관계에 따라 다르게 사용 및 동작됨
  - N:1
    - target 모델 객체만 사용 가능
  - M:N
    - 관련된 두 객체 모두 사용 가능
- 메서드 종류
  - `add()` , `remove()` , `create()` , `clear()` , `set()` …

### ManyToManyField Methods

### 1. `add()`

- “지정된 객체를 관련 객체 집합에 추가”
- 이미 존재하는 관계에 사용하면 관계가 복제되지 않음
- 모델 인스턴스, 필드 값(PK)을 인자로 허용

### 2. `remove()`

- “관련 객체 집합에서 지정된 모델 개체를 제거”
- 내부적으로 `QuerySet.delete()` 를 사용하여 관계가 삭제됨
- 모델 인스턴스, 필드 값(PK)을 인자로 허용

### 중개 테이블 필드 생성 규칙

<img width="962" alt="dj_170" src="https://user-images.githubusercontent.com/86648892/212547771-e43b0d22-2295-4120-afc2-2fee1e39623e.png">

## M : N (Article-User)

---

### Like 기능 구현하기

### 모델 관계 설정

<img width="968" alt="dj_171" src="https://user-images.githubusercontent.com/86648892/212547769-a727db36-6b1a-4798-9eb6-89078f77aa32.png">

- `like_users` 필드 생성 시 자동으로 역참조에는 `.article_set` 매니저가 생성됨
- 그러나 이전 N:1 (Aritcle-User) 관계에서 이미 해당 매니저를 사용 중
  - `user.article_set.all()`: 해당 유저가 작성한 모든 게시글 조회
  - **user가 작성한 글들(`user.article_set`)과 user가 좋아요를 누른 글(`user.article_set`)을 구분할 수 없게 됨**
  - 이런 경우 user와 관계된 ForeignKey 혹은 ManyToManyField 중 하나에 `related_name` 을 작성해야 함

<img width="1022" alt="dj_172" src="https://user-images.githubusercontent.com/86648892/212547765-07fbe386-c6af-4cdb-bb0c-3257d092b1d8.png">

- 생성된 중개 테이블 확인

<img width="485" alt="dj_173" src="https://user-images.githubusercontent.com/86648892/212547761-5dcf4b86-f09a-4cfa-bfd5-94886cd7c232.png">

<img width="1000" alt="dj_174" src="https://user-images.githubusercontent.com/86648892/212547757-9fa18eb3-8299-436d-82c5-96f30988daf6.png">

### url과 view 함수 설정

<img width="586" alt="dj_175" src="https://user-images.githubusercontent.com/86648892/212547755-78740740-e653-4bb4-9518-f4e233613d38.png">

<img width="590" alt="dj_176" src="https://user-images.githubusercontent.com/86648892/212547751-e2de49dd-ce83-4c3a-a12e-f7347a7fd8bc.png">

### `.exists()`

- QuerySet에 결과가 포함되어 있으면 True를 반환하고 그렇지 않으면 False를 반환
- 특히 큰 QuerySet에 있는 특정 개체의 존재와 관련된 검색에 유용

### index 템플릿에서 각 게시글에 좋아요 버튼 출력하기

<img width="810" alt="dj_177" src="https://user-images.githubusercontent.com/86648892/212547747-ec70756d-eb73-4ce1-b563-f299d8d9cbdf.png">

### 데코레이터 및 is_authenticated 추가

<img width="825" alt="dj_178" src="https://user-images.githubusercontent.com/86648892/212547743-6d270f89-6121-48c2-8358-92f30092ed1b.png">

## M : N (User-User)

---

### Profile 및 Follow 구현

### 1. Profile 구현 (자연스러운 follow 흐름을 위한 프로필 페이지를 먼저 작성)

### url 및 view 함수 작성

- urlpatterns는 위에서부터 매칭한다
- 만약 `path(’<str:username>/’, views.profile, name=’profile’),` 를 맨 위에 작성해버리면 그 아래에 있는 login, logout, signup 등 모든 문자열 시작 url들이 죽어버린다

<img width="895" alt="dj_179" src="https://user-images.githubusercontent.com/86648892/212547738-b4ed5f5d-525f-400e-a073-d81f2ac7deb6.png">

<img width="894" alt="dj_180" src="https://user-images.githubusercontent.com/86648892/212547736-853d38ea-5ce4-40ee-a771-782407629a39.png">

### profile 템플릿 작성

<img width="498" alt="dj_181" src="https://user-images.githubusercontent.com/86648892/212547731-c4abdd82-0efa-43de-b5b6-73b6a588e3bc.png">

<img width="553" alt="dj_182" src="https://user-images.githubusercontent.com/86648892/212547727-b3db06a2-a500-448e-9b71-cfa3eed85c31.png">

### profile 템플릿으로 이동할 수 있는 하이퍼링크 작성

<img width="1069" alt="dj_183" src="https://user-images.githubusercontent.com/86648892/212547722-d4e0b25b-6a59-40fc-a703-3f6241d41e61.png">

<img width="1065" alt="dj_184" src="https://user-images.githubusercontent.com/86648892/212547719-8524bedc-cb15-4f51-8c47-8fb9467add67.png">

### 2. Follow 구현

### 모델 관계 설정

<img width="1092" alt="dj_185" src="https://user-images.githubusercontent.com/86648892/212547715-1457bffd-f9bf-4463-8f14-1082f398c070.png">

- 참조할 때 이름은 followings
- followings 당하는 입장에서 역참조는 followers
- migration 진행
- 생성된 중개 테이블 확인

<img width="574" alt="dj_186" src="https://user-images.githubusercontent.com/86648892/212547713-0728164b-2e05-4426-9a7d-9e87d65a02eb.png">

### url 및 view 함수 작성

<img width="897" alt="dj_187" src="https://user-images.githubusercontent.com/86648892/212547709-a8143bf5-526c-4991-ae33-2f3b5330f74d.png">

<img width="893" alt="dj_188" src="https://user-images.githubusercontent.com/86648892/212547704-186239f6-6034-497c-be86-040912fb44ec.png">

### 프로필 유저의 팔로잉, 팔로워 수 & 팔로워, 언팔로우 버튼 작성

<img width="931" alt="dj_189" src="https://user-images.githubusercontent.com/86648892/212547701-312080a9-efc5-4d96-9aef-774960b70c0f.png">

### 데코레이터 및 is_authenticated 추가

<img width="830" alt="dj_190" src="https://user-images.githubusercontent.com/86648892/212547697-71d002b3-cb8d-4f5f-8dec-64974165e521.png">
