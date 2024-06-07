## DB Settings

---

### DB 환경설정

- https://github.com/django/django/tree/main/django/db/backends

```python
# 환경변수를 통한 DB 설정
import os

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DB_ENGINE', 'django.db.backends.mysql'), 
        'HOST': os.environ['DB_HOST'], 
        'PORT': os.environ['DB_PORT'], 
        'NAME': os.environ['DB_NAME'], 
        'USER': os.environ['DB_USER'], 
        'PASSWORD': os.environ['DB_PASSWORD']
    }
}

# MySql 설정 (settings.py)
# pip install mysqlclient 진행 필요
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'HOST': 'localhost', # 데이터베이스 호스트
        'PORT': '3306', 
        'NAME': 'mydb', # 데이터베이스 DB명
        'USER': 'root', # 데이터베이스 유저
        'PASSWORD': 'admin123' # 데이터베이스 암호
    }
}

# SQLite DB 파일 복사
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': BASE_DIR / 'chinook.db'
    }
}

```

### DB Browser for SQLite

- https://sqlitebrowser.org/dl/

- DB Browser를 통해서 데이터베이스 열어서 확인 가능

### shell_plus

- Shell이란 운영체제 상에서 다양한 기능과 서비스를 구현하는 인터페이스를 제공하는 프로그램 (User ↔ Shell ↔ OS)

- Django Shell
    - `pip install django-extensions`
    - `python manage.py shell_plus`
        - django-extension이 제공하는 shell_plus
        - 자주 사용하는 모듈을 자동으로 import
        - 없다면 `python manage.py shell`

- shell 종료 시 `exit()`
