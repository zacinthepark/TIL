## Functional API

---

### Sequential API vs. Functional API

<p align="center">
    <img width="600" alt="sequential_functional" src="https://github.com/zacinthepark/TIL/assets/86648892/6d56073d-680f-488f-8a9e-167598207247">
</p>

좌측은 Sequential, 우측은 Functional

#### Sequential API

- 순차적으로 쌓아가며 모델 생성
- Input에서 Output Layer로 순차적 연결
- `Sequential` 함수 안에 리스트로 레이어 입력

```python
clear_session()

model = Sequential([
    Dense(18, input_shape=(nfeatures,), activation='relu'), 
    Dense(4, activation='relu'), 
    Dense(1)
])

model.summary()
```

#### Functional API

> 1. Input 지정
> 2. 레이어는 앞 레이어와의 연결 지정
> 3. 모델로 시작과 끝을 연결해서 선언

- 모델을 좀 더 복잡하게 구성
- 모델을 분리해서 사용 가능
- 다중 입력, 다중 출력 가능

```python
clear_session()

il = Input(shape=(nfeatures,))
hl_1 = Dense(18, activation='relu')(il)
hl_2 = Dense(4, activation='relu')(hl_1)
ol = Dense(1)(hl_2)

model = Model(inputs=il, outputs=ol)

model.summary()
```

### 다중 입력

- 명시적으로 학습하는 Feature 그룹을 구분하고 싶을 때 사용할 수 있음
- 다양한 종류의 입력을 통해 각 입력에 맞는 특징 도출(feature representation)이 가능
- 여러 개의 Input Layer가 있을 때, 학습하는 데이터의 분석 단위(개수)는 동일해야한다
- 모델 선언, 학습, 예측 시에 다중 입력 층들을 리스트로 제공해야한다

<p align="center">
    <img width="600" alt="many_inputs" src="https://github.com/zacinthepark/TIL/assets/86648892/efc4776a-9055-4d7b-933d-ee51686d27d2">
</p>

- 카시트 판매 데이터를 2가지 입력으로 구분
    - 입력 1: 판매 관련 정보: Advertising, Price, ShelveLoc, US, Urban, CompPrice
    - 입력 2: 외부 환경 정보: Income, Population, Age, Education


<p align="center">
    <img width="400" height="300" alt="carseat_inputs" src="https://github.com/zacinthepark/TIL/assets/86648892/66f5ed82-5936-4302-bf89-9fd3b2ac85c7">
</p>

<p align="center">
    <img width="600" alt="concatenate_layers" src="https://github.com/zacinthepark/TIL/assets/86648892/973db627-6f2b-40e5-b967-3c3eb7ef8efb">
</p>

```python
# 모델 구성
input_1 = Input(shape=(nfeatures_1,), name='input_1')
input_2 = Input(shape=(nfeatures_2,), name='input_2')

# 입력을 위한 레이어
hl_1_1 = Dense(10, activation='relu')(input_1)
hl_1_1 = Dense(20, activation='relu')(input_2)

# 두 히든레이어 옆으로 합치기 (= pd.concat)
cbl = concatenate([hl_1_1, hl_1_1])

# 추가 레이어
hl_2 = Dense(8, activation='relu')(cbl)
output = Dense(1)(hl_2)

# 모델 선언
model = Model(inputs=[input_1, input_2], outputs=output)
```

```python
# 모델 예측 시, 전처리된 두 가지 입력을 리스트로 묶어서 사용

pred = model.predict([x_val_1, x_val_2])
```

### Code

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.metrics import *
from sklearn.preprocessing import MinMaxScaler

from keras.models import Sequential, Model
from keras.layers import Input, Dense, concatenate
from keras.backend import clear_session
from keras.optimizers import Adam
```

```python
def dl_history_plot(history):
    plt.figure(figsize=(10, 6))
    plt.plot(history['loss'], label='train_err', marker='.')
    plt.plot(history['val_loss'], label='val_err', marker='.')

    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend()
    plt.grid()
    plt.show()
