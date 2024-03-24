## Decision Tree

---

![image](https://github.com/zacinthepark/TIL/assets/86648892/04adec5e-41cf-4054-9ac3-9d3bbd647314)

### Decision Tree

![dt_1](https://github.com/zacinthepark/TIL/assets/86648892/40a80860-72a5-41df-a75e-134ce1602b9d)
![dt_2](https://github.com/zacinthepark/TIL/assets/86648892/25294a7d-f17a-4808-b028-61483cb13d6c)

- 특정 변수에 대한 의사결정 규칙을 나무 가지가 뻗는 형태로 분류해 나감
- 분류와 회귀 모두에 사용되는 지도학습 알고리즘
    - 분류: 비용함수는 **불순도** , 마지막 노드에 있는 샘플들의 **최빈값** 을 예측값으로 반환
    - 회귀: 비용함수는 **MSE** , 마지막 노드에 있는 샘플들의 **평균** 을 예측값으로 반환
- 데이터 마이닝에서 일반적으로 사용되는 방법론으로, 몇몇 변수를 바탕으로 목표 변수의 값을 예측하는 모델을 생성하는 것을 목표로 함
- 각 내부 노드들은 하나의 입력 변수에, 자녀 노드들로 이어지는 가지들은 입력 변수의 가능한 값에 대응됨
- 잎 노드는 각 입력 변수들이 루트 노드로부터 잎 노드로 이어지는 경로에 해당되는 값들을 가질 때의 목표 변수 값에 해당됨
- **의미 있는 질문** 을 먼저 하는 것이 중요
- 분석 과정을 실제로 눈으로 확인할 수 있음 (**화이트박스 모델**)
- 훈련 데이터에 대한 제약 사항이 거의 없는 유연한 모델
- **과적합** 으로 모델 성능이 떨어지기 쉬움
- **트리 깊이를 제한** 하는 (가지치기) 튜닝이 필요

### Decision Tree 용어

- Root Node(뿌리 마디): 전체 자료를 갖는 시작하는 마디
- Child Node(자식 마디): 마디 하나로부터 분리된 2개 이상의 마디
- Parent Node(부모 마디): 주어진 마디의 상위 마디
- Terminal Node(끝 마디): 자식 마디가 없는 마디 (= **Leaf Node**)
- Internal Node(중간 마디): 부모 마디와 자식 마디가 모두 있는 마디
- Branch(가지): 연결되어 있는 2개 이상의 마디 집합
- Depth(깊이): 뿌리 마디로부터 끝 마디까지 연결된 마디 개수

### 불순도

![dt_3](https://github.com/zacinthepark/TIL/assets/86648892/51e06004-0a8b-4702-8df2-8dbc9dd695cb)

- 불순도가 낮을수록 분류가 잘된 것임
- 불순도를 수치화할 수 있는 지표
    - 지니 불순도(Gini Impurity)
    - 엔트로피(Entropy)

### 지니 불순도

![dt_4](https://github.com/zacinthepark/TIL/assets/86648892/b62c2e38-d117-465b-abd1-b7877124f47a)
![dt_6](https://github.com/zacinthepark/TIL/assets/86648892/7cadef4f-93d3-4b06-8671-d771f25fdced)

- 지니 불순도: 분류 후에 얼마나 잘 분류했는지 평가하는 지표
    - 얼마나 순도가 증가했는지, 불순도가 감소했는지
    - 계산식에서 `c`는 클래스 개수
- 지니 불순도 특징
    - 지니 불순도가 낮을수록 순도가 높음
    - 지니 불순도는 0 ~ 0.5 사이의 값 (이진 분류의 경우)
        - 순수하게(완벽하게) 분류되면 : `0`
        - 완벽하게 섞이면(50:50) : `0.5`
- 지니 불순도가 낮은 속성으로 의사결정 트리 노드 결정
    - 분류 문제의 경우 불순도를 계산하여 나눴을 때 평균 불순도가 가장 낮아지는 기준을 선정하여 해당 기준으로 분류를 진행함

### 엔트로피(Entropy)

![dt_7](https://github.com/zacinthepark/TIL/assets/86648892/5522b4fe-f019-4dfc-9059-3b6836aefa38)

- $p_i$: 집합 안에서 속성 i의 확률을 나타냄
    - 예를 들어 $p_i = 1$이면 집합 안의 모든 항목이 i 속성을 가진 경우

- 엔트로피는 0 ~ 1 사이의 값
    - 순수하게(완벽하게) 분류되면 : `0`
    - 완벽하게 섞이면(50:50) : `1`

### 정보 이득(Information Gain)

- 엔트로피는 단지 속성의 불순도를 표현
- 우리가 알고 싶은 것 = 어떤 속성이 얼마나 많은 정보를 제공하는가?
- 정보 이득이 크다 = 어떤 속성으로 분할할 때 불순도가 줄어든다
- 모든 속성에 대해 분할한 후 정보 이득 계산
- 정보 이득이 가장 큰 속성부터 분할

![dt_8](https://github.com/zacinthepark/TIL/assets/86648892/3800ab84-35b3-4205-9ff1-ab720173b087)

- `Entropy(T)`: 전체 데이터 세트(트리 T)의 엔트로피. 엔트로피는 불확실성이나 무질서도를 수치화한 것으로, 여기서는 전체 데이터 세트의 불확실성을 의미합니다. 엔트로피가 높다는 것은 데이터 세트 내의 결과(클래스)가 다양하게 섞여 있다는 의미이며, 엔트로피가 낮다는 것은 데이터가 비교적 잘 정렬되어 있다는 것을 의미합니다.
- `Entropy(T, X)`: 특정 속성 X를 기준으로 데이터 세트를 나눈 후의 조건부 엔트로피. 이 값은 X의 각 값에 대해 가중 평균한 엔트로피입니다. 이는 속성 X로 데이터를 나눴을 때의 불확실성을 나타냅니다.
- `Gain(T, X)`는 속성 X를 사용하여 데이터 세트를 분할했을 때 감소하는 불확실성의 양을 측정합니다. 즉, 얼마나 많은 정보를 얻었는지를 나타냅니다.
- `Entropy(T)`는 분할 전 데이터 세트의 불확실성이며, `Entropy(T, X)`는 분할 후의 불확실성입니다.
- 정보 이득이 클수록 해당 속성으로 분할했을 때 데이터 세트의 불확실성이 크게 감소한다는 것을 의미합니다. 이는 그 속성이 좋은 분류 기준이라는 것을 의미하며, 높은 정보 이득을 가진 속성을 결정 트리의 분할 기준으로 선택합니다.
- 정보 이득 공식은 어떤 속성이 데이터를 가장 잘 나누는지, 즉 가장 많은 정보를 제공하는지를 수치화해 보여줍니다. 이를 통해 우리는 데이터를 분류하거나 예측하는 데 있어서 가장 유용한 속성을 선택할 수 있습니다.

### 가지치기

- 가지치기를 하지 않으면 모델이 학습 데이터에는 매우 잘 맞지만, 평가 데이터에는 잘 맞지 않음 (과적합)
- 여러 하이퍼파라미터 값을 조정해 가지치기 할 수 있음
    - `max_depth`, `min_samples_leaf`, `min_samples_split` 등
- 학습 데이터에 대한 성능은 낮아지나, 평가 데이터에 대한 성능을 높일 수 있음
- 가장 적절한 하이퍼파라미터 값을 찾도록 노력해야함

### 주요 하이퍼파라미터

- `max_depth`
    - **트리의 최대 깊이 (기본값: None)**
    - 기본값으로 설정하면 완벽히 분류될 때까지 분할하거나, 노드가 갖는 샘플 개수가 `min_samples_split` 설정값보다 작아질 때까지 계속 분할
    - 계속 분할되면 트리 깊이가 너무 깊어져 과적합이 발생할 수 있으니 적절한 값 설정 필요
- `min_samples_split`
    - **노드를 분할하기 위한 최소한의 샘플 개수 (기본값: 2)**
    - 값을 작게 설정할수록 계속 분할되어 트리 깊이가 깊어져 과적합 발생 가능
    - 적절한 값을 지정해 과적합을 방지할 필요가 있음
- `min_samples_leaf`
    - **리프 노드가 되기 위한 최소한의 샘플 수 (기본값: 1)**
    - min_samples_leaf를 10으로 설정하면 분기했을 때 샘플값이 9, 8 등이 되면 분기할 수 없음
    - min_samples_split과 함께 과적합을 방지할 목적으로 사용
    - 불균형 클래스인 경우 이를 고려하여 작은 값을 설정할 필요가 있음
- `max_feature`
    - 최선의 분할을 위해 고려할 Feature 수 (기본값: None)
    - 기본값으로 설정하면 모든 Feature를 사용해서 분할 수행
    - 정수형으로 선언하면 Feature 수, 실수형으로 선언하면 Feature 비율
    - `sqrt`로 선언하면 전체 Feature 수의 루트 값
    - `auto`로 설정하면 `sqrt`와 같은 의미
    - `log`로 선언하면 `log2` (전체 Feature 수)
- `max_leaf_node`
    - 리프 노드 최대 개수

### Decision Tree 분류 모델

![dt_9](https://github.com/zacinthepark/TIL/assets/86648892/8876eed5-ca1a-45c8-8ee8-3bc4375385ab)

- Decision Tree 분류 모델도 결국 확률에 근거해 예측을 함
- `DecisionTreeClassifier`에서 **random** 한 것은 **1: max_feature를 지정했을 때 뽑는 피쳐들** , **2: 불순도를 동일하게 줄여주는 feature가 있을 때 어떤 feature를 기반으로 가지를 칠지**

### 변수 중요도

- `feature_importances`
- **원하는 Feature들로만 Decision Tree 질문을 설정하고 싶다면 데이터프레임을 해당 Feature들로 따로 생성**
- `feature_importances`는 Decision Tree가 모델을 형성할 때 가장 중요하다고 본 변수
    - **불순도를 가장 많이 줄여준 변수**
- 앙상블은 여러 개의 트리를 기반으로 판단하는 것
    - 하나의 결정 트리보다 예측 성능 높음
    - 하지만 결정 트리가 하나의 트리에서 직관적인 모델의 과정을 보여준다는 장점이 사라짐

### plot_tree로 시각화

- 적절한 figsize 설정 필요
- 불순도가 낮을수록 진한 배경색

```python
from sklearn.tree import plot_tree
fig = plt.figure(figsize=(12, 10))
plot_tree(model,
          filled=True,
          feature_names=x.columns,
          class_names=y.unique(),  # 직접 지정하는 것이 바람직
          fontsize=10)
plt.show()
```

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
path = 'https://raw.githubusercontent.com/jangrae/csv/master/titanic_train.csv'
data = pd.read_csv(path)
```

```python
data['Survived'].value_counts()
```

<pre>
Survived
0    549
1    342
Name: count, dtype: int64
</pre>

```python
data.isnull().sum()
```

<pre>
PassengerId      0
Survived         0
Pclass           0
Name             0
Sex              0
Age            177
SibSp            0
Parch            0
Ticket           0
Fare             0
Cabin          687
Embarked         2
dtype: int64
</pre>

```python
data.corr(numeric_only=True)
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Fare</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>PassengerId</th>
      <td>1.000000</td>
      <td>-0.005007</td>
      <td>-0.035144</td>
      <td>0.036847</td>
      <td>-0.057527</td>
      <td>-0.001652</td>
      <td>0.012658</td>
    </tr>
    <tr>
      <th>Survived</th>
      <td>-0.005007</td>
      <td>1.000000</td>
      <td>-0.338481</td>
      <td>-0.077221</td>
      <td>-0.035322</td>
      <td>0.081629</td>
      <td>0.257307</td>
    </tr>
    <tr>
      <th>Pclass</th>
      <td>-0.035144</td>
      <td>-0.338481</td>
      <td>1.000000</td>
      <td>-0.369226</td>
      <td>0.083081</td>
      <td>0.018443</td>
      <td>-0.549500</td>
    </tr>
    <tr>
      <th>Age</th>
      <td>0.036847</td>
      <td>-0.077221</td>
      <td>-0.369226</td>
      <td>1.000000</td>
      <td>-0.308247</td>
      <td>-0.189119</td>
      <td>0.096067</td>
    </tr>
    <tr>
      <th>SibSp</th>
      <td>-0.057527</td>
      <td>-0.035322</td>
      <td>0.083081</td>
      <td>-0.308247</td>
      <td>1.000000</td>
      <td>0.414838</td>
      <td>0.159651</td>
    </tr>
    <tr>
      <th>Parch</th>
      <td>-0.001652</td>
      <td>0.081629</td>
      <td>0.018443</td>
      <td>-0.189119</td>
      <td>0.414838</td>
      <td>1.000000</td>
      <td>0.216225</td>
    </tr>
    <tr>
      <th>Fare</th>
      <td>0.012658</td>
      <td>0.257307</td>
      <td>-0.549500</td>
      <td>0.096067</td>
      <td>0.159651</td>
      <td>0.216225</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>

```python
# 제거 대상: PassengerId, Name, Ticket, Cabin
drop_cols = ['PassengerId', 'Name', 'Ticket', 'Cabin']

# 변수 제거
data.drop(drop_cols, axis=1, inplace=True)
```

```python
# Age 결측치를 중앙값으로 채우기
age_median = data['Age'].median()
data['Age'].fillna(age_median, inplace=True)
```

```python
# Embarked 최빈값으로 채우기
emb_freq = data['Embarked'].mode()[0]
data['Embarked'].fillna(emb_freq, inplace=True)
```

```python
target = 'Survived'

x = data.drop(target, axis=1)
y = data.loc[:, target]
```

```python
# 가변수화 대상: Pclass, Sex, Embarked
dumm_cols = ['Pclass', 'Sex', 'Embarked']
x = pd.get_dummies(x, columns=dumm_cols, drop_first=True, dtype=int)
```

```python
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)
```

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, classification_report
model = DecisionTreeClassifier(max_depth=5, random_state=1)  # 불순도를 똑같이 줄여주는 변수 중 랜덤하게 골라서 가지를 치기에 random state 하나를 지정
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
```

<pre>
[[137  16]
 [ 46  69]]
              precision    recall  f1-score   support

           0       0.75      0.90      0.82       153
           1       0.81      0.60      0.69       115

    accuracy                           0.77       268
   macro avg       0.78      0.75      0.75       268
weighted avg       0.78      0.77      0.76       268
</pre>

**트리 시각화**

- Graphviz 패키지를 사용
- 사전에 Graphviz 패키지 설치 및 운영체제 환경 설정이 진행

```python
# 시각화 모듈 불러오기
from sklearn.tree import export_graphviz
from IPython.display import Image

# 이미지 파일 만들기
export_graphviz(model,                                 # 모델 이름
                out_file='tree.dot',                   # 파일 이름
                feature_names=x.columns,               # Feature 이름
                class_names=['die', 'survived'],       # Target Class 이름
                rounded=True,                          # 둥근 테두리
                precision=2,                           # 불순도 소숫점 자리수
                # max_depth=3,                           # 표시할 트리 깊이
                filled=True)                           # 박스 내부 채우기

# 파일 변환
!dot tree.dot -Tpng -otree.png -Gdpi=300

# 이미지 파일 표시
Image(filename='tree.png')
```

![z_dt_1](https://github.com/zacinthepark/TIL/assets/86648892/a8a0eabb-3352-45b7-a416-40176bd9c983)

**변수 중요도 시각화**

```python
# 변수 중요도
print(model.feature_importances_)
print(list(x))
```

<pre>
[0.12605791 0.05939124 0.00172331 0.10091982 0.00574436 0.13034353
 0.53213395 0.         0.04368588]
['Age', 'SibSp', 'Parch', 'Fare', 'Pclass_2', 'Pclass_3', 'Sex_male', 'Embarked_Q', 'Embarked_S']
</pre>

```python
# 변수 중요도
# 중요도가 0인 것은 가지치기에 의해 분류에 참여하지 못한 변수
plt.figure(figsize=(5, 5))
plt.barh(list(x), model.feature_importances_)
plt.show()
```

![z_dt_2](https://github.com/zacinthepark/TIL/assets/86648892/0055655f-e6a0-4a7d-a595-2be38dd4ee87)

```python
# 데이터프레임 만들기 1
df = pd.DataFrame()
df['feature'] = list(x)
df['importance'] = model.feature_importances_

# 데이터프레임 만들기 2
perf_dic = {'feature': list(x),
            'importance': model.feature_importances_}
df = pd.DataFrame(perf_dic)

df.sort_values(by='importance', ascending=True, inplace=True)

# 시각화
plt.figure(figsize=(5, 5))
plt.barh(df['feature'], df['importance'])
plt.show()
```

![z_dt_3](https://github.com/zacinthepark/TIL/assets/86648892/303f4161-7009-408b-a0e4-a4e68dc880ca)
