# Numpy 기초

## 리스트 장점과 한계, 그리고 Numpy

- 리스트
    - 값의 집합(collection), 다른 타입의 데이터도 한꺼번에 저장 가능
    - 요소 변경, 추가, 제거가 용이함
- 그러나 데이터 분석에서의 필요는?
    - 단순히 값의 집합 개념을 넘어서 수학적 계산이 가능해야함
    - 대량의 데이터를 처리하는데 처리 속도가 빨라야함
- Numpy(Numerical Python)
    - 빠른 수치 계산을 위해 C언어로 만들어진 Python 라이브러리
    - 벡터와 행렬 연산에 편리한 기능들을 제공
    - 데이터분석용 라이브러리인 Pandas와 Matplotlib의 기반으로 사용됨
    - Array(벡터, 행렬) 단위로 데이터 관리

![](https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/NumPy_logo_2020.svg/330px-NumPy_logo_2020.svg.png)

## 학습 목표

- Numpy 배열의 기본 개념을 이해합니다.
- 1차원, 2차원, 3차원 배열을 만들 수 있습니다.
- Reshape 기능을 사용해 배열 형태를 바꿀 수 있습니다.
- 인덱싱과 슬라이싱으로 원하는 데이터를 조회할 수 있습니다.
- 배열 사이의 기본적인 연산을 수행할 수 있습니다.

## 1.라이브러리 불러오기

- Numpy 배열을 사용하려면 우선 **numpy** 라이브러리를 불러와야 합니다.
- numpy 라이브러리는 일반적으로 **np** 별칭을 붙여 불러옵니다.

```python
# 라이브러리 불러오기
import numpy as np
```

## 2.배열 만들기

- 편의를 위해 **Numpy 배열**을 그냥 **배열**이라고 부르기로 합시다.
- 이후 데이터 처리시 배열로 변환해 연산을 하거나, 결과가 배열로 표시되는 경우가 있습니다.
- 배열에 대한 개념은 정확히 파악해 두기를 권고합니다.

### (1) 용어 정의

<img src='https://raw.githubusercontent.com/Jangrae/img/master/array.png' width=300 align="left"/>


**[용어]**

- axis: 배열의 각 축
- rank: 축의 개수
- shape: 축의 길이, 배열의 크기

**[3 x 4 배열의 경우]**

- axis 0 과 axis 1 을 갖는 2차원 배열
- rank 2 array
- shape는 (3, 4)

### 데이터 분석 및 모델링에서 Axis 0의 의미

- 데이터의 건수
- 2차원 데이터: (1000, 10)
    - 10개의 값(열, 변수)으로 구성된 데이터 1000건
    - 분석 대상이 1000건, 각 대상은 10개의 정보로 구성됨
- 3차원 데이터: (2500, 28, 28)
    - 28행 28열(28x28) 크기의 2차원 데이터가 2500건
    - 만약 흑백 이미지라면 28x28 이미지가 2500장

### (2) 배열 만들기

- **np.array() 함수**를 사용해서 배열을 만듭니다.
- 대부분 **리스트**로부터 배열을 만들거나, 머신러닝 관련 함수 결과값이 배열이 됩니다.

#### 1) 배열 만들기

* **1차원 배열 만들기**

```python
# 1차원 리스트
a1 = [1, 2, 3, 4, 5]

# 배열로 변환
b1 = np.array(a1)

# 확인
print(b1)
```

<pre>
[1 2 3 4 5]
</pre>

* **2차원 배열 만들기**

```python
# 2차원 리스트
# a2 = [[1.5, 2.5, 3.2], [4.2, 5.7, 6.4]]
a2 = [[1.5, 2.5, 3.2],
      [4.2, 5.7, 6.4]]

# 배열로 변환
b2 = np.array(a2)

# 확인
print(b2)
```

<pre>
[[1.5 2.5 3.2]
 [4.2 5.7 6.4]]
</pre>

* **3차원 배열 만들기**

```python
# 3차원 리스트
# a3 = [[[1, 3, 1], [4, 7, 6], [8, 3, 4]], [[6, 2, 4], [8, 1, 5], [3, 5, 9]]]
a3 = [[[1, 3, 1],
       [4, 7, 6],
       [8, 3, 4]],
      [[6, 2, 4],
       [8, 1, 5],
       [3, 5, 9]]]

# 배열로 변환
b3 = np.array(a3)

# 확인
print(b3)
```

