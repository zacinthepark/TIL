### Crawling Naver Stock Data

- 네이버 증권 사이트에서 주가 데이터 수집

- 수집할 데이터 : 일별 kospi, kosdaq 주가, 일별 환율(exchange rate) 데이터

- 데이터 수집 절차

    - 웹서비스 분석 : url

    - 서버에 데이터 요청 : request(url) > response : json(str)

    - 서버에서 받은 데이터 파싱(데이터 형태를 변경) : json(str) > list, dict > DataFrame

```python
import warnings
warnings.filterwarnings('ignore')  # 경고 문구 출력 X
import pandas as pd
import requests
```

#### 1. 웹서비스 분석 : url

- pc 웹페이지가 복잡하면 mobile 웹페이지에서 수집

```python
# https://m.stock.naver.com/domestic/index/KOSPI/total
# Network 탭 -> Fetch/XHR -> price 관련 트래픽 확인 -> Response 탭 정보 확인
# 210.89.168.68.443 -> https 기본 포트 443번
# Payload 탭에서 request 괸련 정보를 더 편하게 볼 수 있음

page, page_size = 1, 60
url = f'https://m.stock.naver.com/api/index/KOSPI/price?pageSize={page_size}&page={page}'
print(url)
```

<pre>
https://m.stock.naver.com/api/index/KOSPI/price?pageSize=60&page=1
</pre>

#### 2. 서버에 데이터 요청 : request(url) > response : json(str)

- response의 status code가 200이 나오는지 확인

- 403이나 500이 나오면 request가 잘못되거나 web server에서 수집이 안되도록 설정이 된것임

    - header 설정 또는 selenium 사용

- 200이 나오더라도 response 안에 있는 내용을 확인 > 확인하는 방법 : response.text

```python
response = requests.get(url)
response
```

<pre>
<Response [200]>
</pre>

```python
response.text[:200]
```

<pre>
'[{"localTradedAt":"2024-03-08","closePrice":"2,671.19","compareToPreviousClosePrice":"23.57","compareToPreviousPrice":{"code":"2","text":"상승","name":"RISING"},"fluctuationsRatio":"0.89","openPrice":"2'
</pre>

#### 3. 서버에서 받은 데이터 파싱(데이터 형태를 변경) : json(str) > list, dict > DataFrame

```python
columns = ["localTradedAt", "closePrice"]
data = response.json()
kospi_df = pd.DataFrame(data)[columns]
kospi_df.head(10)
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>localTradedAt</th>
      <th>closePrice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2024-03-08</td>
      <td>2,671.19</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2024-03-07</td>
      <td>2,647.62</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2024-03-06</td>
      <td>2,641.49</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2024-03-05</td>
      <td>2,649.40</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2024-03-04</td>
      <td>2,674.27</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2024-02-29</td>
      <td>2,642.36</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2024-02-28</td>
      <td>2,652.29</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2024-02-27</td>
      <td>2,625.05</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2024-02-26</td>
      <td>2,647.08</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2024-02-23</td>
      <td>2,667.70</td>
    </tr>
  </tbody>
</table>
</div>

#### 4. 함수로 만들기

```python
def stock_price(code="KOSPI", page=1, page_size=60):
    # 1. 웹 서비스 분석 : URL
    """ This function is crwaling stock price from naver stock web page
    parameters :
        code : str : KOSPI or KOSDAQ
        page : int : page number
        page_size : int : one page size
    return :
        type : DataFame of pandas"""
    url = f'https://m.stock.naver.com/api/index/{code}/price?pageSize={page_size}&page={page}'

    # 2. request(URL) > response(JSON) : JSON(str)
    response = requests.get(url)

    # 3. JSON(str) > list, dict > DataFrame : Data
    columns = ["localTradedAt", "closePrice"]
    data = response.json()
    return pd.DataFrame(data)[columns]
```

```python
help(stock_price)
```

<pre>
Help on function stock_price in module __main__:

stock_price(code='KOSPI', page=1, page_size=60)
    This function is crwaling stock price from naver stock web page
    parameters :
        code : str : KOSPI or KOSDAQ
        page : int : page number
        page_size : int : one page size
    return :
        type : DataFame of pandas

</pre>

```python
kospi_df = stock_price()
kospi_df.head(10)
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>localTradedAt</th>
      <th>closePrice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2024-03-08</td>
      <td>2,671.19</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2024-03-07</td>
      <td>2,647.62</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2024-03-06</td>
      <td>2,641.49</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2024-03-05</td>
      <td>2,649.40</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2024-03-04</td>
      <td>2,674.27</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2024-02-29</td>
      <td>2,642.36</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2024-02-28</td>
      <td>2,652.29</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2024-02-27</td>
      <td>2,625.05</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2024-02-26</td>
      <td>2,647.08</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2024-02-23</td>
      <td>2,667.70</td>
    </tr>
  </tbody>
