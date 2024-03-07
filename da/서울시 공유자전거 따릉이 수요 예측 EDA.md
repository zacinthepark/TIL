# 서울시 공유자전거 '따릉이' 수요 예측 프로젝트

## 단계2. 탐색적 데이터 분석

#### <font color="blue"> 데이터 분석의 주 목적은 가치있는 정보를 찾아내는것!! </font>

 - 기상상황이 따릉이 수요에 주는 영향을 분석해봅시다.

    * 1.데이터를 탐색하며 정보 획득

        * 날씨 데이터와 서울시 공유 자전거 따릉이의 수요 데이터를 제공해드렸습니다. 
        * 우리는 따릉이의 수요와 날씨간 어떤 연관성이 있는지 탐색 해 봅시다.

    * 2.EDA

        * 주어진 데이터의 변수들을 분석해 봅시다. 

### (2) 데이터 소개

#### 1) 기본 데이터

  * 학습데이터 : sbikedata.csv

#### 2) 데이터셋의 변수 소개

  * date : 날짜
  * hour : 시간
  * temperature : 온도
  * precipitation : 강우 여부, 비가 오지 않았으면 0, 비가 오면 1
  * windspeed : 풍속(평균)
  * humidity : 습도
  * visibility : 시정(視程), 시계(視界)(특정 기상 상태에 따른 가시성을 의미)
  * ozone : 오존 수치
  * PM10 : 미세먼지 수치(머리카락 굵기의 1/5에서 1/7 크기의 미세먼지)
  * PM2.5 : 초미세먼지 수치(머리카락 굵기의 1/20에서 1/30 크기의 미세먼지)
  * count : 시간에 따른 따릉이 대여 수


## 1. 준비

#### 1) 로컬 수행(Anaconda)

* project 폴더에 필요한 파일들을 넣고, 본 파일을 열었다면, 별도 경로 지정이 필요하지 않습니다.

```python
# path = 'C:/Users/User/'
```

#### 2) 라이브러리 로딩

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from statsmodels.graphics.mosaicplot import mosaic
from scipy import stats as spst
import statsmodels.api as sm
import joblib
```

### (2) 데이터 불러오기

* 주어진 데이터셋

    * 따릉이 수요 및 날씨 데이터 : sbikedata.csv

#### 1) 데이터로딩

```python
# 아래에 실습코드를 작성하고 결과를 확인합니다.

df = pd.read_csv('sbikedata.csv')
```

#### 2) 기본 정보 조회

```python
# 아래에 실습코드를 작성하고 결과를 확인합니다.
#전체 데이터의 행,열 개수 확인

df.shape
```

<pre>
(5827, 11)
</pre>

```python
# 아래에 실습코드를 작성하고 결과를 확인합니다.
#전체 데이터의 모든 변수 확인

