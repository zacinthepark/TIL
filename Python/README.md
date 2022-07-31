# Python #1
- variable
- datatype
- 연산자
- 문자열 슬라이싱
---
# 프로그래밍이란?

### 프로그래밍의 정의

- 컴퓨터에게 일을 시키기 위해 프로그램을 만드는 행위
- 해야할 일을 순서대로 하도록 컴퓨터에게 명령을 내리는 것
- 컴퓨터는 기계어로 소통
    - 기계어란 0과 1 이진수로 소통함
- 소스코드(프로그래밍 언어로 작성된 프로그램) → 번역기(interpreter or compiler) → 컴퓨터 기계어

# 파이썬이란?

### 파이썬을 배워야 하는 이유

- 알고리즘 코딩 테스트에 유리
- 구현 코딩 테스트에 유리
    - 구현 코딩 테스트? 현업 능력 평가를 위해 서비스나 프로그램을 구현해보는 것
- AI 개발, 데이터 분석, 웹 프로그래밍, 업무 자동화 등 파이썬 활용 분야가 늘어나면서 많은 회사에서 도입 중

### 파이썬의 특징

- 인터프리터 언어
- 객체 지향 프로그래밍(Object Oriented Programming)
    - 현대 프로그래밍의 기본적인 설계 방법론으로 자리잡음
    - 파이썬은 객체 지향 언어이며, 모든 것이 객체로 구현되어 있음

### 파이썬 개발 환경

- IDE(Intergrated Development Environment)
    - 통합 개발 환경의 약자로 개발에 필요한 다양하고 강력한 기능들을 모아놓은 프로그램
- 문법 연습 → Jupyter Notebook, VS code
- 코드 → VS code
- 알고리즘 → Pycharm

# 코드 작성법

### 코드 스타일 가이드

- 파이썬은 공식 문서에서 권장해주는 스타일 가이드가 있음
- PEP8 [PEP 8 - Style Guide for Python](https://www.python.org/dev/peps/pep-0008/)
    - 들여쓰기
        - 문장을 구분할 때 중괄호{} 대신 indentation 사용
        - space 4번 or tab
        - 통일할 것
        - space 권장
    - 주석 (Comment)
        - 코드에 대한 설명
        - 주석을 다는 습관은 초기부터 들여야 할 중요한 습관
        - 한 줄 주석
            - ' # '
        - 여러 줄 주석
            - ‘’’ or “”” 으로 묶어주기

# 기초 문법

## 변수(Variable)

- ‘데이터 저장 → 처리’가 프로그래밍의 핵심!
- 데이터를 저장하기 위해 사용
- 추상화
    - 내부의 복잡한 작동 원리를 몰라도 사용할 수 있도록 함
    - 재사용, 수정, 코드 가독성 등 여러 부분에 중요
- 동일 변수에 다른 데이터를 언제든 할당(저장)할 수 있기에 ‘변수'라 불림

### 변수의 할당

- 할당 연산자(=)를 통해 값을 할당(assignment)
- 같은 값을 동시에 할당할 수 있음
- 각 변수의 값을 바꿔서 저장하기

```python
x, y = 10, 20
y, x = x, y
print(x, y) # 20 10
```

### 식별자(Identifier)

- 식별자의 이름은 영문 알파벳, 언더스코어(_), 숫자로 구성
- 첫 글자에 숫자 x
- 대소문자 구별
- 예약어(reserved words)는 사용할 수 없음 ex) if
- 내장 함수나 모듈 등의 이름도 사용할 수 없음 ex) print

### 연산자(Operator)

- 산술 연산자
    - '+' 덧셈
    - '-' 뺄셈
    - '*' 곱셉
    - '/' 나눗셈
    - '//' 몫
    - '**' 거듭제곱
    - '%' 모듈러 연산자
- 연산자의 우선순위는 기본적으로 수학의 우선순위와 같음

## 자료형(Datatype)

- 사용할 수 있는 데이터의 종류들을 자료형(Datatype)이라고 함

### Numeric Type(수치형)

- Int(정수, integer)
    - 여러 진수 표현 가능
        - 0b(2진수), 0o(8진수), 0x(16진수)를 숫자 앞에 붙이면 해당 진수 숫자로 인식
    
    ```python
    print(0b10) # 2
    print(0o30) # 24
    print(0x10) # 16
    ```
    
- Float(부동소수점, 실수, floating point number)
    - ‘부동’은 떠다닌다는 뜻
    - 컴퓨터는 2진수를 사용하는데, 사람은 10진법을 사용함
        - 10진수 0.1은 2진수로 표현하면 0.00011001100110011001100…같이 무한대로 반복
        - 무한대 숫자를 그대로 저장할 수 없어서 사람이 사용하는 10진법의 근사값만 표시
        - floating point round error
    - 해결법?
    
    ```python
    a = 3.2 - 3.1 # 0.10000000000000009
    b = 1.2 - 1.1 # 0.09999999999999987
    
    # 1. 임의의 작은 수 활용
    print(abs(a - b) <= (1e-10) # True
    
    # 2. python 3.5 이상
    import math
    print(math.isclose(a, b)) # True
    ```
    
- Complex(복소수, complex number)

### String Type

- 작은따옴표(’)나 큰따옴표(”)를 활용하여 표기
- 문자열을 묶을 때 동일한 문장부호 활용
- 소스코드 내 하나의 문장부호 선택하여 유지할 것
- 중첩 따옴표
    - 작은따옴표로 문자열 생성한 경우 → 문자열 안에서 큰따옴표로 표현
- 삼중 따옴표
    - ‘’’ ‘’’
        - 여러 줄 표현 or 문자열 안에서 큰따옴표, 작은따옴표 모두 사용하고 싶을 때
- Escape sequence
    - \n 줄 바꿈
    - \t 탭
    - \r 캐리지 리턴
    - \0 Null
    
    ```python
    print('철수 \'안녕\'') # 철수 '안녕'
    print('이 다음은 엔터. \n 그리고 탭\t탭')
    '''
    이 다음은 엔터.
     그리고 탭      탭
    '''
    ```
    
- 문자열 연산
    - 덧셈
        - String Concatenation
        - 공백없이 붙음
    - 곱셈
        - “Python” * 3은 PythonPythonPython
- String Interpolation
    - 문자열과 변수를 같이 쓰는 것
    
    ```python
    # 1. %-formatting
    name = 'Kim'
    score = 4.5
    
    print('Hello, %s' % name) # Hello, Kim
    print('내 성적은 %d' % score) # 내 성적은 4
    print('내 성적은 %f' % score) # 내 성적은 4.500000
    
    # 2. str.format()
    name = 'Kim'
    score = 4.5
    
    print('Hello, {}! 성적은 {}'.format(name, score))
    # Hello, Kim! 성적은 4.5
    
    # 3. f-strings: python 3.6+
    name = 'Kim'
    score = 4.5
    
    print(f'Hello, {name}! 성적은 {score}')
    # Hello, Kim! 성적은 4.5
    
    import datetime
    today = datetime.datetime.today()
    print(today) # 2022-07-08 16:04:15.200411
    
    print(f'오늘은 {today:%y}년 {today:%m}월 {today:%d}일')
    # 오늘은 22년 07월 08일
    
    pi = 3.141592
    print(f'원주율은 {pi:.3}. 반지름이 2일 때 원의 넓이는 {pi*2*2}')
    # 원주율은 3.14. 반지름이 2일 때 원의 넓이는 12.566368
    ```
    
    - 컴퓨터는 시간을 어떻게 이해하는가?
        - 1970년 1월 1일을 기준으로 시간을 숫자로 변환하여 인식
        - 이 숫자를 Timestamp라 함
        - 그리고 이것을 다시 사람이 이해할 수 있는 형식으로 다시 출력하여 보여주는 것

### None

- 파이썬 자료형 중 하나
- 값이 없음을 표현하기 위해 None 타입이 존재
- 일반적으로 반환 값이 없는 함수에서 사용하기도 함

### Boolean Type

- 논리 자료형으로 참과 거짓을 표현하는 자료형
- True / False
- 비교 / 논리 연산에서 활용됨
    - 비교 연산자
        - 주로 조건문에 사용
        - 결과는 True / False 값을 리턴함
        - '<' :   미만
        - '<=' :  이하
        - '>'  :  초과
        - '>=' :  이상
        - '==' : 같음
        - '!=' : 같지 않음
        - 'is' :  객체 아이덴티티(OOP)
        - 'is not' : 객체 아이덴티티가 아닌 경우
        
        ```python
        print(3 > 6) # False
        print(3.0 == 3) # True 언어마다 다름 파이썬의 경우 변환해서 True를 리턴
        print(3 >= 0) # True
        print('3' != 3) # True 문자열과 숫자이므로 다름
        print('Hi' == 'hi') # False 대문자와 소문자의 차이
        ```
        
    - 논리 연산자
        - 여러가지 조건이 있을 때
            - 모든 조건을 만족하거나(and), 여러 조건 중 하나만 만족해도 될 때(or) 특정 코드를 실행하고 싶을 때 사용
            - 일반적으로 비교 연산자와 함께 사용됨
            - 'A and B' : A와 B 모두 True시, True
            - 'A or B' :  A와 B 모두 False시, False
            - 'Not' : True를 False로, False를 True로
            
            ```python
            # 22시가 지나고 졸리면 True, 졸리지 않다면 False인 코드?
            
            #23시가 되었고, 잠이 오는 경우
            hour = 23
            status = 'sleepy'
            print(hour >= 22 and status == 'sleepy') # True
            
            #23시가 되었고, 잠이 오지 않는 경우
            hour = 23
            status = 'nice'
            print(hour >= 22 and status == 'sleepy') # False
            ```
            
        - Not 연산자 주의할 점
            - Falsy: False는 아니지만 False로 취급되는 다양한 값
                - 0, 0.0, (), [], {}, None, ‘’(빈 문자열)
                - 0은 불이 꺼짐, False / 1은 불이 켜짐, True로 취급된다
            - 논리 연산자도 우선순위가 존재
                - not, and, or 순으로 우선순위가 높음
                
                ```python
                print(not True) # False
                print(not 0) # True
                print(not 'hi') # False
                print(not True and False or not False) # True
                # 위와 같음
                print(((not True) and False) or (not False)) # True
                ```
                
        - 논리 연산자의 단축 평가
            - 빼박이다 이말이야
            - 결과가 확실한 경우 두번째 값은 확인하지 않고 첫번째 값 반환
                - and 연산에서 첫번째 값이 False인 경우 무조건 False → 첫번째 값 반환
                - or 연산에서 첫번째 값이 True인 경우 무조건 True → 첫번째 값 반환
                - 0은 False, 1은 True
                
                ```python
                print(3 and 5) # 5 # and는 둘다 맞는지 확인하는 연산자 # 3을 먼저보고 True가 정해지지 않아서 5까지 본 것
                print(3 and 0) # 0
                print(0 and 3) # 0
                print(0 and 0) # 0
                
                print(5 or 3) # 5
                print(3 or 0) # 3
                print(0 or 3) # 3
                print(0 or 0) # 0
                ```
                
                ```python
                a = 5 and 4
                print(a) # 4
                
                b = 5 or 3
                print(b) # 5
                
                c = 0 and 5
                print(c) # 0
                
                d = 5 or 0
                print(d) # 5
                ```
                

---

## 컨테이너

- 여러 개의 값(데이터)을 담을 수 있는 것(객체)으로, 서로 다른 자료형을 저장할 수 있음
    - ex) List
    - 파이썬의 특징이며 그렇지 않은 언어도 있다
- 컨테이너의 분류
    - 순서가 있는 데이터(Ordered) / 순서가 없는 데이터(Unordered)
    - 순서가 있다 ≠ 정렬되어 있다
    - 리스트: 시퀀스형 / 가변형(mutable)
    - 튜플: 시퀀스형 / 불변형(immutable)
    - 레인지: 시퀀스형 / 불변형(immutable)
    - 세트: 비시퀀스형 / 가변형(mutable)
    - 딕셔너리: 비시퀀스형 / 가변형(mutable)

<img width="866" alt="python_1" src="https://user-images.githubusercontent.com/86648892/181936188-61cc92c8-3a31-4bdc-976e-6c73faff011f.png">

## 시퀀스형

### 리스트

- 여러 개의 값을 순서가 있는 구조로 저장하고 싶을 때 사용

### 리스트의 생성과 접근

- 대괄호([]) 혹은 list()를 통해 생성
- 유연성으로 인해 파이썬에서 가장 흔히 사용
    - 파이썬에서는 어떠한 자료형도 저장 가능, 리스트 안에 리스트도 가능
    - mutable이어서 생성된 이후 내용 변경 가능
- 순서가 있는 시퀀스로 인덱스를 통해 접근 가능
    - list[i]를 통해 해당 인덱스 값에 접근

```python
my_list = []
another_list = list()
print(type(my_list)) # <class 'list'>
print(type(another_list)) # <class 'list'>

location = ['서울', '대전', '구미', '광주', '부울경']
print(type(location)) = # <class 'list'>
print(location[0]) # 서울

# mutable
location[0] = '양양'
print(location) # ['양양', '대전', '구미', '광주', '부울경']
```

```python
boxes = ['A', 'B', ['apple', 'banana', 'cherry']]

print(len(boxes)) # 3
print(boxes[2]) # ['apple', 'banana', 'cherry']
print(boxes[2][-1]) # cherry
print(boxes[-1][1][0]) #b

# len()은 컨테이너 자료형의 길이를 뜻한다
# 인덱스의 경우 오른쪽 방향으로 진행 시 0,1,2...
# 왼쪽 방향으로 진행 시 -1,-2,-3...
# 문자열 역시 각 character에 index로 접근 가능
```

---

### 튜플(Tuple)

- 여러 개의 값을 순서가 있는 구조로 저장하고 싶을 때 사용
- 리스트와 차이점은 immutable이라는 점
- 항상 소괄호 형태로 사용

```python
print((1, 2, 3, 1)) # (1, 2, 3, 1)
print(tuple((1, 2, 3, 1))) # (1, 2, 3, 1)
print(type((1, 2, 3, 1))) # <class 'tuple'>
```

### 튜플의 생성과 접근

- 소괄호(()) 혹은 tuple()을 통해 생성
- immutable 시퀀스로 인덱스를 통해 접근 가능

```python
# 값 접근
a = (1, 2, 3, 1)
print(a[1]) # 2

#값 변경 -> 불가능
a[1] = '3' # TypeError: 'tuple' object does not support item assignment
```

### 튜플 생성 주의사항

- 단일 항목의 경우
    - 하나의 항목으로 구성된 튜플은 생성 시 값 뒤에 쉼표를 붙여야 함
    - 쉼표를 붙이지 않을 경우 문자열로 처리됨
- 복수 항목의 경우
    - 마지막 항목에 붙은 쉼표는 없어도 되지만, 넣는 것을 권장(Trailing comma)

```python
tuple_a = (1,)
print(tuple_a) # (1,)
print(type(tuple_a)) # <class 'tuple'>

tuple_b = (1,2,3,)
print(tuple_b) # (1, 2, 3)
print(type(tuple_b)) # <class 'tuple'>

a = 1,
print(a) # (1,)
print(type(a)) # <class 'tuple'>

b = 1, 2, 3
print(b) # (1, 2, 3)
print(type(b)) # <class 'tuple'>
```

### 튜플 대입(Tuple assignment)

- 튜플 대입이란?
    - 우변의 값을 좌변의 변수에 한 번에 할당하는 과정
- 튜플은 일반적으로 파이썬 내부에서 활용
    - 추후 함수에서 복수의 값을 반환할 때에도 활용

```python
x, y = 1, 2
print(x, y) # 1 2

# 실제로 tuple로 처리
x, y = (1, 2)
print(x, y) # 1 2
```

---

### Range

- 숫자의 시퀀스를 나타내기 위해 사용
- 주로 반복문과 함께 사용됨

```python
print(range(4)) # range(0, 4)

# 담겨 있는 숫자를 확인하기 위하여 리스트로 형변환 (실제 활용시에는 형변환 필요없음)
print(list(range(4))) # [0, 1, 2, 3]
print(type(range(4))) # <class 'range'>
```

### Range 사용 방법

- 기본형: range(n)
    - 0부터 n-1까지의 숫자의 시퀀스
- 범위 지정: range(n, m)
    - n부터 m-1까지의 숫자의 시퀀스
- 범위 및 스텝 지정: range(n, m, s)
    - n부터 m-1까지 s만큼 증가시키며 숫자의 시퀀스

```python
# 0부터 특정숫자까지
print(list(range(3))) # [0, 1, 2]

# 숫자의 범위
print(list(range(1, 5))) # [1, 2, 3, 4]

# step 활용
print(list(range(1, 5, 2))) # [1, 3]

# 역순
print(list(range(6, 1, -1))) # [6, 5, 4, 3, 2]
print(list(range(6, 1, -2))) # [6, 4, 2]
print(list(range(6, 1, 1))) # []
```

---

## 슬라이싱 연산자

### 시퀀스를 특정 단위로 슬라이싱

- 인덱스와 콜론을 사용하여 문자열의 특정 부분만 잘라낼 수 있음
- 슬라이싱을 이용하여 문자열을 나타낼 때 콜론을 기준으로 앞 인덱스에 해당하는 문자는 포함되지만 뒤 인덱스에 해당 문자는 미포함

```python
# 리스트([1:4에서 1은 포함 4는 미포함)
print([1, 2, 3, 5][1:4]) # [2, 3, 5]

# 튜플
print((1, 2, 3)[:2] # (1, 2)

# range
print(range(10)[5:8]) # range(5, 8)

# 문자열
print('abcd'[2:4]) # cd
```

### 시퀀스를 k간격으로 슬라이싱

- 뒤에 간격을 나타내는 파라미터가 추가됨

```python
# 리스트
print([1, 2, 3, 5][0:4:2]) # [1, 3]

# 튜플
print((1, 2, 3, 5)[0:4:2]) # (1, 3)

# range
print(range(10)[1:5:3]) # range(1, 5, 3)

# 문자열
print('abcdefg'[1:3:2]) # b
```

### 문자열 슬라이싱(Slicing) 예제

```python
s = 'abcdefghi'
s[2:5] # cde
s[2:5:2] # ce
s[5:2:-1] # fed
s[:3] #abc
s[5:] #fghi
s[::] # abcdefghi # s[0:len(s):1]과 동일
s[::-1] # ihgfedcba # s[-1:-(len(s)+1):-1]과 동일
```

---

## 비시퀀스형 컨테이너

### 셋(Set)

- Set이란 중복되는 요소가 없고, 순서에 상관없는 데이터들의 묶음
    - 중복x: 중복되는 원소가 있다면 하나만 저장
    - 순서x: 인덱스를 이용한 접근 불가능
- 수학에서의 집합을 표현한 컨테이너
    - 집합 연산이 가능(합집합, 차집합, 교집합)(여집합을 표현하는 연산자는 별도로 존재x)
    - 중복된 값이 존재하지 않음
- mutable
    - 담고 있는 요소를 삽입, 변경, 삭제 가능

### 셋 생성

- 중괄호({}) 혹은 set()을 통해 생성
    - 빈 Set을 만들기 위해서는 set()을 반드시 활용해야 함
    - 빈 중괄호는 Dictionary
- 순서가 없어 별도의 값에 접근할 수 없음

```python
# Set는 중복 값 제거
print({1, 2, 3, 1, 2}) # {1, 2, 3}
print(type({1, 2, 3})) # <class 'set'>

# 빈 중괄호는 Dictionary
blank = {}
print(type(blank)) # <class 'dict'>
blank_set = set()
print(type(blank_set)) # <class 'set'>

# Set는 순서가 없어 인덱스 접근 등 특정 값에 접근할 수 없음
print({1, 2, 3}[0]) # TypeError: 'set' object is not subscriptable
```

### 셋 사용하기

- 셋을 활용하면 다른 컨테이너에서 중복된 값을 쉽게 제거할 수 있음
    - 단, 이후 순서가 무시되므로 순서가 중요한 경우 사용할 수 없음
    - set으로 변환 후 len()을 사용하면 몇 개의 고유한 값이 있는지 확인 가능

```python
my_list = ['서울', '서울', '대전', '광주', '서울', '대전', '부산', '부산']
print(len(set(my_list))) # 4 # 고유한 값 개수 확인

# Set을 사용하는 순간 순서가 사라짐(실행할 때마다 순서가 변경됨)
print(set(my_list)) # {'광주', '서울', '부산', '대전'}
```

### 셋 연산자

- '|' : 합집합 (해당 키는 pipeline이라 부름)
- '&' : 교집합
- '-' : 차집합
- '^' : 대칭차집합 (합집합 - 교집합)
- 여집합은 없음

```python
A_set = {1, 2, 3, 4}
B_set = {1, 2, 3, "Hello", (1, 2, 3)}

print(A_set | B_set) # {1, 2, 3, 4, (1, 2, 3), "Hello"}
print(A_set & B_set) # {1, 2, 3}
print(B_set - A_set) # {"Hello", (1, 2, 3)}
print(A_set ^ B_set) # {4, "Hello", (1, 2, 3)}
```