<pre>
[[[1 3 1]
  [4 7 6]
  [8 3 4]]

 [[6 2 4]
  [8 1 5]
  [3 5 9]]]
</pre>

#### 참조: 배열을 만드는 여러 함수들

```python
# np.zeros(): 0으로 채워진 배열
a = np.zeros((2, 2))
print('-----------------')
print(a)

# np.ones(): 1로 채워진 배열
b = np.ones((1, 2))
print('-----------------')
print(b)

# np.full(): 특정 값으로 채워진 배열
c = np.full((2, 2), 7.)
print('-----------------')
print(c)

# np.eye(): 정방향 행렬
# 2x2 단위 행렬(identity matrix)
d = np.eye(2)
print('-----------------')
print(d)

# np.random.random(): 랜덤값으로 채운 배열
e = np.random.random((2, 2))
print('-----------------')
print(e)
```

<pre>
-----------------
[[0. 0.]
 [0. 0.]]
-----------------
[[1. 1.]]
-----------------
[[7. 7.]
 [7. 7.]]
-----------------
[[1. 0.]
 [0. 1.]]
-----------------
[[0.78722601 0.96089936]
 [0.59705526 0.10688608]]
</pre>

#### 2) 배열 정보 확인

- 배열 정보를 확인하는 다음 속성들을 기억하시기 바랍니다.
- 특히 shape 속성은 이후에도 많이 사용될 것입니다.

<img src='https://github.com/DA4BAM/image/blob/main/1,2,3%20%EC%B0%A8%EC%9B%90.png?raw=true' width=800 align="left"/>

* **차원 확인**

    - ndim 속성으로 배열 차원을 확인합니다.

```python
# 차원 확인
print(b1.ndim)
print(b2.ndim)
print(b3.ndim)
```

<pre>
1
2
3
</pre>

* **형태(크기) 확인**

    - shape 속성으로 배열 형태를 확인합니다.
    - 결과는 다음과 같은 형태의 튜플로 표시됩니다.
        - 1차원: (x, )
        - 2차원: (x, y)
        - 3차원: (x, y, z)
    - 앞에서 부터 axis 0, axis 1, axis 2의 크기를 의미합니다.

```python
# 형태(크기) 확인
print(b1.shape)
print(b2.shape)
print(b3.shape)
```

<pre>
(5,)
(2, 3)
(2, 3, 3)
</pre>

* **요소 자료형 확인**

    - dtype 속성으로 배열에 포함된 요소들의 자료형을 확인합니다.
    - 배열은 한 가지 자료형만 가질 수 있다는 특징이 있습니다.

```python
# 요소 자료형 형식 확인
print(b1.dtype)
print(b2.dtype)
print(b3.dtype)
```

<pre>
int32
float64
int32
</pre>

```python
# 자료형 변환 (참조)
# 리스트, 튜플: 직접 배열로 변환 가능
# 문자열, 딕셔너리, 집합: 다른 자료형으로 변환 후 배열로 변환 가능

# 문자열 --> 자료형 변환 --> 2차원 배열
a = np.array([list('python'), list('flower')])
print(a)

# 딕셔너리 --> 키, 값 분해 --> 자료형 변환 --> 2차원 배열
dic = {'a': 1, 'b': 2, 'c': 3}
a = np.array([list(dic.keys()), list(dic.values())])
print(a)

# 집합 --> 자료형 변환 --> 2차원 배열
st = {1, 2, 3}
a = np.array([list(st), list(st)])
print(a)
```

<pre>
[['p' 'y' 't' 'h' 'o' 'n']
 ['f' 'l' 'o' 'w' 'e' 'r']]
[['a' 'b' 'c']
 ['1' '2' '3']]
[[1 2 3]
 [1 2 3]]
</pre>

> 연습문제

[문1] numpy 라이브러리를 np 별칭을 주어 불러오세요.

```python
# 라이브러리 불러오기
import numpy as np
```

[문2] 다음에 주어진 데이터를 갖는 1차원 배열을 만든 후 ndim, shape, dtype을 확인해 보세요.