df.columns
```

<pre>
Index(['date', 'hour', 'PM10', 'PM2.5', 'ozone', 'temperature',
       'precipitation', 'windspeed', 'humidity', 'visibility', 'count'],
      dtype='object')
</pre>

```python
df.isna().sum()
```

<pre>
date               0
hour               0
PM10             102
PM2.5             95
ozone            128
temperature        0
precipitation      0
windspeed          0
humidity           0
visibility         0
count              0
dtype: int64
</pre>

## 2.EDA 2단계 - 가설 설정

*  '가설' 이란 단어를 생각해보면, 우리가 직접 가설을 만들어야 할것 같지만 통계에서 분석기법별 귀무가설/대립가설은 정해져있습니다.

- 귀무가설은 차이가 없다, 연관성이 없다, 효과가 없다.
- 대립가설은 차이가 있다, 연관성이 있다, 효과가 있다. 라고 간단하게 이해하시면 좋습니다.

    * 간단한 예로, 온도와 따릉이 대여량간 가설을 수립 해본다면

        - 귀무가설 : 온도와 따릉이 간에는 연관성이 없다.
        - 대립가설 : 온도와 따릉이 간에는 연관성이 있다.

      로 가설이 자연스레 수립 됩니다.

### (1) 가설 수립

* 'precipitation' 변수를 포함하여, 최소 5개 이상의 Feature와 따릉이 대여량 간 가설을 수립해주세요.
    * Guide : Target은 따릉이 대여량 입니다.

* 귀무가설 1: 온도와 따릉이 대여량간에는 관계가 없다.
* 대립가설 1: 온도와 따릉이 대여량간에는 관계가 있다.

* 귀무가설 2: 강우여부와 따릉이 대여량간에는 관계가 없다.
* 대립가설 2: 강우여부와 따릉이 대여량간에는 관계가 있다.

* 귀무가설 3: 시간과 따릉이 대여량간에는 관계가 없다.
* 대립가설 3: 시간과 따릉이 대여량간에는 관계가 있다.

* 귀무가설 4: 미세먼지수치(PM10)와 따릉이 대여량간에는 관계가 없다.
* 대립가설 4: 미세먼지수치(PM10)와 따릉이 대여량간에는 관계가 있다.

* 귀무가설 5: 풍속과 따릉이 대여량간에는 관계가 없다.
* 대립가설 5: 풍속과 따릉이 대여량간에는 관계가 있다.

## 3.EDA 3단계 - 이변량 분석 

* 자료의 종류에 맞게 X --> Y 에 대해서 그래프(시각화)와 가설검정(수치화)를 수행하고 결과를 평가합니다.

* 가설검정시 다음의 항목을 참조하여 수행합니다.

    * 유의수준 : 5%
    * 숫자 --> 숫자 : 상관분석
    * 범주 --> 범주 : 카이제곱검정
    * 범주 --> 숫자 : t검정, 분산분석
    * 숫자 --> 범주 : 로지스틱 회귀모형을 통해, 회귀계수의 P.value로 검정을 수행합니다.

### (1) 범주형 Feature --> 숫자형 Y (따릉이 대여 Count)

* 모든 범주형 Feature에 대해서 Y와 비교하여 차트를 그리고 수치화 하시오.  

    1. 시각화 : 그래프를 활용한 데이터 분석
    2. 수치화 : t-test, anova
    3. 관계 평가

#### 1) 강수 여부와 따릉이 대여량간 이변량 분석

```python
# 아래에 실습코드를 작성하고 결과를 확인합니다.

sns.barplot(x='precipitation', y='count', data=df)
plt.show()
```

![z_min_1_2_2_1](https://github.com/zacinthepark/TIL/assets/86648892/aceb233d-b613-45d0-ad01-cc5f76d4e34b)

- 1시간 전 비가 오지 않았을떄 (0 일때) 따릉이 대여 건수 평균이 100이상임
- 1시간 전 비가 왔을때 (1 일때) 따릉이 대여 건수는 매우 낮은 편임

```python
# 아래에 실습코드를 작성하고 결과를 확인합니다.

precipitation_0 = df.loc[df['precipitation'] == 0, 'count']
precipitation_1 = df.loc[df['precipitation'] == 1, 'count']

spst.ttest_ind(precipitation_0, precipitation_1)
```

<pre>
TtestResult(statistic=21.389614151911022, pvalue=8.86239184041254e-98, df=5825.0)
</pre>

```python
# 아래에 실습코드를 작성하고 결과를 확인합니다.

spst.f_oneway(precipitation_0, precipitation_1)
```

<pre>
F_onewayResult(statistic=457.5155935676325, pvalue=8.862391840432034e-98)
</pre>

* 귀무가설은 X가 Y와 관련이 없다. 
* 대립가설은 X와 Y가 관련이 있다.
* P-value (유의확률)가 0.05 이하라면? 해당 변수는 매우 유의미한 값으로 판단 가능함

### (2) 숫자형 Feature --> 숫자형 Y (따릉이 대여 Count)

* 모든 숫자형 Feature에 대해서 Y와 비교하여 차트를 그리고 수치화 하시오.  

    1. 시각화 : 그래프를 활용한 데이터 분석
    2. 수치화 : 상관분석
    3. 관계 평가

#### 1) 시간대별 대여량 분석

```python
# 아래에 실습코드를 작성하고 결과를 확인합니다.

sns.scatterplot(x='hour', y='count', data=df)
plt.show()
```

![z_min_1_2_2_2](https://github.com/zacinthepark/TIL/assets/86648892/b26cb2df-bad7-448d-b6f0-245ffc0608b8)

```python
# 아래에 실습코드를 작성하고 결과를 확인합니다.

spst.pearsonr(df['count'], df['hour'])
```

<pre>
PearsonRResult(statistic=0.5864350283919393, pvalue=0.0)
</pre>

#### 2) 온도 데이터 분석

```python
# 아래에 실습코드를 작성하고 결과를 확인합니다.

