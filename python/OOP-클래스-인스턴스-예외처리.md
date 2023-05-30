## Index

---

- OOP
- class / instance
- abstraction / inheritance / polymorphism / encapsulation
- error / exception handling

## OOP (객체지향 프로그래밍)

---

- 객체지향 프로그래밍(Object-Oriented Programming, OOP)은 컴퓨터 프로그래밍의 패러다임 중 하나이다
- 객체지향 프로그래밍은 컴퓨터 프로그램을 명령어의 목록으로 보는 시각에서 벗어나
- 여러 개의 독립된 단위, 즉 '객체'들의 모임으로 파악하고자 하는 것이다
    - 객체란 2가지, ‘정보와 행동'을 가지고 있는 것
    - 정보는 곧 변수
    - 행동은 곧 함수
- 각각의 객체는 메시지를 주고받고, 데이터를 처리할 수 있다
- 프로그램을 여러 개의 독립된 객체들과, 그 객체 간의 상호작용으로 파악하는 프로그래밍 방법
- 예시
    - 콘서트
        - 가수 객체
        - 감독 객체
        - 관객 객체

### 절차지향 프로그래밍

<img width="652" alt="python_34" src="https://user-images.githubusercontent.com/86648892/181940365-5b7f80a0-decd-4cee-8854-a8961dbd2817.png">

- 과거에는 위처럼 Global Data라는 하나의 꾸러미에서 절차들을 계속 입력하는 형태로 프로그래밍을 했음
- 데이터와 함수로 인한 변화

### 객체지향 프로그래밍

<img width="619" alt="python_35" src="https://user-images.githubusercontent.com/86648892/181940382-c6041019-4bad-448c-878e-2c47c760e932.png">

- 데이터와 기능(메서드)을 분리해줌
- 추상화된 구조를 만듬(인터페이스)

### 객체지향 프로그래밍이 필요한 이유

#### 추상화

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

### 객체지향의 장점

- 클래스 단위로 모듈화시켜 개발할 수 있으므로 많은 인원이 참여하는 대규모 소프트웨어 개발에 적합
    - 예를 들어 저는 ‘로그인 기능' 그쪽은 ‘게시판 기능'을 담당합시다
- 필요한 부분만 수정하기 쉽기 때문에 프로그램의 유지보수가 쉬움

### 객체지향의 단점

- 설계 시 많은 노력과 시간이 필요함
    - 다양한 객체들의 상호 작용 구조를 만들기 위해 많은 시간과 노력이 필요
- 실행 속도가 상대적으로 느림
    - 절차지향 프로그래밍이 컴퓨터의 처리구조와 비슷해서 실행 속도가 빠름

## OOP 기초

---

### 객체

- 컴퓨터 과학에서 객체 또는 오브젝트(object)는 클래스에서 정의한 것을 토대로 메모리(실제 저장공간)에 할당된 것으로 프로그램에서 사용되는 데이터 또는 식별자에 의해 참조되는 공간을 의미하며, 변수, 자료구조, 함수 또는 메서드가 될 수 있다
- 쉽게 말해 속성과 행동으로 구성된 모든 것

### 클래스와 객체

- 클래스는 일종의 설계도, 객체는 실제 사례
- 클래스로 만든 객체를 인스턴스라고도 함
- 클래스 가수 객체 이찬혁
    - 이찬혁은 객체이다 (o)
    - 이찬혁은 인스턴스이다 (x)
    - 이찬혁은 가수의 인스턴스이다 (o)
- 클래스를 만든다 == 타입을 만든다

### 파이썬과 객체

- 파이썬은 모든 것이 객체(object)인, 객체 지향 프로그래밍 언어이다
- 모든 객체는 특정 타입의 인스턴스
- 파이썬의 모든 것엔 속성과 행동이 존재
    - `[3, 2, 1].sort()`
        - 리스트.정렬()
        - 객체.행동()
    - `‘banana’.upper()`
        - 문자열.대문자로()
        - 객체.행동()
