## Model Class and Fields

---

### Model Class

- Django는 Model을 통해 데이터를 저장, 접속 및 관리하는 등 웹 어플리케이션의 데이터를 구조화하고 조작함

- 일반적으로 각각의 모델은 하나의 DB 테이블에 매핑
    - 테이블을 생성하는 경우 `id` 컬럼은 Django가 자동으로 생성
    - 각 모델은 `django.models.Model` 클래스를 상속

```python
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 객체 출력용 메서드
    def __str__(self):
        return self.title

# 기존 데이터베이스와 연결하는 경우
# db_column을 통해 속성과 연관된 Table의 Column 지정
class Albums(models.Model):
    albumid = models.AutoField(db_column='AlbumId', primary_key=True)
    title = models.TextField(db_column='Title')
    artistid = models.ForeignKey('Artists', models.DO_NOTHING, db_column='ArtistId')

    # 모델의 메타데이터 정의
    # managed를 False로 지정하면 Django가 이 모델에 대해 데이터베이스 테이블을 생성하거나 삭제하지 않도록 설정
    # db_table을 통해 모델과 연관된 DB Table 지정
    class Meta:
        managed = False
        db_table = 'albums'
```

### Model Field

- https://docs.djangoproject.com/ko/4.2/ref/models/fields/#model-field-types

- ModelField를 통해 속성의 타입을 지정

- 필요 시 옵션 추가

<p align="center">
    <img width="600" alt="modelfields" src="https://github.com/zacinthepark/TIL/assets/86648892/77b55f9f-fe8f-412c-8636-888999f626fe">
</p>

#### 문자열 필드

- CharField
    - SQL문으로 변환 시 데이터 타입이 VARCHAR로 지정됨
    - CharField는 가변길이 문자열이 저장되기에 CharField 생성 시 문자열의 최대 길이값을 반드시 지정
    - `CharField(max_length=숫자)`

- TextField
    - SQL문으로 변환 시 데이터 타입이 TEXT로 지정됨
    - 길이에 제한이 없는 문자열을 저장하기 위해 사용함

- SlugField
    - slug를 저장하기 위한 필드
    - slug는 친화적인 URL을 만들기 위한 문자, 숫자, underscore, hyphen으로 구성된 짧은 문자열
    - 예를 들어 `http://www.example.com/blog/1`보다 `http://www.example.com/blog/iceland-aurora`가 더 이해하기 쉬운 URL이며, 'iceland-aurora'는 slug

- EmailField
    - SQL문으로 변환 시 데이터 타입이 varchar(254)로 지정됨
    - 입력된 문자열은 Email 형식

- URLField
    - SQL문으로 변환 시 데이터 타입이 varchar(200)로 지정됨
    - 입력된 문자열은 `IP4/IP6` 또는 도메인 이름의 형식

- UUIDField
    - SQL문으로 변환 시 데이터 타입이 varchar(32)로 지정됨
    - 입력된 문자열은 'd6e003a9-ada5-4e50-9913-9e459dd505f9'와 같은 형식

- GenericIPAddressField
    - SQL문으로 변환 시 데이터 타입이 varchar(39)로 지정됨
    - 입력된 문자열은 '192.0.2.30'과 같은 IP4, '2a02:42fe::4'와 같은 IP6 형식

#### 날짜 및 시간 필드

- DateField
    - SQL문으로 변환 시 date 타입으로 지정되며 날짜 저장을 위해 사용됨
    - 필드값은 `datetime.date` 인스턴스로 처리

- DateTimeField
    - SQL문으로 변환 시 datetime 타입으로 지정되며 날짜와 시간을 저장하기 위해 사용됨
    - 필드값은 `datetime.datetime` 인스턴스로 처리

- TimeField
    - SQL문으로 변환 시 time 타입으로 지정되며 시간을 저장하기 위해 사용됨
    - 필드값은 `datetime.time` 인스턴스로 처리

- `auto_now` 옵션은 True 설정 시 데이터가 생성될 때의 날짜, 시간이 자동 저장됨

- `auto_now_add` 옵션은 True 설정 시 데이터가 수정될 때의 날짜, 시간이 자동 저장됨

#### Boolean 필드

- BooleanField
    - SQL문으로 변환 시 bool 타입으로 지정됨
    - true 또는 false 중 하나의 값만 저장하기 위해 사용

- NullBooleanField
    - SQL문으로 변환 시 bool 타입으로 지정됨
    - true 또는 false 중 하나의 값만 저장하기 위해 사용
    - BooleanField는 Null 값을 허용하지 않는 반면 NullBooleanField는 Null을 허용함

#### 숫자 필드

- AutoField
    - SQL문으로 변환 시 데이터 타입을 Integer로 지정됨
    - 필드의 값이 초기값 1부터 시작해서 새로운 레코드가 삽입될 때마다 1씩 증가된 값이 자동으로 저장됨
    - AutoField는 일반적으로 모델 클래스에서 선언해서 사용하기보단 마이그레이션 작업 시 자동으로 추가되어 사용함
    - 모델 클래스 선언시 기본키(primary key) 가 지정된 필드가 없는 경우에 마이그레이션 시 AutoField 타입의 필드가 자동 생성됨