```python
# 10, 11, 12, 13, 14, 15
lst = [10, 11, 12, 13, 14, 15]

# 배열 만들기
arr = np.array(lst)

# 확인
print(arr)

# 정보 확인
print(arr.ndim)
print(arr.shape)
print(arr.dtype)
```

<pre>
[10 11 12 13 14 15]
1
(6,)
int32
</pre>

[문3] 다음에 주어진 리스트를 요소로 갖는 2차원 배열을 만든 후 ndim, shape, dtype을 확인해 보세요

```python
a = [[11, 12, 13, 14], [15, 16, 17, 18], [19, 20, 21, 22]]

# 배열 만들기
arr = np.array(a)

# 확인
print(arr)

# 정보 확인
print(arr.ndim)
print(arr.shape)
print(arr.dtype)
```

<pre>
[[11 12 13 14]
 [15 16 17 18]
 [19 20 21 22]]
2
(3, 4)
int32
</pre>

#### 3) Reshape

- 배열을 사용할 때 다양한 형태(Shape)로 변환할 필요가 있습니다.
- 배열에 포함된 **요소가 사라지지 않는 형태**라면 자유롭게 변환할 수 있습니다.
- (3, 4) → (2, 6) → (4, 3) → (12, 1) → (6, 2) 등등 요소 개수만 변하지 않으면 됩니다.

```python
# (2, 3) 형태의 2차원 배열 만들기
a = np.array([[1, 2, 3],
              [4, 5, 6]])

# 확인
print(a)
```

<pre>
[[1 2 3]
 [4 5 6]]
</pre>

* **(2, 3) → (3, 2)**

```python
# (3, 2) 형태의 2차원 배열로 Reshape
b = a.reshape(3, 2)

# 확인
print(b)
```

<pre>
[[1 2]
 [3 4]
 [5 6]]
</pre>

* **(2, 3) → (6,)**

```python
# 1차원 배열로 Reshape
# c = a.reshape(6,)
c = a.reshape(6)

# 확인
print(c)
```

<pre>
[1 2 3 4 5 6]
</pre>

* **-1의 편리성**
    - **(*m*, -1)** 또는 **(-1, *n*)** 처럼 사용해 행 또는 열 크기 한 쪽만 지정할 수 있습니다.
    - **(*m*, -1)**: 열의 수는 데이터에 맞게
    - **(-1, *n*)**: 행의 수는 데이터에 맞게

```python
# (2, 3) 형태의 2차원 배열 만들기
a = np.array([[1, 2, 3],
              [4, 5, 6]])

# 확인
print(a)
```

<pre>
[[1 2 3]
 [4 5 6]]
</pre>

```python
# reshape(m, -1) 형태로 지정하여 Reshape 가능
print(a.reshape(1, -1))
print()

print(a.reshape(2, -1))
print()

print(a.reshape(3, -1))
print()

#print(a.reshape(4, -1))
#print(a.reshape(5, -1))

print(a.reshape(6, -1))
```

<pre>
[[1 2 3 4 5 6]]

[[1 2 3]
 [4 5 6]]

[[1 2]
 [3 4]
 [5 6]]

[[1]
 [2]
 [3]
 [4]
 [5]
 [6]]
</pre>

```python
# 만들 수 있는 shape으로만 reshape 가능
print(a.reshape(4, -1))
```

> 연습문제

[문1] 다음에 주어진 배열의 형태(shape)를 확인한 후 요구되는 형태로 바꿔 보세요.

```python
# 배열 만들기
a = np.array([[11, 12, 13, 14],
              [15, 16, 17, 18],
              [19, 20, 21, 22]])

# 배열 형태 확인
print(a.shape)

# (4, ?))형태의 2차원 배열
b = a.reshape(4, -1)

# 확인
print(b.shape)

# (2, ?) 형태의 2차원 배열
c = a.reshape(2, -1)

# 확인
print(c.shape)
```

<pre>
(3, 4)
(4, 3)
(2, 6)
</pre>

### 함수와 메서드