---

### 딕셔너리(Dictionary)

- 키-값(key-value)쌍으로 이루어진 자료형
- 3.7부터는 ordered, 이하 버전은 unordered
    - 실제로 그런건 아니고, 출력해줄 때 순서를 보정해준다는 느낌
- Dictionary의 키(key)
    - key는 변경 불가능한 데이터(immutable)만 활용 가능
        - string, integer, float, boolean, tuple, range
- 각 키의 값(values)
    - 어떠한 형태든 관계없음

### 딕셔너리 생성

- 중괄호({}) 혹은 dict()을 통해 생성
- key를 통해 value에 접근

```python
dict_a = {}
print(type(dict_a)) # <class 'dict'>

dict_b = dict()
print(type(dict_b)) # <class 'dict'>

dict_a = {'a': 'apple', 'b': 'banana', 'list': [1, 2, 3]}
print(dict_a) # {'a': 'apple', 'b': 'banana', 'list': [1, 2, 3]}
print(dict_a['list']) # [1, 2, 3]

dict_b = dict(a='apple', b='banana', list=[1, 2, 3])
# 이 경우 key가 문자열임에도 단순히 a, b, list로 선언
print(dict_b) # {'a': 'apple', 'b': 'banana', 'list': [1, 2, 3]}
```

---

## 형 변환(Typecasting)

### 형변환이란

- 파이썬에서 데이터 형태는 서로 변환할 수 있음
- 암시적 형 변환(Implicit)
    - 사용자가 의도하지 않고, 파이썬 내부적으로 자료형을 변환하는 경우
- 명시적 형 변환(Explicit)
    - 사용자가 특정 함수를 활용하여 의도적으로 자료형을 변환하는 경우

### 암시적 형 변환

- bool
- numeric type(int, float)

```python
print(True + 3) # 4 # + 연산자를 통해 true를 암시적으로 1로 변환
print(3 + 5.0) # 8.0 # 3은 int이지만 5.0으로 인해 3.0이라는 float로 형 변환
```

### 명시적 형 변환

- int
    - str, float → int
    - 단, 형식에 맞는 문자열만 정수로 변환 가능
    
    ```python
    # 문자열은 암시적 타입 변환이 되지 않음
    print('3' + 4) # TypeError: can only concatenate str (not "int") to str
    
    # 명시적 타입 변환이 필요함
    print(int('3') + 4) # 7
    
    # 정수 형식이 아닌 경우 타입 변환할 수 없음
    print(int('3.5') + 5) # ValueError: invalid literal for int() with base 10: '3.5'
    
    print('3' + str(4)) # 34 # string concatenation
    ```
    
- float
    - str(참고), int → float
    - 단, 형식에 맞는 문자열만 float만 변환 가능
    
    ```python
    print('3.5' + 3.5) # TypeError: can only concatenate str (not "float") to str
    
    # 정수 형식인 경우에도 float로 타입 변환
    print(float('3')) # 3.0
    
    # float 형식이 아닌 경우 타입 변환할 수 없음
    print(float('3/4') + 5.3) # ValueError: could not convert string to float: '3/4'
    ```
    
- str
    - int, float, list, tuple, dict → str
    
    ```python
    print(str(1)) # 1
    print(str(1.0)) # 1.0
    print(str([1, 2, 3])) # [1, 2, 3]
    print(str((1, 2, 3))) # (1, 2, 3)
    print(str({1, 2, 3})) # {1, 2, 3}
    ```
    
- 컨테이너 간 형 변환

<img width="522" alt="python_2" src="https://user-images.githubusercontent.com/86648892/181936241-e1b56723-acf8-48ae-9251-0569c7c04c63.png">

- input()
    - 사용자 데이터 입력
    - 파이썬에서는 입력값이 문자열로 저장됨
    - 숫자와 같이 다른 type으로 사용하고 싶다면 명시적으로 타입 캐스팅 해줘야 함
    
    ```python
    number = input('아무 숫자나 입력하세요.')
    
    # 111 222 입력
    print(number) # 111 222
    print(type(number)) # <class 'str'>
    map(int, input().split()) # map(함수, 시퀀스) # 받은 문자열을 쪼개서 각각 int로 형 변환
    ```
    

---

# 파이썬 프로그램 구성 단위

- 식별자(Identifier)
    - 변수, 함수, 클래스 등 프로그램이 실행되는 동안 다양한 값을 가질 수 있는 이름
    - 예약어
        - 파이썬 키워드 (명령어)
- 리터럴(Literal)
    - 읽혀지는 대로 쓰여있는 값 그 자체
- 표현식(Expression)
    - 새로운 데이터 값을 생성하거나 계산하는 코드 조각
- 문장(Statement)
    - 특정한 작업을 수행하는 코드 전체
    - 파이썬이 실행 가능한 최소한의 코드 단위
    - 표현식은 값을 생성하는 일부분이고, 문장은 특정작업을 수행하는 코드 전체
    - 모든 표현식(Expression)은 문장(Statement)이다!
- 패키지(Package)
    - 프로그램과 모듈 묶음
        - 프로그램: 실행하기 위한 것
        - 모듈: 다른 프로그램에서 불러와 사용하기 위한 것
- 라이브러리(Library)
    - 패키지 모음

```python
# name은 식별자, 즉 변수
# '김싸피'는 리터럴
name = '김싸피'

# 하나의 값(value)도 문장이 될 수 있다
'ssafy' # ssafy

# 표현식(expression)도 문장이 될 수 있다
5 * 21 - 4 # 101

# 실행가능(executable)해야 하기 때문에 아래 코드는 문장이 될 수 없다
name = '
```

---

# 추가 정리

- 임시변수 활용하여 변수 값 바꿔 저장하는 로직 기억할 것
- 변수에 특정 타입을 넣었다가 다른 타입을 넣어줘도 파이썬은 가능
- 진수 표현 중 16진수는 자주 사용
- 실수값 처리 중 비교 연산은 주의를 해야한다정도로만 이해
- 삼중따옴표는 줄바꿈까지 문자열 안에 저장됨
- escape sequence는 줄 바꿈, 탭, 인용부호 정도로 많이 사용
- 백슬래시 = 원화 키
- String Interpolation
    - f-strings를 쓰면 된다
    - 간단한 연산도 가능
- None
    - 변수는 만들되 값을 아직 넣고 싶지 않을 때 자주 사용
- Boolean
    - 비교 / 논리 연산자에서 주로 사용
    - 비교 연산자
        - =은 항상 뒤에 있다
    - 논리 연산자
        - Trusy, Falsy를 이용하여 간단하고 짧은 코드를 구현할 수 있다
        - 논리 연산자 우선순위 not→and→or
        - 논리 연산자 단축평가
            - True나 False를 최종적으로 확인하는 값을 반환함
- 시퀀스는 반복가능한 것
    - 지금은 구분 외우지 않아도 됨
- List
    - 파이썬은 음수 인덱스를 지정해둠
    - Slicing
        - sublist를 가져오고 싶을 때
        - list[a : b : c]
            - a == start
            - b == end (해당 숫자 전 index까지)
            - c == step
        - end는 -1 범위까지다
- Tuple
    - immutable
- Range
    - range는 반복 가능한 숫자의 목록일 뿐 리스트는 아니다
        - 리스트는 따로 `list(range(4))`와 같이 따로 선언해줘야 함
    - 리스트와 마찬가지로 start, end, step
- Set
    - 데이터베이스에서는 자주 사용
    - 대칭차집합
- Dictionary
    - 중요하다
    - JSON 자료 형태와 같다
    - Key - Value 쌍으로 이루어진 자료형
- Typecasting
    - 암시적 형변환은 의도적으로 사용하면 안됨
        - 반드시 명시적 형변환으로 작성하여 코드를 작성
---
# Python #2
- 제어문
- 함수
- 모듈
- 가상환경
---
# 제어문과 함수

## 제어문(Control Statement)

- WHAT?
    - 조건문
    - 반복문
- HOW?
    - 파이썬은 기본적으로 위에서부터 아래로 차례대로 명령을 수행
- WHY?
    - 특정 상황에 따라 코드를 선택적으로 실행(분기/조건)하거나 계속하여 실행(반복)하는 제어가 필요함
- 제어문은 순서도(flowchart)로 표현이 가능

## 조건문(Conditional Statement)

### 조건문 기본

- 참 / 거짓을 판별할 수 있는 조건식이 필요
    - if 조건식 == True:
        - 들여쓰기 코드 블록 실행
    - else:
        - 들여쓰기 코드 블록 실행
        - else는 선택적으로 활용 가능

```python
num = int(input('숫자 입력: '))
if num % 2: # if num % 2 == 1:
	print('홀수입니다.')
else:
	print('짝수입니다.')
```

### 복수 조건문

- 복수의 조건식은 elif를 활용하여 표현

```python
dust = 80
if dust > 150:
	print('매우 나쁨')
elif dust > 80:
	print('나쁨')
elif dust > 30:
	print('보통')
else:
	print('좋음')
print('미세먼지 확인 완료')

'''
보통
미세먼지 확인 완료!
'''
```

- 조건식을 동시에 검사하는 것이 아니라 순차적으로 비교함

### 중첩 조건문

- 조건문은 다른 조건문에 중첩되어 사용될 수 있음
- 들여쓰기에 유의할 것

```python
dust = 500
if dust > 150:
	print('매우 나쁨')
	if dus > 300:
			print('실외 활동을 자제하세요.')
elif dust > 80:
	print('나쁨')
elif dust > 30:
	print('보통')
elif: dust >= 0:
	print('좋음')
else:
	print('값이 잘못 되었습니다.')

'''
매우나쁨
실외 활동을 자제하세요.
'''
```

### 조건 표현식

- 조건 표현식(Conditional Expression)이란?
    - 일반적으로 조건에 따라 값을 정할 때 활용
    - 삼항 연산자(Ternary Operator)로 부르기도 함
    
    ```python
    true인 경우 값 if 조건 else false인 경우 값
    ```
    
    ```python
    # num이 정수일 때, 아래의 코드는 절댓값을 저장하기 위한 코드다
    
    value = num if num >= 0 else -num
    ```
    
    ```python
    '''
    num = 2
    if num % 2: # if num % 2 == 1:
    	print('홀수입니다.')
    else:
    	print('짝수입니다.')
    '''
    
    num = 2
    result = '홀수입니다.' if num % 2 else '짝수입니다.'
    print(result)
    
    # 짝수입니다.
    ```
    

## 반복문

- 특정 조건을 만족할 때까지 같은 동작을 계속 반복하고 싶을 때 사용
- while 문
    - 종료조건에 해당하는 코드를 통해 반복문을 종료시켜야 함
- for 문
    - 반복가능한 객체를 모두 순회하면 종료 (별도의 종료조건이 필요 없음)
- 반복 제어가 필요
    - break, continue, for-else

### While문

- while문은 조건식이 참인 경우 반복적으로 코드를 실행
    - 조건이 참인 경우 들여쓰기 코드 블록 실행
    - 코드 블록이 모두 실행되고, 다시 조건식을 검사하며 반복적으로 실행됨
    - while문은 무한 루프를 하지 않도록 종료 조건이 반드시 필요
    
    ```python
    a = 0
    while a < 3:
    	print(a)
    	a += 1
    print('끝')
    ```
    
    - 복합 연산자(In-Place Operator)는 연산과 할당을 합쳐 놓은 것

### For문

- for문은 시퀀스(string, tuple, list, range)를 포함한 순회가능한 객체(iterable)의 요소를 모두 순회
    - 처음부터 끝까지 모두 순회하므로 별도의 종료조건이 필요하지 않음
- Iterable
    - 순회할 수 있는 자료형(string, list, dict, tuple, range, set 등)
    - 순회형 함수(range, enumerate)

```python
for 변수명 in iterable:
		# Code Block
```

### for문을 이용한 문자열(String) 순회

```python
# 사용자가 입력한 문자를 한 글자씩 출력하시오.

chars = input()

# 1
for char in chars:
	print(char)

# 2
for idx in range(len(chars)):
	print(char[idx])

# happy 입력
'''
h
a
p
p
y
'''
```

### 딕셔너리(Dictionary) 순회

- 딕셔너리는 기본적으로 key를 순회하며, key를 통해 값을 활용

```python
grades = {'john': 80, 'eric': 90}

for student in grades:
	print(student)

'''
john
eric
'''

for student in grades:
	print(student, grades[studnet])

'''
john 80
eric 90
'''
```

### 추가 메서드를 활용한 딕셔너리(Dictionary) 순회

- 추가 메서드를 활용하여 순회할 수 있음
    - keys(): key로 구성된 결과
    - values(): value로 구성된 결과
    - items(): (key, value)의 튜플로 구성된 결과

```python
grades = {'john': 80, 'eric': 90}

for student, grade in grades.items():
	print(student, grade)

'''
john 80
eric 90
'''
```

### enumerate 순회

- enumerate()
    - 인덱스와 객체를 쌍으로 담은 열거형(enumeration) 객체 반환
        - (index, value) 형태의 tuple로 구성된 열거 객체를 반환

<img width="651" alt="python_3" src="https://user-images.githubusercontent.com/86648892/181936521-5595ba3f-ff78-419e-b44f-31faf926d71c.png">

```python
members = ['민수', '영희', '철수']
enumerate(members) # enumerate at 0x105d3e100
# 숫자와 값의 tuple
print(list(enumerate(members))) # [(0, '민수'), (1, '영희'), (2, '철수')]
# 기본값 0, start를 지정하면 해당 값부터 순차적으로 증가
print(list(enumerate(members,start=1))) # [(1, '민수'), (2, '영희'), (3, '철수')]
```

### List Comprehension

- 표현식과 제어문을 통해 특정한 값을 가진 리스트를 간결하게 생성하는 방법

```python
[code for 변수 in iterable]
[code for 변수 in iterable if 조건식]
```

```python
# 1~3의 세제곱 결과가 담긴 리스트 만들기
cubic_list = []
for number in range(1, 4):
	cubic_list.append(number ** 3)
print(cubic_list)

# [1, 8, 27]

# List Comprehension 활용
cubic_list = [number ** 3 for number in range(1, 4)]
print(cubic_list)

# [1, 8, 27]
```

- List Comprehension vs map?
    - 둘 간의 차이가 있다기보다 선택을 할 수 있음
    - Mapping은 반복가능한 객체에 내가 원하는 함수를 적용시키고 싶을 때 사용함
    - List Comprehension은 리스트에 있는 값을 내가 원하는 대로 필터링 또는 조작한 리스트를 얻기 위해 사용함
    - 리스트 컴프리헨션으로 할 수 있는 작업을 맵으로 할 수 있고, 그 반대 역시 가능함

### Dictionary Comprehension

- 표현식과 제어문을 통해 특정한 값을 가진 딕셔너리를 간결하게 생성하는 방법

```python
{key: value for 변수 in iterable}
{key: value for 변수 in iterable if 조건식}
```

```python
# 1~3의 세제곱 결과가 담긴 딕셔너리 만들기
cubic_dict = {}
for number in range(1,4):
	cubic_dict[number] = number *** 3
print(cubic_dict)

# {1: 1, 2: 8, 3: 27}

# Dictionary Comprehension 활용
cubic_dict = {number: number *** 3 for number in range(1, 4)}
print(cubic_dict)

# {1: 1, 2: 8, 3: 27}
```

## 반복문 제어

### 반복문 제어

- break
    - 반복문을 종료
    - 일종의 파토
- continue
    - continue 이후의 코드 블록은 수행하지 않고, 다음 반복을 수행
    - 일종의 건너뛰기
- for-else
    - 끝까지 반복문을 실행한 이후에 else문 실행
        - break를 통해 중간에 종료되는 경우 else문은 실행되지 않음
        - 즉, 온전히 반복문이 끝난 경우에만 else문이 실행됨
- pass
    - 아무것도 하지 않음
    - 문법적으로 필요하지만, 할 일이 없을 때 사용
    - 일단 패스!

### break

- 특정 조건에 반복문을 종료시키기 위해서는 break!

```python
n = 0
while True:
	if n == 3:
		break
	print(n)
	n += 1

'''
0
1
2
'''

for i in range(10):
	if i > 1:
		print('0과 1만 필요해!')
		break
	print(i)

'''
0
1
0과 1만 필요해
'''
```

### continue

- continue 이후의 코드 블록은 수행하지 않고, 다음 반복을 수행

```python
for i in range(6):
	if i % 2 == 0:
		continue
	print(i)

'''
1
3
5
'''
```

### pass

- 아무것도 하지 않음
- 자리를 채우는 용도
- 반복문 아니어도 사용 가능

```python
# i가 2일때 pass

for i in range(4):
	if i == 2:
		pass
	print(i)

'''
0
1
2
3
'''

# i가 2일때 continue
for i in range(4):
	if i == 2:
		continue
	print(i)

'''
0
1
3
'''
```

### for - else

- 끝까지 반복문을 실행한 이후에 else문 실행
- else문은 break로 중단되었는지 여부에 따라 실행
    - for문에서 break로 중단되었을 시 else문 실행 x

```python
for char in 'apple':
	if char == 'b':
		print('b!')
		break
else:
	print('b가 없습니다.')

# b가 없습니다.

for char in 'banana':
	if char == 'b':
		print('b!')
		break
else:
	print('b가 없습니다.')

# b!
```

---

# 함수

### WHY?

- Decomposition(분해)
    - 기능을 쪼개고
    - 재사용 가능하게 만들고
    
    ```python
    # 평균을 구하는 코드
    
    # 1
    
    numbers = [1, 2, 3]
    result = 0
    count = 0
    for num in numbers:
    	result += num
    	count += 1
    print(result / count) # 2.0
    
    # 2
    
    numbers = [1, 2, 3]
    print(sum(numbers) / len(numbers)) # 2.0
    
    # 3
    
    numbers = [1, 2, 3]
    
    def average(numbers):
    	return sum(numbers) / len(numbers)
    
    print(average(numbers)) # 2.0
    
    # 3으로 갈수록 코드 가독성이 높아짐
    ```
    
- Abstraction(추상화)
    - 복잡한 내용을 모르더라도 사용할 수 있도록
        - 마치 우리가 스마트폰의 원리를 잘 몰라도 사용할 수 있는 것처럼
    - 재사용성, 가독성, 생산성

## 함수 기초

### 함수의 종류

- 크게 3가지로 분류
- 내장 함수
    - 파이썬에 기본적으로 포함된 함수
    - 파이썬 개발자가 만든 것
    - print(), len() 등
- 외장 함수
    - import문을 통해 사용하며, 외부 라이브러리에서 제공하는 함수
    - 다른 개발자가 만든 것
- 사용자 정의 함수
    - 직접 사용자가 만드는 함수

### 함수의 정의

- 함수(Function)
    - 특정한 기능을 하는 코드의 조각(묶음)
    - input, function body, output

### 함수 기본 구조

- 선언과 호출(define & call)
    - 선언은 함수를 만드는 것, 호출은 필요할 때 함수를 사용하는 것
- 입력(input)
- 문서화(docstring)
    - 함수에 대한 설명, 사용자가 조금 더 원활하게 이해할 수 있도록 도움
- 범위(scope)
- 결과값(output)

<img width="721" alt="python_4" src="https://user-images.githubusercontent.com/86648892/181936575-8b42ea19-c54f-4df1-8e80-b4e4d785b0f6.png">

### 선언과 호출(define & call)

- def 키워드로 선언
- 들여쓰기로 function body(실행될 코드 블록)을 작성
- docstring은 함수 body 앞에 선택적으로 작성 가능
    - 작성 시에는 반드시 첫 번째 문장에 문자열 “””
- 함수는 parameter를 넘겨줄 수 있음
- 함수는 동작 후에 return을 통해 결괏값을 전달함

### 함수의 정의

```python
def function_name(parameter):
	# code block
	return returning_value
```

- 함수는 호출되면 코드를 실행하고 return 값을 반환하며 종료된다

```python
num1 = 0
num2 = 1
def func1(a, b):
	return a + b
def func2(a, b):
	return a - b
def func3(a, b):
	return func1(a, 5) + func2(5, b)

result = func3(num1, num2)
print(result) # 9
```

## 함수의 결과값(Output)

### 값에 따른 함수의 종류

- Void function
    - 명시적인 return 값이 없는 경우, None을 반환하고 종료
- Value returning function
    - 함수 실행 후, return문을 통해 값 반환
    - return을 하게 되면, 값 반환 후 함수가 바로 종료

```python
# Void function
print('hello python') # hello python
# print는 값을 출력하지만, 값을 반환하진 않습니다.

# Value returning function
float('3.14') # 3.14
```

- 주의! print vs return
    - print를 사용하면 호출될 때마다 값이 출력됨
        - 주로 테스트를 위해 사용
    - 데이터 처리를 위해서는 return 사용

