## streamlit 활용

---

- 파이썬의 Streamlit
    - 웹 어플리케이션 제작 가능
    - 쉽고 간단한 API 제공으로 낮은 진입 장벽
- Streamlit UI
    - 다양한 UI 구성 요소 활용 가능
    - 텍스트, 데이터프레임, 위젯, 레이아웃 등

### Streamlit

- Data Science를 위한 맞춤형 웹 어플리케이션을 만들 수 있는 파이썬의 라이브러리
- 데이터 분석 결과를 손쉽게 공유할 수 있는 라이브러리
- 간결하고 명확한 API를 제공하며, 다른 프레임워크와 비교하여 상대적으로 진입장벽이 낮음

### Streamlit UI 구성 요소

<img width="711" alt="streamlit1" src="https://github.com/zacinthepark/TIL/assets/86648892/6defff68-06cb-4408-8bc8-75cbcdcb9273">

### 실습

#### streamlit anaconda에서 실행

```
streamlit run /Users/zvc/jupyterprojects/streamlit_test/ds_app.py
```

#### 스케일러, 모델 생성 및 피클 파일로 추출

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from scipy import stats
import statsmodels.api as sm

import joblib
```

```python
# 보스턴 집값 데이터 로딩

# 데이터 로딩
data_url = 'http://lib.stat.cmu.edu/datasets/boston'
raw_df = pd.read_csv(data_url, sep=r'\s+', skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]
boston = pd.merge(pd.DataFrame(data), pd.DataFrame(target), left_index=True, right_index=True, how='inner')
boston.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 
                  'PTRATIO', 'B', 'LSTAT', 'MEDV']

# 데이터 copy
boston_data = boston.copy()
boston_data
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>CRIM</th>
      <th>ZN</th>
      <th>INDUS</th>
      <th>CHAS</th>
      <th>NOX</th>
      <th>RM</th>
      <th>AGE</th>
      <th>DIS</th>
      <th>RAD</th>
      <th>TAX</th>
      <th>PTRATIO</th>
      <th>B</th>
      <th>LSTAT</th>
      <th>MEDV</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.00632</td>
      <td>18.0</td>
      <td>2.31</td>
      <td>0.0</td>
      <td>0.538</td>
      <td>6.575</td>
      <td>65.2</td>
      <td>4.0900</td>
      <td>1.0</td>
      <td>296.0</td>
      <td>15.3</td>
      <td>396.90</td>
      <td>4.98</td>
      <td>24.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.02731</td>
      <td>0.0</td>
      <td>7.07</td>
      <td>0.0</td>
      <td>0.469</td>
      <td>6.421</td>
      <td>78.9</td>
      <td>4.9671</td>
      <td>2.0</td>
      <td>242.0</td>
      <td>17.8</td>
      <td>396.90</td>
      <td>9.14</td>
      <td>21.6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.02729</td>
      <td>0.0</td>
      <td>7.07</td>
      <td>0.0</td>
      <td>0.469</td>
      <td>7.185</td>
      <td>61.1</td>
      <td>4.9671</td>
      <td>2.0</td>
      <td>242.0</td>
      <td>17.8</td>
      <td>392.83</td>
      <td>4.03</td>
      <td>34.7</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.03237</td>
      <td>0.0</td>
      <td>2.18</td>
      <td>0.0</td>
      <td>0.458</td>
      <td>6.998</td>
      <td>45.8</td>
      <td>6.0622</td>
      <td>3.0</td>
      <td>222.0</td>
      <td>18.7</td>
      <td>394.63</td>
      <td>2.94</td>
      <td>33.4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.06905</td>
      <td>0.0</td>
      <td>2.18</td>
      <td>0.0</td>
      <td>0.458</td>
      <td>7.147</td>
      <td>54.2</td>
      <td>6.0622</td>
      <td>3.0</td>
      <td>222.0</td>
      <td>18.7</td>
      <td>396.90</td>
      <td>5.33</td>
      <td>36.2</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>501</th>
      <td>0.06263</td>
      <td>0.0</td>
      <td>11.93</td>
      <td>0.0</td>
      <td>0.573</td>
      <td>6.593</td>
      <td>69.1</td>
      <td>2.4786</td>
      <td>1.0</td>
      <td>273.0</td>
      <td>21.0</td>
      <td>391.99</td>
      <td>9.67</td>
      <td>22.4</td>
    </tr>
    <tr>
      <th>502</th>
      <td>0.04527</td>
      <td>0.0</td>
      <td>11.93</td>
      <td>0.0</td>
      <td>0.573</td>
      <td>6.120</td>
      <td>76.7</td>
      <td>2.2875</td>
      <td>1.0</td>
      <td>273.0</td>
      <td>21.0</td>
      <td>396.90</td>
      <td>9.08</td>
      <td>20.6</td>
    </tr>
    <tr>
      <th>503</th>
      <td>0.06076</td>
      <td>0.0</td>
      <td>11.93</td>
      <td>0.0</td>
      <td>0.573</td>
      <td>6.976</td>
      <td>91.0</td>
      <td>2.1675</td>
      <td>1.0</td>
      <td>273.0</td>
      <td>21.0</td>
      <td>396.90</td>
      <td>5.64</td>
      <td>23.9</td>
    </tr>
    <tr>
      <th>504</th>
      <td>0.10959</td>
      <td>0.0</td>
      <td>11.93</td>
      <td>0.0</td>
      <td>0.573</td>
      <td>6.794</td>
      <td>89.3</td>
      <td>2.3889</td>
      <td>1.0</td>
      <td>273.0</td>
      <td>21.0</td>
      <td>393.45</td>
      <td>6.48</td>
      <td>22.0</td>
    </tr>
    <tr>
      <th>505</th>
      <td>0.04741</td>
      <td>0.0</td>
      <td>11.93</td>
      <td>0.0</td>
      <td>0.573</td>
      <td>6.030</td>
      <td>80.8</td>
      <td>2.5050</td>
      <td>1.0</td>
      <td>273.0</td>
      <td>21.0</td>
      <td>396.90</td>
      <td>7.88</td>
      <td>11.9</td>
    </tr>
  </tbody>