```

```python
path = 'https://raw.githubusercontent.com/DA4BAM/dataset/master/Carseats.csv'
data = pd.read_csv(path)
data.head()
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Sales</th>
      <th>CompPrice</th>
      <th>Income</th>
      <th>Advertising</th>
      <th>Population</th>
      <th>Price</th>
      <th>ShelveLoc</th>
      <th>Age</th>
      <th>Education</th>
      <th>Urban</th>
      <th>US</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>9.50</td>
      <td>138</td>
      <td>73</td>
      <td>11</td>
      <td>276</td>
      <td>120</td>
      <td>Bad</td>
      <td>42</td>
      <td>17</td>
      <td>Yes</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>1</th>
      <td>11.22</td>
      <td>111</td>
      <td>48</td>
      <td>16</td>
      <td>260</td>
      <td>83</td>
      <td>Good</td>
      <td>65</td>
      <td>10</td>
      <td>Yes</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>2</th>
      <td>10.06</td>
      <td>113</td>
      <td>35</td>
      <td>10</td>
      <td>269</td>
      <td>80</td>
      <td>Medium</td>
      <td>59</td>
      <td>12</td>
      <td>Yes</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>3</th>
      <td>7.40</td>
      <td>117</td>
      <td>100</td>
      <td>4</td>
      <td>466</td>
      <td>97</td>
      <td>Medium</td>
      <td>55</td>
      <td>14</td>
      <td>Yes</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4.15</td>
      <td>141</td>
      <td>64</td>
      <td>3</td>
      <td>340</td>
      <td>128</td>
      <td>Bad</td>
      <td>38</td>
      <td>13</td>
      <td>Yes</td>
      <td>No</td>
    </tr>
  </tbody>
</table>

```python
target = 'Sales'
x = data.drop(target, axis=1)
y = data.loc[:, target]
```

```python
# 가변수화

cat_cols = ['ShelveLoc', 'Education', 'US', 'Urban']
x = pd.get_dummies(x, columns=cat_cols, drop_first=True)
```

```python
x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=.2, random_state=20)
```

```python
# 스케일링

scaler = MinMaxScaler()
x_train = scaler.fit_transform(x_train)
x_val = scaler.transform(x_val)
```

```python
nfeatures = x_train.shape[1]
nfeatures
```

<pre>
18
</pre>

#### Sequential 모델링

```python
clear_session()
model = Sequential([Dense(18 ,input_shape=(nfeatures,), activation='relu'),
                    Dense(4, activation='relu'),
                    Dense(1)])
model.summary()
```

<pre>
Model: "sequential"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 dense (Dense)               (None, 18)                342       
                                                                 
 dense_1 (Dense)             (None, 4)                 76        
                                                                 
 dense_2 (Dense)             (None, 1)                 5         
                                                                 
=================================================================
Total params: 423 (1.65 KB)
Trainable params: 423 (1.65 KB)
Non-trainable params: 0 (0.00 Byte)
_________________________________________________________________
</pre>

#### Functional 모델링

```python
clear_session()

il = Input(shape=(nfeatures,))
hl1 = Dense(18, activation='relu')(il)
hl2 = Dense(4, activation='relu')(hl1)
ol = Dense(1)(hl2)

model = Model(inputs=il, outputs=ol)
model.summary()
```

<pre>
Model: "model"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 input_1 (InputLayer)        [(None, 18)]              0         
                                                                 
 dense (Dense)               (None, 18)                342       
                                                                 
 dense_1 (Dense)             (None, 4)                 76        
                                                                 
 dense_2 (Dense)             (None, 1)                 5         
                                                                 
=================================================================
Total params: 423 (1.65 KB)
Trainable params: 423 (1.65 KB)
Non-trainable params: 0 (0.00 Byte)
_________________________________________________________________
</pre>

```python
# 컴파일 + 학습

model.compile(optimizer=Adam(learning_rate=0.01), loss='mse')
hist = model.fit(x_train, y_train, epochs=50, validation_split= 0.2, verbose=0).history
```

```python
dl_history_plot(hist)
```

