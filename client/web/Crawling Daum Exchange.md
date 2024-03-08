### Crawling Daum Exchange

- `https://finance.daum.net`

```python
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import requests
```

```python
# request를 보내면 Headers 내 User-Agent에 요청 송신자 정보가 들어감
# python으로 요청을 보내면 User-Agent가 python이 되는데, 특정 사이트들은 이런 경우 요청이 불가하도록 막음
# User-Agent 정보를 바꾸는 것이 안될 때에는 selenium 사용

# 1. URL
url = "https://finance.daum.net/api/exchanges/summaries"

# 2. Header 설정
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'Referer': 'https://finance.daum.net',
}

# Response (JSON)
response = requests.get(url, headers=headers)
response
```

<pre>
<Response [200]>
</pre>

```python
# JSON Parsing
datas = response.json()["data"]

# DataFrame
df = pd.DataFrame(datas)
df.head(10)
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>symbolCode</th>
      <th>date</th>
      <th>currencyCode</th>
      <th>currencyName</th>
      <th>currencyUnit</th>
      <th>country</th>
      <th>region</th>
      <th>name</th>
      <th>recurrenceCount</th>
      <th>basePrice</th>
      <th>...</th>
      <th>changeRate</th>
      <th>cashBuyingPrice</th>
      <th>cashSellingPrice</th>
      <th>ttBuyingPrice</th>
      <th>ttSellingPrice</th>
      <th>tcBuyingPrice</th>
      <th>fcSellingPrice</th>
      <th>exchangeCommission</th>
      <th>usDollarRate</th>
      <th>chartImageUrl</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>FRX.KRWUSD</td>
      <td>2024-03-08 13:12:55</td>
      <td>USD</td>
      <td>달러</td>
      <td>1</td>
      <td>미국</td>
      <td>{'korName': '아메리카', 'engName': 'America'}</td>
      <td>미국 (USD/KRW)</td>
      <td>268</td>
      <td>1321.50</td>
      <td>...</td>
      <td>0.003394</td>
      <td>1344.62</td>
      <td>1298.38</td>
      <td>1308.60</td>
      <td>1334.40</td>
      <td>None</td>
      <td>None</td>
      <td>7.1677</td>
      <td>1.0000</td>
      <td>{'day': 'https://t1.daumcdn.net/finance/chart/...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>FRX.KRWJPY</td>
      <td>2024-03-08 13:12:55</td>
      <td>JPY</td>
      <td>엔</td>
      <td>100</td>
      <td>일본</td>
      <td>{'korName': '아시아', 'engName': 'Asia'}</td>
      <td>일본 (JPY100/KRW)</td>
      <td>268</td>
      <td>894.02</td>
      <td>...</td>
      <td>0.001775</td>
      <td>909.66</td>
      <td>878.38</td>
      <td>885.26</td>
      <td>902.78</td>
      <td>None</td>
      <td>None</td>
      <td>2.0505</td>
      <td>0.6765</td>
      <td>{'day': 'https://t1.daumcdn.net/finance/chart/...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>FRX.KRWCNY</td>
      <td>2024-03-08 13:12:55</td>
      <td>CNY</td>
      <td>위안</td>
      <td>1</td>
      <td>중국</td>
      <td>{'korName': '아시아', 'engName': 'Asia'}</td>
      <td>중국 (CNY/KRW)</td>
      <td>268</td>
      <td>183.53</td>
      <td>...</td>
      <td>0.003475</td>
      <td>192.70</td>
      <td>174.36</td>
      <td>181.70</td>
      <td>185.36</td>
      <td>None</td>
      <td>None</td>
      <td>5.1412</td>
      <td>0.1389</td>
      <td>{'day': 'https://t1.daumcdn.net/finance/chart/...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>FRX.KRWEUR</td>
      <td>2024-03-08 13:12:55</td>
      <td>EUR</td>
      <td>유로</td>
      <td>1</td>
      <td>유로</td>
      <td>{'korName': '유럽', 'engName': 'Europe'}</td>
      <td>유로 (EUR/KRW)</td>
      <td>268</td>
      <td>1446.78</td>
      <td>...</td>
      <td>0.003437</td>
      <td>1475.57</td>
      <td>1417.99</td>
      <td>1432.32</td>
      <td>1461.24</td>
      <td>None</td>
      <td>None</td>
      <td>5.8400</td>
      <td>1.0948</td>
      <td>{'day': 'https://t1.daumcdn.net/finance/chart/...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>FRX.KRWGBP</td>
      <td>2024-03-08 13:12:55</td>
      <td>GBP</td>
      <td>파운드</td>
      <td>1</td>
      <td>영국</td>
      <td>{'korName': '유럽', 'engName': 'Europe'}</td>
      <td>영국 (GBP/KRW)</td>
      <td>268</td>
      <td>1692.71</td>
      <td>...</td>
      <td>0.003509</td>
      <td>1726.05</td>
      <td>1659.37</td>
      <td>1675.79</td>
      <td>1709.63</td>
      <td>None</td>
      <td>None</td>
      <td>7.2943</td>
      <td>1.2809</td>
      <td>{'day': 'https://t1.daumcdn.net/finance/chart/...</td>
    </tr>
    <tr>
      <th>5</th>
      <td>FRX.KRWCHF</td>
      <td>2024-03-08 13:12:55</td>
      <td>CHF</td>
      <td>프랑</td>
      <td>1</td>
      <td>스위스</td>
      <td>{'korName': '유럽', 'engName': 'Europe'}</td>
      <td>스위스 (CHF/KRW)</td>
      <td>268</td>
      <td>1505.98</td>
      <td>...</td>
      <td>0.003454</td>
      <td>1535.64</td>
      <td>1476.32</td>
      <td>1490.93</td>
      <td>1521.03</td>
      <td>None</td>
      <td>None</td>
      <td>3.7520</td>
      <td>1.1396</td>
      <td>{'day': 'https://t1.daumcdn.net/finance/chart/...</td>
    </tr>
    <tr>
      <th>6</th>
      <td>FRX.KRWCAD</td>
      <td>2024-03-08 13:12:55</td>
      <td>CAD</td>
      <td>달러</td>
      <td>1</td>
      <td>캐나다</td>
      <td>{'korName': '아메리카', 'engName': 'America'}</td>
      <td>캐나다 (CAD/KRW)</td>
      <td>268</td>
      <td>982.67</td>
      <td>...</td>
      <td>0.002801</td>
      <td>1002.02</td>
      <td>963.32</td>
      <td>972.85</td>
      <td>992.49</td>
      <td>None</td>
      <td>None</td>
      <td>7.0230</td>
      <td>0.7436</td>
      <td>{'day': 'https://t1.daumcdn.net/finance/chart/...</td>
    </tr>
    <tr>
      <th>7</th>
      <td>FRX.KRWNZD</td>
      <td>2024-03-08 13:12:55</td>
      <td>NZD</td>
      <td>달러</td>
      <td>1</td>
      <td>뉴질랜드</td>
      <td>{'korName': '아시아', 'engName': 'Asia'}</td>
      <td>뉴질랜드 (NZD/KRW)</td>
      <td>268</td>
      <td>816.03</td>
      <td>...</td>
      <td>0.003395</td>
      <td>832.10</td>
      <td>799.96</td>
      <td>807.87</td>
      <td>824.19</td>
      <td>None</td>
      <td>None</td>
      <td>7.5257</td>
      <td>0.6175</td>
      <td>{'day': 'https://t1.daumcdn.net/finance/chart/...</td>
    </tr>
    <tr>
      <th>8</th>
      <td>FRX.KRWHKD</td>
      <td>2024-03-08 13:12:55</td>
      <td>HKD</td>
      <td>달러</td>
      <td>1</td>
      <td>홍콩</td>
      <td>{'korName': '아시아', 'engName': 'Asia'}</td>
      <td>홍콩 (HKD/KRW)</td>
      <td>268</td>
      <td>168.99</td>
      <td>...</td>
      <td>0.003303</td>
      <td>172.31</td>
      <td>165.67</td>
      <td>167.31</td>
      <td>170.67</td>
      <td>None</td>
      <td>None</td>
      <td>6.5010</td>
      <td>0.1279</td>
      <td>{'day': 'https://t1.daumcdn.net/finance/chart/...</td>
    </tr>
    <tr>
      <th>9</th>
      <td>FRX.KRWBRL</td>
      <td>2024-03-08 13:12:55</td>
      <td>BRL</td>
      <td>레알</td>
      <td>1</td>
      <td>브라질</td>
      <td>{'korName': '아메리카', 'engName': 'America'}</td>
      <td>브라질 (BRL/KRW)</td>
      <td>268</td>
      <td>267.75</td>
      <td>...</td>
      <td>0.003647</td>
      <td>295.06</td>
      <td>240.98</td>
      <td>264.54</td>
      <td>0.00</td>
      <td>None</td>
      <td>None</td>
      <td>11.0030</td>
      <td>0.2026</td>
      <td>{'day': 'https://t1.daumcdn.net/finance/chart/...</td>
    </tr>
  </tbody>
</table>
<p>10 rows × 22 columns</p>
</div>

```python
columns = ["date", "currencyCode", "currencyName", "country", "name", "basePrice"]
df[columns].head()
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>currencyCode</th>
      <th>currencyName</th>
      <th>country</th>
      <th>name</th>
      <th>basePrice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2024-03-08 13:12:55</td>
      <td>USD</td>
      <td>달러</td>
      <td>미국</td>
      <td>미국 (USD/KRW)</td>
      <td>1321.50</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2024-03-08 13:12:55</td>
      <td>JPY</td>
      <td>엔</td>
      <td>일본</td>
      <td>일본 (JPY100/KRW)</td>
      <td>894.02</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2024-03-08 13:12:55</td>
      <td>CNY</td>
      <td>위안</td>
      <td>중국</td>
      <td>중국 (CNY/KRW)</td>
      <td>183.53</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2024-03-08 13:12:55</td>
      <td>EUR</td>
      <td>유로</td>
      <td>유로</td>
      <td>유로 (EUR/KRW)</td>
      <td>1446.78</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2024-03-08 13:12:55</td>
      <td>GBP</td>
      <td>파운드</td>
      <td>영국</td>
      <td>영국 (GBP/KRW)</td>
      <td>1692.71</td>
    </tr>
  </tbody>
</table>
</div>
