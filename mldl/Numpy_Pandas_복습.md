## numpy

---

### numpy Broadcasting, Aggregation

- Broadcasting 연산 (Scalar)

    - 다차원 넘파이 배열과 하나의 숫자를 사칙연산 하는 경우, 넘파이 배열의 모든 원소에 해당 숫자 사칙 연산이 **확장** 되어 적용됨

- Aggregation

    - 넘파이 배열에 모든 원소를 집계하는 연산
    - axis 인자를 주어, 특정 축으로 집계할 수 있다

```python
import numpy as np
```

```python
arr = np.array([[1,2,3,4],[10,11,12,13]])
arr
```

<pre>
array([[ 1,  2,  3,  4],
       [10, 11, 12, 13]])
</pre>

```python
arr + arr    # 배열끼리 연산하기 (＋－*/ 모두 가능)
```

<pre>
array([[ 2,  4,  6,  8],
       [20, 22, 24, 26]])
</pre>

```python
arr + 20     # 덧셈 브로드캐스팅
```

<pre>
array([[21, 22, 23, 24],
       [30, 31, 32, 33]])
</pre>

```python
arr * 100    # 곱셈 브로드캐스팅
```

<pre>
array([[ 100,  200,  300,  400],
       [1000, 1100, 1200, 1300]])
</pre>

```python
# 배열 전체의 덧셈, 평균, 곱셈, 최댓값, 최솟값
arr.sum(), arr.mean(), arr.prod(), arr.max(), arr.min()
```

<pre>
(56, 7.0, 411840, 13, 1)
</pre>

```python
# 배열에서의 최대인 원소의 번호, 최소인 원소의 번호
arr.argmax(), arr[1].argmax(), arr.argmin()
```

<pre>
(7, 3, 0)
</pre>

```python
# 특정 축(차원)으로 덧셈 수행하기
arr.sum(axis=0), arr.sum(axis=1)
```

<pre>
(array([11, 13, 15, 17]), array([10, 46]))
</pre>

```python
# Indexing + Slicing + Aggregation 응용
arr[1].min(), arr[1][2:].sum()
```

<pre>
(10, 25)
</pre>

### 고급 Broadcasting

