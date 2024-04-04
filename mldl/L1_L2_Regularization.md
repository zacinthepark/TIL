## 가중치 규제 (L1, L2 Regularization)

---

### 최적화와 과적합

- 최적화란, 특정 집합에 대한 목적 함수(Objective Function)를 최소화 혹은 최대화시키는 최적해(파라미터)를 찾는 것
- 머신러닝, 딥러닝 알고리즘은 모두 어떤 현상을 가장 잘 설명하기 위한 모델 함수를 찾는 방법
- 학습 기반의 머신러닝 및 딥러닝 알고리즘은 모델 성능을 높이기 위해 **손실 함수를 최소화할 수 있는 방향** 으로 학습을 진행
    - 즉, 손실 함수의 최적화 문제

> 모델 복잡에 따른 분산과 편향 관계
<p align="center">
    <img width="800" alt="underfitting_overfitting" src="https://github.com/zacinthepark/TIL/assets/86648892/15d5bd1f-d130-4e2c-9c1d-52de02b75add"
</p>

- 모델을 만들 때, 한정된 일부 데이터만을 학습 데이터로 사용
- **학습 데이터에만 존재하는 특징(노이즈)들이 과하게 모델에 반영** 되어 손실 함수가 필요 이상으로 작아지게 되는 경우 발생
    - 이를 과적합(Overfitting)이라 칭함
    - 오버피팅 발생 시 train data만 잘 설명하고 데이터의 일반적인 특징을 반영하지 못해 좋은 모델이 아님

<p align="center">
    <img width="800" alt="underfit_optimal_overfit" src="https://github.com/zacinthepark/TIL/assets/86648892/a4bd8a49-a2fe-4d21-b1b9-a068ad86714a"
</p>

- 오버피팅 문제 해결 방안
    - train data 양 늘리기
    - 배치 정규화(Batch Normalization)
    - 모델의 복잡도 줄이기
    - Dropout
    - **가중치 규제(Weight Regularization)**

- 가중치 규제란, **모델의 손실 함수값이 너무 작아지지 않도록 특정한 값(함수)를 추가** 하는 방법
- 이를 통해 **weight 값이 과도하게 커져서 일부 특징에 의존하는 현상을 방지** 하고 **데이터의 일반적인 특징(일반화, Generalization)을 잘 반영** 할 수 있도록 해줌
- 가중치 규제에는 **L1 규제(L1 Regularization, Lasso)**, **L2 규제(L2 Regularization, Ridge)** 가 있음

### L1, L2 Norm and Loss

<p align="center">
    <img width="450" height="132" alt="l1_norm" src="https://github.com/zacinthepark/TIL/assets/86648892/d38d8807-5146-4d7f-ab42-0758d0d3365d">
    <img width="450" height="132" alt="l2_norm" src="https://github.com/zacinthepark/TIL/assets/86648892/d9c32c5b-a3c8-42f5-bb97-fe3a6f21d9e9">
</p>

- Norm: 벡터 공간에서 벡터의 크기(Magnitude) 혹은 벡터 간 거리를 나타냄

- L1 Norm(Manhattan Distance): 서로 다른 두 벡터를 나타내는 각 원소들의 차이의 절댓값의 합
- L2 Norm(Euclidean Distance): 서로 다른 두 벡터 사이의 직선 거리

- L1 Loss: 실제값과 예측값 사이의 오차의 절대값 합
- L2 Loss: 실제값과 예측값 사이의 오차 제곱의 합

- L2 Loss는 오차의 제곱 합을 더해나가기 때문에 Outlier(이상치)에 더욱 민감하게 반응하며, 따라서 L1 Loss가 L2 Loss에 비해 이상치에 조금 더 둔감(robust)하다고 할 수 있고, 그렇기에 이상치가 중요한 상황이라면 L2 Loss를 쓰는 것이 좋음

### L1 Regularization(Lasso), L2 Regularization(Ridge)

Regularization은 학습 기반의 알고리즘에서 모델이 과적합되지 않도록 손실 함수에 특정한 규제 함수를 더하여 손실 함수가 너무 작아지지 않도록 weight에 페널티를 주는 기법으로, L1 규제와 L2 규제를 더한 모델의 Cost Function은 다음과 같다.

<p align="center">
    <img width="470" alt="l1_regularization" src="https://github.com/zacinthepark/TIL/assets/86648892/181db0b7-4950-4080-adcb-cf5b745ce72f">
</p>

<p align="center">
    <img width="470" alt="l2_regularization" src="https://github.com/zacinthepark/TIL/assets/86648892/a64c2394-df8c-473d-91cd-0ab0084166f4">
