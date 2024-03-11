## 힙 자료구조와 heapq

---

### 힙 자료구조

![heap_data_structure](https://github.com/zacinthepark/TIL/assets/86648892/f7c811e2-e203-44ba-b224-813eb4b641d1)

- 힙은 특정한 규칙을 가지는 트리로, **최댓값과 최솟값을 찾는 연산** 을 빠르게 하기 위해 고안된 완전이진트리를 기본으로 함

- **힙 property** : A가 B의 부모 노드이면 A의 키값과 B의 키값 사이의 대소 관계가 성립됨
    - 최소 힙 : 부모 노드의 키값이 자식 노드의 키값보다 항상 작은 힙
    - 최대 힙 : 부모 노드의 키값이 자식 노드의 키값보다 항상 큰 힙

- 이러한 속성으로 인해 힙에서는 가장 낮은 (혹은 높은) 우선순위를 가지는 노드가 항상 루트에 오게 되고, 이를 이용해 **우선순위 큐** 와 같은 추상적인 자료형 구현이 가능함

- 키값의 대소 관계는 부모-자식 간에만 성립하고, 형제 노드 사이에서는 대소 관계가 정해지지 않음

### `heapq`

- 파이썬 `heapq` 모듈은 heapq(priority queue) 알고리즘을 제공함

- 모든 부모 노드는 그의 자식 노드보다 값이 작거나 큰 이진트리(binary tree) 구조인데, 내부적으로는 **인덱스 0에서 시작해 k번째 원소가 항상 자식 원소들(2k+1, 2k+2)보다 작거나 같은 최소 힙** 의 형태로 저장됨

### heap 함수

- `heapq.heappush(heap, item)` : item을 heap에 추가

- `heapq.heappop(heap)` : heap에서 가장 작은 원소를 pop & return
    - 비어있는 경우 IndexError

- `heapq.heapify(x)` : 리스트 x를 즉각적으로 heap으로 변환함 (in linear time, `O(N)`)

#### 힙 생성 & 원소 추가

```python
import heapq

heap = []
heapq.heappush(heap, 50)
heapq.heappush(heap, 10)
heapq.heappush(heap, 20)

print(heap)     # [10, 50, 20]
```

```python
heap2 = [50 ,10, 20]
heapq.heapify(heap2)

print(heap2)    # [10, 50, 20]
```

#### 힙에서 원소 삭제

```python
result = heapq.heappop(heap)

print(result)   # 10
print(heap)     # [20, 50]

result2 = heap[0]

print(result2)  # 20
print(heap)     # [20, 50]
```

#### 최대 힙 만들기

> y = -x 변환을 하면 최솟값 정렬이 최댓값 정렬로 바뀐다.

- 힙에 원소를 추가할 때 `(-item, item)`의 튜플 형태로 넣어주면 튜플의 첫 번째 원소를 우선순위로 힙을 구성
- 원소 값의 부호를 바꿨기 때문에, 최소 힙으로 구현된 heapq 모듈을 최대 힙 구현에 활용하게 되는 것

```python
heap_items = [1,3,5,7,9]

max_heap = []
for item in heap_items:
  heapq.heappush(max_heap, (-item, item))

print(max_heap) # [(-9, 9), (-7, 7), (-5, 5), (-3, 3), (-1, 1)]

max_item = heapq.heappop(max_heap)[1]
print(max_item) # 9
```

#### 예제 : 주어진 리스트의 모든 값이 T 이상이 될 때까지 최솟값 두 개를 합치기

> N개의 비커에 액체가 담겨 있다. 모든 비커에 있는 액체의 양이 T 이상이 될 때까지 액체가 가장 적게 담긴 두 비커의 액체를 합쳐가려 한다. 각각의 비커에 담겨있는 액체의 양을 표기한 리스트 L과 기준 T가 주어질 때, 모든 비커의 양이 T 이상이 될 때까지 필요한 작업 횟수를 리턴하는 함수를 구현해보자.

```python
import heapq

def solution(L, T):
  # 비커 리스트 -> 최소 힙으로 변환
  heapq.heapify(L) 

  result = 0

  while len(L) >= 2:    #IndexError 방지
      # 힙에서 최솟값 가져오기
      min_1 = heapq.heappop(L) 
      
      if min_1 >= T:    # 액체의 최솟값이 T보다 크다는 조건 만족 (종료)
        return result   
      else:             # 두번째로 작은 값 가져와서 합친 값을 힙에 삽입
        min_2 = heapq.heappop(L) 
        heapq.heappush(L, min_1 + min_2)
        result += 1
  
  if L[0] > T:
    return result
  else:
    return -1

```