```python
a = [1, 2, 3]  # 리스트
b = (1, 2, 3)  # 튜플
c= np.array([1, 2, 3])  # 배열

# 평균 구하기: 함수
# np.mean()
# 입력 가능한 형태: 리스트 튜플 등
# np array로 변환해서 평균을 구해줌
print(np.mean(a))
print(np.mean(b))
print(np.mean(c))

# 평균 구하기: 메서드 방식
# print(a.mean())  # AttributeError: 'list' object has no attribute 'mean'
# print(b.mean())  # AttributeError: 'tuple' object has no attribute 'mean'
print(c.mean())
```

<pre>
2.0
2.0
2.0
2.0
</pre>

## 3.배열 인덱싱과 슬라이싱

- 지금까지 다룬 자료형들 보다 배열 인덱싱과 슬라이싱이 조금 어렵습니다.

### (1) 인덱싱

- 1차원 배열은 리스트와 방법이 같으므로 설명을 생략합니다.
- **배열[행, 열]** 형태로 특정 위치의 요소를 조회합니다.
    - **배열[행][열]** 형태도 가능합니다.
- **배열[[행1,행2,..], :]** 또는 **배열[[행1,행2,..]]** 형태로 특정 행을 조회합니다.
- **배열[:, [열1,열2,...]]** 형태로 특정 열을 조회합니다.
- **배열[[행1,행2,...], [열1,열2,...]]** 형태로 특정 행의 특정 열을 조회합니다.

<img src='https://github.com/DA4BAM/image/blob/main/%EB%B0%B0%EC%97%B4%20%EC%8A%AC%EB%9D%BC%EC%9D%B4%EC%8B%B1.png?raw=true' width=800 align="left"/>

```python
# (3, 3) 형태의 2차원 배열 만들기
a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# 확인
print(a)
```

<pre>
[[1 2 3]
 [4 5 6]
 [7 8 9]]
</pre>

```python
a[0, 1]
```

<pre>
2
</pre>

```python
a[[0],[1]]
```

<pre>
array([2])
</pre>

#### **1) 요소 조회**

```python
# 첫 번째 행, 두 번째 열 요소 조회
print(a[0, 1])
```

<pre>
2
</pre>

#### **2) 행 조회**

```python
# 첫 번째, 두 번째 행 조회
# print(a[[0, 1], :])
print(a[[0, 1]])
```

<pre>
[[1 2 3]
 [4 5 6]]
</pre>

```python
# 첫 번째, 두 번째, 세 번째 행 조회
# print(a[[0, 1, 2], :])
print(a[[0, 1, 2]])
```

<pre>
[[1 2 3]
 [4 5 6]
 [7 8 9]]
</pre>

#### **3) 열 조회**

```python
# 첫 번째, 두 번째 열 조회
print(a[:, [0, 1]])
```

<pre>
[[1 2]
 [4 5]
 [7 8]]
</pre>

#### **4) 행, 열 조회**

```python
# 배열 확인
print(a)
```

<pre>
[[1 2 3]
 [4 5 6]
 [7 8 9]]
</pre>

```python
# 두 번째 행 두 번째 열의 요소 조회
print(a[[1], [1]])
```

<pre>
[5]
</pre>

```python
# 세 번째 행 두 번째 열의 요소 조회
print(a[[2], [1]])
```

<pre>
[8]
</pre>

> 연습문제

주어진 배열을 이용하여 다음 결과를 얻도록 문제를 푸시오.

```python
a = np.array([[11, 12, 13, 14],
              [15, 16, 17, 18],
              [19, 20, 21, 22]])
```

[문1] 16

```python
a[1, 1]
```

<pre>
16
</pre>

[문2] [19 20 21 22]

```python
a[2]
# a[2, ]
```

<pre>
array([19, 20, 21, 22])
</pre>

[문3] [13  17  21]

```python
a[:, 2]
```

<pre>
array([13, 17, 21])
</pre>

### (2) 슬라이싱

- 2차원 배열 조회 방법
- **배열[행1:행N,열1:열N]** 형태로 지정해 그 위치의 요소를 조회합니다.
- 조회 결과는 **2차원 배열**이 됩니다.
- 마지막 **범위 값은 대상에 포함되지 않습니다.**
- 즉, **배열[1:M, 2:N]**이라면 1 ~ M-1행, 2 ~ N-1열이 조회 대상이 됩니다.

