## Hyperparameter, RandomSearch, GridSearch

---

### Hyperparameter

- 알고리즘을 사용하여 모델링할 때 모델 성능을 최적화하기 위해 조절할 수 있는 매개변수
    - KNN 알고리즘의 `n_neighbors`, Decision Tree 알고리즘의 `max_depth` 등
- 튜닝하는 방법에 정답은 없음
- 모델의 성능 향상을 위해 최선의 하이퍼파라미터 값을 찾는 **다양한 시도** 를 해야함
- Grid Search, Random Search를 통해 다양한 시도 수행

#### KNN

![image](https://github.com/zacinthepark/TIL/assets/86648892/9e5e1a4b-469a-4212-b95a-437727f5a357)

1. k값(`n_neighbors`)에 따라 성능이 달라짐
- 보통 데이터 건수의 제곱근으로 결정하는 경우 종종 있음
- **k값이 가장 클 때 (= 전체 데이터 개수) 가장 단순 모델** : **평균, 최빈값**
- **k값이 작을수록 복잡** 한 모델이 됨

2. 거리 계산법(metric)에 따라 성능이 달라질 수 있음
- Euclidean Distance
- Manhattan Distance

#### Decision Tree

- `max_depth`: 값이 작을수록 트리 깊이가 제한되어 모델이 단순해짐
- `min_samples_leaf`: leaf가 되기 위한 최소한의 샘플 데이터 수로, 값이 클수록 모델이 단순해짐
- `min_sampels_split`: 노드를 분할하기 위한 최소한의 샘플 데이터 수로, 값이 클수록 모델이 단순해짐

- 위 파라미터 값을 조정해 모델을 단순화시켜 과적합 위험을 줄임

### Hyperparameter 튜닝

> 1. 기본 모델 설정 (model_default)
> 2. 성능을 검증하고자 할 Hyperparameter 값 범위 설정
> 3. 기본 모델을 바탕으로 RandomizedSearchCV, GridSearchCV를 활용하여 다양한 모델 검증
> 3-1. CV가 들어간다는 것은 검증 방식에 K 분할 교차 검증 방식이 사용된다는 것
> 4. model.best_estimator_를 통해 최적 파라미터를 적용한 모델에 접근

- Grid Search는 모든 파라미터 조합에 대한 성능을 확인하여 베스트 파라미터를 찾는 것
- Random Search는 `n_iter` 지정
- 학습 데이터에 대한 성능에서는 Grid Search보다 Random Search가 더 좋은 성능을 파라미터를 찾는 경우는 없을 것
- 하지만 해당 파라미터(`max_depth`, `n_neighbors` 등)가 학습 데이터에 대한 성능은 좋을지 몰라도 이것이 곧 **평가 데이터에서 성능이 좋을 것이라는 것을 보장하지는 않음**
- 고로 Random Search를 통해 얻은 최적의 파라미터가 Grid Search를 통해 얻은 최적의 파라미터보다 평가 데이터에 대해서는 성능이 좋을 수 있음

### Grid Search, Random Search

```python
# 파라미터 1개인 경우
# Grid Search: 100번 수행하여 모든 경우의 성능 확인
# Random Search: 지정한 개수의 임의의 값에 대해서만 성능 확인
param = {'n_neighbors': range(1, 101)}

# 파라미터 2개인 경우
# Grid Search: 200번 수행하여 모든 경우의 성능 확인
# Random Search: 지정한 개수의 임의의 조합에 대해서만 성능 확인
param = {'n_neighbors': range(1, 101),
         'metric': ['euclidean', 'manhattan']}
```

![rand_grid_search](https://github.com/zacinthepark/TIL/assets/86648892/5c64025e-64db-4cda-b0c0-3fec051dbd89)

**Grid Search, Random Search를 사용할 때 내부적인 K-Fold Cross Validation을 위해 cv 값을 지정하므로, 실제 수행되는 횟수는 파라미터 조합 수 x cv 값이 됨**

#### Grid Search

1. 성능을 테스트할 파리미터 값의 범위를 지정 (딕셔너리 형태)
2. 위 파라미터 값 범위를 모두 사용하는 Grid Search 모델 선언 후 학습
3. 학습 데이터에 대해 가장 좋은 성능을 보인 파라미터 값으로 자동으로 학습함
4. 이후 예측 및 평가 과정을 바로 진행하면됨

#### Random Search

1. 성능을 테스트할 파라미터 값의 범위를 지정 (딕셔너리 형태)
2. 위 파라미터 값 범위에서 몇 개 선택할 지 정하여 Random Search 모델 선언 후 학습
3. 학습 데이터에 대해 가장 좋은 성능을 보인 파라미터 값으로 자동으로 학습함
4. 이후 예측 및 평가 과정을 바로 진행하면됨

### 튜닝 고려사항

- Grid Search 범위를 적게 하여 찾은 값을 기준으로 파라미터 범위를 조정하여 Grid Search를 다시 해보는 것 고려
- Random Search를 통해 찾은 값을 기준으로 파라미터 범위를 조정하여 Grid Search를 해보는 것도 고려
- 튜닝을 통해 최적화된 성능을 얻었더라도 운영환경에서 성능이 보장되는 것은 아님
    - 과적합 가능성
    - 미래에 발생할 데이터는 과거와 다를 수 있음
- 모델링 목표: 완벽한이 아닌, **적절한 예측력** 을 위해 **적절한 복잡도** 의 모델 완성

### Code: Random Search

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings(action='ignore')
%config InlineBackend.figure_format = 'retina'
```

```python
path = 'https://raw.githubusercontent.com/jangrae/csv/master/boston.csv'
data = pd.read_csv(path)
```

```python
target = 'medv'

x = data.drop(target, axis=1)
y = data[target]
```

```python
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)
```

```python
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import cross_val_score, RandomizedSearchCV, GridSearchCV
from sklearn.metrics import mean_absolute_error, r2_score

model_dt = DecisionTreeRegressor(random_state=1)

# 성능예측
# cv_score = cross_val_score(model_dt, x_train, y_train, cv=10, scoring='r2')
# 회귀에서는 r2_score, 분류에서는 accuracy_score 기반
cv_score = cross_val_score(model_dt, x_train, y_train, cv=10)

print(cv_score)
print(cv_score.mean())
```

<pre>
[0.65714654 0.60626309 0.90288602 0.81947244 0.2399945  0.78389795
 0.78738545 0.76528187 0.84699641 0.807198  ]
0.7216522274237595
</pre>

**모델 튜닝**

- 성능을 확인할 파라미터를 딕셔너리 형태로 선언

- 기존 모델을 기본으로 RandomizedSearchCV 알고리즘을 사용하는 모델을 선언

- 다음 정보를 최종 모델에 파라미터로 전달
    - 기본 모델 이름
    - 파라미터 변수
    - `cv`: K-Fold 분할 개수(기본값=5)
    - `n_iter`: 시도 횟수(기본값=10)
    - `scoring`: 평가 방법

```python
# 파라미터 선언
  # max_depth: 1~50

param = {'max_depth': range(1, 51)}

# Random Search 선언
  # cv=5
  # n_iter=20
  # scoring='r2'

model = RandomizedSearchCV(model_dt,     # 기본 모델
                           param,        # 파라미터 범위
                           cv=5,         # K-Fold 개수
                           n_iter=20,    # 선택할 임의 파라미터 개수 (테스트 해볼 max_depth 개수)
                           scoring='r2') # 평가 방법

# model = GridSearchCV(model_dt,     # 기본 모델
#                      param,        # 파라미터 범위
#                      cv=5,         # K-Fold 개수
#                      scoring='r2') # 평가 방법

model.fit(x_train, y_train)
```

**결과 확인**

- `model.cv_results_` 속성에 성능 테스트와 관련된 많은 정보가 포함되어있음
    - `model.cv_results_['mean_test_score']`: 테스트로 얻은 성능
    - `model.best_params_`: 최적의 파라미터
    - `model.best_score_`: 최고의 성능

```python
model.cv_results_
```

<pre>
{'mean_fit_time': array([0.00704017, 0.00773053, 0.00700631, 0.00773311, 0.00821328,
        0.00879359, 0.00842896, 0.00842271, 0.00392756, 0.00764828,
        0.00816154, 0.00640192, 0.00790281, 0.00320277, 0.0047297 ,
        0.00860276, 0.00738568, 0.00461664, 0.00750456, 0.00830617]),
 'std_fit_time': array([0.00068268, 0.00041332, 0.00061153, 0.00077895, 0.00049934,
        0.00082297, 0.00085625, 0.00049875, 0.00090442, 0.00084687,
        0.00088986, 0.00048902, 0.00070859, 0.00040194, 0.00060761,
        0.00090895, 0.00054396, 0.0004971 , 0.00044191, 0.0007097 ]),
 'mean_score_time': array([0.00219212, 0.00129948, 0.00140228, 0.00133185, 0.00150223,
        0.00160341, 0.00160847, 0.00203476, 0.00118914, 0.00198178,
        0.0016036 , 0.00139899, 0.00149908, 0.00120091, 0.00232825,
        0.00179944, 0.0016099 , 0.00168576, 0.0019124 , 0.00181184]),
 'std_score_time': array([0.00024414, 0.0004387 , 0.00049431, 0.00037989, 0.00045181,
        0.00079716, 0.00049078, 0.00070232, 0.00041276, 0.00064059,
        0.00053801, 0.00049109, 0.00044824, 0.00039568, 0.00090242,
        0.00074447, 0.0004767 , 0.00041057, 0.00048557, 0.00040758]),
 'param_max_depth': masked_array(data=[8, 35, 10, 14, 18, 26, 33, 49, 4, 31, 43, 11, 40, 3, 5,
                    47, 22, 6, 24, 25],
              mask=[False, False, False, False, False, False, False, False,
                    False, False, False, False, False, False, False, False,
                    False, False, False, False],
        fill_value='?',
             dtype=object),
 'params': [{'max_depth': 8},
  {'max_depth': 35},
  {'max_depth': 10},
  {'max_depth': 14},
  {'max_depth': 18},
  {'max_depth': 26},
  {'max_depth': 33},
  {'max_depth': 49},
  {'max_depth': 4},
  {'max_depth': 31},
  {'max_depth': 43},
  {'max_depth': 11},
  {'max_depth': 40},
  {'max_depth': 3},
  {'max_depth': 5},
  {'max_depth': 47},
  {'max_depth': 22},
  {'max_depth': 6},
  {'max_depth': 24},
  {'max_depth': 25}],
 'split0_test_score': array([0.64547442, 0.65873754, 0.64046397, 0.66821344, 0.65873754,
        0.65873754, 0.65873754, 0.65873754, 0.66601488, 0.65873754,
        0.65873754, 0.62262231, 0.65873754, 0.61138239, 0.6968166 ,
        0.65873754, 0.65873754, 0.67505184, 0.65873754, 0.65873754]),
 'split1_test_score': array([0.50394845, 0.49225288, 0.57205337, 0.49901433, 0.49225288,
        0.49225288, 0.49225288, 0.49225288, 0.57163069, 0.49225288,
        0.49225288, 0.51338038, 0.49225288, 0.57946071, 0.61685725,
        0.49225288, 0.49225288, 0.60650279, 0.49225288, 0.49225288]),
 'split2_test_score': array([0.7532683 , 0.78163071, 0.79876639, 0.75200489, 0.77190551,
        0.78163071, 0.78163071, 0.78163071, 0.80894417, 0.78163071,
        0.78163071, 0.79057112, 0.78163071, 0.71694136, 0.79619701,
        0.78163071, 0.78163071, 0.77811378, 0.78163071, 0.78163071]),
 'split3_test_score': array([0.82383751, 0.80327749, 0.72949709, 0.80104428, 0.80327749,
        0.80327749, 0.80327749, 0.80327749, 0.72006169, 0.80327749,
        0.80327749, 0.84011296, 0.80327749, 0.7175104 , 0.7264127 ,
        0.80327749, 0.80327749, 0.81943688, 0.80327749, 0.80327749]),
 'split4_test_score': array([0.81258669, 0.82834327, 0.78738102, 0.82501139, 0.82834327,
        0.82834327, 0.82834327, 0.82834327, 0.84536812, 0.82834327,
        0.82834327, 0.79723293, 0.82834327, 0.75704375, 0.85530345,
        0.82834327, 0.82834327, 0.85833666, 0.82834327, 0.82834327]),
 'mean_test_score': array([0.70782307, 0.71284838, 0.70563236, 0.70905766, 0.71090334,
        0.71284838, 0.71284838, 0.71284838, 0.72240391, 0.71284838,
        0.71284838, 0.71278394, 0.71284838, 0.67646772, 0.7383174 ,
        0.71284838, 0.71284838, 0.74748839, 0.71284838, 0.71284838]),
 'std_test_score': array([0.1199602 , 0.12477008, 0.087197  , 0.11793025, 0.12375434,
        0.12477008, 0.12477008, 0.12477008, 0.09851618, 0.12477008,
        0.12477008, 0.12432703, 0.12477008, 0.06850047, 0.08203949,
        0.12477008, 0.12477008, 0.09330148, 0.12477008, 0.12477008]),
 'rank_test_score': array([18,  4, 19, 17, 16,  4,  4,  4,  3,  4,  4, 15,  4, 20,  2,  4,  4,
         1,  4,  4])}
</pre>

```python
# 중요 정보 확인
print('=' * 80)
print(model.cv_results_['mean_test_score'])
print('-' * 80)
print('최적파라미터:', model.best_params_)
print('-' * 80)
print('최고성능:', model.best_score_)
print('=' * 80)
```

<pre>
================================================================================
[0.70782307 0.71284838 0.70563236 0.70905766 0.71090334 0.71284838
 0.71284838 0.71284838 0.72240391 0.71284838 0.71284838 0.71278394
 0.71284838 0.67646772 0.7383174  0.71284838 0.71284838 0.74748839
 0.71284838 0.71284838]
--------------------------------------------------------------------------------
최적파라미터: {'max_depth': 6}
--------------------------------------------------------------------------------
최고성능: 0.7474883885080482
================================================================================
</pre>

**변수 중요도**

- `model.best_estimator_` 모델의 변수 중요도를 확인

```python
# 변수 중요도
plt.figure(figsize=(5, 5))
plt.barh(y=list(x), width=model.best_estimator_.feature_importances_)
plt.show()
```

![z_rand_search](https://github.com/zacinthepark/TIL/assets/86648892/3ad0decc-d311-4d20-8eba-ef20bd557823)

```python
y_pred = model.predict(x_test)
print('MAE:', mean_absolute_error(y_test, y_pred))
print('R2-Score:', r2_score(y_test, y_pred))
```

<pre>
MAE: 2.763239793643037
R2-Score: 0.8477248406093285
</pre>

### Code: Grid Search

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings(action='ignore')
%config InlineBackend.figure_format = 'retina'
```

```python
path = 'https://raw.githubusercontent.com/jangrae/csv/master/boston.csv'
data = pd.read_csv(path)
```

```python
target = 'medv'

x = data.drop(target, axis=1)
y = data.loc[:, target]
```

```python
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)
```

```python
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import cross_val_score, GridSearchCV
from sklearn.metrics import mean_absolute_error, r2_score
```

```python
model_dt = DecisionTreeRegressor(random_state=1)

cv_score = cross_val_score(model_dt, x_train, y_train, cv=5)

print(cv_score)
print('평균:', cv_score.mean())
```

<pre>
[0.65873754 0.49225288 0.78163071 0.80327749 0.82834327]
평균: 0.7128483767547819
</pre>

**모델 튜닝**

```python
# 파라미터 선언
  # max_depth: 1~50
param = {'max_depth': range(1, 51)}

model_dt = DecisionTreeRegressor(random_state=2022)

model = GridSearchCV(model_dt,     # 기본 모델 이름
                     param,        # 앞에서 선언한 튜닝용 파라미터 변수
                     cv=5,         # k-fold cross validation (default=5)
                     scoring='r2') # 평가 방법

model.fit(x_train, y_train)
```

**결과 확인**

```python
# 중요 정보 확인
print('=' * 80)
print(model.cv_results_['mean_test_score'])
print('-' * 80)
print('최적파라미터:', model.best_params_)
print('-' * 80)
print('최고성능:', model.best_score_)
print('=' * 80)
```

<pre>
================================================================================
[0.37077174 0.57894062 0.67646772 0.7366794  0.73267571 0.74431291
 0.72422789 0.72013536 0.72618167 0.74227301 0.72794292 0.72910841
 0.71202047 0.73104951 0.73909045 0.73457447 0.73328739 0.74630935
 0.74760199 0.74760199 0.74760199 0.74760199 0.74760199 0.74760199
 0.74760199 0.74760199 0.74760199 0.74760199 0.74760199 0.74760199
 0.74760199 0.74760199 0.74760199 0.74760199 0.74760199 0.74760199
 0.74760199 0.74760199 0.74760199 0.74760199 0.74760199 0.74760199
 0.74760199 0.74760199 0.74760199 0.74760199 0.74760199 0.74760199
 0.74760199 0.74760199]
--------------------------------------------------------------------------------
최적파라미터: {'max_depth': 19}
--------------------------------------------------------------------------------
최고성능: 0.747601992668867
================================================================================
</pre>

**변수 중요도**

```python
# 변수 중요도
plt.figure(figsize=(5, 5))
plt.barh(y=list(x), width=model.best_estimator_.feature_importances_)
plt.show()
```

![z_grid_search](https://github.com/zacinthepark/TIL/assets/86648892/eb46c5b1-97eb-4888-ab40-9c97e0e55513)

```python
y_pred = model.predict(x_test)
print('MAE:', mean_absolute_error(y_test, y_pred))
print('R2-Score:', r2_score(y_test, y_pred))
```

<pre>
MAE: 2.719736842105263
R2-Score: 0.8440510497128647
</pre>
