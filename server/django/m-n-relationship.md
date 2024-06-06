## Django M:N Relationship

---

- [ManyToManyField](#manytomanyfieldto-options)
- [M : N (Article-User) (Likes)](#m--n-article-user)
- [M : N (User-User) (Follows)](#m--n-user-user)

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