- 객체(object)는 특정 타입의 인스턴스(instance)이다
- 객체(object)의 특징
    - 타입(type): 어떤 연산자(operator)와 조작(method)이 가능한가?
    - 속성(attribute): 어떤 상태(데이터)를 가지는가?
    - 조작법(method): 어떤 행위(함수)를 할 수 있는가?

<img width="648" alt="python_36" src="https://user-images.githubusercontent.com/86648892/181940387-40ab361b-821b-4b28-9383-74db40812ed3.png">

## 객체와 클래스 문법

---

### 기본 문법

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

### 객체 비교하기

- `==`
    - 동등한(equal)
    - 변수가 참조하는 객체가 동등한(내용이 같은) 경우 True
        - 주소가 다르더라도 그 안의 내용물이 같으면 됨
    - 두 객체가 같아 보이지만 실제로 동일한 대상을 가리키고 있다고 확인해준 것은 아님
    - 쌍둥이같은 느낌
- `is`
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

## OOP 속성

---

### 속성

- 데이터, 정보, 상태, 즉 변수
- 특정 데이터 타입 / 클래스의 객체들이 가지게 될 상태, 데이터를 의미
- 클래스 변수, 인스턴스 변수가 존재

```python
class Person:
	blood_color = 'red' # 클래스 변수
	population = 100 # 클래스 변수

	def __init__(self, name):
		self.name = name # 인스턴스 변수

person1 = Person('지민')
print(person1.name) # 지민
```

### 인스턴스 변수

- 인스턴스 변수란?
    - 인스턴스가 개인적으로 가지고 있는 속성(attribute)
    - 각 인스턴스들의 고유한 변수
- 생성자 메서드(`__init__`)에서 `self.<name>`으로 정의
- 인스턴스가 생성된 이후 `<instance>.<name>`으로 접근 및 할당

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

### 클래스 변수

- 한 클래스의 모든 인스턴스가 공유하는 값을 의미
- 같은 클래스의 인스턴스들은 같은 값을 갖게 됨
    - ex) 특정 사이트의 User 수 등은 클래스 변수 사용
- 클래스 선언 내부에서 정의
- `<classname>.<name>`으로 접근 및 할당
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


### 클래스 변수 활용(사용자 수 계산하기)

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

### 클래스 변수와 인스턴스 변수

- 클래스 변수를 변경할 때는 항상 `클래스.클래스변수` 형식으로 변경

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

## OOP 메서드

---

### 메서드

- 특정 데이터 타입, 클래스의 객체에 공통적으로 적용가능한 행위 (함수)

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

### 메서드의 종류

- **인스턴스 메서드**
    - 인스턴스를 처리
    - 대개 인스턴스의 변수를 처리함
    - `self`가 있으면 인스턴스 메서드라고 생각
- **클래스 메서드**
    - 클래스를 처리
    - 클래스 변수 등을 처리
- **정적 메서드**
    - 나머지

<img width="528" alt="python_37" src="https://user-images.githubusercontent.com/86648892/181940392-1f158ab2-22e3-4db2-86bf-cc7fd74f9248.png">

### 인스턴스 메서드

- 인스턴스 변수를 사용하거나, 인스턴스 변수에 값을 설정하는 메서드
- 클래스 내부에 정의되는 메서드의 기본
- 호출 시, 첫번째 인자로 인스턴스 자기자신(`self`)이 자동으로 전달됨

```python
class MyClass:
	def instance_method(self, arg1, ...):

my_instance = MyClass()
my_instance.instance_method(arg1, ...)
```

### self

- 인스턴스 자기자신
- 파이썬에서 인스턴스 메서드는 호출 시 첫번째 인자로 인스턴스 자신이 전달되게 설계
- 매개변수 이름으로 `self`를 첫번째 인자로 정의
- 다른 단어로도 작동하지만, 파이썬의 암묵적인 규칙

### 생성자(constructor) 메서드

- 인스턴스 객체가 생성될 때 자동으로 호출되는 메서드
- 인스턴스 변수들의 초기값을 설정
- 인스턴스 생성: `__init__`메서드 자동 호출
    
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
    

### 매직 메서드

