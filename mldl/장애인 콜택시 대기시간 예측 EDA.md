# 장애인콜택시 대기시간 예측

## 0.미션

* 1.개별 변수 분석하기

    * 앞서 생성된 각 변수들 특히 추가로 생성한 변수들에 대해서 단변량 분석을 수행합니다.
    * 시각화 : Histogram, Boxplot, Barplot
    * 통계량 : 기초 통계량
    * `[옵션]` 날짜 요소 관점을 추가해서 EDA 를 수행하시오.

* 2.Features와 Target의 관계 분석하기

    * Target은 숫자입니다.
    * 숫자형 feature들과 Target 과의 관계
        * 한꺼번에 상관관계를 확인하는 방법을 이용하여 분석합시다.
    * 범주형 feature들과 Target
        * sns.barplot, t-검정, 분산분석 등을 이용하여 분석합니다.
    * Target과 관련이 높은 feature와 그렇지 않은 feature를 정리해 봅시다.

## 1.환경설정

### (1) 경로 설정

#### 1) 로컬 수행(Anaconda)

```python
# path = 'C:/Users/User/project/'
```

#### 2) 구글 콜랩 수행

* 구글 드라이브 연결

```python
# colab 그래프 한글화 코드
# jupyter 사용시 코드 주석처리 할 것.
# import seaborn as sns
# import matplotlib.pyplot as plt
# import matplotlib as mpl
# import warnings

# !sudo apt-get install -y fonts-nanum
# !sudo fc-cache -fv
# !rm ~/.cache/matplotlib -rf

# warnings.simplefilter(action='ignore', category=UserWarning)

# plt.rc('font', family='NanumBarunGothic')
# mpl.rcParams['axes.unicode_minus'] = False

# # colab - drive 연동
# from google.colab import drive
# drive.mount('/content/drive')
```

```python
# from google.colab import drive
# drive.mount('/content/drive')
```

```python
# path = '/content/drive/MyDrive/project/'
```

### (2) 라이브러리 설치 및 불러오기

#### 1) 설치

* requirements.txt 파일을 아래 위치에 두고 다음 코드를 실행하시오.
    * 로컬 : 다음 코드셀 실행
    * 구글콜랩 : requirements.txt 파일을 왼쪽 `[파일]`탭에 복사해 넣고 다음 코드셀 실행

```python
# !pip install -r requirements.txt
```

#### 2) 라이브러리 로딩

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib
import seaborn as sns
import scipy.stats as spst
import joblib
```

### (3) 데이터 불러오기

```python
data = pd.read_pickle('data1_1.pkl')
```

```python
display(data.head(5))
display(data.tail(5))
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>count_taxi</th>
      <th>receipt</th>
      <th>boarding</th>
      <th>avg_rate</th>
      <th>avg_ride_distance</th>
      <th>target</th>
      <th>temp_max</th>
      <th>temp_min</th>
      <th>rain(mm)</th>
      <th>...</th>
      <th>season</th>
      <th>year</th>
      <th>weekend</th>
      <th>covid_19</th>
      <th>holiday</th>
      <th>day7_avg_wait_time</th>
      <th>ride_ratio</th>
      <th>temp_avg</th>
      <th>humidity_avg</th>
      <th>weekend_holiday</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2015-01-01</td>
      <td>213</td>
      <td>1023</td>
      <td>924</td>
      <td>2427</td>
      <td>10764</td>
      <td>17.2</td>
      <td>-2.0</td>
      <td>-8.9</td>
      <td>0.0</td>
      <td>...</td>
      <td>Winter</td>
      <td>2015</td>
      <td>0</td>
      <td>0</td>
      <td>1.0</td>
      <td>17.200000</td>
      <td>0.90</td>
      <td>-5.4</td>
      <td>45.5</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2015-01-02</td>
      <td>420</td>
      <td>3158</td>
      <td>2839</td>
      <td>2216</td>
      <td>8611</td>
      <td>26.2</td>
      <td>2.4</td>
      <td>-9.2</td>
      <td>0.0</td>
      <td>...</td>
      <td>Winter</td>
      <td>2015</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>21.700000</td>
      <td>0.90</td>
      <td>-3.4</td>
      <td>55.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2015-01-03</td>
      <td>209</td>
      <td>1648</td>
      <td>1514</td>
      <td>2377</td>
      <td>10198</td>
      <td>24.5</td>
      <td>8.2</td>
      <td>0.2</td>
      <td>0.0</td>
      <td>...</td>
      <td>Winter</td>
      <td>2015</td>
      <td>1</td>
      <td>0</td>
      <td>0.0</td>
      <td>22.633333</td>
      <td>0.92</td>
      <td>4.2</td>
      <td>73.5</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2015-01-04</td>
      <td>196</td>
      <td>1646</td>
      <td>1526</td>
      <td>2431</td>
      <td>10955</td>
      <td>26.2</td>
      <td>7.9</td>
      <td>-0.9</td>
      <td>0.0</td>
      <td>...</td>
      <td>Winter</td>
      <td>2015</td>
      <td>1</td>
      <td>0</td>
      <td>0.0</td>
      <td>23.525000</td>
      <td>0.93</td>
      <td>3.5</td>
      <td>73.5</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2015-01-05</td>
      <td>421</td>
      <td>4250</td>
      <td>3730</td>
      <td>2214</td>
      <td>8663</td>
      <td>23.6</td>
      <td>4.1</td>
      <td>-7.4</td>
      <td>3.4</td>
      <td>...</td>
      <td>Winter</td>
      <td>2015</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>23.540000</td>
      <td>0.88</td>
      <td>-1.7</td>
      <td>63.5</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 25 columns</p>
