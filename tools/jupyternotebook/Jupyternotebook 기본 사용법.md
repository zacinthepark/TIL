## Jupyter Notebook 기본 사용법

---


### 1. 셀 선택, 편집 모드 진입 / 선택 모드

* Enter, Esc, 화살표로 마음껏 움직여 보세요.  
* 편집모드와 선택모드를 구별 할 수 있나요?

### 2. 셀을 실행하는 방법들

아래 실행 단축키 3가지를 다 눌러보고 차이점을 적어 봅시다.

* Alt + Enter : 해당 셀을 실행하고 바로 다음에 빈 코드 셀을 생성함
* Ctrl + Enter : 해당 셀만 실행함
* Shift + Enter : 해당 셀을 실행하고 다음 셀로 넘어감

```python
print('안녕하세요? 에이블스쿨에 참여 하신 여러분을 환영합니다!')
```

### 3. 두가지 종류의 셀

* 코드셀 : 실제 코드를 작성하고 실행하는 셀
* 마크다운 셀(텍스트 셀) : 설명문 등을 작성하는 셀

#### 1) 셀 생성, 셀 삭제

선택된 셀 기준으로

* 위에 셀 생성 : a
* 아래에 셀 생성 : b
* 삭제는 : dd

#### 2) 셀 전환 방법

* 마크다운으로 전환 : m
* 코드셀로 전환 : y

##### 여기는 마크다운 셀

1. Please change this cell into a MarkDown Cell
or we can't run this cell correctly
~< br > 하거나 enter를 두번 치면 한줄 내려감.

```python
#### 여기는 코드셀
# Shift + L: 코드 셀 라인번호 표시

print( '지금 사용하고 있는 웹 기반 개발 도구 이름은?')
answers = input("답 : ")

if answers == 'Jupyter Notebook' :
  print("Good!")
else :
  print('type correctly, plz')
```

### 4. 마크다운 셀(텍스트셀)

몇가지 편집 방법을 알아봅시다.

#### 1) 제목 붙이기

`# 제목1`

`## 제목2`

`### 제목3`

```
* abc
* edf
    * ghi
    * jkl
```

#### 2) 왼쪽 바를 그려줍니다.  

`> 왼쪽 바를 그려줍니다.`

> abc  

#### 3) 굵게 강조하려면...

`오늘은 **jupyter notebook**을 이용합니다.`

#### 4) 링크 삽입, 이미지 삽입

`[여기를 눌러보면 좋은 방법들이 많다!](https://gist.github.com/ninanung/2b81a5db946c26c98c573e3662a92b62)`

`![image.png](attachment:0ed5cbf7-62e2-45d9-a4d6-3b869fa34997.png)`

### 5. 코드 셀

#### 여러줄 주석처리

`Ctrl + /`

```python
sample_list = []
sumsum = 0

for i in range(10) :
  sample_list.append(i)
  sumsum += i
  print(i)
print('loop done')
print(sumsum)
print(sample_list)
```

### 6. 저장

#### 1) jupyter notebook 파일 저장

* ctrl + s

```python
ls
```

#### 2) 코드셀을 python 파일로 저장, 불러오기

```python
%%writefile filename.py
print("aaa")
```

```python
%run filename.py
```

```python
%load filename.py
```
