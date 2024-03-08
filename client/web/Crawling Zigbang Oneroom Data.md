## Zigbang 원룸 매물 데이터 수집

```python
import requests
import pandas as pd
```

#### Process

- 동이름으로 위도 경도 구하기
- 위도 경도로 geohash 알아내기 (geohash는 위도 경도 바탕으로 만든 영역 표시 코드값)
- geohash로 매물 아이디 가져오기
- 매물 아이디로 매물 정보 가져오기

### 1. 동이름으로 위도 경도 구하기

```python
# 망원동으로 검색해서 나온 URL 정보를 Headers에서 확인
# URL Decoder/Encoder를 통해 인코딩된 URL을 디코딩하여 확인
addr = "망원동"
url = f"https://apis.zigbang.com/v2/search?leaseYn=N&q={addr}&serviceType=원룸"
response = requests.get(url)
data = response.json()["items"][0]
lat, lng = data["lat"], data["lng"]
lat, lng
```

<pre>
(37.556785583496094, 126.9013442993164)
</pre>

### 2. 위도 경도로 geohash 알아내기

```python
# install geohash2
# !pip install geohash2
```

```python
import geohash2
```

```python
# precision이 커질수록 영역이 작아짐
geohash = geohash2.encode(lat, lng, precision=5)
geohash
```

<pre>
'wydjx'
</pre>

### 3. geohash로 매물 아이디 가져오기

```python
url = f"https://apis.zigbang.com/v2/items/oneroom\
?geohash={geohash}&depositMin=0&rentMin=0&salesTypes[0]=전세&salesTypes[1]=월세\
&domain=zigbang&checkAnyItemWithoutFilter=true"
response = requests.get(url)
response
```

<pre>
<Response [200]>
</pre>

```python
items = response.json()["items"]
# len(items), items[0]
ids = [item["itemId"] for item in items]
len(ids), ids[:5]
```

<pre>
(603, [39817840, 40042434, 40058332, 39791961, 40096518])
</pre>

### 4. 매물 아이디로 매물 정보 가져오기

```python
# 1000개 넘어가면 나눠서 수집해야 함
url = "https://apis.zigbang.com/v2/items/list"
# Payload에서 확인
params = {
    "domain": "zigbang", 
    "item_ids": ids
}
response = requests.post(url, params)
response
```

<pre>
<Response [200]>
</pre>

```python
pd.options.display.max_columns = 40
```

