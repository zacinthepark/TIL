# REST API

- Representational State Transfer
- Client와 Server가 통신하기 위한 URL 구조에 대한 정의 및 디자인

## 1. Kakao API

```python
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import requests, json
```

### 1-1. request token 얻기

- `https://developers.kakao.com/`
- 내 애플리케이션 > 애플리케이션 추가하기

```python
REST_API_KEY = '9d24634dd2717c0598d508594330aab5'
```

### 1-2. KoGPT

- 문서 > KoGPT > REST API
- tokens : 공백을 제외한 글자수

```python
# 1. URL
url = 'https://api.kakaobrain.com/v1/inference/kogpt/generation'
```

#### 1. 다음문장 만들기

```python
prompt = '원자폭탄을 발명한 사람은'
headers = {'Authorization': f'KakaoAK {REST_API_KEY}', 'Content-Type': 'application/json'}
params = {'prompt': prompt, 'max_tokens': 50, 'temperature': 0.3, 'n': 2}
```

```python
# 2. request > response
# json.dumps: 문자열 인코딩 : 한글은 인터넷 상에서 사용이 안됨 : 한글 > 영문, 특수문자로 인코딩

response = requests.post(url, json.dumps(params), headers=headers)
response
```

```
<Response [200]>
```

```python
# 3. parsing
results = response.json()
results = results['generations']
results = [result['text'] for result in results]
results
```

<pre>
[' 오펜하이머 박사이다. 그는 원자탄의 위력에 대해 확신하고 있었으며, 이를 이용해 전쟁에서 승리할 수 있다고 생각했다. 그러나 그가 만든 원자탄은 히로시마와 나가사키에 투하되어 인류를 파멸로',
 ' 오펜하이머 박사이다. 그는 원자탄의 위력에 매료되어 연구를 거듭하다가 원폭제조법 개발에 성공했다. 그리고 이 공로로 노벨상까지 받았는데, 바로 이때 미국에서 가장 인기 있었던 TV프로']
</pre>

```python
# 함수 만들기
def kogpt_api(prompt, command='', max_tokens=128, temperature=1, n=1):
    headers = {'Authorization': f'KakaoAK {REST_API_KEY}', 'Content-Type': 'application/json'}
    params = {'prompt': prompt + command, 'max_tokens': max_tokens, 'temperature': temperature, 'n': n}
    response = requests.post(url, json.dumps(params), headers=headers)  # params에 한글이 있을 시 json.dumps()로 처리
    results = response.json()
    results = results['generations']
    return [result['text'] for result in results]
```

#### 2. 문장 분류하기

- 문장 마다 `=긍정`, `=부정` 문자열 작성
- 분류할 마지막 문장 `=` 문자열 작성

```python
prompt = '''상품 후기를 긍정 또는 부정으로 분류합니다.
가격대비좀 부족한게많은듯=부정
재구매 친구들이 좋은 향 난다고 해요=긍정
ㅠㅠ약간 후회가 됩니다..=부정
이전에 먹고 만족해서 재구매합니다=긍정
튼튼하고 잘 쓸수 있을 것 같습니다. 이 가격에 이 퀄리티면 훌륭하죠='''
results = kogpt_api(prompt, max_tokens=1, temperature=0.4)
results
```

<pre>
['긍정']
</pre>

#### 3. 뉴스 한 줄 요약하기

- 마지막에 `한줄 요약:` 문자열 작성

