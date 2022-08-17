# Algorithm Concepts

[Algorithm이란](#algorithm)<br>
[Array](#array)<br>
[2차원배열](#2차원-배열)<br>
[정렬](#정렬)<br>
[Bubble Sort](#버블-정렬bubble-sort)<br>
[Counting Sort](#카운팅-정렬counting-sort)<br>
[Selection Sort](#선택-정렬selection-sort)<br>
[완전 검색(Exhaustive Search)](#완전검색-exhaustive-search)<br>
[탐욕(Greedy) 알고리즘](#탐욕greedy-알고리즘)<br>
[부분집합의 합](#부분집합의-합-subset-sum)<br>
[비트 연산자](#비트-연산자)<br>
[검색(Search)](#검색-search)<br>
[순차 검색(Sequential Search)](#순차-검색-sequential-search)<br>
[이진 검색(Binary Search)](#이진-검색-binary-search)<br>
[인덱스](#인덱스)<br>
[문자열(String)](#문자열string)<br>
[문자열의 분류 및 처리](#문자열의-분류-및-처리)<br>
[문자열 Pattern Matching](#pattern-matching)<br>
[문자열 암호화](#문자열-암호화)<br>
[문자열 압축](#문자열-압축)<br>

---

# Algorithm

## 알고리즘

- 유한한 단계를 통해 문제를 해결하기 위한 절차나 방법
- 컴퓨터 분야에서 알고리즘을 표현하는 방법 2가지
    - 의사코드(Pseudocode)
    - 순서도

## 알고리즘의 성능

- APS 과정의 목표 중 하나는 보다 좋은 알고리즘을 이해하고 활용하는 것
- 좋은 알고리즘?
    - 정확성
        - 얼마나 정확하게 동작하는가
    - 작업량
        - 얼마나 적은 연산으로 원하는 결과를 얻어내는가
        - 실행시간
        - 시간복잡도
    - 메모리 사용량
        - 얼마나 적은 메모리를 사용하는가
        - 공간복잡도
    - 단순성
        - 얼마나 단순한가
    - 최적성
        - 더 이상 개선할 여지없이 최적화되었는가

<img width="701" alt="a_1" src="https://user-images.githubusercontent.com/86648892/184582710-720d933f-5c95-474d-a084-d2a3bd167a8a.png">

- 알고리즘 1의 경우 값이 1000이 되면 1000번으로 연산이 늘어나지만, 알고리즘 2의 경우 3번으로 고정

### 시간복잡도(Time Complexity)

- 알고리즘의 작업량을 표현할 때 시간복잡도로 표현
- 실제 걸리는 시간을 측정
    - 실행되는 명령문의 개수를 계산

### Big O Notation

- 시간복잡도를 표현하는 방법
- 시간복잡도 함수 중에서 가장 큰 영향력을 주는 n에 대한 항만을 표시
- 계수(coefficient)는 생략하여 표시

<img width="784" alt="a_2" src="https://user-images.githubusercontent.com/86648892/184582713-9825786b-1bbc-4fa7-a7c5-934c9908c07b.png">

<img width="702" alt="a_3" src="https://user-images.githubusercontent.com/86648892/184582717-6342f759-d3dd-43fc-87c5-20e707f982e0.png">

<img width="791" alt="a_4" src="https://user-images.githubusercontent.com/86648892/184582721-26979cf9-aef2-4847-8133-6f50372d4f4c.png">

- 문제의 시간복잡도를 보고 접근 방법이 옳은지 생각해볼 수 있음

---

# Array

## 배열

### 일정한 자료형의 변수들을 하나의 이름으로 열거하여 사용하는 자료구조

## 배열의 필요성

- 프로그램 내에서 여러 개의 변수가 필요할 때, 일일이 다른 변수명을 이용하여 자료에 접근하는 것은 매우 비효율적일 수 있음
- 배열을 사용하면 하나의 선언을 통해서 둘 이상의 변수를 선언할 수 있음
- 단순히 다수의 변수 선언을 의미하는 것이 아니라, 다수의 변수로는 하기 힘든 작업을 배열을 활용해 쉽게 할 수 있음

## 1차원 배열

### 1차원 배열 선언

- 별도의 선언 방법이 없으면 변수에 처음 값을 할당할 때 생성
- `Arr = list()`
- `Arr = []`
- `Arr = [1, 2, 3]`
- `Arr = [0] * 10`
    - 값은 구체적으로 정하진 않았는데, 10칸짜리 배열을 작성하고 싶을 때

<img width="319" alt="a_5" src="https://user-images.githubusercontent.com/86648892/184583195-d68fe5e2-0dfe-4681-8956-89cfd39e0bae.png">

- 정확히 말하자면 위의 그림처럼 Arr를 Frames에 참조 주소를 넣고, Objects에 데이터를 넣음
- `Arr = []` 는 엄밀히 말하자면 Frames에 Arr만 생긴 상태이고, Objects에 아무것도 없는 것
    - 참조할 준비만 마쳐놓은 상태

### 1차원 배열 접근

- `Arr[0] = 10`
    - 배열 Arr의 0번 원소에 10을 저장하라
- `Arr[idx] = 20`
    - 배열 Arr의 idx번 원소에 20을 저장하라

### **최대값 찾기**

```python
'''
9
7 4 2 0 0 6 0 7 0
3
2 3 4
'''
# 입력값 받기
N = int(input())
arr = list(map(int, input().split()))
# 가장 큰 수를 찾을 수 있는가?
# 모든 원소를 접근하고 나면 maxV를 찾기를 원해
maxV = arr[0] # 첫 원소를 최대값으로 가정
for i in range(1, N):  # 나머지 모든 원소에 대해
    if arr[i] > maxV:
        maxV = arr[i]
print(maxV)

# 첫 원소를 사용할 수 없는 경우도 있다 (구간으로 주어지는 등)
```

### **최대값 index 찾기**

```python
#최대값, 최소값 찾기, 같은 값이 있을 때 왼쪽 오른쪽, 위치 찾기

#maxIdx를 찾아보자
#최대값의 위치, 같은 값이 있을 때는 맨 오른쪽

N = int(input())
arr = list(map(int, input().split()))
maxIdx = 0 # 가정 (맨 앞의 수가 가장 큰 수야)
for i in range(1, N):
    if arr[maxIdx] <= arr[i]: #같은 값이 있을 경우 맨 왼쪽으로 하고 싶다면 <
        maxIdx = i
print(maxIdx)
```

### 배열 활용 예제: Gravity

<img width="697" alt="a_6" src="https://user-images.githubusercontent.com/86648892/184584054-d73cb6dd-321a-4459-9fe7-ad0cf14e4e0b.png">

```python
'''
입력
1
9
7 4 2 0 0 6 0 7 0

출력
#1 7
'''
# 더 작은 애가 있는만큼 떨어질 것이니 우측에 더 작은 애가 있는만큼 cnt를 올려주면 됨

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        cnt = 0
        for j in range(i+1, N):
            if lst[i] > lst[j]:
                cnt += 1
        if ans < cnt:
                ans = cnt
    print(f'#{test_case} {ans}')
```

---

# 2차원 배열

## 2차원 배열의 선언

- 1차원 List를 묶어놓은 List
- 2차원 이상의 다차원 List는 차원에 따라 Index를 선언
- 2차원 List의 선언
    - 세로길이(행의 개수)와 가로길이(열의 개수)를 필요로 함
- Python에서는 데이터 초기화를 통해 변수선언과 초기화가 가능함

<img width="886" alt="a_25" src="https://user-images.githubusercontent.com/86648892/184616746-f4f318a6-6f04-4be0-ab62-530355a7ff15.png">

<img width="882" alt="a_26" src="https://user-images.githubusercontent.com/86648892/184616761-7130e17e-f1b6-4aaa-a141-3e4a330121cb.png">

```python
# 2차원 배열 생성
N, M = int(input())
arr = [list(map(int, input())) for _ in range(N)]

# 2차원 배열 값 접근
for i in range(N): # 각 행에 대해
    for j in range(M): # 각 열에 접근해봐
        print(arr[i][j], end=' ')
    print()

# 2차원 배열 값 접근 2
N, M = int(input())
arr = [list(map(int, input())) for _ in range(N)]

for i in range(len(arr)):
    for j in range(len(arr[0])):
        print(arr[i][j], end=' ')
    print()
```

## 2차원 배열의 접근

### 행 우선 / 열 우선 / 지그재그 순회

<img width="1032" alt="a_27" src="https://user-images.githubusercontent.com/86648892/184616765-ebb8ad6c-556e-4886-a06b-50ffa207cd1a.png">

<img width="1020" alt="a_28" src="https://user-images.githubusercontent.com/86648892/184616774-4e6becbc-2d5b-49ff-852d-1fab3ea0414e.png">

- 위 지그재그의 경우
    - `i%2`는 짝수의 경우 나머지가 0이 되므로 짝수행에 대해 `(m-1-2*j)*(i%2)` 를 날려줌
    - `(m-1-2*j)` 인 이유는 j와 더해서 `Array[i][m-1-j]` 를 만들어주기 위함
        - `m-1-j` 인 이유는 가로 인덱스가 0에서 m-1까지인데 j가 0, 1, 2, 3 증가함에 따라 인덱스는 3, 2, 1, 0처럼 변화시키기 위함

### 델타를 이용한 2차 배열 탐색

<img width="826" alt="a_29" src="https://user-images.githubusercontent.com/86648892/184616783-075c5697-9c0b-4d28-b84d-cb738b86bc46.png">

- 어떤 원소를 중심으로 상하좌우 주변 원소들을 탐색하는 방법
- 오른쪽부터 시계방향으로 각각 0, 1, 2, 3 방향이라 가정
    - 순서는 정하기 나름이다
    - 혹은 문제의 조건에서 제시
- `di` 는 i에 더해주는 값
- `dj` 는 j에 더해주는 값
- `for i : 1 -> N-1`와 `for j : 1 -> N-1`은 `0 -> N-1` 로 수정할 것
- `ni` `nj` 은 이웃한 것의 좌표 위치
- 인덱스 검사하기
- `test(arr[ni][nj])` 는 접근한 이웃좌표에서 수행할 작업

<img width="378" alt="a_30" src="https://user-images.githubusercontent.com/86648892/184616786-23bff7ee-601f-4b5a-9ea8-2dff5cc5a1b9.png">

<img width="414" alt="a_31" src="https://user-images.githubusercontent.com/86648892/184616789-4701a805-5261-4141-b7fa-c4862a18c9bc.png">

```python
# 1
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N = 3
M = 4
arr = [[1, 2, 3, 4], [4, 5, 6, 8]]
for i in range(N):
    for j in range(M):
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<N and 0<=nj<M:
                print(ni, nj)

# 2
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N = 3
M = 4
arr = [[1, 2, 3, 4], [4, 5, 6, 8]]
for i in range(N):
    for j in range(M):
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0<=ni<N and 0<=nj<M:
                print(ni, nj)

# 3 (파리퇴치)
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N = 3
M = 4
arr = [[1, 2, 3, 4], [5, 6, 7, 8]]
for i in range(N):
    for j in range(M):
        for k in range(4):
            for d in range(1, 3): # 4방향 기준 1, 2, 3칸까지 탐색
                ni = i + di[k]*d
                nj = j + dj[k]*d
                if 0<=ni<N and 0<=nj<M:
                    print(ni, nj)
```

---

## 2차원 배열의 활용

### 전치 행렬

<img width="856" alt="a_33" src="https://user-images.githubusercontent.com/86648892/184616796-6fc3349f-37a9-45f7-9314-c6dec893e1af.png">

---

# 정렬

- 2개 이상의 자료를 특정 기준에 의해 작은 값부터 큰 값(오름차순: ascending), 혹은 그 반대의 순서대로(내림차순: descending) 재배열하는 것
- 키
    - 자료를 정렬하는 기준이 되는 특정 값

## 대표적인 정렬 방식의 종류

- 버블 정렬 (Bubble Sort)
- 카운팅 정렬 (Counting Sort)
- 선택 정렬 (Selection Sort)
- 퀵 정렬 (Quick Sort)
- 삽입 정렬 (Insertion Sort)
- 병합 정렬 (Merge Sort)

<img width="1212" alt="a_7" src="https://user-images.githubusercontent.com/86648892/184585478-830deb80-2040-41a1-879d-b3fac24911c4.png">

---

## 버블 정렬(Bubble Sort)

- 인접한 두 개의 원소를 비교하며 자리를 계속 교환하는 방식
- 정렬 과정
    - 첫번째 원소부터 인접한 원소끼리 계속 자리를 교환하면서 맨 마지막 자리까지 이동
    - 한 단계가 끝나면 가장 큰 원소가 마지막 자리로 정렬됨
    - 교환하며 자리를 이동하는 모습이 물 위에 올라오는 거품 모양과 같다고하여 버블 정렬이라 함
- 시간 복잡도
    - `O(n^2)`
        - 이중 for문

<img width="597" alt="a_8" src="https://user-images.githubusercontent.com/86648892/184585671-bca71a4c-813a-40c4-960d-8d312517bbba.png">

<img width="993" alt="a_9" src="https://user-images.githubusercontent.com/86648892/184585684-d5d22cb9-e090-4c38-bf2d-af46d6f75706.png">

<img width="779" alt="a_10" src="https://user-images.githubusercontent.com/86648892/184585691-221ce941-9106-4146-83a3-37d76c7ebf3f.png">

```python
N = int(input())

def BubbleSort(a, N):
    # 가장 오른쪽에서 출발하여 가장 왼쪽 바로 전까지 수행하면 되므로 (N-1, 0, -1)
    for i in range(N-1, 0, -1): # 구간의 맨 끝 인덱스부터 비교 시작
        for j in range(i): # 인접 원소 중 왼쪽 원소 인덱스까지 비교
            if a[j] > a[j+1]: # 오름차순, 더 큰 수를 오른쪽으로
                a[j], a[j+1] = a[j+1], a[j]
    return a
```

---

## 카운팅 정렬(Counting Sort)

- 항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세는 작업을 하여, 선형 시간에 정렬하는 효율적인 알고리즘
- 제한사항
    - 정수나 정수로 표현할 수 있는 자료에 대해서만 적용 가능
        - 각 항목의 발생 횟수를 기록하기 위해, 정수 항목으로 인덱스되는 카운트들의 배열을 사용하기 때문
    - 카운트들을 위한 충분한 공간을 할당하려면 집합 내의 가장 큰 정수를 알아야 함
- 시간 복잡도
    - `O(n+k)`
        - n은 리스트 길이
        - k는 정수의 최댓값

<img width="869" alt="a_11" src="https://user-images.githubusercontent.com/86648892/184585695-8a74133d-d1b7-4223-bbe4-21243ac94f1a.png">

- 보통 0이상 k이하의 정수가 주어진다는 조건이 붙음
- 0을 각각 초기값으로 갖는 count 배열을 만듬
    - 기존 정렬할 배열을 for문으로 순회
        - 카운트 배열에서 순회한 값을 인덱스로 하는 지점에 `+=1`
- indexError가 나지 않도록 길이에 주의

<img width="876" alt="a_12" src="https://user-images.githubusercontent.com/86648892/184585697-cb552a0a-2adf-40ed-8bc7-784f622237ae.png">

- 누적 개수 배열 만듬
- for문으로 순회하여 이전 counts와 자기자신 counts를 더해줌

<img width="785" alt="a_13" src="https://user-images.githubusercontent.com/86648892/184585698-f2092d3a-5c9b-4b21-9479-59ae301dcb15.png">

<img width="806" alt="a_14" src="https://user-images.githubusercontent.com/86648892/184585701-371bf425-2390-4948-b732-356bb6b55705.png">

<img width="745" alt="a_15" src="https://user-images.githubusercontent.com/86648892/184585702-a82f8b5a-2357-4fbd-a723-25ff632b24f9.png">

<img width="747" alt="a_16" src="https://user-images.githubusercontent.com/86648892/184585704-956ad373-a477-4335-9c7a-615da7871576.png">

- 원본 데이터와 같은 크기의 정렬된 결과를 넣은 배열을 만듬
- 해당 값을 인덱스로 가지는 counts 배열값을 감소시키고 temp에 삽입
    - 같은 값인데 뒤에 것부터 넣어주는것을 안정(stable) 정렬이라 함
        - 같은 값 간의 순서도 지켜줌

<img width="677" alt="a_17" src="https://user-images.githubusercontent.com/86648892/184585706-cd75191c-5768-4fbd-b294-25ed8716d4f9.png">

- 인덱스가 k까지 있어야 하니까 `[0] * (k+1)`
- 2번째는 count 배열 만들기
    - n번
- 3번째는 값을 누적하는 과정
    - k번
- 마지막은 정렬 과정
    - n번
- 시간복잡도 `n+k`

```python
# Counting Sort
# 입력된 배열의 카운트 값을 누적시킨 후
# 입력된 값을 인덱스로 활용 -> 해당 값에 해당하는 누적 카운트에 접근
# 접근한 누적 카운트를 인덱스로 활용 -> 해당 인덱스에 정렬용 배열 속으로 데이터 삽입
def CountingSort(A, B, k):
    # A는 입력할 배열 (k는 데이터 최대값)
    # B는 정렬된 배열
    # C는 카운트 배열
    C = [0]*(k+1) # 해당 인덱스에 k까지의 수를 나타내야 하므로 인덱스는 k+1까지
    
    # 카운트 배열 값 채우기
    for i in range(0, len(A)):
        C[A[i]] += 1

    # 카운트 배열 누적으로 전환
    for i in range(1, len(C)):
        C[i] += C[i-1]
    
    # 원본을 뒤에서부터 빼주면서 정렬
    # 왼쪽 끝의 값까지 확인해야 하므로 end 범위는 -1까지
    for i in range(len(B)-1, -1, -1):
        C[A[i]] -= 1
        # 해당 카운트의 위치에 값 삽입
        B[C[A[i]]] = A[i]
    return B

k = int(input())
arr2 = [4, 3, 1, 1, 7, 6, 7, 5, 7]
tmp = [0]*len(arr2)
print(CountingSort(arr2, tmp, k))
```

---

## 선택 정렬(Selection Sort)

- 주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식
- 정렬 과정
    - 주어진 리스트 중에서 최소값을 찾음
        - 오름차순 기준
    - 그 값을 리스트의 맨 앞에 위치한 값과 교환
    - 맨 처음 위치를 제외한 나머지 리스트를 대상으로 위의 과정을 반복
- 시간 복잡도
    - `O(n2)`

<img width="1169" alt="a_51" src="https://user-images.githubusercontent.com/86648892/184630913-fe0f0adf-ddd1-4ce2-81dc-40e69b90bee3.png">

<img width="1187" alt="a_52" src="https://user-images.githubusercontent.com/86648892/184630927-689319ee-b724-4856-8433-f384213b643e.png">

<img width="843" alt="a_53" src="https://user-images.githubusercontent.com/86648892/184630938-9f420741-c52c-422d-87dd-d387b4c8e763.png">

## 셀렉션 알고리즘(Selection Algorithm)

- 저장되어 있는 자료로부터 k번째로 큰 혹은 작은 원소를 찾는 방법을 셀렉션 알고리즘이라 함
    - 최소값, 최대값, 혹은 중간값을 찾는 알고리즘을 의미하기도 함
- 선택 과정
    - 셀렉션은 아래와 같은 과정을 통해 이루어짐
        - 정렬 알고리즘을 이용하여 자료 정렬
        - 원하는 순서에 있는 원소 가져오기

<img width="1208" alt="a_54" src="https://user-images.githubusercontent.com/86648892/184630940-be2b8e12-7603-4f69-a178-cc892bcc63af.png">

## **달팽이 숫자**

<img width="649" alt="a_55" src="https://user-images.githubusercontent.com/86648892/184632687-d64302a9-1ba1-40fc-8538-2979c4f8717d.png">

<img width="766" alt="a_56" src="https://user-images.githubusercontent.com/86648892/184632696-e7c6d66d-237d-4ed4-89fd-41954c164239.png">

<img width="917" alt="a_57" src="https://user-images.githubusercontent.com/86648892/184632703-6e8f5747-1657-446a-a686-998e6803f3d0.png">

```python
'''
수업 풀이를 통한 개선점
1) array에서 값을 빼내 출력할 때 언패킹 연산자(*) 활용
2) % 연산자를 활용한 방향 전환
3) di, dj 초기화 위치
4) cnt += 1을 while 바깥에 한번 진행해주고 while의 범위를 <=으로 설정하여 직관성 상승
'''

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    # 초기 배열 생성
    arr = [[0] * N for _ in range(N)]
    # direction은 우->하->좌->상 순 시계방향으로 0, 1, 2, 3
    direction = 0
    i, j = 0, 0
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    # 출발 지점에 1을 놓고 cnt도 1인 상태로 시작
    cnt = 1
    arr[0][0] = 1
    # cnt 값을 최신화하고 넣어주는 logic이니까 가령 4*4인 경우 15일 때까지만 loop 허용(안에 들어가서 16이 될테니)
    while cnt < N*N:
        # 현재 방향 기준으로 다음 좌표 설정
        ni = i + di[direction]
        nj = j + dj[direction]
        # 좌표가 전체 범위를 넘지 않는다면
        if 0 <= ni < N and 0 <= nj < N:
            # 그리고 도착할 다음 좌표의 값이 0이라면 (아직 도착하지 않은 곳이라면)
            if arr[ni][nj] == 0:
                # 카운트 값을 올려주고 해당 값을 도착할 값에 부여, 그리고 새로운 좌표를 기준점으로 업데이트
                cnt += 1
                arr[ni][nj] = cnt
                i, j = ni, nj
            # 조건이 만족하지 않는 경우 (도착할 값이 0이 아닌 경우)
            else:
                # 방향이 위로 향하고 있는 경우
                if direction == 3:
                    # 잘못 최신화된 ni, nj 좌표를 다시 바로 잡아주고
                    ni -= di[direction]
                    nj -= dj[direction]
                    # 상 -> 우로 방향 전환
                    direction = 0
                    # 다시 ni, nj 최신화
                    ni += di[direction]
                    nj += dj[direction]
                    # 이동 작업 수행
                    cnt += 1
                    arr[ni][nj] = cnt
                    i, j = ni, nj
                # 다른 방향인 경우
                else:
                    ni -= di[direction]
                    nj -= dj[direction]
                    # 방향값에 1을 더해주어 시계방향으로 방향 전환
                    direction += 1
                    ni += di[direction]
                    nj += dj[direction]
                    cnt += 1
                    arr[ni][nj] = cnt
                    i, j = ni, nj
        # 조건이 만족하지 않는 경우 (범위를 초과한 경우)
        else:
            if direction == 3:
                ni -= di[direction]
                nj -= dj[direction]
                direction = 0
                ni += di[direction]
                nj += dj[direction]
                cnt += 1
                arr[ni][nj] = cnt
                i, j = ni, nj
            else:
                ni -= di[direction]
                nj -= dj[direction]
                direction += 1
                ni += di[direction]
                nj += dj[direction]
                cnt += 1
                arr[ni][nj] = cnt
                i, j = ni, nj
    print(f'#{test_case}')
    for line in arr:
        for number in line:
            print(number, end = ' ')
        print()

'''
교수님 풀이

# 고정된 값이니 한 번만 초기화하는게 속도에 유리하므로 밖으로 빼주자
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
# T = 10
for test_case in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    i = j = dr = 0
    cnt = 1
    arr[i][j] = cnt
    # 내 풀이와는 다르게 밖에서 cnt += 1을 해주고 while 범위에 =을 붙여줌
    cnt += 1

    while cnt <= N*N:
        ni, nj = i+di[dr], j+dj[dr] # 이동할 좌표계산
        if 0<=ni<N and 0<=nj<N and arr[ni][nj]==0: # 기록가능: 범위내이고 0이면
            i, j = ni, nj # 현재좌표 이동
            arr[i][j] = cnt
            cnt += 1
        else: # 불가능 -> 방향전환 후 기록
            # dr을 %를 통해 바꾸는 방법 알아두자
            dr = (dr+1)%4

    print(f'#{test_case}')
    for lst in arr:
        # 언패킹 연산자(asterisk) 활용
        print(*lst)
'''
```

---

## 완전검색 (Exhaustive Search)

- 완전 검색 방법은 문제의 해법으로 생각할 수 있는 모든 경우의 수를 나열해보고 확인하는 기법
    - 경우의 수를 만드는 방법은 순열, 조합, 부분집합
- Brute-force 혹은 generate-and-test 기법이라고도 불림
- 모든 경우의 수를 테스트한 후, 최종 해법을 도출함
- 일반적으로 경우의 수가 상대적으로 작을 때 유용함
- 모든 경우의 수를 생성하고 테스트하기때문에 수행 속도는 느리지만, 해답을 찾아내지 못할 확률이 작음
- 자격검정평가 등에서 주어진 문제를 풀 때, 우선 완전 검색으로 접근하여 해답을 도출한 후
    - 성능 개선을 위해 다른 알고리즘을 사용하고 해답을 확인하는 것이 바람직함

### 완전검색을 활용한 Baby-gin 접근

<img width="1148" alt="a_18" src="https://user-images.githubusercontent.com/86648892/184605028-6b852f34-6710-44b5-ac4f-3251302f647c.png">

### **순열(Permutation)**

- 완전검색을 할 경우 경우의 수를 만드는 방법 중 하나
- 연산량이 얼마나 될지 짐작할 수 있음

<img width="1127" alt="a_19" src="https://user-images.githubusercontent.com/86648892/184605050-c0b92245-7bf8-4d99-ba80-4ab31016cf85.png">

<img width="1102" alt="a_20" src="https://user-images.githubusercontent.com/86648892/184605055-98c85a29-ed89-45d4-8936-2b98937afe5d.png">

---

## 탐욕(Greedy) 알고리즘

- 탐욕 알고리즘은 최적해를 구하는데 사용되는 근시안적인 방법
- 여러 경우 중 하나를 결정해야 할 때마다 그 순간에 최적이라고 생각되는 것을 선택해나가는 방식으로 진행하여 최종적인 해답에 도달
- 각 선택의 시점에서 이루어지는 결정은 지역적으로는 최적이지만, 그 선택들을 계속 수집하여 최종적인 해답을 만들었다고 하여, 그것이 최적이라는 보장은 없음
- 일반적으로, 머릿속에 떠오르는 생각을 검증없이 바로 구현하면 Greedy 접근이 된다

### 탐욕 알고리즘의 동작 과정

1. 해 선택
    - 현재 상태에서 부분 문제의 최적 해를 구한 뒤, 이를 부분해 집합(Solution Set)에 추가
2. 실행 가능성 검사
    - 새로운 부분해 집합이 실행 가능한지를 확인
    - 곧, 문제의 제약 조건을 위반하지 않는지를 검사
3. 해 검사
    - 새로운 부분해 집합이 문제의 해가 되는지를 확인
    - 아직 전체 문제의 해가 완성되지 않았다면 1)의 해 선택부터 다시 시작

### 예시(거스름돈 줄이기)

- 어떻게 하면 손님에게 거스름돈으로 주는 지폐와 동전의 개수를 최소한으로 줄일 수 있을까?
1. 해 선택
    - 여기에서는 멀리 내다볼 것 없이 가장 좋은 해를 선택한다
    - 단위가 큰 동전으로만 거스름돈을 만들면 동전의 개수가 줄어드므로 현재 고를 수 있는 가장 단위가 큰 동전을 하나 골라 거스름돈에 추가한다
2. 실행 가능성 검사
    - 거스름돈이 손님에게 내드려야 할 액수를 초과하는지 확인
    - 초과한다면 마지막에 추가한 동전을 거스름돈에서 빼고
        - 1)로 돌아가서 현재보다 한 단계 작은 단위의 동전을 추가
3. 해 검사
    - 거스름돈 문제의 해는 당연히 거스름돈이 손님에게 내드려야 하는 액수와 일치하는 셈
    - 더 드려도, 덜 드려도 안되기에 거스름돈을 확인해서 액수에 모자라면
        - 다시 1)로 돌아가서 거스름돈에 추가할 동전을 고른다

### 탐욕 알고리즘을 활용한 Baby-gin 접근

<img width="1124" alt="a_21" src="https://user-images.githubusercontent.com/86648892/184608280-dcdc2881-9472-43e6-a5fb-e2749f7a7bcb.png">

<img width="1165" alt="a_22" src="https://user-images.githubusercontent.com/86648892/184608305-1f244f0b-547b-4e0b-9b1f-1ded52450638.png">

<img width="1172" alt="a_23" src="https://user-images.githubusercontent.com/86648892/184608310-caece9f2-4755-4872-b8da-772fd4394ab6.png">

<img width="1191" alt="a_24" src="https://user-images.githubusercontent.com/86648892/184608311-770adbf0-1c69-4e77-a84f-697775186f92.png">

---

## 부분집합의 합 (Subset Sum)

- 유한 개의 정수로 이루어진 집합이 있을 때, 이 집합의 부분집합 중에서 그 집합의 원소를 모두 더한 값이 0이 되는 경우가 있는지를 알아내는 문제
- `[-7, -3, -2, 5, 8]` 은 -3, -2, 5의 경우로 인해 참
- 완전검색 기법으로 부분집합 합 문제를 풀기 위해서는, 우선 집합의 모든 부분집합을 생성한 후에 각 부분집합의 합을 계산해야 함
- 집합의 원소가 n개일 때, 공집합을 포함한 부분집합의 수
    - `2^n`

<img width="1210" alt="a_34" src="https://user-images.githubusercontent.com/86648892/184624699-53c9118d-4ab9-4165-b0b7-4dd915599872.png">

---

## 비트 연산자

<img width="1118" alt="a_35" src="https://user-images.githubusercontent.com/86648892/184624725-c71d4102-7400-4225-be06-5ad907232d7e.png">

- 비트는 메모리 상에서 정보를 구분할 수 있는 최소 단위
- 주소로 구분되는 최소 단위는 바이트
    - 8bit는 1Byte
    - bit는 binary digit의 약자 (이진수)
- 비트 연산자는 같은 비트끼리 연산을 함

<img width="352" alt="a_36" src="https://user-images.githubusercontent.com/86648892/184624729-638c4085-88b2-431b-a381-5853b96e4cef.png">

- `1<<n` 은 1을 n번 왼쪽으로 옮기라는 것
- 비트 쉬프트

<img width="592" alt="a_37" src="https://user-images.githubusercontent.com/86648892/184624730-f7bd27e1-b464-42c2-90f5-29f97e4d03b2.png">

- `&`
    - 필요한 비트만 1로 유지시키고 나머지는 0으로 만들기 위해 and 연산 사용
    - 비트마스킹

<img width="696" alt="a_38" src="https://user-images.githubusercontent.com/86648892/184624734-4cf8dccc-0f35-4c15-933d-881596f348ad.png">

- i의 j번 비트를 검사
    - `i&(1<<j)`

### **비트연산자로 부분집합 구현**

```python
'''
10개의 정수를 입력 받아 부분집합의 합이 0이 되는 것이 존재하는지를 계산하는 함수를 작성해보자.
입력
2
19 6 16 19 15 16 8 13 16 10
-20 -6 -13 3 -19 -9 19 -3 9 4
출력
#1 0
#2 1
'''
# 합해서 특정값 k가 된다고 생각해보자
# 해당 index의 값을 사용하지 않는다(0), 사용한다(1)로 각각의 원소에 적용할 수 있음

# 1) bit는 2^n-1까지의 이진수들 # 그리고 이 bit는 각각의 부분집합을 나타내는 숫자 (사용여부 0, 1로 나타내는)
# 2) 부분집합 합이 0이 되는지 판단하기 위해 sm 초기화
# 3) bit >> i # bit 수를 i만큼 오른쪽으로 shift하여 해당 자리 수의 비트 값만 남겨놓고 1과 & 연산
# 3-1) 해당 자리의 비트 수가 1이면, 즉 있으면 True, 그리고 해당 값을 sm에 더해줌
# 3-2) 해당 자리의 비트 수가 0이면, 즉 없으면 False, 그리고 해당 값을 sm에 더해주지 않음
# List의 Index는 편의상 뒤에서부터 부여하자 (N-1, N-2, ... , 3, 2, 1, 0)
T = int(input())
for test_case in range(1, T+1):
    lst = list(map(int, input().split()))
    N = len(lst) #N bit (Lst member: N)
    ans = 0
    k = 0 # 찾아야 될 숫자를 k라 가정
    '''
    for i in range(1<<N):
        sm = 0
        # 내가 보려는 자리를 지칭
        for j in range(N):
            if i & (1<<j):
                sm += lst[j]
    '''
    for bit in range(1, 2**N): # == 1 << N
        sm = 0
        for i in range(0, N): # every Lst index
            if (bit>>i) & 1: # i만큼 shift하여 해당 인덱스 값만 판단
                sm += lst[i] # 부분집합에 있으면 더해줌
        if sm == k: # 부분집합의 합이 목표값(0)과 같다면
            ans += 1 # 맞음을 표시하는 1 표시
            break
    print(f'#{test_case} {ans}')
```

---

# 검색(Search)

- 저장되어 있는 자료 중에서 원하는 항목을 찾는 작업
- 목적하는 탐색 키를 가진 항목을 찾는 것
    - 탐색 키(search key): 자료를 구별하여 인식할 수 있는 키
- 검색의 종류
    - 순차 검색(sequential search)
    - 이진 검색(binary search)
    - 해쉬(hash)

## 순차 검색(Sequential Search)

- 일렬로 되어있는 자료를 순서대로 검색하는 방법
    - 가장 간단하고 직관적인 검색 방법
    - 배열이나 연결 리스트 등 순차구조로 구현된 자료구조에서 원하는 항목을 찾을 때 유용
    - 알고리즘이 단순하여 구현이 쉽지만
        - 검색 대상의 수가 많은 경우 수행시간이 급격히 증가하여 비효율적
- 2가지 경우
    - 정렬되어 있지 않은 경우
    - 정렬되어 있는 경우

### 정렬되어 있지 않은 경우

- 검색 과정
    - 첫번째 원소부터 순서대로 검색 대상과 키 값이 같은 원소가 있는지 비교하며 찾음
    - 키 값이 동일한 원소를 찾으면 그 원소의 인덱스를 반환
    - 자료구조의 마지막에 이를 때까지 검색 대상을 찾지 못하면 검색 실패

<img width="771" alt="a_39" src="https://user-images.githubusercontent.com/86648892/184626689-60635380-080d-4839-8d21-eae29c00050a.png">

<img width="780" alt="a_40" src="https://user-images.githubusercontent.com/86648892/184626695-ba4fd636-3e5d-4606-a625-2ce1c97c46ee.png">

<img width="865" alt="a_41" src="https://user-images.githubusercontent.com/86648892/184626697-3b764b8d-b447-47ab-8304-223909a61217.png">

### 정렬되어 있는 경우

- 검색 과정
    - 자료가 오름차순으로 정렬된 상태에서 검색을 실시한다고 가정
    - 자료를 순차적으로 검색하면서 키 값을 비교하여, 원소의 키 값이 검색 대상의 키 값보다 크면 찾는 원소가 없다는 것이므로 더 이상 검색하지 않고 검색을 종료

<img width="820" alt="a_42" src="https://user-images.githubusercontent.com/86648892/184626700-c3304dac-424f-4752-8e4b-2eaa8d2b8e73.png">

<img width="817" alt="a_43" src="https://user-images.githubusercontent.com/86648892/184626702-11621a31-b69c-4b7e-8ec9-7f6f2968e673.png">

<img width="849" alt="a_44" src="https://user-images.githubusercontent.com/86648892/184626705-e2bd30a4-e671-4304-a0f4-c566dbe6e767.png">

---

## 이진 검색(Binary Search)

- 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법
    - 목적 키를 찾을 때까지 이진 검색을 순환적으로 반복 수행함으로써 검색 범위를 반으로 줄여가면서 보다 빠르게 검색을 수행함
- 이진 검색을 하기 위해서는 자료가 정렬된 상태여야 함
- 검색 과정
    - 자료의 중앙에 있는 원소를 고름
    - 중앙 원소의 값과 찾고자 하는 목표 값을 비교
    - 목표 값이 중앙 원소의 값보다 작으면 자료의 왼쪽 반에 대해서 새로 검색을 수행
        - 크다면 자료의 오른쪽 반에 대해서 새로 검색을 수행
    - 찾고자 하는 값을 찾을 때까지 위의 과정을 반복

<img width="805" alt="a_45" src="https://user-images.githubusercontent.com/86648892/184626706-f2fb79d5-700e-4386-ab32-749409b85007.png">

<img width="839" alt="a_46" src="https://user-images.githubusercontent.com/86648892/184626708-b1c6ba28-bd0e-474a-a194-e1f722c8f4c4.png">

<img width="1013" alt="a_47" src="https://user-images.githubusercontent.com/86648892/184626710-d10f6a54-7859-44c9-98f4-ec47cd98a39a.png">

- 검색 범위의 시작점과 종료점을 이용하여 검색을 반복 수행함
- **이진 검색의 경우, 자료에 삽입이나 삭제가 발생했을 때 배열의 상태를 항상 정렬 상태로 유지하는 추가 작업이 필요함**

<img width="837" alt="a_48" src="https://user-images.githubusercontent.com/86648892/184626711-91a1d632-cf9f-4d22-8a0c-408a9c68a95d.png">

- `start<=end` 에서 등호가 들어가야 함
    - start와 end가 같아지는 경우, 원소가 하나 남은 경우도 작업을 수행해야 하기 때문

### 재귀함수를 이용한 이진검색 구현

<img width="843" alt="a_49" src="https://user-images.githubusercontent.com/86648892/184626714-9c7daf0f-c312-4091-b47f-4b151c537bdd.png">

- 재귀로 이진탐색 구현이 가능하다 정도
- 효율이 떨어지므로 기본적인 반복구조로 이진탐색을 구현하자

---

# 인덱스

- 인덱스라는 용어는 Database에서 유래했으며, 테이블에 대한 동작 속도를 높여주는 자료구조를 일컫는다. Database 분야가 아닌 곳에서는 Look up table 등의 용어를 사용하기도 한다
- 인덱스를 저장하는데 필요한 디스크 공간은 보통 테이블을 저장하는데 필요한 디스크 공간보다 작음
    - 왜냐하면 보통 인덱스는 키-필드만 갖고 있고, 테이블의 다른 세부 항목들은 갖고 있지 않기 때문
- 배열을 사용한 인덱스
    - 대량의 데이터를 매번 정렬하면, 프로그램의 반응은 느려질 수 밖에 없음
    - 이러한 대량 데이터의 성능 저하 문제를 해결하기 위해 배열 인덱스를 사용할 수 있음

<img width="886" alt="a_50" src="https://user-images.githubusercontent.com/86648892/184628827-d69d2f75-7a08-439f-b985-2bf9e27a4b4a.png">

---

# 문자열(String)

- 문자열
- 패턴 매칭
- 문자열 암호화
- 문자열 압축

---

## 문자의 표현

### 컴퓨터에서의 문자표현

- 글자 A를 메모리에 저장하는 방법?
- 메모리는 숫자만을 저장할 수 있기에 A라는 글자 모양 그대로 비트맵으로 저장하는 방법을 사용하지 않는 한(메모리 낭비가 심하다) 각 문자에 대해서 대응되는 숫자를 정해 놓고 이것을 메모리에 저장하는 방법을 사용
- 영어가 대소문자 합쳐서 52이므로 6비트(64가지)면 모두 표현할 수 있음
    - 이를 코드체계라 한다
    - 가령 00000은 ‘a’, 000001은 ‘b’를 나타냄
    - 네트워크가 발전되기 전 미국의 각 지역 별 코드체계를 정해놓고 사용했지만
    - 네트워크(인터넷: 인터넷은 미국에서 발전했다)의 발전으로 인해 서로 정보를 주고 받을 때 정보를 달리 해석한다는 문제 발생
    - 혼동을 피하기 위해 표준안을 만들기로 함
    - 그렇게 1967년 미국에서 ASCII(American Standard Code for Information Interchange)라는 문자 인코딩 표준이 제정됨
- ASCII는 7bit 인코딩으로 128문자를 표현하며 33개의 출력 불가능한 제어 문자들과 공백을 비롯한 95개의 출력 가능한 문자들로 이루어져 있음

### ASCII

<img width="1135" alt="a_58" src="https://user-images.githubusercontent.com/86648892/184694444-b485df0a-d3df-4233-9a7a-bb220f26a901.png">

<img width="1184" alt="a_59" src="https://user-images.githubusercontent.com/86648892/184694466-fdf641d1-510a-4f59-af3a-5ad27aef6861.png">

<img width="1103" alt="a_60" src="https://user-images.githubusercontent.com/86648892/184694473-c05e02dd-1a36-47e8-8463-a611d3426f72.png">

### UNICODE

- 오늘날 대부분의 컴퓨터는 문자를 읽고 쓰는데 ASCII형식을 사용
- 그런데 컴퓨터의 발전에 따라 미국 외 국가에서도 컴퓨터가 발전하여 각 국가들은 자국의 문자를 표현하기 위해 코드체계를 만들어 사용하게 됨
    - 우리나라도 예전에 한글 코드체계를 만들어 사용했고, 조합형, 완성형 두 종류를 가지고 있었음
- 인터넷이 전 세계로 발전하면서 ASCII를 만들었을 때의 문제와 같은 문제가 국가 간에 정보를 주고 받을 때 발생함
- 다국어 처리를 위해 표준을 마련했고, 이를 유니코드라 한다

<img width="1060" alt="a_61" src="https://user-images.githubusercontent.com/86648892/184694477-0ea5fe8d-649c-4e5d-8d6e-43d7e5901788.png">

<img width="1145" alt="a_62" src="https://user-images.githubusercontent.com/86648892/184694482-0b31ee50-2c61-49cb-a9ae-423d177a521a.png">

<img width="1091" alt="a_63" src="https://user-images.githubusercontent.com/86648892/184694486-c81534a6-48c8-4b23-907f-6af467f46811.png">

- 엔디언(Endianess)은 컴퓨터의 메모리와 같은 1차원의 공간에 여러 개의 연속된 대상을 배열하는 방법을 뜻함
    - 바이트를 배열하는 방법을 특히 바이트 순서(Byte order)라 한다
- 엔디언은 보통 큰 단위가 앞에 나오는 Big-endian과 작은 단위가 앞에 나오는 Little-endian으로 나눌 수 있음
    - 빅 엔디언은 사람이 숫자를 쓰는 방법과 같이 큰 단위의 바이트가 앞에 오는 방법
    - 리틀 엔디언은 반대로 작은 단위의 바이트가 앞에 오는 방법
    
    <img width="626" alt="a_64" src="https://user-images.githubusercontent.com/86648892/184694491-7e652c99-d3cf-4f68-83b1-b2c6755640c7.png">
    
    <img width="614" alt="a_65" src="https://user-images.githubusercontent.com/86648892/184694493-fe3e0d1f-ecb2-47cd-a7c5-99ed7a26e23c.png">
    

<img width="1179" alt="a_66" src="https://user-images.githubusercontent.com/86648892/184694497-e52805f8-fcf9-4e5e-bec1-b7a20c73d6f2.png">

<img width="1177" alt="a_67" src="https://user-images.githubusercontent.com/86648892/184694501-9254ae4f-26e4-450f-8c88-9c0c99139d59.png">

---

## 문자열의 분류 및 처리

<img width="1030" alt="a_68" src="https://user-images.githubusercontent.com/86648892/184694505-743c4dd7-92b1-4a5b-bc5d-2d2383b43714.png">

<img width="1115" alt="a_69" src="https://user-images.githubusercontent.com/86648892/184694509-54dbe87c-92d6-4867-bd20-269f65bbd3bc.png">

<img width="1098" alt="a_70" src="https://user-images.githubusercontent.com/86648892/184694510-aea7cd4a-e334-4fa0-875e-8b9c05d91cbc.png">

<img width="1164" alt="a_71" src="https://user-images.githubusercontent.com/86648892/184694512-cfb0b734-e2a0-4c2a-b7c8-9b6a77c06e00.png">

---

### **문자열 뒤집기**

<img width="1117" alt="a_72" src="https://user-images.githubusercontent.com/86648892/184694516-63e222fc-c021-49e8-8b7e-8ef4b515eb30.png">

<img width="1151" alt="a_73" src="https://user-images.githubusercontent.com/86648892/184694517-4e5c5a74-e885-43a1-b424-b4578379328d.png">

```python
string = 'Reverse this strings'
reversed_str = ''
for i in string:
    reversed_str = i + reversed_str
print(reversed_str) # sgnirts siht esreveR
```

---

### **문자열 비교**

<img width="1186" alt="a_74" src="https://user-images.githubusercontent.com/86648892/184694518-57cb1287-055d-4126-9bde-113bb528efcf.png">

```python
s1 = 'abc'
s2 = 'abc'
s3 = 'def'
s4 = s1
s5 = s1[:2] + 'c'

print(s1==s2) # True
print(s1==s3) # False
print(s1==s4) # True
print(s1==s5) # True
print(s1 is s2) # True
print(s1 is s3) # False
print(s1 is s4) # True
print(s1 is s5) # False
```

---

### **문자열 숫자를 정수로 변환하기**

<img width="1133" alt="a_75" src="https://user-images.githubusercontent.com/86648892/184694520-fbf73c40-ab17-4a2f-b4cf-9379cd030ad8.png">

### int()와 같은 atoi()함수, str()과 같은 itoa()함수 구현

```python
# int(str) 구현
def atoi(s):
    i = 0
    for char in s:
        i = i * 10 + ord(char) - ord('0') # 1 -> 10으로, 10 + 2 -> 12 -> 120으로, 120 + 3 -> 123
    return i

# str(int) 구현
# 나머지 연산자를 활용하여 뒤에서부터 잘라주기
def itoa(i):
    st = ''
    while i > 0:
        st = chr(i%10 + ord('0')) + st
        i //= 10
    return st

num = 123
word = '123'
atoi(word)
print(atoi(word)) # 123
print(type(atoi(word))) # <class 'int'>
print(itoa(num)) # 123
print(type(itoa(num))) # <class 'str'>
```

---

# Pattern Matching

## 고지식한 알고리즘(Brute Force)

- 완전탐색을 하는 방법
- 할 수 있어야 함

<img width="1089" alt="a_76" src="https://user-images.githubusercontent.com/86648892/184694522-23be5ca3-da15-4ad2-aae3-43e245b66335.png">

<img width="1109" alt="a_77" src="https://user-images.githubusercontent.com/86648892/184694526-926eab52-7c5f-4417-aaaf-26172e85328d.png">

<img width="1171" alt="a_78" src="https://user-images.githubusercontent.com/86648892/184694527-ab30a33e-f6d2-4d07-83e5-b7475a14f386.png">

<img width="1147" alt="a_79" src="https://user-images.githubusercontent.com/86648892/184694530-f92da276-693b-4e35-9d14-3c120f458a13.png">

- 최악의 경우 텍스트의 모든 위치에서 패턴을 비교해야함
    - 시간복잡도 `O(MN`)
- 비교횟수를 줄이는 방법은?

### Brute Force 코드 예시

```python
def matched(st, p, N, M, start):
    for j in range(M): # j만큼 (p가 포함되어있는지 끝까지 순회하는동안)
        if p[j] != st[start+j]: # 다른 것이 나오면 매칭이 안된 것
            return 0
    return 1 # p를 순회하는동안 다른 것이 안나왔으므로 매칭 # 이것을 start를 옮겨가며 반복

# A가 전체 텍스트 B가 포함되어있는지 확인할 텍스트
A, B = input().split()
N, M = len(A), len(B)
cnt = 0 # B가 A에 포함되어 있는 수 # pattern matching

# B가 포함되어 있는 수 산출
for start in range(N-M+1):
    if matched(A, B, N, M, start):
        cnt += 1

print(cnt)

'''
입력
asakusa sa
banana bana
saaaa aa
aaaas aa
aaaaa aa
'''

'''
출력
2
1
3
3
4
'''

# 위 접근은 해당 패턴을 중복해서 세기 때문에 중복을 허용하지 않는 경우 조건을 추가하거나 다른 접근 방법을 고려하자
```

---

## KMP 알고리즘

<img width="1191" alt="a_80" src="https://user-images.githubusercontent.com/86648892/184694531-de771e4a-877d-42ae-8181-bb0090672dca.png">

<img width="1167" alt="a_81" src="https://user-images.githubusercontent.com/86648892/184694533-b1f442e0-6012-4221-a9b8-328efdd66119.png">

<img width="1179" alt="a_82" src="https://user-images.githubusercontent.com/86648892/184694534-3f5d5d15-4f22-4c6f-b74b-4e603f26a622.png">

---

## 보이어-무어 알고리즘

<img width="1203" alt="a_83" src="https://user-images.githubusercontent.com/86648892/184694536-03166f09-d9af-430b-af62-55c3a97ad269.png">

<img width="1210" alt="a_84" src="https://user-images.githubusercontent.com/86648892/184694539-a95eeec8-c113-4af8-97ff-2f0b809ce15e.png">

<img width="1214" alt="a_85" src="https://user-images.githubusercontent.com/86648892/184694542-39f51a85-132b-427a-8bd5-e35a04cc1503.png">

---

## 문자열 패턴 매칭 알고리즘 비교

<img width="1199" alt="a_86" src="https://user-images.githubusercontent.com/86648892/184694545-88478e1f-4460-4330-befa-3ec31eba1384.png">

<img width="1204" alt="a_87" src="https://user-images.githubusercontent.com/86648892/184694548-74063d3c-b9f3-4ec2-83f9-2d978ecbd4e3.png">

---

# 문자열 암호화

## 시저 암호(Casesar cipher)

<img width="1129" alt="a_88" src="https://user-images.githubusercontent.com/86648892/184694550-3a351b32-024b-4bf3-88f2-6026c848d676.png">

<img width="1098" alt="a_89" src="https://user-images.githubusercontent.com/86648892/184694554-999fc674-0fc3-4d3a-910c-8463c3631733.png">

<img width="1030" alt="a_90" src="https://user-images.githubusercontent.com/86648892/184694558-e4b76a71-d3aa-4d34-b7be-0cef9c5cdf23.png">

## 단일 치환 암호

<img width="940" alt="a_91" src="https://user-images.githubusercontent.com/86648892/184694559-ad74d7d1-62d9-4a57-b535-081377433e30.png">

<img width="1097" alt="a_92" src="https://user-images.githubusercontent.com/86648892/184694560-d4130919-8764-4854-bc39-eff7f58a35d0.png">

- 복호화는 decoding을 의미함

## bit열의 암호화

<img width="1008" alt="a_93" src="https://user-images.githubusercontent.com/86648892/184694562-62d56ec2-25c9-4347-9e8a-10c822b5c0c6.png">

---

# 문자열 압축

<img width="1055" alt="a_94" src="https://user-images.githubusercontent.com/86648892/184694564-ece2dd13-f825-4baa-845a-06c7866077ce.png">

---

# 스택

- 스택
- 재귀호출
- Memoization
- DP
- DFS

---

## 스택(stack)의 특성

- 물건을 쌓아 올리듯 자료를 쌓아 올린 형태의 자료구조
- 스택에 저장된 자료는 선형 구조를 갖는다
    - 선형구조: 자료 간의 관계가 1대1의 관계를 갖는다
    - 비선형구조: 자료 간의 관계가 1대N의 관계를 갖는다
        - ex) 트리
- 스택에 자료를 삽입하거나 스택에서 자료를 꺼낼 수 있음
- LIFO(Last-In-First-Out)
    - 후입선출
    - 마지막에 삽입한 자료를 가장 먼저 꺼낸다

## 스택의 구현

### 자료구조

- 자료를 선형으로 저장할 저장소
- 배열을 사용할 수 있음
- 저장소 자체를 스택이라 부르기도 한다
    - 우리가 구현한 것 외에 컴퓨터 메모리 중 스택으로 동작하는 것이 있음
- 스택에서 마지막 삽입된 원소의 위치를 top이라 부름
    - stack pointer

### 연산

- 삽입
    - push
    - 저장소에 자료를 저장
- 삭제
    - pop
    - 저장소에서 자료를 꺼냄
    - 꺼낸 자료는 삽입한 자료의 역순으로 꺼냄
- isEmpty
    - 스택이 공백인지 아닌지를 확인하는 연산
    - 스택이 비어있는데 pop하면 안되므로 그 때 사용
- peek
    - 스택의 top에 있는 item(원소)을 반환하는 연산

### 스택의 삽입 / 삭제 과정

<img width="882" alt="a_95" src="https://user-images.githubusercontent.com/86648892/185070245-74c63a50-6a17-44bb-8851-c5e753d3604e.png">

- push는 2개의 동작
    - top을 증가시키고
    - 해당 데이터를 넣음
- pop도 2개의 동작
    - top을 감소시키고
    - 해당 데이터를 뺌

### 스택의 push 알고리즘

<img width="885" alt="a_96" src="https://user-images.githubusercontent.com/86648892/185070269-673195e7-60ed-4e4f-ad19-b53868318dae.png">

<img width="868" alt="a_97" src="https://user-images.githubusercontent.com/86648892/185070270-d7ab906e-ca85-419e-adc5-3c6f881a59f9.png">

- 스택의 size와 stack pointer를 지정하자
    - 보통 size를 우선 지정하고 초기화
    - top 역시 지하를 가리키도록 -1로 초기화
- `if top==size` 를 통해 오버플로우를 방지
    - 일종의 디버깅용
- 아이템 삽입
    - `push(10, size)` 과 같이 호출을 통해 삽입
    - `top += 1` 과 `stack[top] = 20` 2줄로 삽입 구현 가능

### 스택의 pop 알고리즘

<img width="903" alt="a_98" src="https://user-images.githubusercontent.com/86648892/185070275-4a8f348b-27d5-4e9b-a0ec-c13dacf64db0.png">

<img width="891" alt="a_99" src="https://user-images.githubusercontent.com/86648892/185070277-c00cfc77-7eee-4415-8155-3e929ca28a2c.png">

- LIFO이므로 `s.pop(-1)`
- `top -= 1` 과 `stack[top+1]` 로도 구현 가능
    - top이 지정하는 위치를 하나 줄여주고
    - 그 전에 지정하던(1칸 위) 아이템을 반환
- 마지막 줄 `stack[top]` 은 `stack[top+1]` 로 수정

```python
stackSize = 10
stack = [0] * stackSize
top = -1

# push(1)
top += 1
stack[top] = 1

# push(2)
top += 1
stack[top] = 2

# push(3)
top += 1
stack[top] = 3

# pop(3)
top -= 1
temp = stack[top+1]
print(temp) # 3

# pop(2)
top -= 1
temp = stack[top+1]
print(temp) # 2

#pop(1)
top -= 1
temp = stack[top+1]
print(temp) # 1
```

## 스택 구현 고려 사항

<img width="904" alt="a_100" src="https://user-images.githubusercontent.com/86648892/185070281-85490fe9-5e4a-4647-8271-867d8a989480.png">

- 알고리즘 문제풀이에서는 1차원 배열을 사용하고 스택의 크기를 예측해서 지정하면 된다
    - 오류가 난다면
        - 크기 예측이 실패했거나
        - 코드상 로직에 오류가 있을 것

## 스택의 응용1: 괄호검사

<img width="903" alt="a_101" src="https://user-images.githubusercontent.com/86648892/185070288-8abae206-4f1a-4e17-b1a8-024937aa2ea2.png">

<img width="885" alt="a_102" src="https://user-images.githubusercontent.com/86648892/185070290-fee7ef62-cf18-4654-9313-67b41b232766.png">

- 문자열에 있는 괄호를 차례대로 조사하면서 왼쪽 괄호를 만나면 스택에 삽입, 오른쪽 괄호를 만나면 스택에서 top 괄호를 삭제한 후 오른쪽 괄호와 짝이 맞는지를 검사
- 이 때, 스택이 비어 있으면 조건 1 또는 조건 2에 위배되고 괄호의 짝이 맞지 않으면 조건 3에 위배
- 마지막 괄호까지를 조사한 후에도 스택에 괄호가 남아있으면 조건 1에 위배

```python
T = int(input())
for test_case in range(1, T + 1):
    st = input()
    stk = []
    ans = 1
    for ch in st:
        if ch == '(':       # '('인경우 스택에 push
            stk.append(ch)
        else:   # 현재는 ')'인 경우 pop
            if stk:         # pop할때는 반드시 스택 empty확인
                stk.pop()
            else:
                ans = 0 # 수식오류 [1] : '(' 짝이 없는데 ')'이 닫힌 경우
                break
    if stk:
        ans = 0 # 수식오류 [2] : 모든 기호 처리 종료후 스택에 push한 데이터가 남은 경우

    print(f'#{test_case} {ans}')
```

## 스택의 응용2: Function Call

- 프로그램에서의 함수 호출과 복귀에 따른 수행 순서를 관리
    - 가장 마지막에 호출된 함수가 가장 먼저 실행을 완료하고 복귀하는 LIFO 구조이므로, ***후입선출 구조의 스택을 이용하여 수행순서 관리***
        - 함수를 호출한다는 것은 사실 만들어놓은 함수에 찾아간다는 것
    - ***함수 호출이 발생***하면 호출한 함수 수행에 필요한 ***지역변수, 매개변수 및 수행 후 복귀할 주소 등의 정보를 스택 프레임(stack frame)에 저장***하여 ***시스템 스택에 삽입***
    - ***함수의 실행이 끝나면*** 시스템 스택의 ***top 원소(스택 프레임)를 삭제(pop)***하면서 프레임에 저장되어 있던 ***복귀주소를 확인하고 복귀***
    - 함수 호출과 복귀에 따라 이 과정을 반복하여 ***전체 프로그램 수행이 종료***되면 시스템 스택은 ***공백 스택***이 된다

<img width="948" alt="a_103" src="https://user-images.githubusercontent.com/86648892/185070291-20c5c1bb-55be-4eb5-8f0d-26643d809096.png">

---

## 재귀호출

<img width="946" alt="a_104" src="https://user-images.githubusercontent.com/86648892/185070294-6cf0a664-a5ea-4a0e-aa38-0dc5ae0b9c63.png">

- 동일한 동작, 서로 다른 메모리 영역
- 끝에서부터 반환되서 나온다!
- 매번 똑같은 동작을 하는 함수를 호출하다보니 이를 하나의 함수로 정의하고
- 불러올 때마다(엄밀히 따지면 이동) 서로 다른 메모리 영역을 사용할 뿐
    - 영역이 몇 개가 생기고(호출된 수만큼) 각각에 변수에 어떤 값이 저장되는지 고려
- 루프처럼 생각하지 말자

### 팩토리얼

<img width="921" alt="a_105" src="https://user-images.githubusercontent.com/86648892/185070296-1a2c4c09-4cce-4ea4-99bb-7b894389a4f5.png">

<img width="708" alt="a_106" src="https://user-images.githubusercontent.com/86648892/185070300-89108e1c-06ee-4618-a946-5b34571ac37f.png">

```python
def f(n):           # 팩토리얼 n!
    if n == 1:      # 1! = 1
        return 1
    else:
        return n * f(n-1)

for i in range(1, 21):  # 0!을 포함하지 않도록 주의
    print(i, f(i))

'''
1 1
2 2
3 6
4 24
5 120
6 720
7 5040
8 40320
9 362880
10 3628800
11 39916800
12 479001600
13 6227020800
14 87178291200
15 1307674368000
16 20922789888000
17 355687428096000
18 6402373705728000
19 121645100408832000
20 2432902008176640000
'''
```

### 피보나치

<img width="939" alt="a_107" src="https://user-images.githubusercontent.com/86648892/185070303-5cf8475d-68f4-4953-9eba-36b07aafdf37.png">

```python
def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

for i in range(21):
    print(i, fibo(i))

'''
0 0
1 1
2 1
3 2
4 3
5 5
6 8
7 13
8 21
9 34
10 55
11 89
12 144
13 233
14 377
15 610
16 987
17 1597
18 2584
19 4181
20 6765
'''
```

### 스택과 재귀

- `f(i, N)`
    - i는 현재 단계
    - N은 목표치

<img width="655" alt="a_108" src="https://user-images.githubusercontent.com/86648892/185070306-8c804eaa-e617-4225-8e99-47d7e7a3eca2.png">

<img width="378" alt="a_109" src="https://user-images.githubusercontent.com/86648892/185070308-e4b97475-9f62-4ea6-bb4a-f6cf4ffa4a4c.png">

```python
def f(i, N):    # i 현재 단계, N 목표 단계
    if i == N:
        print(i)
        return
    else:
        print(i)
        f(i+1, N)

f(0, 3)

'''
0
1
2
3
'''
```

```python
# 1
# 크기가 N인 배열의 모든 원소에 접근하는 재귀함수
def f(i, N):
    if i == N:          # 배열을 벗어남
        return

    else:               # 남은 원소가 있는 경우
        print(A[i])
        f(i+1, N)       # 다음 원소로 이동

N = 3
A = [1, 2, 3]
f(0, N)                 # 0번 원소부터 N개의 원소에 접근

'''
1
2
3
'''

# 2
# 크기가 N인 배열의 모든 원소에 접근하는 재귀함수
def f(i, N):
    if i == N:          # 배열을 벗어남
        return

    else:               # 남은 원소가 있는 경우
        B[i] = A[i]
        f(i+1, N)       # 다음 원소로 이동

N = 3
A = [1, 2, 3]
B = [0] * N
f(0, N)                 # 0번 원소부터 N개의 원소에 접근
print(B)

'''
[1, 2, 3]
'''
```

---

## Memoization

<img width="929" alt="a_110" src="https://user-images.githubusercontent.com/86648892/185070310-c50ddc16-5d59-49bc-8364-56c27ffca068.png">

- 이러한 재귀호출은 엄청난 중복 호출이 존재한다는 문제가 있음
- Memoization으로 해결해보자

### Memoization

- 메모이제이션(memoization)은 컴퓨터 프로그램을 실행할 때 ***이전에 계산한 값을 메모리에 저장***해서 ***매번 다시 계산하지 않도록*** 하여 전체적인 실행속도를 빠르게 하는 기술
- ***동적 계획법의 핵심***이 되는 기술
- ‘memoization’은 글자 그대로 해석하면 ‘메모리에 넣기(to put in memory)’라는 의미이며 ‘기억되어야 할 것'이라는 뜻의 라틴어 memorandum에서 파생되었음
    - memorization과 흔히 혼동하는데 memoize를 동사형으로 갖는 memoization이다

<img width="933" alt="a_111" src="https://user-images.githubusercontent.com/86648892/185070313-f193504a-3548-43ca-bb24-cd76cf7288cc.png">

- `global memo` 는 없어도 됨
- `if n >= 2 and len(memo) <= n:` 은 아직 안 만들어진 경우
- `return memo[n]`
    - 이미 저장되어 있는 값이면 바로 해당 인덱스의 값을 리턴

```python
def fibo(n):
    if memo[n] == -1:   # 계산된 적이 없으면
        memo[n] = fibo(n-1) + fibo(n-2)    # 계산
    return memo[n]

memo = [-1]*101         # -1은 계산된 적이 없음을 나타내는 임의의 숫자
memo[0] = 0
memo[1] = 1

for i in range(21):
    print(i, fibo(i))

'''
0 0
1 1
2 1
3 2
4 3
5 5
6 8
7 13
8 21
9 34
10 55
11 89
12 144
13 233
14 377
15 610
16 987
17 1597
18 2584
19 4181
20 6765
'''

# 중복호출이 없어서 훨씬 빠르다!
```

---

## DP(Dynamic Programming)

- 동적 계획(Dynamic Programming) 알고리즘은 그리디 알고리즘과 같이 ***최적화 문제***를 해결하는 알고리즘
- 동적 계획 알고리즘은 먼저 ***입력 크기가 작은 부분 문제들***을 모두 해결한 후에
    - 그 해들을 이용하여 ***보다 큰 크기의 부분 문제들***을 해결하여
        - 최종적으로 원래 ***주어진 입력의 문제를 해결***하는 알고리즘이다

<img width="957" alt="a_112" src="https://user-images.githubusercontent.com/86648892/185070316-03d0f32b-3b59-458d-be00-4cf2678646a0.png">

<img width="945" alt="a_113" src="https://user-images.githubusercontent.com/86648892/185070319-d9e9e89a-bd84-4532-9081-4a37bbe7c6e6.png">

<img width="927" alt="a_114" src="https://user-images.githubusercontent.com/86648892/185070320-9ef53d64-8c7a-47fb-9c2c-4575602d905e.png">

```python
# N이 주어지고, 피보니치(N)을 구하시오라는 문제라면?

def fibo_dp(n):
    table[0] = 0
    table[1] = 1
    for i in range(2, n+1):
        table[i] = table[i-1] + table[i-2]
    return

# 미리 fibo_dp()를 통해 피보나치 수들을 채워넣음
table = [0]*101
fibo_dp(100)
print(table[20])    # 6765

# table에서 가져와서 출력
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    print(f'#{test_case} {table[N]}')

# 위 fibo_dp()는 다음과 같은 형식으로도 구현이 가능하다

a = 0
b = 1
n = 20
for _ in range(n-1):
    a, b = b, a+b
print(b)            # 6765
```

<img width="951" alt="a_115" src="https://user-images.githubusercontent.com/86648892/185070323-d7ee24b2-c8ff-4fff-8c22-10adb68fd2fe.png">

- 함수 자체가 긴 것은 어차피 함수로 추상화하는 것이기에 괜찮다
- 함수 호출이 많아져 함수 호출이 깊어지는 것이 비효율적이다

---

# DFS(깊이우선탐색)

<img width="934" alt="a_116" src="https://user-images.githubusercontent.com/86648892/185070324-99586642-82c7-465c-9f05-b6f204a75ffb.png">

- 1:1 구조
    - 선형구조
- 1:n 구조
    - 트리
- n:n 구조
    - 그래프
    - 현실세계에 근접한 구조

## DFS란

- 시작 정점(탐색할 목적지)의 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색해 가다가 더 이상 갈 곳이 없게 되면, 가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아와서 다른 방향의 정점으로 탐색을 계속 반복하여 결국 모든 정점을 방문하는 순회방법
- 가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 다시 깊이 우선 탐색을 반복해야 하므로 LIFO 구조의 스택을 사용
    - 스택으로 지나온 경로를 저장
    - 스택 외에 재귀호출로도 저장 가능

## DFS 알고리즘

<img width="963" alt="a_117" src="https://user-images.githubusercontent.com/86648892/185070325-badfeb5b-03a2-4307-9244-d5b01ea82e91.png">

- 인접한 정점은 갈 수 있는 정점을 의미

<img width="954" alt="a_118" src="https://user-images.githubusercontent.com/86648892/185070327-e6b964f1-62a4-4717-9be5-4b33d801c06c.png">

## DFS 예시

<img width="940" alt="a_119" src="https://user-images.githubusercontent.com/86648892/185070331-bfa8d3f1-9c73-4029-a2bb-1b84ca392abf.png">

### Code

- 기본

```python
# 기본적인 DFS를 통한 전체 탐색 구현

# A~G -> 0~6

adjList = [[1, 2],      # 0
            [0, 3, 4],  # 1
            [0, 4],     # 2
            [1, 5],     # 3
            [1, 2, 5],  # 4
            [3, 4, 6],  # 5
            [5]]        # 6

N = 7
visited = [0]*N     # visited 생성
stack = [0]*N       # stack 생성 (이전 탐색 지점)

# v는 시작지점 N은 정점개수
def dfs(v, N):
    top = -1            # stack top 초기화
    print(v)            # 방문해서 할 일
    visited[v] = 1      # A~G 중 시작점 방문 표시
    while True:
        for w in adjList[v]:        # 시작점의 인접 정점 검사
            if visited[w] == 0:     # 아직 탐색하지 않은 곳이라면 탐색
                top += 1            # top 인덱스 추가
                stack[top] = v      # 이전 지점인 v를 스택에 모아놓음
                v = w               # 현재 위치를 w로 변경
                print(v)            # 방문해서 할 일
                visited[w] = 1      # 탐색했으므로 1로 변경
                break
        else:
            if top != -1:           # 스택이 비어있지 않은 경우
                v = stack[top]      # pop
                top -= 1
            else:                   # 스택이 비어있으면
                break               # while 종료

dfs(1, N)

'''
1
0
2
4
5
3
6
'''
```

- 인접원소 리스트 input으로 받기

```python
# 인접원소 리스트를 input으로 받아 DFS를 통한 전체 탐색

'''
0번부터 N번까지, E개의 간선
6 8
0 1
0 2
1 3
1 4
2 4
3 5
4 5
5 6
'''

# input 받기
V, E = map(int, input().split())
N = V+1

# 인접원소 리스트 생성
adjList = [[] for _ in range(N)]
for _ in range(E):
    a, b = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)

visited = [0]*N     # visited 생성
stack = [0]*N       # stack 생성 (이전 탐색 지점)

# v는 시작지점 N은 정점개수
def dfs(v, N):
    top = -1            # stack top 초기화
    print(v)            # 방문해서 할 일
    visited[v] = 1      # A~G 중 시작점 방문 표시
    while True:
        for w in adjList[v]:        # 시작점의 인접 정점 검사
            if visited[w] == 0:     # 아직 탐색하지 않은 곳이라면 탐색
                top += 1            # top 인덱스 추가
                stack[top] = v      # 이전 지점인 v를 스택에 모아놓음
                v = w               # 현재 위치를 w로 변경
                print(v)            # 방문해서 할 일
                visited[w] = 1      # 탐색했으므로 1로 변경
                break
        else:
            if top != -1:           # 스택이 비어있지 않은 경우
                v = stack[top]      # pop
                top -= 1
            else:                   # 스택이 비어있으면
                break               # while 종료

dfs(1, N)

'''
입력

6 8
0 1
0 2
1 3
1 4
2 4
3 5
4 5
5 6

출력

1
0
2
4
5
3
6
'''
```

- 재귀함수를 통한 DFS 구현

<img width="438" alt="a_120" src="https://user-images.githubusercontent.com/86648892/185070332-9d712fae-875a-49c1-ae19-eace856d3597.png">

```python
# 재귀함수를 통한 DFS 구현

'''
0번부터 N번까지, E개의 간선
6 8
0 1
0 2
1 3
1 4
2 4
3 5
4 5
5 6
'''

# input 받기
V, E = map(int, input().split())
N = V+1

# 인접원소 리스트 생성
adjList = [[] for _ in range(N)]
for _ in range(E):
    a, b = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)

visited = [0]*N     # visited 생성
stack = [0]*N       # stack 생성 (이전 탐색 지점)

# v는 시작지점 N은 정점개수
def dfs(v):
    print(v)                    # 방문해서 할 일
    visited[v] = 1
    for w in adjList[v]:
        if visited[w] == 0:     # 방문하지 않은 곳이라면 이동
            dfs(w)

dfs(1)

'''
입력

6 8
0 1
0 2
1 3
1 4
2 4
3 5
4 5
5 6

출력

1
0
2
4
5
3
6
'''
```

### Logic

<img width="957" alt="a_121" src="https://user-images.githubusercontent.com/86648892/185070335-6cee6b0e-a0fb-4b1a-9f10-f717c6e43bf0.png">

<img width="910" alt="a_122" src="https://user-images.githubusercontent.com/86648892/185070338-9565025a-0425-409e-957d-4ca62b3cf824.png">

<img width="927" alt="a_123" src="https://user-images.githubusercontent.com/86648892/185070341-7256a619-5cf4-4369-b142-0206e7f00a32.png">

<img width="919" alt="a_124" src="https://user-images.githubusercontent.com/86648892/185070344-b8e687f4-3e49-469e-a366-08fb9ea76691.png">

<img width="945" alt="a_125" src="https://user-images.githubusercontent.com/86648892/185070345-f037872b-ead6-4d96-9f12-bc3f08e4d9b2.png">

<img width="958" alt="a_126" src="https://user-images.githubusercontent.com/86648892/185070346-ccfe213a-2964-4bd7-838d-1bef96456ea3.png">

<img width="940" alt="a_127" src="https://user-images.githubusercontent.com/86648892/185070348-93f0f9b8-95ee-4d02-b3aa-3a598acf80b8.png">

<img width="951" alt="a_128" src="https://user-images.githubusercontent.com/86648892/185070352-2605189c-5e7f-459b-831f-0a0f896d3411.png">

<img width="935" alt="a_129" src="https://user-images.githubusercontent.com/86648892/185070356-56a4f775-83d6-4f26-b380-338a37e8ce3d.png">

<img width="937" alt="a_130" src="https://user-images.githubusercontent.com/86648892/185070359-157fd20a-327c-4093-836a-fecc5cd44914.png">

<img width="926" alt="a_131" src="https://user-images.githubusercontent.com/86648892/185070362-c581e0ef-d35b-422d-99f6-b5c4f677f981.png">

<img width="938" alt="a_132" src="https://user-images.githubusercontent.com/86648892/185070368-6801fd67-c5d9-4cee-84fb-b3cca98b8fc5.png">

<img width="943" alt="a_133" src="https://user-images.githubusercontent.com/86648892/185070372-408b1b2f-10e8-4bef-9999-8d6a6376dbb5.png">

<img width="928" alt="a_134" src="https://user-images.githubusercontent.com/86648892/185070374-5a66acf0-4f7d-4f10-bcfc-ba1a0f7dd4c1.png">

---