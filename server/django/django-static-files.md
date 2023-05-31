## Django Static Files

---

- Managing static files
- Image Upload
- Image Resizing

## Managing static files

---

### 정적 파일(Static files)

- 응답할 때 별도의 처리없이 파일 내용을 그대로 보여주면 되는 파일
    - 사용자의 요청에 따라 내용이 바뀌는 것이 아니라 요청한 것을 그대로 보여주는 파일
- **파일 자체가 고정**되어있고, 서비스 중에도 추가되거나 **변경되지않고 고정**되어있음
    - ex) 웹 사이트는 일반적으로 이미지, JS, CSS와 같은 미리 준비된 추가 파일(움직이지 않는)을 제공해야함
- Django에서는 이러한 파일들을 “static file”이라함
    - Django는 `staticfiles` 앱을 통해 정적 파일과 관련된 기능을 제공

### Media File

- 미디어 파일
- 사용자가 웹에서 업로드하는 정적 파일 (user-uploaded)
- 유저가 업로드한 모든 정적 파일

### 웹 서버와 정적 파일

<img width="795" alt="dj_194" src="https://user-images.githubusercontent.com/86648892/212550666-31ef3168-0ec4-4878-9ebb-1212b44d9ff5.png">

- 웹 서버의 기본동작은
    - 특정 위치(URL)에 있는 자원을 요청(HTTP request)받아서
    - 응답(HTTP response)을 처리하고 제공(serving)하는 것
- 즉, “자원과 자원에 접근 가능한 주소가 있다”
    - ex) 사진 파일은 자원이고, 해당 **사진 파일을 얻기 위한 경로인 웹 주소(URL)**가 존재함
- 웹 서버는 요청받은 URL로 서버에 존재하는 정적 자원(static resource)을 제공함

### Static files 구성하기

### Django에서 정적 파일을 구성하고 사용하기 위한 몇 가지 단계

1. `INSTALLED_APPS` 에 `django.contrib.staticfiles` 가 포함되어 있는지 확인
2. settings.py에서 `***STATIC_URL***` 을 정의하기
3. 앱의 static 폴더에 정적 파일을 위치하기
    - ex) `my_app/static/sample_img.jpg`
4. 템플릿에서 static 템플릿 태그를 사용하여 지정된 경로에 있는 정적 파일의 URL 만들기

<img width="713" alt="dj_195" src="https://user-images.githubusercontent.com/86648892/212550665-41fc9fe7-3fb6-4083-80dc-f6269df3a357.png">

### Django template tag for static

- `{% load %}`
    - load tag
    - 특정 라이브러리, 패키지에 등록된 모든 템플릿 태그와 필터를 로드
- `{% static '' %}`
    - static tag
    - `STATIC_ROOT` 에 저장된 정적 파일에 연결

### Static files 관련 Core settings

1. `STATIC_ROOT`
2. `STATICFILES_DIRS`
3. `STATIC_URL`

### `1. STATIC_ROOT`

- Default: None
- Django 프로젝트에서 사용하는 모든 정적 파일을 한 곳에 모아 넣는 경로
- `collectstatic`
    - 배포를 위해 정적 파일을 수집하는 디렉토리의 절대 경로
    - admin 폴더에는 기본적으로 생성되는 admin 페이지 관련 내장 정적 파일들이 들어있음
- **개발 과정에서 settings.py의 DEBUG 값이 True로 설정되어 있으면 해당 값은 작용되지 않음**
- 실 서비스 환경(배포 환경)에서 Django의 모든 정적 파일을 다른 웹 서버가 직접 제공하기위해 사용
- 배포 환경에서는 Django를 직접 실행하는 것이 아니라
    - 다른 서버에 의해 실행되기 때문에
    - 실행하는 다른 서버는 Django에 내장되어 있는 정적 파일들을 인식하지 못함
    - 이것이 내장되어 있는 정적 파일들을 밖으로 꺼내는 이유

### [참고] collectstatic

<img width="1509" alt="dj_196" src="https://user-images.githubusercontent.com/86648892/212550663-536860d0-112f-4ae8-bd5c-cf478ef2e90a.png">

### [참고] 소프트웨어 배포(Deploy)

