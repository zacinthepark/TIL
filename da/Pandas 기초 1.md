# Pandas 기초 1: 데이터프레임 생성 및 탐색

## 데이터프레임과 시리즈

### 데이터프레임(Dataframe)이란?

![df](https://github.com/zacinthepark/TIL/assets/86648892/356ca6e2-a1ff-4b8c-b47e-e2d04a31ac6c)

- 데이터 분석에서 가장 중요한 데이터 구조
- 관계형 데이터베이스의 테이블 또는 엑셀 시트와 같은 형태 (2차원 구조)
- 변수들의 집합
    - 각 열을 변수라고 부름

### 시리즈(Series)이란?

![series](https://github.com/zacinthepark/TIL/assets/86648892/d9f3a3ed-892a-42e4-8998-adcbdd384c98)

- 하나의 정보에 대한 데이터들의 집합
- 데이터프레임에서 하나의 열을 떼어낸 것 (1차원)

<img src='https://blog.kakaocdn.net/dn/zy1Or/btqM39h0uLB/fHnntePsHiwAIFStdqGsLk/img.png' width=300 align="left"/>

## 1.데이터프레임 생성

### (1) 데이터프레임 이해

#### 1) 데이터프레임이란

- Pandas 사용 목적이 데이터프레임을 사용하기 위한 목적으로 봐도 됩니다.
- 데이터를 처리, 조회, 분석하는 가장 효율적인 방법이 데이터프레임을 사용하는 것입니다.
- 일반적으로 접하게 되는 **테이블** 형태, **엑셀** 형태로 생각하시면 됩니다.
- 직접 만들 수 있으나 보통은 **csv 파일**, **엑셀 파일** 또는 DB에서 읽어옵니다.

<img src='https://raw.githubusercontent.com/Jangrae/img/master/dataframe_sample.png' width=800 align="left"/>

#### 2) 데이터프레임 형태

- 데이터프레임은 **인덱스(=행 이름)** 와 **열 이름** 이 있고 없고에 따라 다른 형태를 갖습니다.
- 인덱스란 행을 지정할 때 사용하는 정보이고, 열 이름은 열을 지정할 때 사용하는 정보입니다.

<img src='https://raw.githubusercontent.com/Jangrae/img/master/dataframe05.png' width=450 align="left"/>

**① 인덱스와 열 이름이 없는 형태**

- 우선 인덱스와 열 이름이 없는 데이터프레임 형태입니다.
- 열 이름이 없는 데이터프레임은 실무에서는 자주 볼 수 없을 것입니다.

<img src='https://raw.githubusercontent.com/Jangrae/img/master/dataframe01.png' width=380 align="left"/>

**② 열 이름을 지정한 형태**

- 열 이름만 지정한 데이터프레임 형태입니다.
- 특별히 인덱스를 지정할 필요가 없는 경우가 많으므로 자주 보게 되는 형태입니다.

<img src='https://raw.githubusercontent.com/Jangrae/img/master/dataframe02.png' width=380 align="left"/>

**③ 인덱스와 열 이름을 지정한 형태**

- 인덱스와 열 이름 모두를 지정한 데이터프레임 형태입니다.
- 대부분 주식 시세와 같은 날짜가 인덱스로 지정되는 경우입니다.

<img src='https://raw.githubusercontent.com/Jangrae/img/master/dataframe03.png' width=350 align="left"/>

### (2) 데이터프레임 직접 만들기

- **pd.DataFrame()** 함수를 사용해 데이터프레임을 직접 만들 수 있습니다.
- 대부분 리스트, 딕셔너리, Numpy 배열로부터 데이터프레임을 만듭니다.
- 데이터프레임을 만들기 위해서는 다음 세 가지를 위한 데이터가 필요합니다.
    - 데이터
    - 열 이름
    - 인덱스 이름
- 열 이름을 지정하지 않으면 **열 번호**에 기반한 정수(0, 1, 2...)가 열 이름이 됩니다.
- 인덱스 이름을 지정하지 않으면 **행 번호**에 기반한 정수(0, 1, 2...)가 인덱스 이름이 됩니다.

#### 1) 라이브러리 불러오기

- 데이터프레임을 사용하기 위해서 pandas 라이브러리를 pd 별칭을 주어 불러옵니다.

```python
# 라이브러리 불러오기
import pandas as pd
```

#### 2) 딕셔너리로 만들기

- 딕셔너리로 데이터프레임을 만들면 딕셔너리의 **키**가 **열 이름**이 됩니다.
- 인덱스를 지정하지 않으면 행 번호가 인덱스가 됩니다.

```python
# 딕셔너리 만들기
dict1 = {'Name': ['Gildong', 'Sarang', 'Jiemae', 'Yeoin'],
        'Level': ['Gold', 'Bronze', 'Silver', 'Gold'],
        'Score': [56000, 23000, 44000, 52000]}

# 확인
print(dict1)
```

<pre>
{'Name': ['Gildong', 'Sarang', 'Jiemae', 'Yeoin'], 'Level': ['Gold', 'Bronze', 'Silver', 'Gold'], 'Score': [56000, 23000, 44000, 52000]}
</pre>

```python
# 데이터프레임 만들기
df = pd.DataFrame(dict1)

# 확인
print(df.head())
```

<pre>
      Name   Level  Score
0  Gildong    Gold  56000
1   Sarang  Bronze  23000
2   Jiemae  Silver  44000
3    Yeoin    Gold  52000
</pre>

### (3) CSV파일 읽어오기

- 분석용 데이터는 대부분 파일에서 읽어 가져오니 잘 익혀야 할 기능입니다.
- **read_csv()** 함수를 사용해서 CSV 파일에서 데이터를 읽어옵니다.
- csv는 comma로 구분된 텍스트 파일로 이해

**[titanic_simple 데이터 셋 정보]**

- PassengerId : 승객번호
- Survived : 생존여부(1:생존, 0:사망)
- Pclass : 객실등급(1:1등급, 2:2등급, 3:3등급)
- Name : 승객이름
- Sex : 성별(male, female)
- Age : 나이
- Fare : 운임($)
- Embarked : 승선지역(Southhampton, Cherbourg, Queenstown)

```python
# 데이터 읽어오기
path = 'https://raw.githubusercontent.com/DA4BAM/dataset/master/titanic_simple.csv'
data = pd.read_csv(path)  

# 상위 10행만 확인
data.head(10)
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>Fare</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>7.2500</td>
      <td>Southampton</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38.0</td>
      <td>71.2833</td>
      <td>Cherbourg</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26.0</td>
      <td>7.9250</td>
      <td>Southampton</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>
      <td>female</td>
      <td>35.0</td>
      <td>53.1000</td>
      <td>Southampton</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0</td>
      <td>3</td>
      <td>Allen, Mr. William Henry</td>
      <td>male</td>
      <td>35.0</td>
      <td>8.0500</td>
      <td>Southampton</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>0</td>
      <td>3</td>
      <td>Moran, Mr. James</td>
      <td>male</td>
      <td>NaN</td>
      <td>8.4583</td>
      <td>Queenstown</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>0</td>
      <td>1</td>
      <td>McCarthy, Mr. Timothy J</td>
      <td>male</td>
      <td>54.0</td>
      <td>51.8625</td>
      <td>Southampton</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>0</td>
      <td>3</td>
      <td>Palsson, Master. Gosta Leonard</td>
      <td>male</td>
      <td>2.0</td>
      <td>21.0750</td>
      <td>Southampton</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>1</td>
      <td>3</td>
      <td>Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)</td>
      <td>female</td>
      <td>27.0</td>
      <td>11.1333</td>
      <td>Southampton</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>1</td>
      <td>2</td>
      <td>Nasser, Mrs. Nicholas (Adele Achem)</td>
      <td>female</td>
      <td>14.0</td>
      <td>30.0708</td>
      <td>Cherbourg</td>
    </tr>
  </tbody>
</table>
</div>

> 연습문제

[문1] 아래 주어진 경로의 파일에서 데이터를 읽어와 데이터프레임 temp 만들어 보세요.

- 파일 경로: 'https://raw.githubusercontent.com/DA4BAM/dataset/master/Attrition_simple2.CSV'

**[Attrition 데이터 셋 정보]**

|	구분	|	변수 명	|	내용	|	type	|	비고	|

|----|----|----|----|----|

|	**Target**	|	**Attrition**	|	이직여부, Yes , No	|	범주	| 1- 이직, 0- 잔류		|

|	feature	|	Age	|	나이	|	숫자	|		|

|	feature	|	DistanceFromHome	|	집-직장 거리	|	숫자	|	마일	|

|	feature	|	EmployNumber	|	사번	|	숫자	| 	|

|	feature	|	Gender	|	성별	|	범주	| Male, Female		|

|	feature	|	JobSatisfaction	|	직무 만족도	|	범주	|	1 Low, 2 Medium, 3 High, 4 Very High	|

|	feature	|	MaritalStatus	|	결혼상태	|	범주	| Single, Married, Divorced		|

|	feature	|	MonthlyIncome	|	월급	|	숫자	| 달러	|

|	feature	|	OverTime	|	야근여부	|	범주	|	Yes, No	|

|	feature	|	PercentSalaryHike	|	전년대비 급여인상율	|	숫자	|	%	|

|	feature	|	TotalWorkingYears	|	총 경력 연수	|	숫자	|		|

```python
# 데이터 읽어오기
temp_path = 'https://raw.githubusercontent.com/DA4BAM/dataset/master/Attrition_simple2.CSV'
temp = pd.read_csv(temp_path)

# 상위 5개 확인
temp.head(5)
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Attrition</th>
      <th>Age</th>
      <th>DistanceFromHome</th>
      <th>EmployeeNumber</th>
      <th>Gender</th>
      <th>JobSatisfaction</th>
      <th>MaritalStatus</th>
      <th>MonthlyIncome</th>
      <th>OverTime</th>
      <th>PercentSalaryHike</th>
      <th>TotalWorkingYears</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>33</td>
      <td>7</td>
      <td>817</td>
      <td>Male</td>
      <td>3</td>
      <td>Married</td>
      <td>11691</td>
      <td>No</td>
      <td>11</td>
      <td>14</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>35</td>
      <td>18</td>
      <td>1412</td>
      <td>Male</td>
      <td>4</td>
      <td>Single</td>
      <td>9362</td>
      <td>No</td>
      <td>11</td>
      <td>10</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>42</td>
      <td>6</td>
      <td>1911</td>
      <td>Male</td>
      <td>1</td>
      <td>Married</td>
      <td>13348</td>
      <td>No</td>
      <td>13</td>
      <td>18</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0</td>
      <td>46</td>
      <td>2</td>
      <td>1204</td>
      <td>Female</td>
      <td>1</td>
      <td>Married</td>
      <td>17048</td>
      <td>No</td>
      <td>23</td>
      <td>28</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>22</td>
      <td>4</td>
      <td>593</td>
      <td>Male</td>
      <td>3</td>
      <td>Single</td>
      <td>3894</td>
      <td>No</td>
      <td>16</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>

[문2] csv file로부터 읽어옵시다.

- 파일 이름 : 'airquality_simple.csv'
- 파일을 home directory로 복사해 넣고 읽어 옵니다.

**[airquality_simple 데이터 셋 정보]**

- Ozone : 오존농도
- Solar.R: 태양복사열
- Wind: 풍속
- Temp: 기온
- Month: 월
- Day: 일

```python
# import os
# os.getcwd()
```

```python
# 데이터 읽어오기
# temp_path = os.getcwd() + '/airquality_simple.csv'
# temp = pd.read_csv(temp_path)
temp = pd.read_csv('airquality_simple.csv')

# 상위 5개 확인
temp.head(5)
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Ozone</th>
      <th>Solar.R</th>
      <th>Wind</th>
      <th>Temp</th>
      <th>Month</th>
      <th>Day</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>41</td>
      <td>190.0</td>
      <td>7.4</td>
      <td>67</td>
      <td>5</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>36</td>
      <td>118.0</td>
      <td>8.0</td>
      <td>72</td>
      <td>5</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>12</td>
      <td>149.0</td>
      <td>12.6</td>
      <td>74</td>
      <td>5</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>18</td>
      <td>313.0</td>
      <td>11.5</td>
      <td>62</td>
      <td>5</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>19</td>
      <td>NaN</td>
      <td>14.3</td>
      <td>56</td>
      <td>5</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>

## 2.데이터프레임 탐색

- 파일에서 불러온 데이터의 크기, 내용, 분포, 누락된 값 등을 확인할 수 있어야 합니다.
- 확인된 내용을 통해 데이터 전처리 필요 여부를 결정합니다.
- 데이터를 알아야 데이터를 분석할 수 있습니다.

```python
# 라이브러리 불러오기
import pandas as pd
```

* Attrition 데이터 불러오기

**[Attrition 데이터 셋 정보]**

|	구분	|	변수 명	|	내용	|	type	|	비고	|

|----|----|----|----|----|

|	**Target**	|	**Attrition**	|	이직여부, Yes , No	|	범주	| 1- 이직, 0- 잔류		|

|	feature	|	Age	|	나이	|	숫자	|		|

|	feature	|	DistanceFromHome	|	집-직장 거리	|	숫자	|	마일	|

|	feature	|	EmployNumber	|	사번	|	숫자	| 	|

|	feature	|	Gender	|	성별	|	범주	| Male, Female		|

|	feature	|	JobSatisfaction	|	직무 만족도	|	범주	|	1 Low, 2 Medium, 3 High, 4 Very High	|

|	feature	|	MaritalStatus	|	결혼상태	|	범주	| Single, Married, Divorced		|

|	feature	|	MonthlyIncome	|	월급	|	숫자	| 달러	|

|	feature	|	OverTime	|	야근여부	|	범주	|	Yes, No	|

|	feature	|	PercentSalaryHike	|	전년대비 급여인상율	|	숫자	|	%	|

|	feature	|	TotalWorkingYears	|	총 경력 연수	|	숫자	|		|

```python
# 데이터 읽어오기
path = 'https://raw.githubusercontent.com/DA4BAM/dataset/master/Attrition_simple2.CSV'
data = pd.read_csv(path)  

# 상위 5개 확인
data.head(5)
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Attrition</th>
      <th>Age</th>
      <th>DistanceFromHome</th>
      <th>EmployeeNumber</th>
      <th>Gender</th>
      <th>JobSatisfaction</th>
      <th>MaritalStatus</th>
      <th>MonthlyIncome</th>
      <th>OverTime</th>
      <th>PercentSalaryHike</th>
      <th>TotalWorkingYears</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>33</td>
      <td>7</td>
      <td>817</td>
      <td>Male</td>
      <td>3</td>
      <td>Married</td>
      <td>11691</td>
      <td>No</td>
      <td>11</td>
      <td>14</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>35</td>
      <td>18</td>
      <td>1412</td>
      <td>Male</td>
      <td>4</td>
      <td>Single</td>
      <td>9362</td>
      <td>No</td>
      <td>11</td>
      <td>10</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>42</td>
      <td>6</td>
      <td>1911</td>
      <td>Male</td>
      <td>1</td>
      <td>Married</td>
      <td>13348</td>
      <td>No</td>
      <td>13</td>
      <td>18</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0</td>
      <td>46</td>
      <td>2</td>
      <td>1204</td>
      <td>Female</td>
      <td>1</td>
      <td>Married</td>
      <td>17048</td>
      <td>No</td>
      <td>23</td>
      <td>28</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>22</td>
      <td>4</td>
      <td>593</td>
      <td>Male</td>
      <td>3</td>
      <td>Single</td>
      <td>3894</td>
      <td>No</td>
      <td>16</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>

**[참고] 자주 사용할 만한 메서드들**

- head(): 상위 데이터 확인
- tail(): 하위 데이터 확인
- shape: 데이터프레임 크기
- values: 값 정보 확인(저장하면 2차원 numpy 배열이 됨)
- columns: 열 정보 확인
- dtypes: 열 자료형 확인
- info(): 열에 대한 상세한 정보 확인
- describe(): 기초통계정보 확인

### (1) 상위, 하위 일부 데이터, 크기 확인

- **head(*n*), tail(*n*)** 메소드를 사용해 앞 뒤 데이터를 확인합니다.
- 개수를 지정하지 않으면 기본적으로 5개 행이 조회됩니다.

#### **1) 상위 데이터 확인**

```python
# 상위 10개 행 데이터
data.head(10)
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Attrition</th>
      <th>Age</th>
      <th>DistanceFromHome</th>
      <th>EmployeeNumber</th>
      <th>Gender</th>
      <th>JobSatisfaction</th>
      <th>MaritalStatus</th>
      <th>MonthlyIncome</th>
      <th>OverTime</th>
      <th>PercentSalaryHike</th>
      <th>TotalWorkingYears</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>33</td>
      <td>7</td>
      <td>817</td>
      <td>Male</td>
      <td>3</td>
      <td>Married</td>
      <td>11691</td>
      <td>No</td>
      <td>11</td>
      <td>14</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>35</td>
      <td>18</td>
      <td>1412</td>
      <td>Male</td>
      <td>4</td>
      <td>Single</td>
      <td>9362</td>
      <td>No</td>
      <td>11</td>
      <td>10</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>42</td>
      <td>6</td>
      <td>1911</td>
      <td>Male</td>
      <td>1</td>
      <td>Married</td>
      <td>13348</td>
      <td>No</td>
      <td>13</td>
      <td>18</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0</td>
      <td>46</td>
      <td>2</td>
      <td>1204</td>
      <td>Female</td>
      <td>1</td>
      <td>Married</td>
      <td>17048</td>
      <td>No</td>
      <td>23</td>
      <td>28</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>22</td>
      <td>4</td>
      <td>593</td>
      <td>Male</td>
      <td>3</td>
      <td>Single</td>
      <td>3894</td>
      <td>No</td>
      <td>16</td>
      <td>4</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0</td>
      <td>24</td>
      <td>21</td>
      <td>1551</td>
      <td>Male</td>
      <td>1</td>
      <td>Divorced</td>
      <td>2296</td>
      <td>No</td>
      <td>14</td>
      <td>2</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0</td>
      <td>34</td>
      <td>8</td>
      <td>2068</td>
      <td>Male</td>
      <td>3</td>
      <td>Married</td>
      <td>4404</td>
      <td>No</td>
      <td>12</td>
      <td>6</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0</td>
      <td>30</td>
      <td>20</td>
      <td>1084</td>
      <td>Male</td>
      <td>1</td>
      <td>Married</td>
      <td>9957</td>
      <td>No</td>
      <td>15</td>
      <td>7</td>
    </tr>
    <tr>
      <th>8</th>
      <td>0</td>
      <td>26</td>
      <td>6</td>
      <td>686</td>
      <td>Female</td>
      <td>4</td>
      <td>Married</td>
      <td>2659</td>
      <td>Yes</td>
      <td>13</td>
      <td>3</td>
    </tr>
    <tr>
      <th>9</th>
      <td>1</td>
      <td>24</td>
      <td>3</td>
      <td>720</td>
      <td>Female</td>
      <td>3</td>
      <td>Single</td>
      <td>4577</td>
      <td>No</td>
      <td>14</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>

#### **2) 하위 데이터 확인**

```python
# 하위 3개 행 데이터
data.tail(3)
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Attrition</th>
      <th>Age</th>
      <th>DistanceFromHome</th>
      <th>EmployeeNumber</th>
      <th>Gender</th>
      <th>JobSatisfaction</th>
      <th>MaritalStatus</th>
      <th>MonthlyIncome</th>
      <th>OverTime</th>
      <th>PercentSalaryHike</th>
      <th>TotalWorkingYears</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1193</th>
      <td>0</td>
      <td>29</td>
      <td>9</td>
      <td>1558</td>
      <td>Male</td>
      <td>3</td>
      <td>Married</td>
      <td>2451</td>
      <td>No</td>
      <td>18</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1194</th>
      <td>0</td>
      <td>29</td>
      <td>2</td>
      <td>469</td>
      <td>Male</td>
      <td>3</td>
      <td>Married</td>
      <td>4649</td>
      <td>No</td>
      <td>14</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1195</th>
      <td>0</td>
      <td>43</td>
      <td>16</td>
      <td>327</td>
      <td>Female</td>
      <td>4</td>
      <td>Married</td>
      <td>16064</td>
      <td>Yes</td>
      <td>22</td>
      <td>22</td>
    </tr>
  </tbody>
</table>
</div>

#### **3) 크기 확인 .shape**

- **(rows, cols)** 값을 갖는 **튜플** 형태로 확인이 가능합니다.
- 데이터를 분석할 때 처리할 **데이터 양을 확인**하는 목적으로 많이 사용 합니다.

```python
# 행 수와 열 수 확인
data.shape
```

<pre>
(1196, 11)
</pre>

### (2) 열, 행 정보 보기

#### **1) 열 확인**

```python
# 열 확인
print(data.columns)
print(data.columns.values) # np array 형태
```

<pre>
Index(['Attrition', 'Age', 'DistanceFromHome', 'EmployeeNumber', 'Gender',
       'JobSatisfaction', 'MaritalStatus', 'MonthlyIncome', 'OverTime',
       'PercentSalaryHike', 'TotalWorkingYears'],
      dtype='object')
['Attrition' 'Age' 'DistanceFromHome' 'EmployeeNumber' 'Gender'
 'JobSatisfaction' 'MaritalStatus' 'MonthlyIncome' 'OverTime'
 'PercentSalaryHike' 'TotalWorkingYears']
</pre>

```python
# 데이터프레임을 리스트 함수에 넣으면 열 이름이 리스트로 반환됨.
list(data)
```

<pre>
['Attrition',
 'Age',
 'DistanceFromHome',
 'EmployeeNumber',
 'Gender',
 'JobSatisfaction',
 'MaritalStatus',
 'MonthlyIncome',
 'OverTime',
 'PercentSalaryHike',
 'TotalWorkingYears']
</pre>

#### **2) 자료형 확인**

- int64: 정수형 데이터(int)
- float64: 실수형 데이터(float)
- object: 문자열 데이터(string)

```python
# 열 자료형 확인
data.dtypes
```

<pre>
Attrition             int64
Age                   int64
DistanceFromHome      int64
EmployeeNumber        int64
Gender               object
JobSatisfaction       int64
MaritalStatus        object
MonthlyIncome         int64
OverTime             object
PercentSalaryHike     int64
TotalWorkingYears     int64
dtype: object
</pre>

```python
# 열 자료형, 값 개수 확인
data.info()
```

<pre>
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1196 entries, 0 to 1195
Data columns (total 11 columns):
 #   Column             Non-Null Count  Dtype 
---  ------             --------------  ----- 
 0   Attrition          1196 non-null   int64 
 1   Age                1196 non-null   int64 
 2   DistanceFromHome   1196 non-null   int64 
 3   EmployeeNumber     1196 non-null   int64 
 4   Gender             1196 non-null   object
 5   JobSatisfaction    1196 non-null   int64 
 6   MaritalStatus      1196 non-null   object
 7   MonthlyIncome      1196 non-null   int64 
 8   OverTime           1196 non-null   object
 9   PercentSalaryHike  1196 non-null   int64 
 10  TotalWorkingYears  1196 non-null   int64 
dtypes: int64(8), object(3)
memory usage: 102.9+ KB
</pre>

#### **3) 기초통계정보 확인**

- describe() 메소드는 데이터에 대한 많은 정보를 제공하는 매우 중요한 메소드입니다.
- 데이터분석과정에서 자세히 살펴볼 예정이므로 여기서는 **가볍게 실행만** 해봅니다.
- 개수(count), 평균(mean), 표준편차(std), 최솟값(min), 사분위값(25%, 50%, 75%), 최댓값(max)을 표시합니다.

```python
# 기초통계정보
data.describe()
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Attrition</th>
      <th>Age</th>
      <th>DistanceFromHome</th>
      <th>EmployeeNumber</th>
      <th>JobSatisfaction</th>
      <th>MonthlyIncome</th>
      <th>PercentSalaryHike</th>
      <th>TotalWorkingYears</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>1196.000000</td>
      <td>1196.00000</td>
      <td>1196.000000</td>
      <td>1196.000000</td>
      <td>1196.000000</td>
      <td>1196.000000</td>
      <td>1196.000000</td>
      <td>1196.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>0.163043</td>
      <td>36.94398</td>
      <td>9.258361</td>
      <td>1035.629599</td>
      <td>2.716555</td>
      <td>6520.104515</td>
      <td>15.251672</td>
      <td>11.330268</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.369560</td>
      <td>9.09270</td>
      <td>8.166016</td>
      <td>604.340130</td>
      <td>1.110962</td>
      <td>4665.902253</td>
      <td>3.625946</td>
      <td>7.823821</td>
    </tr>
    <tr>
      <th>min</th>
      <td>0.000000</td>
      <td>18.00000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1009.000000</td>
      <td>11.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>0.000000</td>
      <td>30.00000</td>
      <td>2.000000</td>
      <td>507.750000</td>
      <td>2.000000</td>
      <td>2928.250000</td>
      <td>12.000000</td>
      <td>6.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>0.000000</td>
      <td>36.00000</td>
      <td>7.000000</td>
      <td>1028.000000</td>
      <td>3.000000</td>
      <td>4973.500000</td>
      <td>14.000000</td>
      <td>10.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>0.000000</td>
      <td>43.00000</td>
      <td>14.000000</td>
      <td>1581.250000</td>
      <td>4.000000</td>
      <td>8420.500000</td>
      <td>18.000000</td>
      <td>15.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>1.000000</td>
      <td>60.00000</td>
      <td>29.000000</td>
      <td>2068.000000</td>
      <td>4.000000</td>
      <td>19999.000000</td>
      <td>25.000000</td>
      <td>40.000000</td>
    </tr>
  </tbody>
</table>
</div>

> 연습문제

[문1] 다음 경로의 파일을 읽어와 air 데이터프레임으로 저장하세요.

- 파일 경로: 'https://raw.githubusercontent.com/DA4BAM/dataset/master/airquality_simple.csv'

```python
# 데이터 읽어오기
path = 'https://raw.githubusercontent.com/DA4BAM/dataset/master/airquality_simple.csv'
air = pd.read_csv(path)
```

[문2] 데이터프레임 관련 정보를 확인하세요.

```python
# 상위 데이터 확인
air.head()
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Ozone</th>
      <th>Solar.R</th>
      <th>Wind</th>
      <th>Temp</th>
      <th>Date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>41</td>
      <td>190.0</td>
      <td>7.4</td>
      <td>67</td>
      <td>1973-05-01</td>
    </tr>
    <tr>
      <th>1</th>
      <td>36</td>
      <td>118.0</td>
      <td>8.0</td>
      <td>72</td>
      <td>1973-05-02</td>
    </tr>
    <tr>
      <th>2</th>
      <td>12</td>
      <td>149.0</td>
      <td>12.6</td>
      <td>74</td>
      <td>1973-05-03</td>
    </tr>
    <tr>
      <th>3</th>
      <td>18</td>
      <td>313.0</td>
      <td>11.5</td>
      <td>62</td>
      <td>1973-05-04</td>
    </tr>
    <tr>
      <th>4</th>
      <td>19</td>
      <td>NaN</td>
      <td>14.3</td>
      <td>56</td>
      <td>1973-05-05</td>
    </tr>
  </tbody>
</table>
</div>

```python
# 크기 확인
air.shape
```

<pre>
(153, 5)
</pre>

```python
# 열 이름 확인
# air.columns
list(air)
```

<pre>
['Ozone', 'Solar.R', 'Wind', 'Temp', 'Date']
</pre>

```python
# 열 자료형, 값 개수 확인
air.info()
```

<pre>
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 153 entries, 0 to 152
Data columns (total 5 columns):
 #   Column   Non-Null Count  Dtype  
---  ------   --------------  -----  
 0   Ozone    153 non-null    int64  
 1   Solar.R  146 non-null    float64
 2   Wind     153 non-null    float64
 3   Temp     153 non-null    int64  
 4   Date     153 non-null    object 
dtypes: float64(2), int64(2), object(1)
memory usage: 6.1+ KB
</pre>

```python
# 기초통계정보 확인
air.describe()
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Ozone</th>
      <th>Solar.R</th>
      <th>Wind</th>
      <th>Temp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>153.000000</td>
      <td>146.000000</td>
      <td>153.000000</td>
      <td>153.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>42.052288</td>
      <td>185.931507</td>
      <td>9.957516</td>
      <td>77.882353</td>
    </tr>
    <tr>
      <th>std</th>
      <td>30.156127</td>
      <td>90.058422</td>
      <td>3.523001</td>
      <td>9.465270</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>7.000000</td>
      <td>1.700000</td>
      <td>56.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>20.000000</td>
      <td>115.750000</td>
      <td>7.400000</td>
      <td>72.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>34.000000</td>
      <td>205.000000</td>
      <td>9.700000</td>
      <td>79.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>59.000000</td>
      <td>258.750000</td>
      <td>11.500000</td>
      <td>85.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>168.000000</td>
      <td>334.000000</td>
      <td>20.700000</td>
      <td>97.000000</td>
    </tr>
  </tbody>
</table>
</div>

### (3) 정렬해서 보기

- 인덱스를 기준으로 정렬하는 방법과 특정 열을 기준으로 정렬하는 방법이 있습니다.
- **sort_index()** 메소드로 인덱스를 기준으로 정렬합니다.
- **sort_values()** 메소드로 **특정 열**을 기준으로 정렬합니다.
- **ascending** 옵션을 설정해 오름차순, 내림차순을 설정할 수 있습니다.
    - ascending=True: 오름차순 정렬(기본값)
    - ascending=False: 내림차순 정렬

```python
# 단일 열 정렬
data.sort_values(by='MonthlyIncome', ascending=False)
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Attrition</th>
      <th>Age</th>
      <th>DistanceFromHome</th>
      <th>EmployeeNumber</th>
      <th>Gender</th>
      <th>JobSatisfaction</th>
      <th>MaritalStatus</th>
      <th>MonthlyIncome</th>
      <th>OverTime</th>
      <th>PercentSalaryHike</th>
      <th>TotalWorkingYears</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>240</th>
      <td>0</td>
      <td>52</td>
      <td>1</td>
      <td>259</td>
      <td>Male</td>
      <td>3</td>
      <td>Married</td>
      <td>19999</td>
      <td>No</td>
      <td>14</td>
      <td>34</td>
    </tr>
    <tr>
      <th>234</th>
      <td>0</td>
      <td>41</td>
      <td>7</td>
      <td>1035</td>
      <td>Female</td>
      <td>3</td>
      <td>Divorced</td>
      <td>19973</td>
      <td>No</td>
      <td>22</td>
      <td>21</td>
    </tr>
    <tr>
      <th>322</th>
      <td>0</td>
      <td>56</td>
      <td>4</td>
      <td>1191</td>
      <td>Female</td>
      <td>1</td>
      <td>Divorced</td>
      <td>19943</td>
      <td>No</td>
      <td>13</td>
      <td>28</td>
    </tr>
    <tr>
      <th>530</th>
      <td>0</td>
      <td>50</td>
      <td>11</td>
      <td>226</td>
      <td>Female</td>
      <td>2</td>
      <td>Single</td>
      <td>19926</td>
      <td>No</td>
      <td>15</td>
      <td>21</td>
    </tr>
    <tr>
      <th>532</th>
      <td>1</td>
      <td>55</td>
      <td>2</td>
      <td>787</td>
      <td>Male</td>
      <td>1</td>
      <td>Married</td>
      <td>19859</td>
      <td>Yes</td>
      <td>13</td>
      <td>24</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>150</th>
      <td>1</td>
      <td>29</td>
      <td>24</td>
      <td>1928</td>
      <td>Male</td>
      <td>1</td>
      <td>Single</td>
      <td>1091</td>
      <td>No</td>
      <td>17</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1118</th>
      <td>1</td>
      <td>30</td>
      <td>9</td>
      <td>1876</td>
      <td>Male</td>
      <td>4</td>
      <td>Single</td>
      <td>1081</td>
      <td>No</td>
      <td>13</td>
      <td>1</td>
    </tr>
    <tr>
      <th>709</th>
      <td>0</td>
      <td>28</td>
      <td>10</td>
      <td>1056</td>
      <td>Male</td>
      <td>2</td>
      <td>Married</td>
      <td>1052</td>
      <td>No</td>
      <td>22</td>
      <td>1</td>
    </tr>
    <tr>
      <th>862</th>
      <td>0</td>
      <td>18</td>
      <td>5</td>
      <td>1012</td>
      <td>Male</td>
      <td>4</td>
      <td>Single</td>
      <td>1051</td>
      <td>No</td>
      <td>15</td>
      <td>0</td>
    </tr>
    <tr>
      <th>91</th>
      <td>1</td>
      <td>20</td>
      <td>10</td>
      <td>701</td>
      <td>Male</td>
      <td>3</td>
      <td>Single</td>
      <td>1009</td>
      <td>Yes</td>
      <td>11</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>1196 rows × 11 columns</p>
</div>

```python
# 복합 열 정렬
data.sort_values(by=['JobSatisfaction', 'MonthlyIncome'], ascending=[True, False])
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Attrition</th>
      <th>Age</th>
      <th>DistanceFromHome</th>
      <th>EmployeeNumber</th>
      <th>Gender</th>
      <th>JobSatisfaction</th>
      <th>MaritalStatus</th>
      <th>MonthlyIncome</th>
      <th>OverTime</th>
      <th>PercentSalaryHike</th>
      <th>TotalWorkingYears</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>322</th>
      <td>0</td>
      <td>56</td>
      <td>4</td>
      <td>1191</td>
      <td>Female</td>
      <td>1</td>
      <td>Divorced</td>
      <td>19943</td>
      <td>No</td>
      <td>13</td>
      <td>28</td>
    </tr>
    <tr>
      <th>532</th>
      <td>1</td>
      <td>55</td>
      <td>2</td>
      <td>787</td>
      <td>Male</td>
      <td>1</td>
      <td>Married</td>
      <td>19859</td>
      <td>Yes</td>
      <td>13</td>
      <td>24</td>
    </tr>
    <tr>
      <th>273</th>
      <td>0</td>
      <td>58</td>
      <td>1</td>
      <td>1423</td>
      <td>Female</td>
      <td>1</td>
      <td>Married</td>
      <td>19701</td>
      <td>Yes</td>
      <td>21</td>
      <td>32</td>
    </tr>
    <tr>
      <th>418</th>
      <td>0</td>
      <td>60</td>
      <td>7</td>
      <td>549</td>
      <td>Female</td>
      <td>1</td>
      <td>Married</td>
      <td>19566</td>
      <td>No</td>
      <td>11</td>
      <td>33</td>
    </tr>
    <tr>
      <th>685</th>
      <td>0</td>
      <td>54</td>
      <td>5</td>
      <td>522</td>
      <td>Male</td>
      <td>1</td>
      <td>Married</td>
      <td>19406</td>
      <td>No</td>
      <td>11</td>
      <td>24</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>197</th>
      <td>0</td>
      <td>31</td>
      <td>2</td>
      <td>1974</td>
      <td>Female</td>
      <td>4</td>
      <td>Divorced</td>
      <td>1129</td>
      <td>Yes</td>
      <td>11</td>
      <td>1</td>
    </tr>
    <tr>
      <th>386</th>
      <td>1</td>
      <td>25</td>
      <td>24</td>
      <td>1273</td>
      <td>Male</td>
      <td>4</td>
      <td>Single</td>
      <td>1118</td>
      <td>Yes</td>
      <td>14</td>
      <td>1</td>
    </tr>
    <tr>
      <th>684</th>
      <td>1</td>
      <td>19</td>
      <td>2</td>
      <td>243</td>
      <td>Male</td>
      <td>4</td>
      <td>Single</td>
      <td>1102</td>
      <td>No</td>
      <td>22</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1118</th>
      <td>1</td>
      <td>30</td>
      <td>9</td>
      <td>1876</td>
      <td>Male</td>
      <td>4</td>
      <td>Single</td>
      <td>1081</td>
      <td>No</td>
      <td>13</td>
      <td>1</td>
    </tr>
    <tr>
      <th>862</th>
      <td>0</td>
      <td>18</td>
      <td>5</td>
      <td>1012</td>
      <td>Male</td>
      <td>4</td>
      <td>Single</td>
      <td>1051</td>
      <td>No</td>
      <td>15</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>1196 rows × 11 columns</p>
</div>

```python
# 복합 열 정렬: 별도로 저장하고, 인덱스 reset
temp = data.sort_values(by=['JobSatisfaction', 'MonthlyIncome'], ascending=[True, False])
temp.reset_index(drop = True)
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Attrition</th>
      <th>Age</th>
      <th>DistanceFromHome</th>
      <th>EmployeeNumber</th>
      <th>Gender</th>
      <th>JobSatisfaction</th>
      <th>MaritalStatus</th>
      <th>MonthlyIncome</th>
      <th>OverTime</th>
      <th>PercentSalaryHike</th>
      <th>TotalWorkingYears</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>56</td>
      <td>4</td>
      <td>1191</td>
      <td>Female</td>
      <td>1</td>
      <td>Divorced</td>
      <td>19943</td>
      <td>No</td>
      <td>13</td>
      <td>28</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>55</td>
      <td>2</td>
      <td>787</td>
      <td>Male</td>
      <td>1</td>
      <td>Married</td>
      <td>19859</td>
      <td>Yes</td>
      <td>13</td>
      <td>24</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>58</td>
      <td>1</td>
      <td>1423</td>
      <td>Female</td>
      <td>1</td>
      <td>Married</td>
      <td>19701</td>
      <td>Yes</td>
      <td>21</td>
      <td>32</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0</td>
      <td>60</td>
      <td>7</td>
      <td>549</td>
      <td>Female</td>
      <td>1</td>
      <td>Married</td>
      <td>19566</td>
      <td>No</td>
      <td>11</td>
      <td>33</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>54</td>
      <td>5</td>
      <td>522</td>
      <td>Male</td>
      <td>1</td>
      <td>Married</td>
      <td>19406</td>
      <td>No</td>
      <td>11</td>
      <td>24</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1191</th>
      <td>0</td>
      <td>31</td>
      <td>2</td>
      <td>1974</td>
      <td>Female</td>
      <td>4</td>
      <td>Divorced</td>
      <td>1129</td>
      <td>Yes</td>
      <td>11</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1192</th>
      <td>1</td>
      <td>25</td>
      <td>24</td>
      <td>1273</td>
      <td>Male</td>
      <td>4</td>
      <td>Single</td>
      <td>1118</td>
      <td>Yes</td>
      <td>14</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1193</th>
      <td>1</td>
      <td>19</td>
      <td>2</td>
      <td>243</td>
      <td>Male</td>
      <td>4</td>
      <td>Single</td>
      <td>1102</td>
      <td>No</td>
      <td>22</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1194</th>
      <td>1</td>
      <td>30</td>
      <td>9</td>
      <td>1876</td>
      <td>Male</td>
      <td>4</td>
      <td>Single</td>
      <td>1081</td>
      <td>No</td>
      <td>13</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1195</th>
      <td>0</td>
      <td>18</td>
      <td>5</td>
      <td>1012</td>
      <td>Male</td>
      <td>4</td>
      <td>Single</td>
      <td>1051</td>
      <td>No</td>
      <td>15</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>1196 rows × 11 columns</p>
</div>

> 연습문제

[문1] 다음 경로의 파일을 읽어와 데이터프레임으로 저장하세요.

- 파일 경로: 'https://raw.githubusercontent.com/DA4BAM/dataset/master/airquality_simple.csv'

```python
# 데이터 읽어오기
path = 'https://raw.githubusercontent.com/DA4BAM/dataset/master/airquality_simple.csv'
air = pd.read_csv(path)
air
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Ozone</th>
      <th>Solar.R</th>
      <th>Wind</th>
      <th>Temp</th>
      <th>Date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>41</td>
      <td>190.0</td>
      <td>7.4</td>
      <td>67</td>
      <td>1973-05-01</td>
    </tr>
    <tr>
      <th>1</th>
      <td>36</td>
      <td>118.0</td>
      <td>8.0</td>
      <td>72</td>
      <td>1973-05-02</td>
    </tr>
    <tr>
      <th>2</th>
      <td>12</td>
      <td>149.0</td>
      <td>12.6</td>
      <td>74</td>
      <td>1973-05-03</td>
    </tr>
    <tr>
      <th>3</th>
      <td>18</td>
      <td>313.0</td>
      <td>11.5</td>
      <td>62</td>
      <td>1973-05-04</td>
    </tr>
    <tr>
      <th>4</th>
      <td>19</td>
      <td>NaN</td>
      <td>14.3</td>
      <td>56</td>
      <td>1973-05-05</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>148</th>
      <td>30</td>
      <td>193.0</td>
      <td>6.9</td>
      <td>70</td>
      <td>1973-09-26</td>
    </tr>
    <tr>
      <th>149</th>
      <td>23</td>
      <td>145.0</td>
      <td>13.2</td>
      <td>77</td>
      <td>1973-09-27</td>
    </tr>
    <tr>
      <th>150</th>
      <td>14</td>
      <td>191.0</td>
      <td>14.3</td>
      <td>75</td>
      <td>1973-09-28</td>
    </tr>
    <tr>
      <th>151</th>
      <td>18</td>
      <td>131.0</td>
      <td>8.0</td>
      <td>76</td>
      <td>1973-09-29</td>
    </tr>
    <tr>
      <th>152</th>
      <td>20</td>
      <td>223.0</td>
      <td>11.5</td>
      <td>68</td>
      <td>1973-09-30</td>
    </tr>
  </tbody>
</table>
<p>153 rows × 5 columns</p>
</div>

[문2] Ozone 열을 기준으로 내림차순 정렬해서 조회하세요.

```python
# 내림차순 정렬
air.sort_values(by='Ozone', ascending=False)
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Ozone</th>
      <th>Solar.R</th>
      <th>Wind</th>
      <th>Temp</th>
      <th>Date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>116</th>
      <td>168</td>
      <td>238.0</td>
      <td>3.4</td>
      <td>81</td>
      <td>1973-08-25</td>
    </tr>
    <tr>
      <th>61</th>
      <td>135</td>
      <td>269.0</td>
      <td>4.1</td>
      <td>84</td>
      <td>1973-07-01</td>
    </tr>
    <tr>
      <th>98</th>
      <td>122</td>
      <td>255.0</td>
      <td>4.0</td>
      <td>89</td>
      <td>1973-08-07</td>
    </tr>
    <tr>
      <th>120</th>
      <td>118</td>
      <td>225.0</td>
      <td>2.3</td>
      <td>94</td>
      <td>1973-08-29</td>
    </tr>
    <tr>
      <th>29</th>
      <td>115</td>
      <td>223.0</td>
      <td>5.7</td>
      <td>79</td>
      <td>1973-05-30</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>10</th>
      <td>7</td>
      <td>NaN</td>
      <td>6.9</td>
      <td>74</td>
      <td>1973-05-11</td>
    </tr>
    <tr>
      <th>75</th>
      <td>7</td>
      <td>48.0</td>
      <td>14.3</td>
      <td>80</td>
      <td>1973-07-15</td>
    </tr>
    <tr>
      <th>17</th>
      <td>6</td>
      <td>78.0</td>
      <td>18.4</td>
      <td>57</td>
      <td>1973-05-18</td>
    </tr>
    <tr>
      <th>22</th>
      <td>4</td>
      <td>25.0</td>
      <td>9.7</td>
      <td>61</td>
      <td>1973-05-23</td>
    </tr>
    <tr>
      <th>20</th>
      <td>1</td>
      <td>8.0</td>
      <td>9.7</td>
      <td>59</td>
      <td>1973-05-21</td>
    </tr>
  </tbody>
</table>
<p>153 rows × 5 columns</p>
</div>

[문3] Wind 열을 기준으로 내림차순 정렬해서 상위 10개 행만 조회하세요.

```python
# 오름차순 정렬
air.sort_values(by='Wind', ascending=False).head(10)
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Ozone</th>
      <th>Solar.R</th>
      <th>Wind</th>
      <th>Temp</th>
      <th>Date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>47</th>
      <td>37</td>
      <td>284.0</td>
      <td>20.7</td>
      <td>72</td>
      <td>1973-06-17</td>
    </tr>
    <tr>
      <th>8</th>
      <td>8</td>
      <td>19.0</td>
      <td>20.1</td>
      <td>61</td>
      <td>1973-05-09</td>
    </tr>
    <tr>
      <th>17</th>
      <td>6</td>
      <td>78.0</td>
      <td>18.4</td>
      <td>57</td>
      <td>1973-05-18</td>
    </tr>
    <tr>
      <th>24</th>
      <td>17</td>
      <td>66.0</td>
      <td>16.6</td>
      <td>57</td>
      <td>1973-05-25</td>
    </tr>
    <tr>
      <th>21</th>
      <td>11</td>
      <td>320.0</td>
      <td>16.6</td>
      <td>73</td>
      <td>1973-05-22</td>
    </tr>
    <tr>
      <th>147</th>
      <td>14</td>
      <td>20.0</td>
      <td>16.6</td>
      <td>63</td>
      <td>1973-09-25</td>
    </tr>
    <tr>
      <th>33</th>
      <td>18</td>
      <td>242.0</td>
      <td>16.1</td>
      <td>67</td>
      <td>1973-06-03</td>
    </tr>
    <tr>
      <th>128</th>
      <td>32</td>
      <td>92.0</td>
      <td>15.5</td>
      <td>84</td>
      <td>1973-09-06</td>
    </tr>
    <tr>
      <th>112</th>
      <td>21</td>
      <td>259.0</td>
      <td>15.5</td>
      <td>77</td>
      <td>1973-08-21</td>
    </tr>
    <tr>
      <th>134</th>
      <td>21</td>
      <td>259.0</td>
      <td>15.5</td>
      <td>76</td>
      <td>1973-09-12</td>
    </tr>
  </tbody>
</table>
</div>

### (4) 기본 집계

- 데이터를 좀더 이해하기 위해 고유값, 합, 평균, 최댓값, 최솟값 등을 확인합니다.

#### 1) 고유값 확인

- 범주형 열(열이 가진 값이 일정한 값인 경우, 성별, 등급 등)인지 확인할 때 사용합니다.

**① 고유값 확인**

- unique() 메소드로 고유값을 확인하며, 결괏값은 배열 형태가 됩니다.

```python
# MaritalStatus 열 고유값 확인
print(data['MaritalStatus'].unique())
```

<pre>
['Married' 'Single' 'Divorced']
</pre>

**② 고유값과 개수 확인**

- value_counts() 메소드로 고유값과 그 개수를 확인하며, 결괏값은 시리즈 형태가 됩니다.

```python
# MaritalStatus 열 고유값 개수 확인
print(data['MaritalStatus'].value_counts())
```

<pre>
MaritalStatus
Married     548
Single      384
Divorced    264
Name: count, dtype: int64
</pre>

#### 2) 기본 집계 메소드 사용

- 데이터를 1차 집계 한 후 분석을 진행하는 경우가 많으므로 필히 알아두어야 할 내용입니다.
- 이후에 배우는 Groupby 기능에서 같이 사용됩니다.

```python
# MonthlyIncome 열 합계 조회
print(data['MonthlyIncome'].sum())
```

<pre>
7798045
</pre>

```python
# MonthlyIncome 열 최댓값 조회
print(data['MonthlyIncome'].max())
```

<pre>
19999
</pre>

```python
# 'Age', 'MonthlyIncome' 열 평균값 확인
print(data[['Age', 'MonthlyIncome']].mean())
```

<pre>
Age                36.943980
MonthlyIncome    6520.104515
dtype: float64
</pre>

```python
# 'Age', 'MonthlyIncome' 열 중앙값 확인
print(data[['Age', 'MonthlyIncome']].median())
```

<pre>
Age                36.0
MonthlyIncome    4973.5
dtype: float64
</pre>

> 연습문제

[문1] 다음 경로의 파일을 읽어와 데이터프레임으로 저장하세요.

- 파일 경로: 'https://raw.githubusercontent.com/DA4BAM/dataset/master/airquality_simple.csv'

```python
# 데이터 읽어오기
air = pd.read_csv('https://raw.githubusercontent.com/DA4BAM/dataset/master/airquality_simple.csv')
air
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Ozone</th>
      <th>Solar.R</th>
      <th>Wind</th>
      <th>Temp</th>
      <th>Date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>41</td>
      <td>190.0</td>
      <td>7.4</td>
      <td>67</td>
      <td>1973-05-01</td>
    </tr>
    <tr>
      <th>1</th>
      <td>36</td>
      <td>118.0</td>
      <td>8.0</td>
      <td>72</td>
      <td>1973-05-02</td>
    </tr>
    <tr>
      <th>2</th>
      <td>12</td>
      <td>149.0</td>
      <td>12.6</td>
      <td>74</td>
      <td>1973-05-03</td>
    </tr>
    <tr>
      <th>3</th>
      <td>18</td>
      <td>313.0</td>
      <td>11.5</td>
      <td>62</td>
      <td>1973-05-04</td>
    </tr>
    <tr>
      <th>4</th>
      <td>19</td>
      <td>NaN</td>
      <td>14.3</td>
      <td>56</td>
      <td>1973-05-05</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>148</th>
      <td>30</td>
      <td>193.0</td>
      <td>6.9</td>
      <td>70</td>
      <td>1973-09-26</td>
    </tr>
    <tr>
      <th>149</th>
      <td>23</td>
      <td>145.0</td>
      <td>13.2</td>
      <td>77</td>
      <td>1973-09-27</td>
    </tr>
    <tr>
      <th>150</th>
      <td>14</td>
      <td>191.0</td>
      <td>14.3</td>
      <td>75</td>
      <td>1973-09-28</td>
    </tr>
    <tr>
      <th>151</th>
      <td>18</td>
      <td>131.0</td>
      <td>8.0</td>
      <td>76</td>
      <td>1973-09-29</td>
    </tr>
    <tr>
      <th>152</th>
      <td>20</td>
      <td>223.0</td>
      <td>11.5</td>
      <td>68</td>
      <td>1973-09-30</td>
    </tr>
  </tbody>
</table>
<p>153 rows × 5 columns</p>
</div>

[문2] Ozone 최댓값을 확인하세요.

```python
print(air['Ozone'].max())
```

<pre>
168
</pre>

[문3] Temp, Wind 최솟값을 확인하세요.

```python
print(air[['Temp', 'Wind']].min())
```

<pre>
Temp    56.0
Wind     1.7
dtype: float64
</pre>

### (5) 복습문제

1) pandas 라이브러리를 pd 별칭을 주어 불러오세요.

```python
# 라이브러리 불러오기
import pandas as pd
```

2) read_csv() 함수를 사용해 다음 경로의 파일을 불러와 **titanic** 데이터프레임을 만드세요.

