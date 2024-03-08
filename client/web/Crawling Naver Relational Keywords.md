### Crawling Naver Relational Keywords

- 정적(static) 웹페이지 데이터 수집 
- BeautifulSoup을 이용하여 HTML 문자열 데이터 parsing

```python
import pandas as pd
import requests
# html 포맷의 데이터를 css-selector를 이용하여 필요한 데이터 추출
from bs4 import BeautifulSoup
```

#### 1. 웹페이지 분석 : URL

```python
query = "삼성전자"
url = f"https://search.naver.com/search.naver?query={query}"  # 간소화된 url
print(url)
```

<pre>
https://search.naver.com/search.naver?query=삼성전자
</pre>

#### 2. request(URL) > response : str(html)

```python
response = requests.get(url)
response
```

```
<Response [200]>
```

```python
response.text[:100]
```

```
'<!doctype html> <html lang="ko"><head> <meta charset="utf-8"> <meta name="referrer" content="always"'
```

#### 3. str(html) > bs object

```python
dom = BeautifulSoup(response.text, "html.parser")
type(dom)
```

<pre>
bs4.BeautifulSoup
</pre>

#### 4. bs object > .select(css-selector), .select_one(css-selector) > str(text)

```python
# 10개의 엘리먼트들 선택
# .select() : list(Tag, Tag) : 엘리먼트 여러개 선택 : 결과 > 리스트(태그 객체 여러개)
# .select_one() : Tag : 엘리먼트 한개 선택 : 결과 > 태그 객체 한개

# <li>의 클래스 .item만 len을 찍어보면 10개보다 많이 나와서 추가적인 조건 설정 필요
# 상위 <ul>의 클래스 : lst_related_srch _list_box (2개의 클래스가 공백을 두고 적용됨)
# 앞의 클래스만 가져오기
elements = dom.select(".lst_related_srch > .item")
len(elements)
```

<pre>
10
</pre>

```python
element = elements[0]

# 1
element.text.strip()

# 2
# keyword = element.select_one(".tit").text
# keyword
```

<pre>
'삼성전자주가'
</pre>

```python
keywords = [element.text.strip() for element in elements]
keywords
```

<pre>
['삼성전자주가',
 '삼성전자주식',
 '삼성전자 배당금',
 '오늘 삼성전자 주가',
 '삼성전자서비스',
 '삼성전자서비스센타',
 '삼성전자주가지수',
 '삼성전자주식가격',
 '삼성 전자레인지',
 '삼성전자 패밀리몰']
</pre>

```python
link = element.select_one("a").get("href")
link
```

<pre>
'?where=nexearch&ssc=tab.nx.all&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90%EC%A3%BC%EA%B0%80&sm=tab_she&qdt=0'
</pre>

```python
# 각각의 엘리먼트에서 text 데이터 수집
```

```python
keywords = []
for element in elements:
    keyword = element.text.strip()
    keywords.append(keyword)
print(keywords)
```

<pre>
['삼성전자주가', '삼성전자주식', '삼성전자 배당금', '오늘 삼성전자 주가', '삼성전자서비스', '삼성전자서비스센타', '삼성전자주가지수', '삼성전자주식가격', '삼성 전자레인지', '삼성전자 패밀리몰']
</pre>

```python
keywords = [element.text.strip() for element in elements]
print(keywords)
```

<pre>
['삼성전자주가', '삼성전자주식', '삼성전자 배당금', '오늘 삼성전자 주가', '삼성전자서비스', '삼성전자서비스센타', '삼성전자주가지수', '삼성전자주식가격', '삼성 전자레인지', '삼성전자 패밀리몰']
</pre>

#### 5. str(text) > DataFrame

```python
df = pd.DataFrame({"keywords": keywords})
df["query"] = query
df.head()
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>keywords</th>
      <th>query</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>삼성전자주가</td>
      <td>삼성전자</td>
    </tr>
    <tr>
      <th>1</th>
      <td>삼성전자주식</td>
      <td>삼성전자</td>
    </tr>
    <tr>
      <th>2</th>
      <td>삼성전자 배당금</td>
      <td>삼성전자</td>
    </tr>
    <tr>
      <th>3</th>
      <td>오늘 삼성전자 주가</td>
      <td>삼성전자</td>
    </tr>
    <tr>
      <th>4</th>
      <td>삼성전자서비스</td>
      <td>삼성전자</td>
    </tr>
  </tbody>
</table>
</div>

#### 현재 시간 데이터 추가

```python
from datetime import datetime
```

```python
now = datetime.now()
now = now.strftime("%Y-%m-%d %H:%M")
now
```

<pre>
'2024-03-08 16:33'
</pre>

```python
df["date_time"] = now
df.head()
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>keywords</th>
      <th>query</th>
      <th>date_time</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>삼성전자주가</td>
      <td>삼성전자</td>
      <td>2024-03-08 16:33</td>
    </tr>
    <tr>
      <th>1</th>
      <td>삼성전자주식</td>
      <td>삼성전자</td>
      <td>2024-03-08 16:33</td>
    </tr>
    <tr>
      <th>2</th>
      <td>삼성전자 배당금</td>
      <td>삼성전자</td>
      <td>2024-03-08 16:33</td>
    </tr>
    <tr>
      <th>3</th>
      <td>오늘 삼성전자 주가</td>
      <td>삼성전자</td>
      <td>2024-03-08 16:33</td>
    </tr>
    <tr>
      <th>4</th>
      <td>삼성전자서비스</td>
      <td>삼성전자</td>
      <td>2024-03-08 16:33</td>
    </tr>
  </tbody>