- Double Underscore(`__`)가 있는 메서드는 특수한 동작을 위해 만들어진 메서드로, 스페셜 메서드 혹은 매직 메서드라고 불림
- 특정 상황에 자동으로 불리는 메서드
- 매직 메서드도 인스턴스 메서드이다
    - `self`에 적용

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
- `__str__`: 해당 객체의 출력 형태를 지정
    - 프린트 함수를 호출할 때, 자동으로 호출
    - 어떤 인스턴스를 출력하면 `__str__`의 return 값
- `__gt__`: 부등호 연산자(>, greater than)
    - ex) 이찬혁 > 교수
        - 돈? 키? 매력?
            - `__gt__`를 바꿔주면 됨

### 매직 메서드 예시

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

### 소멸자(destructor) 메서드

- 인스턴스 객체가 소멸(파괴)되기 직전에 호출되는 메서드
- 메모리에서 삭제됨

```python
class Person:
	def __del__(self):
		print('인스턴스가 사라졌습니다.')

person1 = Person()
del person1
```

### 클래스 메서드

- 클래스가 사용할 메서드
- `@classmethod` 데코레이터를 사용하여 정의
- 호출 시, 첫번째 인자로 클래스(`cls`)가 전달됨

```python
class MyClass:

	@classmethod
	def class_method(cls, arg1, ...):

MyClass.class_method(arg1, ...)
```

### 클래스 메서드 활용

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

### 데코레이터

- 함수를 어떤 함수로 꾸며서 새로운 기능을 부여
- `@데코레이터(함수명)` 형태로 함수 위에 작성
- 순서대로 적용되기 때문에 작성 순서가 중요
- 일종의 모자라고 이해하자

### 데코레이터 사용 예시

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

### 클래스 메서드와 인스턴스 메서드

- 클래스 메서드
    - 클래스 변수 사용
- 인스턴스 메서드
    - 인스턴스 변수 사용
- 그렇다면 인스턴스 변수, 클래스 변수 모두 사용하고 싶다면?
    - 클래스는 인스턴스 변수 사용이 불가능
    - 인스턴스 메서드는 클래스 변수, 인스턴스 변수 둘 다 사용이 가능

### 스태틱 메서드

- 스태틱 메서드
    - 인스턴스 변수, 클래스 변수를 전혀 다루지 않는 메서드
- 언제 사용하는가?
    - 속성을 다루지 않고 단지 기능(행동)만을 하는 메서드를 정의할 때, 사용
    - **속성을 다루지 않고 == 데이터의 변화 없이**
- 인스턴스 변수, 클래스 변수 아무것도 사용하지 않을 경우 사용
    - 즉, 객체 상태나 클래스 상태를 수정할 수 없음
- `@staticmethod` 데코레이터를 사용하여 정의
- 일반 함수처럼 동작하지만, 클래스의 이름공간에 귀속됨
    - 주로 해당 클래스로 한정하는 용도로 사용

```python
class Myclass:

	@staticmethod
	def static_method(arg1, ...):

MyClass.static_method(arg1, ...)
```

### 스태틱 메서드 사용 예시

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

### 인스턴스와 클래스 간의 이름 공간(namespace)

- 클래스를 정의하면, 클래스와 해당하는 이름 공간 생성
- 인스턴스를 만들면, 인스턴스 객체가 생성되고 이름 공간 생성
- 인스턴스에서 특정 속성에 접근하면, 인스턴스 -> 클래스 순으로 탐색

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

## 메서드 정리

---

- 인스턴스 메서드
    - 호출한 인스턴스를 의미하는 `self` 매개변수를 통해 인스턴스를 조작
- 클래스 메서드
    - 클래스를 의미하는 `cls` 매개변수를 통해 클래스를 조작
- 스태틱 메서드
    - 클래스 변수나 인스턴스 변수를 사용하지 않는 경우에 사용
    - 객체 상태나 클래스 상태를 수정할 수 없음

### 예시

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

## 객체지향의 핵심개념

---

