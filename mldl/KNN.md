## K-Nearest Neighbor

---

### KNN

![knn_1](https://github.com/zacinthepark/TIL/assets/86648892/49780f89-5e35-4ebb-9b08-4c032e551c6c)

- 학습용 데이터에서 k개의 최근접 이웃의 값을 찾아 그 값들로 새로운 값을 예측하는 알고리즘
- 회귀와 분류에 사용되는 간단한 지도학습 알고리즘
    - KNN은 K를 데이터의 개수만큼 설정하면 예측값은 Regression의 경우 데이터의 평균값, Classification의 경우 데이터의 최빈값
- 연산 속도가 느리다는 단점이 있음
    - KNN은 fitting 과정은 단순히 학습 데이터를 메모리에 올리는 것에 불과
    - predict 과정에서 거리 계산을 통해 연산을 하기에 연산 속도가 느린 편임

### K값의 중요성

![knn_2](https://github.com/zacinthepark/TIL/assets/86648892/fe70ed8a-903c-4435-9686-e11f0bbcaf3e)

- k(탐색하는 이웃 개수)에 따라 데이터를 다르게 예측할 수도 있음
- k값에 따라 예측값이 달라지므로 **적절한 k값** 을 찾는 것이 중요 (기본값 = 5)
- 일반적으로
    - k를 1로 설정 안함: 이웃 하나로 현재 데이터를 판단하기에는 너무 편향된 정보
    - k를 홀수로 설정: 짝수인 경우 과반수 이상의 이웃이 나오지 않을 수 있음
- 검증 데이터로 가장 정확도가 높은 k를 찾아 KNN 알고리즘의 k로 사용

### 거리 구하기와 Scaling의 필요성

![knn_3](https://github.com/zacinthepark/TIL/assets/86648892/5859f0a8-56dd-4346-9222-0df6db1d8031)
![knn_4](https://github.com/zacinthepark/TIL/assets/86648892/30cd9bb0-dd05-4918-ac64-68884dae16d3)
![knn_5](https://github.com/zacinthepark/TIL/assets/86648892/f30762c9-c084-48c3-8d55-9bf9f6d904b8)

- 3개의 가장 가까운 이웃 별 색을 통해 검은별 색이 파랑인지 주황인지 분류
- 변수의 범위에 따라 거리 계산에 있어 중요도가 달라질 수 있음
- 대표적인 스케일링 방법은 **정규화(Normalization)** , **표준화(Standaradization)** 가 있음

$$ \large x_{norm}=\frac{x-x_{min}}{x_{max}-x_{min}}$$

1. 정규화: 각 변수의 값이 0과 1사이 값이 됨 (MinMaxScaling은 정규화에 해당)

$$ \large x_{z}=\frac{x-x_{mean}}{x_{std}}$$

2. 표준화: 각 변수의 평균이 0, 표준편차가 1이 됨

### 학습 데이터를 기준으로 정규화

<img src = "https://github.com/Jangrae/img/blob/master/minmax.png?raw=true" width=600 align="center"/>

- 일관된 예측을 위해 학습용 데이터를 통해 정규화를 진행하고 이를 학습 데이터, 평가 데이터 모두에 적용
- 평가용 데이터에도 학습용 데이터를 기준으로 스케일링을 수행함 (학습용 데이터의 최대값, 최소값, 평균 등을 사용)
- 평가용 데이터는 스케일링값이 0 ~ 1 범위라고 보장할 수는 없음
    - 그 차이가 너무 크다면 모델의 예측 성능이 떨어지므로 피팅을 다시 수행해야함
    - 범위에서 벗어나는 값에 대해서도 최근접 K개 이웃을 바탕으로 예측을 수행하기는 함
- Scaling 후에는 데이터프레임이 배열로 변환됨

### Code: 회귀

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
path = 'https://raw.githubusercontent.com/Jangrae/csv/master/airquality_simple.csv'
data = pd.read_csv(path)
```

```python
data.isnull().sum()
```

<pre>
Ozone      0
Solar.R    7
Wind       0
Temp       0
Month      0
Day        0
dtype: int64
</pre>

```python
# 시계열 데이터이므로 선형보간법으로 채우기
data.interpolate(method='linear', inplace=True)

# 확인
data.isnull().sum()
```

<pre>
Ozone      0
Solar.R    0
Wind       0
Temp       0
Month      0
Day        0
dtype: int64
</pre>

```python
#  변수 제거
drop_cols = ['Month', 'Day']
data.drop(drop_cols, axis=1, inplace=True)
```

```python
target = 'Ozone'
x = data.drop(target, axis=1)
y = data.loc[:, target]

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)
```

```python
plt.figure(figsize=(8, 2))
plt.boxplot(x_train, vert=False, labels=list(x))
plt.show()
```

![z_knn_1_1](https://github.com/zacinthepark/TIL/assets/86648892/9160d07e-7d60-4b26-9490-f0911c8ffb01)

- 방법 1: 공식 사용

$$ \large x_{norm}=\frac{x-x_{min}}{x_{max}-x_{min}}$$

```python
# 최댓값, 최솟값 구하기 (학습 데이터)
x_max = x_train.max()
x_min = x_train.min()

# 정규화
x_train = (x_train - x_min) / (x_max - x_min)
x_test = (x_test - x_min) / (x_max - x_min)
```

```python
# 정규화 후 값의 범위 확인
plt.figure(figsize=(8, 2))
plt.boxplot(x_train, vert=False, labels=list(x))
plt.show()
```

![z_knn_1_2](https://github.com/zacinthepark/TIL/assets/86648892/fc5003da-4273-441e-ac8d-27c271799fa3)

- 방법 2: 함수 사용

```python
from sklearn.preprocessing import MinMaxScaler

# 정규화
col_name = list(x_train)
scaler = MinMaxScaler()
# scaler.fit(x_train)
# x_train = scaler.transform(x_train)
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)
```

```python
# 데이터프레임 -> 배열
x_train[:10]
```

<pre>
array([[0.7706422 , 0.42105263, 0.44736842],
       [0.51376147, 0.69473684, 0.65789474],
       [0.96330275, 0.51578947, 0.31578947],
       [0.09174312, 0.39473684, 0.23684211],
       [0.92150866, 0.66315789, 0.        ],
       [0.96330275, 0.51578947, 0.60526316],
       [0.12538226, 0.66315789, 0.63157895],
       [0.86850153, 0.63684211, 0.89473684],
       [0.78593272, 0.66315789, 0.60526316],
       [0.44648318, 0.21052632, 0.84210526]])
</pre>

```python
# 정규화 후 값의 범위 확인
plt.figure(figsize=(8, 2))
plt.boxplot(x_train, vert=False, labels=list(x))
plt.show()
```

![z_knn_1_3](https://github.com/zacinthepark/TIL/assets/86648892/29af8bc2-042f-464a-a0a3-ca22b5a174ae)

```python
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error, r2_score
model = KNeighborsRegressor(n_neighbors=5)  # default: 5
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
print('MAE: ', mean_absolute_error(y_test, y_pred))
print('R2: ', r2_score(y_test, y_pred))
```

<pre>
MAE:  12.443478260869565
R2:  0.6168024614834005
</pre>

```python
plt.plot(y_test.values, label='Actual')
plt.plot(y_pred, label='Predicted')
plt.legend()
plt.ylabel('Ozone')
plt.show()
```

![z_knn_1_4](https://github.com/zacinthepark/TIL/assets/86648892/c74a2879-e4a7-4a2c-b783-0cbf929914f3)

### Code: 분류

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
path = 'https://raw.githubusercontent.com/jangrae/csv/master/Attrition_simple2.csv'
data = pd.read_csv(path)
```

- Attrition: 이직 여부 (1: 이직, 0: 잔류)
- Age: 나이
- DistanceFromHome: 집-직장 거리 (단위: 마일)
- EmployeeNumber: 사번
- Gender: 성별 (Male, Female)
- JobSatisfaction: 직무 만족도(1: Low, 2: Medium, 3: High, 4: Very High)
- MaritalStatus: 결혼 상태 (Single, Married, Divorced)
- MonthlyIncome: 월급 (단위: 달러)
- OverTime: 야근 여부 (Yes, No)
- PercentSalaryHike: 전년 대비 급여 인상율(단위: %)
- TotalWorkingYears: 총 경력 연수

```python
data.isnull().sum()
```

<pre>
Attrition            0
Age                  0
DistanceFromHome     0
EmployeeNumber       0
Gender               0
JobSatisfaction      0
MaritalStatus        0
MonthlyIncome        0
OverTime             0
PercentSalaryHike    0
TotalWorkingYears    0
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
      <th>Attrition</th>
      <th>Age</th>
      <th>DistanceFromHome</th>
      <th>EmployeeNumber</th>
      <th>JobSatisfaction</th>
      <th>MonthlyIncome</th>
      <th>PercentSalaryHike</th>
      <th>TotalWorkingYears</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Attrition</th>
      <td>1.000000</td>
      <td>-0.167866</td>
      <td>0.081973</td>
      <td>-0.008707</td>
      <td>-0.078936</td>
      <td>-0.163572</td>
      <td>-0.000048</td>
      <td>-0.182162</td>
    </tr>
    <tr>
      <th>Age</th>
      <td>-0.167866</td>
      <td>1.000000</td>
      <td>-0.010917</td>
      <td>-0.023786</td>
      <td>-0.012425</td>
      <td>0.490107</td>
      <td>-0.008303</td>
      <td>0.674331</td>
    </tr>
    <tr>
      <th>DistanceFromHome</th>
      <td>0.081973</td>
      <td>-0.010917</td>
      <td>1.000000</td>
      <td>0.054948</td>
      <td>-0.021623</td>
      <td>-0.012803</td>
      <td>0.052348</td>
      <td>0.002606</td>
    </tr>
    <tr>
      <th>EmployeeNumber</th>
      <td>-0.008707</td>
      <td>-0.023786</td>
      <td>0.054948</td>
      <td>1.000000</td>
      <td>-0.022863</td>
      <td>-0.014032</td>
      <td>-0.009514</td>
      <td>-0.016317</td>
    </tr>
    <tr>
      <th>JobSatisfaction</th>
      <td>-0.078936</td>
      <td>-0.012425</td>
      <td>-0.021623</td>
      <td>-0.022863</td>
      <td>1.000000</td>
      <td>-0.025082</td>
      <td>0.030811</td>
      <td>-0.039380</td>
    </tr>
    <tr>
      <th>MonthlyIncome</th>
      <td>-0.163572</td>
      <td>0.490107</td>
      <td>-0.012803</td>
      <td>-0.014032</td>
      <td>-0.025082</td>
      <td>1.000000</td>
      <td>-0.021334</td>
      <td>0.768437</td>
    </tr>
    <tr>
      <th>PercentSalaryHike</th>
      <td>-0.000048</td>
      <td>-0.008303</td>
      <td>0.052348</td>
      <td>-0.009514</td>
      <td>0.030811</td>
      <td>-0.021334</td>
      <td>1.000000</td>
      <td>-0.021988</td>
    </tr>
    <tr>
      <th>TotalWorkingYears</th>
      <td>-0.182162</td>
      <td>0.674331</td>
      <td>0.002606</td>
      <td>-0.016317</td>
      <td>-0.039380</td>
      <td>0.768437</td>
      <td>-0.021988</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>

```python
# 제거 대상: EmployeeNumber
del_cols = ['EmployeeNumber']

# 변수 제거
data.drop(del_cols, axis=1, inplace=True)
```

```python
target = 'Attrition'
x = data.drop(target, axis=1)
y = data.loc[:, target]
```

```python
# 가변수화 대상: Gender, JobSatisfaction, MaritalStatus, OverTime
dumm_cols = ['Gender', 'JobSatisfaction', 'MaritalStatus', 'OverTime']
x = pd.get_dummies(x, columns=dumm_cols, drop_first=True, dtype=int)
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
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report
model = KNeighborsClassifier()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
```

<pre>
[[289  11]
 [ 58   1]]
              precision    recall  f1-score   support

           0       0.83      0.96      0.89       300
           1       0.08      0.02      0.03        59

    accuracy                           0.81       359
   macro avg       0.46      0.49      0.46       359
weighted avg       0.71      0.81      0.75       359
</pre>