- SmallAutoField
    - `1 ~ 32767` 사이의 값을 가진다는 것 외엔 AutoField와 동일

- BigAutoField
    - `1 ~ 9223372036854775807` 사이의 값을 가진다는 것 외엔 AutoField와 동일

- IntegerField
    - `-2147483648 ~ 2147483647` 사이의 정수값을 저장하기 위한 필드

- SmallIntegerField
    - `-32768 ~ 32767` 사이의 정수값을 저장하기 위한 필드

- BigIntegerField
    - `-9223372036854775808 ~ 9223372036854775807` 사이의 정수값을 저장하기 위한 필드

- PositiveBigIntegerField
    - `0 ~ 9223372036854775807` 사이의 정수값을 저장하기 위한 필드

- PositiveIntegerField
    - `0 ~ 2147483647` 사이의 정수값을 저장하기 위한 필드

- PositiveSmallIntegerField
    - `0 ~ 32767` 사이의 정수값을 저장하기 위한 필드

- FloatField
    - 파이썬에서 float 인스턴스로 표현되는 실수를 저장하기 위한 필드

- DecimalField
    - 파이썬에서 Decimal 인스턴스로 표현되는 숫자를 저장하기 위한 필드
    - 반드시 `decimal_places`와 `max_digits` 옵션 지정
        - `decimal_places`: 소수 자릿수 지정
        - `max_digits`: 숫자의 전체 자릿수

#### 파일 필드

- BinaryField
    - 파일의 원본(binary) 데이터를 저장하는 필드
    - 이 필드의 값은 bytes, bytearray 또는 memoryview 인스턴스로 표현
    - BinaryField를 사용하는 것은 DB에 파일을 저장하는 것이므로 사용 시 주의

- FileField
    - 사용자의 파일 업로드를 지원하기 위한 필드
    - 이 필드에 저장되는 데이터는 사용자가 업로드한 파일
    - FileField는 업로드한 파일을 `settings.MEDIA_ROOT` 값으로 지정된 디렉토리에 업로드된 파일을 저장해줌

- ImageField
    - FileField를 상속받으며 사용자가 업로드한 파일이 유효한 이미지 파일인지 유효성을 체크함

- FilePathField
    - 사용자가 업로드한 파일이 아니라 이미 파일 시스템에 있는 파일을 다루기 위해 사용
    - FilePathField 생성 시 반드시 `path` 옵션을 지정
    - `path` 옵션에는 필드에서 사용할 파일이 있는 디렉토리를 지정

```python
import os.path
from django.conf import settings

def images_path():
    return os.path.join(settings.LOCAL_FILE_DIR, 'images')

class MyModel(models.Model):
    file = models.FilePathField(path=images_path)

```

### Model Field Options

#### 필드 제약 조건

- null
    - False or True
    - 기본값은 False
    - `null=False`라면 반드시 값이 입력되어야하는 필드

- blank
    - False or True
    - 기본값은 False

- default
    - 필드의 기본값 지정
    - 입력된 값이 존재하지 않을 경우 지정한 default 값으로 필드의 값이 저장됨

- unique
    - 필드값의 중복 허용 여부
    - `unique=True`로 지정된 필드의 값은 테이블에서 유일해야함

- unique_for_date
    - DateField 또는 DateTimeField 객체의 이름을 지정
    - 지정한 날짜 및 시간 객체에 따라 unique함을 보장

- primary_key
    - 모델의 기본키를 지정
    - `primary_key=True`로 지정하면 자동으로 `null=False`와 `unique=True` 옵션이 설정됨

- choices
    - 필드에 입력되는 값을 제한하기 위해 사용
    - 입력할 수 있는 값들을 시퀀스 객체의 요소로 지정

- validators
    - 필드에 입력된 값의 유효성을 확인하기 위해 별도의 함수를 정의하고, 정의된 함수를 필드값이 입력될 때 실행하기 위해 사용하는 옵션

#### DB 정보

- db_column
    - 기본적으로 모델의 필드 이름이 DB의 컬럼 이름으로 사용됨
    - db_column 지정 시 DB의 컬럼 이름을 모델의 필드 이름과 다르게 지정 가능

- db_index
    - `db_index=True`로 지정하면 필드에 대한 DB Index가 생성됨

#### Form 정보

- editable
    - `editable=False`로 지정된 필드는 HTML Form에서 비활성화되어 표시됨

- error_messages
    - 모델의 필드값을 HTML Form에서 입력받을 때 유효하지 않은 값을 입력한다면 출력할 오류 메세지를 지정

- help_text
    - 모델의 필드값을 입력받기 위한 HTML Form의 위젯을 생성할 때 함께 출력할 메세지를 지정
    - 필드에 입력할 값에 대한 도움말을 지정

- verbose_name
    - 모델의 필드값을 입력받기 위한 HTML Form 위젯의 레이블을 지정
