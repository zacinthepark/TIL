# APS

[APS 환경설정 (Pycharm)](#aps-환경설정-pycharm)<br>
[APS 문제풀이 Guidelines](#aps-문제풀이-guidelines)<br>

---

## APS 환경설정 (PyCharm)

---

## 1. PyCharm 설치

- **pycharm-community-2020.3.5.exe** 받기
    - [Jetbrains](https://www.jetbrains.com/) → 개발자도구(Developer Tools) → PyCharm → Download → 기타버전
        
        ![aps_1](https://user-images.githubusercontent.com/86648892/184478746-aaef594f-6a66-4c18-8076-5c57f6ca33e3.png)
        
    
    - 2020.3.5 버전 - `PyCharm Community Edition` 선택
        
        ![aps_2](https://user-images.githubusercontent.com/86648892/184478747-bd039857-5db3-4402-8ea8-fdd766db9972.png)
        
설치

![aps_3](https://user-images.githubusercontent.com/86648892/184478748-3a10afd6-ded8-41cf-a4b1-7b2325bdf66b.png)

받은 파일 실행

![aps_4](https://user-images.githubusercontent.com/86648892/184478749-449e6af4-7895-44be-a4e8-8500a5f642fd.png)

기존 버전이 있다면면 삭제 여부 결정 (기존 버전이 없으면 생략됨)

![aps_5](https://user-images.githubusercontent.com/86648892/184478750-ef815633-cd4f-4c02-9123-1b4e6e642807.png)

삭제 완료 후 Close. (기존 버전이 없으면 생략됨)

![aps_6](https://user-images.githubusercontent.com/86648892/184478751-e450c705-f24f-4fba-bae5-97e8a3083cf6.png)

![aps_7](https://user-images.githubusercontent.com/86648892/184478753-6a6511dc-af83-49f0-8f1d-54bcd73d0e43.png)

![aps_8](https://user-images.githubusercontent.com/86648892/184478755-6b4c6f47-e4af-4ff3-9ed8-d84e846a826b.png)

설치 완료

![aps_9](https://user-images.githubusercontent.com/86648892/184478756-59800e52-e844-40f4-a8e6-68505d80db0c.png)

파이참 실행 시 (이전 파이참 설정이 있는 경우 출력 됨)

---

## 2. PyCharm 기본 설정

### 2.1. 인터프리터 설정

- Python 설치 환경에 따라 인터프리터 설정이 자동으로 되지 않을 수 있기 때문에 직접 지정

![aps_10](https://user-images.githubusercontent.com/86648892/184478757-d5689409-206f-4839-9def-ae75f00604ea.png)

Customize → All settings 선택

![aps_11](https://user-images.githubusercontent.com/86648892/184478759-b19cc2cc-687d-4b2b-951e-6870a18d7f13.png)

Python Interpreter → `<No interpreter>` → Show All 선택

![aps_12](https://user-images.githubusercontent.com/86648892/184478760-a5b10495-c2ec-4f96-b15c-fa9448297c22.png)

+ 버튼 클릭

![aps_13](https://user-images.githubusercontent.com/86648892/184478761-f307ad62-9ab7-4ccf-831f-be98e130737c.png)

System interpreter → 현 파이썬 global 환경 선택 

- 빌드 테스트
    
    ![aps_14](https://user-images.githubusercontent.com/86648892/184478762-cc87fa3d-1554-4b06-af74-6cc3ffde44cd.png)
    
    Project → New Project
    
    ![aps_15](https://user-images.githubusercontent.com/86648892/184478763-253e42fc-7188-4df3-a69b-6c741493a076.png)
    
    프로젝트 폴더 경로 및 이름 자율 지정 & Previously configured interpreter 선택.
    
    ![aps_16](https://user-images.githubusercontent.com/86648892/184478764-13dcfb4f-68e5-4c38-97ac-5b2eae174114.png)
    
    소스코드에서 마우스우클릭 → Run ‘main’ 혹은 우측 상단 Run 버튼 클릭
    

- 주의
    - Python 인터프리터를 완전히 처음 실행할 경우 파이참 하단에 로딩이 진행되니 
    로딩이 끝난 후 빌드 테스트 할 것
        
        ![aps_17](https://user-images.githubusercontent.com/86648892/184478765-718e2179-0563-4954-9d28-85b7a3958a4d.png)
        

### 2.2. Terminal 설정

- bash를 기본 터미널로 사용하기 위한 설정
- git을 사용하기 위해 설정

![aps_18](https://user-images.githubusercontent.com/86648892/184478766-1d7427ca-84ed-4a50-accc-fd4b9c9a62d8.png)

1. 설정(`ctrl + alt + s`) → `Terminal` 검색 → `Shell path` 클릭

![aps_19](https://user-images.githubusercontent.com/86648892/184478767-8265625d-dc83-4cb8-b808-1fee1f39c69f.png)

2. `C → Program Files → Git → bin → bash.exe` 선택 후 OK 클릭

- ***이때 Git 폴더 안에 있는 파일 선택하지 않도록 유의***

![aps_20](https://user-images.githubusercontent.com/86648892/184478768-048d1cfe-e19f-4932-9dbb-9d67837fbd1f.png)

3. Apply → OK 클릭 

![aps_21](https://user-images.githubusercontent.com/86648892/184478769-8814e21d-6005-449f-bcdb-7cb6342a84f2.png)

![aps_22](https://user-images.githubusercontent.com/86648892/184478770-cb788d1a-926a-461e-a435-1ddaec3acfea.png)

4. 실행결과 확인

### 2.3. 기타 세팅

**폰트 사이즈 조절 설정 (마우스로 폰트 크기 조절)**

- settings → Mouse 검색 → `Change font size (Zoom) with Ctrl + Mouse Wheel` 선택

![aps_23](https://user-images.githubusercontent.com/86648892/184478772-640c8966-98ce-483f-880f-972caccaebbc.png)

**코드 에디터 폰트 설정**

- settings → font 검색 → 원하는 폰트 & 22 세팅

![aps_24](https://user-images.githubusercontent.com/86648892/184478774-d777a78c-c1cb-4ce7-b1df-91b0d56f16c4.png)

**콘솔 폰트 설정**

- settings → console font 검색 → 원하는 폰트 & 22 & 1.2 세팅

![aps_25](https://user-images.githubusercontent.com/86648892/184478775-fb83f725-8224-4a08-90ac-82747f355ba2.png)

**자동으로 git add 되는 설정 끄기**

- settings → confirmation 검색 → `Do not add` 클릭
(비활성화 되어있을 경우 안해도 됨)

<img width="970" alt="aps_26" src="https://user-images.githubusercontent.com/86648892/184478776-1f6fc0ef-6531-4d75-841a-add2a8f29ff1.png">

---

## 3. PyCharm을 활용한 실행

### 3.1. Input 연습

- input.txt

```
33
```

- p1.py

```python
import sys

sys.stdin = open('input.txt')

# 33
# => 홀수면 1, 짝수면 0
N = int(input())
result = 1 if N % 2 else 0
print(f'{result}')
```

### 3.2. 파일 실행

1. **첫 번째 방법 - 우상단의 ▶ 버튼 클릭**
    
    <img width="952" alt="aps_27" src="https://user-images.githubusercontent.com/86648892/184478777-4c5219c0-b1ea-4109-9ea4-6625d8237547.png">
    
2. **두 번째 방법 - 파일에서 우클릭 후 `Run` 클릭**
    
    <img width="952" alt="aps_28" src="https://user-images.githubusercontent.com/86648892/184478778-e7b7491a-3aa3-41a3-a5e0-167516fe712c.png">
    
- **최종적으로 위와 같은 구조로 진행**
    
    ![aps_29](https://user-images.githubusercontent.com/86648892/184478779-5f6c18d1-4c6f-4724-9702-8a7d31183fec.png)

---

## APS 디버깅 (PyCharm)

---

## 디버깅(Debugging)

디버깅(혹은 디버그)는 컴퓨터 프로그램 개발 단계 중에 발생하는 시스템의 논리적인 오류나 
비정상적 연산(버그)을 찾아내고 그 원인을 밝히고 수정하는 작업 과정

### [디버거 도구창](https://www.jetbrains.com/help/pycharm/debug-tool-window.html#steptoolbar)

### 실행

1. `.py` 파일에서 `우클릭` → `Debug 파일 이름` 클릭
2. 우측 상단의 벌레 아이콘 클릭
3. `shift + F9` 클릭

![aps_30](https://user-images.githubusercontent.com/86648892/184479544-a223c9c8-f6d0-4c2e-bcda-dada2fae2810.png)

### 1. Stepping Tools

- 디버깅을 수행할 때 유용한 다양한 도구

![aps_31](https://user-images.githubusercontent.com/86648892/184479545-17d7412e-a520-45d9-8c67-9998c689dfbd.png)

|번호   |도구의 기능   |단축키   |설명   |
|---|---|---|---|
|1   |Show Execution Point   |`Alt + F10`   |현재 실행 지점을 가리킴   |
|2  |Step Over   |`F8`   |현재 실행 지점이 있는 경우 해당 함수(메서드) 또는 파일의 다음 줄까지 이동<br>함수를 만나면 함수 안으로 들어가지 않고 함수의 실행 결과 뒷줄로 바로 이동   |
|3   |Step Into   |`F7`   |디버거가 순차적으로 실행되다가 함수(메서드)를 만나면 해당 함수 내부로 들어감   |
|4   |Step Into My Code   |`Alt + Shift + F7`   |라이브러리 소스 코드가 아닌 내가 작성한 코드의 라인만 디버거를 실행하고 싶은 경우   |
|5   |Force Step Into   |`Alt + Shift + F7`   |   |
|6   |Step Out   |`Shift + F8`   |현재 함수(메서드) 바로 뒤에 실행되는 줄로 이동<br>함수 안으로 들어갔는데 해당 밖으로 밖으로 나오고 싶은 경우 사용   |
|7   |Run to Cursor   |`Alt + F9`   |현재 커서가 위치한 줄로 바로 이동<br>단, 중간에 다른 Breakpoint가 있는 경우 해당 위치에서 멈추게 됨   |
|8   |Evaluate Expression   |`Alt + F8`   |   |

### 2. Frame

- 각 스레드의 콜스택을 살펴볼 수 있게 시각화된 형태로 제공

### 3. Variables

- 현재 실행 맥락에서 활성화된 변수를 보여주며 이를 통해 디버깅을 가능하게 하고 실시간으로 수정하며 디버깅을 할 수 있는 기능을 제공

### 4. Watches

- 특정한 맥락 변수

### 5. Console

- 종단점을 기준으로 디버거의 실행 결과 확인

## Breakpoint

### 의미

> "Breakpoints are special markers that suspend program execution at a specific point. 
This lets you examine the program state and behavior."
>
- 종단점은 특정한 순간에서의 프로그램 실행을 중단 시키는 특수한 마커이며 이를 통해 프로그램의 상태 및 동작을 검사할 수 있다. 
- 종단점만 잘 걸어도 매우 효율적인 디버깅이 가능하다.

- 예제 코드
    
    ```
    3
    2
    2 2 4 4 1
    3 3 6 6 2
    3
    1 2 3 3 1
    3 6 6 8 1
    2 3 5 6 2
    3
    1 4 8 5 1
    1 8 3 9 1
    3 2 5 8 2
    ```
    
    ```python
    import sys
    
    sys.stdin = open('input.txt')
    
    T = int(input())
    
    def solve(N):
        for k in range(N):
            r1, c1, r2, c2, color = map(int, input().split())
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    boxes[i][j] += color
    
    for tc in range(1, T + 1):
        boxes = [[0] * 10 for _ in range(10)]
        n = int(input())
        cnt = 0
    
        solve(n)
    
        for i in range(10):
            for j in range(10):
                if boxes[i][j] == 3:
                    cnt += 1
    
        print('#{} {}'.format(tc, cnt))
    ```
    

### 실행

- 프로그램의 실행이 중단되길 원하는 지점의 숫자 옆 공백을 클릭하고 디버거 실행
    
    <img width="961" alt="aps_32" src="https://user-images.githubusercontent.com/86648892/184479546-9ccffce8-659a-4025-9b93-31ca2595668f.png">
    

- 파일을 실행하면 아래와 같이 해당 지점에서 프로그램의 실행이 멈추게된다.
    
    ![aps_33](https://user-images.githubusercontent.com/86648892/184479548-42404023-b422-41b3-a0b2-11b95fcf4274.png)
    

### 재실행 및 종료

- 디버거 세션의 재실행은 `ctrl + F5`
- 디버거 세션의 종료는 `ctrl + F2`

## 디버깅 활용 예제

### 1️. Breakpoint 설정

![aps_34](https://user-images.githubusercontent.com/86648892/184479550-7eb99508-eafa-4eb6-8516-2deb899bbf18.png)

디버깅을 원하는 지점(라인)의 오른쪽 공백 부분을 체크하여 Breakpoint를 걸어줍니다.

### 2️. Step Into(`F7`)

**종단점에서 실행이 중지된 프로그램에서 `F7`을 누르면 다음 실행 될 라인으로 이동**

이때 `Variables`를 보면 현재 실행 환경(전역)의 변수 목록을 확인할 수 있음

![aps_35](https://user-images.githubusercontent.com/86648892/184479551-cfae5b53-f17a-4fa1-868c-1be5c0dada59.png)

**만약 코드의 실행 과정에서 함수를 만나면 함수 내부로 이동**

- 이때 `Frames`를 보면 현재 실행 환경이 전역 → 함수 내부로 이동 했기 때문에 
변수 목록이 변경 된 것을 확인할 수 있음
    
    <img width="961" alt="aps_36" src="https://user-images.githubusercontent.com/86648892/184479553-e275d413-838a-4246-8772-8713565e204e.png">
    
    전역 
    
    <img width="961" alt="aps_37" src="https://user-images.githubusercontent.com/86648892/184479555-58cf5a3f-ce71-4115-852f-fbd9e49780d1.png">
    
    함수 내부
    

### 3️. Step out(`Shift + F8`)

**함수 내부에서 결과를 실행하는 과정을 종료하고 싶다면 Step out 기능을 사용**

<img width="961" alt="aps_38" src="https://user-images.githubusercontent.com/86648892/184479557-91ec7443-8472-4fe9-b649-092e3ddcf50f.png">

함수 내부에서 디버거 실행 중

<img width="961" alt="aps_39" src="https://user-images.githubusercontent.com/86648892/184479558-2e8094e3-93d1-43cf-b555-527cc30ce79c.png">

Step out을 통해 함수 바깥으로 빠져나온 모습

### 4️. Step over(`F8`)

**특정한 함수의 실행 과정을 거치지 않고 바로 다음으로 넘어가고 싶은 경우 Step over 기능을 사용**

<img width="961" alt="aps_40" src="https://user-images.githubusercontent.com/86648892/184479559-4a96b3c2-8a5a-44c8-ab6c-7943f0653d9c.png">

여기서 F7를 사용하게되면 `solve` 함수 내부로 들어가게 됨

<img width="961" alt="aps_41" src="https://user-images.githubusercontent.com/86648892/184479560-300acd17-2280-44ee-966d-b3bc52271c1c.png">

하지만 Step over(`F8`)를 사용하게 되면 함수의 실행 결과를 거친 이후 바로 다음 줄로 넘어가 실행 가능

### 5️. Run to cursor(`Alt + F9`)

**현재 실행 중인 지점으로부터 특정한 지점으로 바로 이동하고 싶은 경우 Run to cursor 기능을 사용**

- 이동하고 싶은 라인의 코드의 일부분을 드래그 한 후 Run to cursor 버튼 클릭
- (c.f. 모든 상황에 적용 가능한 것은 아님)
    
    <img width="961" alt="aps_42" src="https://user-images.githubusercontent.com/86648892/184479561-28a05027-d4f7-439c-8a6b-742f55fca5b8.png">
    
    14번째 줄에서 19번째 줄로 바로 이동하고 싶다!
    
    <img width="961" alt="aps_43" src="https://user-images.githubusercontent.com/86648892/184479562-675c6e43-e57d-4177-a33c-73a54fbdacbf.png">
    
    Run to cursor 기능을 통해 바로 이동 가능
    

### 6️. Watches

**특정한 함수의 맥락에서 다른 (ex. 전역) 맥락의 변수 등을 확인하고 싶은 경우 Watches를 활용**

<img width="961" alt="aps_44" src="https://user-images.githubusercontent.com/86648892/184479565-92140094-678a-4cd1-b144-931a188f2cfa.png">

<img width="961" alt="aps_45" src="https://user-images.githubusercontent.com/86648892/184479567-991143d7-3f2f-4ce6-8861-3955ad50fe08.png">

### 7️. 이차원 배열 편하게 보기

왼쪽의 토글 버튼을 클릭하면 2차원 배열에서 각 행에 해당하는 리스트를 한 줄로 펼쳐서 보여주기 때문에 매우 편하게 확인 가능

![aps_46](https://user-images.githubusercontent.com/86648892/184479569-eb82bf06-4ebf-4264-a5e3-c114f9f98176.png)

## 참고 자료

[Debug Wikipedia](https://ko.wikipedia.org/wiki/%EB%94%94%EB%B2%84%EA%B7%B8)

[Jetbrains Debug PyCharm](https://www.jetbrains.com/help/pycharm/debugging-code.html)

---

## APS 문제풀이 Guidelines

---

## 문제풀이 과정의 목표

### 빈틈없이!!!!!!

- **입력 TC를 처리하여 정확한 출력을 내보내는 것**
- A형까지는 모든 테스트케이스를 빠짐없이 통과할 수 있도록 하는 것에 초점을 두어야 함
    - 유려한 알고리즘을 짜겠다는 생각은 일단 버리자
    - 숨겨져 있는 테스트케이스들도 통과할 수 있는 실력을 갖추자

## 문제풀이 유형

### 1. 아이디어

- 아이디어를 내고 이를 구현하는 능력
- 1, 2차원 list
    - 다중 loop
    - if

### 2. 알고리즘

- 누군가 아이디어를 체계화시킨 것
- 템플릿
    - 자료구조
        - 스택
        - 큐
        - 등등
    - BFS (너비 우선 탐색)
    - DFS (깊이 우선 탐색)
    - 등등
- 유형을 잘 이해하고
    - 잘 응용하는 능력

## 문제풀이 주의사항

- Sample Case는 맞지만 부분정답이 나오는 경우
    - 문제풀이 방향성이 잘못된 것이다!
    - 예외처리, if조건 등등 덕지덕지 추가한 것은 그저 누더기가 되어 어찌저찌 맞추더라도 다른 테스트케이스에는 작동하지 않을 수 있음
- 범위 설정에서 실수 많이함
- 코테 문제 출제의 대부분은 TC 설계에 시간을 보낸다
    - TC는 더럽게 내는 것이 출제자의 목표
    - TC 설계
        - 30%는 쉬운 상황
        - 40%는 경계값
        - 30%는 범위나 이런 것들 등에서 극한 상황으로 줌
- Sample Case들을 보면서 문제풀이를 어떤 방향으로 할지 출제자의 의도를 파악

### 1. 처음 보는 문제를 이해하고

### 2. 모든 TC를

### 3. 제한조건 내에 정확히 처리

### 유형별 연습은 가능하지만 정해진 유형은 없다

## 문제풀이 단계

- 문제 읽기
    - 1회독
        - 3분정도 훑으며 TC 손코딩
    - 2회독
        - 조건이나 특이사항 체크
    - 3회독
        - 지양하자
        - 디버깅까지 해봤는데 전혀 감이 안올 때
        - 새출발한다는 느낌으로
        - 이런 경우는 연습 때 겪어보자
- 접근방법 구상
    
    <img width="741" alt="aps_47" src="https://user-images.githubusercontent.com/86648892/184578972-130d8009-6aa1-45f0-b043-7de0ca62c6d6.png">
    
    - 알고리즘 유형 적용 가능한지 체크
    - 그게 아니라면 아이디어 구현
        - 규칙성 발견이 어렵다면
            - 가능한 모든 경우 완전탐색
                - big o notation 기준 `n^2` 는 시간 내에 못할 확률 높음
            - 전체문제가 아닌 일부분으로 쪼개거나 단계를 나누어 생각
            - 혹은 생각의 방향을 반대로 해보는 경우
    - 컴퓨터는 단계별로 반복하며 진행하는 존재
        - 인간의 뇌적 사고 방식으로 코드를 짜려다보면 난관에 봉착할 수 있다
- 핵심코드 손코딩
    - 시각적으로
    - 실명의 변수
    - 범위
- 코드구현
- 디버깅 및 개선
    - 공개된 TC와 답이 내 코드로 구현이 되지 않을 때
        - 이런 경우는 오히려 해피한 경우

<img width="840" alt="aps_48" src="https://user-images.githubusercontent.com/86648892/184578984-f615e8ee-fc48-4d89-9997-d58314cd87f0.png">

## Input 처리

<img width="840" alt="aps_49" src="https://user-images.githubusercontent.com/86648892/184578985-396ccadb-add0-4883-b1d5-174e36f11538.png">

<img width="824" alt="aps_50" src="https://user-images.githubusercontent.com/86648892/184578987-b9cc4fcc-54d2-4b35-9568-f2233039e2fe.png">

---