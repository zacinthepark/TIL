# Pandas 기초 2: 데이터프레임 조회 및 집계

## 데이터프레임 조회

- 보고자 하는 데이터를 즉시 조회할 수 있도록 반복 학습과 실습을 통해 익숙해져야 합니다.
- 데이터프레임을 대상으로 조회하는 방법은 다양합니다.
- 그 중 한 가지 방법을 선택해 일관되게 사용하기를 권고합니다.

```python
# 라이브러리 불러오기
import pandas as pd
```

### (1) 데이터 읽어오기

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

```python
# 확인
data.head()
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

* 시리즈(Series)와 데이터프레임(DataFrame)
    * 데이터프레임 : 2차원 구조
    * 시리즈 : 1차원 구조
        * 데이터프레임에서 열 하나를 띄어 내면 시리즈!

<img src='https://github.com/DA4BAM/image/blob/main/%EC%8B%9C%EB%A6%AC%EC%A6%88,%20%EB%8D%B0%EC%9D%B4%ED%84%B0%ED%94%84%EB%A0%88%EC%9E%84.png?raw=true' width=500 align="left"/>

### (2) 특정 열 조회

- **df.loc[ : , [열 이름1, 열 이름2,...]]** 형태로 조회할 열 이름을 리스트로 지정합니다.
- 열 부분은 생략할 수 있었지만, **행 부분을 생략할 수는 없습니다.**
- 하지만 **df[[열 이름1, 열 이름2,...]]** 형태로 인덱서를 생략함이 일반적입니다.
- 조회할 열이 하나면 리스트 형태가 아니어도 됩니다.
    - 리스트 형태가 아니라면 Series 반환
    - 리스트 형태라면 DataFrame 반환

```python
# Attrition 열 조회 : 시리즈로 조회
data['Attrition']
```

<pre>
0       0
1       0
2       0
3       0
4       1
       ..
1191    0
1192    0
1193    0
1194    0
1195    0
Name: Attrition, Length: 1196, dtype: int64
</pre>

```python
# Attrition 열 조회 2 : 시리즈로 조회
data.Attrition
```

<pre>
0       0
1       0
2       0
3       0
4       1
       ..
1191    0
1192    0
1193    0
1194    0
1195    0
Name: Attrition, Length: 1196, dtype: int64
</pre>

```python
# Attrition 열 조회 3 : 데이터프레임으로 반환
data[['Attrition']]
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Attrition</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>1191</th>
      <td>0</td>
    </tr>
    <tr>
      <th>1192</th>
      <td>0</td>
    </tr>
    <tr>
      <th>1193</th>
      <td>0</td>
    </tr>
    <tr>
      <th>1194</th>
      <td>0</td>
    </tr>
    <tr>
      <th>1195</th>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>1196 rows × 1 columns</p>
</div>

```python
# Attrition, Age 열 조회 : 데이터프레임으로 조회
# 대괄호 안에 또 대괄호로 읽지 마시고, 대괄호 안에 리스트!!!
data[['Attrition', 'Age' ]]
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Attrition</th>
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>33</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>35</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>42</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0</td>
      <td>46</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>22</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1191</th>
      <td>0</td>
      <td>32</td>
    </tr>
    <tr>
      <th>1192</th>
      <td>0</td>
      <td>27</td>
    </tr>
    <tr>
      <th>1193</th>
      <td>0</td>
      <td>29</td>
    </tr>
    <tr>
      <th>1194</th>
      <td>0</td>
      <td>29</td>
    </tr>
    <tr>
      <th>1195</th>
      <td>0</td>
      <td>43</td>
    </tr>
  </tbody>
</table>
<p>1196 rows × 2 columns</p>
</div>

> 연습문제

[문1] data 데이터프레임에 대해 아래 요구사항에 맞는 구문을 작성하고 실행하세요.

```python
# 상위 5개 행 조회
data.loc[0:5, :]
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
  </tbody>
</table>
</div>

```python
# PercentSalaryHike 열만 조회
data['PercentSalaryHike']  # type: Series
```

<pre>
0       11
1       11
2       13
3       23
4       16
        ..
1191    12
1192    11
1193    18
1194    14
1195    22
Name: PercentSalaryHike, Length: 1196, dtype: int64
</pre>

```python
data[['PercentSalaryHike']]  # type: DataFrame
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PercentSalaryHike</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>11</td>
    </tr>
    <tr>
      <th>1</th>
      <td>11</td>
    </tr>
    <tr>
      <th>2</th>
      <td>13</td>
    </tr>
    <tr>
      <th>3</th>
      <td>23</td>
    </tr>
    <tr>
      <th>4</th>
      <td>16</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>1191</th>
      <td>12</td>
    </tr>
    <tr>
      <th>1192</th>
      <td>11</td>
    </tr>
    <tr>
      <th>1193</th>
      <td>18</td>
    </tr>
    <tr>
      <th>1194</th>
      <td>14</td>
    </tr>
    <tr>
      <th>1195</th>
      <td>22</td>
    </tr>
  </tbody>
</table>
<p>1196 rows × 1 columns</p>
</div>

```python
#  Age, DistanceFromHome, Gender열만 조회
data[['Age', 'DistanceFromHome', 'Gender']]
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>DistanceFromHome</th>
      <th>Gender</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>33</td>
      <td>7</td>
      <td>Male</td>
    </tr>
    <tr>
      <th>1</th>
      <td>35</td>
      <td>18</td>
      <td>Male</td>
    </tr>
    <tr>
      <th>2</th>
      <td>42</td>
      <td>6</td>
      <td>Male</td>
    </tr>
    <tr>
      <th>3</th>
      <td>46</td>
      <td>2</td>
      <td>Female</td>
    </tr>
    <tr>
      <th>4</th>
      <td>22</td>
      <td>4</td>
      <td>Male</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1191</th>
      <td>32</td>
      <td>5</td>
      <td>Female</td>
    </tr>
    <tr>
      <th>1192</th>
      <td>27</td>
      <td>19</td>
      <td>Male</td>
    </tr>
    <tr>
      <th>1193</th>
      <td>29</td>
      <td>9</td>
      <td>Male</td>
    </tr>
    <tr>
      <th>1194</th>
      <td>29</td>
      <td>2</td>
      <td>Male</td>
    </tr>
    <tr>
      <th>1195</th>
      <td>43</td>
      <td>16</td>
      <td>Female</td>
    </tr>
  </tbody>
</table>
<p>1196 rows × 3 columns</p>
</div>

