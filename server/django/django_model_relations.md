## Model Relations

---

### 관계 설정

- 1:N 관계
    - ForeignKey
    - - 한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 한 개와 관련된 경우

- 1:1 관계
    - OneToOneField
    - - 한 테이블의 레코드 하나가 다른 테이블의 레코드 단 한 개와 관련된 경우

- M:N 관계
    - ManyToManyField
    - 한 테이블의 0개 이상의 레코드가 다른 테이블의 0개 이상의 레코드와 관련된 경우

### Foreign Key(to, on_delete, **options)

- 1:N 관계에서 1에 해당하는 모델명을 지정

- 참조 무결성을 위해 참조하는 값이 부모 테이블의 Primary Key일 필요는 없지만, 유일한 값이어야 함

- `on_delete`
    - 필수 옵션
    - 외래 키가 참조하는 객체가 사라졌을 때, 외래 키를 가진 객체를 어떻게 처리할지 정의
    - `CASCADE`: 참조 인스턴스 삭제 시 함께 삭제
    - `PROTECT`: 참조 인스턴스 삭제 시 ProtectedError를 발생시켜 삭제를 방지
    - `RESTRICT`: 참조 인스턴스 삭제 시 IntegrityError를 발생시켜 삭제를 방지
    - `SET_NULL`: 참조 인스턴스 삭제 시 `null=True` 옵션이 설정된 경우에 null 값으로 변경
    - `SET_DEFAULT`: 참조 인스턴스 삭제 시 default 옵션에 지정한 값으로 변경
    - `SET()`: set의 인자로 함수를 지정
        - 참조 인스턴스 삭제 시인자로 지정한 함수를 호출하여 반환값으로 참조 필드값을 변경
    - `DO_NOTHING`: 참조 인스턴스 삭제 시 어떠한 작업도 하지 않음
        - DB에 따라 참조 무결성 오류가 발생할 수 있음

- 테이블명
    - appName_modelName

- N에 해당하는 모델의 경우 fieldName_id 컬럼이 생성됨

### OneToOneField(to, on_delete, **options)

- 1:1 관계를 갖는 모델명을 지정

- on_delete
    - 필수 옵션
    - 참조하는 인스턴스 삭제 시 처리 방식 지정

- `place = models.OneToOneField(Place, on_delete=models.CASCADE, primary_key=True)`
    - `primary_key=True` 설정 시 Django가 기본적으로 생성해주는 `id` AutoField를 생성하지 않고 place를 기본 키 필드로 사용

### ManyToManyField(to, **options)

- 다대다 관계를 갖는 모델명을 지정

- ManyToManyField는 중개 테이블을 자동으로 생성함

#### DB에서의 표현

- 중개 테이블명
    - appName_modelName_fieldName
    - `db_table` arguments를 활용하여 중개 테이블명을 변경할 수도 있음

- 중개 테이블 컬럼명
    - id
    - sourceModel_id
    - targetModel_id

#### ManyToManyField Options

```python
from django.db import models

class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'

# ManyToManyField
class Patient(models.Model):
    doctors = models.ManyToManyField(Doctor, related_name='patients', through='Reservation')
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'

# ManyToManyField extra data
class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptom = models.TextField()
    reserved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'

```

- `related_name`
    - 역참조 시 manager name

- `through`
    - 중개 테이블을 수동으로 지정하려는 경우 `through` 옵션을 사용하여 사용하려는 중개 테이블을 나타내는 Django 모델 지정 가능
    - 일반적인 용도는 중개 테이블에 extra data를 추가하여 다대다 관계와 연결하려는 경우
    - ManyToManyField를 조회할 때 해당 중개 테이블을 '통해서' 조회하겠다는 뜻
    - `add()`할 경우 `through_defaults={'key': 'value'}` argument 필요
        - `patient2.doctors.add(doctor1, through_defaults={'symptom': 'flu'})

- `symmetrical`
    - ManyToManyField가 동일한 모델(on self)을 가리키는 정의에서만 사용
    - 재귀 참조, self 참조
    - 기본값은 True
        - set 매니저를 추가하지 않음
        - source 모델 인스턴스가 target 모델 인스턴스를 참조하면 자동으로 target 모델 인스턴스도 source 모델 인스턴스를 참조
        - 쉽게 말해 1-2의 관계가 추가된다면, 2-1의 관계도 추가됨
    - 대칭을 원하지 않는 경우 False로 설정

```python
from django.db import models

class Person(models.Model):
    friends = models.ManyToManyField('self')
    # friends = models.ManyToManyField('self', symmetrical=False)

```

#### ManyToManyField Methods

- `add()` , `remove()` , `create()` , `clear()` , `set()`, ...

- `add()`
    - 지정된 객체를 관련 객체 집합에 추가
    - 이미 존재하는 관계에 사용하면 관계가 복제되지 않음
    - 모델 인스턴스, 필드 값(pk)을 인자로 허용

- `remove()`
    - 관련 객체 집합에서 지정된 모델 개체를 제거
    - 내부적으로 `QuerySet.delete()` 를 사용하여 관계가 삭제됨
    - 모델 인스턴스, 필드 값(pk)을 인자로 허용