</div>

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>count_taxi</th>
      <th>receipt</th>
      <th>boarding</th>
      <th>avg_rate</th>
      <th>avg_ride_distance</th>
      <th>target</th>
      <th>temp_max</th>
      <th>temp_min</th>
      <th>rain(mm)</th>
      <th>...</th>
      <th>season</th>
      <th>year</th>
      <th>weekend</th>
      <th>covid_19</th>
      <th>holiday</th>
      <th>day7_avg_wait_time</th>
      <th>ride_ratio</th>
      <th>temp_avg</th>
      <th>humidity_avg</th>
      <th>weekend_holiday</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2917</th>
      <td>2022-12-26</td>
      <td>603</td>
      <td>5555</td>
      <td>4605</td>
      <td>2163</td>
      <td>7889</td>
      <td>44.4</td>
      <td>3.0</td>
      <td>-7.3</td>
      <td>0.0</td>
      <td>...</td>
      <td>Winter</td>
      <td>2022</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>42.771429</td>
      <td>0.83</td>
      <td>-2.2</td>
      <td>68.5</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2918</th>
      <td>2022-12-27</td>
      <td>669</td>
      <td>5635</td>
      <td>4654</td>
      <td>2198</td>
      <td>8178</td>
      <td>44.8</td>
      <td>-0.3</td>
      <td>-5.4</td>
      <td>0.1</td>
      <td>...</td>
      <td>Winter</td>
      <td>2022</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>43.514286</td>
      <td>0.83</td>
      <td>-2.8</td>
      <td>66.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2919</th>
      <td>2022-12-28</td>
      <td>607</td>
      <td>5654</td>
      <td>4648</td>
      <td>2161</td>
      <td>7882</td>
      <td>52.5</td>
      <td>1.7</td>
      <td>-7.8</td>
      <td>0.0</td>
      <td>...</td>
      <td>Winter</td>
      <td>2022</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>42.957143</td>
      <td>0.82</td>
      <td>-3.0</td>
      <td>52.5</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2920</th>
      <td>2022-12-29</td>
      <td>581</td>
      <td>5250</td>
      <td>4247</td>
      <td>2229</td>
      <td>8433</td>
      <td>38.3</td>
      <td>2.1</td>
      <td>-4.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>Winter</td>
      <td>2022</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>41.042857</td>
      <td>0.81</td>
      <td>-1.0</td>
      <td>62.5</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2921</th>
      <td>2022-12-30</td>
      <td>600</td>
      <td>5293</td>
      <td>4200</td>
      <td>2183</td>
      <td>8155</td>
      <td>33.7</td>
      <td>-4.4</td>
      <td>-4.4</td>
      <td>0.0</td>
      <td>...</td>
      <td>Winter</td>
      <td>2022</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>41.657143</td>
      <td>0.79</td>
      <td>-4.4</td>
      <td>66.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 25 columns</p>
</div>

```python
print(data.isna().sum())
print('=' * 50)
print(data.info())
```

<pre>
Date                  0
count_taxi            0
receipt               0
boarding              0
avg_rate              0
avg_ride_distance     0
target                0
temp_max              0
temp_min              0
rain(mm)              0
humidity_max(%)       0
humidity_min(%)       0
sunshine(MJ/m2)       0
weekday               0
month                 0
season                0
year                  0
weekend               0
covid_19              0
holiday               0
day7_avg_wait_time    0
ride_ratio            0
temp_avg              0
humidity_avg          0
weekend_holiday       0
dtype: int64
==================================================
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 2922 entries, 0 to 2921
Data columns (total 25 columns):
 #   Column              Non-Null Count  Dtype         
---  ------              --------------  -----         
 0   Date                2922 non-null   datetime64[ns]
 1   count_taxi          2922 non-null   int64         
 2   receipt             2922 non-null   int64         
 3   boarding            2922 non-null   int64         
 4   avg_rate            2922 non-null   int64         
 5   avg_ride_distance   2922 non-null   int64         
 6   target              2922 non-null   float64       
 7   temp_max            2922 non-null   float64       
 8   temp_min            2922 non-null   float64       
 9   rain(mm)            2922 non-null   float64       
 10  humidity_max(%)     2922 non-null   float64       
 11  humidity_min(%)     2922 non-null   float64       
 12  sunshine(MJ/m2)     2922 non-null   float64       
 13  weekday             2922 non-null   category      
 14  month               2922 non-null   int32         
 15  season              2922 non-null   category      
 16  year                2922 non-null   int32         
 17  weekend             2922 non-null   int64         
 18  covid_19            2922 non-null   int64         
 19  holiday             2922 non-null   float64       
 20  day7_avg_wait_time  2922 non-null   float64       
 21  ride_ratio          2922 non-null   float64       
 22  temp_avg            2922 non-null   float64       
 23  humidity_avg        2922 non-null   float64       
 24  weekend_holiday     2922 non-null   float64       
dtypes: category(2), datetime64[ns](1), float64(13), int32(2), int64(7)
memory usage: 508.1 KB
None
</pre>

## 2.EDA : 1단계 - 개별 정보 분석하기

* **세부요구사항**

    * 의미 있는 변수들을 7개 이상 선정하고 단변량분석을 수행합니다.

    * [옵션] 각 변수에 대한 탐색시, 요일별, 월별, 연도별로 나눠서도 확인해보세요.

    * 단변량 분석을 위한 코드를 함수로 작성하고 수행하세요.


### (1) 단변량 분석 함수 작성

```python
# 숫자형 변수 분석
def eda_1_n(data, var, hue_var = ''):
    display(data[[var]].describe().T)

    if hue_var == '' :
        plt.figure(figsize=(15,10))
        plt.subplot(2,1,1)
        sns.histplot(data[var], kde=True, bins=50)
        plt.grid()

        plt.subplot(2,1,2)
        sns.boxplot(x=data[var])
        plt.grid()
        plt.show()
    else :
        plt.figure(figsize=(15,5))
        plt.subplot(1,2,1)
        sns.kdeplot(x=var, data=data, hue=hue_var)
        plt.grid()

        plt.subplot(1,2,2)
        sns.boxplot(x=hue_var, y=var, data=data)
        plt.grid()
```

```python
# 범주형 변수 분석
def eda_1_c(data, var, hue_var=''):

    cnt = data[var].value_counts()
    prop = data[var].value_counts() / data.shape[0]
    result = pd.DataFrame({'Count': cnt, 'Prop': prop})
    display(result)

    sns.countplot(x=var, data=data)
    plt.grid()
    plt.show()
```

