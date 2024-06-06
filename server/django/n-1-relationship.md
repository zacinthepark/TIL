## Django N:1 Relationship

---

- [N : 1 (Comment - Article)](#n--1-comment---article)
- [N : 1 (Article - User)](#n--1-article---user)
- [N : 1 (Comment - User)](#n--1-comment---user)


## N : 1 (Comment - Article)

---

- Comment(N) - Article(1)
- Comment 모델과 Article 모델 간 관계 설정
- “0개 이상의 댓글은 1개의 게시글에 작성될 수 있음”

<img width="1068" alt="dj_127" src="https://user-images.githubusercontent.com/86648892/212546962-d8c3df94-0bf4-4c13-bfdb-d6fd8085367e.png">

### Comment 모델 정의

<img width="815" alt="dj_128" src="https://user-images.githubusercontent.com/86648892/212546960-57b2b1a5-8516-432e-9a8d-45ab168403dd.png">

- 외래 키 필드는 ForeignKey 클래스를 작성하는 위치와 관계없이 필드의 마지막에 작성됨
- `ForeignKey()` 클래스의 인스턴스 이름은 참조하는 모델 클래스 이름의 단수형(소문자)으로 작성하는 것을 권장
- migration 과정 진행

<img width="1068" alt="dj_129" src="https://user-images.githubusercontent.com/86648892/212546959-901cce13-1e0e-4a21-a31b-9f54c93ea9f8.png">

<img width="1046" alt="dj_130" src="https://user-images.githubusercontent.com/86648892/212546958-c2b7c241-b9cd-45dc-ac8c-5f55dd9a790f.png">

<img width="1031" alt="dj_131" src="https://user-images.githubusercontent.com/86648892/212546957-46ab927b-8bec-4c80-8105-3f5b87e3b176.png">

<img width="1025" alt="dj_132" src="https://user-images.githubusercontent.com/86648892/212546956-631d339f-286c-46c0-8803-82cb36939db4.png">

<img width="1030" alt="dj_133" src="https://user-images.githubusercontent.com/86648892/212546954-72bf657e-4e90-41c1-a457-54af27b340aa.png">

### Comment CRUD 구현

### 1. CREATE

- CommentForm 작성
  - 외래 키 필드는 사용자로부터 받는 입력이 아니므로 출력에서 제외
- 기존의 ArticleForm 클래스의 인스턴스명을 `form` 으로 작성했기에 헷갈리지 않도록 `comment_form` 으로 작성
- 출력에서 제외된 외래 키의 경우 url에서 `variable routing` 을 활용하여 받아온 pk값을 활용
- `save(commit=False)` 옵션 활용
  - “Create, but don’t save the new instance”
    - 아직 데이터베이스에 저장되지 않은 인스턴스를 반환
    - 저장하기 전에 객체에 대한 사용자 지정 처리를 수행할 때 유용하게 사용
  - commit 옵션을 활용해 DB에 저장되기 전 comment 객체에 article 객체 저장하기

<img width="605" alt="dj_134" src="https://user-images.githubusercontent.com/86648892/212546952-62aaed63-6e6e-4ff6-85b5-38d784e89232.png">

<img width="717" alt="dj_135" src="https://user-images.githubusercontent.com/86648892/212546951-b6de9101-d9b6-453f-adf5-d7b8a86426fa.png">

<img width="562" alt="dj_136" src="https://user-images.githubusercontent.com/86648892/212546950-d099bacf-1862-4ca7-ae28-804bd4e9e0cb.png">

<img width="560" alt="dj_137" src="https://user-images.githubusercontent.com/86648892/212546949-40d98ce4-ba67-4f74-9161-cdcac7eaadf2.png">

### 2. READ

- 작성한 댓글 목록 출력하기
- 특정 article에 있는 모든 댓글을 가져온 후 context에 추가
- detail 템플릿에서 댓글 목록 출력하기

<img width="723" alt="dj_138" src="https://user-images.githubusercontent.com/86648892/212546948-e64c7719-527d-4ca0-afc1-0359ff91df7a.png">

<img width="723" alt="dj_139" src="https://user-images.githubusercontent.com/86648892/212546947-f749bcae-b663-4ff8-9837-1911b56d5c8e.png">

### 3. DELETE

- 댓글 삭제 구현하기
- 댓글을 삭제할 수 있는 버튼을 각각의 댓글 옆에 출력될 수 있도록 함

<img width="1154" alt="dj_140" src="https://user-images.githubusercontent.com/86648892/212546945-88fc2e31-b48e-4e90-aa17-e7f68412c031.png">

<img width="710" alt="dj_141" src="https://user-images.githubusercontent.com/86648892/212546943-ddfed818-4ea8-4950-bc36-8d2cd3f195dc.png">

<img width="1026" alt="dj_142" src="https://user-images.githubusercontent.com/86648892/212546939-04c8bad3-623c-4dd1-8a41-c3ee25b536c2.png">

### 4. UPDATE

- 댓글 수정은 구현하지 않음
- 댓글 수정을 구현할 경우 게시글 수정 페이지가 필요했던 것처럼 댓글 수정 페이지가 필요
- 하지만 일반적으로 댓글 수정은 수정 페이지로의 이동없이 현재 페이지를 유지한 상태로 댓글 작성 Form 부분만 변경되어 수정할 수 있도록 함
- 이처럼 페이지의 일부 내용만 업데이트하는 것은 JavaScript의 영역이기 때문에 JavaScript를 학습한 후 별도로 진행

### DTL(Django Template Language)과 QuerySet API를 활용한 추가 댓글 구현 사항

### 댓글 개수 출력하기

<img width="768" alt="dj_143" src="https://user-images.githubusercontent.com/86648892/212546934-3a161a94-3fe7-4288-b76d-273c8d44e032.png">

<img width="951" alt="dj_144" src="https://user-images.githubusercontent.com/86648892/212546930-87135284-fbee-403e-9cbd-5b38dccb1970.png">

### 댓글이 없는 경우 대체 컨텐츠 출력하기

<img width="1162" alt="dj_145" src="https://user-images.githubusercontent.com/86648892/212546925-90d84a12-d382-4864-998d-a70c5ef51533.png">

## N : 1 (Article - User)

---

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

### Article CRUD 구현

### 1. CREATE

- 인증된 회원의 게시글 작성 구현하기
- 작성하기 전 로그인을 먼저 진행한 상태로 진행
- ArticleForm의 출력 필드 수정
- 사용자로부터 키를 받아오는 것이 아닌 `save(commit=False)` 를 통해 request를 보내는 사용자의 정보를 저장

<img width="606" alt="dj_150" src="https://user-images.githubusercontent.com/86648892/212546914-cfa7d769-9db6-4eab-9f8a-444612069e17.png">

<img width="773" alt="dj_151" src="https://user-images.githubusercontent.com/86648892/212547213-17588ae1-d352-44ef-8c48-cbad2e457c2e.png">

### 2. DELETE

- 이제 게시글에 작성자 정보가 함께 들어있기 때문에 현재 삭제를 요청하려는 사람과 게시글을 작성한 사람을 비교하여 본인의 게시글만 삭제할 수 있도록 함

<img width="723" alt="dj_152" src="https://user-images.githubusercontent.com/86648892/212547212-bacff37d-662c-41d1-b0e3-9b65c8badd5c.png">

### 3. UPDATE

- 수정도 마찬가지로 수정을 요청하려는 사람과 게시글을 작성한 사람을 비교하여 본인의 게시글만 수정할 수 있도록 함
- 추가로 해당 게시글의 작성자가 아니라면, 수정 및 삭제 버튼을 출력하지 않도록 함

<img width="1046" alt="dj_153" src="https://user-images.githubusercontent.com/86648892/212547210-53984eb4-101a-4134-88ce-34cd100daa68.png">

<img width="928" alt="dj_154" src="https://user-images.githubusercontent.com/86648892/212547209-9fb5da4f-bfe3-401d-ba3e-aea72c348d30.png">

### 4. READ

- 게시글 작성자 출력
- index 템플릿과 detail 템플릿에서 각 게시글의 작성자 출력

<img width="670" alt="dj_155" src="https://user-images.githubusercontent.com/86648892/212547208-01f2ca1f-a5c7-4856-97b5-0d94f03432da.png">

<img width="483" alt="dj_156" src="https://user-images.githubusercontent.com/86648892/212547207-22992f2a-e007-4a67-a636-aad3e22ef4bc.png">

## N : 1 (Comment - User)

---

- Comment(N) - User(1)
- Comment 모델과 User 모델 간 관계 설정
- “0개 이상의 댓글은 1개의 회원에 의해 작성될 수 있음”
- Comment는 Article의 id, User의 id 2개의 ForeignKey를 가지게 됨
- 마찬가지로 migration 진행 및 NOT NULL 제약조건 해결 진행

<img width="1068" alt="dj_157" src="https://user-images.githubusercontent.com/86648892/212547204-5f5d654c-0de0-4569-924a-ba206e4df450.png">

<img width="1066" alt="dj_158" src="https://user-images.githubusercontent.com/86648892/212547202-5c51c9c7-b939-4bc1-a150-dece6c8f0cb5.png">

<img width="1073" alt="dj_159" src="https://user-images.githubusercontent.com/86648892/212547201-6ac030da-782e-4528-9ea9-5c4253c97556.png">

<img width="1069" alt="dj_160" src="https://user-images.githubusercontent.com/86648892/212547199-efc96456-2a57-4a9e-8362-5c45dcef9ccb.png">

### Comment CRUD 구현

### 1. CREATE

- 인증된 회원의 댓글 작성 구현하기
- 작성하기 전 로그인을 먼저 진행한 상태로 진행
- CommentForm 출력 필드 수정
- 사용자로부터 키를 받아오는 것이 아닌 `save(commit=False)` 를 통해 request를 보내는 사용자의 정보를 저장

<img width="607" alt="dj_161" src="https://user-images.githubusercontent.com/86648892/212547198-c074ae3f-5e7c-4759-abea-f024bd10d5a1.png">

<img width="778" alt="dj_162" src="https://user-images.githubusercontent.com/86648892/212547194-7b900712-8877-4e48-a699-aa6439763405.png">

### 2. READ

- detail 템플릿에서 각 게시글의 작성자 출력

<img width="1023" alt="dj_163" src="https://user-images.githubusercontent.com/86648892/212547192-01df4af7-fb52-4973-827b-88026c1c5e3b.png">

### 3. DELETE

- 이제 댓글에는 작성자 정보가 함께 들어있기 때문에 현재 삭제를 요청하려는 사람과 댓글을 작성한 사람을 비교하여 본인의 댓글만 삭제할 수 있도록 함
- 추가로 해당 댓글의 작성자가 아니라면, 삭제 버튼을 출력하지 않도록 함

<img width="776" alt="dj_164" src="https://user-images.githubusercontent.com/86648892/212547191-323eab57-2704-46a4-a23c-6913167a69c2.png">

<img width="1038" alt="dj_165" src="https://user-images.githubusercontent.com/86648892/212547190-433cc569-cf5a-43d7-9e71-0d8a95c019ae.png">

### 인증된 사용자에 대한 접근 제한하기

- `is_authenticated`
- `View Decorators`

### 인증된 사용자인 경우만 댓글 작성 및 삭제하기

<img width="923" alt="dj_166" src="https://user-images.githubusercontent.com/86648892/212547189-abb6d252-8fac-4cee-a595-0535c1deecce.png">

<img width="847" alt="dj_167" src="https://user-images.githubusercontent.com/86648892/212547186-bfeeaba8-ce4a-419e-8a9f-6daa54e6a986.png">

### 비인증 사용자는 CommentForm을 볼 수 없도록 하기

<img width="1035" alt="dj_168" src="https://user-images.githubusercontent.com/86648892/212547185-f65b0425-d54d-4624-b1fb-59d395f87102.png">

### 정리

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

### 참고 [Django Coding Style Guide about Imports]

- import와 관련한 coding style guide
- [https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/#imports](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/#imports)
- isort 사용
  - **`$** python -m pip install "isort >= 5.1.0"`
  - **`$** isort .`
    - `$ isort accounts/views.py`
- 띄어쓰기, 좌우 공백
- camelCase말고 언더바 사용