```python
# Age, DistanceFromHome, Gender열만 DistanceFromHome 열 기준으로 내림차순 정렬해서 조회
data[['Age', 'DistanceFromHome', 'Gender']].sort_values(by='DistanceFromHome', ascending=False).head(10)
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>DistanceFromHome</th>
      <th>Gender</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>198</th>
      <td>50</td>
      <td>29</td>
      <td>Male</td>
    </tr>
    <tr>
      <th>245</th>
      <td>32</td>
      <td>29</td>
      <td>Female</td>
    </tr>
    <tr>
      <th>614</th>
      <td>24</td>
      <td>29</td>
      <td>Male</td>
    </tr>
    <tr>
      <th>810</th>
      <td>48</td>
      <td>29</td>
      <td>Female</td>
    </tr>
    <tr>
      <th>312</th>
      <td>57</td>
      <td>29</td>
      <td>Male</td>
    </tr>
    <tr>
      <th>307</th>
      <td>28</td>
      <td>29</td>
      <td>Male</td>
    </tr>
    <tr>
      <th>571</th>
      <td>42</td>
      <td>29</td>
      <td>Male</td>
    </tr>
    <tr>
      <th>476</th>
      <td>33</td>
      <td>29</td>
      <td>Female</td>
    </tr>
    <tr>
      <th>289</th>
      <td>52</td>
      <td>29</td>
      <td>Male</td>
    </tr>
    <tr>
      <th>180</th>
      <td>30</td>
      <td>29</td>
      <td>Male</td>
    </tr>
  </tbody>
</table>
</div>

### (3) 조건으로 조회 : **.loc**

- **df.loc[조건]** 형태로 조건을 지정해 조건에 만족하는 데이터만 조회할 수 있습니다.
- 우선 조건이 제대로 판단이 되는지 확인한 후 그 **조건을 대 괄호 안에** 넣으면 됩니다.
- **df.loc[행 조건, 열 이름]**
    - 열 이름은 생략 가능
    - 열 이름 1개 시 결과: 시리즈
    - 열 이름을 리스트로 결과: 데이터프레임

#### 1) 단일 조건 조회

```python
# 조건절(조건문)의 결과는 True, False
data['DistanceFromHome'] > 10
```

<pre>
0       False
1        True
2       False
3       False
4       False
        ...  
1191    False
1192     True
1193    False
1194    False
1195     True
Name: DistanceFromHome, Length: 1196, dtype: bool
</pre>

```python
# DistanceFromHome 열 값이 10 보다 큰 행 조회
data.loc[data['DistanceFromHome'] > 10]
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
      <th>11</th>
      <td>1</td>
      <td>33</td>
      <td>15</td>
      <td>582</td>
      <td>Male</td>
      <td>3</td>
      <td>Married</td>
      <td>13610</td>
      <td>Yes</td>
      <td>12</td>
      <td>15</td>
    </tr>
    <tr>
      <th>15</th>
      <td>0</td>
      <td>34</td>
      <td>23</td>
      <td>60</td>
      <td>Male</td>
      <td>3</td>
      <td>Single</td>
      <td>4568</td>
      <td>No</td>
      <td>20</td>
      <td>10</td>
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
      <th>1181</th>
      <td>0</td>
      <td>35</td>
      <td>28</td>
      <td>1596</td>
      <td>Male</td>
      <td>3</td>
      <td>Married</td>
      <td>3407</td>
      <td>No</td>
      <td>17</td>
      <td>10</td>
    </tr>
    <tr>
      <th>1186</th>
      <td>1</td>
      <td>26</td>
      <td>20</td>
      <td>1818</td>
      <td>Female</td>
      <td>2</td>
      <td>Married</td>
      <td>2148</td>
      <td>Yes</td>
      <td>11</td>
      <td>6</td>
    </tr>
    <tr>
      <th>1188</th>
      <td>0</td>
      <td>29</td>
      <td>19</td>
      <td>1497</td>
      <td>Male</td>
      <td>3</td>
      <td>Divorced</td>
      <td>8620</td>
      <td>No</td>
      <td>14</td>
      <td>10</td>
    </tr>
    <tr>
      <th>1192</th>
      <td>0</td>
      <td>27</td>
      <td>19</td>
      <td>1619</td>
      <td>Male</td>
      <td>1</td>
      <td>Divorced</td>
      <td>4066</td>
      <td>No</td>
      <td>11</td>
      <td>7</td>
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
<p>363 rows × 11 columns</p>
</div>

```python
# 이 방법도 가능하나 결측값이 있을 경우 문제가 발생할 수 있음
# pandas는 loc를 권장
data[data['DistanceFromHome'] > 10]
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
      <th>11</th>
      <td>1</td>
      <td>33</td>
      <td>15</td>
      <td>582</td>
      <td>Male</td>
      <td>3</td>
      <td>Married</td>
      <td>13610</td>
      <td>Yes</td>
      <td>12</td>
      <td>15</td>
    </tr>
    <tr>
      <th>15</th>
      <td>0</td>
      <td>34</td>
      <td>23</td>
      <td>60</td>
      <td>Male</td>
      <td>3</td>
      <td>Single</td>
      <td>4568</td>
      <td>No</td>
      <td>20</td>
      <td>10</td>
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
      <th>1181</th>
      <td>0</td>
      <td>35</td>
      <td>28</td>
      <td>1596</td>
      <td>Male</td>
      <td>3</td>
      <td>Married</td>
      <td>3407</td>
      <td>No</td>
      <td>17</td>
      <td>10</td>
    </tr>
    <tr>
      <th>1186</th>
      <td>1</td>
      <td>26</td>
      <td>20</td>
      <td>1818</td>
      <td>Female</td>
      <td>2</td>
      <td>Married</td>
      <td>2148</td>
      <td>Yes</td>
      <td>11</td>
      <td>6</td>
    </tr>
    <tr>
      <th>1188</th>
      <td>0</td>
      <td>29</td>
      <td>19</td>
      <td>1497</td>
      <td>Male</td>
      <td>3</td>
      <td>Divorced</td>
      <td>8620</td>
      <td>No</td>
      <td>14</td>
      <td>10</td>
    </tr>
    <tr>
      <th>1192</th>
      <td>0</td>
      <td>27</td>
      <td>19</td>
      <td>1619</td>
      <td>Male</td>
      <td>1</td>
      <td>Divorced</td>
      <td>4066</td>
      <td>No</td>
      <td>11</td>
      <td>7</td>
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
<p>363 rows × 11 columns</p>
</div>

#### 2) 여러 조건 조회

- [ ]안에 조건을 여러개 연결할 때 **and 와 or 대신에 & 와 |** 를 사용해야 합니다.
- 그리고 각 조건들은 **(조건1) & (조건2)** 형태로 **괄호** 로 묶어야 합니다.

```python
# and로 여러 조건 연결
data.loc[(data['DistanceFromHome'] > 10) & (data['JobSatisfaction'] == 4)]
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
      <th>50</th>
      <td>0</td>
      <td>29</td>
      <td>15</td>
      <td>346</td>
      <td>Male</td>
      <td>4</td>
      <td>Single</td>
      <td>2340</td>
      <td>No</td>
      <td>19</td>
      <td>6</td>
    </tr>
    <tr>
      <th>51</th>
      <td>0</td>
      <td>45</td>
      <td>28</td>
      <td>1546</td>
      <td>Male</td>
      <td>4</td>
      <td>Married</td>
      <td>2132</td>
      <td>No</td>
      <td>20</td>
      <td>8</td>
    </tr>
    <tr>
      <th>64</th>
      <td>0</td>
      <td>32</td>
      <td>15</td>
      <td>1955</td>
      <td>Female</td>
      <td>4</td>
      <td>Divorced</td>
      <td>6667</td>
      <td>No</td>
      <td>18</td>
      <td>9</td>
    </tr>
    <tr>
      <th>82</th>
      <td>1</td>
      <td>35</td>
      <td>12</td>
      <td>1667</td>
      <td>Male</td>
      <td>4</td>
      <td>Single</td>
      <td>4581</td>
      <td>Yes</td>
      <td>24</td>
      <td>13</td>
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
      <th>1104</th>
      <td>0</td>
      <td>34</td>
      <td>19</td>
      <td>1701</td>
      <td>Female</td>
      <td>4</td>
      <td>Married</td>
      <td>2929</td>
      <td>No</td>
      <td>12</td>
      <td>10</td>
    </tr>
    <tr>
      <th>1126</th>
      <td>0</td>
      <td>35</td>
      <td>11</td>
      <td>1137</td>
      <td>Male</td>
      <td>4</td>
      <td>Divorced</td>
      <td>4968</td>
      <td>No</td>
      <td>11</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1141</th>
      <td>1</td>
      <td>49</td>
      <td>11</td>
      <td>840</td>
      <td>Female</td>
      <td>4</td>
      <td>Married</td>
      <td>7654</td>
      <td>No</td>
      <td>18</td>
      <td>9</td>
    </tr>
    <tr>
      <th>1148</th>
      <td>0</td>
      <td>36</td>
      <td>18</td>
      <td>1133</td>
      <td>Male</td>
      <td>4</td>
      <td>Single</td>
      <td>7779</td>
      <td>No</td>
      <td>20</td>
      <td>18</td>
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
<p>107 rows × 11 columns</p>
</div>

