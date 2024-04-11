## 딥러닝 시계열 모델링: SimpleRNN, LSTM

---

### Sequential Data

<p align="center">
    <img width="500" alt="sequential_data" src="https://github.com/zacinthepark/TIL/assets/86648892/27cb2ef8-f50f-4aff-871a-46194667b2ca">
</p>

- Sequential Data: 데이터의 분석단위끼리 순서가 있다

- Time Series: Sequential Data + 시간의 등간격

### 시계열 데이터 분석

<p align="center">
    <img width="500" alt="sd_analysis" src="https://github.com/zacinthepark/TIL/assets/86648892/be47379a-c069-44ab-a638-838dab29b838">
</p>

- **시간의 흐름에 따른 패턴** 을 분석하는 것

- 흐름을 어떻게 정리할 것인지에 따라 모델링 방식이 달라진다
    - 통계적 시계열 모델링
    - ML 기반 시계열 모델링
    - DL 기반 시계열 모델링

#### 통계적 시계열 모델링

> $y$의 이전 시점 데이터들로부터 흐름의 패턴을 추출하여 예측

<p align="center">
    <img width="500" alt="z_stat_modeling" src="https://github.com/zacinthepark/TIL/assets/86648892/46cb9b03-b4ff-443f-9f1d-86d455d901dd">
</p>

- $y$의 흐름을 분석하는 것으로, $x$ 변수들은 사용하지 않음

- 패턴
    - Trend(추세), Seasonality(계절성) 등

- 모델 구조 예시
    - $y_t = w_1 y_{t-1} + w_2 y_{t-2} + w_3 y_{t-3} + w_0$

- 패턴이 충분히 도출된 모델의 잔차는 Stationary

- ARIMA

> Stationary(정상): 시간이나 위치에 따라 통계적 성질이 변하지 않는 것. 시간 기준이 바뀌어도 그 통계적 성질은 변하지 않는다.

#### ML 기반 시계열 모델링

> 특정 **시점** 데이터들(**1차원**)과 예측대상시점($y_{t+1}$)과의 관계로부터 패턴을 추출하여 예측

<p align="center">
    <img width="500" alt="z_ml_modeling" src="https://github.com/zacinthepark/TIL/assets/86648892/caf76d92-5fc6-4e0e-8416-57d926c25890">
</p>

- Feature Engineering을 통해 시간의 흐름을 $x$ 변수로 도출하는 것이 중요

- 모델 구조 예시
    - $y_{t+1} = w_1 x1_t + w_2 x2_t + w_3 x3_t + w_4 y_t + w_0$

#### DL 기반 시계열 모델링

> **시간흐름 구간(timesteps)** 데이터들(**2차원**)과 예측대상시점($y_{t+1}$과의 관계로부터 패턴을 추출하여 예측)

<p align="center">
    <img width="500" alt="z_dl_modeling" src="https://github.com/zacinthepark/TIL/assets/86648892/5cc09989-e9f7-4953-b11b-49da52b2c18c">
</p>

- 어느정도의 구간(timesteps)을 유의미한 하나의 단위로 정할 것인가를 고려

- 시간흐름 구간(timesteps) 데이터들(2차원)이 분석 단위이므로 데이터셋은 3차원
    - 분석 단위를 2차원으로 만드는 전처리 필요

### 시계열 모델링 절차

#### 시계열 모델링의 일반적인 절차

1. $y$ 시각화 및 정상성 검토

2. 모델 생성

3. train_err(잔차) 분석 &rarr; 분석 후 필요 시 2번으로 돌아감

4. 검증(예측)

5. 검증(평가) &rarr; 검증 후 필요 시 2번으로 돌아감

#### 시계열 모델 평가

다음의 항목으로 모델을 평가합니다.

- 기술적 평가
    - 잔차 분석
        - ACF, PACF
        - 정상성 검정, 정규성 검정 등
    - ML Metric
        - AIC
        - MAE, MAPE, R2
    
- 비즈니스적 평가
    - 수요량 예측
        - 재고 회전율
        - 평균 재고비용

#### 잔차 분석