```python
datas = response.json()["items"]
df = pd.DataFrame(datas)
df.tail()
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>item_id</th>
      <th>section_type</th>
      <th>images_thumbnail</th>
      <th>sales_type</th>
      <th>sales_title</th>
      <th>deposit</th>
      <th>rent</th>
      <th>size_m2</th>
      <th>공급면적</th>
      <th>전용면적</th>
      <th>계약면적</th>
      <th>room_type_title</th>
      <th>floor</th>
      <th>floor_string</th>
      <th>building_floor</th>
      <th>title</th>
      <th>is_first_movein</th>
      <th>room_type</th>
      <th>status</th>
      <th>tags</th>
      <th>service_type</th>
      <th>random_location</th>
      <th>manage_cost</th>
      <th>reg_date</th>
      <th>is_new</th>
      <th>addressOrigin</th>
      <th>action</th>
      <th>contract</th>
      <th>address</th>
      <th>is_zzim</th>
      <th>address1</th>
      <th>address2</th>
      <th>address3</th>
      <th>item_bm_type</th>
      <th>zikim</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>598</th>
      <td>39903982</td>
      <td>None</td>
      <td>https://ic.zigbang.com/ic/items/39903982/78104...</td>
      <td>월세</td>
      <td>월세</td>
      <td>3000</td>
      <td>95</td>
      <td>78.94</td>
      <td>{'m2': 78.94, 'p': '23.9'}</td>
      <td>{'m2': 31.37, 'p': '9.5'}</td>
      <td>None</td>
      <td>None</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>내부 올수리 완료, 깨끗하고 깔끔한 투룸</td>
      <td>None</td>
      <td>04</td>
      <td>True</td>
      <td>[]</td>
      <td>빌라</td>
      <td>{'lat': 37.56799169336686, 'lng': 126.91091894...</td>
      <td>0</td>
      <td>2024-03-06T11:22:53+09:00</td>
      <td>False</td>
      <td>{'local1': '서울시', 'local2': '마포구', 'local3': '...</td>
      <td>{'isRead': False, 'readAt': None, 'isInquired'...</td>
      <td></td>
      <td>마포구 중동</td>
      <td>False</td>
      <td>서울시 마포구 중동</td>
      <td>None</td>
      <td>None</td>
      <td>PARTNERS</td>
      <td>{'hasVrKey': False}</td>
    </tr>
    <tr>
      <th>599</th>
      <td>40071706</td>
      <td>None</td>
      <td>https://ic.zigbang.com/ic/items/40071706/1.jpg</td>
      <td>월세</td>
      <td>월세</td>
      <td>3000</td>
      <td>95</td>
      <td>31.40</td>
      <td>{'m2': 31.4, 'p': '9.5'}</td>
      <td>{'m2': 31.4, 'p': '9.5'}</td>
      <td>None</td>
      <td>None</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>올리모델링 옵션O 깔끔 투룸</td>
      <td>None</td>
      <td>04</td>
      <td>True</td>
      <td>[]</td>
      <td>빌라</td>
      <td>{'lat': 37.567994390023806, 'lng': 126.9115616...</td>
      <td>0</td>
      <td>2024-03-05T17:01:25+09:00</td>
      <td>False</td>
      <td>{'local1': '서울시', 'local2': '마포구', 'local3': '...</td>
      <td>{'isRead': False, 'readAt': None, 'isInquired'...</td>
      <td></td>
      <td>마포구 중동</td>
      <td>False</td>
      <td>서울시 마포구 중동</td>
      <td>None</td>
      <td>None</td>
      <td>ZIGBANG</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>600</th>
      <td>40104629</td>
      <td>None</td>
      <td>https://ic.zigbang.com/ic/items/40104629/78676...</td>
      <td>전세</td>
      <td>전세</td>
      <td>18400</td>
      <td>0</td>
      <td>39.30</td>
      <td>{'m2': 39.3, 'p': '11.9'}</td>
      <td>{'m2': 35.34, 'p': '10.7'}</td>
      <td>None</td>
      <td>None</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>우드 디자인의 아늑한 투룸, 즉시 입주 가능</td>
      <td>None</td>
      <td>04</td>
      <td>True</td>
      <td>[]</td>
      <td>빌라</td>
      <td>{'lat': 37.56807917020881, 'lng': 126.90982816...</td>
      <td>0</td>
      <td>2024-03-08T10:37:31+09:00</td>
      <td>True</td>
      <td>{'local1': '서울시', 'local2': '마포구', 'local3': '...</td>
      <td>{'isRead': False, 'readAt': None, 'isInquired'...</td>
      <td></td>
      <td>마포구 성산동</td>
      <td>False</td>
      <td>서울시 마포구 성산동</td>
      <td>None</td>
      <td>None</td>
      <td>PARTNERS</td>
      <td>{'hasVrKey': False}</td>
    </tr>
    <tr>
      <th>601</th>
      <td>40104877</td>
      <td>None</td>
      <td>https://ic.zigbang.com/ic/items/40104877/1.jpg</td>
      <td>월세</td>
      <td>월세</td>
      <td>14600</td>
      <td>20</td>
      <td>35.34</td>
      <td>{'m2': 35.34, 'p': '10.7'}</td>
      <td>{'m2': 35.34, 'p': '10.7'}</td>
      <td>None</td>
      <td>None</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>보증보험가능 투룸 대출가능 주택가 컨디션좋음 베란다o</td>
      <td>None</td>
      <td>04</td>
      <td>True</td>
      <td>[]</td>
      <td>빌라</td>
      <td>{'lat': 37.56805172167567, 'lng': 126.90918905...</td>
      <td>0</td>
      <td>2024-03-08T10:45:49+09:00</td>
      <td>True</td>
      <td>{'local1': '서울시', 'local2': '마포구', 'local3': '...</td>
      <td>{'isRead': False, 'readAt': None, 'isInquired'...</td>
      <td></td>
      <td>마포구 성산동</td>
      <td>False</td>
      <td>서울시 마포구 성산동</td>
      <td>None</td>
      <td>None</td>
      <td>ZIGBANG</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>602</th>
      <td>39976664</td>
      <td>None</td>
      <td>https://ic.zigbang.com/ic/items/39976664/1.jpg</td>
      <td>전세</td>
      <td>전세</td>
      <td>36500</td>
      <td>0</td>
      <td>41.79</td>
      <td>{'m2': 41.79, 'p': '12.6'}</td>
      <td>{'m2': 41.79, 'p': '12.6'}</td>
      <td>None</td>
      <td>None</td>
      <td>3</td>
      <td>3</td>
      <td>6</td>
      <td>가좌역도보2분거리호재지역신축3룸전세</td>
      <td>None</td>
      <td>05</td>
      <td>True</td>
      <td>[]</td>
      <td>빌라</td>
      <td>{'lat': 37.569321334104906, 'lng': 126.9092469...</td>
      <td>5</td>
      <td>2024-02-27T11:08:28+09:00</td>
      <td>False</td>
      <td>{'local1': '서울시', 'local2': '마포구', 'local3': '...</td>
      <td>{'isRead': False, 'readAt': None, 'isInquired'...</td>
      <td></td>
      <td>마포구 중동</td>
      <td>False</td>
      <td>서울시 마포구 중동</td>
      <td>None</td>
      <td>None</td>
      <td>ZIGBANG</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>

```python
df.columns
```

<pre>
Index(['item_id', 'section_type', 'images_thumbnail', 'sales_type',
       'sales_title', 'deposit', 'rent', 'size_m2', '공급면적', '전용면적', '계약면적',
       'room_type_title', 'floor', 'floor_string', 'building_floor', 'title',
       'is_first_movein', 'room_type', 'status', 'tags', 'service_type',
       'random_location', 'manage_cost', 'reg_date', 'is_new', 'addressOrigin',
       'action', 'contract', 'address', 'is_zzim', 'address1', 'address2',
       'address3', 'item_bm_type', 'zikim'],
      dtype='object')
</pre>

```python
# 필요한 컬럼만 필터링
columns = ["item_id", "sales_type", "deposit", "rent", "size_m2", "floor", "building_floor",
           "address1", "manage_cost"]