- 프로그램 및 어플리케이션을 서버와 같은 기기에 설치하여 서비스를 제공하는 것
- 클라우드 컴퓨팅 서비스(AWS, Google Cloud, MS Azure 등)에 프로그램 및 어플리케이션을 설치해 제공하는 것

<img width="605" alt="dj_197" src="https://user-images.githubusercontent.com/86648892/212550660-e73e86c1-f219-4ef3-b156-43398b82b525.png">

### `2. STATICFILES_DIRS`

- Default: [] (Empty List)
- `app/static/` 디렉토리 경로를 사용하는 것(기본 경로) 외에 추가적인 정적 파일 경로 목록을 정의하는 리스트
- 추가 파일 디렉토리에 대한 전체 경로를 포함하는 문자열 목록으로 작성되어야 함

<img width="474" alt="dj_198" src="https://user-images.githubusercontent.com/86648892/212550659-f2b42f85-4e79-45a8-8a5e-50311b38e521.png">

### `3. STATIC_URL`

- Default: None
- `STATIC_ROOT` 에 있는 정적 파일을 참조할 때 사용할 URL
- 개발 단계에서는 실제 정적 파일들이 저장되어 있는 `app/static/` 경로(기본 경로) 및 `STATICFILES_DIRS` 에 정의된 추가 경로들을 탐색
- 실제 파일이나 디렉토리가 아니며, URL로만 존재
- 비어있지 않은 값으로 설정한다면 반드시 slash(`/`)로 끝나야 함

<img width="412" alt="dj_199" src="https://user-images.githubusercontent.com/86648892/212550657-d11bea73-fd17-4b28-9fc1-5ee00f490d0a.png">

### Static files 가져오기

### 1. 기본 경로에 있는 static file 가져오기

- `articles/static/articles` 경로에 이미지 파일 배치

<img width="275" alt="dj_200" src="https://user-images.githubusercontent.com/86648892/212550656-13a6f064-2159-492f-884f-8d53eb567e6d.png">

- static tag를 사용해 이미지 파일 출력 및 확인

<img width="692" alt="dj_201" src="https://user-images.githubusercontent.com/86648892/212550655-2b3707c1-6fac-4f7d-a147-4e86892d04fd.png">

<img width="445" alt="dj_202" src="https://user-images.githubusercontent.com/86648892/212550653-ffb1656a-0a0c-4f4c-ba98-debf45dd945f.png">

### 2. 추가 경로에 있는 static file 가져오기

- **추가 경로 작성**

<img width="716" alt="dj_203" src="https://user-images.githubusercontent.com/86648892/212550651-be461fa8-7af6-40d6-bc1b-02c463943ef3.png">

- `static/` 경로에 이미지 파일 배치

<img width="288" alt="dj_204" src="https://user-images.githubusercontent.com/86648892/212550649-d9abe969-c6a4-45da-baf3-34e375326028.png">

- statig tag를 사용해 이미지 파일 출력 및 확인

<img width="757" alt="dj_205" src="https://user-images.githubusercontent.com/86648892/212550647-1db5d487-1ceb-4dfc-8cf4-6faf4d238969.png">

<img width="438" alt="dj_206" src="https://user-images.githubusercontent.com/86648892/212550646-d0b2a1f2-71af-47b7-ab87-9750708fd236.png">

### `STATIC_URL` 확인하기

- `http://127.0.0.1:8000/static/articles/sample_img_1.png`
    - Django가 해당 이미지를 클라이언트에게 응답하기 위해 만든 image url
    - 개발자 도구 이미지 Current Source 확인
        - img src의 경로에서 서버 내부적으로 인식하는 경로를 확인할 수 있음
    - Network 탭에서 Request URL 확인
        - 클라이언트에게 이미지를 응답하기 위한 요청 URL을 만든 것
    - **“STATIC_URL + static file 경로”**로 설정됨
        - `/static/` 이 STATIC_URL에서 정의한 부분
        - 클라이언트는 이 URL로 요청을 해야 해당 이미지를 볼 수 있음

<img width="707" alt="dj_207" src="https://user-images.githubusercontent.com/86648892/212550641-c7ec6f29-f0eb-4eec-80a5-161f8983e4d9.png">