</table>
<p>506 rows × 14 columns</p>
</div>

```python
# 스케일러 생성 및 추출

# MinMaxScaler
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X = boston_data[['RM', 'LSTAT', 'INDUS', 'AGE', 'CHAS']]
scaler.fit(X)

# joblib을 통해 피클 파일로 추출
joblib.dump(scaler, 'scaler_X.pkl')
```

<pre>
['scaler_X.pkl']
</pre>

```python
# 종속변수 (타겟 y: 주택가격) <-- 독립변수 X: 방 개수, 하위계층 비율, 주거지역 토지 비율, 오래된 주택 비율, 찰스강 경계 위치 여부 기반 예측
y = boston_data['MEDV'].values
lr = sm.OLS(y, X)
model = lr.fit()
```

```python
model.summary()
```

<table class="simpletable">
<caption>OLS Regression Results</caption>
<tr>
  <th>Dep. Variable:</th>            <td>y</td>        <th>  R-squared (uncentered):</th>      <td>   0.951</td>
</tr>
<tr>
  <th>Model:</th>                   <td>OLS</td>       <th>  Adj. R-squared (uncentered):</th> <td>   0.950</td>
</tr>
<tr>
  <th>Method:</th>             <td>Least Squares</td>  <th>  F-statistic:       </th>          <td>   1938.</td>
</tr>
<tr>
  <th>Date:</th>             <td>Wed, 21 Feb 2024</td> <th>  Prob (F-statistic):</th>           <td>  0.00</td> 
</tr>
<tr>
  <th>Time:</th>                 <td>15:17:23</td>     <th>  Log-Likelihood:    </th>          <td> -1570.8</td>
</tr>
<tr>
  <th>No. Observations:</th>      <td>   506</td>      <th>  AIC:               </th>          <td>   3152.</td>
</tr>
<tr>
  <th>Df Residuals:</th>          <td>   501</td>      <th>  BIC:               </th>          <td>   3173.</td>