filtered_column_df = df[columns]
filtered_column_df.tail()
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>item_id</th>
      <th>sales_type</th>
      <th>deposit</th>
      <th>rent</th>
      <th>size_m2</th>
      <th>floor</th>
      <th>building_floor</th>
      <th>address1</th>
      <th>manage_cost</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>598</th>
      <td>39903982</td>
      <td>월세</td>
      <td>3000</td>
      <td>95</td>
      <td>78.94</td>
      <td>1</td>
      <td>2</td>
      <td>서울시 마포구 중동</td>
      <td>0</td>
    </tr>
    <tr>
      <th>599</th>
      <td>40071706</td>
      <td>월세</td>
      <td>3000</td>
      <td>95</td>
      <td>31.40</td>
      <td>1</td>
      <td>2</td>
      <td>서울시 마포구 중동</td>
      <td>0</td>
    </tr>
    <tr>
      <th>600</th>
      <td>40104629</td>
      <td>전세</td>
      <td>18400</td>
      <td>0</td>
      <td>39.30</td>
      <td>2</td>
      <td>2</td>
      <td>서울시 마포구 성산동</td>
      <td>0</td>
    </tr>
    <tr>
      <th>601</th>
      <td>40104877</td>
      <td>월세</td>
      <td>14600</td>
      <td>20</td>
      <td>35.34</td>
      <td>2</td>
      <td>2</td>
      <td>서울시 마포구 성산동</td>
      <td>0</td>
    </tr>
    <tr>
      <th>602</th>
      <td>39976664</td>
      <td>전세</td>
      <td>36500</td>
      <td>0</td>
      <td>41.79</td>
      <td>3</td>
      <td>6</td>
      <td>서울시 마포구 중동</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>

```python
# 주소에 망원동이 있는 데이터만 필터링
result_df = filtered_column_df[filtered_column_df["address1"].str.contains("망원동")]
result_df = result_df.reset_index(drop=True)
result_df.tail()
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>item_id</th>
      <th>sales_type</th>
      <th>deposit</th>
      <th>rent</th>
      <th>size_m2</th>
      <th>floor</th>
      <th>building_floor</th>
      <th>address1</th>
      <th>manage_cost</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>57</th>
      <td>39591216</td>
      <td>전세</td>
      <td>45000</td>
      <td>0</td>
      <td>99.20</td>
      <td>3</td>
      <td>5</td>
      <td>서울시 마포구 망원동</td>
      <td>5</td>
    </tr>
    <tr>
      <th>58</th>
      <td>39677924</td>
      <td>월세</td>
      <td>41000</td>
      <td>10</td>
      <td>68.68</td>
      <td>7</td>
      <td>7</td>
      <td>서울시 마포구 망원동</td>
      <td></td>
    </tr>
    <tr>
      <th>59</th>
      <td>40099714</td>
      <td>전세</td>
      <td>43000</td>
      <td>0</td>
      <td>68.68</td>
      <td>7</td>
      <td>7</td>
      <td>서울시 마포구 망원동</td>
      <td>7</td>
    </tr>
    <tr>
      <th>60</th>
      <td>40009046</td>
      <td>월세</td>
      <td>500</td>
      <td>50</td>
      <td>13.22</td>
      <td>2</td>
      <td>3</td>
      <td>서울시 마포구 망원동</td>
      <td>7</td>
    </tr>
    <tr>
      <th>61</th>
      <td>40089526</td>
      <td>월세</td>
      <td>200</td>
      <td>63</td>
      <td>16.53</td>
      <td>반지하</td>
      <td>3</td>
      <td>서울시 마포구 망원동</td>
      <td>7</td>
    </tr>
  </tbody>
</table>
</div>