1. **추상화**: 복잡한 것을 숨기고, 필요한 것만 나타냄
2. **상속**: 부모 클래스와 자식 클래스의 관계에 대한 것으로, 부모 클래스에서 물려받고, 자식 클래스에서 재사용하는 것
3. **다형성**: 이름은 같은데 동작은 다른 것
    - 오버라이딩: 자식에서 변경되는 것
    - 오버로딩 (파이썬은 지원하지 않음)
4. **캡슐화**: 민감한 정보를 숨기는 것, 혹은 민감한 정보를 고치지 못하게 하는 것
    - `getter`, `setter`, `_`

### 1. 추상화

- 현실 세계를 프로그램 설계에 반영
- 복잡한 것은 숨기고, 필요한 것만 드러내기
- `User.login()`이라는 기능으로 추상화: 어떻게 로그인이 되는지 그 복잡한 과정은 따로 구현해놓고 숨김

### 추상화 예시

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

### 2. 상속

- 상속이란 두 클래스 사이에 부모 - 자식 관계를 정립하는 것
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

### 상속 관련 함수와 메서드

1. `isinstance(object, classinfo)`

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

2. `issubclass(class, classinfo)`

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

3. `super()`

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

### 상속 정리

- 파이썬의 모든 클래스는 object로부터 상속됨
- 부모 클래스의 모든 요소(속성, 메서드)가 상속됨
- `super()`를 통해 부모 클래스의 요소를 호출할 수 있음
- 메서드 오버라이딩을 통해 자식 클래스에서 재정의 가능함
- 상속관계에서의 이름 공간은 인스턴스 -> 자식 클래스 -> 부모 클래스 순으로 탐색

### 다중 상속

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

### mro 메서드(Method Resolution Order)

- 상속의 순서가 헷갈릴 때는?
    - mro를 사용해보자!
- 해당 인스턴스의 클래스가 어떤 부모 클래스를 가지는지 확인하는 메서드
    - resolution은 탐색, order는 순서
    - 상속의 순서 계보를 보자는 것
- 기존의 인스턴스 → 클래스 순으로 namespace를 탐색하는 과정에서 상속 관계에 있으면 인스턴스 -> 자식 클래스 -> 부모 클래스로 확장

```python
print(FirstChild.mro())
# FirstChild.__mro__ 도 가능
# [<class '__main__.FirstChild'>, <class '__main__.Dad'>, <class '__main__.Mom'>, <class '__main__.Person'>, <class 'object'>]

print(SecondChild.mro())
# SecondChild.__mro__ 도 가능
# [<class '__main__.FirstChild'>, <class '__main__.Mom'>, <class '__main__.Dad'>, <class '__main__.Person'>, <class 'object'>]
```

### 3. 다형성

- 다형성(Polymorphism)이란?
    - 여러 모양을 뜻하는 그리스어
    - 동일한 메서드가 클래스에 따라 다르게 행동할 수 있음을 의미
    - 즉, 서로 다른 클래스에 속해있는 객체들이 동일한 메시지에 대해 다른 방식으로 응답할 수 있음
        - 예를 들어 상속받은 메서드에 대해 자식 클래스_1과 자식 클래스_2가 다르게 작동할 수 있음
    - 상속 관계에 있는 것을 커스터마이징하는 것!
    - Overriding / Overloading
        - 파이썬에서는 오버로딩은 지원하지 않음

### 메서드 오버라이딩(Overriding)

- 상속받은 메서드를 재정의
    - 클래스 상속 시, 부모 클래스에서 정의한 메서드를 자식 클래스에서 변경
    - 부모 클래스의 메서드 이름과 기본 기능은 그대로 사용하지만, 특정 기능을 바꾸고 싶을 때 사용
    - 상속받은 클래스에서 같은 이름의 메서드로 덮어쓰는 것
    - 부모 클래스의 메서드를 실행시키고 싶은 경우 `super()`를 활용
    - `__init__`과 `__str__`의 메서드를 정의하는 것 역시 메서드 오버라이딩
    
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

### 오버로딩(Method Overloading)

