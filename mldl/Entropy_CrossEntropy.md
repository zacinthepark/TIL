## Entropy, Cross Entropy

---

### 정보량과 불확실성의 관계

- 어떤 일이 일어날 확률이 높다면, 그 일이 일어나는 것은 확실
- 어떤 일이 일어날 확률이 낮다면, 그 일이 일어나는 것은 불확실
- 확률이 낮은데, 확실하다가 말하는 정보가 있다면, 그 정보의 가치는 큼
- 즉, 정보는 확률에 반비례함: $\frac{1}{p(x)}$
- 정보를 양으로 수치화 하면
    - 정보량 = $\log{\frac{1}{p(x)}}$ = $-\log{p(x)}$

<p align="center">
    <img src="https://github.com/zacinthepark/TIL/assets/86648892/2b7142d1-45bb-48cf-be4e-49d33ed8c34a" width=250>
    <img src="https://github.com/zacinthepark/TIL/assets/86648892/278ed3ee-ab9d-40cf-b7e5-a19b8eeb57f1" width=250>
</p>

- $log{x}$
    - 곱셈을 덧셈으로 바꿔준다
    - $x$가 0에 가까울수록 $-\infty$, 1일 때 0, 그리고 1 이상일 때 단조증가하는 성격을 가지고 있다
    - $-log{x}$는 $x$가 1에 가까울수록 값을 0에 가깝게, $x$가 0에 가까울수록 커지게 만들 수 있음

- 0 ~ 1 사이의 확률값에 대해 $-\log{p(x)}$ 를 적용하여 $\infty
$ ~ 0 값으로 변환
    - 정보량이 크다(확률이 적다): $\infty$
    - 정보량이 적다(확률이 크다): 0

- `정보량이 크다 = 일어날 확률이 적다 = 불확실성이 크다`

### 평균 정보량 = 엔트로피

$$\Large
{H(x) = \sum_{i=1}^{n} p(x_i)(-\log{p(x_i)}})
$$

<p align="center">
    <img width=700 alt="entropy" src="https://github.com/zacinthepark/TIL/assets/86648892/abd888c5-17d6-41c5-9015-a80e74eab80a">
</p>

- case 1은 불확실성 낮음, case 2는 불확실성 높음
- 평균 정보량은 각각의 정보량에 대해 가중치를 곱하여 정보량, 혹은 불순도를 측정함
- 얼마나 불확실한가?
    - `가중치 * 검은 공 정보량 + 가중치 * 빨간 공 정보량`
    - case 1: `-(0.9 * log0.9 + 0.1 * log0.1) = 0.325`
    - case 2: `-(0.5 * log0.5 + 0.5 * log0.5) = 0.693`

- 이 값을 **엔트로피 불순도(Impurity)** 라고 부름
    - Decision Tree에서는
    - 전체적으로 이 값을 떨어뜨려 가는 것이 모델링의 목표
    - 그래서 split 시 불순도를 가장 많이 떨어뜨려주는 변수와 값으로 기준을 결정함
    - 부모의 불순도에서 자식의 불순도를 뺀 것이 **Information Gain(정보 이득)** 이다

### 분류 모델과 cross entropy loss function

<p align="center">
    <img width=700 alt="log_loss" src="https://github.com/zacinthepark/TIL/assets/86648892/b6117acf-c146-43d2-a98f-78ce67cd1831">
</p>

$$\Large
{-\frac{1}{n} \sum y \log{\hat{y}} + (1 - y) \log{(1 - \hat{y})}}
$$

- 예측값과 실제값에 대한 오차 계산?
    - ${y}$가 1이라면
        - $\hat{y}$이 1에 가까울수록 오차가 0에 가깝고
        - $\hat{y}$이 0에 가까울수록 오차가 $\infty$에 가깝게 만들기
        - $\text{err}_1 = -\log{\hat{y}_1}$
    - ${y}$가 1이라면
        - $\hat{y}$이 1에 가까울수록 오차가 $\infty$에 가깝고
        - $\hat{y}$이 0에 가까울수록 오차가 0에 가깝게 만들기
        - $\text{err}_0 = -\log{(1 - \hat{y}_0)}$

- 이 오차의 식을 일반화시키고(err1과 err0을 하나의 식으로 합치고)
- 평균을 계산한 오차식이 **Log Loss** , 혹은 **Cross Entropy**
