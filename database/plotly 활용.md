## plotly 활용

---

- Plotly의 graph_objects 패키지
    - graph_objects 패키지를 이용하면 섬세하게 그래프를 그릴 수 있음
    - `Figure`: 객체 생성
    - `add_traces`: 그래프 생성
    - `update_layout`: 레이아웃 설정

### graph_objects

- graph_objects는 Plotly의 인기 있는 데이터 시각화 모듈로, 3D 형태의 그래프를 포함한 다양한 그래프를 그릴 수 있음
- go라는 별칭 이용하여 호출

### go 그리는 방법

- `fig=go.Figure()`: Figure 객체 생성
- `fig.add_traces(그래프)`: add_traces로 원하는 유형의 그래프 추가 (go의 그래프 유형 설정)
- `fig.update_layout(옵션)`: 레이아웃 설정
    - 대표적인 옵션: title, yaxis_title 등

### 실습

#### Candlestick 주식 차트 만들기

```python
import plotly.graph_objects as go

import pandas as pd
import numpy as np
```

```python
# 주식 데이터 로딩
df = pd.read_csv('./data/fake_stock_price.csv', index_col=0)
display(df)
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Open</th>
      <th>High</th>
      <th>Low</th>
      <th>Close</th>
      <th>Volume</th>
    </tr>
    <tr>
      <th>Date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2018-04-13</th>
      <td>25.860001</td>
      <td>25.879999</td>
      <td>25.639999</td>
      <td>25.780001</td>
      <td>2060800.0</td>
    </tr>
    <tr>
      <th>2018-04-16</th>
      <td>25.799999</td>
      <td>26.270000</td>
      <td>25.740000</td>
      <td>26.110001</td>
      <td>2045400.0</td>
    </tr>
    <tr>
      <th>2018-04-17</th>
      <td>26.170000</td>
      <td>26.480000</td>
      <td>26.170000</td>
      <td>26.410000</td>
      <td>1464500.0</td>
    </tr>
    <tr>
      <th>2018-04-18</th>
      <td>26.410000</td>
      <td>26.639999</td>
      <td>26.309999</td>
      <td>26.309999</td>
      <td>980300.0</td>
    </tr>
    <tr>
      <th>2018-04-19</th>
      <td>26.260000</td>
      <td>26.370001</td>
      <td>25.820000</td>
      <td>25.920000</td>
      <td>1358700.0</td>
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
      <th>2020-03-26</th>
      <td>26.280001</td>
      <td>28.500000</td>
      <td>25.410000</td>
      <td>28.000000</td>
      <td>3431300.0</td>
    </tr>
    <tr>
      <th>2020-03-27</th>
      <td>26.410000</td>
      <td>28.760000</td>
      <td>25.740000</td>
      <td>28.049999</td>
      <td>2480900.0</td>
    </tr>
    <tr>
      <th>2020-03-30</th>
      <td>27.240000</td>
      <td>27.540001</td>
      <td>25.430000</td>
      <td>26.590000</td>
      <td>3668000.0</td>
    </tr>
    <tr>
      <th>2020-03-31</th>
      <td>26.230000</td>
      <td>26.740000</td>
      <td>25.059999</td>
      <td>26.540001</td>
      <td>5236300.0</td>
    </tr>
    <tr>
      <th>2020-04-01</th>
      <td>25.000000</td>
      <td>25.260000</td>
      <td>23.709999</td>
      <td>24.540001</td>
      <td>3460100.0</td>
    </tr>
  </tbody>
</table>
<p>496 rows × 5 columns</p>
</div>

```python
# 인덱스 확인
df.index
```

<pre>
Index(['2018-04-13', '2018-04-16', '2018-04-17', '2018-04-18', '2018-04-19',
       '2018-04-20', '2018-04-23', '2018-04-24', '2018-04-25', '2018-04-26',
       ...
       '2020-03-19', '2020-03-20', '2020-03-23', '2020-03-24', '2020-03-25',
       '2020-03-26', '2020-03-27', '2020-03-30', '2020-03-31', '2020-04-01'],
      dtype='object', name='Date', length=496)
</pre>

```python
df.index = pd.to_datetime(df.index)
df
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Open</th>
      <th>High</th>
      <th>Low</th>
      <th>Close</th>
      <th>Volume</th>
    </tr>
    <tr>
      <th>Date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2018-04-13</th>
      <td>25.860001</td>
      <td>25.879999</td>
      <td>25.639999</td>
      <td>25.780001</td>
      <td>2060800.0</td>
    </tr>
    <tr>
      <th>2018-04-16</th>
      <td>25.799999</td>
      <td>26.270000</td>
      <td>25.740000</td>
      <td>26.110001</td>
      <td>2045400.0</td>
    </tr>
    <tr>
      <th>2018-04-17</th>
      <td>26.170000</td>
      <td>26.480000</td>
      <td>26.170000</td>
      <td>26.410000</td>
      <td>1464500.0</td>
    </tr>
    <tr>
      <th>2018-04-18</th>
      <td>26.410000</td>
      <td>26.639999</td>
      <td>26.309999</td>
      <td>26.309999</td>
      <td>980300.0</td>
    </tr>
    <tr>
      <th>2018-04-19</th>
      <td>26.260000</td>
      <td>26.370001</td>
      <td>25.820000</td>
      <td>25.920000</td>
      <td>1358700.0</td>
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
      <th>2020-03-26</th>
      <td>26.280001</td>
      <td>28.500000</td>
      <td>25.410000</td>
      <td>28.000000</td>
      <td>3431300.0</td>
    </tr>
    <tr>
      <th>2020-03-27</th>
      <td>26.410000</td>
      <td>28.760000</td>
      <td>25.740000</td>
      <td>28.049999</td>
      <td>2480900.0</td>
    </tr>
    <tr>
      <th>2020-03-30</th>
      <td>27.240000</td>
      <td>27.540001</td>
      <td>25.430000</td>
      <td>26.590000</td>
      <td>3668000.0</td>
    </tr>
    <tr>
      <th>2020-03-31</th>
      <td>26.230000</td>
      <td>26.740000</td>
      <td>25.059999</td>
      <td>26.540001</td>
      <td>5236300.0</td>
    </tr>
    <tr>
      <th>2020-04-01</th>
      <td>25.000000</td>
      <td>25.260000</td>
      <td>23.709999</td>
      <td>24.540001</td>
      <td>3460100.0</td>
    </tr>
  </tbody>