![z_dl_8_1](https://github.com/zacinthepark/TIL/assets/86648892/bf51da93-1f0f-4608-9276-d22109aa4574)

```python
pred = model.predict(x_val)
print(mean_squared_error(y_val, pred, squared=False))
print(mean_absolute_error(y_val, pred))
```

<pre>
3/3 [==============================] - 0s 4ms/step
1.5362562780394342
1.1876072006225589
</pre>

```python
clear_session()
model = Sequential([Dense(18,input_shape=(nfeatures,), activation='relu'),
                    Dense(4, activation='relu') ,
                    Dense(4, activation='relu') ,
                    Dense(1)])
model.summary()
```

#### Sequential을 Functional로 변환해보기

<pre>
Model: "sequential"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 dense (Dense)               (None, 18)                342       
                                                                 
 dense_1 (Dense)             (None, 4)                 76        
                                                                 
 dense_2 (Dense)             (None, 4)                 20        
                                                                 
 dense_3 (Dense)             (None, 1)                 5         
                                                                 
=================================================================
Total params: 443 (1.73 KB)
Trainable params: 443 (1.73 KB)
Non-trainable params: 0 (0.00 Byte)
_________________________________________________________________
</pre>

```python
clear_session()

# Input
il = Input(shape=(nfeatures,))

# 연결
hl1 = Dense(18, activation='relu')(il)
hl2 = Dense(4, activation='relu')(hl1)
hl3 = Dense(4, activation='relu')(hl2)
ol = Dense(1)(hl3)

# Model
model = Model(inputs=il, outputs=ol)
model.summary()
```

<pre>
Model: "model"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 input_1 (InputLayer)        [(None, 18)]              0         
                                                                 
 dense (Dense)               (None, 18)                342       
                                                                 
 dense_1 (Dense)             (None, 4)                 76        
                                                                 
 dense_2 (Dense)             (None, 4)                 20        
                                                                 
 dense_3 (Dense)             (None, 1)                 5         
                                                                 
=================================================================
Total params: 443 (1.73 KB)
Trainable params: 443 (1.73 KB)
Non-trainable params: 0 (0.00 Byte)
_________________________________________________________________
</pre>

<p align="center">
  <img width="500" alt="dl_8_model_structure" src="https://github.com/zacinthepark/TIL/assets/86648892/339d5a1e-a563-4105-90ad-4befda180570">
</p>

```python
clear_session()

# Input
il = Input(shape=(nfeatures,))

# 연결
hl1 = Dense(10, activation='relu')(il)
h12 = Dense(10, activation='relu')(hl1)
hl3 = Dense(2, activation='relu')(h12)
ol = Dense(1)(hl3)

# Model
model = Model(inputs=il, outputs=ol)
model.summary()
```

<pre>
Model: "model"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 input_1 (InputLayer)        [(None, 18)]              0         
                                                                 
 dense (Dense)               (None, 10)                190       
                                                                 
 dense_1 (Dense)             (None, 10)                110       
                                                                 
 dense_2 (Dense)             (None, 2)                 22        
                                                                 
 dense_3 (Dense)             (None, 1)                 3         
                                                                 
=================================================================
Total params: 325 (1.27 KB)
Trainable params: 325 (1.27 KB)
Non-trainable params: 0 (0.00 Byte)
_________________________________________________________________
</pre>

#### 다중 입력

```python
# 전처리 수행

# 데이터 분할: x, y
target = 'Sales'
x = data.drop(target, axis=1)
y = data.loc[:, target]

# 가변수화
cat_cols = ['ShelveLoc', 'Education', 'US', 'Urban']
x = pd.get_dummies(x, columns=cat_cols, drop_first=True)

# 데이터 분할: train, val
x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=.2, random_state=20)

# 스케일링
scaler = MinMaxScaler()
x_train = scaler.fit_transform(x_train)
x_val = scaler.transform(x_val)

# 컬럼 이름으로 조작하기 위해 데이터프레임으로 변환
x_train = pd.DataFrame(x_train, columns=x.columns)
x_val = pd.DataFrame(x_val, columns=x.columns)
```

```python
x_train.head()
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>CompPrice</th>
      <th>Income</th>
      <th>Advertising</th>
      <th>Population</th>
      <th>Price</th>
      <th>Age</th>
      <th>ShelveLoc_Good</th>
      <th>ShelveLoc_Medium</th>
      <th>Education_11</th>
      <th>Education_12</th>
      <th>Education_13</th>
      <th>Education_14</th>
      <th>Education_15</th>
      <th>Education_16</th>
      <th>Education_17</th>
      <th>Education_18</th>
      <th>US_Yes</th>
      <th>Urban_Yes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.387755</td>
      <td>0.767677</td>
      <td>0.172414</td>
      <td>0.248497</td>
      <td>0.402685</td>
      <td>0.545455</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.204082</td>
      <td>0.252525</td>
      <td>0.379310</td>
      <td>0.515030</td>
      <td>0.557047</td>
      <td>1.000000</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.520408</td>
      <td>0.454545</td>
      <td>0.103448</td>
      <td>0.967936</td>
      <td>0.637584</td>
      <td>0.363636</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.234694</td>
      <td>0.333333</td>
      <td>0.310345</td>
      <td>0.847695</td>
      <td>0.436242</td>
      <td>0.363636</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.673469</td>
      <td>1.000000</td>
      <td>0.241379</td>
      <td>0.539078</td>
      <td>0.825503</td>
      <td>0.272727</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>


- 입력 1: 판매 관련 정보: Advertising, Price, ShelveLoc, US, Urban, CompPrice
- 입력 2: 외부 환경 정보: Income, Population, Age, Education

```python
# 입력 1

in_col = ['Advertising', 'Price', 'CompPrice', 'ShelveLoc_Good', 'ShelveLoc_Medium', 'US_Yes', 'Urban_Yes']
x_train1 = x_train[in_col]
x_val1 = x_val[in_col]
# x_val1.head()
```

```python
# 입력 2
x_train2 = x_train.drop(in_col, axis=1)
x_val2 = x_val.drop(in_col, axis=1)
# x_val2.head()
```

```python
# 다중입력 모델링

nfeatures1 = x_train1.shape[1]
nfeatures2 = x_train2.shape[1]
print(nfeatures1, nfeatures2)
```

<pre>
7 11
</pre>

```python
# 모델 구성
input_1 = Input(shape=(nfeatures1,), name='input_1')
input_2 = Input(shape=(nfeatures2,), name='input_2')

# 첫번째 입력을 위한 레이어
hl1_1 = Dense(10, activation='relu')(input_1)

# 두번째 입력을 위한 레이어
hl1_2 = Dense(20, activation='relu')(input_2)

# 두 히든레이어 결합
cbl = concatenate([hl1_1, hl1_2])

# 추가 히든레이어
hl2 = Dense(8, activation='relu')(cbl)

# 출력 레이어
output = Dense(1)(hl2)

# 모델 선언
model = Model(inputs=[input_1, input_2], outputs=output)
model.summary()
```

<pre>
Model: "model_1"
__________________________________________________________________________________________________
 Layer (type)                Output Shape                 Param #   Connected to                  
==================================================================================================
 input_1 (InputLayer)        [(None, 7)]                  0         []                            
                                                                                                  
 input_2 (InputLayer)        [(None, 11)]                 0         []                            
                                                                                                  
 dense_4 (Dense)             (None, 10)                   80        ['input_1[0][0]']             
                                                                                                  
 dense_5 (Dense)             (None, 20)                   240       ['input_2[0][0]']             
                                                                                                  
 concatenate (Concatenate)   (None, 30)                   0         ['dense_4[0][0]',             
                                                                     'dense_5[0][0]']             
                                                                                                  
 dense_6 (Dense)             (None, 8)                    248       ['concatenate[0][0]']         
                                                                                                  
 dense_7 (Dense)             (None, 1)                    9         ['dense_6[0][0]']             
                                                                                                  
==================================================================================================
Total params: 577 (2.25 KB)
Trainable params: 577 (2.25 KB)
Non-trainable params: 0 (0.00 Byte)
__________________________________________________________________________________________________
</pre>

```python
# 컴파일
model.compile(optimizer=Adam(learning_rate=0.01), loss='mse')

# 학습
hist = model.fit([x_train1, x_train2], y_train, epochs=50, validation_split=.2, verbose=0).history
```

```python
dl_history_plot(hist)
```

![z_dl_8_2](https://github.com/zacinthepark/TIL/assets/86648892/26e86342-43f7-42a9-b654-2e06d5399f87)

```python
pred = model.predict([x_val1, x_val2])
print(mean_squared_error(y_val, pred, squared=False))
print(mean_absolute_error(y_val, pred))
```

<pre>
3/3 [==============================] - 0s 5ms/step
1.3350816478524405
1.106137151002884
</pre>

#### 보스턴 집값 데이터를 통한 실습

```python
path = 'https://raw.githubusercontent.com/DA4BAM/dataset/master/boston.csv'
data = pd.read_csv(path)
data.head()
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>crim</th>
      <th>zn</th>
      <th>indus</th>
      <th>chas</th>
      <th>nox</th>
      <th>rm</th>
      <th>age</th>
      <th>dis</th>
      <th>rad</th>
      <th>tax</th>
      <th>ptratio</th>
      <th>lstat</th>
      <th>medv</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.00632</td>
      <td>18.0</td>
      <td>2.31</td>
      <td>0</td>
      <td>0.538</td>
      <td>6.575</td>
      <td>65.2</td>
      <td>4.0900</td>
      <td>1</td>
      <td>296</td>
      <td>15.3</td>
      <td>4.98</td>
      <td>24.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.02731</td>
      <td>0.0</td>
      <td>7.07</td>
      <td>0</td>
      <td>0.469</td>
      <td>6.421</td>
      <td>78.9</td>
      <td>4.9671</td>
      <td>2</td>
      <td>242</td>
      <td>17.8</td>
      <td>9.14</td>
      <td>21.6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.02729</td>
      <td>0.0</td>
      <td>7.07</td>
      <td>0</td>
      <td>0.469</td>
      <td>7.185</td>
      <td>61.1</td>
      <td>4.9671</td>
      <td>2</td>
      <td>242</td>
      <td>17.8</td>
      <td>4.03</td>
      <td>34.7</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.03237</td>
      <td>0.0</td>
      <td>2.18</td>
      <td>0</td>
      <td>0.458</td>
      <td>6.998</td>
      <td>45.8</td>
      <td>6.0622</td>
      <td>3</td>
      <td>222</td>
      <td>18.7</td>
      <td>2.94</td>
      <td>33.4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.06905</td>
      <td>0.0</td>
      <td>2.18</td>
      <td>0</td>
      <td>0.458</td>
      <td>7.147</td>
      <td>54.2</td>
      <td>6.0622</td>
      <td>3</td>
      <td>222</td>
      <td>18.7</td>
      <td>5.33</td>
      <td>36.2</td>
    </tr>
  </tbody>
</table>

```python
# 전처리 수행

# 데이터 분할: x, y
target = 'medv'
x = data.drop(target, axis=1)
y = data.loc[:, target]

# 데이터 분할: train, val
x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=.2, random_state=20)

# 스케일링
scaler = MinMaxScaler()
x_train = scaler.fit_transform(x_train)
x_val = scaler.transform(x_val)

# 컬럼 이름으로 조작하기 위해 데이터프레임으로 변환
x_train = pd.DataFrame(x_train, columns=x.columns)
x_val = pd.DataFrame(x_val, columns=x.columns)
```

```python
x_train.head()
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>crim</th>
      <th>zn</th>
      <th>indus</th>
      <th>chas</th>
      <th>nox</th>
      <th>rm</th>
      <th>age</th>
      <th>dis</th>
      <th>rad</th>
      <th>tax</th>
      <th>ptratio</th>
      <th>lstat</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.001880</td>
      <td>0.125</td>
      <td>0.271628</td>
      <td>0.0</td>
      <td>0.286008</td>
      <td>0.500287</td>
      <td>0.959835</td>
      <td>0.438387</td>
      <td>0.173913</td>
      <td>0.236641</td>
      <td>0.276596</td>
      <td>0.480684</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.007265</td>
      <td>0.200</td>
      <td>0.128666</td>
      <td>0.0</td>
      <td>0.390947</td>
      <td>0.748994</td>
      <td>0.511843</td>
      <td>0.158445</td>
      <td>0.173913</td>
      <td>0.146947</td>
      <td>0.042553</td>
      <td>0.039459</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.000473</td>
      <td>0.250</td>
      <td>0.161290</td>
      <td>0.0</td>
      <td>0.084362</td>
      <td>0.606630</td>
      <td>0.315139</td>
      <td>0.388391</td>
      <td>0.130435</td>
      <td>0.179389</td>
      <td>0.680851</td>
      <td>0.098234</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.015293</td>
      <td>0.000</td>
      <td>0.281525</td>
      <td>0.0</td>
      <td>0.314815</td>
      <td>0.412340</td>
      <td>0.939238</td>
      <td>0.282207</td>
      <td>0.130435</td>
      <td>0.229008</td>
      <td>0.893617</td>
      <td>0.575883</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.091277</td>
      <td>0.000</td>
      <td>0.646628</td>
      <td>0.0</td>
      <td>0.674897</td>
      <td>0.610845</td>
      <td>0.923790</td>
      <td>0.108576</td>
      <td>1.000000</td>
      <td>0.914122</td>
      <td>0.808511</td>
      <td>0.433499</td>
    </tr>
  </tbody>
</table>

```python
# 입력 1: 주택과 직접 관련이 있는 변수들
in_col = ['zn', 'rm', 'age', 'tax']
x_train1 = x_train[in_col]
x_val1 = x_val[in_col]
# x_val1.head()
```

```python
# 입력 2: 주택과 간접 관련이 있는 변수들
x_train2 = x_train.drop(in_col, axis=1)
x_val2 = x_val.drop(in_col, axis=1)
# x_val2.head()
```

```python
# 다중입력 모델링

nfeatures1 = x_train1.shape[1]
nfeatures2 = x_train2.shape[1]
print(nfeatures1, nfeatures2)
```

<pre>
4 8
</pre>

```python
# 입력
input_1 = Input(shape=(nfeatures1,), name='input_1')
input_2 = Input(shape=(nfeatures2,), name='input_2')

# 첫번째 입력을 위한 레이어
hl1_1 = Dense(4, activation='relu')(input_1)
hl1_2 = Dense(8, activation='relu')(input_2)

# 두 히든레이어 결합
cbl = concatenate([hl1_1, hl1_2])

# 추가 히든레이어
hl2 = Dense(12, activation='relu')(cbl)
hl3 = Dense(8, activation='relu')(hl2)

# 출력 레이어
output = Dense(1)(hl3)

# 모델 선언
model = Model(inputs=[input_1, input_2], outputs=output)
model.summary()
```

<pre>
Model: "model_2"
__________________________________________________________________________________________________
 Layer (type)                Output Shape                 Param #   Connected to                  
==================================================================================================
 input_1 (InputLayer)        [(None, 4)]                  0         []                            
                                                                                                  
 input_2 (InputLayer)        [(None, 8)]                  0         []                            
                                                                                                  
 dense_8 (Dense)             (None, 4)                    20        ['input_1[0][0]']             
                                                                                                  
 dense_9 (Dense)             (None, 8)                    72        ['input_2[0][0]']             
                                                                                                  
 concatenate_1 (Concatenate  (None, 12)                   0         ['dense_8[0][0]',             
 )                                                                   'dense_9[0][0]']             
                                                                                                  
 dense_10 (Dense)            (None, 12)                   156       ['concatenate_1[0][0]']       
                                                                                                  
 dense_11 (Dense)            (None, 8)                    104       ['dense_10[0][0]']            
                                                                                                  
 dense_12 (Dense)            (None, 1)                    9         ['dense_11[0][0]']            
                                                                                                  
==================================================================================================
Total params: 361 (1.41 KB)
Trainable params: 361 (1.41 KB)
Non-trainable params: 0 (0.00 Byte)
__________________________________________________________________________________________________
</pre>

```python
# 컴파일
model.compile(optimizer=Adam(learning_rate=0.01), loss='mse')

# 학습
hist = model.fit([x_train1, x_train2], y_train, epochs=50, validation_split=.2, verbose=0).history
```

```python
dl_history_plot(hist)
```

![z_dl_8_3](https://github.com/zacinthepark/TIL/assets/86648892/7b40b693-77f3-45a2-b941-d8613c96a064)

```python
pred = model.predict([x_val1, x_val2])
print(mean_squared_error(y_val, pred, squared=False))
print(mean_absolute_error(y_val, pred))
```

<pre>
4/4 [==============================] - 0s 12ms/step
4.157787496284589
3.10843615064434
</pre>