```python
# or 조건 : |
data.loc[(data['DistanceFromHome'] > 10) | (data['JobSatisfaction'] == 4)]
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
      <th>11</th>
      <td>1</td>
      <td>33</td>
      <td>15</td>
      <td>582</td>
      <td>Male</td>
      <td>3</td>
      <td>Married</td>
      <td>13610</td>
      <td>Yes</td>
      <td>12</td>
      <td>15</td>
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
      <th>1186</th>
      <td>1</td>
      <td>26</td>
      <td>20</td>
      <td>1818</td>
      <td>Female</td>
      <td>2</td>
      <td>Married</td>
      <td>2148</td>
      <td>Yes</td>
      <td>11</td>
      <td>6</td>
    </tr>
    <tr>
      <th>1188</th>
      <td>0</td>
      <td>29</td>
      <td>19</td>
      <td>1497</td>
      <td>Male</td>
      <td>3</td>
      <td>Divorced</td>
      <td>8620</td>
      <td>No</td>
      <td>14</td>
      <td>10</td>
    </tr>
    <tr>
      <th>1190</th>
      <td>0</td>
      <td>27</td>
      <td>5</td>
      <td>844</td>
      <td>Male</td>
      <td>4</td>
      <td>Divorced</td>
      <td>12808</td>
      <td>Yes</td>
      <td>16</td>
      <td>9</td>
    </tr>
    <tr>
      <th>1192</th>
      <td>0</td>
      <td>27</td>
      <td>19</td>
      <td>1619</td>
      <td>Male</td>
      <td>1</td>
      <td>Divorced</td>
      <td>4066</td>
      <td>No</td>
      <td>11</td>
      <td>7</td>
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
<p>629 rows × 11 columns</p>
</div>

#### 참고: 만약 열 이름만 지정하고 모든 행을 가져오려면?

```python
# 모든 행
data.loc[:, ['DistanceFromHome', 'JobSatisfaction']]
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>DistanceFromHome</th>
      <th>JobSatisfaction</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>7</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>18</td>
      <td>4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>3</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1191</th>
      <td>5</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1192</th>
      <td>19</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1193</th>
      <td>9</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1194</th>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1195</th>
      <td>16</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
<p>1196 rows × 2 columns</p>
</div>

#### 3) isin(), between()

- **isin([값1, 값2,..., 값n])**: 값1 또는 값2 또는...값n인 데이터만 조회합니다.
- 주의 isin(**리스트**) 값들을 리스트 형태로 입력해야 합니다.

```python
# 값 나열
data.loc[data['JobSatisfaction'].isin([1,4])]
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
      <th>1184</th>
      <td>0</td>
      <td>33</td>
      <td>5</td>
      <td>1395</td>
      <td>Male</td>
      <td>4</td>
      <td>Married</td>
      <td>9998</td>
      <td>No</td>
      <td>13</td>
      <td>8</td>
    </tr>
    <tr>
      <th>1185</th>
      <td>0</td>
      <td>24</td>
      <td>10</td>
      <td>1746</td>
      <td>Male</td>
      <td>4</td>
      <td>Married</td>
      <td>2145</td>
      <td>No</td>
      <td>14</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1190</th>
      <td>0</td>
      <td>27</td>
      <td>5</td>
      <td>844</td>
      <td>Male</td>
      <td>4</td>
      <td>Divorced</td>
      <td>12808</td>
      <td>Yes</td>
      <td>16</td>
      <td>9</td>
    </tr>
    <tr>
      <th>1192</th>
      <td>0</td>
      <td>27</td>
      <td>19</td>
      <td>1619</td>
      <td>Male</td>
      <td>1</td>
      <td>Divorced</td>
      <td>4066</td>
      <td>No</td>
      <td>11</td>
      <td>7</td>
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
<p>616 rows × 11 columns</p>
</div>

- 위 구문은 다음과 같은 의미를 갖습니다.

```python
# or 조건
data.loc[(data['JobSatisfaction'] == 1) | (data['JobSatisfaction'] == 4)]
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
      <th>1184</th>
      <td>0</td>
      <td>33</td>
      <td>5</td>
      <td>1395</td>
      <td>Male</td>
      <td>4</td>
      <td>Married</td>
      <td>9998</td>
      <td>No</td>
      <td>13</td>
      <td>8</td>
    </tr>
    <tr>
      <th>1185</th>
      <td>0</td>
      <td>24</td>
      <td>10</td>
      <td>1746</td>
      <td>Male</td>
      <td>4</td>
      <td>Married</td>
      <td>2145</td>
      <td>No</td>
      <td>14</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1190</th>
      <td>0</td>
      <td>27</td>
      <td>5</td>
      <td>844</td>
      <td>Male</td>
      <td>4</td>
      <td>Divorced</td>
      <td>12808</td>
      <td>Yes</td>
      <td>16</td>
      <td>9</td>
    </tr>
    <tr>
      <th>1192</th>
      <td>0</td>
      <td>27</td>
      <td>19</td>
      <td>1619</td>
      <td>Male</td>
      <td>1</td>
      <td>Divorced</td>
      <td>4066</td>
      <td>No</td>
      <td>11</td>
      <td>7</td>
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
<p>616 rows × 11 columns</p>
</div>

- **between(값1, 값2)**: 값1 ~ 값2까지 범위안의 데이터만 조회합니다.
    * inclusive = 'both' (기본값)
        * 'left', 'right', 'neither'

```python
# 범위 지정
data.loc[data['Age'].between(25, 30)]
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
      <th>16</th>
      <td>0</td>
      <td>30</td>
      <td>5</td>
      <td>197</td>
      <td>Female</td>
      <td>1</td>
      <td>Divorced</td>
      <td>3204</td>
      <td>No</td>
      <td>14</td>
      <td>8</td>
    </tr>
    <tr>
      <th>28</th>
      <td>0</td>
      <td>26</td>
      <td>1</td>
      <td>1893</td>
      <td>Female</td>
      <td>3</td>
      <td>Married</td>
      <td>2933</td>
      <td>Yes</td>
      <td>13</td>
      <td>1</td>
    </tr>
    <tr>
      <th>32</th>
      <td>0</td>
      <td>30</td>
      <td>7</td>
      <td>1224</td>
      <td>Male</td>
      <td>3</td>
      <td>Divorced</td>
      <td>3491</td>
      <td>No</td>
      <td>13</td>
      <td>10</td>
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
      <th>1188</th>
      <td>0</td>
      <td>29</td>
      <td>19</td>
      <td>1497</td>
      <td>Male</td>
      <td>3</td>
      <td>Divorced</td>
      <td>8620</td>
      <td>No</td>
      <td>14</td>
      <td>10</td>
    </tr>
    <tr>
      <th>1190</th>
      <td>0</td>
      <td>27</td>
      <td>5</td>
      <td>844</td>
      <td>Male</td>
      <td>4</td>
      <td>Divorced</td>
      <td>12808</td>
      <td>Yes</td>
      <td>16</td>
      <td>9</td>
    </tr>
    <tr>
      <th>1192</th>
      <td>0</td>
      <td>27</td>
      <td>19</td>
      <td>1619</td>
      <td>Male</td>
      <td>1</td>
      <td>Divorced</td>
      <td>4066</td>
      <td>No</td>
      <td>11</td>
      <td>7</td>
    </tr>
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
  </tbody>
</table>
<p>238 rows × 11 columns</p>
</div>

- 위 구문은 다음과 같은 의미를 갖습니다.

```python
# and 조건
data.loc[(data['Age'] >= 25) & (data['Age'] <= 30)]
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
      <th>16</th>
      <td>0</td>
      <td>30</td>
      <td>5</td>
      <td>197</td>
      <td>Female</td>
      <td>1</td>
      <td>Divorced</td>
      <td>3204</td>
      <td>No</td>
      <td>14</td>
      <td>8</td>
    </tr>
    <tr>
      <th>28</th>
      <td>0</td>
      <td>26</td>
      <td>1</td>
      <td>1893</td>
      <td>Female</td>
      <td>3</td>
      <td>Married</td>
      <td>2933</td>
      <td>Yes</td>
      <td>13</td>
      <td>1</td>
    </tr>
    <tr>
      <th>32</th>
      <td>0</td>
      <td>30</td>
      <td>7</td>
      <td>1224</td>
      <td>Male</td>
      <td>3</td>
      <td>Divorced</td>
      <td>3491</td>
      <td>No</td>
      <td>13</td>
      <td>10</td>
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
      <th>1188</th>
      <td>0</td>
      <td>29</td>
      <td>19</td>
      <td>1497</td>
      <td>Male</td>
      <td>3</td>
      <td>Divorced</td>
      <td>8620</td>
      <td>No</td>
      <td>14</td>
      <td>10</td>
    </tr>
    <tr>
      <th>1190</th>
      <td>0</td>
      <td>27</td>
      <td>5</td>
      <td>844</td>
      <td>Male</td>
      <td>4</td>
      <td>Divorced</td>
      <td>12808</td>
      <td>Yes</td>
      <td>16</td>
      <td>9</td>
    </tr>
    <tr>
      <th>1192</th>
      <td>0</td>
      <td>27</td>
      <td>19</td>
      <td>1619</td>
      <td>Male</td>
      <td>1</td>
      <td>Divorced</td>
      <td>4066</td>
      <td>No</td>
      <td>11</td>
      <td>7</td>
    </tr>
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
  </tbody>