```python
# 주말, 공휴일에 따른 분석 함수 추가
def eda_1_n_weekend_holiday(data, var):
    display(eda_1_n(data, var, hue_var='weekend'))
    display(eda_1_n(data, var, hue_var='holiday'))
    display(eda_1_n(data, var, hue_var='weekend_holiday'))
```

### (2) 숫자형 변수

#### 1) 접수건

```python
col = 'receipt'
eda_1_n(data, col)
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>receipt</th>
      <td>2922.0</td>
      <td>3925.439767</td>
      <td>1509.964823</td>
      <td>527.0</td>
      <td>2160.5</td>
      <td>4720.5</td>
      <td>5110.0</td>
      <td>6182.0</td>
    </tr>
  </tbody>
</table>
</div>

![z_,min_2_2_2_1](https://github.com/zacinthepark/TIL/assets/86648892/6a9bd873-8c9b-47e8-af0f-a15581f9fdc9)

```python
eda_1_n_weekend_holiday(data, col)
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>receipt</th>
      <td>2922.0</td>
      <td>3925.439767</td>
      <td>1509.964823</td>
      <td>527.0</td>
      <td>2160.5</td>
      <td>4720.5</td>
      <td>5110.0</td>
      <td>6182.0</td>
    </tr>
  </tbody>
</table>
</div>

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>receipt</th>
      <td>2922.0</td>
      <td>3925.439767</td>
      <td>1509.964823</td>
      <td>527.0</td>
      <td>2160.5</td>
      <td>4720.5</td>
      <td>5110.0</td>
      <td>6182.0</td>
    </tr>
  </tbody>
</table>
</div>

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>receipt</th>
      <td>2922.0</td>
      <td>3925.439767</td>
      <td>1509.964823</td>
      <td>527.0</td>
      <td>2160.5</td>
      <td>4720.5</td>
      <td>5110.0</td>
      <td>6182.0</td>
    </tr>
  </tbody>
</table>
</div>