</table>
</div>

```python
kosdaq_df = stock_price("KOSDAQ")
kosdaq_df.tail(10)
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>localTradedAt</th>
      <th>closePrice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>50</th>
      <td>2023-12-21</td>
      <td>859.44</td>
    </tr>
    <tr>
      <th>51</th>
      <td>2023-12-20</td>
      <td>862.98</td>
    </tr>
    <tr>
      <th>52</th>
      <td>2023-12-19</td>
      <td>858.30</td>
    </tr>
    <tr>
      <th>53</th>
      <td>2023-12-18</td>
      <td>850.96</td>
    </tr>
    <tr>
      <th>54</th>
      <td>2023-12-15</td>
      <td>838.31</td>
    </tr>
    <tr>
      <th>55</th>
      <td>2023-12-14</td>
      <td>840.59</td>
    </tr>
    <tr>
      <th>56</th>
      <td>2023-12-13</td>
      <td>829.31</td>
    </tr>
    <tr>
      <th>57</th>
      <td>2023-12-12</td>
      <td>839.53</td>
    </tr>
    <tr>
      <th>58</th>
      <td>2023-12-11</td>
      <td>835.25</td>
    </tr>
    <tr>
      <th>59</th>
      <td>2023-12-08</td>
      <td>830.37</td>
    </tr>
  </tbody>
</table>
</div>

#### 5. 원달러 환율 데이터 수집 : 실습

```python
def exchage_rate(code="FX_USDKRW", page=1, page_size=60):
    url = f'https://m.stock.naver.com/front-api/v1/marketIndex/prices?page={page}\
&category=exchange&reutersCode={code}&pageSize={page_size}'
    response = requests.get(url)
    columns = ["localTradedAt", "closePrice"]
    data = response.json()['result']
    return pd.DataFrame(data)[columns]
```

```python
usd_df = exchage_rate()
usd_df.head(10)
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>localTradedAt</th>
      <th>closePrice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2024-03-08</td>
      <td>1,321.50</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2024-03-07</td>
      <td>1,328.50</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2024-03-06</td>
      <td>1,333.50</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2024-03-05</td>
      <td>1,335.00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2024-03-04</td>
      <td>1,333.00</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2024-02-29</td>
      <td>1,336.00</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2024-02-28</td>
      <td>1,336.00</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2024-02-27</td>
      <td>1,332.00</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2024-02-26</td>
      <td>1,332.00</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2024-02-23</td>
      <td>1,332.50</td>
    </tr>
  </tbody>
</table>
</div>

#### 6. 시각화

```python
%matplotlib inline
%config InlineBackend.figure_formats = {'png', 'retina'}
```

```python
import matplotlib.pyplot as plt
import seaborn as sns
```

```python
# 데이터 수집
page_size = 60
kospi_df = stock_price("KOSPI", page_size=page_size)
kosdaq_df = stock_price("KOSDAQ", page_size=page_size)
usd_df = exchage_rate("FX_USDKRW", page_size=page_size)
```

```python
# 데이터 전처리 1 : 데이터 타입 변경
print(kospi_df.dtypes)
kospi_df["kospi"] = kospi_df["closePrice"].apply(lambda data: float(data.replace(",", "")))
kospi_df = kospi_df.drop(columns=["closePrice"])
print(kospi_df.dtypes)
```

<pre>
localTradedAt    object
closePrice       object
dtype: object
localTradedAt     object
kospi            float64
dtype: object
</pre>

```python
kosdaq_df["kosdaq"] = kosdaq_df["closePrice"].apply(lambda data: float(data.replace(",", "")))
usd_df["usd"] = usd_df["closePrice"].apply(lambda data: float(data.replace(",", "")))
```

```python
kosdaq_df = kosdaq_df.drop(columns=["closePrice"])
usd_df = usd_df.drop(columns=["closePrice"])
```

```python
# 데이터 전처리 2 : 날짜 데이터 맞추기 : merge
```

