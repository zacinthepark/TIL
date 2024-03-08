### selenium

- `https://www.selenium.dev`

- 자동화를 목적으로 만들어진 다양한 브라우져와 언어를 지원하는 라이브러리

- 크롬 브라우져 설치

    - 크롬 브라우져 드라이버 다운로드 (크롬 브라우져와 같은 버전)

        - https://googlechromelabs.github.io/chrome-for-testing/

    - 다운로드한 드라이버 압축 해제

    - chromedriver, chromedriver.exe 생성

    - windows : 주피터 노트북 파일과 동일한 디렉토리에 chromedriver.exe 파일 업로드

    - mac : sudo cp ~/Download/chromedirver /usr/local/bin

```python
# !pip install selenium
```

```python
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
```

```python
# driver = webdriver.Chrome()
```

```python
# 페이지 이동
# driver.get("https://daum.net")
```

```python
# 브라우져 사이즈 조절
# driver.set_window_size(200, 600)
```

```python
# alert 다루기
# driver.execute_script("alert('hello selenium!!!');")
```

```python
# alert 확인 누르기
# alert = driver.switch_to.alert
# alert.accept()
```

```python
# 팝업 닫기 버튼 클릭
# driver.find_element(By.CSS_SELECTOR, '.link_close').click()
```

```python
# 브라우져 스크롤 조절
# driver.execute_script("window.scrollTo(200, 300);")
```

```python
# 브라우져 스크롤 조절
# driver.execute_script("window.scrollTo(0, 0);")
```

```python
# 브라우져 사이즈 조절
# driver.set_window_size(800, 800)
```

```python
# 문자열 입력
# driver.find_element(By.CSS_SELECTOR, "#q").send_keys("셀레니움")
```

```python
# 문자열 입력
# driver.find_element(By.CSS_SELECTOR, "#q").clear()
```

```python
# 검색 버튼 클릭
# driver.find_element(By.CSS_SELECTOR, '.btn_ksearch').click()
```

```python
# 브라우져 종료
# driver.quit()
```

### 텍스트 데이터 가져오기

- TED 사이트 : `https://www.ted.com`

```python
# 브라우져를 실행하여 테드 사이트 열기
driver = webdriver.Chrome()
driver.get("https://www.ted.com/talks")
```

```python
# CSS Selector를 이용하여 HTML 태그와 태그 사이의 text 데이터 가져오기
driver.find_element(By.CSS_SELECTOR, ".text-textPrimary-onLight").text
```

<pre>
'TED Talks: Discover ideas worth spreading'
</pre>

```python
# 제목 데이터 가져오기
selector = '.container > section > .relative > div:nth-child(2) > div > div'
contents = driver.find_elements(By.CSS_SELECTOR, selector)
len(contents)
```

<pre>
24
</pre>

```python
# 가장 처음 텍스트 데이터 가져오기
contents[0].find_element(By.CSS_SELECTOR, '.text-textPrimary-onLight').text
```

<pre>
'The unsung heroes fighting malnutrition'
</pre>

```python
# 전체 제목 데이터 가져오기
titles = []
for content in contents:
    title = content.find_element(By.CSS_SELECTOR, '.text-textPrimary-onLight').text
    titles.append(title)
titles[:3], len(titles)
```

<pre>
(['The unsung heroes fighting malnutrition',
  'How to lead with radical candor',
  'How to find creativity and purpose in the face of adversity'],
 24)
</pre>

```python
# 링크 데이터 크롤링 (속성(attribute)값 가져오는 방법)
links = []
selector = '[data-testid="TalkGrid Talk Item"]'
for content in contents:
    link = content.find_element(By.CSS_SELECTOR, selector).get_attribute("href")
    links.append(link)
links[-3:]
```

<pre>
['https://www.ted.com/talks/zainab_usman_how_sci_fi_informs_our_climate_future_and_what_to_do_next',
 'https://www.ted.com/talks/maryam_banikarim_life_s_an_obstacle_course_here_s_how_to_navigate_it',
 'https://www.ted.com/talks/the_merian_ensemble_atalanta']
</pre>

```python
driver.quit()
```

### 3. Headless

- 브라우져를 화면에 띄우지 않고 메모리상에서만 올려서 크롤링하는 방법 

- window가 지원되지 않는 환경에서 사용이 가능

- chrome version 60.0.0.0 이상부터 지원 합니다.

```python
# 현재 사용중인 크롬 버전 확인
driver = webdriver.Chrome()
version = driver.capabilities["browserVersion"]
print(version)
driver.quit()
```

<pre>
122.0.6261.96
</pre>

```python
# headless 사용
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(options=options)
driver.get("https://www.ted.com/talks")
text = driver.find_element(By.CSS_SELECTOR, ".text-textPrimary-onLight").text
driver.quit()
print(text)
```

<pre>
TED Talks: Discover ideas worth spreading
</pre>