```python
# Void function 예시
def void_product(x, y):
	print(f'{x} x {y} = {x * y}')

void_product(4, 5) # 4 x 5 = 20
ans = void_product(4, 5) # 4 x 5 = 20
print(ans) # None

# Value returning function 예시
def value_returning_product(x, y):
	return x * y

value_returning_product(4, 5)
ans = value_returning_product(4, 5)
print(ans) # 20
```

- 주의! return vs print
    - REPL(Read-Eval-Print-Loop) 환경에서는 마지막으로 작성된 코드의 리턴 값을 보여주므로 같은 동작을 하는 것으로 착각할 수 있음

### 두 개 이상의 값 반환

```python
# return문을 2개 사용하여 잘못됨
def minus_and_product(x, y):
	return x - y
	return x * y

y = minus_and_product(4, 5)
print(y) # -1
```

- return은 항상 하나의 값만을 반환
- return으로 2개 이상의 값을 반환하고 싶다?
    - Tuple 활용

```python
def minus_and_product(x, y):
	return x - y, x * y

y = minus_and_product(4, 5)
print(y) # (-1, 20)
print(type(y)) # <class 'tuple'>
```

### 함수 반환 정리

- return x → None
- return o → 하나를 반환
    - 여러 개를 원하면, Tuple 활용(혹은 리스트와 같은 컨테이너 활용)

```python
# 똑바로 읽어도 거꾸로 읽어도 같은 단어를 찾는 함수
word_list = ['우영우', '기러기', '별똥별', '파이썬']
def is_palindrome(word_list):
	palindrome_list = []
	for word in word_list:
		if word == word[::-1]:
			palindrome_list.append(word)
	return palindrome_list
print(is_palindrome(word_list))
# ['우영우', '기러기', '별똥별']
```

---

## 함수의 입력(Input)

### Parameter와 Argument

- Parameter: 함수를 정의할 때, 함수 내부에서 사용되는 변수
- Argument: 함수를 호출할 때, 넣어주는 값

### Argument

- Argument란?
    - 함수 호출 시 함수의 parameter를 통해 전달되는 값
    - Argument는 소괄호 안에 할당
        - func_name(argument)
        - 필수 Argument: 반드시 전달되어야 하는 argument
        - 선택 Argument: 값을 전달하지 않아도 되는 경우는 기본값이 전달

### Positional Arguments

- 기본적으로 함수 호출 시 Argument는 위치에 따라 함수 내에 전달됨

### Keyword Arguments

- 직접 변수의 이름으로 특정 Argument를 전달할 수 있음
- Keyword Argument 다음에 Positional Argument를 활용할 수 없음

```python
def add(x, y):
	return x + y

add(x=2, y=5) # 가능
add(2, y=5) # 가능
add(x=2, 5) # Error
```

### Default Arguments Values

- 기본값을 지정하여 함수 호출 시 argument 값을 설정하지 않도록 함
    - 정의된 것보다 더 적은 개수의 argument들로 호출될 수 있음

```python
def add(x, y=0):
	return x + y

add(2)
# x에 2가 들어감
```

### 정해지지 않은 여러 개의 Arguments 처리

- print 함수의 Arguments 개수가 변해도 잘 동작하는 이유는?

```python
print('hello') # hello
print('you', 'need', 'python') # you need python
```

- Asterisk(애스터리스크) 혹은 언패킹 연산자라 불리는 * 덕분

<img width="833" alt="python_5" src="https://user-images.githubusercontent.com/86648892/181936613-6abe588b-d38c-4e5d-ba1e-8d628a771224.png">

### 가변인자(*args)

- 가변인자란?
    - 여러 개의 Positional Argument를 하나의 필수 parameter로 받아서 사용
- 가변인자는 언제 사용하는가?
    - 몇 개의 Positional Argument를 받을지 모르는 함수를 정의할 때 유용

```python
def add(*args):
	for arg in args:
		print(arg)

add(2)
add(2, 3, 4, 5)
```

### 패킹 / 언패킹(Packing / Unpacking)

- 가변 인자를 이해하기 위해서는 패킹, 언패킹을 이해해야함
- 패킹
    - 여러 개의 데이터를 묶어서 변수에 할당하는 것
    
    ```python
    numbers = (1, 2, 3, 4, 5) # 패킹
    print(numbers) # (1, 2, 3, 4, 5)
    ```
    
- 언패킹
    - 시퀀스 속의 요소들을 여러 개의 변수에 나누어 할당하는 것
    
    ```python
    numbers = (1, 2, 3, 4, 5)
    a, b, c, d, e = numbers # 언패킹
    print(a, b, c, d, e) # 1 2 3 4 5
    ```
    
- 언패킹 시 변수의 개수와 할당하고자 하는 요소의 개수가 동일해야함

```python
numbers = (1, 2, 3, 4, 5) # 패킹
a, b, c, d, e, f = numbers # 언패킹
# ValueError: not enough values to unpack (expected 6, got 5)
```

- 언패킹 시 왼쪽의 변수에 asterisk(*)를 붙이면, 할당하고 남은 요소를 리스트에 담을 수 있음

```python
numbers = (1, 2, 3, 4, 5)

a, b, *rest = numbers # 1, 2를 제외한 나머지를 rest에 대입
print(a, b, rest) # 1 2 [3, 4, 5]

a, *rest, e = numbers # 1, 5를 제외한 나머지를 rest에 대입
print(rest) # [2, 3, 4]
```

### Asterisk(*)와 가변인자

- *는 시퀀스 언패킹 연산자라고도 불리며, 말 그대로 시퀀스를 풀어 헤치는 연산자
    - 주로 튜플이나 리스트를 언패킹하는데 사용
    - *를 활용하여 가변인자를 만들 수 있음
    
    ```python
    def func(*args):
    	print(args)
    	print(type(args))
    
    func(1, 2, 3, 'a', 'b')
    '''
    (1, 2, 3, 'a', 'b')
    <class 'tuple'>
    '''
    ```
    

### 가변인자 예시

```python
# packing을 통해 받은 모든 숫자들의 합을 구하는 함수 만들기

def sum_all(*numbers):
	result = 0
	for number in numbers:
		result += number
	return result

print(sum_all(1, 2, 3)) # 6
print(sum_all(1, 2, 3, 4, 5, 6)) # 21
```

```python
# 반드시 받아야하는 인자와, 추가적인 인자를 구분해서 사용할 수 있음

def print_family_name(father, mother, *pets):
	print(f'아버지 : {father}')
	print(f'어머니 : {mother}')
	print('반려동물들..')
	for name in pets:
		print(f'반려동물: {name}')

print_family_name('아부지', '어무니', '멍멍이', '냥냥이')

'''
아버지 : 아부지
어머니 : 어무니
반려동물들..
반려동물: 멍멍이
반려동물: 냥냥이
'''
```

### 가변 키워드 인자(**kwargs)

- 몇 개의 키워드 인자를 받을지 모르는 함수를 정의할 때 유용
- **kwargs는 딕셔너리로 묶여 처리되며, parameter에 **를 붙여 표현

```python
def family(**kwargs):
	for key, value in kwargs.items():
		print(key, ":", value)

family(father = '아부지', mother = '어무니', baby = '아기')

'''
father : 아부지
mother : 어무니
baby : 아기
'''
```

```python
def print_family_name(father, mother, **pets):
	print("아버지 :", father)
	print("어머니 :", mother)
	if pets:
		print("반려동물들..")
		for species, name in pets.items():
			print(f'{species} : {name}')

print_family_name('아부지', '어무이', dog = '멍멍이', cat = '냥냥이')

'''
아버지 : 아부지
어머니 : 어무이
반려동물들..
dog : 멍멍이
cat : 냥냥이
'''
```

### 가변 인자(*args)와 가변 키워드 인자(**kwargs) 동시 사용 예시

- 가변 인자와 가변 키워드 인자를 함께 사용할 수 있음

```python
def print_family_name(*parents, **pets):
	print("아버지 :", parents[0])
	print("어머니 :", parents[1])
	if pets:
		print("반려동물들..")
		for title, name in pets.items():
			print('{} : {}'.format(title, name))

print_family_name('아부지', '어무이', dog = '멍멍이', cat = '냥냥이')

'''
아버지 : 아부지
어머니 : 어무이
반려동물들..
dog : 멍멍이
cat : 냥냥이
'''
```

---

# Python의 범위(Scope)

## Python의 범위(Scope)

- 함수는 코드 내부에 local scope를 생성하며, 그 외의 공간인 global scope로 구분
- scope
    - global scope: 코드 어디에서든 참조할 수 있는 공간
    - local scope: 함수가 만든 scope, 함수 내부에서만 참조 가능
- variable
    - global variable: global scope에 정의된 변수
    - local variable: local scope에 정의된 변수

## 변수 수명주기(lifecycle)

- 변수는 각자의 수명주기(lifecycle)가 존재
    - built-in scope
        - 파이썬이 실행된 이후부터 영원히 유지
    - global scope
        - 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
    - local scope
        - 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지

```python
def func():
	a = 20
	print('local', a)

func() # local 20
print('global', a) # NameError: name 'a' is not defined
```

## 이름 검색 규칙(Name Resolution)

- 파이썬에서 사용되는 이름(식별자)들은 이름공간(namespace)에 저장되어 있음
- 아래와 같은 순서로 이름을 찾아나가며, LEGB Rule이라고 부름
    - Local scope: 지역 범위(현재 작업 중인 범위)
    - Enclosed scope: 지역 범위 한 단계 위 범위
    - Global scope: 최상단에 위치한 범위
    - Built-in scope: 모든 것을 담고 있는 범위(정의하지 않고 사용할 수 있는 모든 것)
        - ex) print()
    - 함수 내에서는 바깥 Scope의 변수에 접근 가능하나 수정은 할 수 없음

### LEGB 예시 1

```python
print(sum) # <built-in function sum>
print(sum(range(2))) # 1
sum = 5
print(sum) # 5
print(sum(range(2))) # TypeError: 'int' object is not callable
```

- Global scope 이름공간의 sum 변수에 값 5가 할당
- 이후 global scope에서 sum은 LEGB에 의해 Built-in scope의 내장 함수보다 5가 먼저 탐색

### LEGB 예시 2

```python
a = 0
b = 1
def enclosed():
	a = 10
	c = 3
	def local(c):
		print(a, b, c) # 10 1 300
	local(300)
	print(a, b, c) # 10 1 3
enclosed()
print(a, b) # 0 1
```

## global 문

- 현재 코드 블록 전체에 적용되며, 나열된 식별자(이름)이 global variable임을 나타냄
    - global에 나열된 이름은 같은 코드 블록에서 global 앞에 등장할 수 없음
    - global에 나열된 이름은 parameter, for 루프 대상, 클래스 / 함수 정의 등으로 정의되지 않아야 함

### global 예시

```python
# 함수 내부에서 글로벌 변수 변경하기
a = 10
def func1():
	global a
	a = 3

print(a) # 10
func1()
print(a) # 3
```

- Local scope에서 global 변수 값의 변경
- global 키워드를 사용하지 않으면, Local scope에 a 변수가 생성됨

### global 관련 에러

```python
# global 주의사항
a = 10
def func1():
	print(a) # global a 선언 전에 사용
	global a
	a = 3

print(3)
func1()
print(a)

# SyntaxError: name 'a' is used prior to global declaration

# global 주의사항
a = 10
def func1(a):
	global a # parameter에 global 사용 불가
	a = 3

print(a)
func1(3)
print(a)

$ SyntaxError: name 'a' is parameter and global
```

## nonlocal 문

- global을 제외하고 가장 가까운(둘러싸고 있는) scope의 변수를 연결하도록 함
    - nonlocal에 나열된 이름은 같은 코드 블록에서 nonlocal 앞에 등장할 수 없음
    - nonlocal에 나열된 이름은 parameter, for 루프 대상, 클래스 / 함수 정의 등으로 정의되지 않아야 함
- global과는 달리 이미 존재하는 이름과의 연결만 가능함

### nonlocal 예시

```python
# nonlocal 예시
x = 0
def func1():
	x = 1
	def func2():
		nonlocal x
		x = 2
	func2()
	print(x) # 2

func1()
print(x) # 0
```

- enclosed scope(func1)의 변수 x의 변경

### nonlocal, global 비교

```python
# 선언된 적 없는 변수의 활용
def func1():
	global out
	out = 3

func1()
print(out) # 3

# 선언된 적 없는 변수의 활용
def func1():
	def func2():
		nonlocal y
		y = 2
	func2()
	print(y)

func1()

# SyntaxError: no binding for nonlocal 'y' found
```

## 함수의 범위 주의

- 기본적으로 함수에서 선언된 변수는 Local scope에 생성되며, 함수 종료 시 사라짐
- 해당 scope에 변수가 없는 경우, LEGB rule에 의해 이름을 검색함
    - 변수에 접근은 가능하지만, 해당 변수를 수정할 수는 없음
    - 값을 할당하는 경우 해당 scope의 이름공간에 새롭게 생성되기 때문
    - 단, 함수 내에서 필요한 상위 scope 변수는 argument로 넘겨서 활용할 것
- 상위 scope에 있는 변수를 수정하고 싶다면 *global, nonlocal* 키워드를 활용 가능
    - 단, 코드가 복잡해지면서 변수의 변경을 추적하기 어렵고, 예기치 못한 오류가 발생
    - 가급적 사용하지 않는 것을 권장하며, 함수로 값을 바꾸고자 한다면 항상 argument로 넘기고 리턴 값을 사용하는 것을 추천

---

# 함수 응용

## 내장 함수(Built-in Functions)

- 파이썬 인터프리터에는 항상 사용할 수 있는 많은 함수와 형(type)이 내장되어 있음

<img width="323" alt="python_6" src="https://user-images.githubusercontent.com/86648892/181936662-e989291d-b01f-47fb-92e8-e1bb3bf24466.png">


## map

### map(function, iterable)

- 순회 가능한 데이터구조(iterable)의 모든 요소에 함수(function) 적용하고, 그 결과를 map object로 반환

```python
numbers = [1, 2, 3]
result = map(str, numbers)
print(result, type(result)) # <map object at 0x0000020984097FA0> <class 'map'>
print(list(result)) # ['1', '2', '3']

# 리스트 형변환을 통해 결과를 직접 확인
```

- input 값들을 숫자로 바로 활용하고 싶을 때

```python
n, m = map(int, input().split()) # 3 5를 입력하면
print(n, m) # 3 5
print(type(n), type(m)) # <class 'int'> <class 'int'>
```

## filter

### filter(function, iterable)

- 순회 가능한 데이터구조(iterable)의 모든 요소에 함수(function) 적용하고, 그 결과가 True인 것들을 filter object로 반환

```python
def odd(n):
	return n % 2
numbers = [1, 2, 3]
result = filter(odd, numbers)
print(result, type(result)) # <filter object at 0x000001FB4B217F40> <class 'filter'>
print(list(result)) # [1, 3]

#리스트 형변환을 통해 결과 직접 확인
```

## zip

### zip(*iterables)

- 복수의 iterable을 모아 튜플을 원소로 하는 zip object를 반환

```python
girls = ['jane', 'ashley']
boys = ['justin', 'eric']
pair = zip(girls, boys)
print(pair, type(pair)) # <zip object at 0x000001A4B3DD0380> <class 'zip'>
print(list(pair)) # [('jane', 'justin'), ('ashley', 'eric')]
```

- 2차원 배열에서 자주 사용

## lambda 함수

### lambda[parameter] : 표현식

- 람다함수
    - 표현식을 계산한 결과값을 반환하는 함수로, 이름이 없는 함수여서 익명함수라고도 불림
    - 일종의 클로저
- 특징
    - return문을 가질 수 없음
    - 간편 조건문 외 조건문이나 반복문을 가질 수 없음
- 장점
    - 함수를 정의해서 사용하는 것보다 간결하게 사용 가능
    - def를 사용할 수 없는 곳에서도 사용 가능

```python
# 삼각형의 넓이를 구하는 공식 - def
def triangle_area(b, h):
	return 0.5 * b * h
print(triangle_area(5, 6)) # 15.0

# 삼각형의 넓이를 구하는 공식 - lambda
triangle_area = lambda b, h : 0.5 * b * h
print(triangle_area(5, 6)) # 15.0
```

- 재사용성을 가진 기능의 함수는 def, 일회성인 경우는 lambda를 사용하는 것이 바람직함

## 재귀 함수(recursive function)

- 자기 자신을 호출하는 함수
- 무한한 호출을 목표로 하는 것이 아니며, 알고리즘 설계 및 구현에서 유용하게 활용
    - 알고리즘 중 재귀 함수로 로직을 표현하기 쉬운 경우가 있음 (ex. 점화식)
    - 변수의 사용이 줄어들며, 코드의 가독성이 높아짐
- 1개 이상의 base case(종료되는 상황)가 존재하고, 수렴하도록 작성
- Factorial

```python
def factorial(n):
	if n ==0 or n == 1:
		return 1
	else:
		return n * factorial(n-1)

print(factorial(4)) # 24

# 반복문으로 작성한다면?

def fact(n):
	result = 1
	while n > 1:
		result *= n
		n -= 1
	return result

print(fact(4)) # 24
```

- 2진수로 변환

```python
# 입력된 10진수를 2진수로 반환하는 함수를 작성하라

def dec_to_bin(n):
	if n < 2:
		return str(n)
	return dec_to_bin(n // 2) + dec_to_bin(n % 2)

# 2진수는 0, 1로 구성되므로 base case를 n이 0, 1이 될 때로 설정
# 2진수는 0110101과 같은 식으로 붙어야 되므로 str으로 형변환하여 더해줌
# dec_to_bin에 n이 들어가면
# dec_to_bin(n % 2)에서 나온 숫자 0 or 1이 대기 상태로 남고
# n // 2에 해당하는 값이 dec_to_bin에 다시 호출되고
# 이 과정이 재귀 형태로 반복됨
```

### 재귀함수 주의사항

- 재귀함수는 base case에 도달할 때까지 함수를 호출함
- 메모리 스택이 넘치게 되면(stack overflow) 프로그램이 동작하지 않게 됨
- 파이썬에서는 최대 재귀 깊이(maximum recursion depth)가 1,000번으로, 호출 횟수가 이를 넘어가게 되면 Recursion Error 발생

### 반복문과 재귀함수 비교

- 알고리즘 자체가 재귀적인 표현이 자연스러운 경우 재귀함수를 사용함
- 재귀 호출은 변수 사용을 줄여줄 수 있음
- 재귀 호출은 입력 값이 커질수록 연산 속도가 오래 걸림

---

# 모듈

- 합, 평균, 표준편차…등 자주 쓰는 기능들처럼
- 다양한 기능을 하나의 파일로 (Module)
- 다양한 파일을 하나의 폴더로 (Package)
- 다양한 패키지를 하나의 묶음으로 (Library)
    - 라이브러리 vs 프레임워크?
        - 라이브러리는 삽, 프레임워크는 포크레인 같은 느낌
        - 라이브러리는 주도권이 조금 더 있다
- 이것을 관리하는 관리자 (pip)
- 패키지의 활용 공간 (가상환경)

## 모듈과 패키지

- 모듈
    - 특정 기능을 하는 코드를 파이썬 파일(.py) 단위로 작성한 것
- 패키지
    - 특정 기능과 관련된 여러 모듈의 집합
    - 패키지 안에는 또 다른 서브 패키지를 포함

### 모듈과 패키지 불러오기

```python
import module
from module import var, function, Class
from module import *

from package import module
from package.module import var, function, Class
```

## 파이썬 표준 라이브러리

### 파이썬에 기본적으로 설치된 모듈과 내장 함수

- [파이썬 표준 라이브러리](https://docs.python.org/ko/3/library/index.html)
- ex) random.py

### 파이썬 패키지 관리자(pip)

- PyPI(Python Package Index)에 저장된 외부 패키지들을 설치하도록 도와주는 패키지 관리 시스템
- pip해서 설치하고, import해서 가져온다

### 파이썬 패키지 관리자(pip) 명령어

- 패키지 설치
    - 최신 버전 / 특정 버전 / 최소 버전을 명시하여 설치할 수 있음
    - 이미 설치되어 있는 경우 이미 설치되어 있음을 알리고 아무것도 하지 않음
        - pip install SomePackage
        - pip install SomePackage==1.0.5
        - pip install ‘SomePackage>=1.0.4’
        - 모두 bash, cmd 환경에서 사용되는 명령어
    
    <img width="449" alt="python_7" src="https://user-images.githubusercontent.com/86648892/181936740-396aec59-466f-4c0f-9065-84f76ba9a308.png">
    
    <img width="454" alt="python_8" src="https://user-images.githubusercontent.com/86648892/181936738-ec161226-d9c3-4f29-9b53-ed4deb8520a2.png">
    
- 패키지 삭제
    - pip는 패키지 업그레이드를 하는 경우 과거 버전을 자동으로 지워줌
    - pip uninstall SomePackage
    
    <img width="499" alt="python_9" src="https://user-images.githubusercontent.com/86648892/181936871-8f96547c-39a3-4020-9647-73f1132ee85a.png">
    
