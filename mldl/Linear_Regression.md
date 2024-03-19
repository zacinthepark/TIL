## Linear Regression

---

### 변수 선택

1. r2 score 확인: 데이터프레임에서 for문을 돌려 x 변수들을 하나씩 빼봐서 전체 x일 때의 r2 score와 비교하여 현격히 떨어지면 중요한 변수라고 판단
2. 다중공선성 확인: y를 제외하고 x끼리의 데이터프레임에서 하나의 x를 종속변수로 삼고 나머지 x 변수들로 예측했을 때 r2 score가 높다면 다중공선성이 높다고 판단

### 선형회귀(Linear Regression)

- 선형 회귀 모델은 선형 함수를 이용해서 회귀(Regression)를 수행하는 모델을 뜻함
- `y = Wx + b`
    - x, y는 가지고 있는 데이터
    - **W** 와 **b** 는 **데이터에 적합한 값으로 학습** 될 수 있는 **파라미터(Parameter)**

- 최선은 모델과 실제값의 오차가 더 적은 것
- 회귀에서 변수가 많으면 과적합이 발생할 수 있는 가능성이 크다
- 그렇기에 적절한 변수 선택이 중요하다

### 결정 트리(Decision Tree)

![image](https://github.com/zacinthepark/TIL/assets/86648892/16877002-42b2-4c66-ad69-49c3e3e38175)

- **결정 트리(Decision Tree)** 학습법은 데이터 마이닝에서 일반적으로 사용되는 방법론으로, 몇몇 이볅 변수를 바탕으로 목표 변수의 값을 예측하는 모델을 생성하는 것을 목표로 한다.

- 그림은 그러한 예측 모델의 한 예를 나타내고 있다. 그림의 트리 구조에서, 각 내부 노드들은 하나의 입력 변수에, 자녀 노드들로 이어지는 가지들은 입력 변수의 가능한 값에 대응된다.

- 잎 노드는 각 입력 변수들이 루트 노드로부터 잎 노드로 이어지는 경로에 해당되는 값들을 가질 때의 목표 변수 값에 해당된다.

### preprocessing.LabelEncoder

> 머신러닝 알고리즘은 string(=object) 형태의 값은 처리할 수 없기 때문에 숫자형 값으로 변경 필요

```python
le = preprocessing.LableEncoder()

le.fit(['paris', 'paris', 'tokyo', 'amsterdam'])
list(le.classes_)    # ['amsterdam', 'tokyo', 'paris']

le.transform(['tokyo', 'tokyo', 'paris'])   # array([2, 2, 1]...)

list(le.inverse_transform([2, 2, 1]))   # ['tokyo', 'tokyo', 'paris']
```

```python
from sklearn import preprocessing
le = preprocessing.LabelEncoder()
titanic_df['sex'] = le.fit(titanic_df['sex']).transform(titanic_df['sex'])
titanic_df['adult_male'] = le.fit(titanic_df['adult_male']).transform(titanic_df['adult_male'])
titanic_df['alone'] = le.fit(titanic_df['alone']).transform(titanic_df['alone'])
titanic_df['embarked'] = le.fit(titanic_df['embarked']).transform(titanic_df['embarked'])
titanic_df['deck'] = le.fit(titanic_df['deck']).transform(titanic_df['deck'])
titanic_df['who'] = le.fit(titanic_df['who']).transform(titanic_df['who'])
```

### 범주형 시각화 코드

#### 데이터 분포 살펴보기

```python
figure, ax_list_list = plt.subplots(nrows=3, ncols=3);
figure.set_size_inches(10,10)

ax_list = ax_list_list.reshape(9)  # 다차원 행렬의 차원을 원하는 모양으로 변경합니다.
print(ax_list_list.shape)
print(ax_list.shape)

for i in range(len(categorical_cols)):
    col = categorical_cols[i]
    sns.countplot(data=titanic_df, x=col, ax=ax_list[i])
    ax_list[i].set_title(col)

plt.tight_layout()
```

![z240312](https://github.com/zacinthepark/TIL/assets/86648892/e778b518-77b2-4600-9bcf-4895ba8d1f8e)

#### 범주 분류별 생존 여부 그래프

```python
# hue 인자로 'survived' 컬럼을 입력, 각 분류형 데이터 별로 생존/사망 분리하여 살펴보기
figure, ax_list_list = plt.subplots(nrows=3, ncols=3);
figure.set_size_inches(10,10)

ax_list = ax_list_list.reshape(9)
print(ax_list_list.shape)
print(ax_list.shape)

for i in range(len(categorical_cols)):
    col = categorical_cols[i]
    sns.countplot(data=titanic_df, x=col, ax=ax_list[i], hue='survived')
    ax_list[i].set_title(col)

plt.tight_layout()
```

![z2403121](https://github.com/zacinthepark/TIL/assets/86648892/4e2b15ee-7e85-4848-a76c-41618eeed55c)

- 남성보다 여성의 생존률이 더 높습니다 (남성 > 여성 > 아이)
- 탑승지(embarked)가 C인 경우 생존율이 높습니다
- 1등석 > 2등석 > 3등석 순으로 생존율이 높습니다
- B,D,E 덱 위치의 승객들이 생존율이 높습니다
- 나홀로 승객은 생존율이 낮습니다

#### 생존 여부별 나이 히스토그램

```python
sns.histplot(data=titanic_df, x='age', hue='survived', bins=30, alpha=0.3)
```

![z2403122](https://github.com/zacinthepark/TIL/assets/86648892/5c177a7b-3e69-448b-a996-38ac0cd4f244)

#### 성별과 좌석 등급에 따라 나이의 boxplot

```python
sns.boxplot(data=titanic_df, x='sex', y='age', hue='pclass')
```

![z2403123](https://github.com/zacinthepark/TIL/assets/86648892/48db7559-b4e6-423f-860c-0355b2ec7880)

### K-Fold Cross Validation

![image](https://github.com/zacinthepark/TIL/assets/86648892/e6d81ec0-db4d-4047-a67d-254b024d940c)

- 데이터의 개수가 너무 작을 경우, 트레이닝 데이터와 테스트 데이터가 어떻게 나눠지는가에 따라 학습된 모델과 성능 측정결과가 크게 달라질 수 있음

- 따라서 이러한 문제를 해결하기 위해 **K-Fold Cross Validation (K-Fold 교차 검증)** 을 사용할 수 있음

- 데이터를 무작위로 k개의 fold로 나누어, 각각의 fold를 한 번씩 Validation Set, 나머지 fold를 Training Set으로 추출하여 K번 검증

### KNN 알고리즘

- KNN은 fitting 과정은 단순히 학습 데이터를 메모리에 올리는 것에 불과
- predict 과정에서 거리 계산을 통해 연산을 하기에 연산 속도가 느린 편임
- KNN은 K를 데이터의 개수만큼 설정하면 예측값은 Regression의 경우 데이터의 평균값, Classification의 경우 데이터의 최빈값
- scaling이 필요
- MinMaxScaling은 정규화에 해당
- 평가용 데이터에도 학습용 데이터를 기준으로 스케일링을 수행함
- 평가용 데이터는 스케일링값이 0~1 범위라고 보장할 수는 없음
    - 그 차이가 너무 크다면 모델의 예측 성능이 떨어지므로 피팅을 다시 수행해야함
    - 범위에서 벗어나는 값에 대해서도 최근접 K개 이웃을 바탕으로 예측을 수행하기는 함
- 일관된 예측을 위해 학습용 데이터를 통해 정규화를 진행하고 이를 학습 데이터, 평가 데이터 모두에 적용
- scaling 후에는 데이터프레임이 배열로 변환됨

#### [참고] 학습 데이터를 기준으로 정규화

<img src = "https://github.com/Jangrae/img/blob/master/minmax.png?raw=true" width=600 align="left"/>

### Decision Tree

- 지니 불순도 계산식에서 c는 클래스 개수
- 분류 문제의 경우 불순도를 계산하여 나눴을 때 평균 불순도가 가장 낮아지는 기준을 선정하여 해당 기준으로 분류를 진행함
- 가지치기는 가지를 잘라서 더 뻗어나가지 못하게 하는 것
- min_samples_leaf를 10으로 설정하면 분기했을 때 샘플값이 9, 8 등이 되면 분기할 수 없음
- 원하는 feature들로만 decision tree 질문을 설정하고 싶다면 데이터프레임을 해당 feature들로 따로 생성
- feature_importances는 decision tree가 모델을 형성할 때 가장 중요하다고 본 변수
    - 불순도를 가장 많이 줄여준 변수
- DecisionTreeClassifier에서 random한 것은 1: max_feature를 지정했을 때 뽑는 피쳐들, 2: 불순도를 동일하게 줄여주는 피쳐가 있을 때 어떤 피쳐를 기반으로 가지를 칠지
- 앙상블은 여러 개의 트리를 기반으로 판단하는 것
    - 하나의 결정 트리보다 예측 성능 높음
    - 하지만 결정 트리가 하나의 트리에서 직관적인 모델의 과정을 보여준다는 장점이 사라짐

- Entropy(T): 전체 데이터 세트(트리 T)의 엔트로피. 엔트로피는 불확실성이나 무질서도를 수치화한 것으로, 여기서는 전체 데이터 세트의 불확실성을 의미합니다. 엔트로피가 높다는 것은 데이터 세트 내의 결과(클래스)가 다양하게 섞여 있다는 의미이며, 엔트로피가 낮다는 것은 데이터가 비교적 잘 정렬되어 있다는 것을 의미합니다.
- Entropy(T, X): 특정 속성 X를 기준으로 데이터 세트를 나눈 후의 조건부 엔트로피. 이 값은 X의 각 값에 대해 가중 평균한 엔트로피입니다. 이는 속성 X로 데이터를 나눴을 때의 불확실성을 나타냅니다.

- **Gain(T, X)**는 속성 X를 사용하여 데이터 세트를 분할했을 때 감소하는 불확실성의 양을 측정합니다. 즉, 얼마나 많은 정보를 얻었는지를 나타냅니다.
- **Entropy(T)**는 분할 전 데이터 세트의 불확실성이며, **Entropy(T, X)**는 분할 후의 불확실성입니다.
- 정보 이득이 클수록 해당 속성으로 분할했을 때 데이터 세트의 불확실성이 크게 감소한다는 것을 의미합니다. 이는 그 속성이 좋은 분류 기준이라는 것을 의미하며, 높은 정보 이득을 가진 속성을 결정 트리의 분할 기준으로 선택합니다.
- 정보 이득 공식은 어떤 속성이 데이터를 가장 잘 나누는지, 즉 가장 많은 정보를 제공하는지를 수치화해 보여줍니다. 이를 통해 우리는 데이터를 분류하거나 예측하는 데 있어서 가장 유용한 속성을 선택할 수 있습니다.

### Logistic Regression

> 1. x 데이터를 잘 설명하는 최적의 선형 회귀선(선형 판별식)을 찾는다.
> 2. 이를 로지스틱 함수(시그모이드 함수)를 통해 각 값에 대해 1이 될 확률을 구해 변환한다.
> 3. 최종적으로 임계값을 바탕으로 분류한다.

- 확률값을 얻어서 확률값이 0.5보다 크면 1이라 분류하고, 0.5보다 작으면 0이라 분류할 수 있지 않을까?
- 어떻게 구부릴까?
- f(x)는 구한 선형 회귀식 (-inf ~ +inf)
- `[0, 1]`은 경계값 포함 범위, `(0, 1)`은 경계값 포함하지 않는 범위, `(0, 1]`은 0포함 1포함하지 않음
- 확률값을 얻어서, 임계값을 통한 전략 수립이 가능
    - 은행 대출의 경우 대출을 승인할지 말지 여부에서 임계값을 0.7로 올려 그 위는 1, 아래는 0으로 설정하면 더 엄격하게 심사를 하는 것이라 할 수 있음
- 임계값을 낮추면 적극적으로 1을 판단(recall을 올리려는 시도), 임계값을 올리면 소극적으로 1을 판단

### Random Search, Grid Search

- Grid Search 범위를 적게 하여 찾은 값을 기준으로 파라미터 범위를 조정하여 Grid Search를 다시 해보는 것 고려
- Random Search를 통해 찾은 값을 기준으로 파라미터 범위를 조정하여 Grid Search를 해보는 것도 고려

### Hyperparameter 튜닝

> 1. 기본 모델 설정 (model_default)
> 2. 성능을 검증하고자 할 Hyperparameter 값 범위 설정
> 3. 기본 모델을 바탕으로 RandomizedSearchCV, GridSearchCV를 활용하여 다양한 모델 검증
> 3-1. CV가 들어간다는 것은 검증 방식에 k 분할 교차 검증 방식이 사용된다는 것
> 4. model.best_estimator_를 통해 최적 파라미터를 적용한 모델에 접근

- GridSearch는 모든 파라미터 조합에 대한 성능을 확인하여 베스트 파라미터를 찾는 것
- RandomSearch는 n_iter 지정
- 학습 데이터에 대한 성능에서는 GridSearch보다 RandomSearch가 더 좋은 성능을 파라미터를 찾는 경우는 없을 것
- 하지만 해당 파라미터(max_depth, n_neighbors)가 학습 데이터에 대한 성능은 좋을지 몰라도 이것이 곧 평가 데이터에서 성능이 좋을 것이라는 것을 보장하지는 않는다
- 고로 RandomSearch를 통해 얻은 최적의 파라미터가 GridSearch를 통해 얻은 최적의 파라미터보다 평가 데이터에 대해서는 성능이 좋을 수 있다

### 앙상블(Ensemble)

- 부트스트랩은 복원 추출하는 것을 의미한다
- Random Forest는 Decision Tree 알고리즘을 기반으로 한 대표적인 배깅 알고리즘이다
- Random Forest에서 random한 것은 1: 랜덤하게 데이터를 샘플링, 2: 분할 기준이 되는 feature

- Gradient Boost
- 회귀 모델은 앞에서 찾지 못한 오차에 대해서, 다시 해당 오차에 대해 예측
    - 오차가 발생했다면, 그 오차값을 내가 예상해서 채워주겠다는 로직
    - max_depth만큼 지속적으로 오차를 채워주기
- 분류 모델은 앞에서 찾지 못한 것에 대해 가중치를 주는 것

![image](https://github.com/zacinthepark/TIL/assets/86648892/402bcb2d-564f-43da-a4ea-ea68d21de408)

- XGBoost는 결측치를 고려해서 학습을 함
    - 설문조사 미응답의 경우 해당 결측치는 의미있는 데이터가 될 수 있음

- sklearn Imputer: 결측치 처리용 패키지
- 비용함수: 비용함수(손실함수)는 모델의 예측값과 실제값 사이의 차이를 수치화해주는 함수입니다. 해당 함수의 함수 값이 낮을수록 모델의 예측이 실제와 가깝다는 것을 의미
- sklearn에 있는 모델들은 대부분 default 비용함수를 가지고 있으나, 특수한 경우 직접 설정할 수 있음
- 패널티를 부과한다는 것은 모델이 잘못된 추론을 했을경우 더 큰 비용을 부과하는것을 의미
- 소수 클래스를 잘못 추론했을 경우 더 큰 패널티를 주면 모델에 해당 오류에 큰 영향을 받게 하여 중요도를 높일 수 있음
