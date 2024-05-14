### Decorator `@`

```python
# Decorator

# 함수에서 코드를 변경하지 않고 기능을 추가, 수정하는 문법
# 함수 안에 중복 코드를 데코레이터 함수로 작성
```

```python
def func1():
    print('code1')
    print('--func1--')
    print('code3')

def func2():
    print('code1')
    print('--func2--')
    print('code3')
```

```python
func1()
func2()
```

<pre>
code1
--func1--
code3
code1
--func2--
code3
</pre>

```python
def deco(func):
    def wrapper(*args, **kwargs):
        print('code1')
        func(*args, **kwargs)
        print('code3')
    return wrapper
```

```python
@deco
def func1():
    print('--func1--')

@deco
def func2():
    print('--func2--')

func1()
func2()
```

<pre>
code1
--func1--
code3
code1
--func2--
code3
</pre>

```python
import time

def show_time(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f'processed time: {end - start}')
    return wrapper
```

```python
@show_time
def func1():
    print('--func1--')

def func2():
    print('--func2--')

func1()
func2()
```

<pre>
--func1--
processed time: 0.002077817916870117
--func2--
</pre>

```python
def login(func):
    def wrapper():
        pw = input('pw: ')
        if pw == '1234':
            func()
        else:
            print('wrong password')
    return wrapper
```

```python
@login
@show_time
def func1():
    print('process after login')
```

```python
func1()
```

<pre>
pw:  123
</pre>
<pre>
wrong password
</pre>

```python
func1()
```

<pre>
pw:  1234
</pre>
<pre>
process after login
processed time: 0.00038433074951171875
</pre>