![z_,min_2_2_2_2](https://github.com/zacinthepark/TIL/assets/86648892/e074d850-d501-45d4-9bda-0b281d946164)

```python
display(eda_1_n(data, col, hue_var='covid_19'))
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>receipt</th>
      <td>2922.0</td>
      <td>3925.439767</td>
      <td>1509.964823</td>
      <td>527.0</td>
      <td>2160.5</td>
      <td>4720.5</td>
      <td>5110.0</td>
      <td>6182.0</td>
    </tr>
  </tbody>
</table>
</div>

![z_,min_2_2_2_3](https://github.com/zacinthepark/TIL/assets/86648892/175a7e2b-10f5-4768-9689-a0d4cbdac4b7)

#### 2) 평균대기시간

```python
col = 'target'
eda_1_n(data, col)
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>target</th>
      <td>2922.0</td>
      <td>40.30616</td>
      <td>14.097992</td>
      <td>17.2</td>
      <td>29.6</td>
      <td>38.2</td>
      <td>48.6</td>
      <td>96.1</td>
    </tr>
  </tbody>
</table>
</div>

![z_,min_2_2_2_4](https://github.com/zacinthepark/TIL/assets/86648892/7457ff36-88bc-48a2-ad72-c60dfc63035b)

```python
display(eda_1_n(data, col, hue_var='covid_19'))
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>target</th>
      <td>2922.0</td>
      <td>40.30616</td>
      <td>14.097992</td>
      <td>17.2</td>
      <td>29.6</td>
      <td>38.2</td>
      <td>48.6</td>
      <td>96.1</td>
    </tr>
  </tbody>
</table>
</div>

![z_,min_2_2_2_5](https://github.com/zacinthepark/TIL/assets/86648892/47c2cdad-46c6-4314-9e9d-44abb3cc20fc)

#### 3) 운임

```python
col = 'avg_rate'
eda_1_n(data, col)
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>avg_rate</th>
      <td>2922.0</td>
      <td>2304.357632</td>
      <td>107.369846</td>
      <td>2131.0</td>
      <td>2228.0</td>
      <td>2257.0</td>
      <td>2401.0</td>
      <td>2733.0</td>
    </tr>
  </tbody>
</table>
</div>

![z_,min_2_2_2_6](https://github.com/zacinthepark/TIL/assets/86648892/3e21bc8e-8f1d-4243-90c9-50b5f5f2faee)

```python
eda_1_n_weekend_holiday(data, col)
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>avg_rate</th>
      <td>2922.0</td>
      <td>2304.357632</td>
      <td>107.369846</td>
      <td>2131.0</td>
      <td>2228.0</td>
      <td>2257.0</td>
      <td>2401.0</td>
      <td>2733.0</td>
    </tr>
  </tbody>
</table>
</div>

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>avg_rate</th>
      <td>2922.0</td>
      <td>2304.357632</td>
      <td>107.369846</td>
      <td>2131.0</td>
      <td>2228.0</td>
      <td>2257.0</td>
      <td>2401.0</td>
      <td>2733.0</td>
    </tr>
  </tbody>
</table>
</div>

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>avg_rate</th>
      <td>2922.0</td>
      <td>2304.357632</td>
      <td>107.369846</td>
      <td>2131.0</td>
      <td>2228.0</td>
      <td>2257.0</td>
      <td>2401.0</td>
      <td>2733.0</td>
    </tr>
  </tbody>
</table>
</div>

![z_,min_2_2_2_7](https://github.com/zacinthepark/TIL/assets/86648892/b37194e7-a325-4fac-856c-519d59fe57f7)

```python
display(eda_1_n(data, col, hue_var='covid_19'))
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>avg_rate</th>
      <td>2922.0</td>
      <td>2304.357632</td>
      <td>107.369846</td>
      <td>2131.0</td>
      <td>2228.0</td>
      <td>2257.0</td>
      <td>2401.0</td>
      <td>2733.0</td>
    </tr>
  </tbody>
</table>
</div>

![z_,min_2_2_2_8](https://github.com/zacinthepark/TIL/assets/86648892/2ddeff1f-7882-4de2-bb1a-bfe6e55cf545)

#### 4) 평균거리

```python
col = 'avg_ride_distance'
eda_1_n(data, col)
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>avg_ride_distance</th>
      <td>2922.0</td>
      <td>9254.291239</td>
      <td>1020.236019</td>
      <td>7672.0</td>
      <td>8521.0</td>
      <td>8821.5</td>
      <td>10154.0</td>
      <td>14136.0</td>
    </tr>
  </tbody>
</table>
</div>

![z_,min_2_2_2_9](https://github.com/zacinthepark/TIL/assets/86648892/b5f68723-8846-4806-9e82-4063c54ee465)

```python
eda_1_n_weekend_holiday(data, col)
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>avg_ride_distance</th>
      <td>2922.0</td>
      <td>9254.291239</td>
      <td>1020.236019</td>
      <td>7672.0</td>
      <td>8521.0</td>
      <td>8821.5</td>
      <td>10154.0</td>
      <td>14136.0</td>
    </tr>
  </tbody>
</table>
</div>

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>avg_ride_distance</th>
      <td>2922.0</td>
      <td>9254.291239</td>
      <td>1020.236019</td>
      <td>7672.0</td>
      <td>8521.0</td>
      <td>8821.5</td>
      <td>10154.0</td>
      <td>14136.0</td>
    </tr>
  </tbody>
</table>
</div>

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>avg_ride_distance</th>
      <td>2922.0</td>
      <td>9254.291239</td>
      <td>1020.236019</td>
      <td>7672.0</td>
      <td>8521.0</td>
      <td>8821.5</td>
      <td>10154.0</td>
      <td>14136.0</td>
    </tr>
  </tbody>
</table>
</div>

![z_,min_2_2_2_10](https://github.com/zacinthepark/TIL/assets/86648892/4d536797-6b82-4f3d-abe7-bab108317be5)

```python
display(eda_1_n(data, col, hue_var='covid_19'))
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>avg_ride_distance</th>
      <td>2922.0</td>
      <td>9254.291239</td>
      <td>1020.236019</td>
      <td>7672.0</td>
      <td>8521.0</td>
      <td>8821.5</td>
      <td>10154.0</td>
      <td>14136.0</td>
    </tr>
  </tbody>
</table>
</div>

![z_,min_2_2_2_11](https://github.com/zacinthepark/TIL/assets/86648892/c899bc38-5110-48f1-a4fa-09ae7159f72e)

#### 5) 탑승률

```python
col = 'ride_ratio'
eda_1_n(data, col)
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>ride_ratio</th>
      <td>2922.0</td>
      <td>0.84154</td>
      <td>0.052311</td>
      <td>0.6</td>
      <td>0.81</td>
      <td>0.85</td>
      <td>0.88</td>
      <td>0.97</td>
    </tr>
  </tbody>
</table>
</div>

![z_,min_2_2_2_12](https://github.com/zacinthepark/TIL/assets/86648892/85eaf756-99d5-4983-b2eb-eac4b366d273)

```python
eda_1_n_weekend_holiday(data, col)
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>ride_ratio</th>
      <td>2922.0</td>
      <td>0.84154</td>
      <td>0.052311</td>
      <td>0.6</td>
      <td>0.81</td>
      <td>0.85</td>
      <td>0.88</td>
      <td>0.97</td>
    </tr>
  </tbody>
</table>
</div>

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>ride_ratio</th>
      <td>2922.0</td>
      <td>0.84154</td>
      <td>0.052311</td>
      <td>0.6</td>
      <td>0.81</td>
      <td>0.85</td>
      <td>0.88</td>
      <td>0.97</td>
    </tr>
  </tbody>
</table>
</div>

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>ride_ratio</th>
      <td>2922.0</td>
      <td>0.84154</td>
      <td>0.052311</td>
      <td>0.6</td>
      <td>0.81</td>
      <td>0.85</td>
      <td>0.88</td>
      <td>0.97</td>
    </tr>
  </tbody>
</table>
</div>

![z_,min_2_2_2_13](https://github.com/zacinthepark/TIL/assets/86648892/0caa5343-8208-4ca3-8338-c4c50fcaf31d)

```python
display(eda_1_n(data, col, hue_var='covid_19'))
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>ride_ratio</th>
      <td>2922.0</td>
      <td>0.84154</td>
      <td>0.052311</td>
      <td>0.6</td>
      <td>0.81</td>
      <td>0.85</td>
      <td>0.88</td>
      <td>0.97</td>
    </tr>
  </tbody>
</table>
</div>

![z_,min_2_2_2_14](https://github.com/zacinthepark/TIL/assets/86648892/f33a19e1-314f-4053-ae2a-92ddfef89e38)

#### 6) 최고기온(°C)

```python
col = 'temp_max'
eda_1_n(data, col)
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>temp_max</th>
      <td>2922.0</td>
      <td>18.0795</td>
      <td>10.705421</td>
      <td>-11.2</td>
      <td>9.0</td>
      <td>19.7</td>
      <td>27.4</td>
      <td>39.4</td>
    </tr>
  </tbody>
</table>
</div>

![z_,min_2_2_2_15](https://github.com/zacinthepark/TIL/assets/86648892/47b12a36-0b13-4d88-9d2c-b96386789d13)

```python
eda_1_n_weekend_holiday(data, col)
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>temp_max</th>
      <td>2922.0</td>
      <td>18.0795</td>
      <td>10.705421</td>
      <td>-11.2</td>
      <td>9.0</td>
      <td>19.7</td>
      <td>27.4</td>
      <td>39.4</td>
    </tr>
  </tbody>
</table>
</div>

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>temp_max</th>
      <td>2922.0</td>
      <td>18.0795</td>
      <td>10.705421</td>
      <td>-11.2</td>
      <td>9.0</td>
      <td>19.7</td>
      <td>27.4</td>
      <td>39.4</td>
    </tr>
  </tbody>
</table>
</div>

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>temp_max</th>
      <td>2922.0</td>
      <td>18.0795</td>
      <td>10.705421</td>
      <td>-11.2</td>
      <td>9.0</td>
      <td>19.7</td>
      <td>27.4</td>
      <td>39.4</td>
    </tr>
  </tbody>
</table>
</div>

![z_,min_2_2_2_16](https://github.com/zacinthepark/TIL/assets/86648892/5d8a27c6-4264-40e4-82ab-05dd5fdda514)

```python
display(eda_1_n(data, col, hue_var='covid_19'))
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>temp_max</th>
      <td>2922.0</td>
      <td>18.0795</td>
      <td>10.705421</td>
      <td>-11.2</td>
      <td>9.0</td>
      <td>19.7</td>
      <td>27.4</td>
      <td>39.4</td>
    </tr>
  </tbody>
</table>
</div>

![z_,min_2_2_2_17](https://github.com/zacinthepark/TIL/assets/86648892/75ff6d46-547b-4f81-b1cb-1c594e5900df)

#### 7) 일강수량(mm)

```python
col = 'rain(mm)'
eda_1_n(data, col)
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>rain(mm)</th>
      <td>2922.0</td>
      <td>3.355613</td>
      <td>12.595804</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.3</td>
      <td>178.9</td>
    </tr>
  </tbody>
</table>
</div>

![z_,min_2_2_2_18](https://github.com/zacinthepark/TIL/assets/86648892/e36d10aa-3fbf-4bc5-8c97-e6b559c20d51)

```python
eda_1_n_weekend_holiday(data, col)
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>rain(mm)</th>
      <td>2922.0</td>
      <td>3.355613</td>
      <td>12.595804</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.3</td>
      <td>178.9</td>
    </tr>
  </tbody>
</table>
</div>

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>rain(mm)</th>
      <td>2922.0</td>
      <td>3.355613</td>
      <td>12.595804</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.3</td>
      <td>178.9</td>
    </tr>
  </tbody>
</table>
</div>

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>rain(mm)</th>
      <td>2922.0</td>
      <td>3.355613</td>
      <td>12.595804</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.3</td>
      <td>178.9</td>
    </tr>
  </tbody>
</table>
</div>

![z_,min_2_2_2_19](https://github.com/zacinthepark/TIL/assets/86648892/24b58353-c94a-440b-b1fe-394cfcd7ccf8)

```python
display(eda_1_n(data, col, hue_var='covid_19'))
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>rain(mm)</th>
      <td>2922.0</td>
      <td>3.355613</td>
      <td>12.595804</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.3</td>
      <td>178.9</td>
    </tr>
  </tbody>
</table>
</div>

![z_,min_2_2_2_20](https://github.com/zacinthepark/TIL/assets/86648892/57618052-1b90-46b5-a719-12bb47adac98)

### (3) 범주형 변수

#### 1) 공휴일 유무

```python
eda_1_c(data, var='holiday')
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Count</th>
      <th>Prop</th>
    </tr>
    <tr>
      <th>holiday</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0.0</th>
      <td>2802</td>
      <td>0.958932</td>
    </tr>
    <tr>
      <th>1.0</th>
      <td>120</td>
      <td>0.041068</td>
    </tr>
  </tbody>
</table>
</div>

![z_,min_2_2_2_21](https://github.com/zacinthepark/TIL/assets/86648892/ac4893c0-a5d5-48a1-b47d-da132ad83ee5)

#### 2) 주말

```python
eda_1_c(data, var='weekend')
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Count</th>
      <th>Prop</th>
    </tr>
    <tr>
      <th>weekend</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2088</td>
      <td>0.714579</td>
    </tr>
    <tr>
      <th>1</th>
      <td>834</td>
      <td>0.285421</td>
    </tr>
  </tbody>
</table>
</div>

![z_,min_2_2_2_22](https://github.com/zacinthepark/TIL/assets/86648892/fd503aae-25d8-4c51-946a-ef019a2c216b)

#### 주말&공휴일

```python
eda_1_c(data, var='weekend_holiday')
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Count</th>
      <th>Prop</th>
    </tr>
    <tr>
      <th>weekend_holiday</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0.0</th>
      <td>2005</td>
      <td>0.686174</td>
    </tr>
    <tr>
      <th>1.0</th>
      <td>917</td>
      <td>0.313826</td>
    </tr>
  </tbody>
</table>
</div>

![z_,min_2_2_2_23](https://github.com/zacinthepark/TIL/assets/86648892/30b3da46-7da4-4973-b83b-146a24888811)

#### 코로나

```python
eda_1_c(data, var='covid_19')
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Count</th>
      <th>Prop</th>
    </tr>
    <tr>
      <th>covid_19</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2102</td>
      <td>0.71937</td>
    </tr>
    <tr>
      <th>1</th>
      <td>820</td>
      <td>0.28063</td>
    </tr>
  </tbody>
</table>
</div>

![z_,min_2_2_2_24](https://github.com/zacinthepark/TIL/assets/86648892/d6aa2be8-4e93-44c7-9ca9-66af9e131277)

## 3.EDA 2단계 - feature와 target 비교 분석하기

### (1) 숫자 feature --> Target

* 전체 상관계수 시각화(heatmap)
* 상위 n개 산점도 그리기

```python
data['weekend'] = data['weekend'].astype('category')
data['covid_19'] = data['covid_19'].astype('category')
data['holiday'] = data['holiday'].astype('category')
data['weekend_holiday'] = data['weekend_holiday'].astype('category')
```

```python
plt.figure(figsize = (12, 8))

sns.heatmap(data = data.corr(numeric_only = True),
            annot = True,
            fmt = '.2f',
            cmap = 'Blues')
plt.show()
```

![z_,min_2_2_2_25](https://github.com/zacinthepark/TIL/assets/86648892/47225797-8781-47b9-97da-4a1821e0d034)

#### 1) 전체 상관계수 시각화

```python
# 전체 상관관계를 한눈에 보여주기 함수
def eda_2_corr(data, num_vars):

    temp = data.loc[:, num_vars]
    corr = temp.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))

    display(mask * corr)

    sns.set(style='white')
    plt.figure(figsize=(12, 12))
    cmap = sns.diverging_palette(220, 10, as_cmap=True)
    sns.heatmap(corr, mask=mask, cmap=cmap, center=0, square=True, linewidths=.5, annot=True)
    plt.show()
```

```python
display(data.columns)
```

<pre>
Index(['Date', 'count_taxi', 'receipt', 'boarding', 'avg_rate',
       'avg_ride_distance', 'target', 'temp_max', 'temp_min', 'rain(mm)',
       'humidity_max(%)', 'humidity_min(%)', 'sunshine(MJ/m2)', 'weekday',
       'month', 'season', 'year', 'weekend', 'covid_19', 'holiday',
       'day7_avg_wait_time', 'ride_ratio', 'temp_avg', 'humidity_avg',
       'weekend_holiday'],
      dtype='object')
</pre>

```python
num_vars = ['count_taxi', 'receipt', 'boarding', 'avg_rate', 'avg_ride_distance', 'ride_ratio',
            'temp_max', 'temp_min', 'rain(mm)', 'humidity_max(%)', 'humidity_min(%)', 'sunshine(MJ/m2)',
            'temp_avg', 'humidity_avg', 'month', 'year', 'target']

eda_2_corr(data, num_vars)
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count_taxi</th>
      <th>receipt</th>
      <th>boarding</th>
      <th>avg_rate</th>
      <th>avg_ride_distance</th>
      <th>ride_ratio</th>
      <th>temp_max</th>
      <th>temp_min</th>
      <th>rain(mm)</th>
      <th>humidity_max(%)</th>
      <th>humidity_min(%)</th>
      <th>sunshine(MJ/m2)</th>
      <th>temp_avg</th>
      <th>humidity_avg</th>
      <th>month</th>
      <th>year</th>
      <th>target</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count_taxi</th>
      <td>1.0</td>
      <td>0.885891</td>
      <td>0.904666</td>
      <td>-0.844747</td>
      <td>-0.857720</td>
      <td>-0.027245</td>
      <td>0.108444</td>
      <td>0.109567</td>
      <td>0.002630</td>
      <td>0.049112</td>
      <td>0.088131</td>
      <td>0.076509</td>
      <td>0.110110</td>
      <td>0.077438</td>
      <td>0.131941</td>
      <td>0.243698</td>
      <td>0.088040</td>
    </tr>
    <tr>
      <th>receipt</th>
      <td>0.0</td>
      <td>1.000000</td>
      <td>0.988755</td>
      <td>-0.850509</td>
      <td>-0.847931</td>
      <td>-0.250082</td>
      <td>0.057957</td>
      <td>0.054169</td>
      <td>-0.012803</td>
      <td>-0.013810</td>
      <td>-0.000597</td>
      <td>0.024437</td>
      <td>0.056619</td>
      <td>-0.007383</td>
      <td>0.089444</td>
      <td>0.001568</td>
      <td>0.316562</td>
    </tr>
    <tr>
      <th>boarding</th>
      <td>0.0</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>-0.868124</td>
      <td>-0.858811</td>
      <td>-0.116599</td>
      <td>0.064283</td>
      <td>0.058452</td>
      <td>-0.015746</td>
      <td>-0.008045</td>
      <td>0.006238</td>
      <td>0.040464</td>
      <td>0.061984</td>
      <td>-0.000382</td>
      <td>0.060421</td>
      <td>0.001700</td>
      <td>0.229574</td>
    </tr>
    <tr>
      <th>avg_rate</th>
      <td>-0.0</td>
      <td>-0.000000</td>
      <td>-0.000000</td>
      <td>1.000000</td>
      <td>0.977615</td>
      <td>0.007111</td>
      <td>0.083955</td>
      <td>0.070507</td>
      <td>0.011267</td>
      <td>0.019822</td>
      <td>-0.035445</td>
      <td>0.008843</td>
      <td>0.077912</td>
      <td>-0.011006</td>
      <td>0.051396</td>
      <td>-0.108421</td>
      <td>-0.049645</td>
    </tr>
    <tr>
      <th>avg_ride_distance</th>
      <td>-0.0</td>
      <td>-0.000000</td>
      <td>-0.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>0.046916</td>
      <td>0.088111</td>
      <td>0.073573</td>
      <td>0.004747</td>
      <td>0.020547</td>
      <td>-0.040055</td>
      <td>-0.000657</td>
      <td>0.081582</td>
      <td>-0.013380</td>
      <td>0.033894</td>
      <td>-0.217514</td>
      <td>-0.084684</td>
    </tr>
    <tr>
      <th>ride_ratio</th>
      <td>-0.0</td>
      <td>-0.000000</td>
      <td>-0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>0.023046</td>
      <td>0.012661</td>
      <td>-0.003844</td>
      <td>0.053111</td>
      <td>0.059024</td>
      <td>0.101094</td>
      <td>0.018101</td>
      <td>0.062152</td>
      <td>-0.205401</td>
      <td>0.054649</td>
      <td>-0.588492</td>
    </tr>
    <tr>
      <th>temp_max</th>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>0.961573</td>
      <td>0.116839</td>
      <td>0.306414</td>
      <td>0.284582</td>
      <td>0.475197</td>
      <td>0.990269</td>
      <td>0.325282</td>
      <td>0.200772</td>
      <td>-0.012206</td>
      <td>0.044325</td>
    </tr>
    <tr>
      <th>temp_min</th>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>0.201817</td>
      <td>0.401052</td>
      <td>0.462011</td>
      <td>0.308483</td>
      <td>0.990414</td>
      <td>0.479028</td>
      <td>0.231321</td>
      <td>0.006385</td>
      <td>0.033592</td>
    </tr>
    <tr>
      <th>rain(mm)</th>
      <td>0.0</td>
      <td>-0.000000</td>
      <td>-0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>-0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>0.335441</td>
      <td>0.446553</td>
      <td>-0.285402</td>
      <td>0.161071</td>
      <td>0.436440</td>
      <td>0.043834</td>
      <td>0.051944</td>
      <td>0.028469</td>
    </tr>
    <tr>
      <th>humidity_max(%)</th>
      <td>0.0</td>
      <td>-0.000000</td>
      <td>-0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>0.638800</td>
      <td>-0.203655</td>
      <td>0.357428</td>
      <td>0.889034</td>
      <td>0.152004</td>
      <td>0.091800</td>
      <td>-0.036370</td>
    </tr>
    <tr>
      <th>humidity_min(%)</th>
      <td>0.0</td>
      <td>-0.000000</td>
      <td>0.000000</td>
      <td>-0.000000</td>
      <td>-0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>-0.435041</td>
      <td>0.377271</td>
      <td>0.920166</td>
      <td>0.238017</td>
      <td>0.167532</td>
      <td>-0.092435</td>
    </tr>
    <tr>
      <th>sunshine(MJ/m2)</th>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>-0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>-0.000000</td>
      <td>-0.000000</td>
      <td>-0.000000</td>
      <td>1.000000</td>
      <td>0.395349</td>
      <td>-0.362525</td>
      <td>-0.171376</td>
      <td>0.104532</td>
      <td>-0.042084</td>
    </tr>
    <tr>
      <th>temp_avg</th>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>0.406401</td>
      <td>0.218202</td>
      <td>-0.002920</td>
      <td>0.039209</td>
    </tr>
    <tr>
      <th>humidity_avg</th>
      <td>0.0</td>
      <td>-0.000000</td>
      <td>-0.000000</td>
      <td>-0.000000</td>
      <td>-0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>-0.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>0.218994</td>
      <td>0.146412</td>
      <td>-0.073515</td>
    </tr>
    <tr>
      <th>month</th>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>-0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>-0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>-0.000861</td>
      <td>0.275723</td>
    </tr>
    <tr>
      <th>year</th>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>-0.000000</td>
      <td>-0.000000</td>
      <td>0.000000</td>
      <td>-0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>-0.000000</td>
      <td>0.000000</td>
      <td>-0.000000</td>
      <td>1.000000</td>
      <td>-0.125410</td>
    </tr>
    <tr>
      <th>target</th>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>-0.000000</td>
      <td>-0.000000</td>
      <td>-0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>-0.000000</td>
      <td>-0.000000</td>
      <td>-0.000000</td>
      <td>0.000000</td>
      <td>-0.000000</td>
      <td>0.000000</td>
      <td>-0.000000</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>

![z_,min_2_2_2_26](https://github.com/zacinthepark/TIL/assets/86648892/129f17b3-cd40-4d07-b2bd-90ae1f7397db)

#### 2) 산점도

```python
def eda_2_nn(data, target, var, hue=''):

    plt.figure(figsize = (8,8))
    if hue == '' :
        sns.scatterplot(x=var, y=target, data=data)
        plt.grid()

    if hue != '' :
        sns.scatterplot(x=var, y=target, data=data, hue=hue)
        plt.grid()

    plt.show()
```

* ride_rate == ride_ratio

```python
eda_2_nn(data, 'target', 'ride_ratio')
```

![z_,min_2_2_2_27](https://github.com/zacinthepark/TIL/assets/86648892/a38767c8-24ef-4f45-ac61-0b5f627a4f88)

* fare == avg_rate

```python
eda_2_nn(data, 'target', 'avg_rate', 'weekday')
```

![z_,min_2_2_2_28](https://github.com/zacinthepark/TIL/assets/86648892/5bfc5cc3-3e63-4435-a3ae-b0c2828ec456)

### (2) 범주 feature --> Target

* 휴일 여부

```python
sns.barplot(x='holiday', y='target', data=data)
plt.xticks(ticks=[0, 1], labels=['not_holiday', 'holiday'])
plt.grid()
plt.show()
```

![z_,min_2_2_2_29](https://github.com/zacinthepark/TIL/assets/86648892/b958957c-d740-4e72-9b92-ebcc8ec17c48)

```python
# t-test
h0 = data.loc[data['holiday']==0, 'target']
h1 = data.loc[data['holiday']==1, 'target']
print(spst.ttest_ind(h0, h1))
```

<pre>
TtestResult(statistic=5.078160958101015, pvalue=4.0505005123594406e-07, df=2920.0)
</pre>

* 주말

```python
sns.barplot(x='weekend', y='target', data=data)
plt.xticks(ticks=[0, 1], labels=['not_weekend', 'weekend'])
plt.grid()
plt.show()
```

![z_,min_2_2_2_30](https://github.com/zacinthepark/TIL/assets/86648892/304d4f0b-b378-4f0d-a550-b8d2d52f07d5)

```python
# t-test
h0 = data.loc[data['weekend']==0, 'target']
h1 = data.loc[data['weekend']==1, 'target']
print(spst.ttest_ind(h0, h1))
```

<pre>
TtestResult(statistic=7.917032903397524, pvalue=3.42488756704735e-15, df=2920.0)
</pre>

* 주말 & 공휴일

```python
sns.barplot(x='weekend_holiday', y='target', data=data)
plt.xticks(ticks=[0, 1], labels=['not weekend and not holiday', 'weekend or holiday'])
plt.grid()
plt.show()
```

![z_,min_2_2_2_31](https://github.com/zacinthepark/TIL/assets/86648892/cc1a8804-c9d5-4c57-8027-5457b10fea99)

```python
# t-test
h0 = data.loc[data['weekend_holiday']==0, 'target']
h1 = data.loc[data['weekend_holiday']==1, 'target']
print(spst.ttest_ind(h0, h1))
```

<pre>
TtestResult(statistic=9.097885902310416, pvalue=1.6609595250008957e-19, df=2920.0)
</pre>

* 코로나

```python
sns.barplot(x='covid_19', y='target', data=data)
plt.xticks(ticks=[0, 1], labels=['not_covid', 'covid'])
plt.grid()
plt.show()
```

![z_,min_2_2_2_32](https://github.com/zacinthepark/TIL/assets/86648892/fcdb14b1-312b-48c3-8077-3df29a6c22de)

```python
# t-test
h0 = data.loc[data['covid_19']==0, 'target']
h1 = data.loc[data['covid_19']==1, 'target']
print(spst.ttest_ind(h0, h1))
```

<pre>
TtestResult(statistic=31.718933261457867, pvalue=5.512162412795066e-190, df=2920.0)
</pre>

* 요일

```python
sns.barplot(x='weekday', y='target', data=data)
plt.grid()
plt.show()
```

![z_,min_2_2_2_33](https://github.com/zacinthepark/TIL/assets/86648892/ca17951d-db15-44de-91fb-b462c4c8a9b6)

```python
# anova
temp = data.loc[data['weekday'].notnull()]

w0 = temp.loc[temp['weekday']=='Monday', 'target']
w1 = temp.loc[temp['weekday']=='Tuesday', 'target']
w2 = temp.loc[temp['weekday']=='Wednesday', 'target']
w3 = temp.loc[temp['weekday']=='Thursday', 'target']
w4 = temp.loc[temp['weekday']=='Friday', 'target']
w5 = temp.loc[temp['weekday']=='Saturday', 'target']
w6 = temp.loc[temp['weekday']=='Sunday', 'target']

print(spst.f_oneway(w0,w1,w2,w3,w4,w5,w6))
```

<pre>
F_onewayResult(statistic=15.668738200566109, pvalue=8.766163819661817e-18)
</pre>

* 계절

```python
sns.barplot(x='season', y='target', data=data)
plt.grid()
plt.show()
```

![z_,min_2_2_2_34](https://github.com/zacinthepark/TIL/assets/86648892/070eeff9-f71a-4060-a351-5798439458d9)

```python
# anova
temp = data.loc[data['season'].notnull()]

s0 = temp.loc[temp['season']=='Spring', 'target']
s1 = temp.loc[temp['season']=='Summer', 'target']
s2 = temp.loc[temp['season']=='Fall', 'target']
s3 = temp.loc[temp['season']=='Winter', 'target']

print(spst.f_oneway(s0,s1,s2,s3))
```

<pre>
F_onewayResult(statistic=34.73562423868687, pvalue=4.719868115759872e-22)
</pre>

```python
sns.lineplot(data=data, x='Date', y='avg_ride_distance')
plt.show()

sns.lineplot(data=data, x='Date', y='avg_rate')
plt.show()
```

![z_,min_2_2_2_35](https://github.com/zacinthepark/TIL/assets/86648892/9b47a846-39d7-4e70-9fa4-ddedf81efc99)

## 4.변수 정리

* Target과 관련성이 높은 feature와 그렇지 않은 feature를 정리합니다.
* 여기서의 판단은 다소 주관적입니다. 조금 정확하지 않아도 괜찮습니다.
* 다음 단계 모델링에서 관련이 적은 변수는 포함시키거나, 제외를 고려할때 활용합니다.

```python
print(data.info())
```

<pre>
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 2922 entries, 0 to 2921
Data columns (total 25 columns):
 #   Column              Non-Null Count  Dtype         
---  ------              --------------  -----         
 0   Date                2922 non-null   datetime64[ns]
 1   count_taxi          2922 non-null   int64         
 2   receipt             2922 non-null   int64         
 3   boarding            2922 non-null   int64         
 4   avg_rate            2922 non-null   int64         
 5   avg_ride_distance   2922 non-null   int64         
 6   target              2922 non-null   float64       
 7   temp_max            2922 non-null   float64       
 8   temp_min            2922 non-null   float64       
 9   rain(mm)            2922 non-null   float64       
 10  humidity_max(%)     2922 non-null   float64       
 11  humidity_min(%)     2922 non-null   float64       
 12  sunshine(MJ/m2)     2922 non-null   float64       
 13  weekday             2922 non-null   category      
 14  month               2922 non-null   int32         
 15  season              2922 non-null   category      
 16  year                2922 non-null   int32         
 17  weekend             2922 non-null   category      
 18  covid_19            2922 non-null   category      
 19  holiday             2922 non-null   category      
 20  day7_avg_wait_time  2922 non-null   float64       
 21  ride_ratio          2922 non-null   float64       
 22  temp_avg            2922 non-null   float64       
 23  humidity_avg        2922 non-null   float64       
 24  weekend_holiday     2922 non-null   category      
dtypes: category(6), datetime64[ns](1), float64(11), int32(2), int64(5)
memory usage: 429.2 KB
None
</pre>

* **강한 관계의 변수**

    - 'day7_avg_wait_time': 7일 간 운행 평균 (0.84)
    - 'ride_ratio': 탑승률 (-0.59)
    - 'covid_19': 코로나 발생 시점 ~ 집합 금지, 집합 금지 ~ 사회적 거리두기, 그 이후로 3분류
    - 'holiday', 'weekend_holiday', 'weekday_Saturday', 'weekday_Sunday', 'rainyday (차후 추가)'


* **중간(약한) 관계의 변수**

    - 'receipt': 접수 건수 (0.32)
    - 'boarding': 탑승 건수 (0.23)
    - 'month': 월 (0.28)
    - 'weekend', 'weekday_Monday', 'weekday_Tuesday', 'weekday_Wednesday', 'weekday_Thursday', 'weekday_Friday': 평일의 요일 간 차이는 없다고 보고 평일/토요일/일요일로 나눔

* **(거의) 관계가 없는 변수**

    - 'season_Spring', 'season_Summer', 'season_Fall', 'season_Winter': 날씨 정보와 상관없이 '달'로 구분했기 때문에 관계가 적다고 생각함
    - 'sunshine(MJ/m2)'

## 5.데이터 저장

* joblib.dump를 이용하여 저장합시다.
* 저장할 파일 이름 : data2.pkl

```python
# joblib.dump(data, 'data2_1.pkl')
```