sns.scatterplot(x='temperature', y='count', data=df)
plt.show()
```

![z_min_1_2_2_3](https://github.com/zacinthepark/TIL/assets/86648892/f316ad0a-1eff-437b-8dbd-ebab64932e9a)

```python
# 아래에 실습코드를 작성하고 결과를 확인합니다.

spst.pearsonr(df['count'], df['temperature'])
```

<pre>
PearsonRResult(statistic=0.2771692363089791, pvalue=2.940516555113978e-103)
</pre>

#### 3) 풍속에 대한 분석

```python
# 아래에 실습코드를 작성하고 결과를 확인합니다.

sns.scatterplot(x='windspeed', y='count', data=df)
plt.show()
```

![z_min_1_2_2_4](https://github.com/zacinthepark/TIL/assets/86648892/923eb0b0-6e53-4d03-b0ee-c740dfef81ef)

```python
# 아래에 실습코드를 작성하고 결과를 확인합니다.

spst.pearsonr(df['count'], df['windspeed'])
```

<pre>
PearsonRResult(statistic=0.22372189900674888, pvalue=5.243317678213925e-67)
</pre>

#### 4) 습도에 대한 분석

```python
# 아래에 실습코드를 작성하고 결과를 확인합니다.

sns.scatterplot(x='humidity', y='count', data=df)
plt.show()
```

![z_min_1_2_2_5](https://github.com/zacinthepark/TIL/assets/86648892/09592be5-5919-44d3-8026-825abaa2060d)

```python
# 아래에 실습코드를 작성하고 결과를 확인합니다.

spst.pearsonr(df['count'], df['humidity'])
```

<pre>
PearsonRResult(statistic=-0.4789554265904137, pvalue=0.0)
</pre>

#### 5) 시정에 대한 분석

```python
# 아래에 실습코드를 작성하고 결과를 확인합니다.

sns.scatterplot(x='visibility', y='count', data=df)
plt.show()
```

![z_min_1_2_2_6](https://github.com/zacinthepark/TIL/assets/86648892/255a1038-482c-4f53-ad63-e7a7bd4ea6fa)

```python
# 아래에 실습코드를 작성하고 결과를 확인합니다.

spst.pearsonr(df['count'], df['visibility'])
```

<pre>
PearsonRResult(statistic=0.26582778327488765, pvalue=7.87600385276935e-95)
</pre>

#### 6) 오존 데이터 분석

```python
# 아래에 실습코드를 작성하고 결과를 확인합니다.

sns.scatterplot(x='ozone', y='count', data=df)
plt.show()
```

![z_min_1_2_2_7](https://github.com/zacinthepark/TIL/assets/86648892/0fca80ad-e84c-48a6-801e-b85e3aefa2ec)

```python
# 보간법을 이용해 결측치 처리 (주변 값들 바탕)

df['ozone'].interpolate(inplace=True)
```


```python
# 아래에 실습코드를 작성하고 결과를 확인합니다.

spst.pearsonr(df['count'], df['ozone'])
```

<pre>
PearsonRResult(statistic=0.3179918655691485, pvalue=4.721727543129668e-137)
</pre>

#### 7) 미세먼지 농도 데이터 분석

```python
# 아래에 실습코드를 작성하고 결과를 확인합니다.

sns.scatterplot(x='PM10', y='count', data=df)
plt.show()
```

![z_min_1_2_2_8](https://github.com/zacinthepark/TIL/assets/86648892/1b0eac02-2798-4490-8542-ff0327b629c0)

```python
df['PM10'].interpolate(inplace=True)
```

```python
# 아래에 실습코드를 작성하고 결과를 확인합니다.

spst.pearsonr(df['count'], df['PM10'])
```

<pre>
PearsonRResult(statistic=0.02753552779908241, pvalue=0.035564992622628286)
</pre>

#### 8) 초미세먼지 농도에 대한 분석

```python
# 아래에 실습코드를 작성하고 결과를 확인합니다.

sns.scatterplot(x='PM2.5', y='count', data=df)
plt.show()
```

![z_min_1_2_2_9](https://github.com/zacinthepark/TIL/assets/86648892/ba2f2b3f-2c56-4411-83ff-980284aa7169)

```python
df['PM2.5'].interpolate(inplace=True)
```

```python
# 아래에 실습코드를 작성하고 결과를 확인합니다.