</table>
<p>238 rows × 11 columns</p>
</div>

#### **4) 조건을 만족하는 행의 일부 열 조회**

- **df.loc[조건, ['열 이름1', '열 이름2',...]]** 형태로 조회할 열을 리스트로 지정합니다. ==> 2차원, 데이터프레임형태로 조회

```python
# 조건에 맞는 하나의 열 조회
data.loc[data['MonthlyIncome'] >= 10000, ['Age']]
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>33</td>
    </tr>
    <tr>
      <th>2</th>
      <td>42</td>
    </tr>
    <tr>
      <th>3</th>
      <td>46</td>
    </tr>
    <tr>
      <th>11</th>
      <td>33</td>
    </tr>
    <tr>
      <th>13</th>
      <td>39</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>1157</th>
      <td>42</td>
    </tr>
    <tr>
      <th>1158</th>
      <td>54</td>
    </tr>
    <tr>
      <th>1166</th>
      <td>34</td>
    </tr>
    <tr>
      <th>1190</th>
      <td>27</td>
    </tr>
    <tr>
      <th>1195</th>
      <td>43</td>
    </tr>
  </tbody>
</table>
<p>230 rows × 1 columns</p>
</div>

```python
# 조건에 맞는 여러 열 조회
data.loc[data['MonthlyIncome'] >= 10000, ['Age', 'MaritalStatus', 'TotalWorkingYears']]
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>MaritalStatus</th>
      <th>TotalWorkingYears</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>33</td>
      <td>Married</td>
      <td>14</td>
    </tr>
    <tr>
      <th>2</th>
      <td>42</td>
      <td>Married</td>
      <td>18</td>
    </tr>
    <tr>
      <th>3</th>
      <td>46</td>
      <td>Married</td>
      <td>28</td>
    </tr>
    <tr>
      <th>11</th>
      <td>33</td>
      <td>Married</td>
      <td>15</td>
    </tr>
    <tr>
      <th>13</th>
      <td>39</td>
      <td>Single</td>
      <td>21</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1157</th>
      <td>42</td>
      <td>Single</td>
      <td>24</td>
    </tr>
    <tr>
      <th>1158</th>
      <td>54</td>
      <td>Married</td>
      <td>36</td>
    </tr>
    <tr>
      <th>1166</th>
      <td>34</td>
      <td>Single</td>
      <td>14</td>
    </tr>
    <tr>
      <th>1190</th>
      <td>27</td>
      <td>Divorced</td>
      <td>9</td>
    </tr>
    <tr>
      <th>1195</th>
      <td>43</td>
      <td>Married</td>
      <td>22</td>
    </tr>
  </tbody>
</table>
<p>230 rows × 3 columns</p>
</div>

### (4) 복습문제

[문1] pandas 라이브러리를 pd 별칭을 주어 불러오세요.

```python
# 라이브러리 불러오기
import pandas as pd
```

[문2] read_csv() 함수를 사용해 다음 경로의 파일을 불러와 **titanic** 데이터프레임을 만드세요.

- 파일 경로: 'https://raw.githubusercontent.com/DA4BAM/dataset/master/titanic_simple.csv'

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
path = 'https://raw.githubusercontent.com/DA4BAM/dataset/master/titanic_simple.csv'
titanic = pd.read_csv(path)
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

```python
# nan은 결측치
titanic['Embarked'].unique()
```

<pre>
array(['Southampton', 'Cherbourg', 'Queenstown', nan], dtype=object)
</pre>

[문3] Name 열만 조회하세요.

```python
titanic[['Name']]
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Braund, Mr. Owen Harris</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Heikkinen, Miss. Laina</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Allen, Mr. William Henry</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>886</th>
      <td>Montvila, Rev. Juozas</td>
    </tr>
    <tr>
      <th>887</th>
      <td>Graham, Miss. Margaret Edith</td>
    </tr>
    <tr>
      <th>888</th>
      <td>Johnston, Miss. Catherine Helen "Carrie"</td>
    </tr>
    <tr>
      <th>889</th>
      <td>Behr, Mr. Karl Howell</td>
    </tr>
    <tr>
      <th>890</th>
      <td>Dooley, Mr. Patrick</td>
    </tr>
  </tbody>
</table>
<p>891 rows × 1 columns</p>
</div>

[문4] Name, Age, Sex 열만 조회하세요.

```python
titanic[['Name', 'Age', 'Sex']]
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Age</th>
      <th>Sex</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Braund, Mr. Owen Harris</td>
      <td>22.0</td>
      <td>male</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>38.0</td>
      <td>female</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Heikkinen, Miss. Laina</td>
      <td>26.0</td>
      <td>female</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>
      <td>35.0</td>
      <td>female</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Allen, Mr. William Henry</td>
      <td>35.0</td>
      <td>male</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>886</th>
      <td>Montvila, Rev. Juozas</td>
      <td>27.0</td>
      <td>male</td>
    </tr>
    <tr>
      <th>887</th>
      <td>Graham, Miss. Margaret Edith</td>
      <td>19.0</td>
      <td>female</td>
    </tr>
    <tr>
      <th>888</th>
      <td>Johnston, Miss. Catherine Helen "Carrie"</td>
      <td>NaN</td>
      <td>female</td>
    </tr>
    <tr>
      <th>889</th>
      <td>Behr, Mr. Karl Howell</td>
      <td>26.0</td>
      <td>male</td>
    </tr>
    <tr>
      <th>890</th>
      <td>Dooley, Mr. Patrick</td>
      <td>32.0</td>
      <td>male</td>
    </tr>
  </tbody>
</table>
<p>891 rows × 3 columns</p>
</div>

[문5] Name, Age, Sex 열의 상위 10개 행만 확인하세요.

```python
titanic.loc[:9, ['Name', 'Age', 'Sex']]
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Age</th>
      <th>Sex</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Braund, Mr. Owen Harris</td>
      <td>22.0</td>
      <td>male</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>38.0</td>
      <td>female</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Heikkinen, Miss. Laina</td>
      <td>26.0</td>
      <td>female</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>
      <td>35.0</td>
      <td>female</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Allen, Mr. William Henry</td>
      <td>35.0</td>
      <td>male</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Moran, Mr. James</td>
      <td>NaN</td>
      <td>male</td>
    </tr>
    <tr>
      <th>6</th>
      <td>McCarthy, Mr. Timothy J</td>
      <td>54.0</td>
      <td>male</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Palsson, Master. Gosta Leonard</td>
      <td>2.0</td>
      <td>male</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)</td>
      <td>27.0</td>
      <td>female</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Nasser, Mrs. Nicholas (Adele Achem)</td>
      <td>14.0</td>
      <td>female</td>
    </tr>
  </tbody>
</table>
</div>

[문6] 나이가 70세 이상인 탑승객을 조회하시오.

```python
titanic.loc[titanic['Age'] >= 70]
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
      <th>96</th>
      <td>97</td>
      <td>0</td>
      <td>1</td>
      <td>Goldschmidt, Mr. George B</td>
      <td>male</td>
      <td>71.0</td>
      <td>34.6542</td>
      <td>Cherbourg</td>
    </tr>
    <tr>
      <th>116</th>
      <td>117</td>
      <td>0</td>
      <td>3</td>
      <td>Connors, Mr. Patrick</td>
      <td>male</td>
      <td>70.5</td>
      <td>7.7500</td>
      <td>Queenstown</td>
    </tr>
    <tr>
      <th>493</th>
      <td>494</td>
      <td>0</td>
      <td>1</td>
      <td>Artagaveytia, Mr. Ramon</td>
      <td>male</td>
      <td>71.0</td>
      <td>49.5042</td>
      <td>Cherbourg</td>
    </tr>
    <tr>
      <th>630</th>
      <td>631</td>
      <td>1</td>
      <td>1</td>
      <td>Barkworth, Mr. Algernon Henry Wilson</td>
      <td>male</td>
      <td>80.0</td>
      <td>30.0000</td>
      <td>Southampton</td>
    </tr>
    <tr>
      <th>672</th>
      <td>673</td>
      <td>0</td>
      <td>2</td>
      <td>Mitchell, Mr. Henry Michael</td>
      <td>male</td>
      <td>70.0</td>
      <td>10.5000</td>
      <td>Southampton</td>
    </tr>
    <tr>
      <th>745</th>
      <td>746</td>
      <td>0</td>
      <td>1</td>
      <td>Crosby, Capt. Edward Gifford</td>
      <td>male</td>
      <td>70.0</td>
      <td>71.0000</td>
      <td>Southampton</td>
    </tr>
    <tr>
      <th>851</th>
      <td>852</td>
      <td>0</td>
      <td>3</td>
      <td>Svensson, Mr. Johan</td>
      <td>male</td>
      <td>74.0</td>
      <td>7.7750</td>
      <td>Southampton</td>
    </tr>
  </tbody>