<img src='https://github.com/DA4BAM/image/blob/main/%EB%B0%B0%EC%97%B4%20%EC%8A%AC%EB%9D%BC%EC%9D%B4%EC%8B%B12.png?raw=true' width=800 align="left"/>

```python
# (3, 3) 형태의 2차원 배열 만들기
a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# 확인
print(a)
```

<pre>
[[1 2 3]
 [4 5 6]
 [7 8 9]]
</pre>

```python
# 첫 번째 ~ 두 번째 행 조회
# print(a[0:2, :])
print(a[0:2])
```

<pre>
[[1 2 3]
 [4 5 6]]
</pre>

```python
# 첫 번째 행, 첫 번째 ~ 두 번째 열 조회
print(a[0, 0:2])
```

<pre>
[1 2]
</pre>

```python
# 위 셀에 대해서 1차원이 아닌 2차원으로 결과를 만들고 싶은 경우
print(a[[0], 0:2])
# print(a[0:1, 0:2])
```

<pre>
[[1 2]]
</pre>

```python
# 첫 번째 ~ 세 번째 행, 두 번째 ~ 세 번째 열 조회
print(a[0:3, 1:3])
```

<pre>
[[2 3]
 [5 6]
 [8 9]]
</pre>

```python
# 두 번째 ~ 끝 행, 두 번째 ~ 끝 열 조회
print(a[1:, 1:])
```

<pre>
[[5 6]
 [8 9]]
</pre>

> 연습문제

주어진 배열을 이용하여 다음 결과를 얻도록 문제를 푸시오.

```python
a = np.array([[11, 12, 13, 14],
              [15, 16, 17, 18],
              [19, 20, 21, 22]])
```

[문1]   

[[12]  
[16]  
[20]]

```python
# print(a[:, 1]) # [12 16 20]
print(a[:, [1]])
```

<pre>
[[12]
 [16]
 [20]]
</pre>

[문2]

[[16  17]  
 [20  21]]

```python
print(a[1:, 1:3])
```

<pre>
[[16 17]
 [20 21]]
</pre>

### (3) 조건 조회

- **조건에 맞는 요소를 선택**하는 방식이며, **불리안 방식**이라고 부릅니다.
- 조회 결과는 **1차원 배열**이 됩니다.

```python
# 2차원 배열 만들기
score= np.array([[78, 91, 84, 89, 93, 65],
                 [82, 87, 96, 79, 91, 73]])

# 확인
print(score)
```

<pre>
[[78 91 84 89 93 65]
 [82 87 96 79 91 73]]
</pre>

- **배열[조건]** 형태로 해당 조건에 맞는 요소만 조회합니다.

```python
# 요소 중에서 90 이상인 것만 조회
print(score[score >= 90])
```

<pre>
[91 93 96 91]
</pre>

- 검색 조건을 변수로 선언해 사용할 수 있습니다.

```python
# 요소 중에서 90 이상인 것만 조회
condition = score >= 90
print(score[condition])
```

<pre>
[91 93 96 91]
</pre>

- 여러 조건을 **&** 와 **|** 로 연결하여 조회할 수 있습니다.

```python
# 모든 요소 중에서 90 이상 95 미만인 것만 조회
print(score[(score >= 90) & (score <= 95)])
```

<pre>
[91 93 91]
</pre>

> 연습문제

[문1] 다음 배열에서 80 미만의 데이터만 추출하시오.

```python
# 2차원 배열 만들기
score= np.array([[78, 91, 84, 89, 93, 65],
                 [82, 87, 96, 79, 91, 73]])

# 확인
condition = score < 80
print(condition)

# 80 미만 데이터 조회
print(score[condition])
```

<pre>
[[ True False False False False  True]
 [False False False  True False  True]]
[78 65 79 73]
</pre>

[문2] 다음 배열에서 짝수만 추출해 보세요.

```python
# 2차원 배열 만들기
score= np.array([[78, 91, 84, 89, 93, 65],
                 [82, 87, 96, 79, 91, 73]])

# 확인
condition = score % 2 == 0
print(condition)

# 짝수만 조회
print(score[condition])
```

<pre>
[[ True False  True False False False]
 [ True False  True False False False]]
[78 84 82 96]
</pre>

## 4.배열 연산