```python
prompt = '''
미국의 생성형 AI(인공지능) 모델·서비스 개발사 오픈AI(OpenAI)를 상대로 제기된 소송이 누적되고 있다. 쟁점 또한 AI 자료 학습부터 오픈소스 공개까지 전선이 전방위로 확산되는 모양새다.
5일 IT(정보기술) 업계와 블룸버그 등 외신에 따르면 일론 머스크 테슬라 CEO(최고경영자)는 미국 캘리포니아주 샌프란시스코에서 오픈AI 법인과 창립자 샘 알트먼을 상대로 영리사업 중단과 AI 기술공개를 청구하는 소송을 지난달 29일(현지시간) 제기했다.
머스크는 소장에서 오픈AI가 마이크로소프트(MS)와 체결한 수십억달러 규모의 파트너십과 사실상 비공개된 AI 기술정보 등에 비춰 오픈AI가 인류의 이익을 위해 AI 기술을 공개하기로 한 당초 창업 합의를 파기했다고 주장했다. 머스크는 2015년 알트먼 등과 오픈AI를 비영리단체 형태로 공동 설립한 뒤 2018년 이사회에서 물러났다.
오픈AI를 둘러싼 법적 분쟁은 지난해 7월 미국 코미디언 겸 작가 사라 실버맨 등이 소송을 제기하면서 부각됐다. 언어모델 훈련 과정에서 창작물이 도용돼 저작권 침해, 저작권 관리정보 삭제에 따른 디지털 밀레니엄 저작권법(DMCA) 위반, 불공정 경쟁 등이 발생했다는 주장이다.
다만 법원은 챗GPT로 생성된 결과물과 작가들의 원작물 사이의 유사성이 떨어진다는 이유로 지난달 실버맨 등의 청구를 상당 부분 기각한 채 심리를 진행 중이다. 이 사건과 별개로 '왕좌의 게임' 원작자 조지 R.R. 마틴을 비롯한 미국 작가조합은 지난해 9월 집단소송을 제기한 상태다.
지난해 12월에는 미국 신문사 뉴욕타임스가 뉴스 저작권 침해를 주장하며 오픈AI와 오픈AI의 주요 투자자 MS를 상대로 소송을 제기했다. 뉴욕타임스 측은 회사 웹사이트에서 유료로 제공되던 기사 구절이 오픈AI의 서비스 챗GPT에 노출돼 이용자들이 우회적으로 기사를 무료로 읽을 수 있게 됐다고 주장했다. 오픈AI 측은 공개된 기사로 언어 모델을 훈련시켜 저작권법상 '공정이용 원칙'을 위반하지 않았다는 입장이다.
업계에선 오픈AI가 지난달 15일 동영상 생성 AI 모델 '소라(Sora)'를 출시한 데 따라 법적 분쟁이 더 복잡해질 것이라는 전망도 나온다. AI 학습과 결과물 생성에 이용되는 데이터의 종류가 기존 언어모델보다 다양하고, 학습된 데이터의 원작자는 저작권을 주장할 여지가 있지만 AI로 결과물을 산출한 주체는 저작권을 주장하기 어려운 탓이다.
법무법인 화우 정보보호센터는 지난달 29일 "데이터를 입력한 주체는 권리침해 등에 대해 책임을 질 가능성이 존재하므로 사전에 입력 데이터에 대한 검수 절차를 마련할 필요가 있다"고 밝혔다. 또 "저작권에 관련해선 현행 저작권법과 유관기관은 인간의 창작적 개입이 없는 산출물에 대한 저작권 등록을 불허하므로 사람과 AI 작업의 구별 등 등록기관 가이드와 별도의 입법을 확인할 필요가 있다"고 덧붙였다.
한줄 요약:'''
results = kogpt_api(prompt, max_tokens=50, temperature=0.2)
results
```

<pre>
[" 일론 머스크 테슬라 CEO가 미국 캘리포니아 주 샌프란시스코에서 인공지능(AI) 기반의 기업 '오픈AI'를 상대로 영리 사업 중단 및 AI 기술 공개를 요구하는 소송을 제기했으며, 이에 오픈AI측은 해당 내용이 DM"]
</pre>

#### 4. 질문에 답변하기

- 문장 마지막에 `?:` 로 끝남

