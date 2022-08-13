# APS

## APS 환경설정

---

## 1. PyCharm 설치

- **pycharm-community-2020.3.5.exe** 받기
    - [jetbrains](https://www.jetbrains.com/) → 개발자도구(Developer Tools) → PyCharm → Download → 기타버전
        
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