</tr>
<tr>
  <th>Df Model:</th>              <td>     5</td>      <th>                     </th>              <td> </td>   
</tr>
<tr>
  <th>Covariance Type:</th>      <td>nonrobust</td>    <th>                     </th>              <td> </td>   
</tr>
</table>
<table class="simpletable">
<tr>
    <td></td>       <th>coef</th>     <th>std err</th>      <th>t</th>      <th>P>|t|</th>  <th>[0.025</th>    <th>0.975]</th>  
</tr>
<tr>
  <th>RM</th>    <td>    4.8224</td> <td>    0.092</td> <td>   52.460</td> <td> 0.000</td> <td>    4.642</td> <td>    5.003</td>
</tr>
<tr>
  <th>LSTAT</th> <td>   -0.6198</td> <td>    0.045</td> <td>  -13.705</td> <td> 0.000</td> <td>   -0.709</td> <td>   -0.531</td>
</tr>
<tr>
  <th>INDUS</th> <td>   -0.1161</td> <td>    0.049</td> <td>   -2.353</td> <td> 0.019</td> <td>   -0.213</td> <td>   -0.019</td>
</tr>
<tr>
  <th>AGE</th>   <td>    0.0156</td> <td>    0.012</td> <td>    1.263</td> <td> 0.207</td> <td>   -0.009</td> <td>    0.040</td>
</tr>
<tr>
  <th>CHAS</th>  <td>    4.2390</td> <td>    0.964</td> <td>    4.396</td> <td> 0.000</td> <td>    2.344</td> <td>    6.134</td>
</tr>
</table>
<table class="simpletable">
<tr>
  <th>Omnibus:</th>       <td>141.809</td> <th>  Durbin-Watson:     </th> <td>   0.932</td> 
</tr>
<tr>
  <th>Prob(Omnibus):</th> <td> 0.000</td>  <th>  Jarque-Bera (JB):  </th> <td> 460.807</td> 
</tr>
<tr>
  <th>Skew:</th>          <td> 1.292</td>  <th>  Prob(JB):          </th> <td>8.65e-101</td>
</tr>
<tr>
  <th>Kurtosis:</th>      <td> 6.896</td>  <th>  Cond. No.          </th> <td>    306.</td> 
</tr>
</table><br/><br/>Notes:<br/>[1] R² is computed without centering (uncentered) since the model does not contain a constant.<br/>[2] Standard Errors assume that the covariance matrix of the errors is correctly specified.

```python
new_data = np.array([3.00, 30.00, 20.00, 23.00, 1])
new_data = new_data.reshape(1, 5)
new_data = scaler.transform(new_data)
y_pred = model.predict(new_data)
y_pred_new = y_pred * 10000
y_pred_new_round = round(y_pred_new[0], 3)
print(f'주택가격 예측: {y_pred_new_round}')
```

<pre>
주택가격 예측: 31571.89
</pre>

```python
# 모델 추출
joblib.dump(model, 'reg_model_boston.pkl')
```

<pre>
['reg_model_boston.pkl']
</pre>

#### `ds_app.py`