</table>
<p>496 rows × 5 columns</p>
</div>

```python
df.index
```

<pre>
DatetimeIndex(['2018-04-13', '2018-04-16', '2018-04-17', '2018-04-18',
               '2018-04-19', '2018-04-20', '2018-04-23', '2018-04-24',
               '2018-04-25', '2018-04-26',
               ...
               '2020-03-19', '2020-03-20', '2020-03-23', '2020-03-24',
               '2020-03-25', '2020-03-26', '2020-03-27', '2020-03-30',
               '2020-03-31', '2020-04-01'],
              dtype='datetime64[ns]', name='Date', length=496, freq=None)
</pre>

#### plotly의 graph_objects

```python
# Figure 객체 생성
fig = go.Figure()
```

```python
# fig 출력
print(fig)
```

<pre>
Figure({
    'data': [], 'layout': {'template': '...'}
})
</pre>

```python
fig
```

<img width="852" alt="plotly1" src="https://github.com/zacinthepark/TIL/assets/86648892/858f69e3-6a2d-4afe-a1c2-9087ba032b33">

#### `add_trace`: 캔들스틱 차트 구현

```python
# add_trace는 fig 안에 무엇인가를 채울 때 사용
fig.add_trace(
    go.Candlestick(
        x=df.index, # x축은 날짜로 표기
        open=df.Open, # 시초가
        high=df.High, # 고가
        low=df.Low, # 저가
        close=df.Close, # 종가
        increasing_line_color='red', # 주가 상승 빨강
        decreasing_line_color='blue' # 주가 하락 파랑
    ))
```