```python
prompt = '''
의료 스타트업으로 구성된 원격의료산업협의회가 10월부터 열리는 국정감사 시기에 맞춰 국회와 정부에 비대면 진료법 근거 마련을 
촉구하는 정책제안서를 제출한다. 코로나19 사태에 비대면 진료의 한시 허용으로 원격 진료, 의약품 배송 등 서비스가 속속 등장하는 
가운데 제도화 논의를 서둘러야 한다는 목소리가 높아질 것으로 전망된다. 코리아스타트업포럼 산하 원격의료산업협의회는 '위드(with) 코로나' 
방역 체계 전환을 염두에 두고 비대면 진료 제도화 촉구를 위한 공동 대응 작업을 추진하고 있다. 협의회는 닥터나우, 엠디스퀘어, SH바이오, 
메디버디 등 의료 스타트업 13개사로 구성됐다. 협의회는 국정감사 시기를 겨냥해 국회와 주무 부처인 보건복지부에 비대면 진료의 법적 근거 마련을 
촉구할 방침이다. 이를 위해 주요 의원실과 관련 의견을 교환하고 있다. 협의회는 궁극적으로 의료법과 약사법 개정이 필요하지만 의료법 테두리 안에서 
시행령 개정 등으로도 비대면 진료 가능성과 대상·의료기관 등을 구체화할 수 있다는 복안이다. 복지부 장관령으로 비대면 진료 기간을 명시하는 방안 
등을 통해 사업 리스크도 줄일 수 있다. 올해 안에 국내 방역체계 패러다임이 바뀔 것으로 예상되는 점도 비대면 진료 제도화의 필요성을 높이고 있다. 
최근 코로나19 백신 접종이 속도를 내면서 방역 당국은 위드 코로나 방역체계 전환을 고려하고 있다. 인구 대비 백신 접종 완료율이 70%가 되는 
오는 10월 말에는 전환 논의가 수면 위로 뜰 것으로 보인다.
정책제안서를 제출하는 시기는 언제인가?:'''
results = kogpt_api(prompt, temperature=0.2)
results
```

<pre>
[' 9월 중순 이후']
</pre>

#### 5. 응용하기