- `실제 = 모델 + 오차`

- `잔차(Residuals) = 실제데이터 - 예측값`

- 시계열 모델 $y = f(x) + \epsilon$
    - 모델이 잘 만들어졌다면
        - 잔차 $\epsilon$은 White Noise에 가까워야함
        - 즉, 잔차에는 어떠한 패턴이 없었으면 좋겠다는 것
        - 만약 잔차 $\epsilon$이 White Noise에 가깝지 않다면 $f(x)$는 아직 $y$의 패턴을 제대로 반영하지 않은 것 &rarr; 더 해야할 일이 남아있다는 것

- 잔차 분석
    - 시각화
        - ACF, PACF
    - 검정
        - 정상성 검정(ADF Test, KPSS Test)
        - 정규성 검정(Shapiro-wilk Test)
        - 자기상관 검정(Ljung-Box Test)
        - 등분산성 검정(G-Q Test)

---

### 딥러닝 기반 시계열 모델링 (RNN)

> 1: 데이터 전처리<br>
<br>
1-1: 데이터 분할: x, y<br>
<br>
1-2: 스케일링<br>
x의 스케일링은 필수 (여러 독립변수를 기준으로 분석하기에 독립변수 간 범위를 맞춰야함)<br>
y값이 크다면 최적화를 위해 스케일링 필요 (단, 모델 평가 시 원래 값으로 복원)<br>
<br>
1-3: timesteps를 바탕으로 3차원 데이터셋 구성 (sliding window)<br>
timesteps를 지정할 떄 유의미한 분석 단위가 무엇일지 생각해보고 지정<br>
<br>
1-4: train, validation 분할

> 2: input_shape 지정

> 3: 모델링

#### RNN (Recurrent Neural Networks)

<p align="center">
    <img width="500" alt="rnn_what_time_is_it" src="https://github.com/zacinthepark/TIL/assets/86648892/2a85e1ae-92a5-4278-84f0-56592e924f4b">
</p>

- 이전 timestep의 값이 다음 timestep의 값에 영향을 미침
- 오래된 값일수록 영향이 줄어듬
- 2차원 데이터가 input으로 들어가면 노드 하나에서 나오는 값은 스칼라 값

#### RNN으로 시계열 모델링하기

> 최근 4일 간의 주가, 거래량, 환율, 유가의 흐름을 학습해서 다음날 주가를 예측하는 모델

<p align="center">
    <img width="650" alt="rnn_stock_data" src="https://github.com/zacinthepark/TIL/assets/86648892/411f2532-e46a-4b08-ac41-d31928c9afb2">
</p>

<p align="center">
    <img width="650" alt="rnn_sequential_modeling_1" src="https://github.com/zacinthepark/TIL/assets/86648892/ad7b84b0-119f-467c-a3c0-43959e08652e">
</p>

- 최근 4일간 데이터($x0$, $x1$, $x2$, $x3$)를 기반으로 다음날 주가 예측($y$)을 할 때
    - $x0$, $x1$, $x2$, $x3$: input
    - $h0$, $h1$, $h2$, $h3$: hidden state (중간 결과물)

<p align="center">
    <img width="650" alt="rnn_sequential_modeling_2" src="https://github.com/zacinthepark/TIL/assets/86648892/ce1fc4f8-04a5-4cd6-80ba-c61077537b13">
</p>

- **과거의 정보를 현재에 반영**해 학습하도록 설계
    - 최근 4일간 데이터: input data (4x4)
        - n: timesteps, 4
        - m: nfeatures, 4
    - $h0$: $x0$ 을 바탕으로 $y$ 예측
        - $x0$ input vector(nfeatures x 1) 바탕으로 예측
    - $h1$: $h0$ + $x1$ 바탕으로 $y$ 예측
        - $x1$ input vector(`nfeatures x 1`) + $h0$ hidden layer vector(`timesteps x 1`) 바탕으로 예측
    - $h2$: $h1$ + $x2$ 바탕으로 $y$ 예측
        - $x2$ input vector(`nfeatures x 1`) + $h1$ hidden layer vector(`timesteps x 1`) 바탕으로 예측
    - $h3$: $h2$ + $x3$ 바탕으로 $y$ 예측
        - $x3$ input vector(`nfeatures x 1`) + $h2$ hidden layer vector(`timesteps x 1`) 바탕으로 예측