- 배열 사이의 더하기, 빼기, 곱하기, 나누기 등은 이해하기 쉽습니다.
- 하지만 행렬 곱, 행렬 합등의 연산은 약간의 수학적 지식이 필요합니다.
- 행렬 연산은 선형 대수를 위한 것이므로 설명을 생략합니다.

<img src='https://github.com/DA4BAM/image/blob/main/%EB%B0%B0%EC%97%B4%EC%97%B0%EC%82%B0.png?raw=true' width=600 align="left"/>

```python
# 두 개의 (2, 2) 형태의 2차원 배열 만들기
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])

# 확인
print(x)
print(y)
```

<pre>
[[1 2]
 [3 4]]
[[5 6]
 [7 8]]
</pre>

### **(1) 배열 사칙연산**

* **더하기**
    - `+` 또는 **np.add()** 함수를 사용합니다.



```python
# 배열 더하기
print(x + y)

# 또는
print(np.add(x, y))
```

<pre>
[[ 6  8]
 [10 12]]
[[ 6  8]
 [10 12]]
</pre>

* **빼기**
    - `-` 또는 **np.subtract()** 함수를 사용합니다.

```python
# 배열 빼기
print(x - y)

# 또는
print(np.subtract(x, y))
```

<pre>
[[-4 -4]
 [-4 -4]]
[[-4 -4]
 [-4 -4]]
</pre>

* **곱하기**
    - `*` 또는 **np.multiply()** 함수를 사용합니다.

```python
# 배열 곱하기
print(x * y)

# 또는
print(np.multiply(x, y))
```

<pre>
[[ 5 12]
 [21 32]]
[[ 5 12]
 [21 32]]
</pre>

* **배열 나누기**
    - `/` 또는 **np.divide()** 함수를 사용합니다.

```python
# 배열 나누기
print(x / y)

# 또는
print(np.divide(x, y))
```

<pre>
[[0.2        0.33333333]
 [0.42857143 0.5       ]]
[[0.2        0.33333333]
 [0.42857143 0.5       ]]
</pre>

* **지수 연산**
    - `**` 또는 **np.power()** 함수를 사용합니다.

```python
# 배열 y 제곱
print(x ** y)

# 또는
print(np.power(x, y))
```

<pre>
[[    1    64]
 [ 2187 65536]]
[[    1    64]
 [ 2187 65536]]
</pre>

```python
# 배열 제곱
print(x ** 2)
```

<pre>
[[ 1  4]
 [ 9 16]]
</pre>

```python
x + 2  # 각 원소에 2를 더함
```

<pre>
array([[3, 4],
       [5, 6]])
</pre>

### **(2) 배열 집계**

- np.sum(), 혹은 array.sum()
    * array.sum() 가능
    * axis = 0 : 열 기준 집계, 행 방향 집계 (행 인덱스 증가 방향)
    * axis = 1 : 행 기준 집계, 열 방향 집계 (열 인덱스 증가 반향)
    * 생략하면 : 전체 집계
- 동일한 형태로 사용 가능한 함수 : np.max(), np.min(), np.mean(), np.std()

```python
# array를 생성합니다.
a = np.array([[1,5,7],[2,3,8]])
print(a)
```

<pre>
[[1 5 7]
 [2 3 8]]
</pre>

```python
# 전체 집계
print(np.sum(a))

# 열기 준 집계
print(np.sum(a, axis = 0))

# 행 기준 집계
print(np.sum(a, axis = 1))
```

<pre>
26
[ 3  8 15]
[13 13]
</pre>

### **(3) 자주 사용되는 함수들**

#### **1) np.argmax(), np.argmin()**

- argmax: 최대값이 있는 곳의 인덱스를 알려달라
- argmin: 최소값이 있는 곳의 인덱스를 알려달라

<img src='https://github.com/DA4BAM/image/blob/main/%EB%B0%B0%EC%97%B4_argmin.png?raw=true' width=800 align="left"/>

```python
print(a)
# 전체 중에서 가장 큰 값의 인덱스
print(np.argmax(a))

# 행 방향 최대값의 인덱스
print(np.argmax(a, axis = 0))

# 열 방향 최대값의 인덱스
print(np.argmax(a, axis = 1))
```

<pre>
[[1 5 7]
 [2 3 8]]
5
[1 0 1]
[2 2]
</pre>

#### **2) np.where**