- 오버로딩이란 한 클래스 내에 같은 이름의 메서드를 여러 개 정의하는 것
    - 메서드 이름은 같고
    - 매개변수의 개수 또는 타입이 달라야 함
    - 오버로딩된 메서드들은 매개변수에 의해서만 구별될 수 있으므로 리턴 타입은 오버로딩을 구현하는데 아무런 영향을 주지 못함
- 파이썬에는 오버로딩이 없다
    - 파이썬은 `*args`라는 개념, 가변인자가 있기에 오버로딩을 지원하지 않음

### 4. 캡슐화

- 객체의 일부 구현 내용에 대해 외부로부터의 직접적인 액세스를 차단
    - ex) 주민등록번호
- 파이썬에서 암묵적으로 존재하지만, 언어적으로는 존재하지 않음
- 데이터의 캡슐화란 직접적으로 변수에 대한 접근을 막는 것
    - 보통 `getter`와 `setter` 메서드를 통해 구현

<img width="542" alt="python_44" src="https://user-images.githubusercontent.com/86648892/181940427-4f0ef3d1-3cee-466f-a500-9961e4b6740f.png">

### 접근제어자 종류

- Public Access Modifier
- Protected Access Modifier
- Private Access Modifier

### Public Member

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

### Protected Member

- `_` (언더바 1개)로 시작하는 메서드나 속성
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

### Private Member

- `__` (언더바 2개)로 시작하는 메서드나 속성
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

### getter 메서드와 setter 메서드

- `getter`와 `setter` 메서드를 통해 보통 캡슐화를 완성함
- 변수에 접근할 수 있는 메서드를 별도로 생성
    - getter 메서드: 변수의 값을 읽는 메서드
        - `@property` 데코레이터 사용
    - setter 메서드: 변수의 값을 설정하는 성격의 메서드
        - `@변수.setter` 사용
    - 데코레이터를 사용하지 않을 경우 `property()` 내장 함수에 `getter`와 `setter`를 넣어주자
- 직접 조회, 변경하는 것을 막는 데이터(클래스 멤버)의 경우 getter, setter로 우회하여 조회, 변경하도록 하는 것
- 협업할 때 많이 사용함
    - 코드의 안전성 향상