![np_broadcasting](https://github.com/zacinthepark/TIL/assets/86648892/49bbd4b2-5719-423e-ab88-1e70250d4b34)

```python
arr1 = np.array([[0,0,0],[10,10,10],[20,20,20],[30,30,30]])
arr2 = np.array([[0,1,2],[0,1,2],[0,1,2],[0,1,2]])
arr1.shape, arr2.shape
```

<pre>
((4, 3), (4, 3))
</pre>

```python
arr1 + arr2          # (4x3)  +  (4x3)
```

<pre>
array([[ 0,  1,  2],
       [10, 11, 12],
       [20, 21, 22],
       [30, 31, 32]])
</pre>

```python
arr1 + np.array([0,1,2])     # (4x3) + (1x3)
```

<pre>
array([[ 0,  1,  2],
       [10, 11, 12],
       [20, 21, 22],
       [30, 31, 32]])
</pre>

```python
#  (4x1) + (1x3)
np.array([[0],[10],[20],[30]]) + np.array([0,1,2])
```

<pre>
array([[ 0,  1,  2],
       [10, 11, 12],
       [20, 21, 22],
       [30, 31, 32]])
</pre>

```python
np.array([0,1,2])
```

<pre>
array([0, 1, 2])
</pre>

## DataFrame 연산 총 정리

---

- 단일 연산

    - `.abs()` : 절댓값
    - `.isna()` : na 여부
    - `.notna()` : 유효 여부
    - `.pow()` : 거듭제곱

- 축 방향 연산(axis=0 or 1)

    - `.mean()` : 평균
    - `.median()` : 중앙값
    - `.max()` : 최댓값
    - `.min()` : 최솟값
    - `.sum()` : 더하기
    - `.prod()` : 곱하기
    - `.idxmax()` : 최대원소의 인덱스
    - `.idxmin()` : 최소원소의 인덱스

- 누적 축 방향 연산(axis=0 or 1)

    - `.cummax()` : 누적최댓값
    - `.cummin()` : 누적최솟값
    - `.cumprod()` : 누적곱셈
    - `.cumsum()` : 누적덧셈

- 정렬

    - `df.sort_values(정렬기준, axis=축, ascending=True)`

    - `df.rank(axis=축, ascending=True)`
        - 축의 방향으로 정렬
        - 각각의 행 또는 열들의 순위를 매김
        - 축과 오름차순 여부 지정 가능

## concat, groupby, query

---

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

plt.rcParams['font.family'] = 'Malgun Gothic'  # (Windows 용) 한글 출력을 위한 글꼴 설정
#plt.rcParams['font.family'] = 'AppleGothic'  # (MAC, 리눅스 용)

plt.rcParams['axes.unicode_minus'] = False    # 문자 - (마이너스) 정상 출력을 위한 코드
```

##### stock.adj_close.csv - https://drive.google.com/file/d/1AnWjtW9bdIqBEnxeOMfST_Pxx2IVQfMJ/view?usp=sharing
##### stockinfo.itemname.csv - https://drive.google.com/file/d/18pCREyPq41nK1VGSPZx5_RcL3D-sX4tB/view?usp=sharing
##### stockinfo.sector.csv - https://drive.google.com/file/d/1HN85HsUqDCPKL0ulfwDzDAK6mf5cRrQ_/view?usp=sharing

```python
# dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d')
adj_close = pd.read_csv("./stock.adj_close.csv", index_col=0, encoding='cp949')
adj_close.head()
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>2018-06-01</th>
      <th>2018-06-04</th>
      <th>2018-06-05</th>
      <th>2018-06-07</th>
      <th>2018-06-08</th>
      <th>2018-06-11</th>
      <th>2018-06-12</th>
      <th>2018-06-14</th>
      <th>2018-06-15</th>
      <th>2018-06-18</th>
      <th>...</th>
      <th>2020-09-25</th>
      <th>2020-09-28</th>
      <th>2020-09-29</th>
      <th>2020-10-05</th>
      <th>2020-10-06</th>
      <th>2020-10-07</th>
      <th>2020-10-08</th>
      <th>2020-10-12</th>
      <th>2020-10-13</th>
      <th>2020-10-14</th>
    </tr>
    <tr>
      <th>Symbol</th>
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
      <th>A000020</th>
      <td>11550.0</td>
      <td>11750.0</td>
      <td>11700.0</td>
      <td>11650.0</td>
      <td>11500.0</td>
      <td>11500.0</td>
      <td>11650.0</td>
      <td>12000.0</td>
      <td>11800.0</td>
      <td>11450.0</td>
      <td>...</td>
      <td>22100.0</td>
      <td>22000.0</td>
      <td>21850.0</td>
      <td>24100.0</td>
      <td>23750.0</td>
      <td>23500.0</td>
      <td>24150.0</td>
      <td>24000.0</td>
      <td>24300.0</td>
      <td>23850.0</td>
    </tr>
    <tr>
      <th>A000030</th>
      <td>15500.0</td>
      <td>15950.0</td>
      <td>16050.0</td>
      <td>16500.0</td>
      <td>16600.0</td>
      <td>16650.0</td>
      <td>16850.0</td>
      <td>16500.0</td>
      <td>16100.0</td>
      <td>16350.0</td>
      <td>...</td>
      <td>14800.0</td>
      <td>14800.0</td>
      <td>14800.0</td>
      <td>14800.0</td>
      <td>14800.0</td>
      <td>14800.0</td>
      <td>14800.0</td>
      <td>14800.0</td>
      <td>14800.0</td>
      <td>14800.0</td>
    </tr>
    <tr>
      <th>A000040</th>
      <td>2992.0</td>
      <td>3021.0</td>
      <td>3025.0</td>
      <td>3069.0</td>
      <td>3045.0</td>
      <td>2984.0</td>
      <td>2976.0</td>
      <td>3033.0</td>
      <td>3033.0</td>
      <td>3017.0</td>
      <td>...</td>
      <td>771.0</td>
      <td>743.0</td>
      <td>767.0</td>
      <td>829.0</td>
      <td>810.0</td>
      <td>860.0</td>
      <td>863.0</td>
      <td>863.0</td>
      <td>850.0</td>
      <td>874.0</td>
    </tr>
    <tr>
      <th>A000050</th>
      <td>13200.0</td>
      <td>13550.0</td>
      <td>13600.0</td>
      <td>13800.0</td>
      <td>13800.0</td>
      <td>13800.0</td>
      <td>13650.0</td>
      <td>13850.0</td>
      <td>14500.0</td>
      <td>14550.0</td>
      <td>...</td>
      <td>10750.0</td>
      <td>10500.0</td>
      <td>10550.0</td>
      <td>10850.0</td>
      <td>10900.0</td>
      <td>10900.0</td>
      <td>11000.0</td>
      <td>11000.0</td>
      <td>10850.0</td>
      <td>10800.0</td>
    </tr>
    <tr>
      <th>A000060</th>
      <td>20050.0</td>
      <td>20050.0</td>
      <td>20150.0</td>
      <td>20050.0</td>
      <td>20400.0</td>
      <td>20150.0</td>
      <td>20700.0</td>
      <td>20950.0</td>
      <td>20150.0</td>
      <td>20900.0</td>
      <td>...</td>
      <td>12750.0</td>
      <td>12750.0</td>
      <td>12850.0</td>
      <td>13150.0</td>
      <td>13300.0</td>
      <td>13350.0</td>
      <td>13900.0</td>
      <td>13950.0</td>
      <td>13700.0</td>
      <td>13550.0</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 582 columns</p>
</div>

```python
itemname = pd.read_csv("stockinfo.itemname.csv", index_col=0, encoding='cp949')
sector = pd.read_csv("stockinfo.sector.csv", index_col=0, encoding='cp949')

stock_info = pd.concat([itemname, sector], axis=1)
stock_info.head()
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>itemname</th>
      <th>Sector</th>
    </tr>
    <tr>
      <th>Symbol</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A000020</th>
      <td>동화약품</td>
      <td>제약_및_바이오</td>
    </tr>
    <tr>
      <th>A000030</th>
      <td>우리은행</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>A000040</th>
      <td>KR모터스</td>
      <td>자동차_및_부품</td>
    </tr>
    <tr>
      <th>A000050</th>
      <td>경방</td>
      <td>내구_소비재_및_의류</td>
    </tr>
    <tr>
      <th>A000060</th>
      <td>메리츠화재</td>
      <td>보험</td>
    </tr>
  </tbody>
</table>
</div>

```python
# 데이터 준비
df_a = stock_info.iloc[:14]
df_a
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>itemname</th>
      <th>Sector</th>
    </tr>
    <tr>
      <th>Symbol</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A000020</th>
      <td>동화약품</td>
      <td>제약_및_바이오</td>
    </tr>
    <tr>
      <th>A000030</th>
      <td>우리은행</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>A000040</th>
      <td>KR모터스</td>
      <td>자동차_및_부품</td>
    </tr>
    <tr>
      <th>A000050</th>
      <td>경방</td>
      <td>내구_소비재_및_의류</td>
    </tr>
    <tr>
      <th>A000060</th>
      <td>메리츠화재</td>
      <td>보험</td>
    </tr>
    <tr>
      <th>A000070</th>
      <td>삼양홀딩스</td>
      <td>소재</td>
    </tr>
    <tr>
      <th>A000080</th>
      <td>하이트진로</td>
      <td>음식료_및_담배</td>
    </tr>
    <tr>
      <th>A000100</th>
      <td>유한양행</td>
      <td>제약_및_바이오</td>
    </tr>
    <tr>
      <th>A000120</th>
      <td>CJ대한통운</td>
      <td>운송</td>
    </tr>
    <tr>
      <th>A000140</th>
      <td>하이트진로홀딩스</td>
      <td>음식료_및_담배</td>
    </tr>
    <tr>
      <th>A000150</th>
      <td>두산</td>
      <td>자본재</td>
    </tr>
    <tr>
      <th>A000180</th>
      <td>성창기업지주</td>
      <td>소재</td>
    </tr>
    <tr>
      <th>A000210</th>
      <td>대림산업</td>
      <td>자본재</td>
    </tr>
    <tr>
      <th>A000220</th>
      <td>유유제약</td>
      <td>제약_및_바이오</td>
    </tr>
  </tbody>
</table>
</div>

```python
df_b = adj_close.loc[:,'2020-10-13':].iloc[:14]
df_b
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>2020-10-13</th>
      <th>2020-10-14</th>
    </tr>
    <tr>
      <th>Symbol</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A000020</th>
      <td>24300.0</td>
      <td>23850.0</td>
    </tr>
    <tr>
      <th>A000030</th>
      <td>14800.0</td>
      <td>14800.0</td>
    </tr>
    <tr>
      <th>A000040</th>
      <td>850.0</td>
      <td>874.0</td>
    </tr>
    <tr>
      <th>A000050</th>
      <td>10850.0</td>
      <td>10800.0</td>
    </tr>
    <tr>
      <th>A000060</th>
      <td>13700.0</td>
      <td>13550.0</td>
    </tr>
    <tr>
      <th>A000070</th>
      <td>63000.0</td>
      <td>61800.0</td>
    </tr>
    <tr>
      <th>A000080</th>
      <td>38700.0</td>
      <td>38500.0</td>
    </tr>
    <tr>
      <th>A000100</th>
      <td>64100.0</td>
      <td>63600.0</td>
    </tr>
    <tr>
      <th>A000120</th>
      <td>186500.0</td>
      <td>180500.0</td>
    </tr>
    <tr>
      <th>A000140</th>
      <td>17300.0</td>
      <td>17250.0</td>
    </tr>
    <tr>
      <th>A000150</th>
      <td>47500.0</td>
      <td>47700.0</td>
    </tr>
    <tr>
      <th>A000180</th>
      <td>1715.0</td>
      <td>1825.0</td>
    </tr>
    <tr>
      <th>A000210</th>
      <td>78300.0</td>
      <td>76600.0</td>
    </tr>
    <tr>
      <th>A000220</th>
      <td>16600.0</td>
      <td>16250.0</td>
    </tr>
  </tbody>
</table>
</div>

```python
# .rename 함수를 이용, 딕셔너리로 컬럼 명을 바꿀 수 있습니다
df_b = df_b.rename(columns={
    '2020-10-13':'주가_10_13',
    '2020-10-14':'주가_10_14'
})
df_b
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>주가_10_13</th>
      <th>주가_10_14</th>
    </tr>
    <tr>
      <th>Symbol</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A000020</th>
      <td>24300.0</td>
      <td>23850.0</td>
    </tr>
    <tr>
      <th>A000030</th>
      <td>14800.0</td>
      <td>14800.0</td>
    </tr>
    <tr>
      <th>A000040</th>
      <td>850.0</td>
      <td>874.0</td>
    </tr>
    <tr>
      <th>A000050</th>
      <td>10850.0</td>
      <td>10800.0</td>
    </tr>
    <tr>
      <th>A000060</th>
      <td>13700.0</td>
      <td>13550.0</td>
    </tr>
    <tr>
      <th>A000070</th>
      <td>63000.0</td>
      <td>61800.0</td>
    </tr>
    <tr>
      <th>A000080</th>
      <td>38700.0</td>
      <td>38500.0</td>
    </tr>
    <tr>
      <th>A000100</th>
      <td>64100.0</td>
      <td>63600.0</td>
    </tr>
    <tr>
      <th>A000120</th>
      <td>186500.0</td>
      <td>180500.0</td>
    </tr>
    <tr>
      <th>A000140</th>
      <td>17300.0</td>
      <td>17250.0</td>
    </tr>
    <tr>
      <th>A000150</th>
      <td>47500.0</td>
      <td>47700.0</td>
    </tr>
    <tr>
      <th>A000180</th>
      <td>1715.0</td>
      <td>1825.0</td>
    </tr>
    <tr>
      <th>A000210</th>
      <td>78300.0</td>
      <td>76600.0</td>
    </tr>
    <tr>
      <th>A000220</th>
      <td>16600.0</td>
      <td>16250.0</td>
    </tr>
  </tbody>
</table>
</div>

### `.concat()` - 여러 개의 DataFrame 합치기

```python
pd.concat([df_a, df_b])
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>itemname</th>
      <th>Sector</th>
      <th>주가_10_13</th>
      <th>주가_10_14</th>
    </tr>
    <tr>
      <th>Symbol</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A000020</th>
      <td>동화약품</td>
      <td>제약_및_바이오</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>A000030</th>
      <td>우리은행</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>A000040</th>
      <td>KR모터스</td>
      <td>자동차_및_부품</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>A000050</th>
      <td>경방</td>
      <td>내구_소비재_및_의류</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>A000060</th>
      <td>메리츠화재</td>
      <td>보험</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>A000070</th>
      <td>삼양홀딩스</td>
      <td>소재</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>A000080</th>
      <td>하이트진로</td>
      <td>음식료_및_담배</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>A000100</th>
      <td>유한양행</td>
      <td>제약_및_바이오</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>A000120</th>
      <td>CJ대한통운</td>
      <td>운송</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>A000140</th>
      <td>하이트진로홀딩스</td>
      <td>음식료_및_담배</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>A000150</th>
      <td>두산</td>
      <td>자본재</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>A000180</th>
      <td>성창기업지주</td>
      <td>소재</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>A000210</th>
      <td>대림산업</td>
      <td>자본재</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>A000220</th>
      <td>유유제약</td>
      <td>제약_및_바이오</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>A000020</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>24300.0</td>
      <td>23850.0</td>
    </tr>
    <tr>
      <th>A000030</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>14800.0</td>
      <td>14800.0</td>
    </tr>
    <tr>
      <th>A000040</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>850.0</td>
      <td>874.0</td>
    </tr>
    <tr>
      <th>A000050</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>10850.0</td>
      <td>10800.0</td>
    </tr>
    <tr>
      <th>A000060</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>13700.0</td>
      <td>13550.0</td>
    </tr>
    <tr>
      <th>A000070</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>63000.0</td>
      <td>61800.0</td>
    </tr>
    <tr>
      <th>A000080</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>38700.0</td>
      <td>38500.0</td>
    </tr>
    <tr>
      <th>A000100</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>64100.0</td>
      <td>63600.0</td>
    </tr>
    <tr>
      <th>A000120</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>186500.0</td>
      <td>180500.0</td>
    </tr>
    <tr>
      <th>A000140</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>17300.0</td>
      <td>17250.0</td>
    </tr>
    <tr>
      <th>A000150</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>47500.0</td>
      <td>47700.0</td>
    </tr>
    <tr>
      <th>A000180</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>1715.0</td>
      <td>1825.0</td>
    </tr>
    <tr>
      <th>A000210</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>78300.0</td>
      <td>76600.0</td>
    </tr>
    <tr>
      <th>A000220</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>16600.0</td>
      <td>16250.0</td>
    </tr>
  </tbody>
</table>
</div>

```python
my_concat_df = pd.concat([df_a, df_b], axis=1)
my_concat_df
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>itemname</th>
      <th>Sector</th>
      <th>주가_10_13</th>
      <th>주가_10_14</th>
    </tr>
    <tr>
      <th>Symbol</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A000020</th>
      <td>동화약품</td>
      <td>제약_및_바이오</td>
      <td>24300.0</td>
      <td>23850.0</td>
    </tr>
    <tr>
      <th>A000030</th>
      <td>우리은행</td>
      <td>NaN</td>
      <td>14800.0</td>
      <td>14800.0</td>
    </tr>
    <tr>
      <th>A000040</th>
      <td>KR모터스</td>
      <td>자동차_및_부품</td>
      <td>850.0</td>
      <td>874.0</td>
    </tr>
    <tr>
      <th>A000050</th>
      <td>경방</td>
      <td>내구_소비재_및_의류</td>
      <td>10850.0</td>
      <td>10800.0</td>
    </tr>
    <tr>
      <th>A000060</th>
      <td>메리츠화재</td>
      <td>보험</td>
      <td>13700.0</td>
      <td>13550.0</td>
    </tr>
    <tr>
      <th>A000070</th>
      <td>삼양홀딩스</td>
      <td>소재</td>
      <td>63000.0</td>
      <td>61800.0</td>
    </tr>
    <tr>
      <th>A000080</th>
      <td>하이트진로</td>
      <td>음식료_및_담배</td>
      <td>38700.0</td>
      <td>38500.0</td>
    </tr>
    <tr>
      <th>A000100</th>
      <td>유한양행</td>
      <td>제약_및_바이오</td>
      <td>64100.0</td>
      <td>63600.0</td>
    </tr>
    <tr>
      <th>A000120</th>
      <td>CJ대한통운</td>
      <td>운송</td>
      <td>186500.0</td>
      <td>180500.0</td>
    </tr>
    <tr>
      <th>A000140</th>
      <td>하이트진로홀딩스</td>
      <td>음식료_및_담배</td>
      <td>17300.0</td>
      <td>17250.0</td>
    </tr>
    <tr>
      <th>A000150</th>
      <td>두산</td>
      <td>자본재</td>
      <td>47500.0</td>
      <td>47700.0</td>
    </tr>
    <tr>
      <th>A000180</th>
      <td>성창기업지주</td>
      <td>소재</td>
      <td>1715.0</td>
      <td>1825.0</td>
    </tr>
    <tr>
      <th>A000210</th>
      <td>대림산업</td>
      <td>자본재</td>
      <td>78300.0</td>
      <td>76600.0</td>
    </tr>
    <tr>
      <th>A000220</th>
      <td>유유제약</td>
      <td>제약_및_바이오</td>
      <td>16600.0</td>
      <td>16250.0</td>
    </tr>
  </tbody>
</table>
</div>

### `.groupby()` – 그룹으로 묶어서 Aggregation 하기

```python
my_concat_df
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>itemname</th>
      <th>Sector</th>
      <th>주가_10_13</th>
      <th>주가_10_14</th>
    </tr>
    <tr>
      <th>Symbol</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A000020</th>
      <td>동화약품</td>
      <td>제약_및_바이오</td>
      <td>24300.0</td>
      <td>23850.0</td>
    </tr>
    <tr>
      <th>A000030</th>
      <td>우리은행</td>
      <td>NaN</td>
      <td>14800.0</td>
      <td>14800.0</td>
    </tr>
    <tr>
      <th>A000040</th>
      <td>KR모터스</td>
      <td>자동차_및_부품</td>
      <td>850.0</td>
      <td>874.0</td>
    </tr>
    <tr>
      <th>A000050</th>
      <td>경방</td>
      <td>내구_소비재_및_의류</td>
      <td>10850.0</td>
      <td>10800.0</td>
    </tr>
    <tr>
      <th>A000060</th>
      <td>메리츠화재</td>
      <td>보험</td>
      <td>13700.0</td>
      <td>13550.0</td>
    </tr>
    <tr>
      <th>A000070</th>
      <td>삼양홀딩스</td>
      <td>소재</td>
      <td>63000.0</td>
      <td>61800.0</td>
    </tr>
    <tr>
      <th>A000080</th>
      <td>하이트진로</td>
      <td>음식료_및_담배</td>
      <td>38700.0</td>
      <td>38500.0</td>
    </tr>
    <tr>
      <th>A000100</th>
      <td>유한양행</td>
      <td>제약_및_바이오</td>
      <td>64100.0</td>
      <td>63600.0</td>
    </tr>
    <tr>
      <th>A000120</th>
      <td>CJ대한통운</td>
      <td>운송</td>
      <td>186500.0</td>
      <td>180500.0</td>
    </tr>
    <tr>
      <th>A000140</th>
      <td>하이트진로홀딩스</td>
      <td>음식료_및_담배</td>
      <td>17300.0</td>
      <td>17250.0</td>
    </tr>
    <tr>
      <th>A000150</th>
      <td>두산</td>
      <td>자본재</td>
      <td>47500.0</td>
      <td>47700.0</td>
    </tr>
    <tr>
      <th>A000180</th>
      <td>성창기업지주</td>
      <td>소재</td>
      <td>1715.0</td>
      <td>1825.0</td>
    </tr>
    <tr>
      <th>A000210</th>
      <td>대림산업</td>
      <td>자본재</td>
      <td>78300.0</td>
      <td>76600.0</td>
    </tr>
    <tr>
      <th>A000220</th>
      <td>유유제약</td>
      <td>제약_및_바이오</td>
      <td>16600.0</td>
      <td>16250.0</td>
    </tr>
  </tbody>
</table>
</div>

```python
my_concat_df.groupby('Sector')[['주가_10_13', '주가_10_14']].sum()
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>주가_10_13</th>
      <th>주가_10_14</th>
    </tr>
    <tr>
      <th>Sector</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>내구_소비재_및_의류</th>
      <td>10850.0</td>
      <td>10800.0</td>
    </tr>
    <tr>
      <th>보험</th>
      <td>13700.0</td>
      <td>13550.0</td>
    </tr>
    <tr>
      <th>소재</th>
      <td>64715.0</td>
      <td>63625.0</td>
    </tr>
    <tr>
      <th>운송</th>
      <td>186500.0</td>
      <td>180500.0</td>
    </tr>
    <tr>
      <th>음식료_및_담배</th>
      <td>56000.0</td>
      <td>55750.0</td>
    </tr>
    <tr>
      <th>자동차_및_부품</th>
      <td>850.0</td>
      <td>874.0</td>
    </tr>
    <tr>
      <th>자본재</th>
      <td>125800.0</td>
      <td>124300.0</td>
    </tr>
    <tr>
      <th>제약_및_바이오</th>
      <td>105000.0</td>
      <td>103700.0</td>
    </tr>
  </tbody>
</table>
</div>

```python
my_concat_df.groupby('Sector')[['주가_10_13', '주가_10_14']].mean()
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>주가_10_13</th>
      <th>주가_10_14</th>
    </tr>
    <tr>
      <th>Sector</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>내구_소비재_및_의류</th>
      <td>10850.0</td>
      <td>10800.000000</td>
    </tr>
    <tr>
      <th>보험</th>
      <td>13700.0</td>
      <td>13550.000000</td>
    </tr>
    <tr>
      <th>소재</th>
      <td>32357.5</td>
      <td>31812.500000</td>
    </tr>
    <tr>
      <th>운송</th>
      <td>186500.0</td>
      <td>180500.000000</td>
    </tr>
    <tr>
      <th>음식료_및_담배</th>
      <td>28000.0</td>
      <td>27875.000000</td>
    </tr>
    <tr>
      <th>자동차_및_부품</th>
      <td>850.0</td>
      <td>874.000000</td>
    </tr>
    <tr>
      <th>자본재</th>
      <td>62900.0</td>
      <td>62150.000000</td>
    </tr>
    <tr>
      <th>제약_및_바이오</th>
      <td>35000.0</td>
      <td>34566.666667</td>
    </tr>
  </tbody>
</table>
</div>

```python
my_concat_df.groupby('Sector')[['주가_10_13', '주가_10_14']].count()
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>주가_10_13</th>
      <th>주가_10_14</th>
    </tr>
    <tr>
      <th>Sector</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>내구_소비재_및_의류</th>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>보험</th>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>소재</th>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>운송</th>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>음식료_및_담배</th>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>자동차_및_부품</th>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>자본재</th>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>제약_및_바이오</th>
      <td>3</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>

```python
my_concat_df.groupby('Sector')[['주가_10_13', '주가_10_14']].max()
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>주가_10_13</th>
      <th>주가_10_14</th>
    </tr>
    <tr>
      <th>Sector</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>내구_소비재_및_의류</th>
      <td>10850.0</td>
      <td>10800.0</td>
    </tr>
    <tr>
      <th>보험</th>
      <td>13700.0</td>
      <td>13550.0</td>
    </tr>
    <tr>
      <th>소재</th>
      <td>63000.0</td>
      <td>61800.0</td>
    </tr>
    <tr>
      <th>운송</th>
      <td>186500.0</td>
      <td>180500.0</td>
    </tr>
    <tr>
      <th>음식료_및_담배</th>
      <td>38700.0</td>
      <td>38500.0</td>
    </tr>
    <tr>
      <th>자동차_및_부품</th>
      <td>850.0</td>
      <td>874.0</td>
    </tr>
    <tr>
      <th>자본재</th>
      <td>78300.0</td>
      <td>76600.0</td>
    </tr>
    <tr>
      <th>제약_및_바이오</th>
      <td>64100.0</td>
      <td>63600.0</td>
    </tr>
  </tbody>
</table>
</div>

### `.query()` - DataFrame 필터링하기

- `query(작성한_쿼리문)`

    - dataframe의 컬럼을 대상, **작성한 쿼리문으로 dataframe을 필터링하여 추출**
    - 컬럼은 큰 따옴표 없이 작성하며, 값을 작성할 경우 숫자는 그대로 작성, 문자열은 `""` 큰 따옴표로 묶어줌
    - 쿼리문은 `and`, `or` 등으로 여러 개 중첩할 수 있음

```python
my_concat_df
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>itemname</th>
      <th>Sector</th>
      <th>주가_10_13</th>
      <th>주가_10_14</th>
    </tr>
    <tr>
      <th>Symbol</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A000020</th>
      <td>동화약품</td>
      <td>제약_및_바이오</td>
      <td>24300.0</td>
      <td>23850.0</td>
    </tr>
    <tr>
      <th>A000030</th>
      <td>우리은행</td>
      <td>NaN</td>
      <td>14800.0</td>
      <td>14800.0</td>
    </tr>
    <tr>
      <th>A000040</th>
      <td>KR모터스</td>
      <td>자동차_및_부품</td>
      <td>850.0</td>
      <td>874.0</td>
    </tr>
    <tr>
      <th>A000050</th>
      <td>경방</td>
      <td>내구_소비재_및_의류</td>
      <td>10850.0</td>
      <td>10800.0</td>
    </tr>
    <tr>
      <th>A000060</th>
      <td>메리츠화재</td>
      <td>보험</td>
      <td>13700.0</td>
      <td>13550.0</td>
    </tr>
    <tr>
      <th>A000070</th>
      <td>삼양홀딩스</td>
      <td>소재</td>
      <td>63000.0</td>
      <td>61800.0</td>
    </tr>
    <tr>
      <th>A000080</th>
      <td>하이트진로</td>
      <td>음식료_및_담배</td>
      <td>38700.0</td>
      <td>38500.0</td>
    </tr>
    <tr>
      <th>A000100</th>
      <td>유한양행</td>
      <td>제약_및_바이오</td>
      <td>64100.0</td>
      <td>63600.0</td>
    </tr>
    <tr>
      <th>A000120</th>
      <td>CJ대한통운</td>
      <td>운송</td>
      <td>186500.0</td>
      <td>180500.0</td>
    </tr>
    <tr>
      <th>A000140</th>
      <td>하이트진로홀딩스</td>
      <td>음식료_및_담배</td>
      <td>17300.0</td>
      <td>17250.0</td>
    </tr>
    <tr>
      <th>A000150</th>
      <td>두산</td>
      <td>자본재</td>
      <td>47500.0</td>
      <td>47700.0</td>
    </tr>
    <tr>
      <th>A000180</th>
      <td>성창기업지주</td>
      <td>소재</td>
      <td>1715.0</td>
      <td>1825.0</td>
    </tr>
    <tr>
      <th>A000210</th>
      <td>대림산업</td>
      <td>자본재</td>
      <td>78300.0</td>
      <td>76600.0</td>
    </tr>
    <tr>
      <th>A000220</th>
      <td>유유제약</td>
      <td>제약_및_바이오</td>
      <td>16600.0</td>
      <td>16250.0</td>
    </tr>
  </tbody>
</table>
</div>

```python
my_concat_df.query('Sector == "운송"')
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>itemname</th>
      <th>Sector</th>
      <th>주가_10_13</th>
      <th>주가_10_14</th>
    </tr>
    <tr>
      <th>Symbol</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A000120</th>
      <td>CJ대한통운</td>
      <td>운송</td>
      <td>186500.0</td>
      <td>180500.0</td>
    </tr>
  </tbody>
</table>
</div>

```python
my_concat_df.query('Sector == "제약_및_바이오"')
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>itemname</th>
      <th>Sector</th>
      <th>주가_10_13</th>
      <th>주가_10_14</th>
    </tr>
    <tr>
      <th>Symbol</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A000020</th>
      <td>동화약품</td>
      <td>제약_및_바이오</td>
      <td>24300.0</td>
      <td>23850.0</td>
    </tr>
    <tr>
      <th>A000100</th>
      <td>유한양행</td>
      <td>제약_및_바이오</td>
      <td>64100.0</td>
      <td>63600.0</td>
    </tr>
    <tr>
      <th>A000220</th>
      <td>유유제약</td>
      <td>제약_및_바이오</td>
      <td>16600.0</td>
      <td>16250.0</td>
    </tr>
  </tbody>
</table>
</div>

```python
my_concat_df.query('주가_10_13 > 20000')
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>itemname</th>
      <th>Sector</th>
      <th>주가_10_13</th>
      <th>주가_10_14</th>
    </tr>
    <tr>
      <th>Symbol</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A000020</th>
      <td>동화약품</td>
      <td>제약_및_바이오</td>
      <td>24300.0</td>
      <td>23850.0</td>
    </tr>
    <tr>
      <th>A000070</th>
      <td>삼양홀딩스</td>
      <td>소재</td>
      <td>63000.0</td>
      <td>61800.0</td>
    </tr>
    <tr>
      <th>A000080</th>
      <td>하이트진로</td>
      <td>음식료_및_담배</td>
      <td>38700.0</td>
      <td>38500.0</td>
    </tr>
    <tr>
      <th>A000100</th>
      <td>유한양행</td>
      <td>제약_및_바이오</td>
      <td>64100.0</td>
      <td>63600.0</td>
    </tr>
    <tr>
      <th>A000120</th>
      <td>CJ대한통운</td>
      <td>운송</td>
      <td>186500.0</td>
      <td>180500.0</td>
    </tr>
    <tr>
      <th>A000150</th>
      <td>두산</td>
      <td>자본재</td>
      <td>47500.0</td>
      <td>47700.0</td>
    </tr>
    <tr>
      <th>A000210</th>
      <td>대림산업</td>
      <td>자본재</td>
      <td>78300.0</td>
      <td>76600.0</td>
    </tr>
  </tbody>
</table>
</div>

```python
my_concat_df.query('주가_10_13 > 20000  and  Sector == "제약_및_바이오"')
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>itemname</th>
      <th>Sector</th>
      <th>주가_10_13</th>
      <th>주가_10_14</th>
    </tr>
    <tr>
      <th>Symbol</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A000020</th>
      <td>동화약품</td>
      <td>제약_및_바이오</td>
      <td>24300.0</td>
      <td>23850.0</td>
    </tr>
    <tr>
      <th>A000100</th>
      <td>유한양행</td>
      <td>제약_및_바이오</td>
      <td>64100.0</td>
      <td>63600.0</td>
    </tr>
  </tbody>
</table>
</div>