- 정리하자면 서버에 올라가있는 static file 자원을 제공하려면 제공을 할 URL, 자원의 위치가 필요
    - 그 경로를 담당하는 것이 `STATIC_URL`
    - 그리고 이 주소를 static 태그를 통해 만들어낼 수 있다

## Image Upload

---

Django ImageField를 사용하여 사용자가 업로드한 정적 파일(미디어 파일) 관리하기

### `ImageField()`

- 이미지 업로드에 사용하는 모델 필드
- FileField를 상속받는 서브클래스로서 FileField의 모든 속성 및 메서드를 사용 가능함과 더불어
  - 사용자에 의해 업로드된 파일이 유효한 이미지인지 검사
- ImageField의 인스턴스는 DB에 이미지 덩어리로서 들어가지 않는다
  - 최대 길이가 100자인 **문자열로 DB에 생성**되며
    - **업로드된 파일의 경로가 저장**됨
    - max_length 인자를 사용하여 최대 길이를 변경할 수 있음

### `FileField()`

- `FileField(upload_to='', storage=None, max_length=100, **options)`
- 파일 업로드에 사용하는 모델 필드
- 2개의 선택 인자
  1. `upload_to`
  2. `storage`

### FileField와 ImageField를 사용하기 위한 단계

1. settings.py에 `MEDIA_ROOT` , `MEDIA_URL` 설정
2. `upload_to` 속성을 정의하여 업로드된 파일에 사용할 `MEDIA_ROOT` 의 하위 경로를 지정 (선택사항)
    - `upload_to`
        - 어떤 경로에 이 파일을 업로드할 것인지 문자열로 작성
        - `MEDIA_ROOT/path`
        - MEDIA_ROOT 이후의 경로(path)를 지정

### `MEDIA_ROOT`

- Default: ‘’ (Empty String)
- 사용자가 업로드한 파일(미디어 파일)들을 보관할 디렉토리의 절대경로
    - 즉, 사용자가 파일을 업로드했을 때 **실제 파일을 어디에 둘 것인지** 정의
- Django는 성능을 위해 업로드 파일은 데이터베이스에 저장하지 않음
    - 데이터베이스에 저장되는 것은 “파일 경로”
- MEDIA_ROOT는 STATIC_ROOT와 반드시 다른 경로로 지정해야함

<img width="385" alt="dj_208" src="https://user-images.githubusercontent.com/86648892/212550640-6c24274c-8225-4898-aac7-d73e7112cfd0.png">

### `MEDIA_URL`

- Default: ‘’ (Empty String)
- **MEDIA_ROOT에서 제공되는 미디어 파일을 처리하는 URL**
- 업로드된 파일의 주소(URL)를 만들어주는 역할
    - 웹 서버 사용자가 사용하는 public URL
- 비어있지 않은 값으로 설정한다면 반드시 slash(`/`)로 끝나야함
- MEDIA_URL은 STATIC_URL과 반드시 다른 경로로 지정해야함

<img width="392" alt="dj_209" src="https://user-images.githubusercontent.com/86648892/212550639-bd7c2d22-0461-4074-ac37-05d4a72e3007.png">

### 개발 단계에서 사용자가 업로드한 미디어 파일 제공하기

<img width="720" alt="dj_210" src="https://user-images.githubusercontent.com/86648892/212550634-8dc88134-5b1a-4eb6-841f-4780b9adaa50.png">

- 사용자로부터 업로드된 파일이 프로젝트에 업로드 되고나서, 실제로 사용자에게 제공하기 위해서는 업로드된 파일의 URL이 필요함
  - 업로드된 **파일의 URL** == `settings.MEDIA_URL`
  - 위 **URL을 통해 참조하는 파일의 실제 위치** == `settings.MEDIA_ROOT`

## CRUD

---

### 1. CREATE

### ImageField 작성

<img width="879" alt="dj_211" src="https://user-images.githubusercontent.com/86648892/212550858-c6da5b00-d1a5-4ec0-bc64-057a970f3c43.png">

### blank

- Default: False
- True인 경우 필드를 비워둘 수 있음
    - 이럴 경우 DB에는 ‘’(빈 문자열)이 저장됨
- 유효성 검사에서 사용됨 (is_valid)
    - “Validation-related”
    - 필드에 `blank=True` 가 있으면 form 유효성 검사에서 빈 값을 입력할 수 있음