- getter와 setter를 `.age`와 같이 간단하게 사용하는 법
    - 참고 [https://www.daleseo.com/python-property/](https://www.daleseo.com/python-property/)
    - property() 사용
        - `age = property(get_age(), set_age())`
    - 데코레이터 사용
        - `@property, @age.setter`

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

## 에러 / 예외 처리(Error / Exception Handling)

---

- 디버깅
- 에러와 예외
- 예외 처리
- 예외 발생시키기

## 디버깅

---

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

### 디버깅

- 오류가 많이 발생하는 곳은 어딜까요?
    - 제어가 되는 시점
    - 조건문, 반복문, 함수 등에서 의도하지 않은 동작이 종종 발생함
    - for i in iterable: print(i)와 같이 프린트를 먼저 찍어보면서 하는 것이 좋다

> '코드의 상태를 신중하게 출력해가면 심사숙고하는 것보다 효과적인 디버깅 도구는 없습니다.'

> 브라이언 커니핸, Unix for Beginners

- print 함수 활용
    - 특정 함수 결과, 반복 / 조건 결과 등 나눠서 생각, 코드를 bisection으로 나눠서 생각
- 개발 환경(text editor, IDE) 등에서 제공하는 기능 활용
    - breakpoint, 변수 조회 등
- python tutor 활용 (단순 파이썬 코드인 경우)
- 뇌컴파일, 눈디버깅

## 에러와 예외

---

### 문법 에러(Syntax Error)

- 문장이나 표현식이 올바르지 않은 것
- SyntaxError가 발생하면, 파이썬 프로그램은 실행이 되지 않음
- 파일이름, 줄번호, `^` 문자를 통해 파이썬이 코드를 읽어나갈 때(parser) 문제가 발생한 위치를 표현
    - 파이썬은 인터프리터 방식이기에 에러가 발생하는 라인에서 실행이 끝남
- 줄에서 에러가 감지된 가장 앞의 위치를 가리키는 캐럿(caret)기호(`^`)를 표시

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

## 예외(Exception)

---

- 실행 도중 예상치 못한 상황을 맞이하면, 프로그램 실행을 멈춤
    - 문장이나 표현식이 문법적으로 올바르더라도 발생하는 에러
- 실행 중에 감지되는 에러들을 예외(Exception)라고 부름
- 예외는 여러 타입(type)으로 나타나고, 타입이 메시지의 일부로 출력됨
    - NameError, TypeError 등은 발생한 예외 타입의 종류(이름)
- 모든 내장 예외는 Exception Class를 상속받아 이뤄짐
- 사용자 정의 예외를 만들어 관리할 수 있음
    - 예외 발생시키기(Exception Raising)
        - `raise <’에러’>(’메시지’)`
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

## 예외처리

---

- `try / except`을 이용하여 예외 처리를 할 수 있음
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

### 에러 메시지 처리(as)

- `as` 키워드를 활용하여 원본 에러 메시지를 사용할 수 있음
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

### 복수의 예외 처리

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

### 예외 처리 종합

- `try`
    - 실행해볼 코드
- `except`
    - try문에서 실행한 코드에서 예외가 발생 시 실행할 내용
    - 작은 범주부터 나열
- `else`
    - try문에서 실행한 코드에서 예외가 발생하지 않으면 실행할 내용
    - 모든 except절 뒤에 와야함
    - try절이 예외를 일으키지 않을 때 실행되어야만 하는 처리에 적합
- `finally`
    - 예외 발생 여부와 관계없이 try문을 떠날 때 항상 실행함
    - 반드시 수행해야 하는 문장에 적합

### 예외 처리 종합 예시

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

### try except? if?

- 어떤 것을 쓰는 것이 더 좋을까?
    - case by case
- 어떤 것을 쓰는 것이 더 빠를까?
    - 보통 if문을 사용하는 것을 권장한다
    - try로 모든 경우를 나열하는 것보다 깔끔하게 if 조건을 만드는 것이 조금 더 빠르다
    - try는 도저히 모르겠는데 일단 프로그램을 돌리고 싶으면 `try-finally`를 통해 어찌되었든 진행할 수 있다는 점은 있다

## 추가 정리

---

- 클래스 이름은 PascalCase로 짓는다
    - `snake_case`: 언더바(_)로 단어 구분
        - my_class_list
    - `camelCase`: 소문자로 시작 및 대문자로 단어 구분
        - myClassList
    - `PascalCase`: 대문자로 시작 및 대문자로 단어 구분
        - MyClassList
- docstring을 통해 클래스에 대한 설명 덧붙일 수 있음
    
    ```python
    class Person:
        """
        이것은 Person 클래스(class)입니다.
        """
    
    print(Person.__doc__) # 이것은 Person 클래스(class)입니다.
    ```
    
- `print(type(person1))`
    - `# <class ‘__main__ Person’>`
    - 해당 클래스가 어디있는지 알려주는 것
    - "지금 네가 실행하고 있는 스크립트 안에 있는 Person이라는 클래스야"라는 뜻
    - 다른 스크립트에 있는 클래스를 가져온다면 __main__이 아닌 다른 것이 찍힐 것

- `__init__`은 클래스의 인스턴스를 생성할 때 자동으로 불림
    - 정의하지 않았다면 기본적으로 내장되어 있는 아무것도 없는 __init__이 불림

- `__del__`은 인스턴스가 메모리에서 사라질 때 호출됨
    - 파이썬은 언어 내부적으로 알아서 메모리를 늘어났다 줄었다가 관리해줌

- 데코레이터는 함수를 꾸며주는 기능을 하는 함수
- static method는 클래스 내 속성을 사용하지 않지만 구조적으로 특정 클래스 안에만 종속시키고 싶을 때 사용

- **DRY**
    - Don’t Repeat Yourself!

- 디버깅을 위해 `print()`를 많이 사용하자
- `assert`문을 디버깅에 사용하기도 한다
    - 예외를 발생시키는 방법 중 하나
    - `assert 'Boolean Expression', 'error message'`
        - 조건이 True가 아니면 `AssertionError` 발생시킴
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