```python
merge_df_1 = pd.merge(kospi_df, kosdaq_df, on="localTradedAt")
merge_df_2 = pd.merge(merge_df_1, usd_df, on="localTradedAt")
merge_df = merge_df_2.copy()
merge_df.head(10)
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>localTradedAt</th>
      <th>kospi</th>
      <th>kosdaq</th>
      <th>usd</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2024-03-08</td>
      <td>2671.19</td>
      <td>868.56</td>
      <td>1321.5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2024-03-07</td>
      <td>2647.62</td>
      <td>863.37</td>
      <td>1328.5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2024-03-06</td>
      <td>2641.49</td>
      <td>870.67</td>
      <td>1333.5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2024-03-05</td>
      <td>2649.40</td>
      <td>866.37</td>
      <td>1335.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2024-03-04</td>
      <td>2674.27</td>
      <td>872.97</td>
      <td>1333.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2024-02-29</td>
      <td>2642.36</td>
      <td>862.96</td>
      <td>1336.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2024-02-28</td>
      <td>2652.29</td>
      <td>863.39</td>
      <td>1336.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2024-02-27</td>
      <td>2625.05</td>
      <td>853.75</td>
      <td>1332.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2024-02-26</td>
      <td>2647.08</td>
      <td>867.40</td>
      <td>1332.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2024-02-23</td>
      <td>2667.70</td>
      <td>868.57</td>
      <td>1332.5</td>
    </tr>
  </tbody>
</table>
</div>

```python
# 시각화
plt.figure(figsize=(20, 5))

# plt.plot(merge_df["localTradedAt"], merge_df["kospi"], label="kospi")
# plt.plot(merge_df["localTradedAt"], merge_df["kosdaq"], label="kosdaq")
# plt.plot(merge_df["localTradedAt"], merge_df["usd"], label="usd")

columns = merge_df.columns[1:]
for column in columns:
    plt.plot(merge_df["localTradedAt"], merge_df[column], label=column)
    
xticks_count = 11
plt.xticks(merge_df["localTradedAt"][::int(len(merge_df) // xticks_count) + 1])
plt.legend(loc=0)
plt.show()
```

![naver_stock_data_1](https://github.com/zacinthepark/TIL/assets/86648892/1160cb04-e026-42f6-acb2-480a525e709a)

#### 7. 데이터 스케일링

- min max scaling: 최소값은 0, 최대값은 1의 형태로 표현

- $z = \frac{x_i - min(x)}{max(x) - min(x)} (0 \leqq z \leqq 1)$

- latex syntax : `https://jjycjnmath.tistory.com/117`

```python
from sklearn.preprocessing import minmax_scale
```

```python
# 시각화
plt.figure(figsize=(20, 5))

columns = merge_df.columns[1:]
for column in columns:
    plt.plot(merge_df["localTradedAt"], minmax_scale(merge_df[column]), label=column)
    
xticks_count = 11
plt.xticks(merge_df["localTradedAt"][::int(len(merge_df) // xticks_count) + 1])
plt.legend(loc=0)
plt.show()
```

![naver_stock_data_2](https://github.com/zacinthepark/TIL/assets/86648892/9458c58d-5408-4fae-8cd8-ba1398b61f85)

#### 8. 상관관계 분석

- 피어슨 상관계수(Pearson Correlation Coefficient)

- 두 데이터 집합의 상관도를 분석할때 사용되는 지표

- 상관계수의 해석

    - -1에 가까울수록 서로 반대방향으로 움직임
    - 1에 가까울수록 서로 같은방향으로 움직임
    - 0에 가까울수록 두 데이터는 관계가 없음

```python
# 해석 1 : kospi, kosdaq은 아주 강한 양의 상관관계를 갖는다. (데이터가 같은 방향으로 움직임)
# 해석 2 : kospi와 usd를 강한 음의 상관관계를 갖는다. (데이터가 반대 방향으로 움직임)
corr_df = merge_df[merge_df.columns[1:]].corr()
corr_df
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>kospi</th>
      <th>kosdaq</th>
      <th>usd</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>kospi</th>
      <td>1.000000</td>
      <td>0.466090</td>
      <td>-0.157069</td>
    </tr>
    <tr>
      <th>kosdaq</th>
      <td>0.466090</td>
      <td>1.000000</td>
      <td>-0.294285</td>
    </tr>
    <tr>
      <th>usd</th>
      <td>-0.157069</td>
      <td>-0.294285</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>

```python
# 결정계수 : r-squared 
# 1과 가까울수록 강한 관계, 0과 가까울수록 약한 관계
plt.figure(figsize=(20, 5))
sns.heatmap(corr_df**2, cmap="YlGnBu", annot=True)
plt.show()
```

![naver_stock_data_3](https://github.com/zacinthepark/TIL/assets/86648892/537a460c-548c-4956-981b-695573810418)