- 파일 경로: https://raw.githubusercontent.com/DA4BAM/dataset/master/titanic_simple.csv

**[titanic_simple 데이터 셋 정보]**

- PassengerId : 승객번호
- Survived : 생존여부(1:생존, 0:사망)
- Pclass : 객실등급(1:1등급, 2:2등급, 3:3등급)
- Name : 승객이름
- Sex : 성별(male, female)
- Age : 나이
- Fare : 운임($)
- Embarked : 승선지역(Southhampton, Cherbourg, Queenstown)

```python
# 파일 읽어오기
titanic = pd.read_csv('https://raw.githubusercontent.com/DA4BAM/dataset/master/titanic_simple.csv')
```

3) head() 메소드로 상위 10개 행 데이터를 확인하세요.

```python
# 상위 10행 출력
titanic.head(10)
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>Fare</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>7.2500</td>
      <td>Southampton</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38.0</td>
      <td>71.2833</td>
      <td>Cherbourg</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26.0</td>
      <td>7.9250</td>
      <td>Southampton</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>
      <td>female</td>
      <td>35.0</td>
      <td>53.1000</td>
      <td>Southampton</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0</td>
      <td>3</td>
      <td>Allen, Mr. William Henry</td>
      <td>male</td>
      <td>35.0</td>
      <td>8.0500</td>
      <td>Southampton</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>0</td>
      <td>3</td>
      <td>Moran, Mr. James</td>
      <td>male</td>
      <td>NaN</td>
      <td>8.4583</td>
      <td>Queenstown</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>0</td>
      <td>1</td>
      <td>McCarthy, Mr. Timothy J</td>
      <td>male</td>
      <td>54.0</td>
      <td>51.8625</td>
      <td>Southampton</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>0</td>
      <td>3</td>
      <td>Palsson, Master. Gosta Leonard</td>
      <td>male</td>
      <td>2.0</td>
      <td>21.0750</td>
      <td>Southampton</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>1</td>
      <td>3</td>
      <td>Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)</td>
      <td>female</td>
      <td>27.0</td>
      <td>11.1333</td>
      <td>Southampton</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>1</td>
      <td>2</td>
      <td>Nasser, Mrs. Nicholas (Adele Achem)</td>
      <td>female</td>
      <td>14.0</td>
      <td>30.0708</td>
      <td>Cherbourg</td>
    </tr>
  </tbody>
</table>
</div>

4) shape 속성을 사용해 행과 열의 개수를 확인하세요.

```python
# 크기 확인
titanic.shape
```

<pre>
(891, 8)
</pre>

5) dtype 속성을 사용해 각 열의 데이터 형식을 확인하세요.

```python
# 열 데이터 형식 확인
titanic.dtypes
```

<pre>
PassengerId      int64
Survived         int64
Pclass           int64
Name            object
Sex             object
Age            float64
Fare           float64
Embarked        object
dtype: object
</pre>

6) info() 메소드를 사용해 각 열의 값 개수와 데이터 형식 등을 한 번에 확인하세요.

```python
# 열 정보 확인
titanic.info()
```

<pre>
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 8 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   PassengerId  891 non-null    int64  
 1   Survived     891 non-null    int64  
 2   Pclass       891 non-null    int64  
 3   Name         891 non-null    object 
 4   Sex          891 non-null    object 
 5   Age          714 non-null    float64
 6   Fare         891 non-null    float64
 7   Embarked     889 non-null    object 
dtypes: float64(2), int64(3), object(3)
memory usage: 55.8+ KB
</pre>

7) describe() 함수를 사용해 기초통계정보를 확인하세요.

```python
# 기초통계정보 확인
titanic.describe()
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Age</th>
      <th>Fare</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>891.000000</td>
      <td>891.000000</td>
      <td>891.000000</td>
      <td>714.000000</td>
      <td>891.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>446.000000</td>
      <td>0.383838</td>
      <td>2.308642</td>
      <td>29.699118</td>
      <td>32.204208</td>
    </tr>
    <tr>
      <th>std</th>
      <td>257.353842</td>
      <td>0.486592</td>
      <td>0.836071</td>
      <td>14.526497</td>
      <td>49.693429</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>0.420000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>223.500000</td>
      <td>0.000000</td>
      <td>2.000000</td>
      <td>20.125000</td>
      <td>7.910400</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>446.000000</td>
      <td>0.000000</td>
      <td>3.000000</td>
      <td>28.000000</td>
      <td>14.454200</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>668.500000</td>
      <td>1.000000</td>
      <td>3.000000</td>
      <td>38.000000</td>
      <td>31.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>891.000000</td>
      <td>1.000000</td>
      <td>3.000000</td>
      <td>80.000000</td>
      <td>512.329200</td>
    </tr>
  </tbody>