<img width="845" alt="plotly2" src="https://github.com/zacinthepark/TIL/assets/86648892/1da79883-a663-40ad-bffd-799494439a0c">

#### `update_layout`: 그래프 레이아웃 설정

```python
print(fig)
```

<pre>
Figure({
    'data': [{'close': array([25.78000069, 26.11000061, 26.40999985, ..., 26.59000015, 26.54000092,
                              24.54000092]),
              'decreasing': {'line': {'color': 'blue'}},
              'high': array([25.87999916, 26.27000046, 26.47999954, ..., 27.54000092, 26.73999977,
                             25.26000023]),
              'increasing': {'line': {'color': 'red'}},
              'low': array([25.63999939, 25.73999977, 26.17000008, ..., 25.43000031, 25.05999947,
                            23.70999908]),
              'open': array([25.86000061, 25.79999924, 26.17000008, ..., 27.23999977, 26.22999954,
                             25.        ]),
              'type': 'candlestick',
              'x': array([datetime.datetime(2018, 4, 13, 0, 0),
                          datetime.datetime(2018, 4, 16, 0, 0),
                          datetime.datetime(2018, 4, 17, 0, 0), ...,
                          datetime.datetime(2020, 3, 30, 0, 0),
                          datetime.datetime(2020, 3, 31, 0, 0),
                          datetime.datetime(2020, 4, 1, 0, 0)], dtype=object)},
             {'close': array([25.78000069, 26.11000061, 26.40999985, ..., 26.59000015, 26.54000092,
                              24.54000092]),
              'decreasing': {'line': {'color': 'blue'}},
              'high': array([25.87999916, 26.27000046, 26.47999954, ..., 27.54000092, 26.73999977,
                             25.26000023]),
              'increasing': {'line': {'color': 'red'}},
              'low': array([25.63999939, 25.73999977, 26.17000008, ..., 25.43000031, 25.05999947,
                            23.70999908]),
              'open': array([25.86000061, 25.79999924, 26.17000008, ..., 27.23999977, 26.22999954,
                             25.        ]),
              'type': 'candlestick',
              'x': array([datetime.datetime(2018, 4, 13, 0, 0),
                          datetime.datetime(2018, 4, 16, 0, 0),
                          datetime.datetime(2018, 4, 17, 0, 0), ...,
                          datetime.datetime(2020, 3, 30, 0, 0),
                          datetime.datetime(2020, 3, 31, 0, 0),
                          datetime.datetime(2020, 4, 1, 0, 0)], dtype=object)},
             {'close': array([25.78000069, 26.11000061, 26.40999985, ..., 26.59000015, 26.54000092,
                              24.54000092]),
              'decreasing': {'line': {'color': 'blue'}},
              'high': array([25.87999916, 26.27000046, 26.47999954, ..., 27.54000092, 26.73999977,
                             25.26000023]),
              'increasing': {'line': {'color': 'red'}},
              'low': array([25.63999939, 25.73999977, 26.17000008, ..., 25.43000031, 25.05999947,
                            23.70999908]),
              'open': array([25.86000061, 25.79999924, 26.17000008, ..., 27.23999977, 26.22999954,
                             25.        ]),
              'type': 'candlestick',
              'x': array([datetime.datetime(2018, 4, 13, 0, 0),
                          datetime.datetime(2018, 4, 16, 0, 0),
                          datetime.datetime(2018, 4, 17, 0, 0), ...,
                          datetime.datetime(2020, 3, 30, 0, 0),
                          datetime.datetime(2020, 3, 31, 0, 0),
                          datetime.datetime(2020, 4, 1, 0, 0)], dtype=object)},
             {'close': array([25.78000069, 26.11000061, 26.40999985, ..., 26.59000015, 26.54000092,
                              24.54000092]),
              'decreasing': {'line': {'color': 'blue'}},
              'high': array([25.87999916, 26.27000046, 26.47999954, ..., 27.54000092, 26.73999977,
                             25.26000023]),
              'increasing': {'line': {'color': 'red'}},
              'low': array([25.63999939, 25.73999977, 26.17000008, ..., 25.43000031, 25.05999947,
                            23.70999908]),
              'open': array([25.86000061, 25.79999924, 26.17000008, ..., 27.23999977, 26.22999954,
                             25.        ]),
              'type': 'candlestick',
              'x': array([datetime.datetime(2018, 4, 13, 0, 0),
                          datetime.datetime(2018, 4, 16, 0, 0),
                          datetime.datetime(2018, 4, 17, 0, 0), ...,
                          datetime.datetime(2020, 3, 30, 0, 0),
                          datetime.datetime(2020, 3, 31, 0, 0),
                          datetime.datetime(2020, 4, 1, 0, 0)], dtype=object)}],
    'layout': {'template': '...'}
})
</pre>