### null

- Default: False
- True인 경우 Django는 빈 값을 DB에 NULL로 저장함
    - “Database-related”

### null 관련 주의사항

- ImageField에는 왜 blank 옵션을 줄까?
    - **“CharField, TextField와 같은 문자열 기반 필드에는 null 옵션 사용을 피해야함”**
        - 문자열 기반 필드들은 빈 문자열을 통해 빈 값이라는 의미를 가짐
        - 문자열 필드가 아닌 다른 필드들은 NULL이라는 값을 통해 빈 값이라는 의미를 가짐
        - 문자열 기반 필드에서 `null=True` 로 설정 시 데이터 없음에 대한 표현이 “빈 문자열”과 “NULL” 2가지 모두 가능하게 됨
            - “데이터 없음”에 대한 표현에 2개의 가능한 값을 갖는 것은 좋지 않음
            - 데이터베이스의 일관성에 어긋남
        - Django는 문자열 기반 필드에서 NULL이 아닌 빈 문자열을 사용하는 것이 규칙

### Pillow 설치

- ImageField를 사용하려면 반드시 Pillow 라이브러리가 필요
    - Pillow 설치없이는 makemigrations 실행 불가

<img width="475" alt="dj_212" src="https://user-images.githubusercontent.com/86648892/212550857-53a864c4-98f4-47ec-bd20-6d502dc3df2d.png">

### [참고] Pillow

- 광범위한 파일 형식 지원, 효율적이고 강력한 이미지 처리 기능을 제공하는 라이브러리
- 이미지 처리 도구를 위한 견고한 기반을 제공

### ArticleForm의 enctype 속성 변경

- 기본적인 form 태그는 파일을 업로드할 수 없음
  - 파일 또는 이미지 업로드 시에는 form 태그에 enctype(encoding type) 속성을 바꿔줘야 파일까지 업로드 가능

<img width="753" alt="dj_213" src="https://user-images.githubusercontent.com/86648892/212550856-70ef479a-ec82-4adc-9821-602793e17c97.png">

### [참고] form 태그의 enctype(인코딩) 속성 값

1. `application/x-www-form-urlencoded`
    - 기본값
    - 모든 문자 인코딩
2. `multipart/form-data`
    - 파일 및 이미지 업로드 시에 반드시 사용
    - 전송되는 데이터의 형식을 지정
    - `<input type="file">` 을 사용할 경우 사용
3. `text/plain`

### `request.FILES`

- 파일 및 이미지는 request의 POST 속성값으로 넘어가지 않고 FILES 속성값에 담겨 넘어감
    - 문자열 데이터만 `request.POST` 에 담김
    - 파일은 `request.FILES` 라는 속성값에 별도로 담김

<img width="582" alt="dj_214" src="https://user-images.githubusercontent.com/86648892/212550854-7d7e544b-9178-4f5f-ad7e-7d96070eb687.png">

### [참고] `request.FILES` 가 두번째 위치 인자인 이유

- BasModelForm Class의 생성자 함수에 2번째 위치 인자로 정의

<img width="281" alt="dj_215" src="https://user-images.githubusercontent.com/86648892/212550852-15cb7c7f-3e07-45ce-a42c-23d2b448a957.png">

### 이미지 업로드 후 확인

<img width="846" alt="dj_216" src="https://user-images.githubusercontent.com/86648892/212550850-26b64681-1fc6-46f6-adc1-39227806cd92.png">

<img width="833" alt="dj_217" src="https://user-images.githubusercontent.com/86648892/212550849-f32ab5b1-bc8f-4984-bbf2-fe1dccfc3265.png">

- 이미지 업로드에 성공했다면 자동으로 MEDIA_ROOT 경로에서 정의한 media 디렉토리가 생성됨
    - 테이블에는 파일이 아닌 이미지 경로가 저장됨
    - 이미지를 첨부한 경우 MEDIA_ROOT 경로에 이미지가 업로드됨
    - 이미지를 첨부하지 않으면 `blank=True` 속성으로 인해 빈 문자열이 저장됨
- 서로 다른 사용자가 같은 이름으로 파일을 업로드한다면 Django는 파일 이름 끝에 임의의 난수 문자열을 붙여서 구분 및 저장함