* np.where(조건문, True일때 값, False일 때 값)

```python
# 선언
a = np.array([1,3,2,7])

# 조건
np.where(a > 2, 1, 0)
```

<pre>
array([0, 1, 0, 1])
</pre>

```python
np.where(a > 2, a, 0)
```

<pre>
array([0, 3, 0, 7])
</pre>

## 5.복습문제

1) numpy 라이브러리를 np 별칭을 주어 불러오세요.

```python
# 라이브러리 불러오기
import numpy as np
```

2) 다음 형태를 갖는 2차원 배열을 만들어 np_arr 변수로 선언하세요.

```python
# [[  1  2  3]
#  [  4  5  6]
#  [  7  8  9]
#  [ 10 11 12]]

# 배열 만들기
np_arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

# 확인
print(np_arr)
```

<pre>
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]
</pre>

3) shape 속성을 사용해 np_arr 배열의 행과 열의 크기를 확인하세요.

```python
# 배열 크기 확인
np_arr.shape
```

<pre>
(4, 3)
</pre>

4) np_arr 배열을 아래 주어진 3 X 4 형태의 배열로 바꿔서 np_02 배열로 선언하고 확인하세요.

```python
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

# 형태 변경
np_02 = np_arr.reshape(3, 4)

# 확인
print(np_02)
```

<pre>
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
</pre>

5) np_arr 배열의 세 번째 행의 요소들을 조회하세요.

```python
# [7 8 9] 조회
print(np_arr[2, :])
```

<pre>
[7 8 9]
</pre>

6) np_arr 배열의 모든 요소에 10을 곱한 결과를 조회하세요.

```python
# 10 곱하기
print(np_arr * 10)
```

<pre>
[[ 10  20  30]
 [ 40  50  60]
 [ 70  80  90]
 [100 110 120]]
</pre>

7) 아래의 출력문이 어떤 값을 출력할 지 추측한 후에 결과를 확인하세요.  

[ 8  9 10 11 12]

```python
# 조건 조회
print(np_arr[np_arr > 7])
```

<pre>
[ 8  9 10 11 12]
</pre>

8) 7번 실습에서 선택된 요소들의 값만 각각 2배로 만드세요.

```python
# 조회 결과에 대한 연산
np_arr[np_arr > 7] = np_arr[np_arr > 7] * 2
```

9) np_arr 배열의 값을 조회해서 변경된 내용을 확인해 보세요.

```python
# 원본 배열 확인
print(np_arr)
```

<pre>
[[ 1  2  3]
 [ 4  5  6]
 [ 7 16 18]
 [20 22 24]]
</pre>

10) np_arr 배열의 요소들 중에서 3의 배수는 1, 아니면 0인 배열을 만들고 조회하시오.

```python
a = np.where(np_arr % 3 == 0, 1, 0)
print(a)
```

<pre>
[[0 0 1]
 [0 0 1]
 [0 0 1]
 [0 0 1]]
</pre>

11) np_arr의 전체 평균, 열별 평균, 행별 평균을 구하세요.

```python
print(np_arr)
print('-'* 50)
print(np.mean(np_arr))
print('-'* 50)
print(np.mean(np_arr, axis = 0))
print('-'* 50)
print(np.mean(np_arr, axis = 1))
```

<pre>
[[ 1  2  3]
 [ 4  5  6]
 [ 7 16 18]
 [20 22 24]]
--------------------------------------------------
10.666666666666666
--------------------------------------------------
[ 8.   11.25 12.75]
--------------------------------------------------
[ 2.          5.         13.66666667 22.        ]
</pre>

## 요약

- 수치 연산을 위해 배열(array)을 생성하고 다루는 패키지
- Array 구조: Axis, Rank, Shape
    - 특별히 Axis 0의 의미 이해
- Array 조회
    - 인덱스: 특정 인덱스, 여러 인덱스, 범위 / 조건 조회
- Array Shape 변형: reshape
- Array 연산
    - 기본 연산: 사칙연산, 지수, 제곱근
- Array 집계
    - sum, mean, min, max, std, ...
    - axis = 0, 1에 따른 연산 방향
- 몇 가지 자주 사용하는 함수
    - np.argmax, np.where, ...
- https://wikidocs.net/14569