```python
# Figure 객체를 최초 생성 시 data에 대한 값을 주는 방법으로 캔들스틱을 구현할 수 있음
# plotly의 layout은 다양하기에 보다 간편하게 update_layout 메서드로 업데이트

fig = go.Figure(
    data=[go.Candlestick(
        x=df.index, # x축은 날짜로 표기
        open=df.Open, # 시초가
        high=df.High, # 고가
        low=df.Low, # 저가
        close=df.Close, # 종가
        increasing_line_color='red', # 주가 상승 빨강
        decreasing_line_color='blue' # 주가 하락 파랑
    )]
)

fig.show()
```

<img width="850" alt="plotly3" src="https://github.com/zacinthepark/TIL/assets/86648892/cc6a5fb9-7c0e-452a-b81c-8ee4b19cd2a2">

```python
# graph_objects의 그래프에 타이틀과 축 레이블을 표기하는 방법 -> update_layout 사용
fig.update_layout(title='Stock Price of XXX (OHLC, $)', 
                  yaxis_title='$'
                 )

fig.layout.height = 600  # figure의 크기 설정 (너비는 width로 가능)
fig.show()
```

<img width="855" alt="plotly4" src="https://github.com/zacinthepark/TIL/assets/86648892/18c4bdda-7e9f-431c-a378-6ca446a356e5">

```python
# 주가 그래프에 많이 들어가는 이동 평균선 생성 (Moving Average)
# 종가를 이용한 MA
ma_3 = df.Close.rolling(3).mean()
ma_10 = df.Close.rolling(10).mean()
ma_30 = df.Close.rolling(30).mean()
```

```python
df['MA3'] = ma_3
df['MA10'] = ma_10
df['MA30'] = ma_30
```

