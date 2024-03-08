### Crawling Gmarket Best and Image Data

- 베스트 상품 200개 데이터 수집
- 상품의 이미지 200개 다운로드

```python
import pandas as pd
import requests
from bs4 import BeautifulSoup
```

#### 1. URL 찾기

```python
url = "https://www.gmarket.co.kr/n/best"
```

#### 2. request > response : str(html)

```python
response = requests.get(url)
response
```

```
<Response [200]>
```

#### 3. bs > DataFrame

```python
dom = BeautifulSoup(response.text, "html.parser")
```

```python
# select 200 items
# 첫번째 상품 Chrome -> Copy -> Copy selector
# '#gBestWrap > div.best-list > ul > li:nth-child(1)'
elements = dom.select("#gBestWrap > div.best-list > ul > li")
len(elements)
```

<pre>
200
</pre>

```python
element = elements[0]
```

```python
# select item data
data = {
    "title": element.select_one(".itemname").text,
    "link": element.select_one(".itemname").get("href"),
    # "img": element.select_one("img").get("data-original"),
    "img": 'https:'+ element.select_one("img.image__lazy").get("src"),
    # element.select_one(".o-price").text: 정가36,100원
    "o_price": element.select_one(".o-price").text[2:-1].replace(',', ''),
    # element.select_one(".s-price").text: 할인가10,830원 70%
    "s_price": element.select_one(".s-price").text.split(' ')[0][3:-1].replace(',', ''),
    "dc": element.select_one(".s-price").text.split(' ')[1][:3]
}
data
```

<pre>
{'title': '[출판사 블루래빗]LEGO  사이언스 스타트 2종(판타스틱 머신 + 기어 봇) 선택구매',
 'link': 'http://item.gmarket.co.kr/Item?goodscode=2498713345&ver=20240308',
 'img': 'https://gdimg.gmarket.co.kr/2498713345/still/300?ver=1680482283',
 'o_price': '29000',
 's_price': '13800',
 'dc': '52%'}
</pre>

```python
# make DataFrame
datas = []
for element in elements:
    datas.append({
        "title": element.select_one(".itemname").text,
    "link": element.select_one(".itemname").get("href"),
    # "img": element.select_one("img").get("data-original"),
    "img": 'https:'+ element.select_one("img.image__lazy").get("src"),
    # element.select_one(".o-price").text: 정가36,100원
    "o_price": element.select_one(".o-price").text[2:-1].replace(',', ''),
    # element.select_one(".s-price").text: 할인가10,830원 70%
    "s_price": element.select_one(".s-price").text.split(' ')[0][3:-1].replace(',', ''),
    "dc": element.select_one(".s-price").text.split(' ')[1][:3]
    })
df = pd.DataFrame(datas)
df.head()
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>link</th>
      <th>img</th>
      <th>o_price</th>
      <th>s_price</th>
      <th>dc</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>[출판사 블루래빗]LEGO  사이언스 스타트 2종(판타스틱 머신 + 기어 봇) 선택구매</td>
      <td>http://item.gmarket.co.kr/Item?goodscode=24987...</td>
      <td>https://gdimg.gmarket.co.kr/2498713345/still/3...</td>
      <td>29000</td>
      <td>13800</td>
      <td>52%</td>
    </tr>
    <tr>
      <th>1</th>
      <td>[캘리포니아골드뉴트리션](아이허브) 2개X오메가800 피쉬오일 EPA/DHA 80%...</td>
      <td>http://item.gmarket.co.kr/Item?goodscode=29045...</td>
      <td>https://gdimg.gmarket.co.kr/2904551502/still/3...</td>
      <td>67800</td>
      <td>60970</td>
      <td>10%</td>
    </tr>
    <tr>
      <th>2</th>
      <td>[3M]베이킹소다 크린스틱 리필 5+5입 2개(총20입)</td>
      <td>http://item.gmarket.co.kr/Item?goodscode=16063...</td>
      <td>https://gdimg.gmarket.co.kr/1606351005/still/3...</td>
      <td>38800</td>
      <td>18900</td>
      <td>51%</td>
    </tr>
    <tr>
      <th>3</th>
      <td>[디스커버리]공용 소매포인트 맨투맨 DXMT3A031</td>
      <td>http://item.gmarket.co.kr/Item?goodscode=34913...</td>
      <td>https://gdimg.gmarket.co.kr/3491347053/still/3...</td>
      <td>53400</td>
      <td>37920</td>
      <td>28%</td>
    </tr>
    <tr>
      <th>4</th>
      <td>[CGV](CGV) G마켓 예매권 (금요특가_3/8)</td>
      <td>http://item.gmarket.co.kr/Item?goodscode=35742...</td>
      <td>https://gdimg.gmarket.co.kr/3574247932/still/3...</td>
      <td>15000</td>
      <td>9980</td>
      <td>33%</td>
    </tr>
  </tbody>
</table>
</div>

#### to_excel

```python
# df.to_excel("g_items.xlsx", index=False, engine="openpyxl")
```

```python
# 4. download image
```

```python
# 디렉토리 생성
import os

if not os.path.exists("data"):           
    os.makedirs("data")
```

```python
%ls data
```

<pre>
 C 드라이브의 볼륨에는 이름이 없습니다.
 볼륨 일련 번호: FCA9-41A6

 C:\Users\User\kt_ai_crawling\data 디렉터리

2024-03-08  오후 04:08    <DIR>          .
2024-03-08  오후 04:08    <DIR>          ..
               0개 파일                   0 바이트
               2개 디렉터리  168,766,259,200 바이트 남음
</pre>

```python
# 파일 리스트 출력
os.listdir("data")
```

<pre>
[]
</pre>

```python
img_link = df.loc[0, "img"]
print(img_link)
```

```
https://gdimg.gmarket.co.kr/2498713345/still/300?ver=1680482283
```

#### download image

```python
response = requests.get(img_link)
response
```

```
<Response [200]>
```

```python
# wb : write binary, 이진 형태로 파일 쓰기
with open("data/test.png", "wb") as file:
    file.write(response.content)
```

```python
os.listdir("data")
```

<pre>
['test.png']
</pre>

```python
# pillow 패키지 : 이미지 전처리
from PIL import Image as pil
```

```python
pil.open("data/test.png")
```

![z_gmarket_1](https://github.com/zacinthepark/TIL/assets/86648892/9ac306e4-b117-4516-a6f8-299c25bdb911)

```python
# 5개의 아이템 이미지 다운로드
for idx, data in df[:5].iterrows():
    # print(idx, data["s_price"], data["img"])
    response = requests.get(data["img"])
    filename = f'data/{idx}.png'
    with open(filename, "wb") as file:
        file.write(response.content)
```

```python
os.listdir("data")
```

<pre>
['0.png', '1.png', '2.png', '3.png', '4.png', 'test.png']
</pre>

```python
pil.open("data/4.png")
```

![z_gmarket_2](https://github.com/zacinthepark/TIL/assets/86648892/2b62f9fd-875c-48c8-9ca9-44c500ecd17b)

```python
# 디렉토리 삭제
import shutil
shutil.rmtree("data")
```
