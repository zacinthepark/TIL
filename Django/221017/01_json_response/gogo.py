# gogo.py

# 요청보낼 때 requests 라이브러리 사용
import requests
from pprint import pprint


response = requests.get('http://127.0.0.1:8000/api/v1/json-3/') # requests가 GET Method로 해당 url에 요청을 보냄
result = response.json()                                        # 응답받은 것을 JSON으로 변환

pprint(result)
# pprint(result[0])
# pprint(result[0].get('title'))
