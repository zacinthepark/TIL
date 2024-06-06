## Django Settings

---

- https://www.djangoproject.com/
- https://docs.djangoproject.com/en/4.2/ref/
- https://github.com/django/django

### 가상환경 및 패키지 설치

- `python -m venv qa_system`: qa_system이라는 가상환경 생성

- `source ./venv/Scripts/activate`: 가상환경 활성화

- `pip install Django==4.2`: 장고 설치
    - `django-admin --version`: 버전 확인
    - `python -m django --version`: 버전 확인

- `pip install ipython`

- `pip install django-extensions`
    - settings.py 내 INSTALLED_APPS에 'django_extensions' 추가 필수

- `pip freeze > requirements.txt`: 패키지 목록 생성

- `pip install -r requirements.txt`: 패키지 목록 바탕으로 패키지 설치

### VSCode Extensions

- Python
- Django
- Django Template
- SQLite
- Excel Viewer

### .gitignore

- gitignore 설정으로 venv, db.sqlite3는 업로드하지 않음
- 가상환경 패키지 공유는 requirements.txt로 설정 대체
- migrations와 fixtures를 사용하여 앱에 초기 데이터 공유

### Fixtures

- Django가 데이터베이스로 가져오는 방법을 알고 있는 데이터 모음
    - Django가 데이터들을 하나의 구조화된 파일로 만듬
    - 다른 프로젝트에서 같은 모델 구조로 일치한다면
    - 그대로 import하여 초기 데이터를 넣은 상태로 시작 가능

- `app_name/fixtures/` 가 기본 경로
    - Django는 설치된 모든 app의 디렉토리에서 fixtures 폴더 이후의 경로로 fixtures 파일을 찾음

- fixtures 파일은 직접 만드는 것이 아니라 `dumpdata`를 사용하여 생성하는 것
    - `dumpdata`의 출력 결과물은 `loaddata`의 입력으로 사용됨

#### dumpdata (데이터 추출)

- 여러 모델을 하나의 json 파일로 만들 수 있음
    - `python manage.py dumpdata [app_name[.ModelName] [app_name[.ModelName]] ...]] > {filename}.json`
    - `>` 앞에서 나온 문자열을 json 파일로 만들겠다는 것

```python
# articles 앱에 있는 article 모델 데이터를 articles.json으로 추출하겠다는 뜻
# manage.py와 동일한 위치에 data가 담긴 articles.json 파일이 생성됨
# --indent 4 옵션 적용
python manage.py dumpdata --indent 4 articles.article > articles.json

# -Xutf8이라는 옵션을 통해 유니코드 형태로 인코딩 설정
python -Xutf8 manage.py dumpdata --indent 4 articles.comment > comment.json

# 3개의 모델을 하나의 json 파일로 dump
python manage.py dumpdata --indent 4 articles.article articles.comment accounts.user > data.json

# 모든 모델을 하나의 json 파일로 dump
python manage.py dumpdata --indent 4 > data.json
```

#### loaddata (데이터 로드)

- migrate 우선 진행

- 데이터 로드
    - `python manage.py loaddata articles.json comments.json users.json`

- 하나씩 로드하는 경우 외래키에 의한 관계를 고려하여 우선적으로 로드해야할 파일부터 로드
    - comment는 article에 대한 key 및 user에 대한 key가 필요하고
    - article은 user에 대한 key가 필요하다면
    - user, article, comment 순으로 데이터 로드를 진행해야 오류가 발생하지 않음

- encoding codec 관련 에러가 발생하는 경우
    -  dumpdata 시 `-Xutf8` 옵션 추가
    - 혹은 메모장으로 json 파일을 열어 다른 이름으로 저장 클릭 후 인코딩을 UTF8로 선택 후 저장

- dumpdata를 통해 만든 파일을 약속된 기본 경로에 넣어줘야 load할 때 읽을 수 있음
