## Form

---

### Django Form Class

- Form 클래스 기능
    - 입력 폼 HTML 생성: `as_table()`, `as_p()`, `as_ul()`
    - 입력 폼 값들에 대한 유효성 검증 및 값 변경: `is_valid()`
    - 검증 완료한 값들을 사전 타입으로 제공: `cleaned_data`

- 동일한 요청에 대해 GET, POST를 구분하여 다른 작업을 진행
    - GET 방식으로 요청 시: 입력 폼 출력
    - POST 방식으로 요청 시: 데이터 유효성을 검증
        - 검증 성공 시: 입력 데이터 저장 후 success URL로 이동
        - 검증 실패 시: error message와 함께 입력 폼으로 이동

- forms.py 파일에 작성하는 것을 관행적으로 권장
    - 사용자로부터 무엇을, 어떤 타입으로 받을지 고려하여 작성
    - `forms.Form` 클래스를 상속
    - 필드, 위젯 작성
    - 유효성 검사 로직 작성

### Form Fields and Widgets

- https://docs.djangoproject.com/en/4.2/ref/forms/fields/
- https://docs.djangoproject.com/en/5.0/ref/forms/widgets/

<p align="center">
    <img width="500" alt="form_fields" src="https://github.com/zacinthepark/TIL/assets/86648892/ecf04592-1d8b-445e-af16-9f8f873a0662">
</p>

- Form Fields
    - `forms.CharField()`
    - 사용자의 입력이 어떠한 입력값이어야하는지 정의
    - 입력에 대한 유효성 검사 로직을 처리

- Widgets
    - `forms.CharField(widget=forms.Textarea)`
    - input 요소의 세부적인 렌더링 조정을 처리

- 렌더링 과정
    - 사용자 입력
    - 유효성 검사 진행
    - 검사 후 데이터를 views의 context 형태로 템플릿에 전달
    - 템플릿에서 `{{ form.as_p }}`와 같이 Django Form Field를 HTML Form 태그로 변환
        - `as_p`: 각 필드를 p 태그로 감싸 렌더링
        - `as_ul`: 각 필드를 li 태그로 감싸 렌더링 (ul 태그는 직접 작성)
        - `as_table`: 각 필드를 tr 태그로 감싸 렌더링

### 유효성 검사

- `forms.Form` 객체에서 입력값의 유효성을 판단하기 위한 `is_valid()` 메서드를 제공하며 다음과 같이 동작함
    - 입력값에 대한 모든 validator를 호출한다
    - 유효한 입력값들은 `cleaned_data` 딕셔너리 요소로 저장한다
    - 모든 입력값이 유효하면 True를 반환한다
    - 유효하지 않은 입력값이 있다면 False를 반환하고 error message와 함께 입력 폼으로 이동한다

- 호출되는 validator
    - 필드에 내장된 Validator
    - validators 속성에 지정된 Validator
    - `clean_fieldName()` 메서드
    - `clean()` 메서드

- `is_valid()`의 결과가 False인 경우 form 인스턴스의 `errors` 속성에 값이 저장됨

#### 필드 내장 validator

<p align="center">
    <img width="600" alt="built_in_validators" src="https://github.com/zacinthepark/TIL/assets/86648892/57368141-4873-4400-a619-d765905c2b8e">
</p>

- `BinaryField.max_length`, `CharField.max_length` 속성은 MaxLengthValidator 사용

- `DecimalField`는 DecimalValidator 사용

- `EmailField`는 EmailValidator 사용

- `IntegerField`는 MinValueValidator와 MaxValueValidator가 -2147483648, 2147483648로 지정

- `URLField`는 URLValidator 사용

#### 사용자 정의 validator

```python
# value: 사용자 입력값
def temp_validator(value):
    # 유효성 검사

    # 유효성 검사 실패 시 raise ValidationError('error message')

    # 유효성 검사 성공시 반환값 없이 함수 종료

```

```python
# validator 지정
class modelName(models.Model):
    ...
    fieldName = ?Field(validators=[validator1, validator2, ...])

class formName(forms.Form):
    ...
    fieldName = ?Field(validators=[validator1, validator2, ...])

```

#### `clean_fieldName()`, `clean()`

```python
# member/forms.py
import re
from django import forms
from django.core.validators import MinLengthValidator
from django.forms import ValidationError

def username_validator(value):
    if re.search('[^A-Za-z0-9_@.+-]', value):
        raise ValidationError('8자 이상 150자 이하 문자ㅡ, 숫자, 그리고 @/./+/-/_만 가능합니다.')

class UserCreationForm(forms.Form):
    username = forms.CharField(label='사용자 이름', max_length=150, 
                                validators=[username_validator, MinLengthValidator(8)])
    password1 = forms.CharField(label='비밀번호', widget=forms.PasswordInput(), 
                                validators=[MinLengthValidator(8)])
    password2 = forms.CharField(label='비밀번호 확인', widget=forms.PasswordInput())

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 password1 != password2:
            raise ValidationError('비밀번호가 일치하지 않습니다.')
        
        return password2
    
    def clean(self):
        username = self.cleaned_data.get('username')
        password1 = self.cleaned_data.get('password1')

        if username and password1 and password1.startswith(username):
            raise ValidationError('사용자 이름과 비밀번호가 유사합니다.')
        
        return self.cleaned_data

```