- 패키지 목록 및 특정 패키지 정보
    - pip list
    
    <img width="440" alt="python_10" src="https://user-images.githubusercontent.com/86648892/181936872-b02f5702-0d25-4d09-98e0-f7d8153fedb8.png">
    
    - pip show SomePackage
    
    <img width="446" alt="python_11" src="https://user-images.githubusercontent.com/86648892/181936873-9340abb0-eac7-4858-b6bb-d04fc38cf73b.png">
    
- 패키기 관리하기
    - 아래의 명령어들을 통해 패키지 목록을 관리[1]하고 설치할 수 있음[2]
    - 일반적으로 패키지를 기록하는 파일의 이름은 requirements.txt로 정의함
    - pip freeze > requirements.txt
        - 설치된 pip 목록들(설치한 라이브러리들)을 requirements.txt로 박제하겠다는 것
    - pip install -r requirements.txt
        - 박제한 requirements.txt를 집이나 강의장으로 들고가서 같은 환경으로 만들 수 있음
    
    <img width="453" alt="python_12" src="https://user-images.githubusercontent.com/86648892/181936876-b118e3eb-0162-4abd-b8ee-186dd1f60924.png">
    
    <img width="467" alt="python_13" src="https://user-images.githubusercontent.com/86648892/181936877-a67c3bd7-adcd-4319-be38-ed0a534b8e35.png">
    
    - requirements.txt를 바탕으로 설치
- 다양한 파이썬 프로젝트에서 사용된
    
    <img width="561" alt="python_14" src="https://user-images.githubusercontent.com/86648892/181936878-aaee3ba2-8d84-457c-b8e9-7df346f8c088.png">
    
    <img width="605" alt="python_15" src="https://user-images.githubusercontent.com/86648892/181936880-aecbdd1b-1d1c-4e96-925f-e101d6462e2b.png">
    

## 사용자 모듈과 패키지

### 패키지 만들기

- 패키지는 여러 모듈 / 하위 패키지로 구조화
    - 활용 예시: package.module
- 모든 폴더에는 __init__.py를 만들어 패키지로 인식
    - Python 3.3부터는 파일이 없어도 되지만, 하위 버전 호환 및 프레임워크 등에서의 동작을 위해 파일을 생성하는 것을 권장
- 계산 기능이 들어간 calculator 패키지를 아래와 같이 구성
    - check.py에서 calculator의 tools.py의 기능을 사용
    - 폴더 구조
        - my_package/
            - __init__.py
            - check.py
            - calculator/
                - __init__.py
                - tools.py
    
    <img width="289" alt="python_16" src="https://user-images.githubusercontent.com/86648892/181936881-3d897c7f-e5ec-4e6a-afe5-7def4fd2200f.png">
    

### 모듈 만들기 - calculator

- calculator/tools.py에 add 함수와 minus 함수 작성

```python
# calculator/tools.py

def add(num1, num2):
	return num1 + num2

def minus(num1, num2):
	return num1 - num2
```

### 모듈 활용하기 - check

- 모듈을 활용하기 위해서는 import문을 통해 가져옴

```python
from calculator import tools

print(dir(tools)) # tools에 어떤 변수와 메소드(method)를 가지고 있는지 나열
'''
['__builtins__', '__cached__', '__doc__', '__file__',
'__loader__', '__name__', '__package__', '__spec__',
'add', 'minus']
'''
print(tools.add(3, 5)) # 8
print(tools.minus(3, 5)) # -2
```

## 가상환경

### 가상환경

- 파이썬 표준 라이브러리가 아닌 외부 패키지와 모듈을 사용하는 경우 모두 pip를 통해 설치를 해야함
- 복수의 프로젝트를 하는 경우 버전이 상이할 수 있음
    - 컴퓨터는 한 대인데, 가령 python의 django 라이브러리를 다양한 버전으로 사용하고 싶을 경우
        - 과거 외주 프로젝트 - django 버전 2.x
        - 신규 회사 프로젝트 - django 버전 3.x
        - 이런 경우 사용하는 것이 가상환경
- 이러한 경우 가상환경을 만들어 프로젝트별로 독립적인 패키지를 관리할 수 있음
- 가상환경을 만들고 관리하는데 사용되는 모듈이 있는데, Python 버전 3.5부터 생김
- 특정 디렉토리에 가상환경을 만들고, 고유한 파이썬 패키지 집합을 가질 수 있음
    - 특정 폴더에 가상환경이(패키지 집합 폴더 등) 있고
    - 실행환경(예 - bash)에서 가상환경을 활성화시켜
    - 해당 폴더에 있는 패키지를 관리 / 사용함

### 가상환경 생성

- 가상환경을 생성하면, 해당 디렉토리에 별도의 파이썬 패키지가 설치됨
- python -m venv <폴더명>
    - venv는 virtual environment의 줄임말
    - 폴더명을 이름으로 갖는 가상환경을 만들겠다!
    - 아래 사진은 venv라 불리는 가상환경을 만들겠다는 것

<img width="540" alt="python_17" src="https://user-images.githubusercontent.com/86648892/181936882-65a6a4d5-a169-404d-8a83-7eab21a96175.png">

<img width="449" alt="python_18" src="https://user-images.githubusercontent.com/86648892/181936883-45380420-327c-44e9-83e1-128986301bbb.png">

### 가상환경 활성화 비활성화

- 아래의 명령어를 통해 가상환경을 활성화
    - <venv>는 가상환경을 포함하는 디렉토리의 경로
    
    <img width="575" alt="python_19" src="https://user-images.githubusercontent.com/86648892/181936884-76ed7da0-fadf-4b3d-8837-a0c9385db54c.png">
    
- 가상환경 비활성화는 $ deactivate 명령어를 사용
- cmd와 bash 환경
    - $ source venv/Scripts/activate
        - 가상환경을 활성화함
        - $ pip list
            - 확인해보면 텅 빈 상태가 된 것을 확인
        - $ pip install requests
            - 여기에 다시 새롭게 requests라는 패키지 설치한 것

<img width="1166" alt="python_20" src="https://user-images.githubusercontent.com/86648892/181936865-26fbb8f0-fb38-4316-9152-6c642eb769a1.png">

- 동일 컴퓨터에서 별도의 가상환경
    - 동일 컴퓨터 프로젝트별 가상환경
    - 각 프로젝트별 가상환경(venv 폴더별로 고유한 프로젝트가 설치됨)

<img width="977" alt="python_21" src="https://user-images.githubusercontent.com/86648892/181936867-c36a2fd6-8d18-4d9a-9a07-c40eb2eee562.png">

<img width="1097" alt="python_22" src="https://user-images.githubusercontent.com/86648892/181937108-adc2949f-b76f-48b8-a129-91df8ffa810e.png">

---

# 추가 정리

- print()의 end option은 기본적으로 줄 바꿈이 들어가있다
    - print(x, end = ‘’)으로 새로 설정하면 줄 바꿈이 되지 않음
- continue와 pass 구분을 잘하자
- LEGB에서 한 문제 나온다
- 가상환경이 무엇인지만 알면 된다

---