```python
df = pd.read_excel('covid.xlsx')
df.head()
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>category</th>
      <th>link</th>
      <th>title</th>
      <th>content</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>101</td>
      <td>https://news.naver.com/main/read.nhn?mode=LSD&amp;...</td>
      <td>SK바이오사이언스, 코로나19 백신 임상 3상 시험계획 제출</td>
      <td>SK바이오사이언스가 코로나19 백신 후보물질(GBP510)의 임상 3상 시험계획...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>102</td>
      <td>https://news.naver.com/main/read.nhn?mode=LSD&amp;...</td>
      <td>고양시 노래연습장 코로나19 누적확진 41명</td>
      <td>【파이낸셜뉴스 고양=강근주 기자】 고양시는 28일 16시 기준 29명이 코로...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>103</td>
      <td>https://news.naver.com/main/read.nhn?mode=LSD&amp;...</td>
      <td>코로나19 신규 감염, 28일 오후 9시까지 542명</td>
      <td>[스포츠경향] 28일 서울 중구 서울역 광장에 마련된 코로나19 임시 선별검사소...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>103</td>
      <td>https://news.naver.com/main/read.nhn?mode=LSD&amp;...</td>
      <td>프로야구 수도권 구단서 코로나19 확진자 발생</td>
      <td>[이데일리 김지완 기자] 복수의 프로야구 수도권 구단에서 코로나19 확진자가 발...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>104</td>
      <td>https://news.naver.com/main/read.nhn?mode=LSD&amp;...</td>
      <td>"코로나 확진자 '0명'인 날은 절대 오지 않는다" 美전문가</td>
      <td>"주기적 발병…미국서 항상 어느 정도의 확산 있을 것""팬데믹 초기와는 다를 것…백...</td>
    </tr>
  </tbody>
</table>
</div>

```python
summaries = df['content'].apply(kogpt_api, command='한줄요약:', max_tokens=20, temperature=0.5)
```

```python
summaries = [summary[0] for summary in summaries]
df['summary'] = summaries
df.head()
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>category</th>
      <th>link</th>
      <th>title</th>
      <th>content</th>
      <th>summary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>101</td>
      <td>https://news.naver.com/main/read.nhn?mode=LSD&amp;...</td>
      <td>SK바이오사이언스, 코로나19 백신 임상 3상 시험계획 제출</td>
      <td>SK바이오사이언스가 코로나19 백신 후보물질(GBP510)의 임상 3상 시험계획...</td>
      <td>코로나백신,임상3상 계획제출로 기대감 상승 ​ ​ 오늘은 외국인과 기관 동반 매도</td>
    </tr>
    <tr>
      <th>1</th>
      <td>102</td>
      <td>https://news.naver.com/main/read.nhn?mode=LSD&amp;...</td>
      <td>고양시 노래연습장 코로나19 누적확진 41명</td>
      <td>【파이낸셜뉴스 고양=강근주 기자】 고양시는 28일 16시 기준 29명이 코로...</td>
      <td>확진자 하루 20명대 유지중인데, 오늘도 15명 발생했네요.</td>
    </tr>
    <tr>
      <th>2</th>
      <td>103</td>
      <td>https://news.naver.com/main/read.nhn?mode=LSD&amp;...</td>
      <td>코로나19 신규 감염, 28일 오후 9시까지 542명</td>
      <td>[스포츠경향] 28일 서울 중구 서울역 광장에 마련된 코로나19 임시 선별검사소...</td>
      <td>28일도 코로나19 확진자...주말·휴일 검사량 감소 효과로 주 중반 이후 확진</td>
    </tr>
    <tr>
      <th>3</th>
      <td>103</td>
      <td>https://news.naver.com/main/read.nhn?mode=LSD&amp;...</td>
      <td>프로야구 수도권 구단서 코로나19 확진자 발생</td>
      <td>[이데일리 김지완 기자] 복수의 프로야구 수도권 구단에서 코로나19 확진자가 발...</td>
      <td>서울, 인천 등 수도권 팀의 2군 전력분석원 겸 투수코치가 지난 27일 신종</td>
    </tr>
    <tr>
      <th>4</th>
      <td>104</td>
      <td>https://news.naver.com/main/read.nhn?mode=LSD&amp;...</td>
      <td>"코로나 확진자 '0명'인 날은 절대 오지 않는다" 美전문가</td>
      <td>"주기적 발병…미국서 항상 어느 정도의 확산 있을 것""팬데믹 초기와는 다를 것…백...</td>
      <td>미국의 코로나19 신규 확진자는 계속 나오겠지만 백신 접종이 늘면서 팬데믹이 엔</td>
    </tr>
  </tbody>
</table>
</div>

## 2. Naver API

- 통합검색어 트렌드 API
    - https://datalab.naver.com/
    - https://datalab.naver.com/keyword/trendSearch.naver

```python
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import requests, json
```

### 2-1. Request Token 얻기

- `https://developers.naver.com`
- 1. Request Token 얻기 : 애플리케이션등록 -> app_key 획득
- 2. app_key를 이용해서 데이터 가져오기

### 2-2. 통합검색어 트렌드 API

- 서비스 : `https://datalab.naver.com/keyword/trendSearch.naver`
- 내 애플리케이션 > dss 애플리케이션 > API 설정 > 데이터랩(검색어 트렌드) 추가
- 사용법 : `https://developers.naver.com/docs/serviceapi/datalab/search/search.md#통합-검색어-트렌드`

```python
# 1. App Key : http://localhost
CLIENT_ID, CLIENT_SECRET = 'Rl6wzLBxVArlYq9pJYD3', '12mIo4Bu6D'

# 2. document : url(params, headers)
url = 'https://openapi.naver.com/v1/datalab/search'
params = {
    'startDate': '2018-01-01',
    'endDate': '2024-03-01',
    'timeUnit': 'month',
    'keywordGroups': [
        {'groupName': '트위터', 'keywords': ['트위터', '트윗']},
        {'groupName': '페이스북', 'keywords': ['페이스북', '페북']},
        {'groupName': '인스타그램', 'keywords': ['인스타그램', '인스타']},
    ]
}
headers = {
    'Content-Type': 'application/json', 
    'X-Naver-Client-Id': CLIENT_ID, 
    'X-Naver-Client-Secret': CLIENT_SECRET
}

# 3. request(url:params,headers) > response : json(str)
response = requests.post(url, data=json.dumps(params), headers=headers)
response
```

