## Migrations

---

- 작성한 모델의 클래스를 실제 데이터베이스에 반영하는 과정

- models.py에 작성한 것은 테이블의 스키마, migrations 파일들은 DB에 직접 만들 테이블의 설계도

- makemigrations을 통해 설계도를 생성하고, migrate를 통해 설계도를 DB에 동기화

### makemigrations

- `python manage.py makemigrations appName`

- 설계도 생성

### migrate

- `python manage.py migrate appName`

- 설계도를 DB에 반영

### sqlmigrate

- `python manage.py sqlmigrate appName migrationFileName`

- 해당 migration 파일이 SQL문으로 어떻게 해석될지 미리 확인

### showmigrations

- `python manage.py showmigrations`

- migration 파일들이 migrate 됐는지 안됐는지 여부를 확인하는 용도

### 추가 필드 정의

- models.py에 변경사항이 생긴다면 추가 migration 진행

- 설계도를 확인하면 `dependencies`에서 의존성을 확인할 수 있음
    - 새로운 클래스를 생성하는 경우 이전 설계도와 의존성 없음
    - 의존성이 있는 경우 추가되는 컬럼에 대한 기본값 설정 필요

- shell에서 직접 기존 데이터에서 추가되는 컬럼에 대한 값을 정할 수도 있고, 혹은 models.py에서 추가되는 컬럼에 대한 기본값을 설정