## 모듈 추가내용
![python_23](https://user-images.githubusercontent.com/86648892/181937109-23e46d73-27eb-4001-b724-75c65ba8a71c.png)
```python
# 1) import에서 가져오는 것은 모듈, 함수, 클래스 단위
# 2) __init__.py의 역할?
	# 2-1) 패키지로 인식시켜주는 기능
	# 2-2) 패키지를 namespace에 등록시켜주는 기능
	# 2-3) __init__.py 안에 작성하는 코드는 이 패키지가 생성되는 동시에 이러이러한 것을 자동으로 시켜주겠다는 것
# 3) .은 현재 위치
```
![python_24](https://user-images.githubusercontent.com/86648892/181937107-1efbf435-738a-40c1-b706-1ca780d29fa7.png)

```python
# test.py

name = 'zac'
```

```python
# main.py

import my_pac # __init__.py에 설정해놓은 것을 통해 연계되어 math와 test를 import
print(dir())
print(my_pac.math.test.name)

'''
math init 실행됨
my_pac init 실행됨
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'my_pac']
zac
'''
```
---
# Python #3
- method
- shallow copy
- deep copy
---
# 데이터 구조 (Data Structure)

## 목차

### 순서가 있는 데이터 구조

- 문자열(String)
- 리스트(List)
- 튜플(Tuple)

### 순서가 없는 데이터 구조

- 셋(Set)
- 딕셔너리(Dictionary)

### 얕은 복사와 깊은 복사

- 알고리즘 관련하여 중요하다

---

# 데이터 구조 활용

- 데이터 구조를 활용하기 위해서는 메서드(method)를 활용
    - 메서드는 클래스 내부에 정의한 함수, 사실상 함수와 동일
    - 쉽게 설명하자면 객체의 기능
    - 데이터 구조.메서드() 형태로 활용!
        - 주어.동사() 라고 이해하자

### 활용 예시

```python
List.append(10)
String.split()
```

### 파이썬 공식 문서의 표기법(배커스-나우르 표기법)

- 컴퓨터 언어에서 언어의 문법을 수학적인 수식으로 나타낼 때 사용하는 언어 도구
- 프로그래밍 언어의 구문을 기술하는데 매우 자연스러운 표기법
    - python 구문이 아니며, 배커스-나우르 표기법(문서 표준일 뿐)
    
    ```python
    str.replace(old, new [,count])
    
    # 프로그래밍 언어 문서에서 표기할 때 위와 같이 표기한다
    # old, new는 필수 / [count]는 선택적 인자를 의미함
    # old: 현재 문자열에서 변경하고 싶은 문자
    # new: 새로 바꿀 문자
    # count: 변경할 횟수 / 횟수는 입력하지 않으면 old의 문자열 전체를 변경한다 / 기본값은 전체를 의미하는 count = -1로 지정되어 있음
    ```
    

---

# 순서가 있는 데이터 구조

## 문자열(String Type)

- 문자들의 나열(sequence of characters)
    - 모든 문자는 str 타입(변경 불가능한 immutable)
- 문자열은 작은 따옴표(’)나 큰 따옴표(”)를 활용하여 표기
    - 문자열을 묶을 때 동일한 문장부호를 활용
    - PEP8에서는 소스코드 내에서 하나의 문장부호를 선택하여 유지하도록 함

```python
word = 'ssafy'
print(id(word)) # 1698910375216
word = 'test'
print(id(word)) # 1698910375280

word = 'python'
print(word) # python
print(id(word)) # 2006262763184
print(word.upper()) # PYTHON
print(id(word.upper())) # 2006262763120

# id()는 메모리 주소 확인
# 얼핏보면 word라는 문자열이 변경가능한 것처럼 보이지만, 서로 다른 메모리 별개로 저장됨을 확인할 수 있음
# 기존의 문자열을 변경한 것이 아니라 변경된 문자열을 새롭게 만들어서 반환
# ex) replace, strip, title 등
```

## 문자열 조회 / 탐색 및 검증 메서드

```python
s.find(x) // x의 첫번째 위치를 반환. 없으면 -1을 반환
s.index(x) // x의 첫번째 위치를 반환. 없으면, 오류 발생
# .find(x)와 .index(x)의 차이는 찾는 것이 없을 때 오류를 발생시키느냐 아니냐의 차이다
s.isalpha() // 문자열이 숫자가 아닌 글자로 이루어져 있는가? // 단순 알파벳이 아닌 유니코드 상 Letter(한국어도 포함)
s.isupper() // 문자열이 대문자로 이루어져 있는가?
s.islower() // 문자열이 소문자로 이루어져 있는가?
s.istitle() // 문자열이 타이틀 형식으로 이루어져 있는가?
s.isspace() // 문자열이 공백으로 이루어져 있는가?
s.startswith(x) // 접두문자열이 x인지 확인 // True나 False 반환
s.endswith(x) // 접미문자열이 x인지 확인 // True나 False 반환
```

## 문자열 조회 / 탐색

### .find(x)

- x의 첫번째 위치를 반환. 없으면 -1을 반환

```python
print('apple'.find('p')) # 1
print('apple'.find('k')) # -1
```

### .index(x)

- x의 첫번째 위치를 반환. 없으면 오류 발생

```python
print('apple'.index('p')) # 1
print('apple'.index('k')) # ValueError: substring not found
```

## 문자열 관련 검증 메서드

```python
print('abc'.isalpha()) # True
print('ㄱㄴㄷ'.isalpha()) # True #isalpha()는 숫자냐 아니냐 정도로 생각하면 된다
print('Ab'.isupper()) # False
print('ab'.islower()) # True
print('Title Title!'.istitle()) # True
```

### isdecimal() / isdigit() / isnumeric()

- 가장 엄격한 것이 decimal, 그 다음이 digit, 그 다음이 numeric
- isdecimal()
    - 문자열이 0~9까지의 수로 이루어져 있는가?
- isdigit()
    - 문자열이 숫자로 이루어져 있는가?
- isnumeric()
    - 문자열이 수로 볼 수 있는가?

<img width="883" alt="python_25" src="https://user-images.githubusercontent.com/86648892/181937279-e41387c4-0efa-468c-8f19-abd9721b1a33.png">

<img width="831" alt="python_26" src="https://user-images.githubusercontent.com/86648892/181937276-d1b5ec34-272b-480c-b759-9aeb281634b4.png">

## 문자열 변경 메서드 (S는 문자열)

```python
s.replace(old, new [,count]) # 바꿀 대상이 글자를 새로운 글자로 바꿔서 반환
s.strip([chars]) #공백이나 특정 문자를 제거
s.split(sep = None, maxsplit = -1) # 공백이나 특정 문자를 기준으로 분리
'seperator'.join([iterable]) # 구분자로 iterable을 합침
s.capitalize() # 가장 첫번째 글자를 대문자로 변경
s.title() # 문자열 내 띄어쓰기 기준으로 각 단어의 첫글자를 대문자로, 나머지는 소문자로 반환
s.upper() # 모두 대문자로 변경
s.lower() # 모두 소문자로 변경
s.swapcase() # 대<->소문자 서로 변경
```

### .replace(old, new [,count])

- 바꿀 대상 글자를 새로운 글자로 바꿔서 전환
- count를 지정하면, 해당 개수만큼만 시행

```python
print('coone'.replace('o', 'a')) # caane
print('wooooowoo'.replace('o', '!', 2)) # w!!ooowoo
```

### .strip([chars])

- 특정 문자들을 지정하면
    - 양쪽을 제거하거나(strip), 왼쪽을 제거하거나(lstrip), 오른쪽을 제거(rstrip)
- 문자열을 지정하지 않으면 공백을 제거함
- rstrip([chars])의 경우 오른쪽에서부터 [chars]에 해당하는 모든 문자(공백 포함)를 제거하다가 아닌 것이 나왔을 때 멈춤
    - lstrip([chars])의 경우 왼쪽에서부터 동일

```python
print('    와우!\n'.strip()) # 와우!
print('    와우!\n'.lstrip()) # 와우!
print('    와우!\n'.rstrip()) #     와우!
print('안녕하세요????'.rstrip('?')) # 안녕하세요
```

### .split(sep = None, maxsplit = -1)

- 문자열을 특정한 단위로 나누어 리스트로 반환
    - sep이 None이거나 지정되지 않으면 연속된 공백문자를 단일한 공백문자로 간주하고, 선행 / 후행 공백은 빈 문자열에 포함시키지 않음
    - maxsplit이 -1인 경우에는 제한이 없음

```python
print('a,b,c'.split(',') # ['a', 'b', 'c']
print('a b c',split()) # ['a', 'b', 'c']
print('서울시 강남구 00동'.split()[0]) # 서울시
print('010-1234-5678'.split('-')) # ['010', '1234', '5678']
```

### ‘seperator’.join([iterable])

- split의 반대 느낌
- 반복가능한(iterable) 컨테이너 요소들을 seperator(구분자)로 합쳐 문자열 반환
    - iterable에 문자열이 아닌 값이 있으면 TypeError 발생

```python
print('!'.join('ssafy')) # s!s!a!f!y
print(' '.join(['3', '5'])) # 3 5
```

### 문자열 변경 예시

```python
msg = 'hI! Everyone, I\'m ssafy'

print(msg) # hI! Everyone, I'm ssafy
print(msg.capitalize()) # Hi! everyone, i'm ssafy
print(msg.title()) # Hi! Everyone, I'M Ssafy
print(msg.upper()) # HI! EVERYONE, I'M SSAFY
print(msg.lower()) # hi! everyone, i'm ssafy
print(msg.swapcase()) # Hi! eVERYONE, i'M SSAFY
```

---

## 리스트(List)

- 리스트는 여러 개의 값을 순서가 있는 구조로 저장하고 싶을 때 사용

### 리스트의 생성과 접근

- 리스트는 대괄호([]) 혹은 list()를 통해 작성
    - 파이썬에서는 어떠한 자료형도 저장할 수 있으며, 리스트 안에 리스트도 넣을 수 있음
    - 생성된 이후 내용 변경이 가능 → 가변 자료형
    - 이러한 유연성 때문에 파이썬에서 가장 흔히 사용
- 순서가 있는 시퀀스로 인덱스를 통해 접근 가능
    - 값에 대한 접근은 list[i]

## 리스트 메서드

```python
L.append(x) # 리스트 마지막에 항목 x를 추가
L.insert(i, x) # 리스트 인덱스 i에 항목 x를 삽입
L.remove(x) # 리스트 가장 왼쪽에 있는 항목(첫번째) x를 제거 # 항목이 존재하지 않을 경우, ValueError
L.pop() # 리스트 가장 오른쪽에 있는 항목(마지막)을 반환 후 제거
L.pop(i) # 리스트의 인덱스 i에 있는 항목을 반환 후 제거
L.extend(m) # 순회형 m의 모든 항목들을 리스트 끝에 추가 (+=과 같은 기능)
L.index(x, start, end) # 리스트에 있는 항목 중 가장 왼쪽에 있는 항목 x의 인덱스를 반환 # 일종의 find와 비슷 # start는 찾기 시작할 인덱스, end는 바로 직전까지 찾을 인덱스
L.reverse() # 리스트를 거꾸로 정렬
L.sort() # 리스트를 정렬 (매개변수 이용가능)
L.sort(reverse = True) # 리스트 내림차순 정렬
L.count(x) # 리스트에서 항목 x가 몇개 존재하는지 갯수를 반환

# del list[index] # list의 index에 해당하는 원소 삭제
```

## 값 추가 및 삭제

### .append(x)

- 리스트에 값을 추가함
- a[len(a) : ] = [x]와 동일
- a.insert(len(a), x)와 동일

```python
cafe = ['starbucks', 'tomntoms', 'hollys']
print(cafe) # ['starbucks', 'tomntoms', 'hollys']
cafe.append('banapresso')
print(cafe) # ['starbucks', 'tomntoms', 'hollys', 'banapresso']
```

### .insert(i, x)

- 정해진 위치 i에 x값을 추가함

```python
cafe = ['starbucks', 'tomntoms', 'hollys']
cafe.insert(0, 'start')
print(cafe) # ['start', 'starbucks', 'tomntoms', 'hollys']

cafe = ['starbucks', 'tomntoms', 'hollys']
cafe.insert(len(cafe), 'end')
print(cafe) # ['starbucks', 'tomntoms', 'hollys', 'end']

cafe = ['starbucks', 'tomntoms', 'hollys']
cafe.insert(10000, end)
print(cafe) # ['starbucks', 'tomntoms', 'hollys', 'end']

# i에 들어가는 값이 리스트 길이보다 큰 경우 그냥 맨 뒤에 insert됨
```

### .extend(iterable)

- 리스트에 iterable의 항목을 추가함
- a[len(a) : ] = iterable과 동일

```python
cafe = ['starbucks', 'tomntoms', 'hollys']
cafe.extend(['coffee'])
print(cafe) # ['starbucks', 'tomntoms', 'hollys', 'coffee']

cafe = ['starbucks', 'tomntoms', 'hollys']
cafe += ['coffee']
print(cafe) # ['starbucks', 'tomntoms', 'hollys', 'coffee']

cafe = ['starbucks', 'tomntoms', 'hollys']
cafe.extend('coffee') # 문자열 'coffee'들의 항목이 추가됨
print(cafe) # ['starbucks', 'tomntoms', 'hollys', 'c', 'o', 'f', 'f', 'e', 'e']
```

### .remove(x)

- 리스트에서 값이 x인 것을 삭제

```python
numbers = [1, 2, 3, 'hi']
print(numbers)
numbers.remove('hi')
print(numbers) # [1, 2, 3]

numbers.remove('hi')
# ValueError: list.remove(x): x not in list
# 없는 것을 remove할 경우 ValueError 발생
```

### .pop(i)

- 정해진 위치 i에 있는 값을 삭제하고, 그 항목을 반환함
- i가 지정되지 않으면, 마지막 항목을 삭제하고 반환함

```python
numbers = ['hi', 1, 2, 3]
print(numbers) # ['hi', 1, 2, 3]
numbers.pop()
print(numbers) # ['hi', 1, 2]

numbers = ['hi', 1, 2, 3]
print(numbers) # ['hi', 1, 2, 3]
numbers.pop(0)
print(numbers) # [1, 2, 3]
```

### .clear()

- 모든 항목을 삭제함

```python
numbers = [1, 2, 3]
print(numbers) # [1, 2, 3]
numbers.clear()
print(numbers) # []
```

## 탐색 및 정렬

### .index(x)

- x값을 찾아 해당 index 값을 반환
- x값이 없는 경우 ValueError

```python
numbers = [1, 2, 3, 4]
print(numbers.index(3)) # 2
print(numbers.index(100) # ValueError: 100 is not in list
```

### .count(x)

- 원하는 값의 개수를 반환함

```python
numbers = [1, 2, 3, 1, 1]

print(numbers.count(1)) # 3
print(numbers.count(100)) # 0
```

```python
# 원하는 값 모두 삭제하기

a = [1, 2, 1, 3, 4]
target_value = 1
for i in range(a.count(target_value)):
    a.remove(target_value)
print(a) # [2, 3, 4]
```

### .sort()

- 원본 리스트를 정렬함
- None을 반환
- sorted 함수와 비교할 것
    - sorted는 원본 리스트를 변경하지 않고 정렬된 새로운 리스트를 반환함

```python
# 원본 변경 sort()
numbers = [3, 2, 5, 1]
result = numbers.sort()
print(numbers, result) # [1, 2, 3, 5] None

# 원본 내림차순 정렬 sort(reverse = True)
numbers = [3, 2, 5, 1]
result = numbers.sort(reverse = True)
print(numbers, result) # [5, 3, 2, 1] None

# 새로운 정렬 리스트 반환 및 원본 변경 없음 sorted()
numbers = [3, 2, 5, 1]
result = sorted(numbers)
print(numbers, result) # [3, 2, 5, 1] [1, 2, 3, 5]
```

### .reverse()

- 원본의 순서를 반대로 뒤집음
- 정렬하는 것이 아님!

```python
numbers = [3, 2, 5, 1]
result = numbers.reverse()
print(numbers, result) # [1, 5, 2, 3] None
```

---

## 튜플(Tuple)

### 튜플의 정의

- 튜플은 여러 개의 값을 순서가 있는 구조로 저장하고 싶을 때 사용
    - 리스트와의 차이점은 생성 후, 담고 있는 값 변경이 불가 (불변 자료형)
- 항상 소괄호 형태로 사용

### 튜플 관련 메서드

- 튜플은 변경할 수 없기 때문에 값에 영향을 미치지 않는 메서드만을 지원
- 리스트 메서드 중 항목을 변경하는 메서드들을 제외하고 대부분 동일

```python
T.index(x[, start[, end]]) # x가 처음 나오는 인덱스 # x없을 시 error
T.count(x) # x의 개수
```

```python
day_name = ('월', '화', '수', '목', '금')
print(type(day_name)) # <class 'tuple'>

# 인덱스로 접근
print(day_name[-2]) # 목

# 반복결합 연산자
print(day_name * 2) # ('월', '화', '수', '목', '금', '월', '화', '수', '목', '금')
print(id(day_name)) # 1909158923696

# 확장연산자: 값을 병합해서 재할당
# 그러나 extend는 값을 변경하기 때문에 지원하지 않음
day_name += False, True
print(day_name) # ('월', '화', '수', '목', '금', False, True)
print(id(day_name) # 1909160279008

# 위아래 id()의 결과가 다른 것을 통해 원본인 day_name이 변한 것이 아니라 새로 만든 것임을 알 수 있다
```

---

# 연산자

## 멤버십 연산자(Membership Operator)

- 멤버십 연산자 in을 통해 특정 요소가 속해 있는지 여부 확인
- 포함 여부 확인
    - in
    - not in

```python
# 리스트
1 in [3, 2] # False

# 튜플
4 in (1, 2, 'hi') # False

# range
-3 in range(3) # False

# 문자열
'a' in 'apple' # True

# not in
'b' not in 'apple' # True
```

```python
print('apple' in 'a') # False
print('a' in 'apple') # True
print('hi' in 'hi I am ssafy') # True
print('서순' in ['요까일엇무', '기러기', '서순']) # True
```

## 시퀀스형 연산자(Sequence Type Operator)

- 산술연산자 (+)
    - 시퀀스 간의 concatenation (연결 / 연쇄)

```python
# 리스트
[1, 2] + ['a'] # [1, 2, 'a']

# 튜플
(1, 2) + ('a',) # (1, 2, 'a')

# range
range(2) + range(2, 5) # TypeError: unsupported operand type

# 문자열
'12' + 'b' # '12b'
```

- 반복연산자 (*)
    - 시퀀스를 반복

```python
# 리스트
[0] * 8 # [0, 0, 0, 0, 0, 0, 0, 0]

# 튜플
(1, 2) * 3 # (1, 2, 1, 2, 1, 2)

# range
range(1) * 3 # TypeError: unsupported operand type

# 문자열
'hi' * 3 # 'hihihi'
```

---

# 비시퀀스형 데이터 구조

## 셋(Set)

- Set이란 중복되는 요소가 없이, 순서에 상관없는 데이터들의 묶음
    - 데이터의 중복을 허용하지 않기 때문에 중복되는 원소가 있다면 하나만 저장
    - 순서가 없기 때문에 인덱슬르 이용한 접근 불가능
- 수학에서의 집합을 표현한 컨테이너
    - 집합 연산이 가능(여집합을 표현하는 연산자는 별도로 존재 x)
    - 중복된 값이 존재하지 않음
- 담고 있는 요소를 삽입 변경, 삭제 가능 → 가변 자료형(mutable)

## 셋 메서드

```python
s.copy() # 셋의 얕은 복사본을 반환
s.add(x) # 항목 x가 셋 s에 없다면 추가
s.pop() # 셋 s에서 랜덤하게 항목을 반환하고, 해당 항목을 제거 # set이 비어있을 경우, KeyError
s.remove(x) # 항목 x를 셋 s에서 삭제 # 항목이 존재하지 않을 경우, KeyError
s.discard(x) # 항목 x가 셋 s에 있는 경우, 항목 x를 셋 s에서 삭제
s.update(t) # 셋 t에 있는 모든 항목 중 셋 s에 없는 항목을 추가
s.clear() # 모든 항목을 제거
s.isdisjoint(t) # 셋 s가 셋 t와 서로 같은 항목을 하나라도 갖고 있지 않은 경우, True 반환
s.issubset(t) # 셋 s가 셋 t의 하위 셋인 경우, True 반환
s.issuperset(t) # 셋 s가 셋 t의 상위 셋인 경우, True 반환
```

## 추가 및 변경

### .add(elem)

- 셋에 값을 추가

```python
a = {'사과', '바나나', '수박'}
print(a) # {'바나나', '사과', '수박'}
a.add('딸기')
print(a) # {'바나나', '딸기', '사과', '수박'}
```

### .update(*others)

- 여러 값을 추가

```python
a = {'사과', '바나나', '수박'}
print(a) # {'바나나', '사과', '수박'}
a.update(['딸기', '바나나', '참외'])
print(a) # {'참외', '바나나', '딸기', '수박', '사과'}
```

## 요소 삭제

### .remove(elem)

- Set에서 삭제하고, 없으면 KeyError
- 무조건 없애야 할 값이 있다면 remove 사용

```python
a = {'사과', '바나나', '수박'}
print(a) # {'바나나', '사과', '수박'}
a.remove('사과')
print(a) # {'바나나', '수박'}
a.remove('애플')
print(a) # KeyError: '애플'
```

### .discard(elem)

- Set에서 삭제하고 없어도 에러가 발생하지 않음
- 어떤 값이 있는지 없는지 잘모르겠는데 일단 없앤다고 하자는 느낌이면 discard 사용 가능

```python
a = {'사과', '바나나', '수박'}
print(a) # {'바나나', '사과', '수박'}
a.discard('사과')
print(a) # {'바나나', '수박'}
a.discard('애플')
print(a) # {'바나나', '수박'} # 에러가 발생하지 않고 그대로 유지됨
```

### .pop()

- 임의의 원소를 제거해 반환
- 순서가 없기에 무엇이 제거될지 모름

```python
a = {'사과', '바나나', '수박'}
print(a) # {'바나나', '사과', '수박'}
a.pop()
print(a) # {'사과', '수박'}

a = {'1', '2', '3'}
print(a) # {'3', '1', '2'}
a.pop()
print(a) # {'1', '2'}
```

## 모두 삭제

### .clear()

- 모든 항목을 제거

```python
a = {'사과', '바나나', '수박'}
print(a) # {'바나나', '사과', '수박'}
a.clear()
print(a) # set()
```

## 집합 관련 함수

- s.isdisjoint(t)
    - 셋 s가 셋 t의 서로 같은 항목을 하나라도 갖고 있지 않은 경우, True 반환 (서로소)
- s.issubset(t)
    - 셋 s가 셋 t의 하위 셋인 경우, True 반환
- s.issuperset(t)
    - 셋 s가 셋 t의 상위 셋인 경우, True 반환

```python
a = {'사과', '바나나', '수박'}
b = {'포도', '망고'}
c = {'사과', '포도', '망고', '수박', '바나나'}

print(a.isdisjoint(b)) # True # a와 b는 서로소인가?
print(b.issubset(c)) # True # b가 c의 하위셋인가?
print(a.issuperset(c)) # False # a가 c의 상위셋인가?
```

---

# 딕셔너리

## 딕셔너리의 정의

- 키-값(key-value) 쌍으로 이루어진 자료형 (3.7부터는 ordered, 이하 버전은 unordered)
- Dictionary의 키(key)
    - key는 변경 불가능한 데이터(immutable)만 활용 가능
        - string, integer, float, boolean, tuple, range
- 각 키의 값(values)
    - 어떠한 형태든 관계없음

## 딕셔너리 메서드

```python
d.clear() # 모든 항목을 제거
d.copy() # 딕셔너리 d의 얕은 복사본을 반환
d.keys() # 딕셔너리 d의 모든 키를 담은 뷰를 반환
d.values() # 딕셔너리 d의 모든 값을 담은 뷰를 반환
d.items() # 딕셔너리 d의 모든 키-값의 쌍을 담은 뷰를 반환
d.get(k) # 키 k의 값을 반환하는데, 키 k가 딕셔너리 d에 없을 경우 None을 반환
d.get(k, v) # 키 k의 값을 반환하는데, 키 k가 딕셔너리 d에 없을 경우 v를 반환
d.pop(k) # 키 k의 값을 반환하고 키 k인 항목을 딕셔너리 d에서 삭제하는데, 키 k가 딕셔너리 d에 없을 경우 KeyError 발생
d.pop(k, v) # 키 k의 값을 반환하고 키 k인 항목을 딕셔너리 d에서 삭제하는데, 키 k가 딕셔너리 d에 없을 경우 v를 반환
d.update([other]) # 딕셔너리 d의 값을 매핑하여 업데이트

# .get(key)와 ['key']의 차이는 전자의 경우 없을 경우 None을 반환, 후자의 경우 KeyError 발생
# 딕셔너리 순회는 기본적으로 key를 순회함
```

## 조회

### .get(key[,default])

- key를 통해 value를 가져옴
- KeyError가 발생하지 않으며, default 값을 설정할 수 있음 (기본: None)

```python
my_dict = {'apple': '사과', 'banana': '바나나'}
my_dict['pineapple'] # KeyError: 'pineapple'

my_dict = {'apple': '사과', 'banana': '바나나'}
print(my_dict.get('pineapple')) # None
print(my_dict.get('apple')) # 사과
print(my_dict.get('pineapple', 0)) # 0
```

### .setdefault(key[,default])

- get()은 단순히 딕셔너리를 해당 key에서 조회하여 None이나 해당값을 반환해주는 것이며, 딕셔너리에는 변화가 없음
- setdefault()는 해당 key가 있다면 해당 key의 값을 조회하게 되지만, 만약 해당 key가 없다면 기입한 key의 값을 (None 포함) 기존 딕셔너리에 박아넣음

```python
my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}

# get()
my_dict.get('pineapple') # None 반환
print(my_dict) # {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}
my_dict.get('pineapple', '파인애플') # 파인애플 반환
print(my_dict) # {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}

# setdefault()
my_dict.setdefault('pineapple') # None 반환
print(my_dict) # {'apple': '사과', 'banana': '바나나', 'melon': '멜론', 'pineapple': None}
my_dict.setdefault('pineapple', '파인애플') # 파인애플 반환
	print(my_dict) # {'apple': '사과', 'banana': '바나나', 'melon': '멜론', 'pineapple': '파인애플'}
```

## 추가 및 삭제

### .pop(key[,default])

- key가 딕셔너리에 있으면 제거하고 해당 값을 반환
- 그렇지 않으면 default를 반환
- default값이 없으면 KeyError

```python
my_dict = {'apple': '사과', 'banana': '바나나'}
data = my_dict.pop('apple')
print(data, my_dict) # 사과 {'banana': '바나나'}

my_dict = {'apple': '사과', 'banana': '바나나'}
data = my_dict.pop('pineapple')
print(data, my_dict) # KeyError: 'pineapple'

my_dict = {'apple': '사과', 'banana': '바나나'}
data = my_dict.pop('pineapple', 0)
print(data, my_dict) # 0 {'apple': '사과', 'banana': '바나나'}
```

### .update()

- 값을 제공하는 key, value로 덮어씀

```python
my_dict = {'apple': '사', 'banana': '바나나'}
my_dict.update(apple = '사과')
print(my_dict) # {'apple': '사과', 'banana': '바나나'}

my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}
d = {'mango': '망고', 'watermelon': '수박'}
my_dict.update(d)
print(my_dict) # {'apple': '사과', 'banana': '바나나', 'melon': '멜론', 'mango': '망고', 'watermelon': '수박'}
```

## 순회

```python
my_dict = {'apple': '사과', 'banana': '바나나'}

# 기본적으로 key를 순회
for key in my_dict:
	print(key)
'''
apple
banana
'''
# values()
for value in my_dict.values():
	print(value)
'''
사과
바나나
'''
# items()
for key, value in my_dict.items():
	print(f'key: {key} / value: {value}')
'''
key: apple / value: 사과
key: banana / value: 바나나
'''
```

---

# 얕은 복사와 깊은 복사(Shallow Copy & Deep Copy)

## 데이터 분류

- 변경 불가능한(immutable) 데이터
    - 리터럴(Literal)
        - 숫자(Number)
        - 글자(String)
        - 참 / 거짓(Bool)
    - range()
    - tuple()
    - frozenset()
- 변경 가능한(mutable) 데이터
    - list
    - dict
    - set
- immutable한 객체들(int, float 등)은 얕은 복사를 하든 깊은 복사를 하든 해당 객체들은 값이 변경되면 무조건 참조가 변경됨
- 결론적으로 얕은 복사, 깊은 복사에 대해 구분하고 학습해야 하는 객체는 immutable한 객체들이 아니라, list, set, dictionary와 같은 mutable한 객체들이다

## 파이썬에서 데이터를 복사하는 방법

- 할당(Assignment)
- 얕은 복사(Shallow Copy)
- 깊은 복사(Deep Copy)

## 할당(assignment)

- 대입 연산자(=)
    - 리스트 복사 확인하기
    
    ```python
    original_list = [1, 2, 3]
    copy_list = original_list
    print(original_list, copy_list) # [1, 2, 3] [1, 2, 3]
    
    copy_list[0] = 'hello'
    print(original_list, copy_list) # ['hello', 2, 3] ['hello', 2, 3]
    ```
    
- 대입 연산자를 통한 복사는 해당 객체에 대한 객체 참조를 복사!
    - 내용물까지 주는 것이 아니라 주소만 준다
    - 즉, A1이라는 박스를 너도 보렴이라는 느낌
    - 안에 내용물이 바뀌면 당연히 같이 보던 친구도 바뀐 내용을 갖게 됨
- 이로 인해 해당 주소의 일부 값을 변경하는 경우 이를 참조하는 모든 변수에 영향

<img width="500" alt="python_27" src="https://user-images.githubusercontent.com/86648892/181937464-86698168-a647-4870-b26c-6b5a98af839c.png">

## 얕은 복사(shallow copy)

- 위의 경우처럼 객체 참조를 복사하는 것을 얕은 복사라 한다
- 해결 방법은?
    - slice 연산자 활용
    - list() 활용
    - 둘 다 여전히 얕은 복사이긴 하다
- Slice 연산자 활용하여 같은 원소를 가진 리스트지만 연산된 결과를 복사할 수 있다 (다른 주소)
    - 즉, 내용물까지 복사하여 하나 새로 만드는 것
    
    ```python
    a = [1, 2, 3]
    b = a[:]
    print(a, b) # [1, 2, 3] [1, 2, 3]
    b[0] = 5
    print(a, b) # [1, 2, 3][5, 2, 3]
    ```
    
    <img width="525" alt="python_28" src="https://user-images.githubusercontent.com/86648892/181937468-1ca06e80-138c-4838-a3c8-b95ad8677f16.png">
    
- list()도 활용 가능

```python
a = [1, 2, 3]
b = list(a)
print(b) # [1, 2, 3]
b[0] = 5
print(a) # [1, 2, 3]
```

### 얕은 복사(shallow copy) 주의사항

- 복사하는 리스트의 원소가 주소를 참조하는 경우
    - 예를 들어, 리스트 안에 리스트가 다시 들어가는 2차원 리스트의 경우
    - 슬라이싱을 통한 복사에 한계가 생긴다

```python
a = [1, 2, ['a', 'b']]
b = a[:]
print(a, b) # [1, 2, ['a', 'b']] [1, 2, ['a', 'b']]
b[2][0] = 0
print(a, b) # [1, 2, ['0', 'b']] [1, 2, ['0', 'b']]

# b자체는 a와 별도로 저장한 것이지만, 그 안의 원소인 'a'와 'b'는 참조 복사 상태
```

<img width="510" alt="python_29" src="https://user-images.githubusercontent.com/86648892/181937470-983655ff-7b28-41ff-bc3e-8334874096e1.png">

![python_30](https://user-images.githubusercontent.com/86648892/181937471-66c64744-fe9b-48b1-80c2-10cb17d549d4.png)


### WHY 얕은 복사?

- 컴퓨터는 0과 1만 기억할 수 있기에 다른 언어들 같은 경우 long, int와 같은 식으로 숫자도 범위가 있다. 예를 들어 int는 2칸, long은 4칸과 같이 쓸 수 있는 칸이 다르다. 효율적으로 만들기 위해서는 long, int 등 자료형을 내가 지정하여 레고처럼 쓸 수 있다. 가령 10칸을 사용해야 한다고 하면, 4칸짜리 하나, 4칸짜리 하나, 2칸짜리 하나 이런 식이다. 이런 식으로 프로그램을 만들면 코드가 효율적이다.
- 그런데 파이썬은 이런 것이 없다. long, int 구분 없이 모두 int다. 이런 문제를 해결하기 위해서 주소 참조를 사용한다. 가령 진짜 큰 수가 있으면 어딘가에 넣어두고, 주소만 들고오는 식이다.
- 어떤 언어에는 여러 개를 담는 자료구조에 한가지 자료형만 넣을 수 있는 경우가 있다. 파이썬의 경우 pandas(데이터 분석용 라이브러리)에 있는 array다. 여기는 숫자만 넣을 수 있다. 이 친구의 경우 계산을 효율적으로 하기 위해 칸 수가 똑같다. 왜냐하면 박스에 숫자만 넣을 것이어서 그렇다.
- 하지만 파이썬은 어차피 주소만 들고 오기 때문에 데이터 박스에 리스트, 숫자, 문자열이 들어가든 상관없다.

## 깊은 복사(deep copy)

- 슬라이싱을 통한 얕은 복사 해결에 한계가 있다
- import copy를 통해 copy 모듈을 들고와야 한다
- 나중에 알고리즘에서 2차원 이상의 리스트를 많이 사용하기에 복사할 일이 있다면 deepcopy를 사용해야 한다고 생각하면 좋다

```python
import copy
a = [1, 2, ['a', 'b']]
b = copy.deepcopy(a)
print(a, b) # [1, 2, ['a', 'b']] [1, 2, ['a', 'b']]
b[2][0]
print(a, b) # [1, 2, ['a', 'b']] [1, 2, ['0', 'b']]
```

<img width="552" alt="python_31" src="https://user-images.githubusercontent.com/86648892/181937472-8ccb6450-9d98-49d1-9918-81b3489807e3.png">

---

# 추가 정리

```python
a = 3
b = 4
b = a
print(f'a = {a}, b = {b}') # a = 3, b = 3
a = 5
print(f'a = {a}, b = {b}') # a = 5, b = 3

# 여러 개의 원소가 있는 데이터가 아닌 하나의 값을 가진 데이터는 얕은 복사가 아닌 값의 복사가 일어남
```

![python_32](https://user-images.githubusercontent.com/86648892/181937473-03874581-468a-41bf-9b8e-3109c5204c96.png)

![python_33](https://user-images.githubusercontent.com/86648892/181937474-d0f54eeb-876c-455f-9dd2-8ab24dc2ada0.png)

- 위의 사진처럼 단일값의 데이터인 경우 Objects에서 관리하지 않음
- 여러 원소를 가진 데이터의 경우 Objects에서 관리함
- dir()를 통해 내장함수를 출력해서 확인할 수 있다
    - dir(’string’)
    - dir(list)
    - dir(set)
    - dir(dict)
- 딕셔너리에서 get(key)와 [key]의 차이점
    - get(key)는 해당 키가 없더라도 KeyError가 발생하지 않고 None을 반환
    - get(key, n)을 통해 key가 없을 시 n을 반환하도록 설정 역시 가능
---
# Python #4
- OOP
- class / instance
- abstraction / inheritance / polymorphism / encapsulation
- error / exception handling
---
# OOP

## 개요

- 객체지향 프로그래밍(OOP)
    - 객체지향 프로그래밍이란?
    - OOP 기초
        - 객체 / 인스턴스 / 클래스
        - 클래스
        - 메서드
- 객체지향의 핵심 개념
    - 추상화
    - 상속
    - 다형성
    - 캡슐화
- 에러와 예외

---

# 객체지향 프로그래밍

- 객체지향 프로그래밍(Object-Oriented Programming, OOP)은 컴퓨터 프로그래밍의 패러다임 중 하나이다
- 객체지향 프로그래밍은 컴퓨터 프로그램을 명령어의 목록으로 보는 시각에서 벗어나
- 여러 개의 독립된 단위, 즉 '객체'들의 모임으로 파악하고자 하는 것이다
    - 객체란 2가지, ‘정보와 행동'을 가지고 있는 것
    - 정보는 곧 변수
    - 행동은 곧 함수
- 각각의 객체는 메시지를 주고받고, 데이터를 처리할 수 있다

## 객체지향 프로그래밍이란?

- 프로그램을 여러 개의 독립된 객체들과, 그 객체 간의 상호작용으로 파악하는 프로그래밍 방법
- 예시
    - 콘서트
        - 가수 객체
        - 감독 객체
        - 관객 객체

## 절차지향 프로그래밍

<img width="652" alt="python_34" src="https://user-images.githubusercontent.com/86648892/181940365-5b7f80a0-decd-4cee-8854-a8961dbd2817.png">

- 과거에는 위처럼 Global Data라는 하나의 꾸러미에서 절차들을 계속 입력하는 형태로 프로그래밍을 했음
- 데이터와 함수로 인한 변화

## 객체지향 프로그래밍

<img width="619" alt="python_35" src="https://user-images.githubusercontent.com/86648892/181940382-c6041019-4bad-448c-878e-2c47c760e932.png">

- 데이터와 기능(메서드)을 분리해줌
- 추상화된 구조를 만듬(인터페이스)

## 객체지향 프로그래밍이 필요한 이유

- 추상화
    - 추상화란 복잡한 것을 숨기고 필요한 것만 드러내는 것
    - 현실 세계를 프로그램 설계에 반영할 수 있음
    
    ```python
    class Person:
    	def __init__(self, name, gender):
    		self.name = name
    		self.gender = gender
    
    	def greeting(self):
    		print(f'안녕하세요, {self.name}입니다.')
    
    jimin = Person('지민', '남')
    jimin.greeting() # 안녕하세요, 지민입니다.
    
    jieun = Person('아이유', '여')
    jieun.greeting() # 안녕하세요, 아이유입니다.
    ```
    

## 객체지향의 장점 / 단점

### 장점

- 클래스 단위로 모듈화시켜 개발할 수 있으므로 많은 인원이 참여하는 대규모 소프트웨어 개발에 적합
    - 예를 들어 저는 ‘로그인 기능' 그쪽은 ‘게시판 기능'을 담당합시다
- 필요한 부분만 수정하기 쉽기 때문에 프로그램의 유지보수가 쉬움

### 단점

- 설계 시 많은 노력과 시간이 필요함
    - 다양한 객체들의 상호 작용 구조를 만들기 위해 많은 시간과 노력이 필요
- 실행 속도가 상대적으로 느림
    - 절차지향 프로그래밍이 컴퓨터의 처리구조와 비슷해서 실행 속도가 빠름

---

# OOP 기초

## 객체

- 컴퓨터 과학에서 객체 또는 오브젝트(object)는 클래스에서 정의한 것을 토대로 메모리(실제 저장공간)에 할당된 것으로 프로그램에서 사용되는 데이터 또는 식별자에 의해 참조되는 공간을 의미하며, 변수, 자료구조, 함수 또는 메서드가 될 수 있다
- 쉽게 말해 속성과 행동으로 구성된 모든 것

## 클래스와 객체

- 클래스는 일종의 설계도, 객체는 실제 사례
- 클래스로 만든 객체를 인스턴스라고도 함
- 클래스 가수 객체 이찬혁
    - 이찬혁은 객체이다 (o)
    - 이찬혁은 인스턴스이다 (x)
    - 이찬혁은 가수의 인스턴스이다 (o)
- 클래스를 만든다 == 타입을 만든다

## 객체

- 파이썬은 모든 것이 객체(object)인, 객체 지향 프로그래밍 언어이다
    - 모든 객체는 특정 타입의 인스턴스
    - 파이썬의 모든 것엔 속성과 행동이 존재
        - [3, 2, 1].sort()
            - 리스트.정렬()
                - 객체.행동()
        - ‘banana’.upper()
            - 문자열.대문자로()
                - 객체.행동()
- 객체(object)는 특정 타입의 인스턴스(instance)이다
- 객체(object)의 특징
    - 타입(type): 어떤 연산자(operator)와 조작(method)이 가능한가?
    - 속성(attribute): 어떤 상태(데이터)를 가지는가?
    - 조작법(method): 어떤 행위(함수)를 할 수 있는가?
    
    <img width="648" alt="python_36" src="https://user-images.githubusercontent.com/86648892/181940387-40ab361b-821b-4b28-9383-74db40812ed3.png">
    

---

# 객체와 클래스 문법

## 기본 문법

```python
class MyClass: # 클래스 정의
my_instance = MyClass() # 인스턴스 생성
my_instance.my_method() # 메서드 호출
my_instance.my_attribute # 속성

class Person:
	pass
print(type(Person)) # <class 'type'>

person1 = Person()

print(isinstance(person1, Person)) # True
print(type(person1)) # <class '__main__.Person'>
```

## 객체 비교하기

- ==
    - 동등한(equal)
    - 변수가 참조하는 객체가 동등한(내용이 같은) 경우 True
        - 주소가 다르더라도 그 안의 내용물이 같으면 됨
    - 두 객체가 같아 보이지만 실제로 동일한 대상을 가리키고 있다고 확인해준 것은 아님
    - 쌍둥이같은 느낌
- is
    - 동일한(identical)
    - 두 변수가 동일한 객체를 가리키는 경우 True
        - 주소까지 같아야 됨
    - 분신술같은 느낌

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b, a is b) # True False

a = [1, 2, 3]
b = a

print(a == b, a is b) # True True
```

---

# OOP 속성

## 속성

- 데이터, 정보, 상태, 즉 변수
- 특정 데이터 타입 / 클래스의 객체들이 가지게 될 상태 / 데이터를 의미
- 클래스 변수 / 인스턴스 변수가 존재

```python
class Person:
	blood_color = 'red' # 클래스 변수
	population = 100 # 클래스 변수

	def __init__(self, name):
		self.name = name # 인스턴스 변수

person1 = Person('지민')
print(person1.name) # 지민
```

## 인스턴스 변수

- 인스턴스 변수란?
    - 인스턴스가 개인적으로 가지고 있는 속성(attribute)
    - 각 인스턴스들의 고유한 변수
- 생성자 메서드(__init__)에서 self.<name>으로 정의
- 인스턴스가 생성된 이후 <instance>.<name>으로 접근 및 할당

```python
class Person:
	def __init__(self, name, mbti): # 인스턴스 변수 정의
		self.name = name
		self.mbti = mbti

john = Person('john')
print(john.name) # john # 인스턴스 변수 접근
john.name = 'John Kim' # 인스턴스 변수 할당
print(john.name) # John Kim

# 파이썬에서는 인스턴스마다 따로 값을 가지는 인스턴스 변수의 경우 initializer 괄호 안에서 모두 선언
# initializer의 첫번째 파라미터는 self
```

## 클래스 변수

- 한 클래스의 모든 인스턴스가 공유하는 값을 의미
- 같은 클래스의 인스턴스들은 같은 값을 갖게 됨
    - ex) 특정 사이트의 User 수 등은 클래스 변수 사용
- 클래스 선언 내부에서 정의
- <classname>.<name>으로 접근 및 할당
- 인스턴스.클래스변수로 접근 가능!
    - 인스턴스.클래스변수 = x로 새로 할당한 경우, 해당 인스턴스만 바뀜
    
    ```python
    class Circle():
    	pi = 3.14 # 클래스 변수 정의
    
    	def __init__(self, r):
    		self.r = r # 인스턴스 변수 정의
    
    c1 = Circle(5)
    c2 = Circle(10)
    
    print(Circle.pi) # 3.14
    print(c1.pi) # 3.14
    print(c2.pi) # 3.14
    
    Circle.pi = 5
    print(Circle.pi) # 5
    print(c1.pi) # 5
    print(c2.pi) # 5
    ```
    

## 클래스 변수 활용(사용자 수 계산하기)

- 사용자가 몇 명인지 확인하고 싶다면?
    - 인스턴스가 생성될 때마다 클래스 변수가 늘어나도록 설정하면됨
    
    ```python
    class Person:
    	count = 0
    	# 인스턴스 변수 설정
    	def __init__(self, name):
    		self.name = name
    		Person.count += 1
    
    person1 = Person('아이유')
    person2 = Person('이찬혁')
    
    print(Person.count) # 2
    ```
    

## 클래스 변수와 인스턴스 변수

- 클래스 변수를 변경할 때는 항상 클래스.클래스변수 형식으로 변경

```python
class Circle():
	pi = 3.14

	def __init__(self, r):
		self.r = r

c1 = Circle(5)
c2 = Cirlce(10)

print(Circle.pi) # 3.14
print(c1.pi) # 3.14 # 선언된 인스턴스 변수에서 찾을 수 없을 때 클래스 변수에서 찾아 가져옴
print(c2.pi) # 3.14

# 클래스 변수 변경한 경우
Circle.pi = 5
print(Circle.pi) # 5
print(c1.pi) # 5
print(c2.pi) # 5

# 인스턴스 변수 변경한 경우
c2.pi = 5
print(Circle.pi) # 3.14
print(c1.pi) # 3.14
print(c2.pi) # 5 # 새로운 인스턴스 변수가 생성됨
```

---

# OOP 메서드

## 메서드

- 특정 데이터 타입 / 클래스의 객체에 공통적으로 적용가능한 행위(함수)

```python
class Person:
	def talk(self):
		print('안녕')

	def eat(self, food):
		print(f'{food}를 냠냠')

person1 = Person()
person1.talk() # 안녕
person1.eat('피자') # 피자를 냠냠
person1.eat('치킨') # 치킨를 냠냠
```

## 메서드의 종류

- 인스턴스 메서드
    - 인스턴스를 처리
        - 대개 인스턴스의 변수를 처리함
        - self가 있으면 인스턴스 메서드라고 생각
- 클래스 메서드
    - 클래스를 처리
        - 클래스 변수 등을 처리
- 정적 메서드
    - 나머지

<img width="528" alt="python_37" src="https://user-images.githubusercontent.com/86648892/181940392-1f158ab2-22e3-4db2-86bf-cc7fd74f9248.png">

---

## 인스턴스 메서드

- 인스턴스 변수를 사용하거나, 인스턴스 변수에 값을 설정하는 메서드
- 클래스 내부에 정의되는 메서드의 기본
- 호출 시, 첫번째 인자로 인스턴스 자기자신(self)이 자동으로 전달됨

```python
class MyClass:
	def instance_method(self, arg1, ...):

my_instance = MyClass()
my_instance.instance_method(arg1, ...)
```

## self

- 인스턴스 자기자신
- 파이썬에서 인스턴스 메서드는 호출 시 첫번째 인자로 인스턴스 자신이 전달되게 설계
    - 매개변수 이름으로 self를 첫번째 인자로 정의
    - 다른 단어로도 작동하지만, 파이썬의 암묵적인 규칙

## 생성자(constructor) 메서드

- 인스턴스 객체가 생성될 때 자동으로 호출되는 메서드
- 인스턴스 변수들의 초기값을 설정
    - 인스턴스 생성
    - __init__메서드 자동 호출
    
    ```python
    class Person:
    	def __init__(self):
    		print('인스턴스가 생성되었습니다.')
    
    person1 = Person() # 인스턴스가 생성되었습니다.
    
    class Person:
    	def __init__(self, name):
    		print(f'인스턴스가 생성되었습니다. {name}')
    
    person1 = Person('지민') # 인스턴스가 생성되었습니다. 지민
    ```
    

## 매직 메서드

- Double Underscore(__)가 있는 메서드는 특수한 동작을 위해 만들어진 메서드로, 스페셜 메서드 혹은 매직 메서드라고 불림
- 특정 상황에 자동으로 불리는 메서드
- 매직 메서드도 인스턴스 메서드이다
    - self에 적용
- 예시

```python
__str__(self) # 객체를 문자열로 반환하여 출력 # string
__len__(self) # 객체의 길이를 판단할 수 있도록 구현 # length
__repr__(self) # 객체를 문자열로 표현 # representation
__lt__(self, other) # < 연산자에 대한 동작을 정의 # less than
__le__(self, other) # <= 연산자에 대한 동작을 정의 # less than and equal
__eq__(self, other) # == 연산자에 대한 동작을 정의 # equal
__gt__(self, other) # > 연산자에 대한 동작을 정의 # greater than
__ge__(self, other) # >= 연산자에 대한 동작을 정의 # greater than and equal
__ne__(self, other) # != 연산자에 대한 동작을 정의 # not equal

# 인스턴스 메서드니까 개별이다
```

```python
# __str__과 __repr__는 모두 객체를 문자열로 반환한다는 공통점
# 차이점은 서로 다른 목적

# __str__
a = 1
b = 'hi'
c = [1, 2, 3]
print(a, b, c) # 1 hi [1, 2, 3] # 이처럼 print는 내부적으로 str 메소드를 호출 # 서로 다른 타입의 데이터임에도 __str__ 메소드를 통해 문자열이라는 하나의 형태로 통일되었기 때문

class test:
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return f'Hello, my name is {self.name}'

	def __repr__(self):
		return f'Hello, my name is {self.name}'

test1 = test('fox')

print(a, b, c, test1) # 1 hi [1, 2, 3] Hello, my name is fox

# 이처럼 str 메소드는 서로 다른 타입을 가진 데이터끼리 상호작용할 때 문자열 변환시킴으로써 상호간의 호환이 가능하도록 하는 interface로서의 역할 수행

# __repr__ (representation)
# repr 메소드는 객체를 문자열로 표현하기 위해 존재

# Class 객체 출력 시 __str__과 __repr__이 정의되지 않았다면 메모리 주소를 출력, 둘 다 정의되어있다면 출력 우선순위는 1)__str__ 2)__repr__
```

- 객체의 특수 조작 행위를 지정(함수, 연산자 등)
    - __str__: 해당 객체의 출력 형태를 지정
        - 프린트 함수를 호출할 때, 자동으로 호출
        - 어떤 인스턴스를 출력하면 __str__의 return 값
    - __gt__: 부등호 연산자(>, greater than)
        - ex) 이찬혁 > 교수
            - 돈? 키? 매력?
                - __gt__를 바꿔주면 됨

## 매직 메서드 예시

```python
class Circle:
	def __init__(self, r):
		self.r = r

	def area(self):
		return 3.14 * self.r * self.r

	def __str__(self):
		return f'[원] radius: {self.r}'

	def __gt__(self, other):
		return self.r > other.r

c1 = Circle(10)
c2 = Circle(1)

print(c1) # [원] radius: 10
print(c2) # [원] radius: 1
print(c1 > c2) # True
print(c1 < c2) # False
```

## 소멸자(destructor) 메서드

- 인스턴스 객체가 소멸(파괴)되기 직전에 호출되는 메서드
- 메모리에서 삭제됨

```python
class Person:
	def __del__(self):
		print('인스턴스가 사라졌습니다.')

person1 = Person()
del person1
```

---

## 클래스 메서드

- 클래스가 사용할 메서드
- @classmethod 데코레이터를 사용하여 정의
- 호출 시, 첫번째 인자로 클래스(cls)가 전달됨

```python
class MyClass:

	@classmethod
	def class_method(cls, arg1, ...):

MyClass.class_method(arg1, ...)
```

## 클래스 메서드 활용

```python
class Person:
	count = 0 # 클래스 변수
	def __init__(self, name): # 인스턴스 변수 설정
		self.name = name
		Person.count += 1

	@classmethod
	def number_of_population(cls):
		print(f'인구수는 {cls.count}입니다.')

person1 = Person('아이유')
person2 = Person('이찬혁')
print(Person.count) # 2
```
```python
class Person:
    # 생성자를 통한 인스턴스 생성
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # details 클래스 메서드를 통한 인스턴스 생성
    @classmethod
    def details(cls, name, year):
        return cls(name, 2022 - year) # name, 2022 - year를 __init__()의 name과 age에 넘겨줌

    # 19세 기준 미성년자 판별
    def check_age(self, age):
        return self.age < 19
```

## 데코레이터

- 함수를 어떤 함수로 꾸며서 새로운 기능을 부여
- @데코레이터(함수명) 형태로 함수 위에 작성
- 순서대로 적용되기 때문에 작성 순서가 중요
- 일종의 모자라고 이해하자

## 데코레이터 사용 예시

- 데코레이터 없이 함수 꾸미기

```python
def hello():
	print('hello')

# 데코레이팅 함수
def add_print(original): # 파라미터로 함수를 받는다
	def wrapper(): # 함수 내에서 새로운 함수 선언
		print('함수 시작') # 부가기능 -> original 함수를 꾸민다
		original()
		print('함수 끝') # 부가기능 -> original 함수를 꾸민다
	return wrapper

add_print(hello)()
'''
함수 시작
hello
함수 끝
'''
# wrapper가 return된 것임
# 즉, add_print(hello)까지가 wrapper
# 반환된 wrapper는 변수가 아닌 함수이므로 뒤에 ()를 통해 wrapper를 호출

print_hello = add_print(hello)
print_hello()
'''
함수 시작
hello
함수 끝
'''
```

- 데코레이터를 활용하면 쉽게 여러 함수를 원하는대로 변경할 수 있음

```python
# 데코레이팅 함수
def add_print(original): # 파라미터로 함수를 받는다
	def wrapper(): # 함수 내에서 새로운 함수 선언
		print('함수 시작') # 부가기능 -> original 함수를 꾸민다
		original()
		print('함수 끝') # 부가기능 -> original 함수를 꾸민다
	return wrapper

@add_print # 이 선언을 통해 print_hello()는 자동으로 original로 들어감
def print_hello():
	print('hello')

print_hello() # 사실은 wrapper()인 것임
'''
함수 시작
hello
함수 끝
'''
```

## 클래스 메서드와 인스턴스 메서드

- 클래스 메서드
    - 클래스 변수 사용
- 인스턴스 메서드
    - 인스턴스 변수 사용
- 그렇다면 인스턴스 변수, 클래스 변수 모두 사용하고 싶다면?
    - 클래스는 인스턴스 변수 사용이 불가능
    - 인스턴스 메서드는 클래스 변수, 인스턴스 변수 둘 다 사용이 가능

---

## 스태틱 메서드

- 스태틱 메서드
    - 인스턴스 변수, 클래스 변수를 전혀 다루지 않는 메서드
- 언제 사용하는가?
    - 속성을 다루지 않고 단지 기능(행동)만을 하는 메서드를 정의할 때, 사용
    - 속성을 다루지 않고 == 데이터의 변화 없이
- 인스턴스 변수, 클래스 변수 아무것도 사용하지 않을 경우 사용
    - 즉, 객체 상태나 클래스 상태를 수정할 수 없음
- @staticmethod 데코레이터를 사용하여 정의
- 일반 함수처럼 동작하지만, 클래스의 이름공간에 귀속됨
    - 주로 해당 클래스로 한정하는 용도로 사용

```python
class Myclass:

	@staticmethod
	def static_method(arg1, ...):

MyClass.static_method(arg1, ...)
```

## 스태틱 메서드 사용 예시

```python
class Person:
	count = 0 # 클래스 변수
	def __init__(self, name): # 인스턴스 변수 설정
		self.name = name
		Person.count += 1

	@staticmethod
	def check_rich(money): # 스태틱은 cls, self 사용 x
		return money > 10000

person1 = Person('아이유')
person2 = Person('이찬혁')
print(Person.check_rich(100000)) # True 스태틱은 클래스로 접근 가능
print(person1.check_rich(100000)) # True 스태틱은 인스턴스로 접근 가능
```

---

## 인스턴스와 클래스 간의 이름 공간(namespace)

- 클래스를 정의하면, 클래스와 해당하는 이름 공간 생성
- 인스턴스를 만들면, 인스턴스 객체가 생성되고 이름 공간 생성
- 인스턴스에서 특정 속성에 접근하면, 인스턴스 - 클래스 순으로 탐색

<img width="1090" alt="python_38" src="https://user-images.githubusercontent.com/86648892/181940397-bd17d7ba-66d7-4988-b6c8-e54cb2c66660.png">

```python
# Person 정의
class Person:
	name = 'unknown'

	def talk(self):
		print(self.name)

p1 = Person()
p1.talk() # unknown # p1은 인스턴스 변수가 정의되어 있지 않아 클래스 변수(unknown)가 출력됨

# p2 인스턴스 변수 설정 전 / 후
p2 = Person()
p2.talk() # unknown
p2.name = 'Kim'
p2.talk() # Kim # p2는 인스턴스 변수가 정의되어 인스턴스 변수(Kim)가 출력됨

print(Person.name) # unknown
print(p1.name) # unknown
print(p2.name) # Kim
# Person 클래스의 값이 Kim으로 변경된 것이 아닌 p2 인스턴스의 이름 공간에 name이 Kim으로 저장됨
```

<img width="1209" alt="python_39" src="https://user-images.githubusercontent.com/86648892/181940402-6fe70d2f-9f3c-408f-ae55-9732e38acf5e.png">

---

## 메서드 정리

- 인스턴스 메서드
    - 호출한 인스턴스를 의미하는 self 매개변수를 통해 인스턴스를 조작
- 클래스 메서드
    - 클래스를 의미하는 cls 매개변수를 통해 클래스를 조작
- 스태틱 메서드
    - 클래스 변수나 인스턴스 변수를 사용하지 않는 경우에 사용
        - 객체 상태나 클래스 상태를 수정할 수 없음

## 예시

```python
class MyClass:
	def method(self):
		return 'instance method', self

	@classmethod
	def classmethod(cls):
		return 'class method', cls

	@staticmethod
	def staticmethod():
		return 'static method'
```

- 인스턴스 메서드를 호출한 결과

```python
obj = MyClass()
print(obj.method()) # ('instance method', <__main__.MyClass at 0x185fd086a00>)
print(MyClass.method(obj)) # ('instance method', <__main__.MyClass at 0x185fd086a00>)
```

- 클래스 자체에서 각 메서드를 호출하는 경우
    - 인스턴스 메서드는 호출할 수 없음

```python
print(MyClass.classmethod()) # ('class method', <class '__main__.MyClass'>)
print(MyClass.staticmethod()) # static method
MyClass.method() # method() missing 1 required positional argument: 'self'
```

- 인스턴스는 클래스 메서드와 스태틱 메서드 모두 접근할 수 있음

```python
print(obj.classmethod()) # ('class method', <class '__main__.MyClass'>)
print(MyClass.classmethod()) # ('class method', <class '__main__.MyClass'>)
print(obj.staticmethod()) # static method
```

---

# 객체지향의 핵심개념

## 객체지향의 핵심개념 4가지

- 추상화
    - 복잡한 것을 숨기고, 필요한 것만 나타냄
- 상속
    - 부모 클래스와 자식 클래스의 관계에 대한 것으로, 부모 클래스에서 물려받고, 자식 클래스에서 재사용하는 것
- 다형성
    - 이름은 같은데 동작은 다른 것
        - 오버라이딩
            - 자식에서 변경되는 것
        - 오버로딩 (파이썬은 지원하지 않음)
- 캡슐화
    - 민감한 정보를 숨기는 것, 혹은 민감한 정보를 고치지 못하게 하는 것
        - getter, setter, _

---

## 추상화

- 현실 세계를 프로그램 설계에 반영
    - 복잡한 것은 숨기고, 필요한 것만 드러내기
    - User.login()이라는 기능으로 추상화
        - 어떻게 로그인이 되는지 그 복잡한 과정은 따로 구현해놓고 숨김

## 추상화 예시

```python
# 학생(Student)을 표현하기 위한 클래스를 생성합니다.

class Student:
	def __init__(self, name, age, gpa):
		self.name = name
		self.age = age
		self.gpa = gpa

	def talk(self):
		print(f'반갑습니다. {self.name}입니다.')

	def study(self):
		self.gpa += 0.1

# 교수(Professor)를 표현하기 위한 클래스를 생성합니다.

class Professor:
	def __init__(self, name, age, department):
		self.name = name
		self.age = age
		self.department = department

	def talk(self):
		print(f'반갑습니다. {self.name}입니다.')

	def teach(self):
		self.age += 1

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def talk(self):
		print(f'반갑습니다. {self.name}입니다.')
```

---

## 상속

- 상속이란
    - 두 클래스 사이에 부모 - 자식 관계를 정립하는 것
- 클래스는 상속이 가능함
    - 모든 파이썬 클래스는 object를 상속받음
        - 클래스를 타고 타고 올라가면 맨 위에 object가 있다

```python
class ChildClass(ParentClass):
	pass
```

- 하위 클래스는 상위 클래스에 정의된 속성, 행동, 관계 및 제약 조건을 모두 상속받음
- 부모 클래스의 속성, 메서드가 자식 클래스에 상속되므로, 코드 재사용성이 높아짐

### 상속없이 구현하는 경우 I

- 학생 / 교수 정보를 나타내기 어려움

<img width="199" alt="python_40" src="https://user-images.githubusercontent.com/86648892/181940407-6495f13e-f56b-471c-8ea8-909da02320d4.png">

```python
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def talk(self):
		print(f'반갑습니다. {self.name}입니다.')

s1 = Person('김학생', 23)
s1.talk() # 반갑습니다. 김학생입니다.

p1 = Person('박교수', 49)
p1.talk() # 반갑습니다. 박교수입니다.

s1.gpa = 4.5
p1.department = '컴퓨터공학과'
```

### 상속없이 구현하는 경우 II

- 메서드 중복 정의

<img width="364" alt="python_41" src="https://user-images.githubusercontent.com/86648892/181940412-bbf8996f-fc56-4c74-afb2-6785cd95ceb2.png">

```python
class Professor:
	def __init__(self, name, age, department):
		self.name = name
		self.age = age
		self.department = department

	def talk(self): # 중복
		print(f'반갑습니다. {self.name}입니다.')

class Student:
	def __init__(self, name, age, gpa):
		self.name = name
		self.age = age
		self.gpa = gpa

	def talk(self): # 중복
		print(f'반갑습니다. {self.name}입니다.')

p1 = Professor('박교수', 49, '컴퓨터공학과')
s1 = Student('김학생', 20, 3.5)
```

### 상속을 통한 메서드 재사용

<img width="253" alt="python_42" src="https://user-images.githubusercontent.com/86648892/181940417-2c55bac2-c251-4dcb-9381-722c55049012.png">

```python
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def talk(self): # 메서드 재사용
		print(f'반갑습니다. {self.name}입니다.')

class Professor(Person):
	def __init__(self, name, age, department):
		self.name = name
		self.age = age
		self.department = department

class Student(Person):
	def __init__(self, name, age, gpa):
		self.name = name
		self.age = age
		self.gpa = gpa

p1 = Professor('박교수', 49, '컴퓨터공학과')
s1 = Student('김학생', 20, 3.5)

# 부모 Person 클래스의 talk 메서드를 활용
p1.talk() # 반갑습니다. 박교수입니다.

# 부모 Person 클래스의 talk 메서드를 활용
s1.talk() # 반갑습니다. 김학생입니다.
```

## 상속 관련 함수와 메서드

- isinstance(object, classinfo)
    - classinfo의 instance이거나 subclass인 경우 True
    
    ```python
    class Person:
    	pass
    
    class Professor:
    	pass
    
    class Student:
    	pass
    
    # 인스턴스 생성
    p1 = Professor()
    s1 = Student()
    
    print(isinstance(p1, Person)) # False
    print(isinstance(p1, Professor)) # True
    print(isinstance(p1, Student)) # False
    print(isinstance(s1, Person)) # False
    print(isinstance(s1, Professor)) # False
    print(isinstance(s1, Student)) # True
    
    class Person:
    	pass
    
    class Professor(Person):
    	pass
    
    class Student(Person):
    	pass
    
    # 인스턴스 생성
    p1 = Professor()
    s1 = Student()
    
    print(isinstance(p1, Person)) # True
    print(isinstance(p1, Professor)) # True
    print(isinstance(p1, Student)) # False
    print(isinstance(s1, Person)) # True
    print(isinstance(s1, Professor)) # False
    print(isinstance(s1, Student)) # True
    ```
    
- issubclass(class, classinfo)
    - class가 classinfo의 subclass이면 True
    - classinfo는 클래스 객체의 튜플일 수 있으며, classinfo의 모든 항목을 검사
    
    ```python
    class Person:
    	pass
    
    class Professor(Person):
    	pass
    
    class Student(Person):
    	pass
    
    # 인스턴스 생성
    p1 = Professor()
    s1 = Student()
    
    print(issubclass(bool, int)) # True
    print(issubclass(float, int)) # False
    print(issubclass(Professor, Person)) # True
    print(issubclass(Professor, (Person, Student))) # True
    ```
    

```python
# __subclasses__()를 통해 해당 클래스의 subclass 확인 가능

print(object.__subclasses__())

# [<class 'type'>, <class 'async_generator'>, <class 'int'>, <class 'bytearray_iterator'>, <class 'bytearray'>, <class 'bytes_iterator'>, <class 'bytes'>, <class 'builtin_function_or_method'>, <class 'callable_iterator'>, <class 'PyCapsule'>, <class 'cell'>, <class 'classmethod_descriptor'>, <class 'classmethod'>, <class 'code'>, <class 'complex'>, <class 'coroutine'>, <class 'dict_items'>, <class 'dict_itemiterator'>, <class 'dict_keyiterator'>, <class 'dict_valueiterator'>, <class 'dict_keys'>, <class 'mappingproxy'>, <class 'dict_reverseitemiterator'>, <class 'dict_reversekeyiterator'>, <class 'dict_reversevalueiterator'>, <class 'dict_values'>, <class 'dict'>, <class 'ellipsis'>, <class 'enumerate'>, <class 'float'>, <class 'frame'>, <class 'frozenset'>, <class 'function'>, <class 'generator'>, <class 'getset_descriptor'>, <class 'instancemethod'>, <class 'list_iterator'>, <class 'list_reverseiterator'>, <class 'list'>, <class 'longrange_iterator'>, <class 'member_descriptor'>, <class 'memoryview'>, <class 'method_descriptor'>, <class 'method'>, <class 'moduledef'>, <class 'module'>, <class 'odict_iterator'>, <class 'pickle.PickleBuffer'>, <class 'property'>, <class 'range_iterator'>, <class 'range'>, <class 'reversed'>, <class 'symtable entry'>, <class 'iterator'>, <class 'set_iterator'>, <class 'set'>, <class 'slice'>, <class 'staticmethod'>, <class 'stderrprinter'>, <class 'super'>, <class 'traceback'>, <class 'tuple_iterator'>, <class 'tuple'>, <class 'str_iterator'>, <class 'str'>, <class 'wrapper_descriptor'>, <class 'types.GenericAlias'>, <class 'anext_awaitable'>, <class 'async_generator_asend'>, <class 'async_generator_athrow'>, <class 'async_generator_wrapped_value'>, <class 'coroutine_wrapper'>, <class 'InterpreterID'>, <class 'managedbuffer'>, <class 'method-wrapper'>, <class 'types.SimpleNamespace'>, <class 'NoneType'>, <class 'NotImplementedType'>, <class 'weakcallableproxy'>, <class 'weakproxy'>, <class 'weakref'>, <class 'types.UnionType'>, <class 'EncodingMap'>, <class 'fieldnameiterator'>, <class 'formatteriterator'>, <class 'BaseException'>, <class 'hamt'>, <class 'hamt_array_node'>, <class 'hamt_bitmap_node'>, <class 'hamt_collision_node'>, <class 'keys'>, <class 'values'>, <class 'items'>, <class '_contextvars.Context'>, <class '_contextvars.ContextVar'>, <class '_contextvars.Token'>, <class 'Token.MISSING'>, <class 'filter'>, <class 'map'>, <class 'zip'>, <class '_frozen_importlib._ModuleLock'>, <class '_frozen_importlib._DummyModuleLock'>, <class '_frozen_importlib._ModuleLockManager'>, <class '_frozen_importlib.ModuleSpec'>, <class '_frozen_importlib.BuiltinImporter'>, <class '_frozen_importlib.FrozenImporter'>, <class '_frozen_importlib._ImportLockContext'>, <class '_thread.lock'>, <class '_thread.RLock'>, <class '_thread._localdummy'>, <class '_thread._local'>, <class '_io._IOBase'>, <class '_io._BytesIOBuffer'>, <class '_io.IncrementalNewlineDecoder'>, <class 'posix.ScandirIterator'>, <class 'posix.DirEntry'>, <class '_frozen_importlib_external.WindowsRegistryFinder'>, <class '_frozen_importlib_external._LoaderBasics'>, <class '_frozen_importlib_external.FileLoader'>, <class '_frozen_importlib_external._NamespacePath'>, <class '_frozen_importlib_external._NamespaceLoader'>, <class '_frozen_importlib_external.PathFinder'>, <class '_frozen_importlib_external.FileFinder'>, <class 'codecs.Codec'>, <class 'codecs.IncrementalEncoder'>, <class 'codecs.IncrementalDecoder'>, <class 'codecs.StreamReaderWriter'>, <class 'codecs.StreamRecoder'>, <class '_abc._abc_data'>, <class 'abc.ABC'>, <class 'collections.abc.Hashable'>, <class 'collections.abc.Awaitable'>, <class 'collections.abc.AsyncIterable'>, <class 'collections.abc.Iterable'>, <class 'collections.abc.Sized'>, <class 'collections.abc.Container'>, <class 'collections.abc.Callable'>, <class 'os._wrap_close'>, <class '_sitebuiltins.Quitter'>, <class '_sitebuiltins._Printer'>, <class '_sitebuiltins._Helper'>]
```

- super()
    - 자식클래스에서 부모클래스를 사용하고 싶은 경우
    - 생성자에서 많이 사용함
    
    ```python
    # super() 사용하지 않은 경우
    
    class Person:
    	def __init__(self, name, age, number, email):
    		self.name = name
    		self.age = age
    		self.number = number
    		self.email = email
    
    class Student(Person):
    	def __init__(self, name, age, number, email, student_id):
    		self.name = name
    		self.age = age
    		self.number = number
    		self.email = email
    		self.student_id = student_id
    
    # super() 사용한 경우
    # super()라는 상위 클래스에 접근해서 initialize해줘!
    
    class Student(Person):
    	def __init__(self, name, age, number, email, student_id):
    		# Person 클래스
    		super().__init__(name, age, number, email)
    		self.student_id = student_id
    ```
    

## 상속 정리

- 파이썬의 모든 클래스는 object로부터 상속됨
- 부모 클래스의 모든 요소(속성, 메서드)가 상속됨
- super()를 통해 부모 클래스의 요소를 호출할 수 있음
- 메서드 오버라이딩을 통해 자식 클래스에서 재정의 가능함
- 상속관계에서의 이름 공간은 인스턴스 - 자식 클래스 - 부모 클래스 순으로 탐색

## 다중 상속

- 두 개 이상의 클래스를 상속받는 경우
- 상속받은 모든 클래스의 요소를 활용 가능함
- 중복된 속성이나 메서드가 있는 경우 상속 순서에 의해 결정됨
- 다중상속이 되지 않는 프로그래밍 언어도 있다

```python
class Person:
	def __init__(self, name):
		self.name = name

	def greeting(self):
		return f'안녕, {self.name}'

class Mom(Person):
	gene = 'XX'

	def swim(self):
		return '엄마가 수영'

class Dad(Person):
	gene = 'XY'

	def walk(self):
		return '아빠가 걷기'

class FirstChild(Dad, Mom): # 다중상속 # 순서는 Dad -> Mom
	def swim(self):
		return '첫째가 수영'

	def cry(self):
		return '첫째가 응애'

class SecondChild(Mom, Dad): # 다중상속 순서는 Mom -> Dad
	def walk(self):
		return '둘째가 걷기'

	def cry(self):
		return '둘째가 응애'

baby1 = FirstChild('아가')
baby2 = SecondChild('아가')

print(baby1.cry()) # 첫째가 응애
print(baby1.swim()) # 첫째가 수영 # overriding
print(baby1.walk()) # 아빠가 걷기 # 상속
print(baby1.gene) # XY # Dad가 우선 상속됨

print(baby2.cry()) # 둘째가 응애
print(baby2.walk()) # 둘째가 걷기 # overriding
print(baby2.swim)) # 엄마가 수영 # 상속
print(baby2.gene)) # XX # Mom이 우선 상속됨
```

## mro 메서드(Method Resolution Order)

- 상속의 순서가 헷갈릴 때는?
    - mro를 사용해보자!
- 해당 인스턴스의 클래스가 어떤 부모 클래스를 가지는지 확인하는 메서드
    - resolution은 탐색, order는 순서
    - 상속의 순서 계보를 보자는 것
- 기존의 인스턴스 → 클래스 순으로 namespace를 탐색하는 과정에서 상속 관계에 있으면 인스턴스 → 자식 클래스 → 부모 클래스로 확장

```python
print(FirstChild.mro())
# FirstChild.__mro__ 도 가능
# [<class '__main__.FirstChild'>, <class '__main__.Dad'>, <class '__main__.Mom'>, <class '__main__.Person'>, <class 'object'>]

print(SecondChild.mro())
# SecondChild.__mro__ 도 가능
# [<class '__main__.FirstChild'>, <class '__main__.Mom'>, <class '__main__.Dad'>, <class '__main__.Person'>, <class 'object'>]
```

---

## 다형성

- 다형성(Polymorphism)이란?
    - 여러 모양을 뜻하는 그리스어
    - 동일한 메서드가 클래스에 따라 다르게 행동할 수 있음을 의미
    - 즉, 서로 다른 클래스에 속해있는 객체들이 동일한 메시지에 대해 다른 방식으로 응답할 수 있음
        - 예를 들어 상속받은 메서드에 대해 자식 클래스_1과 자식 클래스_2가 다르게 작동할 수 있음
    - 상속 관계에 있는 것을 커스터마이징하는 것!
    - Overriding / Overloading
        - 파이썬에서는 오버로딩은 지원하지 않음

## 메서드 오버라이딩(Overriding)

- 상속받은 메서드를 재정의
    - 클래스 상속 시, 부모 클래스에서 정의한 메서드를 자식 클래스에서 변경
    - 부모 클래스의 메서드 이름과 기본 기능은 그대로 사용하지만, 특정 기능을 바꾸고 싶을 때 사용
    - 상속받은 클래스에서 같은 이름의 메서드로 덮어쓰는 것
    - 부모 클래스의 메서드를 실행시키고 싶은 경우 super()를 활용
    - __init__과 __str__의 메서드를 정의하는 것 역시 메서드 오버라이딩
    
    <img width="376" alt="python_43" src="https://user-images.githubusercontent.com/86648892/181940422-7f5b10ca-6e24-4567-b1b0-18f768f5f880.png">
    

```python
class Person:
	def __init__(self, name):
		self.name = name

	def talk(self):
		print(f'반갑습니다. {self.name}입니다.')

# 자식 클래스 Professor
class Professor(Person):
	def talk(self): # overriding
		print(f'{self.name}일세.')

# 자식 클래스 Student
class Student(Person):
	def talk(self): # overriding
		super().talk()
		print(f'저는 학생입니다.')

p1 = Professor('김교수')
p1.talk() # 김교수일세.

s1 = Student('이학생')
s1.talk()
# 반갑습니다. 이학생입니다.
# 저는 학생입니다.
```

## 오버로딩(Method Overloading)

- 오버로딩이란 한 클래스 내에 같은 이름의 메서드를 여러 개 정의하는 것
    - 메서드 이름은 같고
    - 매개변수의 개수 또는 타입이 달라야 함
    - 오버로딩된 메서드들은 매개변수에 의해서만 구별될 수 있으므로 리턴 타입은 오버로딩을 구현하는데 아무런 영향을 주지 못함
- 파이썬에는 오버로딩이 없다
    - 파이썬은 *args라는 개념, 가변인자가 있기에 오버로딩을 지원하지 않음

---

## 캡슐화

- 객체의 일부 구현 내용에 대해 외부로부터의 직접적인 액세스를 차단
    - ex) 주민등록번호
- 파이썬에서 암묵적으로 존재하지만, 언어적으로는 존재하지 않음
- 데이터의 캡슐화란 직접적으로 변수에 대한 접근을 막는 것
    - 보통 getter와 setter 메서드를 통해 구현

<img width="542" alt="python_44" src="https://user-images.githubusercontent.com/86648892/181940427-4f0ef3d1-3cee-466f-a500-9961e4b6740f.png">

## 접근제어자 종류

- Public Access Modifier
- Protected Access Modifier
- Private Access Modifier

## Public Member

- 언더바 없이 시작하는 메서드나 속성
- 어디서나 호출이 가능
- 하위 클래스 override도 허용
- 일반적으로 작성되는 메서드와 속성의 대다수를 차지

```python
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = 30

# Person 클래스의 인스턴스인 p1은 name, age 모두 접근 가능
p1 = Person('김싸피', 30)
print(p1.name) # 김싸피
print(p1.age) # 30
```

## Protected Member

- 언더바 1개로 시작하는 메서드나 속성
- 암묵적 규칙에 의해 부모 클래스 내부와 자식 클래스에서만 호출 가능
- 하위 클래스 override 허용
- 암묵적으로 ‘이건 직접 건드리지는 맙시다!’라고 하는 것

```python
class Person:
	def __init__(self, name, age):
		self.name = name
		self._age = age

	def get_age(self):
		return self._age

# 인스턴스를 만들고 get_age 메서드를 활용하여 호출할 수 있음
p1 = Person('김싸피', 30)
print(p1.get_age()) # 30

# _age에 직접 접근하여도 확인 가능
# 파이썬에서는 암묵적으로 활용될 뿐
print(p1._age) # 30
```

```python
# WHY?

'''
가령 age가 민감정보라고 해보자
그러면 p1._age = 30과 같이 직접적으로 설정하는 것이 아닌
set_age()와 같은 것을 통해 적어도 한 단계는 거치도록 하고 싶은 것
물론
	def set_age(self):
		p1._age = 30
		print('~~ 변경됨')
		나이에 따라 변경되는 또 다른 연계 정보들 처리
과 같이 구현 내용은 결국 같겠지만
이 절차를 통해서 바꾸면 위와 같이 나이를 바꿨을 때 다른 처리도 하도록 할 수 있고 그렇다
'''
```

## Private Member

- 언더바 2개로 시작하는 메서드나 속성
- 본 클래스 내부에서만 사용이 가능
- 하위클래스 상속 및 호출 불가능 (오류)
- 외부 호출 불가능 (오류)

```python
class Person:
	def __init__(self, name, age):
		self.name = name
		self.__age = age

	def get_age(self):
		return self.__age

# 인스턴스를 만들고 get_age 메서드를 활용하여 호출할 수 있음
p1 = Person('김싸피', 30)
print(p1.get_age()) # 30

# __age에 직접 접근 불가
print(p1.__age)
# AttributeError: 'Person' object has no attribute '__age'
```

## getter 메서드와 setter 메서드

- getter와 setter 메서드를 통해 보통 캡슐화를 완성함
- 변수에 접근할 수 있는 메서드를 별도로 생성
    - getter 메서드: 변수의 값을 읽는 메서드
        - @property 데코레이터 사용
    - setter 메서드: 변수의 값을 설정하는 성격의 메서드
        - @변수.setter 사용
    - 데코레이터를 사용하지 않을 경우 property() 내장 함수에 getter와 setter를 넣어주자
- 직접 조회, 변경하는 것을 막는 데이터(클래스 멤버)의 경우 getter, setter로 우회하여 조회, 변경하도록 하는 것
- 협업할 때 많이 사용함
    - 코드의 안전성 향상
- getter와 setter를 ‘.age’와 같이 간단하게 사용하는 법
    - 참고 [https://www.daleseo.com/python-property/](https://www.daleseo.com/python-property/)
    - property() 사용
        - age = property(get_age(), set_age())
    - 데코레이터 사용
        - @property, @age.setter

```python
class Person:
	def __init__(self, age):
		self._age = age

	@property # 이 친구는 getter야
	def age(self):
		return self._age

	@age.setter # 이 친구는 age의 setter야
	# 새로 부여하려는 나이가 19세 이하이면 ValueError를 발생시키고 None을 반환하고 종료
	# 그렇지 않다면 new_age로 변경해줌
	def age(self, new_age):
		if new_age <= 19:
				raise ValueError('Too Young For SSAFY')
				return
		self._age = new_age

# raise는 어떤 상황에서 원하는 종류의 에러를 발생시키도록 하는 것
# raise ErrorType('Message')

p1 = Person(20)
print(p1.age) # 20 # 실제론 _age이지만 값을 가져오는 것이기에 알아서 getter를 통해 _age를 가져옴

p1.age = 33 # setter 함수를 선언했고, 새로운 값을 부여한 것이기에 알아서 setter의 new_age로 인식하여 변경
print(p1.age) # 33

p1.age = 19
print(p1.age) # ValueError: Too Young For SSAFY

'''
이처럼 getter와 setter를 선언해놓음을 통해
간단하게 p1.age, p1.age = n과 같이 명령해도
getter와 setter를 통해
1) 데이터 및 이를 조회와 변경하는 로직을 숨기고
2) 잘못된 데이터가 할당되는 것을 막을 수 있다
'''
```

```python
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age < 0:
            raise ValueError("Invalid age")
        self._age = age

    age = property(get_age, set_age) # property() 사용

>>> person = Person("John", "Doe", 20)
>>> person.age
20
>>> person.age = -1
ValueError: Invalid age
>>> person.age = person.age + 1
>>> person.age
21

'''
이처럼 property()를 통해 getter와 setter를 설정해줄 수도 있음
'''
```

---

# 에러 / 예외 처리(Error / Exception Handling)

## 개요

- 디버깅
- 에러와 예외
- 예외 처리
- 예외 발생시키기

---

## 디버깅

### 버그란?

- 최초의 버그는 1945년 프로그래밍 언어의 일종인 코볼 발명자 그레이스 호퍼가 발견
- 역사상 최초의 컴퓨터 버그는 Mark II 라는 컴퓨터 회로에 벌레인 나방이 들어가 합선을 일으켜 비정상적으로 동작
- 이때부터 소프트웨어에서 발생하는 문제를 버그라고 부름

<img width="323" alt="python_45" src="https://user-images.githubusercontent.com/86648892/181940431-90ec3484-dff6-4116-9493-ebc66166d76c.png">

### 디버깅의 정의

- 잘못된 프로그램을 수정하는 것을 디버깅이라함
    - de(없앤다) + bugging(버그)
- 에러 메시지가 발생하는 경우
    - 해당하는 위치를 찾아 메시지를 해결
- 로직 에러가 발생하는 경우
    - 명시적인 에러 메시지없이 예상과 다른 결과가 나온 경우
        - 정상적으로 동작하였던 코드 이후 작성된 코드를 생각해봄
        - 전체 코드를 살펴봄
        - 휴식을 가져봄
        - 누군가에게 설명해봄
        - …

### 디버깅

- 오류가 많이 발생하는 곳은 어딜까요?
    - 제어가 되는 시점
    - 조건문, 반복문, 함수 등에서 의도하지 않은 동작이 종종 발생함
    - for i in iterable: print(i)와 같이 프린트를 먼저 찍어보면서 하는 것이 좋다

```python
'코드의 상태를 신중하게 출력해가면 심사숙조하는 것보다 효과적인 디버깅 도구는 없습니다.'
- 브라이언 커니핸, Unix for Beginners
```

- print 함수 활용
    - 특정 함수 결과, 반복 / 조건 결과 등 나눠서 생각, 코드를 bisection으로 나눠서 생각
- 개발 환경(text editor, IDE) 등에서 제공하는 기능 활용
    - breakpoint, 변수 조회 등
- python tutor 활용 (단순 파이썬 코드인 경우)
- 뇌컴파일, 눈디버깅

---

# 에러와 예외

## 문법 에러(Syntax Error)

- 문장이나 표현식이 올바르지 않은 것
- SyntaxError가 발생하면, 파이썬 프로그램은 실행이 되지 않음
- 파일이름, 줄번호, ^ 문자를 통해 파이썬이 코드를 읽어나갈 때(parser) 문제가 발생한 위치를 표현
    - 파이썬은 인터프리터 방식이기에 에러가 발생하는 라인에서 실행이 끝남
- 줄에서 에러가 감지된 가장 앞의 위치를 가리키는 캐럿(caret)기호(^)를 표시

```python
if else

'''
File "...", line 1
	if else
		 ^

SyntaxError: invalid syntax
'''
```

### Invalid syntax

- 문법 오류

```python
while # SyntaxError: invalid syntax
```

### assign to literal

- 잘못된 할당
- sum = 5
    - sum()은 함수인데 sum = 5라고 선언해버리면 sum()이 동작하지 않음

```python
5 = 3 # SyntaxError: cannot assign to literal
```

### EOL(End of Line)

- 보통 따옴표 안닫으면 이 에러가 발생함

```python
print('hello
# SyntaxError: EOL while scanning string literal
```

### EOF(End of File)

- 보통 괄호 안닫으면 해당 에러가 발생함

```python
print(
# SyntaxError: unexpected EOF while parsing
```

---

## 예외(Exception)

- 실행 도중 예상치 못한 상황을 맞이하면, 프로그램 실행을 멈춤
    - 문장이나 표현식이 문법적으로 올바르더라도 발생하는 에러
- 실행 중에 감지되는 에러들을 예외(Exception)라고 부름
- 예외는 여러 타입(type)으로 나타나고, 타입이 메시지의 일부로 출력됨
    - NameError, TypeError 등은 발생한 예외 타입의 종류(이름)
- 모든 내장 예외는 Exception Class를 상속받아 이뤄짐
- 사용자 정의 예외를 만들어 관리할 수 있음
    - 예외 발생시키기(Exception Raising)
        - raise <’에러’>(’메시지’)
        - ex) 로그인이 되지 않은 경우 등
        
```python
def avg(scores):
    if len(scores) == 0:
        raise Exception('학생이 없습니다')
    else:
        return sum(scores) / len(scores)
        
        print(avg([]))
        
'''
---------------------------------------------------------------------------
Exception                         Traceback (most recent call last)
Input In [12], in <cell line: 2>()
      1 # 다음 코드를 통해 올바른 결과가 나오는지 확인하세요.
----> 2 print(avg([]))
        
Input In [10], in avg(scores)
      1 def avg(scores):
      2     if len(scores) == 0:
----> 3         raise Exception('학생이 없습니다')
      4     else:
      5         return sum(scores) / len(scores)

Exception: 학생이 없습니다
'''
```
        

### ZeroDivisionError

- 0으로 나눌 수 없는데, 0으로 나누고자 하는 경우
- 보통 num1 / num2에서 num2에 0이 들어간 경우

```python
10 / 0 # ZeroDivisionError: division by zero
```

### NameError

- namespace 상에 이름이 없는 경우
- not defined인 경우

```python
print(name_error) # NameError: name 'name_error' is not defined
```

### TypeError

- 타입 불일치

```python
1 + '1' # TypeError: unsupported operand type(s) for +: 'int' and 'str'
round('3.5') # TypeError: type str doesn't define __round__ method
```

- argument 누락

```python
divmod() # TypeError: divmod expected 2 arguments, got 0

import random
random.sample()
# TypeError: sample() missing 2 required positional arguments: 'population' and 'k'
```

- argument 개수 초과

```python
divmod(1, 2, 3) # TypeError: divmod expected 2 arguments, got 3

import random
random.sample(range(3), 1, 2)
# TypeError: sample() takes 3 positional arguments but 4 were given
```

- argument type 불일치

```python
import random
random.sample(1, 2)
# TypeError: Population must be a sequence. For dicts or sets, use sorted(d).
```

### ValueError

- 타입은 올바르나 값이 적절하지 않거나 없는 경우

```python
int('3.5') # ValueError: invalid literal for int() with base 10: '3.5'
range(3).index(6) # ValueError: 6 is not in range
```

### IndexError

- 인덱스가 존재하지 않거나 범위를 벗어나는 경우

```python
empty_list = []
empty_list[2]
# IndexError: list index out of range
# 이런 경우를 피하기 위해 .find(x) 사용
```

### KeyError

- 해당 키가 존재하지 않는 경우

```python
song = {'IU': '좋은날'}
song['BTS'] # KeyError: 'BTS'
# 이런 경우를 피하기 위해 .get(key)를 사용
```

### ModuleNotFoundError

- 해당 Module이 존재하지 않는 경우
- 설치가 제대로 되지 않았거나, 가상환경에 문제가 있는 경우 등

```python
import ssafy # ModuleNotFoundError: No module named 'ssafy'
```

### ImportError

- Module은 있으나 존재하지 않는 클래스 / 함수를 가져오는 경우

```python
from random import sample
print(sample(range(3), 1)) # [1]

from random import samp
# ImportError: cannot import name 'samp' from 'random'(/usr/lib/python3.9/random.py)
```

### KeyboardInterrupt

- 임의로 프로그램을 종료하였을 때

```python
while True:
		continue

'''
Traceback (most recent call last):
	File '...', line 2, in <module>
		continue
KeyboardInterrupt
'''
# 위 코드는 무한루프 코드
# ctrl c 누르면 취소됨
```

### IndentationError

- Indentation이 적절하지 않은 경우

```python
for i in range(3):
print(i) # IndentationError: expected an indented block

for i in range(3):
		print(i)
				print(i_ # IndentationError: unexpected indent
```

## 파이썬 내장 예외(Built-in Exceptions)

- 파이썬 내장 예외의 클래스 계층 구조
    - [예외 계층 구조](https://docs.python.org/ko/3/library/exceptions.html#exception-hierarchy)
    - 에러도 클래스 계층으로 이루어져 있어 상속이 적용됨

<img width="866" alt="python_46" src="https://user-images.githubusercontent.com/86648892/181940436-402281e4-d848-4a1e-968e-68feefa78500.png">

---

## 예외처리

- try문(statement) / except 절(clause)을 이용하여 예외 처리를 할 수 있음
- try문
    - 돌려볼 코드
    - 오류가 발생할 가능성이 있는 코드를 실행
    - 예외가 발생되지 않으면, except없이 실행 종료
- except문
    - 문제가 발생할 때 취할 처리
    - 예외가 발생하면, except 절이 실행
    - 예외 상황을 처리하는 코드를 받아서 적절한 조치를 취함

<img width="955" alt="python_47" src="https://user-images.githubusercontent.com/86648892/181940442-f279c409-ec4e-4f79-9dfc-54781c9c1459.png">

```python
'''
try:
	try 명령문
except 예외그룹 1 as 변수 1:
	예외처리 명령문 1
except 예외그룹 2 as 변수 2:
	예외처리 명령문 2
finally:
	finally 명령문
'''

try:
	num = input('숫자입력: ')
	print(int(num))
except ValueError:
	print('숫자가 입력되지 않았습니다.')

'''
숫자입력: 3
3
'''
'''
숫자입력: 안녕
숫자가 아닙니다
'''
```

## 에러 메시지 처리(as)

- as 키워드를 활용하여 원본 에러 메시지를 사용할 수 있음
    - 예외를 다른 이름에 대입

```python
try:
	empty_list = []
	print(empty_list[-1])
except IndexError as err:
	print(f'{err}, 오류가 발생했습니다.')

'''
list index out of range, 오류가 발생했습니다.
'''
```

## 복수의 예외 처리

- 순차적으로 수행됨으로 가장 작은 범주부터 예외 처리를 해야함
- 100을 사용자가 입력한 값으로 나누고 출력하는 코드를 작성해보시오
    - 먼저 발생가능한 에러가 무엇인지 예상
    
    ```python
    num = input('100으로 나눌 값을 입력하시오: ')
    print(100 / int(num))
    
    # 100 / int('a') 문자열을 int로 형변환: TypeError
    # 100 / int('0') 0으로 숫자를 나눔: ZeroDivisionError
    ```
    
- 100을 사용자가 입력한 정수로 나누고 출력하는 코드를 작성해보시오

```python
try:
	num = input('100으로 나눌 값을 입력하시오: ')
	print(100 / int(num))
except (ValueError, ZeroDivisionError):
	print('제대로 입력해줘.')

# 발생가능한 에러를 모두 명시
```

- 100을 사용자가 입력한 정수로 나누고 출력하는 코드를 작성해보시오

```python
try:
	num = input('100으로 나눌 값을 입력하시오: ')
	print(100 / int(num))
except ValueError:
	print('숫자를 넣어주세요.')
except ZeroDivisionError:
	print('0으로 나눌 수 없습니다.')
except:
	print('에러는 모르지만 에러가 발생하였습니다.')

# 에러 별로 별도의 에러처리
# 순차적으로 처리하여 해당하는 것이 있으면 그 아래는 수행하지 않음
```

## 예외 처리 종합

- try
    - 실행해볼 코드
- except
    - try문에서 실행한 코드에서 예외가 발생 시 실행할 내용
    - 작은 범주부터 나열
- else
    - try문에서 실행한 코드에서 예외가 발생하지 않으면 실행할 내용
    - 모든 except절 뒤에 와야함
    - try절이 예외를 일으키지 않을 때 실행되어야만 하는 처리에 적합
- finally
    - 예외 발생 여부와 관계없이 try문을 떠날 때 항상 실행함
    - 반드시 수행해야 하는 문장에 적합

## 예외 처리 종합 예시

- 파일을 열고 읽는 코드를 작성하는 경우
    - 파일 열기 시도 (try)
        - 파일 없는 경우 → ‘해당 파일이 없습니다.’ 출력 (except)
        - 파일 있는 경우 → 파일 내용을 출력 (else)
    - 해당 파일 읽기 작업 종료 메시지 출력 (finally)

```python
try:
	f = open('nooofile.txt')
except FileNotFoundError:
	print('해당 파일이 없습니다.')
else:
	print('파일을 읽기 시작합니다.')
	print(f.read())
	print('파일을 모두 읽었습니다.')
	f.close()
finally:
	print('파일 읽기를 종료합니다.')

# 파일이 없는 경우
'''
해당 파일이 없습니다.
파일 읽기를 종료합니다.
'''

# 파일이 있는 경우
'''
파일을 읽기 시작합니다.
파일내용
파일을 모두 읽었습니다.
파일 읽기를 종료합니다.
'''
```

## try except? if?

- 어떤 것을 쓰는 것이 더 좋을까?
    - case by case
- 어떤 것을 쓰는 것이 더 빠를까?
    - 보통 if문을 사용하는 것을 권장한다
    - try로 모든 경우를 나열하는 것보다 깔끔하게 if 조건을 만드는 것이 조금 더 빠르다
    - try는 도저히 모르겠는데 일단 프로그램을 돌리고 싶으면 try-finally를 통해 어찌되었든 진행할 수 있다는 점은 있다

---

# 추가 정리

- 클래스 이름은 pascal case로 짓는다
    - snake_case: 언더바(_)로 단어 구분
        - my_class_list
    - camelCase: 소문자로 시작 및 대문자로 단어 구분
        - myClassList
    - PascalCase: 대문자로 시작 및 대문자로 단어 구분
        - MyClassList
- docstring을 통해 클래스에 대한 설명 덧붙일 수 있음
    
    ```python
    class Person:
        """
        이것은 Person 클래스(class)입니다.
        """
    
    print(Person.__doc__) # 이것은 Person 클래스(class)입니다.
    ```
    
- print(type(person1)) # <class ‘__main__ Person’> # __main__임
    - 해당 클래스가 어디있는지 알려주는 것
    - 지금 네가 실행하고 있는 스크립트 안에 있는 Person이라는 클래스야라는 뜻
    - 다른 스크립트에 있는 클래스를 가져온다면 __main__이 아닌 다른 것이 찍힐 것
- __init__은 클래스의 인스턴스를 생성할 때 자동으로 불림
    - 정의하지 않았다면 기본적으로 내장되어 있는 아무것도 없는 __init__이 불림
- __del__은 인스턴스가 메모리에서 사라질 때 호출됨
    - 파이썬은 언어 내부적으로 알아서 메모리를 늘어났다 줄었다가 관리해줌
- 데코레이터는 함수를 꾸며주는 기능을 하는 함수
- static method는 클래스 내 속성을 사용하지 않지만 구조적으로 특정 클래스 안에만 종속시키고 싶을 때 사용
- DRY
    - Don’t Repeat Yourself!
- 디버깅을 위해 print()를 많이 사용하자
- assert문을 디버깅에 사용하기도 한다
    - 예외를 발생시키는 방법 중 하나
    - assert 'Boolean Expression', 'error message'
        - 조건이 True가 아니면 AssertionError 발생시킴
        - 상태를 검증하는데 사용
```python
assert len([1, 2]) == 1, '길이가 1이 아닙니다.'

'''
$ python code.py
Traceback (most recent call last):
    File "code.py", line 1, in <module>
        assert len([1, 2]) == 1, '길이가 1이 아닙니다.'
AssertionError: 길이가 1이 아닙니다.
'''

lists = [1, 3, 6, 3, 8, 7, 13, 23, 13, 2, 3.14, 2, 3, 7]
def test(number):
    assert type(number) is int, '정수 아닌 값이 있네'

for i in lists:
    test(i)

'''
AssertionError: 정수 아닌 값이 있네
'''
```
---