```
<Response [200]>
```

```python
# 4. json(str) > list, dict : DataFrame
# parsing
data = response.json()['results']
data[2]
```

<pre>
{'title': '인스타그램',
 'keywords': ['인스타그램', '인스타'],
 'data': [{'period': '2018-01-01', 'ratio': 23.41982},
  {'period': '2018-02-01', 'ratio': 22.53544},
  {'period': '2018-03-01', 'ratio': 25.3988},
  {'period': '2018-04-01', 'ratio': 26.55983},
  {'period': '2018-05-01', 'ratio': 28.60035},
  {'period': '2018-06-01', 'ratio': 28.40753},
  {'period': '2018-07-01', 'ratio': 27.84405},
  {'period': '2018-08-01', 'ratio': 29.84383},
  {'period': '2018-09-01', 'ratio': 25.05096},
  {'period': '2018-10-01', 'ratio': 27.2048},
  {'period': '2018-11-01', 'ratio': 21.97864},
  {'period': '2018-12-01', 'ratio': 20.8739},
  {'period': '2019-01-01', 'ratio': 22.51379},
  {'period': '2019-02-01', 'ratio': 19.33788},
  {'period': '2019-03-01', 'ratio': 21.67678},
  {'period': '2019-04-01', 'ratio': 21.16257},
  {'period': '2019-05-01', 'ratio': 20.9485},
  {'period': '2019-06-01', 'ratio': 21.76954},
  {'period': '2019-07-01', 'ratio': 22.586},
  {'period': '2019-08-01', 'ratio': 21.43535},
  {'period': '2019-09-01', 'ratio': 19.83802},
  {'period': '2019-10-01', 'ratio': 22.24957},
  {'period': '2019-11-01', 'ratio': 21.55812},
  {'period': '2019-12-01', 'ratio': 21.52333},
  {'period': '2020-01-01', 'ratio': 22.0381},
  {'period': '2020-02-01', 'ratio': 21.53446},
  {'period': '2020-03-01', 'ratio': 25.01454},
  {'period': '2020-04-01', 'ratio': 24.12708},
  {'period': '2020-05-01', 'ratio': 25.68412},
  {'period': '2020-06-01', 'ratio': 25.47291},
  {'period': '2020-07-01', 'ratio': 27.08637},
  {'period': '2020-08-01', 'ratio': 26.73002},
  {'period': '2020-09-01', 'ratio': 26.0109},
  {'period': '2020-10-01', 'ratio': 26.21388},
  {'period': '2020-11-01', 'ratio': 25.81836},
  {'period': '2020-12-01', 'ratio': 25.74078},
  {'period': '2021-01-01', 'ratio': 25.5243},
  {'period': '2021-02-01', 'ratio': 22.79679},
  {'period': '2021-03-01', 'ratio': 28.04835},
  {'period': '2021-04-01', 'ratio': 27.90414},
  {'period': '2021-05-01', 'ratio': 26.56014},
  {'period': '2021-06-01', 'ratio': 26.31208},
  {'period': '2021-07-01', 'ratio': 25.15776},
  {'period': '2021-08-01', 'ratio': 25.07517},
  {'period': '2021-09-01', 'ratio': 24.95299},
  {'period': '2021-10-01', 'ratio': 28.76584},
  {'period': '2021-11-01', 'ratio': 23.30904},
  {'period': '2021-12-01', 'ratio': 22.87539},
  {'period': '2022-01-01', 'ratio': 22.0805},
  {'period': '2022-02-01', 'ratio': 20.23895},
  {'period': '2022-03-01', 'ratio': 22.4226},
  {'period': '2022-04-01', 'ratio': 22.07676},
  {'period': '2022-05-01', 'ratio': 22.23291},
  {'period': '2022-06-01', 'ratio': 21.63141},
  {'period': '2022-07-01', 'ratio': 21.40551},
  {'period': '2022-08-01', 'ratio': 21.78211},
  {'period': '2022-09-01', 'ratio': 21.07918},
  {'period': '2022-10-01', 'ratio': 23.38901},
  {'period': '2022-11-01', 'ratio': 21.51581},
  {'period': '2022-12-01', 'ratio': 20.33907},
  {'period': '2023-01-01', 'ratio': 20.30135},
  {'period': '2023-02-01', 'ratio': 19.498},
  {'period': '2023-03-01', 'ratio': 22.17574},
  {'period': '2023-04-01', 'ratio': 22.74806},
  {'period': '2023-05-01', 'ratio': 24.513},
  {'period': '2023-06-01', 'ratio': 23.92009},
  {'period': '2023-07-01', 'ratio': 22.59081},
  {'period': '2023-08-01', 'ratio': 21.96847},
  {'period': '2023-09-01', 'ratio': 21.10131},
  {'period': '2023-10-01', 'ratio': 22.15029},
  {'period': '2023-11-01', 'ratio': 23.18797},
  {'period': '2023-12-01', 'ratio': 21.84237},
  {'period': '2024-01-01', 'ratio': 21.69092},
  {'period': '2024-02-01', 'ratio': 19.91368},
  {'period': '2024-03-01', 'ratio': 7.91971}]}