</table>
</div>

[문7] Fare(운임)의 평균을 Fare_mean으로 저장하고 그 값을 확인하세요.

```python
# 평균
Fare_mean = titanic['Fare'].mean()

# 확인
Fare_mean
```

<pre>
32.204207968574636
</pre>

[문8] 평균 운임보다 적게 내고 탑승한 승객을 조회하시오.

```python
titanic.loc[titanic['Fare'] < Fare_mean]
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
      <th>...</th>
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
      <th>886</th>
      <td>887</td>
      <td>0</td>
      <td>2</td>
      <td>Montvila, Rev. Juozas</td>
      <td>male</td>
      <td>27.0</td>
      <td>13.0000</td>
      <td>Southampton</td>
    </tr>
    <tr>
      <th>887</th>
      <td>888</td>
      <td>1</td>
      <td>1</td>
      <td>Graham, Miss. Margaret Edith</td>
      <td>female</td>
      <td>19.0</td>
      <td>30.0000</td>
      <td>Southampton</td>
    </tr>
    <tr>
      <th>888</th>
      <td>889</td>
      <td>0</td>
      <td>3</td>
      <td>Johnston, Miss. Catherine Helen "Carrie"</td>
      <td>female</td>
      <td>NaN</td>
      <td>23.4500</td>
      <td>Southampton</td>
    </tr>
    <tr>
      <th>889</th>
      <td>890</td>
      <td>1</td>
      <td>1</td>
      <td>Behr, Mr. Karl Howell</td>
      <td>male</td>
      <td>26.0</td>
      <td>30.0000</td>
      <td>Cherbourg</td>
    </tr>
    <tr>
      <th>890</th>
      <td>891</td>
      <td>0</td>
      <td>3</td>
      <td>Dooley, Mr. Patrick</td>
      <td>male</td>
      <td>32.0</td>
      <td>7.7500</td>
      <td>Queenstown</td>
    </tr>
  </tbody>
</table>
<p>680 rows × 8 columns</p>
</div>

[문9] 승선지역(Embarked)이 'Southampton', 'Queenstown' 인 승객을 조회하시오.

```python
titanic.loc[titanic['Embarked'].isin(['Southampton', 'Queenstown'])]
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
      <th>...</th>
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
      <th>885</th>
      <td>886</td>
      <td>0</td>
      <td>3</td>
      <td>Rice, Mrs. William (Margaret Norton)</td>
      <td>female</td>
      <td>39.0</td>
      <td>29.1250</td>
      <td>Queenstown</td>
    </tr>
    <tr>
      <th>886</th>
      <td>887</td>
      <td>0</td>
      <td>2</td>
      <td>Montvila, Rev. Juozas</td>
      <td>male</td>
      <td>27.0</td>
      <td>13.0000</td>
      <td>Southampton</td>
    </tr>
    <tr>
      <th>887</th>
      <td>888</td>
      <td>1</td>
      <td>1</td>
      <td>Graham, Miss. Margaret Edith</td>
      <td>female</td>
      <td>19.0</td>
      <td>30.0000</td>
      <td>Southampton</td>
    </tr>
    <tr>
      <th>888</th>
      <td>889</td>
      <td>0</td>
      <td>3</td>
      <td>Johnston, Miss. Catherine Helen "Carrie"</td>
      <td>female</td>
      <td>NaN</td>
      <td>23.4500</td>
      <td>Southampton</td>
    </tr>
    <tr>
      <th>890</th>
      <td>891</td>
      <td>0</td>
      <td>3</td>
      <td>Dooley, Mr. Patrick</td>
      <td>male</td>
      <td>32.0</td>
      <td>7.7500</td>
      <td>Queenstown</td>
    </tr>
  </tbody>
</table>
<p>721 rows × 8 columns</p>
</div>

[문10] 나이(Age)가 10대(10이상, 20 미만)인 남자 청소년의 평균 운임(Fare)을 구해 봅시다.

```python
# titanic.loc[(titanic['Age']>= 10) & (titanic['Age'] < 20) & (titanic['Sex'] == 'male'), 'Fare' ].mean()
# 25.30884385964912

titanic.loc[titanic['Age'].between(10, 20, inclusive = 'left') & (titanic['Sex'] == 'male'), 'Age']
```

<pre>
27     19.0
59     11.0
67     19.0
86     16.0
125    12.0
138    16.0
143    19.0
144    18.0
145    19.0
163    17.0
175    18.0
191    19.0
204    18.0
220    16.0
226    19.0
228    18.0
238    19.0
266    16.0
282    16.0
283    19.0
302    19.0
333    16.0
352    15.0
371    18.0
372    19.0
379    19.0
385    18.0
424    18.0
433    17.0
500    17.0
505    18.0
532    17.0
550    17.0
566    19.0
574    16.0
575    19.0
646    19.0
675    18.0
683    14.0
686    14.0
687    19.0
688    18.0
715    19.0
721    17.0
731    11.0
746    16.0
748    19.0
757    18.0
764    16.0
775    18.0
791    16.0
802    11.0
819    10.0
834    18.0
841    16.0
844    17.0
877    19.0
Name: Age, dtype: float64
</pre>

```python
temp = titanic.groupby(['Sex','Embarked'])[['Age','Fare']].mean()
temp
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Age</th>
      <th>Fare</th>
    </tr>
    <tr>
      <th>Sex</th>
      <th>Embarked</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="3" valign="top">female</th>
      <th>Cherbourg</th>
      <td>28.344262</td>
      <td>75.169805</td>
    </tr>
    <tr>
      <th>Queenstown</th>
      <td>24.291667</td>
      <td>12.634958</td>
    </tr>
    <tr>
      <th>Southampton</th>
      <td>27.771505</td>
      <td>38.740929</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">male</th>
      <th>Cherbourg</th>
      <td>32.998841</td>
      <td>48.262109</td>
    </tr>
    <tr>
      <th>Queenstown</th>
      <td>30.937500</td>
      <td>13.838922</td>
    </tr>
    <tr>
      <th>Southampton</th>
      <td>30.291440</td>
      <td>21.711996</td>
    </tr>
  </tbody>
</table>
</div>

```python
temp1 = temp.reset_index()
temp1
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Sex</th>
      <th>Embarked</th>
      <th>Age</th>
      <th>Fare</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>female</td>
      <td>Cherbourg</td>
      <td>28.344262</td>
      <td>75.169805</td>
    </tr>
    <tr>
      <th>1</th>
      <td>female</td>
      <td>Queenstown</td>
      <td>24.291667</td>
      <td>12.634958</td>
    </tr>
    <tr>
      <th>2</th>
      <td>female</td>
      <td>Southampton</td>
      <td>27.771505</td>
      <td>38.740929</td>
    </tr>
    <tr>
      <th>3</th>
      <td>male</td>
      <td>Cherbourg</td>
      <td>32.998841</td>
      <td>48.262109</td>
    </tr>
    <tr>
      <th>4</th>
      <td>male</td>
      <td>Queenstown</td>
      <td>30.937500</td>
      <td>13.838922</td>
    </tr>
    <tr>
      <th>5</th>
      <td>male</td>
      <td>Southampton</td>
      <td>30.291440</td>
      <td>21.711996</td>
    </tr>
  </tbody>