```python
display(df)
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Open</th>
      <th>High</th>
      <th>Low</th>
      <th>Close</th>
      <th>Volume</th>
      <th>MA3</th>
      <th>MA10</th>
      <th>MA30</th>
    </tr>
    <tr>
      <th>Date</th>
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
      <th>2018-04-13</th>
      <td>25.860001</td>
      <td>25.879999</td>
      <td>25.639999</td>
      <td>25.780001</td>
      <td>2060800.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2018-04-16</th>
      <td>25.799999</td>
      <td>26.270000</td>
      <td>25.740000</td>
      <td>26.110001</td>
      <td>2045400.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2018-04-17</th>
      <td>26.170000</td>
      <td>26.480000</td>
      <td>26.170000</td>
      <td>26.410000</td>
      <td>1464500.0</td>
      <td>26.100000</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2018-04-18</th>
      <td>26.410000</td>
      <td>26.639999</td>
      <td>26.309999</td>
      <td>26.309999</td>
      <td>980300.0</td>
      <td>26.276667</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2018-04-19</th>
      <td>26.260000</td>
      <td>26.370001</td>
      <td>25.820000</td>
      <td>25.920000</td>
      <td>1358700.0</td>
      <td>26.213333</td>
      <td>NaN</td>
      <td>NaN</td>
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
      <th>2020-03-26</th>
      <td>26.280001</td>
      <td>28.500000</td>
      <td>25.410000</td>
      <td>28.000000</td>
      <td>3431300.0</td>
      <td>26.450000</td>
      <td>22.456</td>
      <td>34.413333</td>
    </tr>
    <tr>
      <th>2020-03-27</th>
      <td>26.410000</td>
      <td>28.760000</td>
      <td>25.740000</td>
      <td>28.049999</td>
      <td>2480900.0</td>
      <td>27.386667</td>
      <td>22.612</td>
      <td>33.891333</td>
    </tr>
    <tr>
      <th>2020-03-30</th>
      <td>27.240000</td>
      <td>27.540001</td>
      <td>25.430000</td>
      <td>26.590000</td>
      <td>3668000.0</td>
      <td>27.546666</td>
      <td>23.371</td>
      <td>33.300333</td>
    </tr>
    <tr>
      <th>2020-03-31</th>
      <td>26.230000</td>
      <td>26.740000</td>
      <td>25.059999</td>
      <td>26.540001</td>
      <td>5236300.0</td>
      <td>27.060000</td>
      <td>24.234</td>
      <td>32.701333</td>
    </tr>
    <tr>
      <th>2020-04-01</th>
      <td>25.000000</td>
      <td>25.260000</td>
      <td>23.709999</td>
      <td>24.540001</td>
      <td>3460100.0</td>
      <td>25.890001</td>
      <td>25.201</td>
      <td>32.056333</td>
    </tr>
  </tbody>
</table>
<p>496 rows × 8 columns</p>
</div>

```python
# moving average (이동 평균을 라인 그래프로 표현)

ma3 = go.Scatter(
    x=df.index, 
    y=df.MA3, 
    line=dict(color='black', width=0.5), 
    name='MA(3)'
)

ma10 = go.Scatter(
    x=df.index, 
    y=df.MA10, 
    line=dict(color='red', width=0.8), 
    name='MA(10)'
)

ma30 = go.Scatter(
    x=df.index, 
    y=df.MA30, 
    line=dict(color='green', width=1), 
    name='MA(30)'
)
```

```python
# 생성한 scatter plot을 fig 객체에 추가
fig.add_traces(ma3)
fig.show()
```

<img width="852" alt="plotly5" src="https://github.com/zacinthepark/TIL/assets/86648892/695c1ccc-a4e0-4ec0-a983-ac1078f4233f">

```python
fig.add_traces(ma10)
fig.add_traces(ma30)
fig.show()
```

<img width="856" alt="plotly6" src="https://github.com/zacinthepark/TIL/assets/86648892/85db3d72-c8a2-47d8-a580-dcabffd8518c">

##### Bollinger Bands 추가

볼린저 밴드는 주가의 변동이 표준정규분포를 따른다고 가정하고, 주가의 추세를 따라 위아래로 폭이 같이 움직이는 밴드를 만들어 주가를 그 밴드 기준선으로 판단하고자 만들어진 지표입니다.

볼린저 밴드를 만드는 다양한 방법이 있지만, 원리는 동일하며 생각보다 간단합니다.

1. 기준선을 구해야합니다. 본 실습에선 기준선을 이미 계산한 `ma30`으로 설정하겠습니다.
2. 기준선에 대응하는 표준편차를 구해야합니다. `df.Close.rolling(30).std`
3. 상한선 = 기준선 + (2 * 표준편차)
4. 하한선 = 기준선 - (2 * 표준편차)

```python
# 표준편차 구하기
std_30 = df.Close.rolling(30).std()
```

```python
df['STD30'] = std_30
```

```python
# Bollinger Bands 그리기

# 상한선
upper_bound = go.Scatter(
    x=df.index, 
    y=df.MA30 + (df.STD30 * 2), 
    line=dict(dash='dash', color='gray', width=1), 
    name='upper bounds'
)