- `timesteps x 1`: output layer에서 각 timestep마다 도출한 특징 값들($h0$, $h1$, $h2$, $h3$)을 모은 결과를 반환 (hidden layer에서도 전체적인 구조가 유지된다고 생각)

#### 3차원 데이터셋 구성

<p align="center">
    <img width="500" alt="3_dimensional_data_1" src="https://github.com/zacinthepark/TIL/assets/86648892/e2b76206-9066-47dd-95c6-9dd57006e68a">
</p>

<p align="center">
    <img width="500" alt="3_dimensional_data_2" src="https://github.com/zacinthepark/TIL/assets/86648892/83d9acf1-b759-486c-9360-dc4d46c7ef45">
</p>

- timesteps 단위로 잘라서 2차원 분석 단위를 구성
    - 행: 시간간격(timesteps), 열: nfeatures
    - 어떤 간격이 적절한 것인지 결정하는 것이 중요
- sliding window 방식으로 3차원 데이터셋 단위를 구성

#### SimpleRNN and Return Sequences

- 각 timestep마다 특징 값 하나씩 도출하여 노드 1개씩에 사용 가능

- timesteps가 4개라면, 4행 1열의 특징이 만들어짐

- `return_sequences`
    - 다음 레이어로 특징 값(hidden state)를 어떻게 넘길지 결정
    - `True`: 출력 크기 그대로 전달: `timesteps * node 개수`
    - `False`: 가장 마지막(최근) hidden state 값만 전달: `1 * node 개수`
    - `SimpleRNN`의 `return_sequences` 옵션은 default가 `False`

- 마지막 RNN Layer가 아니라면, 다음 RNN Layer로 출력값을 넘길 때, 다음 RNN Layer가 timesteps 단위에 맞게 입력을 받아야 하므로, `return_sequences=True`가 되어야함
    - 쉽게 말해서, RNN Layer는 Sequential Data를 input으로 받아야함
    - ($h0$, $h1$, $h2$, $h3$)는 Sequential Data, $h3$ 단독은 Sequential Data가 아님

- 마지막 RNN Layer인 경우 `False`, `True` 모두 가능
    - **단, `True`를 사용하려면 `Flatten`으로 펼친 후 Dense Layer로 연결**

```python
model = Sequential([SimpleRNN(1, input_shape=(timesteps, nfeatures), return_sequences=True), # 1
                    SimpleRNN(1, return_sequences=False),                                    # 2
                    Dense(1)])
```

<p align="center">
    <img width="650" alt="simple_rnn_return_sequences" src="https://github.com/zacinthepark/TIL/assets/86648892/9a6f2c13-a3d9-4b3c-9a78-a1bc4d547714">
</p>

<p align="center">
    <img width="650" alt="rnn_return_sequences" src="https://github.com/zacinthepark/TIL/assets/86648892/f7512cfc-5a53-4a31-95a0-e58635032cff">
</p>

```python
# 중간 과정의 hidden state를 모두 이용
# Flatten으로 펼치기: 중간 과정의 hidden state 값들(2차원 구조)을 1차원으로 펼치기
# Dense Layer로 연결

model = Sequential([SimpleRNN(16, input_shape=(timesteps, nfeatures), return_sequences=True), 
                    SimpleRNN(8, return_sequences=True), 
                    Flatten(), 
                    Dense(8, activation='relu'), 
                    Dense(1)])
```

#### tanh





---

### 시계열 LSTM

- timestep 간에 두 종류(Cell State, Hidden State)의 상태값 업데이트 관리
- RNN은 timesteps가 길면, 초창기 기억이 사라지게 되어있음
- Cell State: 장기 기억을 오래 유지하기 위한 메모리
- 오차를 줄이는 방향으로 가중치를 업데이트 (Forget Gate, Input Gate)