spst.pearsonr(df['count'], df['PM2.5'])
```

<pre>
PearsonRResult(statistic=0.034833977797175945, pvalue=0.007830765224447958)
</pre>

## 4. 가설 검정

### 1. 강한 관계의 변수 (대립가설 채택) 

- 강수 여부, 시간대
- 습도 (조금 약함)


### 2. 약한 관계의 변수

- 온도, 풍속, 시정, 오존

### 3. 관계 없는 변수 (귀무가설 채택)

- 미세먼지 농도, 초미세먼지 농도
- 범주화 추가분석 필요

## 5. Insight 도출

* 자전거를 타는데 직접적인 영향을 주는 강수 여부와 시간대의 상관 계수가 모두 0.5이상이고 p-value도 낮은 값을 보여 강한 관계를 가진다는 것을 알 수 있다.
* 온도와 풍속, 시정, 오존은 p-value는 낮지만 상관 계수가 작아 약한 관계를 가진다고 정의하였다.
* 미세먼지 농도와 초미세먼지 농도 모두 p-value는 0.05 이하이지만, 상관 계수가 0.05 이하이기 때문에 관계가 없다고 판단하였다.

---

## 추가 분석

```python
low_df = df[df['count'] < 53]
```

```python
low_df.describe()
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>hour</th>
      <th>PM10</th>
      <th>PM2.5</th>
      <th>ozone</th>
      <th>temperature</th>
      <th>precipitation</th>
      <th>windspeed</th>
      <th>humidity</th>
      <th>visibility</th>
      <th>count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>1446.000000</td>
      <td>1446.000000</td>
      <td>1446.000000</td>
      <td>1446.000000</td>
      <td>1446.000000</td>
      <td>1446.000000</td>
      <td>1446.000000</td>
      <td>1446.000000</td>
      <td>1446.00000</td>
      <td>1446.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>5.721992</td>
      <td>26.767635</td>
      <td>13.708910</td>
      <td>0.023771</td>
      <td>16.652075</td>
      <td>0.243430</td>
      <td>1.976556</td>
      <td>80.816736</td>
      <td>1502.88935</td>
      <td>24.634163</td>
    </tr>
    <tr>
      <th>std</th>
      <td>5.371348</td>
      <td>39.289277</td>
      <td>13.188994</td>
      <td>0.012518</td>
      <td>6.873288</td>
      <td>0.429301</td>
      <td>1.016948</td>
      <td>13.530855</td>
      <td>662.38884</td>
      <td>13.061830</td>
    </tr>
    <tr>
      <th>min</th>
      <td>0.000000</td>
      <td>3.000000</td>
      <td>1.000000</td>
      <td>0.001000</td>
      <td>-2.700000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>37.000000</td>
      <td>61.00000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>3.000000</td>
      <td>12.000000</td>
      <td>5.000000</td>
      <td>0.015000</td>
      <td>11.500000</td>
      <td>0.000000</td>
      <td>1.300000</td>
      <td>73.000000</td>
      <td>853.00000</td>
      <td>15.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>4.000000</td>
      <td>20.000000</td>
      <td>11.000000</td>
      <td>0.024500</td>
      <td>18.100000</td>
      <td>0.000000</td>
      <td>1.900000</td>
      <td>83.000000</td>
      <td>2000.00000</td>
      <td>24.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>6.000000</td>
      <td>31.000000</td>
      <td>18.000000</td>
      <td>0.032000</td>
      <td>21.400000</td>
      <td>0.000000</td>
      <td>2.500000</td>
      <td>92.000000</td>
      <td>2000.00000</td>
      <td>34.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>23.000000</td>
      <td>615.000000</td>
      <td>120.000000</td>
      <td>0.073000</td>
      <td>31.500000</td>
      <td>1.000000</td>
      <td>6.800000</td>
      <td>100.000000</td>
      <td>2000.00000</td>
      <td>52.000000</td>
    </tr>
  </tbody>
</table>
</div>

```python
high_df = df[df['count'] > 315]
```

