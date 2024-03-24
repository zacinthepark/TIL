## Logistic Regression

---

> 1. x 데이터를 잘 설명하는 최적의 선형 회귀선(선형 판별식)을 찾는다.
> 2. 이를 로지스틱 함수(시그모이드 함수)를 통해 각 값에 대해 1이 될 확률을 구해 변환한다.
> 3. 최종적으로 임계값을 바탕으로 분류한다.

### 로지스틱 회귀

- 이진분류를 위한 알고리즘

- 확률 문제를 선형회귀로 모델링

- 확률값을 얻어서 확률값이 0.5보다 크면 1이라 분류하고, 0.5보다 작으면 0이라 분류할 수 있지 않을까?

- **$x$ 데이터가 주어졌을 때 확률을 예측하는 로지스틱 회귀분석은 학습 데이터를 잘 설명하는 선형 판별식의 기울기 $a$와 절편 $b$를 찾는 문제**

- 그리고 얻은 선형 판별식을 통해 확률값을 계산하여 분류

### 로지스틱 함수

![image](https://github.com/zacinthepark/TIL/assets/86648892/df2bd74b-88ea-4d0b-ab5e-56de74efd02d)

![image](https://github.com/zacinthepark/TIL/assets/86648892/9dfff225-a4aa-42de-9867-cd8a9917e5e0)

![image](https://github.com/zacinthepark/TIL/assets/86648892/4f8e6589-3258-42c8-a005-a018f3c71f74)

$$\large p = \frac{1}{1 + e^{-f(x)}}$$

- **시그모이드(sigmoid)** 함수라고도 부름

- $-f(x)$는 구한 선형 회귀식 (-inf ~ +inf)

- 확률값 $p$는 선형 판별식 값이 커지면 1, 작아지면 0에 가까운 값이 됨

- $(-\infty, \infty)$ 범위를 갖는 선형 판별식 결과로 `(0, 1)` 범위의 확률값을 얻게됨
    - `[0, 1]`은 경계값 포함 범위, `(0, 1)`은 경계값 포함하지 않는 범위, `(0, 1]`은 0포함 1포함하지 않음

- 기본적으로 확률값 `0.5`를 임계값(Threshold)로 하여 이보다 크면 1, 아니면 0으로 분류함

- 확률값을 얻어서, 임계값을 통한 전략 수립이 가능
    - 은행 대출의 경우 대출을 승인할지 말지 여부에서 임계값을 0.7로 올려 그 위는 1, 아래는 0으로 설정하면 더 엄격하게 심사를 하는 것이라 할 수 있음

- 임계값을 낮추면 적극적으로 1을 판단(recall을 올리려는 시도), 임계값을 올리면 소극적으로 1을 판단

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
path = 'https://raw.githubusercontent.com/jangrae/csv/master/diabetes.csv'
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
      <th>Pregnancies</th>
      <th>Glucose</th>
      <th>BloodPressure</th>
      <th>SkinThickness</th>
      <th>Insulin</th>
      <th>BMI</th>
      <th>DiabetesPedigreeFunction</th>
      <th>Age</th>
      <th>Outcome</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>6</td>
      <td>148</td>
      <td>72</td>
      <td>35</td>
      <td>0</td>
      <td>33.6</td>
      <td>0.627</td>
      <td>50</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>85</td>
      <td>66</td>
      <td>29</td>
      <td>0</td>
      <td>26.6</td>
      <td>0.351</td>
      <td>31</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>8</td>
      <td>183</td>
      <td>64</td>
      <td>0</td>
      <td>0</td>
      <td>23.3</td>
      <td>0.672</td>
      <td>32</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>89</td>
      <td>66</td>
      <td>23</td>
      <td>94</td>
      <td>28.1</td>
      <td>0.167</td>
      <td>21</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>137</td>
      <td>40</td>
      <td>35</td>
      <td>168</td>
      <td>43.1</td>
      <td>2.288</td>
      <td>33</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>

```python
data['Outcome'].value_counts()
```

<pre>
Outcome
0    500
1    268
Name: count, dtype: int64
</pre>

```python
data.corr(numeric_only=True)
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Pregnancies</th>
      <th>Glucose</th>
      <th>BloodPressure</th>
      <th>SkinThickness</th>
      <th>Insulin</th>
      <th>BMI</th>
      <th>DiabetesPedigreeFunction</th>
      <th>Age</th>
      <th>Outcome</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Pregnancies</th>
      <td>1.000000</td>
      <td>0.129459</td>
      <td>0.141282</td>
      <td>-0.081672</td>
      <td>-0.073535</td>
      <td>0.017683</td>
      <td>-0.033523</td>
      <td>0.544341</td>
      <td>0.221898</td>
    </tr>
    <tr>
      <th>Glucose</th>
      <td>0.129459</td>
      <td>1.000000</td>
      <td>0.152590</td>
      <td>0.057328</td>
      <td>0.331357</td>
      <td>0.221071</td>
      <td>0.137337</td>
      <td>0.263514</td>
      <td>0.466581</td>
    </tr>
    <tr>
      <th>BloodPressure</th>
      <td>0.141282</td>
      <td>0.152590</td>
      <td>1.000000</td>
      <td>0.207371</td>
      <td>0.088933</td>
      <td>0.281805</td>
      <td>0.041265</td>
      <td>0.239528</td>
      <td>0.065068</td>
    </tr>
    <tr>
      <th>SkinThickness</th>
      <td>-0.081672</td>
      <td>0.057328</td>
      <td>0.207371</td>
      <td>1.000000</td>
      <td>0.436783</td>
      <td>0.392573</td>
      <td>0.183928</td>
      <td>-0.113970</td>
      <td>0.074752</td>
    </tr>
    <tr>
      <th>Insulin</th>
      <td>-0.073535</td>
      <td>0.331357</td>
      <td>0.088933</td>
      <td>0.436783</td>
      <td>1.000000</td>
      <td>0.197859</td>
      <td>0.185071</td>
      <td>-0.042163</td>
      <td>0.130548</td>
    </tr>
    <tr>
      <th>BMI</th>
      <td>0.017683</td>
      <td>0.221071</td>
      <td>0.281805</td>
      <td>0.392573</td>
      <td>0.197859</td>
      <td>1.000000</td>
      <td>0.140647</td>
      <td>0.036242</td>
      <td>0.292695</td>
    </tr>
    <tr>
      <th>DiabetesPedigreeFunction</th>
      <td>-0.033523</td>
      <td>0.137337</td>
      <td>0.041265</td>
      <td>0.183928</td>
      <td>0.185071</td>
      <td>0.140647</td>
      <td>1.000000</td>
      <td>0.033561</td>
      <td>0.173844</td>
    </tr>
    <tr>
      <th>Age</th>
      <td>0.544341</td>
      <td>0.263514</td>
      <td>0.239528</td>
      <td>-0.113970</td>
      <td>-0.042163</td>
      <td>0.036242</td>
      <td>0.033561</td>
      <td>1.000000</td>
      <td>0.238356</td>
    </tr>
    <tr>
      <th>Outcome</th>
      <td>0.221898</td>
      <td>0.466581</td>
      <td>0.065068</td>
      <td>0.074752</td>
      <td>0.130548</td>
      <td>0.292695</td>
      <td>0.173844</td>
      <td>0.238356</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>

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
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
model = LogisticRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
```

<pre>
[[132  14]
 [ 36  49]]
              precision    recall  f1-score   support

           0       0.79      0.90      0.84       146
           1       0.78      0.58      0.66        85

    accuracy                           0.78       231
   macro avg       0.78      0.74      0.75       231
weighted avg       0.78      0.78      0.78       231
</pre>

```python
# 예측값 확인
print(y_test.values[10:30])
print(y_pred[10:30])
```

<pre>
[0 0 1 1 0 1 1 0 0 0 1 1 1 1 0 0 0 1 0 1]
[0 0 1 1 0 1 0 0 0 0 0 0 1 0 0 0 0 1 0 0]
</pre>

```python
# 확률값 확인
p = model.predict_proba(x_test)
# p: [0이 될 확률(1- 1이 될 확률), 1이 될 확률]
print(p[10:30])
```

<pre>
[[0.56950848 0.43049152]
 [0.92486108 0.07513892]
 [0.01884579 0.98115421]
 [0.27328721 0.72671279]
 [0.9752838  0.0247162 ]
 [0.28338027 0.71661973]
 [0.7640035  0.2359965 ]
 [0.69651884 0.30348116]
 [0.87012032 0.12987968]
 [0.84402724 0.15597276]
 [0.61771972 0.38228028]
 [0.86680791 0.13319209]
 [0.04823555 0.95176445]
 [0.73908678 0.26091322]
 [0.92726293 0.07273707]
 [0.59294068 0.40705932]
 [0.79790819 0.20209181]
 [0.27468483 0.72531517]
 [0.91827889 0.08172111]
 [0.54150086 0.45849914]]
</pre>

```python
# 1의 확률값 얻기
p1 = p[:, [1]]

# 임계값: 0.5 (default)
y_pred2 = np.array([1 if x > 0.5 else 0 for x in p1])
print(y_pred2[:20])
print(classification_report(y_test, y_pred2))
```

<pre>
[0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 1 0 0 0 0]
              precision    recall  f1-score   support

           0       0.79      0.90      0.84       146
           1       0.78      0.58      0.66        85

    accuracy                           0.78       231
   macro avg       0.78      0.74      0.75       231
weighted avg       0.78      0.78      0.78       231
</pre>

```python
# 임계값: 0.45
# recall 값 상승 (당뇨병 환자를 덜 놓치자)

y_pred3 = np.array([1 if x > 0.45 else 0 for x in p1])
print(y_pred3[:20])
print(classification_report(y_test, y_pred3))
```

<pre>
[0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 1 0 0 0 0]
              precision    recall  f1-score   support

           0       0.80      0.90      0.85       146
           1       0.78      0.60      0.68        85

    accuracy                           0.79       231
   macro avg       0.79      0.75      0.76       231
weighted avg       0.79      0.79      0.79       231
</pre>
