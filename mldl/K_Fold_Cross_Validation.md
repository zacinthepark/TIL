## Cross Validation, K Fold Validation, Stratified K Fold Validation

---

![image](https://github.com/zacinthepark/TIL/assets/86648892/e6d81ec0-db4d-4047-a67d-254b024d940c)

### 교차 검증(Cross Validation)

알고리즘을 학습시키기 위해선 학습 데이터와 이에 대한 예측 성능을 평가하기 위한 별도의 테스트용 데이터가 필요하다. 하지만 이 방법은 **과적합(Overfitting)** 에 약점을 가진다. 과적합이란, 모델이 학습 데이터에만 과도하게 최적화되어, 실제 예측을 다른 데이터로 수행할 경우에는 예측 성능이 과도하게 떨어지는 것을 말한다. 게다가 고정된 학습 데이터와 테스트 데이터로 평가를 하다 보면 테스트 데이터에만 최적의 성능을 발휘할 수 있도록 편항되게 모델을 유도하게 되고, 결국 해당 테스트 데이터에만 과적합되는 학습 모델이 만들어져 다른 테스트용 데이터가 들어올 경우에는 성능이 저하된다.

이러한 문제점을 개선하는 방법은 교차 검증을 이용해 더 다양한 학습과 평가를 수행하는 것이다. **교차 검증** 이란, **별도의 여러 세트로 구성된 학습 데이터 세트와 검증 데이터 세트에서 학습과 평가를 수행하는 것** 인데, 테스트 데이터 세트에 대해 평가하는 것을 수능이라고 비유한다면, 교차 검증에서 많은 학습과 검증 세트에서 알고리즘 학습과 평가를 수행하는 것을 모의고사에 비유할 수 있다. 이러한 교차 검증 과정에서 각 세트마다 수행한 평가 결과에 따라 하이퍼 파라미터 튜닝 등의 모델 최적화를 더욱 손쉽게 할 수 있다.

대부분의 ML 모델의 성능 평가는 **교차 검증 기반으로 1차 평가를 한 뒤에 최종적으로 테스트 데이터 세트에 적용해 평가하는 프로세스** 이다. ML에 사용되는 데이터 세트를 세분화해서 학습(Train), 검증(Validation), 테스트(Test) 데이터 세트로 나눌 수 있다. 즉, 기존에 학습 데이터를 다시 학습 데이터 + 검증 데이터(학습된 모델의 성능을 1차 평가)로 분할한다.

### K 분할 교차 검증 (K Fold Cross Validation)

> K개의 분할(Fold)에 대한 성능을 예측 -> 평균과 표준편차 계산 -> 일반화 성능

> K가 10인 경우 최종 정확도 = Average(Round1, Round2, ... , Round10)

- 모든 데이터가 **평가에 한 번, 학습에 k-1번 사용**

- 데이터의 개수가 너무 작을 경우, 트레이닝 데이터와 테스트 데이터가 어떻게 나눠지는가에 따라 학습된 모델과 성능 측정결과가 크게 달라질 수 있음

- 데이터를 무작위로 k개의 fold로 나누어, 각각의 fold를 한 번씩 Validation Set, 나머지 fold를 Training Set으로 추출하여 k번 검증

- 단, k는 2 이상 (최소한 한 개씩의 학습용, 검증용 데이터가 필요)

K 분할 교차 검증은 가장 보편적으로 사용되는 교차 검증 기법으로, **K개의 데이터 폴드 세트를 만들어서 K번만큼 각 폴드 세트에 학습과 검증 평가를 반복적으로 수행하는 방법** 이다. 만약 K=5로 설정한다면 5 폴드 교차 검증 과정은 다음과 같다.

1. 데이터 세트를 5등분 한다.
2. 1~4번째 등분을 학습 데이터로, 5번째 등분 하나를 검증 데이터 세트로 설정하고 평가를 수행한다.
3. 1~3번 등분과 5번 등분을 학습 데이터로, 4번 등분을 검증 데이터 세트로 설정하고 평가를 수행한다.
4. 학습 데이터 세트와 검증 데이터 세트를 점진적으로 변경하면서 5번째까지 검증을 수행한다.
5. 5개의 예측 평가를 평균해 K 폴드 평과 결과로 반영한다.

- 장점
  - 모든 데이터를 학습과 평가에 사용할 수 있음
  - 반복 학습과 평가를 통해 정확도 향상
  - 데이터가 부족해서 발생하는 과소적합 문제 방지
  - 평가에 사용되는 데이터 편향을 막을 수 있음
  - 좀 더 일반화된 모델을 만들 수 있음
- 단점
  - 반복 횟수가 많아서 모델 학습과 평가에 많은 시간이 소요됨

```python
import numpy as np
import pandas as pd
```

```python
path = 'https://raw.githubusercontent.com/Jangrae/csv/master/iris.csv'
data = pd.read_csv(path)
```

```python
data.head()
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Sepal.Length</th>
      <th>Sepal.Width</th>
      <th>Petal.Length</th>
      <th>Petal.Width</th>
      <th>Species</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5.1</td>
      <td>3.5</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.9</td>
      <td>3.0</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.7</td>
      <td>3.2</td>
      <td>1.3</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.6</td>
      <td>3.1</td>
      <td>1.5</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5.0</td>
      <td>3.6</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
  </tbody>
</table>
</div>

```python
data.info()
```

<pre>
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 150 entries, 0 to 149
Data columns (total 5 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   Sepal.Length  150 non-null    float64
 1   Sepal.Width   150 non-null    float64
 2   Petal.Length  150 non-null    float64
 3   Petal.Width   150 non-null    float64
 4   Species       150 non-null    object 
dtypes: float64(4), object(1)
memory usage: 6.0+ KB
</pre>

```python
# target 확인
target = 'Species'

# 데이터 분리
features = data.drop(target, axis=1)
label = data.loc[:, target]
```

```python
from sklearn.model_selection import KFold
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
```

```python
model = DecisionTreeClassifier(random_state=156)
```

```python
# kfold: 5개의 폴드 세트로 분리하는 KFold 객체, cv_accuracy: 폴드 세트별로 정확도 값 저장 리스트
kfold = KFold(n_splits=5)
cv_accuracy = []
print('Iris Data Size: ', features.shape[0])
```

<pre>
Iris Data Size:  150
</pre>

```python
cnt_iter = 0  # 교차 검증 회수

# kfold.split(): 폴드 조합 별 학습 데이터 인덱스, 검증 데이터 인덱스를 array로 반환
for train_idx, test_idx in kfold.split(data):
    # 폴드 조합 별 학습 데이터, 검증 데이터 추출
    x_train, x_test = features.iloc[train_idx], features.iloc[test_idx]
    y_train, y_test = label.iloc[train_idx], label.iloc[test_idx]
    
    # 학습 및 예측
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    cnt_iter += 1
    
    # 정확도 측정
    accuracy = np.round(accuracy_score(y_test, y_pred), 4)
    train_size = x_train.shape[0]
    test_size = x_test.shape[0]
    print('-' * 50)
    print(f'#{cnt_iter} 검증 데이터 인덱스 : {test_idx}')
    print(f'#{cnt_iter} 교차 검증 정확도 : {accuracy}, 학습 데이터 크기 : {train_size}, 검증 데이터 크기 : {test_size}')
    
    # 해당 교차 검증 정확도 추가
    cv_accuracy.append(accuracy)

# 각 폴드 별 교차 검증 정확도를 합하여 평균 정확도 계산
print('-' * 50)
print(f'평균 검증 정확도 : {np.mean(cv_accuracy)}')
```

<pre>
--------------------------------------------------
#1 검증 데이터 인덱스 : [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29]
#1 교차 검증 정확도 : 1.0, 학습 데이터 크기 : 120, 검증 데이터 크기 : 30
--------------------------------------------------
#2 검증 데이터 인덱스 : [30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53
 54 55 56 57 58 59]
#2 교차 검증 정확도 : 0.9667, 학습 데이터 크기 : 120, 검증 데이터 크기 : 30
--------------------------------------------------
#3 검증 데이터 인덱스 : [60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83
 84 85 86 87 88 89]
#3 교차 검증 정확도 : 0.8667, 학습 데이터 크기 : 120, 검증 데이터 크기 : 30
--------------------------------------------------
#4 검증 데이터 인덱스 : [ 90  91  92  93  94  95  96  97  98  99 100 101 102 103 104 105 106 107
 108 109 110 111 112 113 114 115 116 117 118 119]
#4 교차 검증 정확도 : 0.9333, 학습 데이터 크기 : 120, 검증 데이터 크기 : 30
--------------------------------------------------
#5 검증 데이터 인덱스 : [120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137
 138 139 140 141 142 143 144 145 146 147 148 149]
#5 교차 검증 정확도 : 0.7333, 학습 데이터 크기 : 120, 검증 데이터 크기 : 30
--------------------------------------------------
평균 검증 정확도 : 0.9
</pre>

### Stratified K 폴드(Stratified K Fold)

Stratified K 폴드는 **불균형한(imbalanced) 분포도를 가진 레이블(결정 클래스) 데이터 집합을 위한 K 폴드 방식** 이다. 여기서 말하는 불균형한 분포도를 가진 레이블 데이터 집합이란, 특정 레이블 값이 특이하게 많거나 매우 적어서 값의 분포가 한쪽으로 치우치는 것을 말한다.

예를 들어, 대출 사기 데이터를 예측한다고 했을 때, 전체 데이터 중 대출 사기 여부(0: 정상 대출, 1: 사기 대출)에서 1의 값을 가진 데이터의 비율은 매우 적을 것이다. 그러나 이는 매우 중요한 피처값이기에 원본 데이터와 유사한 대출 사기 레이블 값의 분포를 학습/테스트 세트에서도 유지하는게 매우 중요하다.

Stratified K 폴드는 이처럼 K 폴드가 레이블 데이터 집합이 원본 데이터 집합의 레이블 분포를 학습 및 테스트 세트에 제대로 분배하지 못하는 경우의 문제를 해결해준다. Stratified K 폴드는 **원본 데이터의 레이블 분포를 먼저 고려한 뒤 이 분포와 동일하게 학습과 검증 데이터 세트를 분배** 하여 학습 데이터와 검증 데이터 세트가 가지는 레이블 분포도가 유사하도록 검증 데이터를 추출한다.

```python
data['Species'].value_counts()
```

<pre>
Species
setosa        50
versicolor    50
virginica     50
Name: count, dtype: int64
</pre>

```python
kfold = KFold(n_splits=3)
cnt_iter = 0

for train_idx, test_idx in kfold.split(data):
    cnt_iter += 1
    y_train, y_test = label.iloc[train_idx], label.iloc[test_idx]
    print('-' * 50)
    print(f'# 교차 검증 : {cnt_iter}')
    print('학습 레이블 데이터 분포:\n', y_train.value_counts())
    print('검증 레이블 데이터 분포:\n', y_test.value_counts())
```

<pre>
--------------------------------------------------
# 교차 검증 : 1
학습 레이블 데이터 분포:
 Species
versicolor    50
virginica     50
Name: count, dtype: int64
검증 레이블 데이터 분포:
 Species
setosa    50
Name: count, dtype: int64
--------------------------------------------------
# 교차 검증 : 2
학습 레이블 데이터 분포:
 Species
setosa       50
virginica    50
Name: count, dtype: int64
검증 레이블 데이터 분포:
 Species
versicolor    50
Name: count, dtype: int64
--------------------------------------------------
# 교차 검증 : 3
학습 레이블 데이터 분포:
 Species
setosa        50
versicolor    50
Name: count, dtype: int64
검증 레이블 데이터 분포:
 Species
virginica    50
Name: count, dtype: int64
</pre>

K 폴드를 통해 데이터를 분할한 결과 **교차 검증 시마다 3개의 폴드 세트로 만들어지는 학습/검증 레이블이 완전히 다른 값으로 추출** 된다. 예를 들어, 첫번째 교차 검증을 보면 학습 레이블은 versicolor, virginica 밖에 없으므로 setosa의 경우는 전혀 학습하지 못하며, 검증 레이블의 경우 setosa 밖에 없으므로 학습 모델은 절대 setosa를 예측하지 못한다. 따라서 검증 예측 정확도는 0이 될 수 밖에 없다. Stratified K 폴드는 이렇게 KFold로 분할된 레이블 데이터 세트가 전체 레이블 값의 분포도를 반영하지 못하는 문제점을 해결해준다.

```python
from sklearn.model_selection import StratifiedKFold
stratified_kfold = StratifiedKFold(n_splits=3)
cnt_iter = 0

for train_idx, test_idx in stratified_kfold.split(data, data['Species']):
    cnt_iter += 1
    y_train, y_test = label.iloc[train_idx], label.iloc[test_idx]
    print('-' * 50)
    print(f'# 교차 검증 : {cnt_iter}')
    print('학습 레이블 데이터 분포:\n', y_train.value_counts())
    print('검증증 레이블 데이터 분포:\n', y_test.value_counts())
```

<pre>
--------------------------------------------------
# 교차 검증 : 1
학습 레이블 데이터 분포:
 Species
virginica     34
setosa        33
versicolor    33
Name: count, dtype: int64
검증증 레이블 데이터 분포:
 Species
setosa        17
versicolor    17
virginica     16
Name: count, dtype: int64
--------------------------------------------------
# 교차 검증 : 2
학습 레이블 데이터 분포:
 Species
versicolor    34
setosa        33
virginica     33
Name: count, dtype: int64
검증증 레이블 데이터 분포:
 Species
setosa        17
virginica     17
versicolor    16
Name: count, dtype: int64
--------------------------------------------------
# 교차 검증 : 3
학습 레이블 데이터 분포:
 Species
setosa        34
versicolor    33
virginica     33
Name: count, dtype: int64
검증증 레이블 데이터 분포:
 Species
versicolor    17
virginica     17
setosa        16
Name: count, dtype: int64
</pre>

실행 결과를 보면 **학습 및 검증 레이블 데이터 값의 분포도가 동일하게 할당** 된 것을 볼 수 있다. 이를 통해 versicolor, virginica, setosa 의 레이블 값을 모두 학습할 수 있고, 이에 기반해 검증을 수행할 수 있다. Stratified K 폴드를 수행하는 경우 레이블 데이터 분포도에 따라 학습/검증 데이터를 분할하기 때문에 `split()` 메서드에 인자로 **피처 데이터 세트뿐만 아니라 레이블 데이터 세트도 반드시 필요** 하다.

```python
cnt_iter = 0  # 교차 검증 회수
stratified_kfold = StratifiedKFold(n_splits=5)

for train_idx, test_idx in stratified_kfold.split(data, data['Species']):
    # 폴드 조합 별 학습 데이터, 검증 데이터 추출
    x_train, x_test = features.iloc[train_idx], features.iloc[test_idx]
    y_train, y_test = label.iloc[train_idx], label.iloc[test_idx]
    
    # 학습 및 예측
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    cnt_iter += 1
    
    # 정확도 측정
    accuracy = np.round(accuracy_score(y_test, y_pred), 4)
    train_size = x_train.shape[0]
    test_size = x_test.shape[0]
    print('-' * 50)
    print(f'#{cnt_iter} 검증 데이터 인덱스 : {test_idx}')
    print(f'#{cnt_iter} 교차 검증 정확도 : {accuracy}, 학습 데이터 크기 : {train_size}, 검증 데이터 크기 : {test_size}')
    
    # 해당 교차 검증 정확도 추가
    cv_accuracy.append(accuracy)

# 각 폴드 별 교차 검증 정확도를 합하여 평균 정확도 계산
print('-' * 50)
print(f'평균 검증 정확도 : {np.mean(cv_accuracy)}')
```

<pre>
--------------------------------------------------
#1 검증 데이터 인덱스 : [  0   1   2   3   4   5   6   7   8   9  50  51  52  53  54  55  56  57
  58  59 100 101 102 103 104 105 106 107 108 109]
#1 교차 검증 정확도 : 0.9667, 학습 데이터 크기 : 120, 검증 데이터 크기 : 30
--------------------------------------------------
#2 검증 데이터 인덱스 : [ 10  11  12  13  14  15  16  17  18  19  60  61  62  63  64  65  66  67
  68  69 110 111 112 113 114 115 116 117 118 119]
#2 교차 검증 정확도 : 0.9667, 학습 데이터 크기 : 120, 검증 데이터 크기 : 30
--------------------------------------------------
#3 검증 데이터 인덱스 : [ 20  21  22  23  24  25  26  27  28  29  70  71  72  73  74  75  76  77
  78  79 120 121 122 123 124 125 126 127 128 129]
#3 교차 검증 정확도 : 0.9, 학습 데이터 크기 : 120, 검증 데이터 크기 : 30
--------------------------------------------------
#4 검증 데이터 인덱스 : [ 30  31  32  33  34  35  36  37  38  39  80  81  82  83  84  85  86  87
  88  89 130 131 132 133 134 135 136 137 138 139]
#4 교차 검증 정확도 : 0.9667, 학습 데이터 크기 : 120, 검증 데이터 크기 : 30
--------------------------------------------------
#5 검증 데이터 인덱스 : [ 40  41  42  43  44  45  46  47  48  49  90  91  92  93  94  95  96  97
  98  99 140 141 142 143 144 145 146 147 148 149]
#5 교차 검증 정확도 : 1.0, 학습 데이터 크기 : 120, 검증 데이터 크기 : 30
--------------------------------------------------
평균 검증 정확도 : 0.9384692307692307
</pre>

정확도가 상승했음을 확인할 수 있다. Stratified K 폴드의 경우 원본 데이터의 레이블 분포도 특성을 반영한 학습 및 검증 데이터 세트를 만들 수 있으므로 **왜곡된 레이블 데이터 세트에서는 반드시 Stratified K 폴드를 이용해 교차 검증해야한다.** 일반적으로 분류(Classification)에서의 교차 검증에는 K 폴드가 아니라 Stratified K 폴드로 분할되어야한다. 그러나 회귀(Regression)에서는 Stratified K 폴드가 지원되지 않는데, **회귀의 결정값은 이산값 형태의 레이블이 아니라 연속된 숫자값이기에 결정값별로 분포를 정하는 의미가 없기 때문이다.**

### Code

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings(action='ignore')
%config InlineBackend.figure_format='retina'
```

```python
path = 'https://raw.githubusercontent.com/Jangrae/csv/master/diabetes.csv'
data = pd.read_csv(path)
```

**데이터설명**

- Pregnancies: 임신 횟수
- Glucose: 포도당 부하 검사 수치
- BloodPressure: 혈압(mm Hg)
- SkinThickness: 팔 삼두근 뒤쪽의 피하지방 측정값(mm)
- Insulin: 혈청 인슐린(mu U/ml)
- BMI: 체질량지수(체중(kg)/키(m))^2
- DiabetesPedigreeFunction: 당뇨 내력 가중치 값
- Age: 나이
- Outcome: 클래스 결정 값(0 또는 1)

```python
target = 'Outcome'

x = data.drop(target, axis=1)
y = data.loc[:, target]
```

```python
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)
```

```python
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
scaler.fit(x_train)
x_train_s = scaler.transform(x_train)
x_test_s = scaler.transform(x_test)
```

**K분할 교차 검증 방법으로 모델 성능을 예측**

- `cross_val_score(model, x_train, y_train, cv=n)` 형태로 사용
- `cv` 옵션에 `k값(분할 개수, 기본값=5)`을 지정
- `cross_val_score` 함수는 넘파이 배열 형태의 값을 반환
- `cross_val_score` 함수 반환 값의 평균을 해당 모델의 예측 성능으로 볼 수 있음

**Decision Tree**

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score

model = DecisionTreeClassifier(max_depth=5,  random_state=1)
# cv_score = cross_val_score(model, x_train, y_train, cv=10, scoring='accuracy')
cv_score = cross_val_score(model, x_train, y_train, cv=10)

print(cv_score)
print('평균:', cv_score.mean())
print('표준편차:', cv_score.std())

result = {}
result['Decision Tree'] = cv_score.mean()
```

<pre>
[0.66666667 0.75925926 0.74074074 0.64814815 0.7037037  0.74074074
 0.75925926 0.81132075 0.79245283 0.67924528]
평균: 0.7301537386443047
표준편차: 0.05141448587329709
</pre>

**KNN**

```python
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score

model = KNeighborsClassifier()

cv_score = cross_val_score(model, x_train_s, y_train, cv=10)

print(cv_score)
print('평균:', cv_score.mean())

result['KNN'] = cv_score.mean()
```

<pre>
[0.64814815 0.68518519 0.72222222 0.64814815 0.72222222 0.74074074
 0.68518519 0.66037736 0.77358491 0.60377358]
평균: 0.6889587700908455
</pre>

**Logistic Regression**

- LogisticRegression 사용시 발생하는 Warning을 없애려면 충분한 max_iter를 지정

```python
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

model = LogisticRegression()

cv_score = cross_val_score(model, x_train, y_train, cv=10)

print(cv_score)
print(cv_score.mean())

result['Logistic Regression'] = cv_score.mean()
```

<pre>
[0.7037037  0.72222222 0.85185185 0.74074074 0.83333333 0.81481481
 0.74074074 0.75471698 0.77358491 0.75471698]
0.7690426275331936
</pre>

```python
# 성능 시각화 비교
plt.figure(figsize = (5, 3))
plt.barh(y=list(result), width=result.values())
plt.xlabel('Score')
plt.ylabel('Model')
plt.show()
```

![z_cv_score](https://github.com/zacinthepark/TIL/assets/86648892/ff2bcc50-723b-4483-8eae-a7461380cf4c)

```python
# 성능 평가
from sklearn.metrics import classification_report

model = LogisticRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
print(classification_report(y_test, y_pred))
```

<pre>
              precision    recall  f1-score   support

           0       0.79      0.90      0.84       146
           1       0.78      0.58      0.66        85

    accuracy                           0.78       231
   macro avg       0.78      0.74      0.75       231
weighted avg       0.78      0.78      0.78       231
</pre>