</table>
</div>

```python
temp1.set_index(['Sex', 'Embarked'])
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Age</th>
      <th>Fare</th>
    </tr>
    <tr>
      <th>Sex</th>
      <th>Embarked</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="3" valign="top">female</th>
      <th>Cherbourg</th>
      <td>28.344262</td>
      <td>75.169805</td>
    </tr>
    <tr>
      <th>Queenstown</th>
      <td>24.291667</td>
      <td>12.634958</td>
    </tr>
    <tr>
      <th>Southampton</th>
      <td>27.771505</td>
      <td>38.740929</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">male</th>
      <th>Cherbourg</th>
      <td>32.998841</td>
      <td>48.262109</td>
    </tr>
    <tr>
      <th>Queenstown</th>
      <td>30.937500</td>
      <td>13.838922</td>
    </tr>
    <tr>
      <th>Southampton</th>
      <td>30.291440</td>
      <td>21.711996</td>
    </tr>
  </tbody>
</table>
</div>

## 데이터프레임 집계

- `dataframe.groupby('집계기준변수', as_index = )['집계대상변수'].집계함수`
    - 집계기준 변수: 월별, 지역별 등 '별'에 해당되는 변수 혹은 리스트 (범주형 변수)
    - 집계대상 변수: 집계함수로 집계할 변수 혹은 리스트 (예: 매출액 합계)
- 상세 데이터가 아닌 집계된 데이터에 대한 분석을 자주 요구하니 익숙해져야 할 내용입니다.
- sum(), mean(), max(), min(), count() 메소드를 사용해 지정한 열 또는 열들을 기준으로 집계합니다.
- 평균을 구하는 메소드가 avg()가 아닌 mean() 임을 주의하기 바랍니다.

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

### (1) 열 하나 집계

- 우선 특정 열의 값 합은 다음과 같이 구할 수 있습니다.

```python
# MonthlyIncome 합계
data['MonthlyIncome'].sum()
```

<pre>
7798045
</pre>

```python
# MonthlyIncome, TotalWorkingYears 각각의 평균
data[['MonthlyIncome', 'TotalWorkingYears']].mean()
```

<pre>
MonthlyIncome        6520.104515
TotalWorkingYears      11.330268
dtype: float64
</pre>

#### 1) 집계하기

- 만일 day 별로 합을 구하고자 한다면 다음과 같이 합니다.
- 아래 결과 값 네 개를 더하면 전체 합이 됩니다.
- **as_index=True**를 설정(기본값)하면 집계 기준이 되는 열이 인덱스 열이 됩니다.
- 집계 결과가 data 열만 가지니 **시리즈**가 됩니다.

```python
# MaritalStatus 별 Age 평균 --> 시리즈
data.groupby('MaritalStatus', as_index=True)['Age'].mean()
```

<pre>
MaritalStatus
Divorced    37.522727
Married     37.704380
Single      35.460938
Name: Age, dtype: float64
</pre>

- [['data']].sum()과 같이 하면 열이 여럿이라는 의미여서 결과가 **데이터프레임**이 됩니다.

```python
# MaritalStatus 별 Age 평균 --> 데이터프레임
data.groupby('MaritalStatus', as_index=True)[['Age']].mean()
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
    </tr>
    <tr>
      <th>MaritalStatus</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Divorced</th>
      <td>37.522727</td>
    </tr>
    <tr>
      <th>Married</th>
      <td>37.704380</td>
    </tr>
    <tr>
      <th>Single</th>
      <td>35.460938</td>
    </tr>
  </tbody>
</table>
</div>

- **as_index=False**를 설정하면 행 번호를 기반으로 한 정수 값이 인덱스로 설정됩니다.

```python
# MaritalStatus 별 Age 평균 --> 데이터프레임
data.groupby('MaritalStatus', as_index=False)[['Age']].mean()
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MaritalStatus</th>
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Divorced</td>
      <td>37.522727</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Married</td>
      <td>37.704380</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Single</td>
      <td>35.460938</td>
    </tr>
  </tbody>
</table>
</div>

#### 2) 데이터프레임으로 선언

- 집계 결과를 새로운 데이터프레임으로 선언하여 사용하는 경우가 많습니다.
- 집계된 결과를 반복해서 사용하거나, 분석 대상이 되는 경우 데이터프레임으로 선언함이 유익합니다.

```python
age_by_maritalstatus = data.groupby('MaritalStatus', as_index=False)[['Age']].mean()
age_by_maritalstatus
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MaritalStatus</th>
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Divorced</td>
      <td>37.522727</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Married</td>
      <td>37.704380</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Single</td>
      <td>35.460938</td>
    </tr>
  </tbody>
</table>
</div>

### (2) 여러 열 집계

- 여러 열에 대한 집계를 같이 할 수 있습니다.
- **[ ['feature1', 'feature2'] ].sum()** 형태와 같이 집계 대상 열을 리스트로 지정합니다.

```python
data.groupby('MaritalStatus', as_index=False)[['Age','MonthlyIncome']].mean()
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MaritalStatus</th>
      <th>Age</th>
      <th>MonthlyIncome</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Divorced</td>
      <td>37.522727</td>
      <td>6707.018939</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Married</td>
      <td>37.704380</td>
      <td>6880.144161</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Single</td>
      <td>35.460938</td>
      <td>5877.794271</td>
    </tr>
  </tbody>
</table>
</div>

- sum() 메소드 앞에 아무 열도 지정하지 않으면 **기준열 이외의 모든 열에 대한 집계**가 수행됩니다.
    * 향후에는 이 기능이 제거될 수 있으므로 숫자형 변수만 집계되도록 명시적으로 지정할 필요가 있음

```python
data.groupby('MaritalStatus', as_index=False).sum()
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MaritalStatus</th>
      <th>Attrition</th>
      <th>Age</th>
      <th>DistanceFromHome</th>
      <th>EmployeeNumber</th>
      <th>Gender</th>
      <th>JobSatisfaction</th>
      <th>MonthlyIncome</th>
      <th>OverTime</th>
      <th>PercentSalaryHike</th>
      <th>TotalWorkingYears</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Divorced</td>
      <td>23</td>
      <td>9906</td>
      <td>2404</td>
      <td>266305</td>
      <td>MaleFemaleFemaleMaleFemaleMaleMaleFemaleFemale...</td>
      <td>716</td>
      <td>1770653</td>
      <td>NoYesNoYesNoNoNoYesNoNoYesNoYesNoNoNoNoNoNoYes...</td>
      <td>3958</td>
      <td>3106</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Married</td>
      <td>69</td>
      <td>20662</td>
      <td>5295</td>
      <td>584446</td>
      <td>MaleMaleFemaleMaleMaleFemaleMaleMaleMaleMaleFe...</td>
      <td>1468</td>
      <td>3770319</td>
      <td>NoNoNoNoNoYesYesNoYesNoYesYesNoNoYesNoNoNoNoNo...</td>
      <td>8431</td>
      <td>6470</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Single</td>
      <td>103</td>
      <td>13617</td>
      <td>3374</td>
      <td>387862</td>
      <td>MaleMaleFemaleMaleMaleMaleFemaleMaleMaleMaleMa...</td>
      <td>1065</td>
      <td>2257073</td>
      <td>NoNoNoNoNoNoYesNoNoNoNoNoNoYesYesNoNoNoYesYesN...</td>
      <td>5852</td>
      <td>3975</td>
    </tr>
  </tbody>
</table>
</div>

