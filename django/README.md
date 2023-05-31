# Database Basics and Django

- [Django N:1 Relationship](#django-n1-relationship)
- [Django M:N Relationship](#django-mn-relationship)
- [Django REST Framework and Serializer](#django-rest-framework-and-serializer)



# Django N:1 Relationship

- A-many-to-one-relationship
- N : 1 (Comment - Article)
- N : 1 (Article - User)
- N : 1 (Comment - User)

---

# A-many-to-one-relationship

- 관계형 데이터베이스에서의 외래키 속성을 사용해 모델간 N:1 관계 설정하기
- 외래 키(ForeignKey)를 사용하여 RDB의 테이블 간 관계를 만들 수 있음
  - 관계(Relationship)란?
    - 테이블 간의 상호작용을 기반으로 설정되는 여러 테이블 간의 논리적인 연결

### 테이블 간 관계 예시

<img width="1176" alt="dj_124" src="https://user-images.githubusercontent.com/86648892/212546968-e41f595f-7e34-4ab4-8970-35446e7ecceb.png">

## RDB에서의 관계

1. `1:1`
   - One-to-one relationships
   - 한 테이블의 레코드 하나가 다른 테이블의 레코드 단 한 개와 관련된 경우
2. `N:1`
   - Many-to-one relationships
   - 한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 한 개와 관련된 경우
   - 기준 테이블에 따라 1:N, One-to-many relationships라고도 함
3. `M:N`
   - Many-to-many relationships
   - 한 테이블의 0개 이상의 레코드가 다른 테이블의 0개 이상의 레코드와 관련된 경우
   - 양쪽 모두에서 N:1 관계를 가짐

## Django Relationship Fields

1. `OneToOneField()`
   - A one-to-one relationship
2. `ForeignKey()`
   - A many-to-one relationship
3. `ManyToManyField()`
   - A-many-to-many relationship

---

## Foreign Key

- 외래 키 (외부 키)
- 관계형 데이터베이스에서 다른 테이블의 행을 식별할 수 있는 키
- 참조되는 테이블의 기본 키(Primary Key)를 가리킴
- 참조하는 테이블의 행 1개의 값은, 참조되는 측 테이블의 행 값에 대응됨
  - 즉, 참조하는 테이블의 행에는, 참조되는 테이블에 나타나지 않는 값을 포함할 수 없음
- 참조하는 테이블 행 여러 개가, 참조되는 테이블의 동일한 행을 참조할 수 있음
- **부모 테이블의 유일한 값을 참조**
  - **참조 무결성**
  - **외래 키의 값이 반드시 부모 테이블의 Primary Key일 필요는 없지만 유일한 값이어야 함**

### [참고] 참조 무결성

- 데이터베이스 관계 모델에서 관련된 2개의 테이블 간의 일관성을 말함
- 외래 키가 선언된 테이블의 외래 키 속성(열)의 값은 그 테이블의 부모가 되는 테이블의 기본 키 값으로 존재해야 함

## `ForeignKey(to, on_delete, **options)`

- A many-to-one relationship을 담당하는 Django의 모델 필드 클래스
- Django 모델에서 관계형 데이터베이스의 외래 키 속성을 담당
- 2개의 필수 위치 인자가 필요
  1. **참조하는 model class**
  2. `***on_delete` 옵션
     - 외래 키가 참조하는 객체가 사라졌을 때, 외래 키를 가진 객체를 어떻게 처리할지 정의
     - 데이터 무결성을 위해 매우 중요한 설정
     - `on_delete` 옵션 값
       - `CASCADE`
         - 부모 객체(참조된 개체)가 삭제되었을 때 이를 참조하는 객체도 삭제
       - `PROJECT`
         - 참조하는 객체가 있다면 참조되는 해당 객체를 못지우도록 설정
       - `SET_NULL`
         - 부모 객체가 삭제되었을 때 참조하는 객체의 값을 NULL로 설정
       - `SET_DEFAULT`
         - 부모 객체가 삭제되었을 때 참조하는 객체의 값을 설정한 기본값으로 대체

### [참고] 데이터 무결성 (Data Integrity)

- 데이터의 정확성과 일관성을 유지하고 보증하는 것
- 데이터베이스나 RDBMS의 중요한 기능
- 무결성 제한의 유형
  1. 개체 무결성 (Entity Integrity)
  2. 참조 무결성 (Referential Integrity)
  3. 범위 무결성 (Domain Integrity)

---

## Related Manager (관계 모델 참조)

- Related manager는 N:1 혹은 M:N 관계에서 사용가능한 문맥(context)
- Django는 모델 간 N:1 혹은 M:N 관계가 설정되면 `역참조` 할 때에 사용할 수 있는 manager를 생성
  - 이전에 모델 생성 시 `objects` 라는 매니저를 통해 queryset api를 사용했던 것처럼
    - Related manager를 통해 queryset api를 사용할 수 있게 됨
- N:1 관계에서 생성되늰 Related manager 이름은 참조하는 **“모델명_set”** 이름 규칙으로 만들어짐
  - `ForeignKey()` 설정 시 `related_name` 옵션을 통해 역참조 시 사용할 매니저 이름을 설정 가능
    - 작성 후 migration 과정 필요
    - 설정 시 기존의 `modelName_set` 은 더이상 사용할 수 없고, 대체됨

## 역참조

- 나를 참조하는 테이블(나를 외래 키로 지정한)을 참조하는 것
  - 본인을 외래 키로 참조 중인 다른 테이블에 접근하는 것
  - N:1에서는 1이 N을 참조하는 상황

<img width="1163" alt="dj_125" src="https://user-images.githubusercontent.com/86648892/212546967-3acdd5b9-c4b5-45df-81b3-a240c8f7b9e0.png">

<img width="1090" alt="dj_126" src="https://user-images.githubusercontent.com/86648892/212546965-bef1a122-25cb-402b-9978-f9f6229b8a2c.png">

---

# Referencing the User Model

## Django에서 User 모델을 참조하는 2가지 방법

1. `settings.AUTH_USER_MODEL`
   - 문자열을 반환
     - 반환값은 ‘accounts.User’ (문자열)
   - User 모델에 대한 외래 키 또는 M:N 관계를 정의할 때 사용
   - **`models.py`의 모델 필드에서 User 모델을 참조할 때 사용**
     - 장고 내부적인 동작순서에 따라 아직 유저 객체가 생성되지 않은 시점에서 `models.py` 가 임시로 참조할 수 있도록 문자열을 주는 것
2. `get_user_model()`
   - 객체를 반환
     - 반환값은 User Object (객체)
   - 현재 활성화(Active)된 User 모델을 반환
     - 커스터마이징한 User 모델이 있을 경우는 Custom User 모델, 그렇지 않으면 User를 반환
   - **`models.py` 가 아닌 다른 모든 곳에서 유저 모델을 참조할 때 사용**

---

# N : 1 (Comment - Article)

- Comment(N) - Article(1)
- Comment 모델과 Article 모델 간 관계 설정
- “0개 이상의 댓글은 1개의 게시글에 작성될 수 있음”

<img width="1068" alt="dj_127" src="https://user-images.githubusercontent.com/86648892/212546962-d8c3df94-0bf4-4c13-bfdb-d6fd8085367e.png">

## Comment 모델 정의

<img width="815" alt="dj_128" src="https://user-images.githubusercontent.com/86648892/212546960-57b2b1a5-8516-432e-9a8d-45ab168403dd.png">

- 외래 키 필드는 ForeignKey 클래스를 작성하는 위치와 관계없이 필드의 마지막에 작성됨
- `ForeignKey()` 클래스의 인스턴스 이름은 참조하는 모델 클래스 이름의 단수형(소문자)으로 작성하는 것을 권장
  - migration 과정 진행
    <img width="1068" alt="dj_129" src="https://user-images.githubusercontent.com/86648892/212546959-901cce13-1e0e-4a21-a31b-9f54c93ea9f8.png">

<img width="1046" alt="dj_130" src="https://user-images.githubusercontent.com/86648892/212546958-c2b7c241-b9cd-45dc-ac8c-5f55dd9a790f.png">

<img width="1031" alt="dj_131" src="https://user-images.githubusercontent.com/86648892/212546957-46ab927b-8bec-4c80-8105-3f5b87e3b176.png">

<img width="1025" alt="dj_132" src="https://user-images.githubusercontent.com/86648892/212546956-631d339f-286c-46c0-8803-82cb36939db4.png">

<img width="1030" alt="dj_133" src="https://user-images.githubusercontent.com/86648892/212546954-72bf657e-4e90-41c1-a457-54af27b340aa.png">

---

# Comment CRUD 구현

## CREATE

- CommentForm 작성
  - 외래 키 필드는 사용자로부터 받는 입력이 아니므로 출력에서 제외
- 기존의 ArticleForm 클래스의 인스턴스명을 `form` 으로 작성했기에 헷갈리지 않도록 `comment_form` 으로 작성
- 출력에서 제외된 외래 키의 경우 url에서 `variable routing` 을 활용하여 받아온 pk값을 활용
- `***save(commit=False)` 옵션 활용\*\*\*
  - “Create, but don’t save the new instance”
    - 아직 데이터베이스에 저장되지 않은 인스턴스를 반환
    - 저장하기 전에 객체에 대한 사용자 지정 처리를 수행할 때 유용하게 사용
  - commit 옵션을 활용해 DB에 저장되기 전 comment 객체에 article 객체 저장하기

<img width="605" alt="dj_134" src="https://user-images.githubusercontent.com/86648892/212546952-62aaed63-6e6e-4ff6-85b5-38d784e89232.png">

<img width="717" alt="dj_135" src="https://user-images.githubusercontent.com/86648892/212546951-b6de9101-d9b6-453f-adf5-d7b8a86426fa.png">

<img width="562" alt="dj_136" src="https://user-images.githubusercontent.com/86648892/212546950-d099bacf-1862-4ca7-ae28-804bd4e9e0cb.png">

<img width="560" alt="dj_137" src="https://user-images.githubusercontent.com/86648892/212546949-40d98ce4-ba67-4f74-9161-cdcac7eaadf2.png">

---

## READ

- 작성한 댓글 목록 출력하기
- 특정 article에 있는 모든 댓글을 가져온 후 context에 추가
- detail 템플릿에서 댓글 목록 출력하기

<img width="723" alt="dj_138" src="https://user-images.githubusercontent.com/86648892/212546948-e64c7719-527d-4ca0-afc1-0359ff91df7a.png">

<img width="723" alt="dj_139" src="https://user-images.githubusercontent.com/86648892/212546947-f749bcae-b663-4ff8-9837-1911b56d5c8e.png">

## DELETE

- 댓글 삭제 구현하기
- 댓글을 삭제할 수 있는 버튼을 각각의 댓글 옆에 출력될 수 있도록 함

<img width="1154" alt="dj_140" src="https://user-images.githubusercontent.com/86648892/212546945-88fc2e31-b48e-4e90-aa17-e7f68412c031.png">

<img width="710" alt="dj_141" src="https://user-images.githubusercontent.com/86648892/212546943-ddfed818-4ea8-4950-bc36-8d2cd3f195dc.png">

<img width="1026" alt="dj_142" src="https://user-images.githubusercontent.com/86648892/212546939-04c8bad3-623c-4dd1-8a41-c3ee25b536c2.png">

## UPDATE

- 댓글 수정은 구현하지 않음
  - 댓글 수정을 구현할 경우 게시글 수정 페이지가 필요했던 것처럼 댓글 수정 페이지가 필요
  - 하지만 일반적으로 댓글 수정은 수정 페이지로의 이동없이 현재 페이지를 유지한 상태로 댓글 작성 Form 부분만 변경되어 수정할 수 있도록 함
  - 이처럼 페이지의 일부 내용만 업데이트하는 것은 JavaScript의 영역이기 때문에 JavaScript를 학습한 후 별도로 진행

---

## DTL(Django Template Language)과 QuerySet API를 활용한 추가 댓글 구현 사항

### 댓글 개수 출력하기

<img width="768" alt="dj_143" src="https://user-images.githubusercontent.com/86648892/212546934-3a161a94-3fe7-4288-b76d-273c8d44e032.png">

<img width="951" alt="dj_144" src="https://user-images.githubusercontent.com/86648892/212546930-87135284-fbee-403e-9cbd-5b38dccb1970.png">

### 댓글이 없는 경우 대체 컨텐츠 출력하기

<img width="1162" alt="dj_145" src="https://user-images.githubusercontent.com/86648892/212546925-90d84a12-d382-4864-998d-a70c5ef51533.png">

---

# N : 1 (Article - User)

- Article(N) - User(1)
- Article 모델과 User 모델 간 관계 설정
- “0개 이상의 게시글은 1개의 회원에 의해 작성될 수 있음”
- Article 모델에 User 모델을 참조하는 외래 키 작성
  - migration 진행

<img width="1072" alt="dj_146" src="https://user-images.githubusercontent.com/86648892/212546924-3268cef1-0d14-4b05-8023-2b8c66154396.png">

<img width="1091" alt="dj_147" src="https://user-images.githubusercontent.com/86648892/212546923-3aefe3fb-9fc7-4c86-807d-93d3518bf9b5.png">

<img width="1071" alt="dj_148" src="https://user-images.githubusercontent.com/86648892/212546920-b2fa8f66-0adf-4aa7-a90c-3d00e0cd2514.png">

- 기본적으로 모든 컬럼은 `NOT NULL` 제약조건이 있기에 데이터가 없이는 새로 추가되는 외래 키 필드 user_id가 생성되지 않음
- 기본값을 어떻게 작성할지 선택
- 1을 입력하고 Enter 진행

<img width="1069" alt="dj_149" src="https://user-images.githubusercontent.com/86648892/212546918-e7f98d17-cd34-40b1-9b31-0e5d59031a9e.png">

- articel의 user_id에 어떤 데이터를 넣을 것인지 직접 입력
- 1 입력 후 Enter 진행
- 기존에 작성된 게시글은 모두 1번 회원이 작성한 것으로 처리됨

---

# Article CRUD 구현

## CREATE

- 인증된 회원의 게시글 작성 구현하기
- 작성하기 전 로그인을 먼저 진행한 상태로 진행
- ArticleForm의 출력 필드 수정
  - 사용자로부터 키를 받아오는 것이 아닌 `save(commit=False)` 를 통해 request를 보내는 사용자의 정보를 저장

<img width="606" alt="dj_150" src="https://user-images.githubusercontent.com/86648892/212546914-cfa7d769-9db6-4eab-9f8a-444612069e17.png">

<img width="773" alt="dj_151" src="https://user-images.githubusercontent.com/86648892/212547213-17588ae1-d352-44ef-8c48-cbad2e457c2e.png">

## DELETE

- 이제 게시글에 작성자 정보가 함께 들어있기 때문에 현재 삭제를 요청하려는 사람과 게시글을 작성한 사람을 비교하여 본인의 게시글만 삭제할 수 있도록 함

<img width="723" alt="dj_152" src="https://user-images.githubusercontent.com/86648892/212547212-bacff37d-662c-41d1-b0e3-9b65c8badd5c.png">

## UPDATE

- 수정도 마찬가지로 수정을 요청하려는 사람과 게시글을 작성한 사람을 비교하여 본인의 게시글만 수정할 수 있도록 함
- 추가로 해당 게시글의 작성자가 아니라면, 수정 및 삭제 버튼을 출력하지 않도록 함

<img width="1046" alt="dj_153" src="https://user-images.githubusercontent.com/86648892/212547210-53984eb4-101a-4134-88ce-34cd100daa68.png">

<img width="928" alt="dj_154" src="https://user-images.githubusercontent.com/86648892/212547209-9fb5da4f-bfe3-401d-ba3e-aea72c348d30.png">

## READ

- 게시글 작성자 출력
  - index 템플릿과 detail 템플릿에서 각 게시글의 작성자 출력

<img width="670" alt="dj_155" src="https://user-images.githubusercontent.com/86648892/212547208-01f2ca1f-a5c7-4856-97b5-0d94f03432da.png">

<img width="483" alt="dj_156" src="https://user-images.githubusercontent.com/86648892/212547207-22992f2a-e007-4a67-a636-aad3e22ef4bc.png">

---

# N : 1 (Comment - User)

- Comment(N) - User(1)
- Comment 모델과 User 모델 간 관계 설정
- “0개 이상의 댓글은 1개의 회원에 의해 작성될 수 있음”
- Comment는 Article의 id, User의 id 2개의 ForeignKey를 가지게 됨
- 마찬가지로 migration 진행 및 NOT NULL 제약조건 해결 진행

<img width="1068" alt="dj_157" src="https://user-images.githubusercontent.com/86648892/212547204-5f5d654c-0de0-4569-924a-ba206e4df450.png">

<img width="1066" alt="dj_158" src="https://user-images.githubusercontent.com/86648892/212547202-5c51c9c7-b939-4bc1-a150-dece6c8f0cb5.png">

<img width="1073" alt="dj_159" src="https://user-images.githubusercontent.com/86648892/212547201-6ac030da-782e-4528-9ea9-5c4253c97556.png">

<img width="1069" alt="dj_160" src="https://user-images.githubusercontent.com/86648892/212547199-efc96456-2a57-4a9e-8362-5c45dcef9ccb.png">

---

# Comment CRUD 구현

## CREATE

- 인증된 회원의 댓글 작성 구현하기
- 작성하기 전 로그인을 먼저 진행한 상태로 진행
- CommentForm 출력 필드 수정
  - 사용자로부터 키를 받아오는 것이 아닌 `save(commit=False)` 를 통해 request를 보내는 사용자의 정보를 저장

<img width="607" alt="dj_161" src="https://user-images.githubusercontent.com/86648892/212547198-c074ae3f-5e7c-4759-abea-f024bd10d5a1.png">

<img width="778" alt="dj_162" src="https://user-images.githubusercontent.com/86648892/212547194-7b900712-8877-4e48-a699-aa6439763405.png">

## READ

- detail 템플릿에서 각 게시글의 작성자 출력

<img width="1023" alt="dj_163" src="https://user-images.githubusercontent.com/86648892/212547192-01df4af7-fb52-4973-827b-88026c1c5e3b.png">

## DELETE

- 이제 댓글에는 작성자 정보가 함께 들어있기 때문에 현재 삭제를 요청하려는 사람과 댓글을 작성한 사람을 비교하여 본인의 댓글만 삭제할 수 있도록 함
- 추가로 해당 댓글의 작성자가 아니라면, 삭제 버튼을 출력하지 않도록 함

<img width="776" alt="dj_164" src="https://user-images.githubusercontent.com/86648892/212547191-323eab57-2704-46a4-a23c-6913167a69c2.png">

<img width="1038" alt="dj_165" src="https://user-images.githubusercontent.com/86648892/212547190-433cc569-cf5a-43d7-9e71-0d8a95c019ae.png">

---

## 인증된 사용자에 대한 접근 제한하기

- `is_authenticated`
- `View Decorators`

### 인증된 사용자인 경우만 댓글 작성 및 삭제하기

<img width="923" alt="dj_166" src="https://user-images.githubusercontent.com/86648892/212547189-abb6d252-8fac-4cee-a595-0535c1deecce.png">

<img width="847" alt="dj_167" src="https://user-images.githubusercontent.com/86648892/212547186-bfeeaba8-ce4a-419e-8a9f-6daa54e6a986.png">

### 비인증 사용자는 CommentForm을 볼 수 없도록 하기

<img width="1035" alt="dj_168" src="https://user-images.githubusercontent.com/86648892/212547185-f65b0425-d54d-4624-b1fb-59d395f87102.png">

---

## 정리

- 다대일 관계 (A many-to-one relationship)
  - Foreign Key
  - Django Relationship Fields
  - Related Manager
  - Referencing the User Model
- N : 1 모델 관계 설정
  - Comment - Article
  - Article - User
  - Comment - User
- 작성 과정
  - models에서 참조 키를 설정
  - forms에서 필드를 가리기
  - view 함수에서 동작을 처리
  - html에서 조건에 따라 출력 여부 설정

---

## 참고 [Django Coding Style Guide about Imports]

- import와 관련한 coding style guide
  - [https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/#imports](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/#imports)
  - isort 사용
    - **`$** python -m pip install "isort >= 5.1.0"`
    - **`$** isort .`
      - `$ isort accounts/views.py`
- 띄어쓰기, 좌우 공백
- camelCase말고 언더바 사용

---

# Django M:N Relationship

- Many to many relationship
- M:N (Article-User)
  - Like
- M:N (User-User)
  - Follow
- Fixtures

---

# Many-to-many relationship practice (patients-doctors)

### target and source model?

- target model
  - 관계 필드를 가지지 않은 모델
  - N:1에서는 1에 해당
- source model
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

---

# `ManyToManyField(to, **options)`

## ManyToManyField란

- 다대다 관계 설정 시 사용하는 모델 필드
- 하나의 필수 위치인자가 필요
  - M:N 관계로 설정할 모델 클래스
- 모델 필드의 RelatedManager를 사용하여 관련 개체를 추가, 제거, 혹은 만들 수 있음
  - `add()` , `remove()` , `create()` , `clear()` …

## 데이터베이스에서의 표현

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

## ManyToManyField Arguments

1. `related_name`
2. `through`
3. `symmetrical`

- blank=True
  - db의 유효성 검사와 관련없음 (값이 있어야함)
    - 사용자가 입력할 때 blank를 허용하는 것

### `related_name` argument

- target model이 source model을 참조할 때 사용할 manager name
- ForeignKey의 related_name과 동일

### `through` argument

- 중개 테이블을 수동으로 지정하려는 경우 `through` 옵션을 사용하여 사용하려는 중개 테이블을 나타내는 Django 모델을 지정할 수 있음
- 가장 일반적인 용도는 중개 테이블에 extra data를 추가하여 다대다 관계와 연결하려는 경우
- ManyToManyField를 조회할 때 해당 중개 테이블을 ‘통해서’ 조회를 하겠다는 뜻
- ManyToManyField에 자동으로 생성하는 것을 이제는 through 테이블로 대체하겠다는 뜻
- 예약을 주체로 예약을 생성하는 것도 가능하지만
  - 환자 혹은 의사를 주체로 관계를 추가하는 것이 더 합리적
- `add()` 시 `through_defaults={'key': 'value'}` argument 필요
  - `through_defaults` 값에 딕셔너리 타입으로 입력
  - ex) `patient2.doctors.add(doctor1, through_defaults={'symptom': 'flu'})`

### `symmetrical` argument

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

## ManyToManyField Related Manager

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

## Methods (ManyToManyField)

### `add()`

- “지정된 객체를 관련 객체 집합에 추가”
- 이미 존재하는 관계에 사용하면 관계가 복제되지 않음
- 모델 인스턴스, 필드 값(PK)을 인자로 허용

### `remove()`

- “관련 객체 집합에서 지정된 모델 개체를 제거”
- 내부적으로 `QuerySet.delete()` 를 사용하여 관계가 삭제됨
- 모델 인스턴스, 필드 값(PK)을 인자로 허용

## 중개 테이블 필드 생성 규칙

<img width="962" alt="dj_170" src="https://user-images.githubusercontent.com/86648892/212547771-e43b0d22-2295-4120-afc2-2fee1e39623e.png">

---

# M:N (Article-User)

- Article과 User의 M:N 관계 설정을 통한 좋아요 기능 구현하기

## Like 기능 구현하기

### 모델 관계 설정

<img width="968" alt="dj_171" src="https://user-images.githubusercontent.com/86648892/212547769-a727db36-6b1a-4798-9eb6-89078f77aa32.png">

- `like_users` 필드 생성 시 자동으로 역참조에는 `.article_set` 매니저가 생성됨
- 그러나 이전 N:1 (Aritcle-User) 관계에서 이미 해당 매니저를 사용 중
  - `user.article_set.all()`
    - 해당 유저가 작성한 모든 게시글 조회
  - **user가 작성한 글들(`user.article_set`)과 user가 좋아요를 누른 글(`user.article_set`)을 구분할 수 없게 됨**
  - 이런 경우 user와 관계된 ForeignKey 혹은 ManyToManyField 중 하나에 `related_name` 을 작성해야 함

<img width="1022" alt="dj_172" src="https://user-images.githubusercontent.com/86648892/212547765-07fbe386-c6af-4cdb-bb0c-3257d092b1d8.png">

- 생성된 중개 테이블 확인

<img width="485" alt="dj_173" src="https://user-images.githubusercontent.com/86648892/212547761-5dcf4b86-f09a-4cfa-bfd5-94886cd7c232.png">

<img width="1000" alt="dj_174" src="https://user-images.githubusercontent.com/86648892/212547757-9fa18eb3-8299-436d-82c5-96f30988daf6.png">

### LIKE 구현

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

---

# M:N (User-User)

- User 자기 자신과의 M:N 관계 설정을 통한 팔로우 기능 구현하기

## Profile 구현

- 자연스러운 follow 흐름을 위한 프로필 페이지를 먼저 작성

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

---

## Follow 구현

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

---


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

---
