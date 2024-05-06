## Class Imbalance

---

- 클래스 불균형 문제의 경우 보통 알고리즘이 **다수 클래스를 더 많이 예측하는 쪽으로 모델이 편향** 되는 경향이 있음
- 즉, 소수의 클래스에서 오분류 비율이 높아짐
- 비즈니스 상황에서 Class Imbalance는 흔한 현상
    - 고객 이탈 예측: 잔존 > 이탈
    - 금융 비정상 거래 예측: 정상 > 비정상(사기거래)
    - 제조 공정 간 불량 예측: 정상 > 불량
- Accuracy는 높을 수 있지만 **적은 Class쪽 Recall이 매우 낮게 나올 수 있음**
- Resampling이나 Class Weight 조정을 통해 해결
    - **전반적인 성능을 높이기 위한 작업이 아니라, 소수 클래스 성능을 높이기 위한 작업임 (다수 클래스는 성능이 떨어짐)**

- [Resampling](#해결-방법-1-resampling)
- [Class Weight 조정](#해결-방법-2-class-weight-조정)

### 해결 방법 1: Resampling

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

import warnings
warnings.filterwarnings(action='ignore')
```

```python
seed = 28
x, y = make_classification(n_samples=1000, 
                           n_features=2, 
                           n_redundant=0, 
                           weights = [0.95, 0.05],  # class 0과 1의 비율 조정 (class imbalance 상황 만들기) 
                           n_clusters_per_class=1, 
                           random_state=seed)
```

```python
# 데이터 분포 확인
def data_scatter(x, y) :
    # y가 numpy이므로 시리즈로 변환하고 클래스별 개수 세기
    temp = pd.Series(y).value_counts()
    plt.figure(figsize=(6, 6))
    plt.title(f'0: {temp[0]}, 1: {temp[1]}')
    sns.scatterplot(x=x[:, 0], y=x[:, 1], hue=y)
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.show()
```

```python
data_scatter(x, y)
```

<p align="center">
  <img width="300" alt="z_imb_resampling_1" src="https://github.com/zacinthepark/TIL/assets/86648892/9587a8b3-90dd-4b53-9e47-8a034a2ded24">
</p>

```python
# SVM 모델 시각화 (Feature 수가 2개일 때 사용)
# 모델 2개를 비교
def svm_visualize(x, y, model1, model2=0):
    # mesh grid
    xx, yy = np.meshgrid(np.linspace(x[:, 0].min(), x[:, 0].max(), 50), 
                         np.linspace(x[:, 1].min(), x[:, 1].max(), 50))

    # mesh grid값에 대해 모델부터 거리값 만들기
    Z = model1.decision_function(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    if model2 != 0:  # 두번째 모델이 있으면 처리
        Z1 = model2.decision_function(np.c_[xx.ravel(), yy.ravel()])
        Z1 = Z1.reshape(xx.shape)

    plt.figure(figsize=(6, 6))
    sns.scatterplot(x=x[:, 0], y=x[:, 1], hue=y)
    plt.contour(xx, yy, Z, levels=[0], colors='gray', linestyles='--')

    if model2 != 0: # 두번째 모델이 있으면 처리
        plt.contour(xx, yy, Z1, levels=[0], colors='r', linestyles='--')

    plt.axis("tight")
    plt.show()
```

#### 불균형 데이터 그대로 사용하기

```python
# class imbalance
print(pd.Series(y).value_counts())
print('=' * 50)
print(pd.Series(y).value_counts(normalize=True))
```

<pre>
0    948
1     52
Name: count, dtype: int64
==================================================
0    0.948
1    0.052
Name: proportion, dtype: float64
</pre>

```python
from sklearn.svm import SVC
from sklearn.metrics import *

# 모델링 및 평가
model = SVC(kernel='linear')
model.fit(x, y)
pred = model.predict(x)

print(confusion_matrix(y, pred))
print('=' * 50)
print(classification_report(y, pred))
```

<pre>
[[940   8]
 [ 19  33]]
==================================================
              precision    recall  f1-score   support

           0       0.98      0.99      0.99       948
           1       0.80      0.63      0.71        52

    accuracy                           0.97      1000
   macro avg       0.89      0.81      0.85      1000
weighted avg       0.97      0.97      0.97      1000
</pre>

```python
svm_visualize(x, y, model)
```
<p align="center">
  <img width="300" alt="z_imb_resampling_2" src="https://github.com/zacinthepark/TIL/assets/86648892/b8afa2a8-0c4b-4b8c-a5c5-d986023e3508">
</p>

```python
from imblearn.under_sampling import RandomUnderSampler  # down
from imblearn.over_sampling import RandomOverSampler, SMOTE  # up, smote
```

#### 1-1. Down Sampling

<p align="center">
  <img width="700" alt="down_sampling" src="https://github.com/zacinthepark/TIL/assets/86648892/f5f7b6d7-3c6f-4ede-a5d5-3afd0c717533">
</p>

- 다수 Class의 데이터를
- 소수 Class의 수만큼 random sampling (비복원 추출)

```python
# Down Sampling: 적은 쪽 클래스는 그대로, 많은 쪽 클래스는 랜덤 샘플링 (적은 쪽 클래수 개수만큼)
rus = RandomUnderSampler(random_state=4)
x_d, y_d = rus.fit_resample(x, y)

data_scatter(x, y)
data_scatter(x_d, y_d)
```

<p align="center">
  <img width="300" alt="z_imb_resampling_3" src="https://github.com/zacinthepark/TIL/assets/86648892/931ed1f1-5fb9-433e-aadd-7f34e85d8cba">
  <img width="300" alt="z_imb_resampling_4" src="https://github.com/zacinthepark/TIL/assets/86648892/a392c399-7bd5-4853-be97-73f5b2118a88">
</p>

```python
# Down Sampling 데이터셋으로 학습 및 모델 시각화
model_d = SVC(kernel='linear')
model_d.fit(x_d, y_d)
svm_visualize(x_d, y_d, model_d)
```

<p align="center">
  <img width="300" alt="z_imb_resampling_5" src="https://github.com/zacinthepark/TIL/assets/86648892/329038c3-3782-4ecf-b944-d75b5b558248">
</p>

```python
# 기존 모델과 비교
svm_visualize(x, y, model, model_d)
```

<p align="center">
  <img width="300" alt="z_imb_resampling_6" src="https://github.com/zacinthepark/TIL/assets/86648892/2c59fbf9-9bc4-4692-a14c-c6804863daa8">
</p>

```python
# 기존 데이터 예측 및 평가 ==> 소수 클래스에 대한 recall이 매우 향상
pred = model_d.predict(x)

print(confusion_matrix(y, pred))
print('=' * 50)
print(classification_report(y, pred))
```

<pre>
[[888  60]
 [  2  50]]
==================================================
              precision    recall  f1-score   support

           0       1.00      0.94      0.97       948
           1       0.45      0.96      0.62        52

    accuracy                           0.94      1000
   macro avg       0.73      0.95      0.79      1000
weighted avg       0.97      0.94      0.95      1000
</pre>

#### 1-2. Up Sampling

<p align="center">
  <img width="700" alt="up_sampling" src="https://github.com/zacinthepark/TIL/assets/86648892/b60dc1eb-2286-43a1-96b3-b6514814473a">
</p>

- 소수 Class의 데이터를
- 다수 Class의 수만큼 random sampling (복원 추출)

```python
# Up Sampling: 많은 쪽 클래스는 그대로, 적은 쪽 클래스는 랜덤 샘플링(많은 쪽 클래스 개수만큼)
ros = RandomOverSampler(random_state=4)
x_u, y_u = ros.fit_resample(x, y)

data_scatter(x, y)
data_scatter(x_u, y_u)
```

<p align="center">
  <img width="300" alt="z_imb_resampling_7" src="https://github.com/zacinthepark/TIL/assets/86648892/5a75a7d6-3619-480d-8409-1cdda011cfc2">
  <img width="300" alt="z_imb_resampling_8" src="https://github.com/zacinthepark/TIL/assets/86648892/30496e20-ef61-4359-9d9e-8027af01eef4">
</p>

```python
# random 복원추출이다보니, 모든 값이 동일한 수만큼 추출된 것이 아니라, 각각 다르게 추출됨
UpSample = pd.DataFrame(x_u, columns=['x1', 'x2'])
UpSample['y'] = y_u

UpSample.loc[UpSample['y'] == 1].value_counts()
```

<pre>
x1         x2         y
 0.894752  -1.855946  1    28
 0.785587  -1.618389  1    25
 0.574446  -1.407863  1    24
 0.697953  -1.342480  1    24
 0.405838  -2.561105  1    23
 1.571462   0.370428  1    23
 1.499472  -0.916432  1    23
 1.096105  -0.849348  1    23
 1.895357  -0.006780  1    22
 1.226977  -0.111816  1    22
 0.879246  -2.158189  1    22
 0.643148  -0.878539  1    22
 1.282513  -1.406968  1    21
 1.333153  -1.287846  1    21
 1.288207  -0.564498  1    21
 1.127556   0.112743  1    20
 0.626623  -0.904875  1    20
 1.702421  -1.101668  1    20
 0.853566  -1.051973  1    19
 1.598135   0.362476  1    19
 1.188926  -0.770098  1    19
 1.159467  -1.587275  1    19
 0.985638  -1.697665  1    19
 1.245931  -0.031008  1    18
 1.447459  -0.425332  1    18
 1.300197  -0.267356  1    18
-1.328629  -2.054089  1    18
 0.919813  -0.903274  1    18
-1.127272  -1.611335  1    17
 0.577839  -0.572423  1    17
 0.648435  -1.927372  1    17
 0.656499  -1.617329  1    17
 0.692529  -1.062496  1    17
 1.064690  -0.876420  1    17
 1.159401  -0.927673  1    17
 1.185366  -0.425438  1    16
 0.632065  -1.369550  1    16
 1.220065  -0.399005  1    16
 0.721049  -1.207923  1    15
 0.531974  -1.876923  1    15
 1.123811  -0.093543  1    15
 0.743544  -1.196015  1    15
 1.102485  -0.066180  1    15
 0.747705  -1.656617  1    15
 1.684718  -0.454372  1    14
 1.702402   0.285148  1    14
 0.916845  -1.219220  1    14
 0.738462  -1.214681  1    13
 1.013208  -1.508976  1    13
 0.944517  -0.628437  1    12
 1.268728  -0.612163  1    11
 1.341268  -1.272969  1    11
Name: count, dtype: int64
</pre>

```python
# Up Sampling 데이터셋으로 학습 및 모델 시각화
model_u = SVC(kernel='linear')
model_u.fit(x_u, y_u)

svm_visualize(x_u, y_u, model_u)
```

<p align="center">
  <img width="300" alt="z_imb_resampling_9" src="https://github.com/zacinthepark/TIL/assets/86648892/59d87f6b-7697-41b0-9cbb-cb549ba6ba8d">
</p>

```python
# 기존 모델과 비교
svm_visualize(x, y, model, model_u)
```

<p align="center">
  <img width="300" alt="z_imb_resampling_10" src="https://github.com/zacinthepark/TIL/assets/86648892/5d315404-f9d2-4ee0-b4d3-77e9b22ca939">
</p>

```python
# 기존 데이터 예측 및 평가 ==> 소수 클래스에 대한 recall이 매우 향상
pred = model_u.predict(x)

print(confusion_matrix(y, pred))
print('=' * 50)
print(classification_report(y, pred))
```

<pre>
[[888  60]
 [  2  50]]
==================================================
              precision    recall  f1-score   support

           0       1.00      0.94      0.97       948
           1       0.45      0.96      0.62        52

    accuracy                           0.94      1000
   macro avg       0.73      0.95      0.79      1000
weighted avg       0.97      0.94      0.95      1000
</pre>

#### 1-3. SMOTE (Synthetic Minority Oversampling TEchnique)

<p align="center">
  <img width="700" alt="smote_1" src="https://github.com/zacinthepark/TIL/assets/86648892/488554e0-46ee-4669-9753-c37cae054584">
</p>

<p align="center">
  <img width="700" alt="smote_2" src="https://github.com/zacinthepark/TIL/assets/86648892/2e89e538-2ae4-4421-a9fe-6b60985273a5">
</p>

- 소수 Class의 데이터를
- 보간법(Interpolation)으로 새로운 데이터를 만듬

```python
# SMOTE: 많은 쪽 클래스는 그대로 혹은 약간의 Down Sampling, 적은 쪽 클래스는 보간법
smote = SMOTE(random_state=4)
x_sm, y_sm = smote.fit_resample(x, y)

data_scatter(x, y)
data_scatter(x_sm, y_sm)
```

<p align="center">
  <img width="300" alt="z_imb_resampling_11" src="https://github.com/zacinthepark/TIL/assets/86648892/6ff40950-0795-49c4-aef9-e65964181c8d">
  <img width="300" alt="z_imb_resampling_12" src="https://github.com/zacinthepark/TIL/assets/86648892/9fc1f31f-4815-4ebc-8616-0976d45f628f">
</p>

```python
# SMOTE Sampling 데이터셋으로 학습 및 모델 시각화
model_sm = SVC(kernel='linear')
model_sm.fit(x_sm, y_sm)

svm_visualize(x_sm, y_sm, model_sm)
```

<p align="center">
  <img width="300" alt="z_imb_resampling_13" src="https://github.com/zacinthepark/TIL/assets/86648892/b887f78b-e952-4c18-ad58-4be69da0f6a2">
</p>

```python
# 기존 모델과 비교
svm_visualize(x, y, model, model_sm)
```

<p align="center">
  <img width="300" alt="z_imb_resampling_14" src="https://github.com/zacinthepark/TIL/assets/86648892/f2fef98f-1110-4d54-bff1-168f15e089f1">
</p>

```python
# 기존 데이터 예측 및 평가 ==> 소수 클래스에 대한 recall이 매우 향상
pred = model_sm.predict(x)

print(confusion_matrix(y, pred))
print('=' * 50)
print(classification_report(y, pred))
```

<pre>
[[895  53]
 [  2  50]]
==================================================
              precision    recall  f1-score   support

           0       1.00      0.94      0.97       948
           1       0.49      0.96      0.65        52

    accuracy                           0.94      1000
   macro avg       0.74      0.95      0.81      1000
weighted avg       0.97      0.94      0.95      1000
</pre>

#### 1-4. 실습: Semiconductor Manufacturing Process Dataset

- 반도체 제조 공정은 시점별 수많은 센서로부터 정보를 수집하여 공정을 감시
- 센서 정보와 함께 공정 간 발생된 불량품에 대한 정보 저장
- 불량을 예측

```python
path = "https://raw.githubusercontent.com/DA4BAM/dataset/master/secom_9.csv"
data = pd.read_csv(path)

data['label'] = 0
data.loc[data['defeat'] == 'defeat', 'label'] = 1
data.drop(['datetime','defeat'], axis=1, inplace=True)
data.head()
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>v021</th>
      <th>v087</th>
      <th>v088</th>
      <th>v089</th>
      <th>v114</th>
      <th>v115</th>
      <th>v116</th>
      <th>v117</th>
      <th>v118</th>
      <th>v120</th>
      <th>...</th>
      <th>v528</th>
      <th>v571</th>
      <th>v572</th>
      <th>v573</th>
      <th>v574</th>
      <th>v575</th>
      <th>v576</th>
      <th>v577</th>
      <th>v578</th>
      <th>label</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.4026</td>
      <td>2.3895</td>
      <td>0.9690</td>
      <td>1747.6049</td>
      <td>0.9460</td>
      <td>0.0</td>
      <td>748.6115</td>
      <td>0.9908</td>
      <td>58.4306</td>
      <td>0.9804</td>
      <td>...</td>
      <td>6.6926</td>
      <td>533.8500</td>
      <td>2.1113</td>
      <td>8.95</td>
      <td>0.3157</td>
      <td>3.0624</td>
      <td>0.1026</td>
      <td>1.6765</td>
      <td>14.9509</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.3825</td>
      <td>2.3754</td>
      <td>0.9894</td>
      <td>1931.6464</td>
      <td>0.9425</td>
      <td>0.0</td>
      <td>731.2517</td>
      <td>0.9902</td>
      <td>58.6680</td>
      <td>0.9731</td>
      <td>...</td>
      <td>8.8370</td>
      <td>535.0164</td>
      <td>2.4335</td>
      <td>5.92</td>
      <td>0.2653</td>
      <td>2.0111</td>
      <td>0.0772</td>
      <td>1.1065</td>
      <td>10.9003</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1.4123</td>
      <td>2.4532</td>
      <td>0.9880</td>
      <td>1685.8514</td>
      <td>0.9231</td>
      <td>0.0</td>
      <td>718.5777</td>
      <td>0.9899</td>
      <td>58.4808</td>
      <td>0.9772</td>
      <td>...</td>
      <td>6.4568</td>
      <td>535.0245</td>
      <td>2.0293</td>
      <td>11.21</td>
      <td>0.1882</td>
      <td>4.0923</td>
      <td>0.0640</td>
      <td>2.0952</td>
      <td>9.2721</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1.4011</td>
      <td>2.4004</td>
      <td>0.9904</td>
      <td>1752.0968</td>
      <td>0.9564</td>
      <td>0.0</td>
      <td>709.0867</td>
      <td>0.9906</td>
      <td>58.6635</td>
      <td>0.9761</td>
      <td>...</td>
      <td>6.4865</td>
      <td>530.5682</td>
      <td>2.0253</td>
      <td>9.33</td>
      <td>0.1738</td>
      <td>2.8971</td>
      <td>0.0525</td>
      <td>1.7585</td>
      <td>8.5831</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1.3888</td>
      <td>2.4530</td>
      <td>0.9902</td>
      <td>1828.3846</td>
      <td>0.9424</td>
      <td>0.0</td>
      <td>796.5950</td>
      <td>0.9908</td>
      <td>58.3858</td>
      <td>0.9628</td>
      <td>...</td>
      <td>6.3745</td>
      <td>532.0155</td>
      <td>2.0275</td>
      <td>8.83</td>
      <td>0.2224</td>
      <td>3.1776</td>
      <td>0.0706</td>
      <td>1.6597</td>
      <td>10.9698</td>
      <td>0</td>
    </tr>
  </tbody>
</table>

<p>5 rows × 53 columns</p>

```python
print(data['label'].value_counts())  # 0: 정상, 1: 불량
print('=' * 50)
print(data['label'].value_counts() / data.shape[0])  # 비율
```

<pre>
label
0    1463
1     104
Name: count, dtype: int64
==================================================
label
0    0.933631
1    0.066369
Name: count, dtype: float64
</pre>

```python
target = 'label'
x = data.drop(target, axis=1)
y = data.loc[:, target]
x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.3, random_state=10)

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(x_train, y_train)

pred = model.predict(x_val)
print(confusion_matrix(y_val, pred))
print('=' * 50)
print(classification_report(y_val, pred))
```

<pre>
[[438   4]
 [ 29   0]]
==================================================
              precision    recall  f1-score   support

           0       0.94      0.99      0.96       442
           1       0.00      0.00      0.00        29

    accuracy                           0.93       471
   macro avg       0.47      0.50      0.48       471
weighted avg       0.88      0.93      0.90       471
</pre>

```python
# Resampling with SMOTE
smote = SMOTE()
x_train_sm, y_train_sm = smote.fit_resample(x_train, y_train)

model_sm = LogisticRegression()
model_sm.fit(x_train_sm, y_train_sm)

pred = model_sm.predict(x_val)
print(confusion_matrix(y_val, pred))
print('=' * 50)
print(classification_report(y_val, pred))
```

<pre>
[[273 169]
 [ 17  12]]
==================================================
              precision    recall  f1-score   support

           0       0.94      0.62      0.75       442
           1       0.07      0.41      0.11        29

    accuracy                           0.61       471
   macro avg       0.50      0.52      0.43       471
weighted avg       0.89      0.61      0.71       471
</pre>

```python
'''
- down sampling, up sampling, smote로 각각 데이터 저장
- 각각의 샘플을 활용하여 LogisticRegression Model 생성
- 각 모델의 예측 및 f1-score 결과를 저장 및 f1-score의 density plot을 비교
''';
```

```python
def lr_modeling(x_train, y_train, x_val, y_val):
    model = LogisticRegression()
    model.fit(x_train, y_train)
    pred = model.predict(x_val)
    return f1_score(y_val, pred, pos_label=1)
```

```python
from tqdm import tqdm  # 진행율

result_d, result_u, result_s = [], [], []

down_sampler = RandomUnderSampler()
up_sampler = RandomOverSampler()
smote = SMOTE()

for i in tqdm(range(100)):
    x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.4)
    d_x_train, d_y_train = down_sampler.fit_resample(x_train, y_train)
    u_x_train, u_y_train = up_sampler.fit_resample(x_train, y_train)
    s_x_train, s_y_train = smote.fit_resample(x_train, y_train)

    result_d.append(lr_modeling(d_x_train, d_y_train, x_val, y_val))
    result_u.append(lr_modeling(u_x_train, u_y_train, x_val, y_val))
    result_s.append(lr_modeling(s_x_train, s_y_train, x_val, y_val))
```

<pre>
100%|██████████████████████████████████████████████████████████████| 100/100 [00:15<00:00,  6.33it/s]
</pre>

```python
plt.figure(figsize=(10, 6))
sns.kdeplot(result_d, label='down')
sns.kdeplot(result_u, label='up')
sns.kdeplot(result_s, label='smote')

plt.xlabel('f1-score')
plt.legend()
plt.grid()
plt.show()
```

<p align="center">
  <img width="650" alt="z_imb_resampling_15" src="https://github.com/zacinthepark/TIL/assets/86648892/d11a9a50-f07d-4857-9248-7ade80875f1d">
</p>

### 해결 방법 2: Class Weight 조정

<p align="center">
    <img width="250" alt="imb_cls_weight" src="https://github.com/zacinthepark/TIL/assets/86648892/ee85dc8f-e5ce-4f36-b3b4-d648b1355e4f">
</p>

- Resampling 없이 클래스에 가중치를 부여하여 클래스 불균형 문제 해결
    - 학습하는 동안 알고리즘의 **비용 함수에서 소수 클래스에 더 많은 가중치를 부여** 하여 소수 클래스에 더 높은 페널티를 제공함으로써, 소수 클래스에 대한 오류를 줄이게 됨
        - 비용함수(손실함수)는 모델의 예측값과 실제값 사이의 차이를 수치화해주는 함수로, 해당 함수의 함수 값이 낮을수록 모델의 예측이 실제와 가깝다는 것을 의미
        - 패널티를 부과한다는 것은 모델이 잘못된 추론을 했을경우 더 큰 비용을 부과하는것을 의미
        - 소수 클래스를 잘못 추론했을 경우 더 큰 패널티를 주면 모델에 해당 오류에 큰 영향을 받게 하여 중요도를 높일 수 있음
    - sklearn의 알고리즘들은 대부분 옵션 `class_weight` 제공
        - `class_weight='None'`: 기본값
        - `class_weight='balanced'`: `y_train`의 class 비율을 역으로 적용
        - `class_weight={0: 0.2, 1: 0.8}`: 비율 지정 (단, 비율의 합은 1)

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

from tqdm import tqdm

import warnings
warnings.filterwarnings(action='ignore')
```

```python
seed = 28
x, y = make_classification(n_samples=1000, 
                           n_features=2, 
                           n_redundant=0, 
                           weights = [0.95, 0.05],  # class 0과 1의 비율 조정 (class imbalance 상황 만들기) 
                           n_clusters_per_class=1, 
                           random_state=seed)
```

```python
# 데이터 분포 확인
def data_scatter(x, y) :
    # y가 numpy이므로 시리즈로 변환하고 클래스별 개수 세기
    temp = pd.Series(y).value_counts()
    plt.figure(figsize=(6, 6))
    plt.title(f'0: {temp[0]}, 1: {temp[1]}')
    sns.scatterplot(x=x[:, 0], y=x[:, 1], hue=y)
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.show()
```

```python
# SVM 모델 시각화 (Feature 수가 2개일 때 사용)
# 모델 2개를 비교
def svm_visualize(x, y, model1, model2=0):
    # mesh grid
    xx, yy = np.meshgrid(np.linspace(x[:, 0].min(), x[:, 0].max(), 50), 
                         np.linspace(x[:, 1].min(), x[:, 1].max(), 50))

    # mesh grid값에 대해 모델부터 거리값 만들기
    Z = model1.decision_function(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    if model2 != 0:  # 두번째 모델이 있으면 처리
        Z1 = model2.decision_function(np.c_[xx.ravel(), yy.ravel()])
        Z1 = Z1.reshape(xx.shape)

    plt.figure(figsize=(6, 6))
    sns.scatterplot(x=x[:, 0], y=x[:, 1], hue=y)
    plt.contour(xx, yy, Z, levels=[0], colors='gray', linestyles='--')

    if model2 != 0: # 두번째 모델이 있으면 처리
        plt.contour(xx, yy, Z1, levels=[0], colors='r', linestyles='--')

    plt.axis("tight")
    plt.show()
```

```python
data_scatter(x, y)
```

<p align="center">
  <img width="300" alt="z_imb_class_weight_1" src="https://github.com/zacinthepark/TIL/assets/86648892/828db5bb-58fd-48b8-8d33-35dfaa055ff3">
</p>

```python
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import *
```

```python
# 모델링 및 평가
model = SVC(kernel='linear')
model.fit(x, y)
pred = model.predict(x)

print(confusion_matrix(y, pred))
print('=' * 50)
print(classification_report(y, pred))
```

<pre>
[[940   8]
 [ 19  33]]
==================================================
              precision    recall  f1-score   support

           0       0.98      0.99      0.99       948
           1       0.80      0.63      0.71        52

    accuracy                           0.97      1000
   macro avg       0.89      0.81      0.85      1000
weighted avg       0.97      0.97      0.97      1000
</pre>

#### 2-1. `class_weight='balanced'`

```python
# 모델링 및 평가
model_w = SVC(kernel='linear', class_weight='balanced')
model_w.fit(x, y)
pred = model1.predict(x)

print(confusion_matrix(y, pred))
print('=' * 50)
print(classification_report(y, pred))
```

<pre>
[[890  58]
 [  2  50]]
==================================================
              precision    recall  f1-score   support

           0       1.00      0.94      0.97       948
           1       0.46      0.96      0.62        52

    accuracy                           0.94      1000
   macro avg       0.73      0.95      0.80      1000
weighted avg       0.97      0.94      0.95      1000
</pre>

```python
svm_visualize(x, y, model, model_w)
```

<p align="center">
  <img width="300" alt="z_imb_class_weight_2" src="https://github.com/zacinthepark/TIL/assets/86648892/d1c9790c-9d58-4eb4-afa6-d23191ba00fe">
</p>

#### 2-2. `class_weight={0: ##, 1: ##}`

```python
weight = 0.99
model_w = SVC(kernel='linear', class_weight={0: (1-weight), 1: weight})
model_w.fit(x, y)
pred = model_w.predict(x)
print(confusion_matrix(y, pred))
print('=' * 50)
print(classification_report(y, pred))
```

<pre>
[[798 150]
 [  2  50]]
==================================================
              precision    recall  f1-score   support

           0       1.00      0.84      0.91       948
           1       0.25      0.96      0.40        52

    accuracy                           0.85      1000
   macro avg       0.62      0.90      0.65      1000
weighted avg       0.96      0.85      0.89      1000
</pre>

```python
svm_visualize(x, y, model, model_w)
```

<p align="center">
  <img width="300" alt="z_imb_class_weight_3" src="https://github.com/zacinthepark/TIL/assets/86648892/df2dc0f1-7b73-483c-a6d3-d2fd0a5ff0c0">
</p>

#### 2-3. 실습: Semiconductor Manufacturing Process Dataset

- 반도체 제조 공정은 시점별 수많은 센서로부터 정보를 수집하여 공정을 감시
- 센서 정보와 함께 공정 간 발생된 불량품에 대한 정보 저장
- 불량을 예측

```python
path = "https://raw.githubusercontent.com/DA4BAM/dataset/master/secom_9.csv"
data = pd.read_csv(path)

data['label'] = 0
data.loc[data['defeat'] == 'defeat', 'label'] = 1
data.drop(['datetime','defeat'], axis=1, inplace=True)
data.head()
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>v021</th>
      <th>v087</th>
      <th>v088</th>
      <th>v089</th>
      <th>v114</th>
      <th>v115</th>
      <th>v116</th>
      <th>v117</th>
      <th>v118</th>
      <th>v120</th>
      <th>...</th>
      <th>v528</th>
      <th>v571</th>
      <th>v572</th>
      <th>v573</th>
      <th>v574</th>
      <th>v575</th>
      <th>v576</th>
      <th>v577</th>
      <th>v578</th>
      <th>label</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.4026</td>
      <td>2.3895</td>
      <td>0.9690</td>
      <td>1747.6049</td>
      <td>0.9460</td>
      <td>0.0</td>
      <td>748.6115</td>
      <td>0.9908</td>
      <td>58.4306</td>
      <td>0.9804</td>
      <td>...</td>
      <td>6.6926</td>
      <td>533.8500</td>
      <td>2.1113</td>
      <td>8.95</td>
      <td>0.3157</td>
      <td>3.0624</td>
      <td>0.1026</td>
      <td>1.6765</td>
      <td>14.9509</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.3825</td>
      <td>2.3754</td>
      <td>0.9894</td>
      <td>1931.6464</td>
      <td>0.9425</td>
      <td>0.0</td>
      <td>731.2517</td>
      <td>0.9902</td>
      <td>58.6680</td>
      <td>0.9731</td>
      <td>...</td>
      <td>8.8370</td>
      <td>535.0164</td>
      <td>2.4335</td>
      <td>5.92</td>
      <td>0.2653</td>
      <td>2.0111</td>
      <td>0.0772</td>
      <td>1.1065</td>
      <td>10.9003</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1.4123</td>
      <td>2.4532</td>
      <td>0.9880</td>
      <td>1685.8514</td>
      <td>0.9231</td>
      <td>0.0</td>
      <td>718.5777</td>
      <td>0.9899</td>
      <td>58.4808</td>
      <td>0.9772</td>
      <td>...</td>
      <td>6.4568</td>
      <td>535.0245</td>
      <td>2.0293</td>
      <td>11.21</td>
      <td>0.1882</td>
      <td>4.0923</td>
      <td>0.0640</td>
      <td>2.0952</td>
      <td>9.2721</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1.4011</td>
      <td>2.4004</td>
      <td>0.9904</td>
      <td>1752.0968</td>
      <td>0.9564</td>
      <td>0.0</td>
      <td>709.0867</td>
      <td>0.9906</td>
      <td>58.6635</td>
      <td>0.9761</td>
      <td>...</td>
      <td>6.4865</td>
      <td>530.5682</td>
      <td>2.0253</td>
      <td>9.33</td>
      <td>0.1738</td>
      <td>2.8971</td>
      <td>0.0525</td>
      <td>1.7585</td>
      <td>8.5831</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1.3888</td>
      <td>2.4530</td>
      <td>0.9902</td>
      <td>1828.3846</td>
      <td>0.9424</td>
      <td>0.0</td>
      <td>796.5950</td>
      <td>0.9908</td>
      <td>58.3858</td>
      <td>0.9628</td>
      <td>...</td>
      <td>6.3745</td>
      <td>532.0155</td>
      <td>2.0275</td>
      <td>8.83</td>
      <td>0.2224</td>
      <td>3.1776</td>
      <td>0.0706</td>
      <td>1.6597</td>
      <td>10.9698</td>
      <td>0</td>
    </tr>
  </tbody>
</table>

<p>5 rows × 53 columns</p>

```python
print(data['label'].value_counts())  # 0: 정상, 1: 불량
print('=' * 50)
print(data['label'].value_counts() / data.shape[0])  # 비율
```

<pre>
label
0    1463
1     104
Name: count, dtype: int64
==================================================
label
0    0.933631
1    0.066369
Name: count, dtype: float64
</pre>

```python
target = 'label'
x = data.drop(target, axis=1)
y = data.loc[:, target]
x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.3, random_state=10)
```

```python
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import *

from sklearn.model_selection import GridSearchCV
```

```python
# 1. class_weight 옵션 활용
model = LogisticRegression(class_weight='balanced')
model.fit(x_train, y_train)
pred = model.predict(x_val)

print(confusion_matrix(y_val, pred))
print('=' * 50)
print(classification_report(y_val, pred))
```

<pre>
[[280 162]
 [ 16  13]]
==================================================
              precision    recall  f1-score   support

           0       0.95      0.63      0.76       442
           1       0.07      0.45      0.13        29

    accuracy                           0.62       471
   macro avg       0.51      0.54      0.44       471
weighted avg       0.89      0.62      0.72       471
</pre>

```python
# 2. Grid Search를 활용하여 클래스 비율 산출
from sklearn.model_selection import GridSearchCV

weights = np.linspace(0, 0.99, 100)
params = {'class_weight': [{0: x, 1: 1-x} for x in weights]}
params
```

<pre>
{'class_weight': [{0: 0.0, 1: 1.0},
  {0: 0.01, 1: 0.99},
  {0: 0.02, 1: 0.98},
  {0: 0.03, 1: 0.97},
  {0: 0.04, 1: 0.96},
  {0: 0.05, 1: 0.95},
  {0: 0.06, 1: 0.94},
  {0: 0.07, 1: 0.9299999999999999},
  {0: 0.08, 1: 0.92},
  {0: 0.09, 1: 0.91},
  {0: 0.1, 1: 0.9},
  {0: 0.11, 1: 0.89},
  {0: 0.12, 1: 0.88},
  {0: 0.13, 1: 0.87},
  {0: 0.14, 1: 0.86},
  {0: 0.15, 1: 0.85},
  {0: 0.16, 1: 0.84},
  {0: 0.17, 1: 0.83},
  {0: 0.18, 1: 0.8200000000000001},
  {0: 0.19, 1: 0.81},
  {0: 0.2, 1: 0.8},
  {0: 0.21, 1: 0.79},
  {0: 0.22, 1: 0.78},
  {0: 0.23, 1: 0.77},
  {0: 0.24, 1: 0.76},
  {0: 0.25, 1: 0.75},
  {0: 0.26, 1: 0.74},
  {0: 0.27, 1: 0.73},
  {0: 0.28, 1: 0.72},
  {0: 0.29, 1: 0.71},
  {0: 0.3, 1: 0.7},
  {0: 0.31, 1: 0.69},
  {0: 0.32, 1: 0.6799999999999999},
  {0: 0.33, 1: 0.6699999999999999},
  {0: 0.34, 1: 0.6599999999999999},
  {0: 0.35000000000000003, 1: 0.6499999999999999},
  {0: 0.36, 1: 0.64},
  {0: 0.37, 1: 0.63},
  {0: 0.38, 1: 0.62},
  {0: 0.39, 1: 0.61},
  {0: 0.4, 1: 0.6},
  {0: 0.41000000000000003, 1: 0.59},
  {0: 0.42, 1: 0.5800000000000001},
  {0: 0.43, 1: 0.5700000000000001},
  {0: 0.44, 1: 0.56},
  {0: 0.45, 1: 0.55},
  {0: 0.46, 1: 0.54},
  {0: 0.47000000000000003, 1: 0.53},
  {0: 0.48, 1: 0.52},
  {0: 0.49, 1: 0.51},
  {0: 0.5, 1: 0.5},
  {0: 0.51, 1: 0.49},
  {0: 0.52, 1: 0.48},
  {0: 0.53, 1: 0.47},
  {0: 0.54, 1: 0.45999999999999996},
  {0: 0.55, 1: 0.44999999999999996},
  {0: 0.56, 1: 0.43999999999999995},
  {0: 0.5700000000000001, 1: 0.42999999999999994},
  {0: 0.58, 1: 0.42000000000000004},
  {0: 0.59, 1: 0.41000000000000003},
  {0: 0.6, 1: 0.4},
  {0: 0.61, 1: 0.39},
  {0: 0.62, 1: 0.38},
  {0: 0.63, 1: 0.37},
  {0: 0.64, 1: 0.36},
  {0: 0.65, 1: 0.35},
  {0: 0.66, 1: 0.33999999999999997},
  {0: 0.67, 1: 0.32999999999999996},
  {0: 0.68, 1: 0.31999999999999995},
  {0: 0.6900000000000001, 1: 0.30999999999999994},
  {0: 0.7000000000000001, 1: 0.29999999999999993},
  {0: 0.71, 1: 0.29000000000000004},
  {0: 0.72, 1: 0.28},
  {0: 0.73, 1: 0.27},
  {0: 0.74, 1: 0.26},
  {0: 0.75, 1: 0.25},
  {0: 0.76, 1: 0.24},
  {0: 0.77, 1: 0.22999999999999998},
  {0: 0.78, 1: 0.21999999999999997},
  {0: 0.79, 1: 0.20999999999999996},
  {0: 0.8, 1: 0.19999999999999996},
  {0: 0.81, 1: 0.18999999999999995},
  {0: 0.8200000000000001, 1: 0.17999999999999994},
  {0: 0.8300000000000001, 1: 0.16999999999999993},
  {0: 0.84, 1: 0.16000000000000003},
  {0: 0.85, 1: 0.15000000000000002},
  {0: 0.86, 1: 0.14},
  {0: 0.87, 1: 0.13},
  {0: 0.88, 1: 0.12},
  {0: 0.89, 1: 0.10999999999999999},
  {0: 0.9, 1: 0.09999999999999998},
  {0: 0.91, 1: 0.08999999999999997},
  {0: 0.92, 1: 0.07999999999999996},
  {0: 0.93, 1: 0.06999999999999995},
  {0: 0.9400000000000001, 1: 0.05999999999999994},
  {0: 0.9500000000000001, 1: 0.04999999999999993},
  {0: 0.96, 1: 0.040000000000000036},
  {0: 0.97, 1: 0.030000000000000027},
  {0: 0.98, 1: 0.020000000000000018},
  {0: 0.99, 1: 0.010000000000000009}]}
</pre>

```python
model = GridSearchCV(LogisticRegression(), params, cv=5, scoring='f1')
model.fit(x_train, y_train)
```

```python
result = pd.DataFrame(model.cv_results_)
result.head()
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>mean_fit_time</th>
      <th>std_fit_time</th>
      <th>mean_score_time</th>
      <th>std_score_time</th>
      <th>param_class_weight</th>
      <th>params</th>
      <th>split0_test_score</th>
      <th>split1_test_score</th>
      <th>split2_test_score</th>
      <th>split3_test_score</th>
      <th>split4_test_score</th>
      <th>mean_test_score</th>
      <th>std_test_score</th>
      <th>rank_test_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.014684</td>
      <td>0.002226</td>
      <td>0.003913</td>
      <td>0.000806</td>
      <td>{0: 0.0, 1: 1.0}</td>
      <td>{'class_weight': {0: 0.0, 1: 1.0}}</td>
      <td>0.127660</td>
      <td>0.128205</td>
      <td>0.128205</td>
      <td>0.128205</td>
      <td>0.128205</td>
      <td>0.128096</td>
      <td>0.000218</td>
      <td>13</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.027960</td>
      <td>0.005981</td>
      <td>0.002504</td>
      <td>0.000633</td>
      <td>{0: 0.01, 1: 0.99}</td>
      <td>{'class_weight': {0: 0.01, 1: 0.99}}</td>
      <td>0.123348</td>
      <td>0.127854</td>
      <td>0.123894</td>
      <td>0.136986</td>
      <td>0.131004</td>
      <td>0.128617</td>
      <td>0.005028</td>
      <td>12</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.023398</td>
      <td>0.001318</td>
      <td>0.003172</td>
      <td>0.000663</td>
      <td>{0: 0.02, 1: 0.98}</td>
      <td>{'class_weight': {0: 0.02, 1: 0.98}}</td>
      <td>0.121495</td>
      <td>0.133971</td>
      <td>0.126126</td>
      <td>0.134615</td>
      <td>0.141509</td>
      <td>0.131544</td>
      <td>0.006999</td>
      <td>10</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.019057</td>
      <td>0.001348</td>
      <td>0.002275</td>
      <td>0.000182</td>
      <td>{0: 0.03, 1: 0.97}</td>
      <td>{'class_weight': {0: 0.03, 1: 0.97}}</td>
      <td>0.135266</td>
      <td>0.119403</td>
      <td>0.129353</td>
      <td>0.143590</td>
      <td>0.143590</td>
      <td>0.134240</td>
      <td>0.009164</td>
      <td>9</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.020293</td>
      <td>0.001008</td>
      <td>0.002572</td>
      <td>0.000481</td>
      <td>{0: 0.04, 1: 0.96}</td>
      <td>{'class_weight': {0: 0.04, 1: 0.96}}</td>
      <td>0.141176</td>
      <td>0.121547</td>
      <td>0.142012</td>
      <td>0.135593</td>
      <td>0.142857</td>
      <td>0.136637</td>
      <td>0.007962</td>
      <td>8</td>
    </tr>
  </tbody>
</table>

```python
weight = 1 - weights
f1 = result['mean_test_score']
best_cw = model.best_params_['class_weight'][1]
print(best_cw)
```

<pre>
0.9
</pre>

```python
plt.figure(figsize=(15, 8))
plt.plot(weight, f1)
plt.axvline(best_cw, color='r')
plt.grid()
plt.show()
```

<p align="center">
  <img width="650" alt="z_imb_class_weight_4" src="https://github.com/zacinthepark/TIL/assets/86648892/5b8a02ad-fde1-425a-a3b4-5fb3bb06b10a">
</p>