```python
high_df.describe()
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>hour</th>
      <th>PM10</th>
      <th>PM2.5</th>
      <th>ozone</th>
      <th>temperature</th>
      <th>precipitation</th>
      <th>windspeed</th>
      <th>humidity</th>
      <th>visibility</th>
      <th>count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>1447.000000</td>
      <td>1447.000000</td>
      <td>1447.000000</td>
      <td>1447.000000</td>
      <td>1447.000000</td>
      <td>1447.000000</td>
      <td>1447.000000</td>
      <td>1447.000000</td>
      <td>1447.000000</td>
      <td>1447.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>17.071873</td>
      <td>31.472391</td>
      <td>15.688059</td>
      <td>0.037801</td>
      <td>22.128611</td>
      <td>0.004838</td>
      <td>2.529026</td>
      <td>58.800968</td>
      <td>1905.518314</td>
      <td>475.901866</td>
    </tr>
    <tr>
      <th>std</th>
      <td>3.686592</td>
      <td>31.571253</td>
      <td>11.304467</td>
      <td>0.017938</td>
      <td>6.112053</td>
      <td>0.069408</td>
      <td>1.031731</td>
      <td>15.657218</td>
      <td>286.280522</td>
      <td>145.186583</td>
    </tr>
    <tr>
      <th>min</th>
      <td>7.000000</td>
      <td>3.000000</td>
      <td>1.000000</td>
      <td>0.002000</td>
      <td>-1.100000</td>
      <td>0.000000</td>
      <td>0.100000</td>
      <td>19.000000</td>
      <td>225.000000</td>
      <td>316.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>16.000000</td>
      <td>18.000000</td>
      <td>8.000000</td>
      <td>0.026000</td>
      <td>18.050000</td>
      <td>0.000000</td>
      <td>1.900000</td>
      <td>48.000000</td>
      <td>2000.000000</td>
      <td>367.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>18.000000</td>
      <td>26.000000</td>
      <td>13.000000</td>
      <td>0.036750</td>
      <td>23.000000</td>
      <td>0.000000</td>
      <td>2.500000</td>
      <td>58.000000</td>
      <td>2000.000000</td>
      <td>440.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>20.000000</td>
      <td>39.000000</td>
      <td>21.000000</td>
      <td>0.048500</td>
      <td>26.500000</td>
      <td>0.000000</td>
      <td>3.100000</td>
      <td>70.000000</td>
      <td>2000.000000</td>
      <td>540.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>22.000000</td>
      <td>606.000000</td>
      <td>99.000000</td>
      <td>0.107000</td>
      <td>35.700000</td>
      <td>1.000000</td>
      <td>6.600000</td>
      <td>99.000000</td>
      <td>2000.000000</td>
      <td>1746.000000</td>
    </tr>
  </tbody>
</table>
</div>

* 시간대: `3~6 / 16~20` -> 대체로 오후 시간에 이용량이 많음
* 미세먼지: `12~31/18~39`, `5~18/8~21` -> 관계찾기 힘듬
* 오존: `0.015~0.032` / `0.026~0.048` -> 오존 수치가 높을 때 이용량이 많음
    * 반대가 아닌 이유? 오존 수치가 높을 때 대중교통을 권장하는 제도의 유효성? 계절의 영향?
* 기온: `11.5~21.4 / 18.05~26.5` -> 기온이 높을 때가 이용량이 많음
* 강우여부: `(평균) 0.429301 / 0.004838` -> 비가 오지 않을 때 이용량이 많음
* 풍속: `1.3~2.5 / 1.9~3.1` -> 관계가 약함
* 습도: `73~92 / 48~70` -> 습도가 낮을 때 이용량이 많음
* 가시성: `(평균) 1502 / 1905` -> 가시성이 높을 때 이용량이 많음

### 강수 여부, 습도의 관계

```python
# 아래에 실습코드를 작성하고 결과를 확인합니다.

sns.barplot(x='precipitation', y='humidity', data=df)
plt.show()
```

![z_min_1_2_2_10](https://github.com/zacinthepark/TIL/assets/86648892/32029055-01ab-433b-ae26-61e7851107bc)

```python
x_0 = df.loc[df['precipitation'] == 0, 'humidity']
x_1 = df.loc[df['precipitation'] == 1, 'humidity']

print(spst.ttest_ind(x_0, x_1))
print(spst.f_oneway(x_0, x_1))
```

<pre>
TtestResult(statistic=-31.798633125685747, pvalue=9.309643500829344e-205, df=5825.0)
F_onewayResult(statistic=1011.1530686619589, pvalue=9.309643500849526e-205)
</pre>

- 강수 여부에 따라 습도의 평균 차이가 유의하다
- 강수 여부에 따라 습도는 차이가 있다