### 2. READ

### 업로드된 이미지 출력

- 업로드된 파일의 상대 URL은 Django가 제공하는 url 속성을 통해 얻을 수 있음

<img width="667" alt="dj_218" src="https://user-images.githubusercontent.com/86648892/212550847-c9e31954-228d-4352-9b97-8f8d5247be7b.png">

- `article.image.url`
    - 업로드 파일의 경로
- `article.image`
    - 업로드 파일의 파일 이름

### 출력 확인

<img width="744" alt="dj_219" src="https://user-images.githubusercontent.com/86648892/212550846-e3060818-93c8-4e79-8ba8-de94b565a1a9.png">

### MEDIA_URL 확인

<img width="700" alt="dj_220" src="https://user-images.githubusercontent.com/86648892/212550845-98a0edf3-9978-4f6a-a57e-28ab46c520be.png">

### 이미지를 업로드하지 않은 경우 detail 템플릿 출력 불가 문제 해결

- 이미지 데이터가 있는 경우에만 이미지를 출력하도록 처리

<img width="609" alt="dj_221" src="https://user-images.githubusercontent.com/86648892/212550843-9eb9e164-86d5-4108-81fe-fbf5e0f9315f.png">

### 3. UPDATE

- 이미지는 바이너리 데이터이기 때문에 텍스트처럼 일부만 수정 불가
    - 그러므로 새로운 사진으로 대체하는 방식을 사용

<img width="1481" alt="dj_222" src="https://user-images.githubusercontent.com/86648892/212550842-0e84412a-8397-441a-8e24-88bc97f391bf.png">

<img width="1162" alt="dj_223" src="https://user-images.githubusercontent.com/86648892/212550841-dbb65130-3e23-4245-8f38-80e57b9cca6b.png">

### upload_to argument

### `upload_to` argument를 활용하여 MEDIA_ROOT 이후 추가 경로 작성 가능

- ImageField는 업로드 디렉토리와 파일 이름을 2가지 방법을 통해 설정 가능
    1. 문자열 값 및 경로 지정 방법
    2. 함수 호출 방법

### 문자열 값 및 경로 지정 방법

<img width="768" alt="dj_224" src="https://user-images.githubusercontent.com/86648892/212550837-853ec6a5-9ead-408e-bed0-eba2eb65341e.png">

<img width="746" alt="dj_225" src="https://user-images.githubusercontent.com/86648892/212550836-7e29c8da-14f9-4193-a63a-3faf06edf1d3.png">

<img width="776" alt="dj_226" src="https://user-images.githubusercontent.com/86648892/212550835-7ddb9f6e-602d-4647-a0d0-70233f852311.png">

<img width="713" alt="dj_227" src="https://user-images.githubusercontent.com/86648892/212550833-947e1ede-7194-473f-a4eb-3645cca181bc.png">

- `upload_to` 에 작성하는 문자열을 MEDIA_ROOT 이후 추가 경로로 설정
- 단순 문자열 뿐만 아니라 파이썬 time 모듈의 `strftime()` 형식도 포함될 수 있으며
    - 이는 파일 업로드 날짜 및 시간으로 대체됨
- 변경 후 migration 과정 진행 필요

### 함수 호출 방법

<img width="776" alt="dj_228" src="https://user-images.githubusercontent.com/86648892/212550831-9bf5e146-69bc-4e47-a0df-642c458d50ce.png">

<img width="654" alt="dj_229" src="https://user-images.githubusercontent.com/86648892/212550830-2326d3b0-2700-44eb-870f-b1ae18838400.png">

- `upload_to` 는 독특하게 함수처럼 호출이 가능하며
    - 해당 함수가 호출되면서 반드시 2개의 인자를 받음
    1. `instance`
        - FileField가 정의된 모델의 인스턴스
        - 대부분 이 객체는 아직 데이터베이스에 저장되기 전이므로 아직 PK 값이 없을 수 있으니 주의
    2. `filename`
        - 기존 파일 이름
- 변경 후 migration 과정 진행 필요
- 상단의 결과는 username이 test인 회원이 업로드한 결과

## Image Resizing

---