</pre>

```python
# 5. preprocessing
dfs = []
for row in data:
    df = pd.DataFrame(row['data'])
    df['title'] = row['title']  # 트위터, 페이스북, 인스타그램
    dfs.append(df)
    
# df[0] : 트위터, df[1] : 페이스북, df[2] :인스타그램
result_df = pd.concat(dfs, ignore_index=True)
result_df.tail()
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>period</th>
      <th>ratio</th>
      <th>title</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>220</th>
      <td>2023-11-01</td>
      <td>23.18797</td>
      <td>인스타그램</td>
    </tr>
    <tr>
      <th>221</th>
      <td>2023-12-01</td>
      <td>21.84237</td>
      <td>인스타그램</td>
    </tr>
    <tr>
      <th>222</th>
      <td>2024-01-01</td>
      <td>21.69092</td>
      <td>인스타그램</td>
    </tr>
    <tr>
      <th>223</th>
      <td>2024-02-01</td>
      <td>19.91368</td>
      <td>인스타그램</td>
    </tr>
    <tr>
      <th>224</th>
      <td>2024-03-01</td>
      <td>7.91971</td>
      <td>인스타그램</td>
    </tr>
  </tbody>
</table>
</div>

```python
pivot_df = result_df.pivot(index='period', columns='title', values='ratio')
pivot_df.columns = ['instagram', 'twitter', 'facebook']
pivot_df.tail()
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>instagram</th>
      <th>twitter</th>
      <th>facebook</th>
    </tr>
    <tr>
      <th>period</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2023-11-01</th>
      <td>23.18797</td>
      <td>22.86116</td>
      <td>9.97093</td>
    </tr>
    <tr>
      <th>2023-12-01</th>
      <td>21.84237</td>
      <td>23.01963</td>
      <td>10.12856</td>
    </tr>
    <tr>
      <th>2024-01-01</th>
      <td>21.69092</td>
      <td>23.82156</td>
      <td>10.20900</td>
    </tr>
    <tr>
      <th>2024-02-01</th>
      <td>19.91368</td>
      <td>22.80641</td>
      <td>9.19334</td>
    </tr>
    <tr>
      <th>2024-03-01</th>
      <td>7.91971</td>
      <td>5.07203</td>
      <td>2.86928</td>
    </tr>
  </tbody>
</table>
</div>

```python
# 6. visualization
```

```python
%matplotlib inline
%config InlineBackend.figure_formats = {'png', 'retina'}
```

```python
import matplotlib.pyplot as plt
```

```python
pivot_df.plot(figsize=(20, 5))
plt.legend(loc=0)
plt.show()
```

![naver_search_trend](https://github.com/zacinthepark/TIL/assets/86648892/f58c8e29-4bc0-4bd8-b403-f952bd67facc)