# 하한선
lower_bound = go.Scatter(
    x=df.index, 
    y=df.MA30 - (df.STD30 * 2), 
    line=dict(dash='dash', color='gray', width=1), 
    fill='tonexty', # 상한선과 하한선 사이 면적 채우기
    opacity=0.5, # 투명도 조절
    name='lower bounds'
)
```

```python
# 캔들스틱에 상한선, 하한선 추가
fig.add_traces([upper_bound, lower_bound])
```

<img width="856" alt="plotly7" src="https://github.com/zacinthepark/TIL/assets/86648892/9b1d648f-6d5a-4e65-92c3-6462b4e3de40">

#### 바 그래프: 거래량 추가

```python
# 거래량을 나타내는 trading_volume의 바 플롯
trading_volume = go.Bar(x=df.index, y=df.Volume)
```

```python
import plotly.subplots as ms  # 거래량 바그래프 추가를 위해 plotly의 subplots 패키지 로딩
```

```python
# (2x1) Axes를 갖고 있는 figure 생성
fig = ms.make_subplots(rows=2, 
                       cols=1, 
                       shared_xaxes=True, # x축 값 공유
                       # vertical_spacing=0.02, 
                       subplot_titles=('Stock Prices of XXX ($)', 'Trading Volumes')
                      )
```

```python
fig
```

<img width="850" alt="plotly8" src="https://github.com/zacinthepark/TIL/assets/86648892/254fcda5-0dd4-4808-8a09-36837c1fd87a">

```python
# 캔들스틱 그래프 추가
# subplots에서는 add_trace
# 1행 1열에 추가
fig.add_trace(
    go.Candlestick(
        x=df.index, 
        open=df.Open, 
        high=df.High, 
        low=df.Low, 
        close=df.Close, 
        increasing_line_color='red', 
        decreasing_line_color='blue'
    ), 
    row=1, 
    col=1
)

# figure 높이 설정
fig.layout.height = 600
fig.show()
```

<img width="852" alt="plotly9" src="https://github.com/zacinthepark/TIL/assets/86648892/53e4fe76-891a-40eb-b2a2-7770aaacd419">

```python
# 이동평균선 추가 (1행 1열 그래프에 추가)
fig.add_trace(ma3, row=1, col=1)
fig.add_trace(ma10, row=1, col=1)
fig.add_trace(ma30, row=1, col=1)
fig.show()
```

<img width="856" alt="plotly10" src="https://github.com/zacinthepark/TIL/assets/86648892/6f67f279-2ee2-47ba-bad2-260d27240847">

```python
# 볼린저 라인 추가
fig.add_trace(upper_bound, row=1, col=1)  # 상한선
fig.add_trace(lower_bound, row=1, col=1)  # 하한선
```

<img width="857" alt="plotly11" src="https://github.com/zacinthepark/TIL/assets/86648892/cfd68260-18f5-4911-ad92-ad5b033632a7">

```python
# 거래량 추가 2행 1열 (두번째 그래프)에 추가
fig.add_trace(trading_volume, row=2, col=1)
fig.show()
```

<img width="854" alt="plotly12" src="https://github.com/zacinthepark/TIL/assets/86648892/25be270b-c98f-40b6-9e9c-16279c98fd8d">

```python
# figure 레이아웃 설정
fig.update_layout(
    yaxis1_title='Stock Price ($)', # 첫번째 캔들스틱에 대한 y축 레이블
    yaxis2_title='Trading Volumes', # 두번째 트레이딩 바 차트에 대한 y축 레이블
    xaxis2_title='Periods', # 두번째 그래프 x축 레이블
    xaxis1_rangeslider_visible=False, # 첫번째 그래프 레인지 슬라이더 숨김
    xaxis2_rangeslider_visible=True # 두번째 그래프 레인지 슬라이더 활성화
)

fig.show()
```

<img width="857" alt="plotly13" src="https://github.com/zacinthepark/TIL/assets/86648892/f43ed50a-556e-41f6-b3b8-9b7477dc3d5e">

```python
# 동적인 요소를 녹여내어 저장하고 싶을 때
fig.write_html('./data/interactive_candle_stick.html')
```
