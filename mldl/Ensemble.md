## Ensemble

---

- Voting(보팅)
- Bagging(배깅)
- 부스팅(Boosting)
- 스태킹(Stacking)

### 1. 보팅(Voting)

![voting_1](https://github.com/zacinthepark/TIL/assets/86648892/5d14dd9a-7671-4cf5-b58a-0fd0ca8b848f)

![voting_2](https://github.com/zacinthepark/TIL/assets/86648892/cd93f68a-ceee-40a2-b497-5ab06ea8e7f1)

### 2. 배깅(Bagging)

![bagging](https://github.com/zacinthepark/TIL/assets/86648892/7e7934ee-52bf-41bc-ba19-96f47e8e8d24)

- Bootstrap Aggregating의 약자
- 데이터로부터 **부트스트랩** 한 데이터로 모델들을 학습시킨 후, 모델들의 예측 결과를 집계해 최종 결과를 얻는 방법
    - 부트스트랩은 **복원 추출** 하는 것을 의미
- **같은 유형의 알고리즘 기반 모델** 들을 사용
- 데이터 분할 시 중복을 허용 (복원 랜덤 샘플링 방식이라고 함)
- **범주형** 데이터(Categorical Data)는 **투표** 방식(Voting)으로 결vf과를 집계
- **연속형** 데이터(Continuous Data)는 **평균** 으로 결과를 집계
- 대표적인 배깅 알고리즘으로 **Random Forest** 가 있음

### 배깅(Bagging): 랜덤 포레스트(Random Forest)

![random_forest_1](https://github.com/zacinthepark/TIL/assets/86648892/e40710eb-8867-4bd3-a0b9-74bb3a345500)
![random_forest_2](https://github.com/zacinthepark/TIL/assets/86648892/a09e2a15-523b-4af1-8bc7-3ad4ad10ab23)

- Decision Tree 알고리즘을 기반으로 한 대표적인 배깅 알고리즘
- 여러 Decision Tree 모델이 전체 데이터에서 배깅 방식으로 각자의 데이터 샘플링
- 모델들이 개별적으로 학습을 수행한 뒤 모든 결과를 집계하여 최종 결과 결정
- **Random** 의 의미
    - 1) 랜덤하게 데이터를 샘플링
    - 2) 개별 모델이 트리를 구성할 때 분할 기준이 되는 Feature를 랜덤하게 선정
        - 무작위로 뽑은 n개의 Feature들 중에서 가장 정보이득이 큰 Feature를 기준으로 트리를 분할할 것이기에 개별 모델마다 다른 구조의 트리를 구성할 것임
- 각 결정 트리들이 모여 숲을 이룸

### Random Forest 주요 하이퍼파라미터

- `n_estimators`
    - 만들어질 Decision Tree 개수 지정 (기본값: 100)
    - 많이 지정할수록 성능이 좋아질 것으로 기대할 수 있지만 무조건 그런 것은 아님
    - 너무 늘리면 학습 속도가 너무 느려질 수 있음을 고려
- `max_depth`
    - 트리의 최대 깊이 (기본값: None)
    - 기본값으로 설정하면 완벽히 분류될 때까지 분할하거나, 노드가 갖는 샘플 개수가 `min_samples_split` 설정값보다 작아질 때까지 계속 분할
- `min_samples_split`
    - 노드를 분할하기 위한 최소한의 샘플 개수 (기본값: 2)
    - 값을 작게 설정할수록 계속 분할되어 트리 깊이가 깊어져 과적합 발생 가능
- `min_samples_leaf`
    - 리프 노드가 되기 위한 최소한의 샘플 수 (기본값: 1)
    - min_samples_split과 함께 과적합을 방지할 목적으로 사용
- `max_featrue`
    - 최선의 분할을 위해 고려할 Feature 수 (기본값: None)
    - 기본값으로 설정하면 모든 Feature를 사용해서 분할 수행
    - 정수형으로 선언하면 Feature 수, 실수형으로 선언하면 Feature 비율
    - `sqrt`로 선언하면 전체 Feature 수의 루트 값
    - `auto`로 설정하면 `sqrt`와 같은 의미
    - `log`로 선언하면 `log2` (전체 Feature 수)

### 3. 부스팅(Boosting)

- 같은 유형의 알고리즘 기반 모델 여러 개에 대해 순차적으로 학습을 수행
- 이전 모델이 제대로 **예측하지 못한 데이터에 대해서 가중치를 부여** 하여 다음 모델이 학습과 예측을 진행하는 방법
- 계속하여 모델에게 가중치를 부스팅하며 학습을 진행해 부스팅 방식이라 함
- 예측 성능이 뛰어나 앙상블 학습을 주도함
- 배깅에 비해 성능이 좋지만, **속도가 느리고 과적합 발생 가능성** 이 있음
- 대표적인 부스팅 알고리즘으로 **XGBoost** , **LightGBM** 이 있음

#### Gradient Boost

![gradient_boost_1](https://github.com/zacinthepark/TIL/assets/86648892/9b9a8518-1272-4ad0-b6a4-54512cd37ef7)
![gradient_boost_2](https://github.com/zacinthepark/TIL/assets/86648892/a28891a3-52a8-4298-bbaa-be529a5e2b48)

- 회귀 모델: 앞에서 찾지 못한 오차에 대해서, 다시 해당 오차에 대해 예측
    - 오차가 발생했다면, 그 오차값을 내가 예상해서 채워주겠다는 로직
    - `max_depth`만큼 지속적으로 오차를 채워주기
- 분류 모델: 앞에서 찾지 못한 것에 대해 가중치를 주는 방식

#### XGBoost(eXtreme Gradient Boosting)

- 부스팅을 구현한 대표적인 알고리즘 중 하나가 GBM(Gradient Boost Machine)
- GBM 알고리즘을 병렬 학습이 가능하도록 구현한 것이 XGBoost
- 회귀, 분류 문제를 모두 지원하며, 성능과 자원 효율이 좋아 많이 사용됨

XGBoost의 장점

- 높은 예측 성능
    - 분류와 회귀 모두에서 뛰어난 성능을 보임
- 빠른 수행 시간(GBM 대비)
    - 병렬 수행 및 다양한 기능으로 GBM에 비해 빠르게 수행됨
    - 하지만 여전히 다른 알고리즘에 비해서는 느림
- 규제(Regularization)
    - GBM에는 없었던 과적합 규제 기능을 가지고 있음
- 가지치기(Tree Pruning)
    - max_depth 등의 하이퍼파라미터로 가지치기를 할 수 있음
    - Tree Pruning 기능으로 성능에 이점이 없는 분할은 가지치기 할 수 있음
- 내장된 교차 검증(Cross Validation)
    - 반복 수행 시마다 내부적으로 학습 데이터와 검증 데이터에 대한 교차 검증을 수행
    - 지정된 반복 횟수가 아닌 교차 검증을 통해 성능을 확인하여 필요 시 조기 중단 가능

![image](https://github.com/zacinthepark/TIL/assets/86648892/402bcb2d-564f-43da-a4ea-ea68d21de408)

- **결측치 자체 처리**
    - 알아서 결측치를 고려해서 학습을 함 (결측치 여부를 노드 분기를 위한 질문에 포함시킴)
        - 설문조사 미응답 데이터의 경우 해당 결측치는 의미있는 데이터가 될 수 있음
    - 하지만 명시적으로 결측치에 대한 처리를 진행하기를 권고

#### 주요 하이퍼파라미터

- `learning_rate`
    - 0 ~ 1 사이의 값을 지정하여 부스팅 스텝을 반복적으로 수행될 때 업데이트되는 학습률 값
    - 일반적으로 0.01 ~ 0.2 사이의 값을 지정 (기본값: 0.1)
- `n_estimators`
    - weak learner 개수로, 개수가 많을수록 일정 수준까지는 성능이 좋아질 수 있음
    - 너무 많이 지정하면 학습에 많은 시간이 소요됨 (기본값: 100)
- `min_child_weight`
    - 트리에서 추가적으로 분할할 지를 결정하기 위해 필요한 데이터들의 weight 총합
    - 이 값이 클수록 분할을 자제함 (기본값: 1)
- `gamma`
    - 트리에서 추가적으로 분할할 지를 결정하기 위해 필요한 최소 손실 감소 값
    - 이 값보다 큰 손실이 감소된 경우에 분할함, 값이 클수록 과적합 위험 감소 (기본값: 0)
- `max_depth`
    - 트리 기반 알고리즘의 max_depth와 같은 의미
    - 0을 지정하면 깊이 제한 없어짐 (기본값: 6)
- `sub_sample`
    - weak learner가 학습에 사용하는 데이터 샘플링 비율
    - 과적합이 염려되는 경우 1보다 작은 값으로 설정 (기본값: 1, 전체 데이터를 기반으로 학습)
- `colsample_bytree`
    - 트리 생성에 필요한 Feature 샘플링 비율
    - Feature가 많은 경우 과적합을 조절하기 위해서 사용 (기본값: 1, 모든 Feature 사용)
- `reg_lambda`
    - L2 규제 적용값
    - Feature가 많은 경우 이 값을 키워 과적합 위험을 줄일 수 있음 (기본값: 1)
- `reg_alpha`
    - L1 규제 적용값
    - Feature가 많은 경우 이 값을 키워 과적합 위험을 줄일 수 있음 (기본값: 0)

### 4. 스태킹(Stacking)

![stacking](https://github.com/zacinthepark/TIL/assets/86648892/d7144c86-d58b-4440-a293-341d9711aed1)

- 여러 모델의 예측값을 최종 모델의 학습 데이터로 사용하여 예측하는 방법
- 예를 들어
    - KNN, Logistic Regression, XGBoost 모델을 사용하여 각 예측값을 구한 후
    - 이 예측값을 최종 모델인 RandomForest 학습 데이터로 사용
- 현실 모델에서 많이 사용되지 않으며, Kaggle과 같이 미세한 성능 차이로 승부를 결정하는 대회에서 사용됨
- 기본 모델로 4개 이상 선택해야 좋은 결과를 기대할 수 있음

### Code

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings(action='ignore')
%config InlineBackend.figure_format = 'retina'
```

```python
path = 'https://raw.githubusercontent.com/jangrae/csv/master/admission_simple.csv'
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
      <th>GRE</th>
      <th>TOEFL</th>
      <th>RANK</th>
      <th>SOP</th>
      <th>LOR</th>
      <th>GPA</th>
      <th>RESEARCH</th>
      <th>ADMIT</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>337</td>
      <td>118</td>
      <td>4</td>
      <td>4.5</td>
      <td>4.5</td>
      <td>9.65</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>324</td>
      <td>107</td>
      <td>4</td>
      <td>4.0</td>
      <td>4.5</td>
      <td>8.87</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>316</td>
      <td>104</td>
      <td>3</td>
      <td>3.0</td>
      <td>3.5</td>
      <td>8.00</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>322</td>
      <td>110</td>
      <td>3</td>
      <td>3.5</td>
      <td>2.5</td>
      <td>8.67</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>314</td>
      <td>103</td>
      <td>2</td>
      <td>2.0</td>
      <td>3.0</td>
      <td>8.21</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>

```python
target = 'ADMIT'

x = data.drop(target, axis=1)
y = data[target]
```

```python
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)
```

```python
from sklearn.preprocessing import MinMaxScaler

# 정규화
scaler = MinMaxScaler()
scaler.fit(x_train)
x_train_s = scaler.transform(x_train)
x_test_s = scaler.transform(x_test)
```

```python
# xgboost 설치
# !pip install xgboost
```


```python
# lightgbm 설치
# !pip install lightgbm
```

```python
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier

from sklearn.metrics import *
```

**KNN**

```python
model = KNeighborsClassifier(n_neighbors=5)
model.fit(x_train_s, y_train)
y_pred = model.predict(x_test_s)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
```

<pre>
[[79  5]
 [15 51]]
              precision    recall  f1-score   support

           0       0.84      0.94      0.89        84
           1       0.91      0.77      0.84        66

    accuracy                           0.87       150
   macro avg       0.88      0.86      0.86       150
weighted avg       0.87      0.87      0.86       150
</pre>

**Decision Tree**

```python
model = DecisionTreeClassifier(max_depth=5, random_state=1)
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
```

<pre>
[[77  7]
 [13 53]]
              precision    recall  f1-score   support

           0       0.86      0.92      0.89        84
           1       0.88      0.80      0.84        66

    accuracy                           0.87       150
   macro avg       0.87      0.86      0.86       150
weighted avg       0.87      0.87      0.87       150
</pre>

**Logistic Regression**

```python
model = LogisticRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
```

<pre>
[[75  9]
 [14 52]]
              precision    recall  f1-score   support

           0       0.84      0.89      0.87        84
           1       0.85      0.79      0.82        66

    accuracy                           0.85       150
   macro avg       0.85      0.84      0.84       150
weighted avg       0.85      0.85      0.85       150
</pre>

**Random Forest**

```python
model = RandomForestClassifier(max_depth=5, random_state=1)
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
```

<pre>
[[78  6]
 [13 53]]
              precision    recall  f1-score   support

           0       0.86      0.93      0.89        84
           1       0.90      0.80      0.85        66

    accuracy                           0.87       150
   macro avg       0.88      0.87      0.87       150
weighted avg       0.88      0.87      0.87       150
</pre>

```python
# Feature 중요도 확인
plt.barh(y=list(x), width=model.feature_importances_)
plt.show()
```

![z_ensemble_1](https://github.com/zacinthepark/TIL/assets/86648892/64a8c4b0-6bce-43e8-91ed-cba2c9b9f6ef)

**XGBoost**

```python
model = XGBClassifier(max_depth=5, random_state=1)
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
```

<pre>
[[77  7]
 [15 51]]
              precision    recall  f1-score   support

           0       0.84      0.92      0.88        84
           1       0.88      0.77      0.82        66

    accuracy                           0.85       150
   macro avg       0.86      0.84      0.85       150
weighted avg       0.86      0.85      0.85       150
</pre>

```python
# Feature 중요도 확인
plt.barh(y=list(x), width=model.feature_importances_)
plt.show()
```

![z_ensemble_2](https://github.com/zacinthepark/TIL/assets/86648892/9e3b904f-2f07-4f06-9f68-026d5c19dbe1)

**LightGBM**

```python
# 선언하기
# verbose: 학습과정을 보여주는지 여부 (1이 default)
# LGBM에서 `feature_importances_`는 해당 변수들이 전체 트리 안에서 몇 번 분기에 사용되었는가, 즉 split count의 토탈값을 보여줌
# model = LGBMClassifier(max_depth=5, importance_type='split', random_state=1, verbose=-1)

# 보통 feature_importances를 산정하는데 사용되는 정보이득을 바탕으로 설정
# 하지만 LGBM에서는 0~1 사이 퍼센트 값으로 주지 않음
model = LGBMClassifier(max_depth=5, importance_type='gain', random_state=1, verbose=-1)
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
```

<pre>
[[77  7]
 [14 52]]
              precision    recall  f1-score   support

           0       0.85      0.92      0.88        84
           1       0.88      0.79      0.83        66

    accuracy                           0.86       150
   macro avg       0.86      0.85      0.86       150
weighted avg       0.86      0.86      0.86       150
</pre>

```python
# Feature 중요도 확인 (정규화)
fi_norm = model.feature_importances_ / np.sum(model.feature_importances_)
plt.barh(y=list(x), width=fi_norm)
plt.show()
```

![z_ensemble_3](https://github.com/zacinthepark/TIL/assets/86648892/f88062a4-e747-4a62-9cce-236e0f6ae0b2)