</table>
</div>

#### 함수를 통한 자동화

```python
# query를 입력하면 데이터 프레임을 출력하는 함수
def naver_relate_keyword(query):
    
    url = f"https://search.naver.com/search.naver?query={query}"
    response = requests.get(url)
    dom = BeautifulSoup(response.text, "html.parser")
    elements = dom.select(".lst_related_srch > .item")
    keywords = [element.text.strip() for element in elements]
    
    df = pd.DataFrame({"keywords": keywords})
    df["query"] = query
    
    now = datetime.now()
    now = now.strftime("%Y-%m-%d %H:%M")
    df["date_time"] = now
    
    return df
```

```python
query = "삼성전자"
df = naver_relate_keyword(query)
df.head()
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>keywords</th>
      <th>query</th>
      <th>date_time</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>삼성전자주가</td>
      <td>삼성전자</td>
      <td>2024-03-08 16:33</td>
    </tr>
    <tr>
      <th>1</th>
      <td>삼성전자주식</td>
      <td>삼성전자</td>
      <td>2024-03-08 16:33</td>
    </tr>
    <tr>
      <th>2</th>
      <td>삼성전자 배당금</td>
      <td>삼성전자</td>
      <td>2024-03-08 16:33</td>
    </tr>
    <tr>
      <th>3</th>
      <td>오늘 삼성전자 주가</td>
      <td>삼성전자</td>
      <td>2024-03-08 16:33</td>
    </tr>
    <tr>
      <th>4</th>
      <td>삼성전자서비스</td>
      <td>삼성전자</td>
      <td>2024-03-08 16:33</td>
    </tr>
  </tbody>
</table>
</div>

```python
dfs = []
queries = ["삼성전자", "LG전자"]

for query in queries:
    print(query, end=" ")
    df = naver_relate_keyword(query)
    dfs.append(df)
    
result = pd.concat(dfs, ignore_index=True)
result
```

<pre>
삼성전자 LG전자 
</pre>

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>keywords</th>
      <th>query</th>
      <th>date_time</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>삼성전자주가</td>
      <td>삼성전자</td>
      <td>2024-03-08 16:33</td>
    </tr>
    <tr>
      <th>1</th>
      <td>삼성전자주식</td>
      <td>삼성전자</td>
      <td>2024-03-08 16:33</td>
    </tr>
    <tr>
      <th>2</th>
      <td>삼성전자 배당금</td>
      <td>삼성전자</td>
      <td>2024-03-08 16:33</td>
    </tr>
    <tr>
      <th>3</th>
      <td>오늘 삼성전자 주가</td>
      <td>삼성전자</td>
      <td>2024-03-08 16:33</td>
    </tr>
    <tr>
      <th>4</th>
      <td>삼성전자서비스</td>
      <td>삼성전자</td>
      <td>2024-03-08 16:33</td>
    </tr>
    <tr>
      <th>5</th>
      <td>삼성전자서비스센타</td>
      <td>삼성전자</td>
      <td>2024-03-08 16:33</td>
    </tr>
    <tr>
      <th>6</th>
      <td>삼성전자주가지수</td>
      <td>삼성전자</td>
      <td>2024-03-08 16:33</td>
    </tr>
    <tr>
      <th>7</th>
      <td>삼성전자주식가격</td>
      <td>삼성전자</td>
      <td>2024-03-08 16:33</td>
    </tr>
    <tr>
      <th>8</th>
      <td>삼성 전자레인지</td>
      <td>삼성전자</td>
      <td>2024-03-08 16:33</td>
    </tr>
    <tr>
      <th>9</th>
      <td>삼성전자 패밀리몰</td>
      <td>삼성전자</td>
      <td>2024-03-08 16:33</td>
    </tr>
    <tr>
      <th>10</th>
      <td>lg전자 주가</td>
      <td>LG전자</td>
      <td>2024-03-08 16:33</td>
    </tr>
    <tr>
      <th>11</th>
      <td>lg전자 베스트샵</td>
      <td>LG전자</td>
      <td>2024-03-08 16:33</td>
    </tr>
    <tr>
      <th>12</th>
      <td>lg전자 서비스센터 전화번호</td>
      <td>LG전자</td>
      <td>2024-03-08 16:33</td>
    </tr>
    <tr>
      <th>13</th>
      <td>lg 전자레인지</td>
      <td>LG전자</td>
      <td>2024-03-08 16:33</td>
    </tr>
    <tr>
      <th>14</th>
      <td>lg전자 고객센터</td>
      <td>LG전자</td>
      <td>2024-03-08 16:33</td>
    </tr>
    <tr>
      <th>15</th>
      <td>lg전자렌지</td>
      <td>LG전자</td>
      <td>2024-03-08 16:33</td>
    </tr>
    <tr>
      <th>16</th>
      <td>lg전자 as</td>
      <td>LG전자</td>
      <td>2024-03-08 16:33</td>
    </tr>
    <tr>
      <th>17</th>
      <td>lg전자 고객센터 전화번호</td>
      <td>LG전자</td>
      <td>2024-03-08 16:33</td>
    </tr>
    <tr>
      <th>18</th>
      <td>lg전자 구독료</td>
      <td>LG전자</td>
      <td>2024-03-08 16:33</td>
    </tr>
    <tr>
      <th>19</th>
      <td>lg전자 주식</td>
      <td>LG전자</td>
      <td>2024-03-08 16:33</td>
    </tr>
  </tbody>
</table>
</div>
