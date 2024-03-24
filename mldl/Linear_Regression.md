## Linear Regression

---

### 선형회귀란

> Regression to the mean!

- 선형 회귀 모델은 선형 함수를 이용해서 회귀(Regression)를 수행하는 모델을 뜻함
- `y = Wx + b`
    - x, y는 가지고 있는 데이터
    - **W** 와 **b** 는 **데이터에 적합한 값으로 학습** 될 수 있는 **파라미터(Parameter)**
    - W는 가중치, b는 편향
    - 최선의 회귀모델은 전체 데이터의 **오차 합이 최소** 가 되는 모델을 의미
        - sklearn은 linear regression의 경우 독립변수의 가중치를 계산할 때 경사하강법, 최소제곱법 중 최소제곱법을 사용함
    - 결국 오차 합이 최소가 되는 가중치와 편향을 찾는 것이 선형 회귀 모델링
- 독립변수가 하나라면 단순 회귀, 독립변수가 여러 개라면 다중 회귀

### 변수 선택

- 회귀 모델에서 변수가 많으면 과적합이 발생할 수 있는 가능성이 크다
- 그렇기에 적절한 변수 선택이 중요하다

1. r2 score 확인: 데이터프레임에서 for문을 돌려 x 변수들을 하나씩 빼봐서 전체 x일 때의 r2 score와 비교하여 현격히 떨어지면 중요한 변수라고 판단
2. 다중공선성 확인: y를 제외하고 x끼리의 데이터프레임에서 하나의 x를 종속변수로 삼고 나머지 x 변수들로 예측했을 때 r2 score가 높다면 다중공선성이 높다고 판단

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
data.head()
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>speed</th>
      <th>dist</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>10</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7</td>
      <td>4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>7</td>
      <td>22</td>
    </tr>
    <tr>
      <th>4</th>
      <td>8</td>
      <td>16</td>
    </tr>
  </tbody>
</table>
</div>

```python
data.describe()
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>speed</th>
      <th>dist</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>50.000000</td>
      <td>50.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>15.400000</td>
      <td>42.980000</td>
    </tr>
    <tr>
      <th>std</th>
      <td>5.287644</td>
      <td>25.769377</td>
    </tr>
    <tr>
      <th>min</th>
      <td>4.000000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>12.000000</td>
      <td>26.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>15.000000</td>
      <td>36.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>19.000000</td>
      <td>56.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>25.000000</td>
      <td>120.000000</td>
    </tr>
  </tbody>
</table>
</div>

```python
data.isnull().sum()
```

<pre>
speed    0
dist     0
dtype: int64
</pre>

```python
# speed, dist 관계
plt.scatter(x='speed', y='dist', data=data)
plt.xlabel('Speed(mph)')
plt.ylabel('Dist(ft)')
plt.show()
```

![z_ml_3_1](https://github.com/zacinthepark/TIL/assets/86648892/685306a4-8e7f-4423-8d6f-2f5f879e7525)

```python
target = 'dist'
x = data.drop(target, axis=1)
y = data.loc[:, target]

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

model = LinearRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

print('MAE: ', mean_absolute_error(y_test, y_pred))
print('R2: ', r2_score(y_test, y_pred))
```

<pre>
MAE:  15.113442990354987
R2:  0.5548332681132087
</pre>

```python
# 회귀계수 확인

print(list(x_train))
print('가중치(기울기): ', model.coef_)
print('편향(절편): ', model.intercept_)
```

<pre>
['speed']
가중치(기울기):  [3.91046344]
편향(절편):  -16.373364149357656
</pre>

```python
# 가중치 시각화
tmp = pd.DataFrame()
tmp['feature'] = list(x)
tmp['weight'] = model.coef_
plt.figure(figsize=(5, 8))
plt.barh(y=tmp['feature'], width=tmp['weight'])
plt.show()
```

$$\Large Distance = -16.373364149357656 + 3.91046344*Speed $$

```python
np.linspace(1, 10, 5)
```

<pre>
array([ 1.  ,  3.25,  5.5 ,  7.75, 10.  ])
</pre>

```python
# 회귀식 만들기

a = model.coef_
b = model.intercept_
speed = np.linspace(x_test.min(), x_test.max(), 10)
dist = a * speed + b
```

```python
# 회귀선 표시
# a와 b는 train data를 바탕으로 한 것
# 선의 y값은 y_pred 이며, 테스트 데이터보다 학습 데이터에 더 최적화됨

dist_mean = y_train.mean()

plt.scatter(x_test, y_test)
plt.scatter(x_test, y_pred)
plt.scatter(x_train, y_train)
plt.plot(speed, dist, color='r')
plt.axhline(dist_mean, color='r', linestyle='--')

plt.title('Speed & Distance', size=15, pad=10)
plt.ylabel('Dist(ft)')
plt.xlabel('Speed(mph)')

plt.show()
```

![z_ml_3_2](https://github.com/zacinthepark/TIL/assets/86648892/17fc7372-6703-4e6a-9899-e8625bfd7757)

```python
# 시각화
plt.plot(y_test.values, label='Actual')
plt.plot(y_pred, label='Predicted')
plt.legend()
plt.ylabel('Dist(ft)')
plt.show()
```

![z_ml_3_3](https://github.com/zacinthepark/TIL/assets/86648892/2f66c93e-0695-432f-aa99-d58309e50b91)
