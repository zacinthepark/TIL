# Algorithm Live

[Algorithm이란](#algorithm)<br>
[Array](#array)<br>
[정렬](#정렬)<br>
[Bubble Sort](#버블-정렬bubble-sort)<br>
[Counting Sort](#카운팅-정렬counting-sort)<br>
[완전 검색(Exhaustive Search)](#완전검색-exhaustive-search)<br>
[탐욕(Greedy) 알고리즘](#탐욕greedy-알고리즘)<br>

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

## 정렬

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