</table>
</div>

8) unique() 메소드를 사용해 다음 두 열의 고유값과 그 개수를 각각 확인하세요.

- Embarked
- Pclass

```python
# 고유값 개수 확인
print(titanic['Embarked'].unique())
print(titanic['Pclass'].unique())
```

<pre>
['Southampton' 'Cherbourg' 'Queenstown' nan]
[3 1 2]
</pre>

9) Age, Fare 두 열의 최댓값을 한 번에 확인하세요.

```python
print(titanic[['Age', 'Fare']].max())
```

<pre>
Age      80.0000
Fare    512.3292
dtype: float64
</pre>

10) Fare 열을 기준으로 내림차순 정렬해서 상위 10개를 조회하세요.

```python
titanic.sort_values('Fare', ascending=False).head(10)
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>Fare</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>258</th>
      <td>259</td>
      <td>1</td>
      <td>1</td>
      <td>Ward, Miss. Anna</td>
      <td>female</td>
      <td>35.0</td>
      <td>512.3292</td>
      <td>Cherbourg</td>
    </tr>
    <tr>
      <th>737</th>
      <td>738</td>
      <td>1</td>
      <td>1</td>
      <td>Lesurer, Mr. Gustave J</td>
      <td>male</td>
      <td>35.0</td>
      <td>512.3292</td>
      <td>Cherbourg</td>
    </tr>
    <tr>
      <th>679</th>
      <td>680</td>
      <td>1</td>
      <td>1</td>
      <td>Cardeza, Mr. Thomas Drake Martinez</td>
      <td>male</td>
      <td>36.0</td>
      <td>512.3292</td>
      <td>Cherbourg</td>
    </tr>
    <tr>
      <th>88</th>
      <td>89</td>
      <td>1</td>
      <td>1</td>
      <td>Fortune, Miss. Mabel Helen</td>
      <td>female</td>
      <td>23.0</td>
      <td>263.0000</td>
      <td>Southampton</td>
    </tr>
    <tr>
      <th>27</th>
      <td>28</td>
      <td>0</td>
      <td>1</td>
      <td>Fortune, Mr. Charles Alexander</td>
      <td>male</td>
      <td>19.0</td>
      <td>263.0000</td>
      <td>Southampton</td>
    </tr>
    <tr>
      <th>341</th>
      <td>342</td>
      <td>1</td>
      <td>1</td>
      <td>Fortune, Miss. Alice Elizabeth</td>
      <td>female</td>
      <td>24.0</td>
      <td>263.0000</td>
      <td>Southampton</td>
    </tr>
    <tr>
      <th>438</th>
      <td>439</td>
      <td>0</td>
      <td>1</td>
      <td>Fortune, Mr. Mark</td>
      <td>male</td>
      <td>64.0</td>
      <td>263.0000</td>
      <td>Southampton</td>
    </tr>
    <tr>
      <th>311</th>
      <td>312</td>
      <td>1</td>
      <td>1</td>
      <td>Ryerson, Miss. Emily Borie</td>
      <td>female</td>
      <td>18.0</td>
      <td>262.3750</td>
      <td>Cherbourg</td>
    </tr>
    <tr>
      <th>742</th>
      <td>743</td>
      <td>1</td>
      <td>1</td>
      <td>Ryerson, Miss. Susan Parker "Suzette"</td>
      <td>female</td>
      <td>21.0</td>
      <td>262.3750</td>
      <td>Cherbourg</td>
    </tr>
    <tr>
      <th>118</th>
      <td>119</td>
      <td>0</td>
      <td>1</td>
      <td>Baxter, Mr. Quigg Edmond</td>
      <td>male</td>
      <td>24.0</td>
      <td>247.5208</td>
      <td>Cherbourg</td>
    </tr>
  </tbody>
</table>
</div>