</p>

#### L1 Regularization

- 오차함수 = 오차 + $\lambda * \sum |w|$

- 가중치 절대값의 합을 최소화
    - 가중치가 작은 값들은 0으로 만드는 경향
    - Feature Selection

- 효과
    - 가중치 값을 0으로 만듬
    - 중요한 특징을 선택하는 효과
    - 모델에 Sparsity를 가함

$$\Large
w_{\text{new}} = w - \eta \frac{df(w)}{dw} - \frac{\eta \lambda}{n}{sgn(w)}
$$

- $\lambda$: 규제 강도

- $\eta$: 학습률

- $sgn(w)$: sign function, 절대값 함수의 도함수

- $w - \eta \frac{df(w)}{dw}$: 기존 경사하강법에 의해 가중치 갱신

- $- \frac{\eta \lambda}{n}{sgn(w)}$: Lasso Penalty

> sign function
<p align="center">
    <img width="250" alt="sign_function" src="https://github.com/zacinthepark/TIL/assets/86648892/3c16c90d-1178-40b8-a3e4-81c57ac54528">
</p>

- 양수의 가중치라면 ($w>0$), $sgn(w)$ 값은 `1`일 것이고 $-\frac{\eta \lambda}{n}{sgn(w)}$에 의해 갱신 시 규제 강도($\lambda$) 값만큼 빼줌
- 음수의 가중치라면 ($w<0$), $sgn(w)$ 값은 `-1`일 것이고 $-\frac{\eta \lambda}{n}{sgn(w)}$에 의해 갱신 시 규제 강도($\lambda$) 값만큼 더해줌
- 결국, 공평하게 규제 강도($\lambda$) 값이 모든 항에 대해 빠지면서, **자잘한 가중치들은 0이 되고, 중요한 가중치들만 남아서 feature 수가 줄어들고, 모델은 sparse해짐**

#### L2 Regularization

- 오차함수 = 오차 + $\lambda * \sum w^2$

- 가중치 제곱의 합을 최소화
    - 규제 강도에 따라 가중치 영향력을 제어
    - 강도가 크면, 큰 가중치가 좀 더 줄어드는 효과, 작은 가중치는 0에 수렴
    - Weight Decay

- 효과
    - 큰 가중치의 값을 작게 만듬
    - 모델 전반적인 복잡도를 감소시키는 효과
    - 가중치의 값이 0이 되게 하지는 못함

$$\Large
w_{\text{new}} = w - \eta \frac{df(w)}{dw} - \frac{\eta \lambda}{n}{w} = (1 - \frac{\eta \lambda}{n}){w} - \eta \frac{df(w)}{dw}
$$

- $\lambda$: 규제 강도

- $\eta$: 학습률

- $w$: 제곱 함수의 도함수

- $w - \eta \frac{df(w)}{dw}$: 기존 경사하강법에 의해 가중치 갱신

- $- \frac{\eta \lambda}{n}{w}$: Ridge Penalty

> identity function
<p align="center">
    <img width="250" alt="identity_function" src="https://github.com/zacinthepark/TIL/assets/86648892/80fe0ee4-3546-4e04-9e62-d01553d2db0b">
</p>

- 큰 가중치일수록 $- \frac{\eta \lambda}{n}{w}$에 의해 더 많이 감쇠함

#### L1, L2 규제에 의한 가중치 변화 예시

<p align="center">
    <img width="500" alt="weight_regularized" src="https://github.com/zacinthepark/TIL/assets/86648892/e458ff4c-1f29-4548-afcf-2366d8b40505">
<p/>

#### L1, L2 Regularization과 Loss Function의 관계

> L1, L2 규제에 의한 Loss Function의 최적해 위치

<p align="center">
    <img width="500" alt="l1_l2" src="https://github.com/zacinthepark/TIL/assets/86648892/f615c853-9b97-4bf6-a6a2-24886dc2e658">
<p/>

- Loss Function의 Space에서 L1, L2의 규제 영역을 두어, **실제 최적값에 대한 bias에 손해를 보더라도 variance를 낮춰 Overfitting 발생을 낮추는 것**

- L1, L2 Loss에서 $\lambda$ 값이 커질수록 **위의 규제 영역 크기가 작아지게** 되어 **bias는 더 커지고 variance는 줄어들게** (Underfitting 가능성이 커짐) 되며, L1, L2 Regularization을 추가한 Loss Function의 **최적값은 규제 영역 내에서 Global Optimum과 제일 가까운 지점** 이라고 볼 수 있음

- L1과 L2 Regularization을 모두 사용하는 것을 **Elastic Net** 이라고 부름