- 실제 원본 이미지를 서버에 그대로 로드하는 것은 부담이 큼
- HTML <img> 태그에서 직접 사이즈를 조정할 수도 있지만
- 업로드 될 때 이미지 자체를 resizing하는 방법을 사용해볼 것

### django-imagekit 모듈 설치 및 등록

<img width="522" alt="dj_230" src="https://user-images.githubusercontent.com/86648892/212550829-9d805075-7830-44e9-885b-31ce189cf06e.png">

- django-imagekit
  - 이미지 처리를 위한 Django 앱
    - 썸네일, 해상도, 사이즈, 색깔 등을 조정할 수 있음

### 썸네일 만들기

2가지 방식으로 썸네일 만들기 진행

1. 원본 이미지 저장 x
    - `ProcessedImageField()`
2. 원본 이미지 저장 o
    - `ImageField()` 와 `ImageSpecField()`

### `ProcessedImageField()` (원본 이미지 저장 x)

- 원본 이미지를 저장하지 않는 방식
- `ProcessedImageField()` 의 parameter로 작성된 값들은 makemigrations 후에 변경이 되더라도 다시 makemigrations 해줄 필요없이 즉시 반영됨
- processors에 작성하는 여러 클래스는 해당 라이브러리 문서를 별도로 확인
    - [https://github.com/matthewwithanm/pilki](https://github.com/matthewwithanm/pilkit)

<img width="648" alt="dj_231" src="https://user-images.githubusercontent.com/86648892/212550828-434661a8-0cd7-4147-b556-e917dcbd5cf8.png">

<img width="741" alt="dj_232" src="https://user-images.githubusercontent.com/86648892/212550826-99487a5b-4ecb-4d08-a1cc-4b6393341380.png">

<img width="712" alt="dj_233" src="https://user-images.githubusercontent.com/86648892/212550824-01db136e-bf17-4e3b-9400-8b290eded2b5.png">

### `ImageField()` 와 `ImageSpecField()` (원본 이미지 저장 o)

<img width="758" alt="dj_234" src="https://user-images.githubusercontent.com/86648892/212550821-bd051fff-6b0e-44ad-a9e5-9fde87d8c0c0.png">

<img width="781" alt="dj_235" src="https://user-images.githubusercontent.com/86648892/212550818-cae79a66-c3af-4532-972d-47d0a56c9e2d.png">

<img width="867" alt="dj_236" src="https://user-images.githubusercontent.com/86648892/212550817-9dbecc54-bb44-412b-832d-6bd2fc5257c0.png">

<img width="845" alt="dj_237" src="https://user-images.githubusercontent.com/86648892/212550816-3d638d8a-1799-4cfd-8058-ccb53e8a814e.png">

<img width="801" alt="dj_238" src="https://user-images.githubusercontent.com/86648892/212550814-b9e91c26-81ff-4fbd-9f4f-b176ec7783ae.png">

- `ImageSpecField()`
  - 테이블에 생성되는 물리적인 column은 아니다
    - 출력을 할 때 CACHE에 생성해준다
      - CACHE?
        - 브라우저가 이미지를 memory cache에 들고있다가 사용
        - 이미 받았던 것은 서버로부터 받지 않고 캐시에서 사용
        - 시간이 빠름

### model 필드 예제 코드

```python
# models.py

from django.db import models
from django.conf import settings
from imagekit.processors import Thumbnail
from imagekit.models import ProcessedImageField, ImageSpecField

def articles_image_path(instance, filename):
    return f'images/{instance.user.username}/{filename}'

# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    content = models.TextField()
    image = models.ImageField(blank=True)
    # image = models.ImageField(blank=True, upload_to='images/')
    # image = models.ImageField(blank=True, upload_to='%Y/%m/%d/')
    # image = models.ImageField(blank=True, upload_to=articles_image_path)

    # 원본 저장하지 않는 방식 (Processed ImageField)
    # image = ProcessedImageField(
    #     blank=True,
    #     upload_to='thumbnails/',
    #     processors=[Thumbnail(200,300)],
    #     format='JPEG',
    #     options={'quality': 80},
    # )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 원본 저장하는 방식 (source image 필요)
    image_thumbnail=ImageSpecField(
        source='image',
        processors=[Thumbnail(200,300)],
        format='JPEG',
        options={'quality': 80},
    )

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
```
