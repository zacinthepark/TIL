## Linear Regression

---

### 선형회귀(Linear Regression)

- 선형 회귀 모델은 선형 함수를 이용해서 회귀(Regression)를 수행하는 모델을 뜻함
- `y = Wx + b`
    - x, y는 가지고 있는 데이터
    - **W** 와 **b** 는 **데이터에 적합한 값으로 학습** 될 수 있는 **파라미터(Parameter)**

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

![image](https://github.com/zacinthepark/TIL/assets/86648892/04f548a6-57d9-4470-87aa-52c4bafb71e8)

- 데이터의 개수가 너무 작을 경우, 트레이닝 데이터와 테스트 데이터가 어떻게 나눠지는가에 따라 학습된 모델과 성능 측정결과가 크게 달라질 수 있습니다.

- 따라서 이러한 문제를 해결하기 위해 **K-Fold Cross Validation (K-Fold 교차 검증)** 을 사용할 수 있습니다.
    - K개의 나누는 개수를 지정하고
    - 테스트를 진행할 때, train과 test를 나누는 것에 대해 k-fold개만큼 바꿔가면서 측정