- **by=['feature1', 'feature2']** 과 같이 집계 기준 열을 여럿 설정할 수도 있습니다.

```python
# 'MaritalStatus', 'Gender'별 나머지 열들 평균 조회
data_sum = data.groupby(['MaritalStatus', 'Gender'], as_index=False)[['Age','MonthlyIncome']].mean()

# 확인
data_sum
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MaritalStatus</th>
      <th>Gender</th>
      <th>Age</th>
      <th>MonthlyIncome</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Divorced</td>
      <td>Female</td>
      <td>37.010526</td>
      <td>6626.315789</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Divorced</td>
      <td>Male</td>
      <td>37.810651</td>
      <td>6752.384615</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Married</td>
      <td>Female</td>
      <td>38.774194</td>
      <td>7301.493088</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Married</td>
      <td>Male</td>
      <td>37.003021</td>
      <td>6603.912387</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Single</td>
      <td>Female</td>
      <td>35.261146</td>
      <td>5963.445860</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Single</td>
      <td>Male</td>
      <td>35.599119</td>
      <td>5818.555066</td>
    </tr>
  </tbody>
</table>
</div>

### (3) 여러 함수로 한꺼번에 집계 .agg

* df.groupby(  )**.agg(['함수1','함수2', ...])**
* 열 하나에 대해 합계, 평균 등의 집계를 한 번에 수행 가능
* agg() 메소드에 원하는 집계함수 이름을 리스트 형태로 지정
* 여러 열에 대해 여러 집계를 한 번에 수행 가능
* 집계 대상 열과 집계 방법을 리스트 형태로 지정
* 여러 열에 대한 각 열마다 다른 집계를 한 번에 수행 가능
* '열 이름' : '집계 방법' 형태의 key : value 를 갖는 딕셔너리 형태로 지정

```python
data_agg1 = data.groupby('MaritalStatus', as_index=False)[['MonthlyIncome']].agg(['min','max','mean'])
data_agg2 = data.groupby('MaritalStatus', as_index=False)[['MonthlyIncome', 'DistanceFromHome']].agg(['min', 'max', 'mean'])
data_agg3 = data.groupby('MaritalStatus', as_index=False).agg({'MonthlyIncome':'mean', 'DistanceFromHome':'max'})
```

```python
data_agg1
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="3" halign="left">MonthlyIncome</th>
    </tr>
    <tr>
      <th></th>
      <th>min</th>
      <th>max</th>
      <th>mean</th>
    </tr>
    <tr>
      <th>MaritalStatus</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Divorced</th>
      <td>1129</td>
      <td>19973</td>
      <td>6707.018939</td>
    </tr>
    <tr>
      <th>Married</th>
      <td>1052</td>
      <td>19999</td>
      <td>6880.144161</td>
    </tr>
    <tr>
      <th>Single</th>
      <td>1009</td>
      <td>19926</td>
      <td>5877.794271</td>
    </tr>
  </tbody>
</table>
</div>

```python
data_agg2
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="3" halign="left">MonthlyIncome</th>
      <th colspan="3" halign="left">DistanceFromHome</th>
    </tr>
    <tr>
      <th></th>
      <th>min</th>
      <th>max</th>
      <th>mean</th>
      <th>min</th>
      <th>max</th>
      <th>mean</th>
    </tr>
    <tr>
      <th>MaritalStatus</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Divorced</th>
      <td>1129</td>
      <td>19973</td>
      <td>6707.018939</td>
      <td>1</td>
      <td>29</td>
      <td>9.106061</td>
    </tr>
    <tr>
      <th>Married</th>
      <td>1052</td>
      <td>19999</td>
      <td>6880.144161</td>
      <td>1</td>
      <td>29</td>
      <td>9.662409</td>
    </tr>
    <tr>
      <th>Single</th>
      <td>1009</td>
      <td>19926</td>
      <td>5877.794271</td>
      <td>1</td>
      <td>29</td>
      <td>8.786458</td>
    </tr>
  </tbody>
</table>
</div>

```python
data_agg3
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MaritalStatus</th>
      <th>MonthlyIncome</th>
      <th>DistanceFromHome</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Divorced</td>
      <td>6707.018939</td>
      <td>29</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Married</td>
      <td>6880.144161</td>
      <td>29</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Single</td>
      <td>5877.794271</td>
      <td>29</td>
    </tr>
  </tbody>
</table>
</div>

> 연습문제

[문1] 데이터를 불러와 데이터프레임으로 저장합니다.

- 파일 경로 : https://raw.githubusercontent.com/DA4BAM/dataset/master/airquality.csv

**[airquality_simple 데이터 셋 정보]**

- Ozone : 오존농도
- Solar.R: 태양복사열
- Wind: 풍속
- Temp: 기온
- Month: 월
- Day: 일

```python
# 데이터 읽어오기
air = pd.read_csv('https://raw.githubusercontent.com/DA4BAM/dataset/master/airquality.csv')

# 상위 5개 확인
air.head(5)
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
      <td>41.0</td>
      <td>190.0</td>
      <td>7.4</td>
      <td>67</td>
      <td>5</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>36.0</td>
      <td>118.0</td>
      <td>8.0</td>
      <td>72</td>
      <td>5</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>12.0</td>
      <td>149.0</td>
      <td>12.6</td>
      <td>74</td>
      <td>5</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>18.0</td>
      <td>313.0</td>
      <td>11.5</td>
      <td>62</td>
      <td>5</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>14.3</td>
      <td>56</td>
      <td>5</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>

[문2] 월별 Ozone, Wind, Temp 평균을 구해 봅시다.

```python
air_monthly_mean = air.groupby('Month', as_index=False)[['Ozone', 'Wind', 'Temp']].mean()
air_monthly_mean
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Month</th>
      <th>Ozone</th>
      <th>Wind</th>
      <th>Temp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5</td>
      <td>23.615385</td>
      <td>11.622581</td>
      <td>65.548387</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6</td>
      <td>29.444444</td>
      <td>10.266667</td>
      <td>79.100000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7</td>
      <td>59.115385</td>
      <td>8.941935</td>
      <td>83.903226</td>
    </tr>
    <tr>
      <th>3</th>
      <td>8</td>
      <td>59.961538</td>
      <td>8.793548</td>
      <td>83.967742</td>
    </tr>
    <tr>
      <th>4</th>
      <td>9</td>
      <td>31.448276</td>
      <td>10.180000</td>
      <td>76.900000</td>
    </tr>
  </tbody>
</table>
</div>

[문3] 월별 Ozone, Wind, Temp에 대해 최대, 최소, 평균, 표준편차 값을 구해 봅시다.