```python
import streamlit as st
import joblib
import numpy as np
import seaborn as sns

from PIL import Image
import pandas as pd

import os

import warnings
warnings.filterwarnings('ignore')

# 경로 설정해둠으로써 향후 상대경로로 편하게 이동 가능
os.chdir('/Users/zvc/jupyterprojects/streamlit_test')

img = Image.open('./bicycle_logo.jpg')
# 세로로 3 영역으로 나누고, 가운데 영역에 이미지 로드
col1, col2, col3 = st.columns(3)
with col2:
    st.image(img)

# 타이틀
st.title('Streamliiiiiittttttttttt')

# 데이터 로딩
loading_process = st.text('Boston Housing Data Loading...')
boston = pd.read_csv('./boston.csv')
loading_process.success('Boston Housing Data Loaded! :house:')

# 데이터프레임 확인
# checkbox 위젯
if st.checkbox('원본 데이터 확인'):
    nrows = st.slider('총 %s개의 데이터 중 몇 개를 보여줄까요?' % boston.shape[0])
    st.subheader('보스턴 집값 원본 데이터')
    st.dataframe(boston[:nrows])    # streamlit이 제공하는 dataframe (interactive 기능 제공)

# 변수 시각화
st.header('변수의 단변량 & 다변량 시각화')

# selectbox 위젯
plot_list = ['집값 / 방 개수', '집값 / 방 개수 / 빈곤층 비율']
choice = st.selectbox('원하는 변수의 조합을 선택하세요', plot_list)

if choice == plot_list[0]:
    fig = sns.pairplot(boston[['MEDV', 'RM']])
else:
    fig = sns.pairplot((boston[['MEDV', 'RM', 'LSTAT']]))

st.pyplot(fig)  # figure 출력

# 주택가격 예측 모델
st.header('주택가격 금액 예측')

# Loading the model

# 피클 (pkl) 파일은 파이썬이 기본적으로 지원하는 객체 저장 모듈이다.
# 파이썬에서 사용하는 모든 객체를 저장할 수 있으며, 인공지능 분야에서는 주로 가중치 등의 파라미터 값이나 학습시킨 모델을 저장할 때 사용한다.

# The pickle module implements binary protocols for serializing and de-serializing a Python object structure.
# “Pickling” is the process whereby a Python object hierarchy is converted into a byte stream.
# “Unpickling” is the inverse operation whereby a byte stream (from a binary file or bytes-like object) is converted back into an object hierarchy.

model = joblib.load('./reg_model_boston.pkl')
scaler = joblib.load('./scaler_X.pkl')

st.markdown('*아래의 회귀식으로부터 예측 진행*')
# 라텍스는 raw string을 이용 -> 백슬래시(\) 사용을 위함
st.latex(r'''Y=\alpha + \gamma_1 (\text{찰스강}) + \beta_1 (\text{오래된 주택 비율}) + \beta_2 (\text{방 개수}) + 
                \beta_3 (\text{하위계층 비율}) + \beta_4 (\text{주거지역 비율}) + \epsilon''')

chas_list = ['위치', '위치안함']
CHAS = st.radio('찰스강 경계 위치 여부 입력', chas_list)
if CHAS == '위치':
    CHAS = 1
else:
    CHAS = 0

AGE = st.number_input('오래된 주택 비율 입력 (0 ~ 100사이의 값 입력)', min_value=0.00, max_value=100.00, step=1.00)
RM = st.number_input('평균 방의 개수 입력 (단위: 개)', min_value=0.00, max_value=100.00, step=1.00)
LSTAT = st.number_input('하위계층 비율 입력 (0 ~ 100사이의 값 입력)', min_value=0.00, max_value=100.00, step=1.00)
INDUS = st.number_input('주거지역 토지 비율 입력 (0 ~ 100사이의 값 입력)', min_value=0.00, max_value=100.00, step=1.00)

if st.button('Town 주택 가격 예측'):
    new_data = np.array([RM, LSTAT, INDUS, AGE, CHAS])
    new_data = new_data.reshape(1, 5)
    new_data = scaler.transform(new_data)
    y_pred = model.predict(new_data)
    y_pred_new = y_pred * 10000
    y_pred_new_round = round(y_pred_new[0], 3)

    st.success('이 town의 예측된 주택 가격은 ' + str(y_pred_new_round) + '달러 입니다. :house:')
```

#### 결과물

<img width="935" alt="st_test_1" src="https://github.com/zacinthepark/TIL/assets/86648892/128a9067-c994-434f-9e81-087691bd1cd7">

<img width="949" alt="st_test_2" src="https://github.com/zacinthepark/TIL/assets/86648892/97c9454a-b899-40bf-a1bc-7a2bbc9c5a7e">

<img width="946" alt="st_test_3" src="https://github.com/zacinthepark/TIL/assets/86648892/c6790617-1aba-4bfa-b07d-dd96897a0ec8">

<img width="993" alt="st_test_4" src="https://github.com/zacinthepark/TIL/assets/86648892/df55731d-3a2a-49e0-90db-0cf56dd256a6">