```python
air_monthly_info = air.groupby('Month', as_index = False)[['Ozone', 'Wind','Temp' ]].agg(['max', 'min', 'mean', 'std'])
air_monthly_info
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="4" halign="left">Ozone</th>
      <th colspan="4" halign="left">Wind</th>
      <th colspan="4" halign="left">Temp</th>
    </tr>
    <tr>
      <th></th>
      <th>max</th>
      <th>min</th>
      <th>mean</th>
      <th>std</th>
      <th>max</th>
      <th>min</th>
      <th>mean</th>
      <th>std</th>
      <th>max</th>
      <th>min</th>
      <th>mean</th>
      <th>std</th>
    </tr>
    <tr>
      <th>Month</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5</th>
      <td>115.0</td>
      <td>1.0</td>
      <td>23.615385</td>
      <td>22.224449</td>
      <td>20.1</td>
      <td>5.7</td>
      <td>11.622581</td>
      <td>3.531450</td>
      <td>81</td>
      <td>56</td>
      <td>65.548387</td>
      <td>6.854870</td>
    </tr>
    <tr>
      <th>6</th>
      <td>71.0</td>
      <td>12.0</td>
      <td>29.444444</td>
      <td>18.207904</td>
      <td>20.7</td>
      <td>1.7</td>
      <td>10.266667</td>
      <td>3.769234</td>
      <td>93</td>
      <td>65</td>
      <td>79.100000</td>
      <td>6.598589</td>
    </tr>
    <tr>
      <th>7</th>
      <td>135.0</td>
      <td>7.0</td>
      <td>59.115385</td>
      <td>31.635837</td>
      <td>14.9</td>
      <td>4.1</td>
      <td>8.941935</td>
      <td>3.035981</td>
      <td>92</td>
      <td>73</td>
      <td>83.903226</td>
      <td>4.315513</td>
    </tr>
    <tr>
      <th>8</th>
      <td>168.0</td>
      <td>9.0</td>
      <td>59.961538</td>
      <td>39.681210</td>
      <td>15.5</td>
      <td>2.3</td>
      <td>8.793548</td>
      <td>3.225930</td>
      <td>97</td>
      <td>72</td>
      <td>83.967742</td>
      <td>6.585256</td>
    </tr>
    <tr>
      <th>9</th>
      <td>96.0</td>
      <td>7.0</td>
      <td>31.448276</td>
      <td>24.141822</td>
      <td>16.6</td>
      <td>2.8</td>
      <td>10.180000</td>
      <td>3.461254</td>
      <td>93</td>
      <td>63</td>
      <td>76.900000</td>
      <td>8.355671</td>
    </tr>
  </tbody>
</table>
</div>

### (4) 복습문제

[문1] pandas 라이브러리를 pd 별칭을 주어 불러오세요.

```python
# 라이브러리 불러오기
import pandas as pd
```

[문2] read_csv() 함수를 사용해 다음 경로의 파일을 불러와 **titanic** 데이터프레임을 만드세요.

- 파일 경로: 'https://raw.githubusercontent.com/DA4BAM/dataset/master/titanic_simple.csv'

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
path = 'https://raw.githubusercontent.com/DA4BAM/dataset/master/titanic_simple.csv'
titanic = pd.read_csv(path)
titanic
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
      <th>...</th>
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
      <th>886</th>
      <td>887</td>
      <td>0</td>
      <td>2</td>
      <td>Montvila, Rev. Juozas</td>
      <td>male</td>
      <td>27.0</td>
      <td>13.0000</td>
      <td>Southampton</td>
    </tr>
    <tr>
      <th>887</th>
      <td>888</td>
      <td>1</td>
      <td>1</td>
      <td>Graham, Miss. Margaret Edith</td>
      <td>female</td>
      <td>19.0</td>
      <td>30.0000</td>
      <td>Southampton</td>
    </tr>
    <tr>
      <th>888</th>
      <td>889</td>
      <td>0</td>
      <td>3</td>
      <td>Johnston, Miss. Catherine Helen "Carrie"</td>
      <td>female</td>
      <td>NaN</td>
      <td>23.4500</td>
      <td>Southampton</td>
    </tr>
    <tr>
      <th>889</th>
      <td>890</td>
      <td>1</td>
      <td>1</td>
      <td>Behr, Mr. Karl Howell</td>
      <td>male</td>
      <td>26.0</td>
      <td>30.0000</td>
      <td>Cherbourg</td>
    </tr>
    <tr>
      <th>890</th>
      <td>891</td>
      <td>0</td>
      <td>3</td>
      <td>Dooley, Mr. Patrick</td>
      <td>male</td>
      <td>32.0</td>
      <td>7.7500</td>
      <td>Queenstown</td>
    </tr>
  </tbody>
</table>
<p>891 rows × 8 columns</p>
</div>

[문3] Fare의 중앙값을 확인해 봅시다.

```python
titanic.Fare.median()
```

<pre>
14.4542
</pre>

[문4] 승선지역(Embarked)별 평균 운임(Fare)을 구해 봅시다.

```python
titanic.groupby('Embarked', as_index=False)[['Fare']].mean()
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Embarked</th>
      <th>Fare</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Cherbourg</td>
      <td>59.954144</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Queenstown</td>
      <td>13.276030</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Southampton</td>
      <td>27.079812</td>
    </tr>
  </tbody>
</table>
</div>

[문5] 승선지역(Embarked)별, 성별(Sex)별 평균 운임(Fare)과 평균 나이(Age)를 tmp에 저장하고 조회하시오.

```python
tmp = titanic.groupby(['Embarked', 'Sex'], as_index=False)[['Fare', 'Age']].mean()
tmp
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Embarked</th>
      <th>Sex</th>
      <th>Fare</th>
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Cherbourg</td>
      <td>female</td>
      <td>75.169805</td>
      <td>28.344262</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cherbourg</td>
      <td>male</td>
      <td>48.262109</td>
      <td>32.998841</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Queenstown</td>
      <td>female</td>
      <td>12.634958</td>
      <td>24.291667</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Queenstown</td>
      <td>male</td>
      <td>13.838922</td>
      <td>30.937500</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Southampton</td>
      <td>female</td>
      <td>38.740929</td>
      <td>27.771505</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Southampton</td>
      <td>male</td>
      <td>21.711996</td>
      <td>30.291440</td>
    </tr>
  </tbody>
</table>
</div>

[문6] 5번의 결과로 부터 파악할 수 있는 내용은 무엇인가요?

- Cherbourg의 운임료가 비싼 편
- Cherbourg와 Southampton에서는 남녀의 운임 차이가 큼
- Queenstown에서 여성의 나이 평균이 적음

[문7] 객실등급(Pclass)별, 생존여부(Survived)별 나이(Age), 운임(Fare)의 최대, 최소, 평균, 표준편차를 tmp에 저장하고 조회하시오.

```python
tmp = titanic.groupby(['Pclass','Survived'], as_index=False)[['Age','Fare']].agg(['max', 'min', 'mean', 'std'])
tmp
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th colspan="4" halign="left">Age</th>
      <th colspan="4" halign="left">Fare</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th>max</th>
      <th>min</th>
      <th>mean</th>
      <th>std</th>
      <th>max</th>
      <th>min</th>
      <th>mean</th>
      <th>std</th>
    </tr>
    <tr>
      <th>Pclass</th>
      <th>Survived</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">1</th>
      <th>0</th>
      <td>71.0</td>
      <td>2.00</td>
      <td>43.695312</td>
      <td>15.284243</td>
      <td>263.0000</td>
      <td>0.0000</td>
      <td>64.684007</td>
      <td>60.662089</td>
    </tr>
    <tr>
      <th>1</th>
      <td>80.0</td>
      <td>0.92</td>
      <td>35.368197</td>
      <td>13.760017</td>
      <td>512.3292</td>
      <td>25.9292</td>
      <td>95.608029</td>
      <td>85.286820</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">2</th>
      <th>0</th>
      <td>70.0</td>
      <td>16.00</td>
      <td>33.544444</td>
      <td>12.151581</td>
      <td>73.5000</td>
      <td>0.0000</td>
      <td>19.412328</td>
      <td>15.307175</td>
    </tr>
    <tr>
      <th>1</th>
      <td>62.0</td>
      <td>0.67</td>
      <td>25.901566</td>
      <td>14.837787</td>
      <td>65.0000</td>
      <td>10.5000</td>
      <td>22.055700</td>
      <td>10.853502</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">3</th>
      <th>0</th>
      <td>74.0</td>
      <td>1.00</td>
      <td>26.555556</td>
      <td>12.334882</td>
      <td>69.5500</td>
      <td>0.0000</td>
      <td>13.669364</td>
      <td>12.118338</td>
    </tr>
    <tr>
      <th>1</th>
      <td>63.0</td>
      <td>0.42</td>
      <td>20.646118</td>
      <td>11.995047</td>
      <td>56.4958</td>
      <td>0.0000</td>
      <td>13.694887</td>
      <td>10.692993</td>
    </tr>
  </tbody>
</table>
</div>

## 요약: pandas

- pandas는 우리에게 익숙한 표 형태로 데이터를 다루게 해줌
    - 엑셀의 표, 데이터베이스의 테이블
- 2차원 구조: 데이터프레임, 1차원 구조: 시리즈
    - 보통 데이터프레임의 열 하나를 떼어내서 시리즈로 다룸
- 데이터프레임 조회
    - `.loc[조건문, 열이름]`
- 집계: groupby
    - `df.groupby('집계기준변수', as_index=)['집계대상변수'].집계함수`
    - `df.groupby('집계기준변수', as_index=)['집계대상변수'].agg( )`
- https://wikidocs.net/book/4639
