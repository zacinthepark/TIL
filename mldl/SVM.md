## Support Vector Machine

---

### 1. 서포트 벡터 머신 (Support Vector Machine)

서포트 벡터 머신은 분류, 회귀에 모두 사용할 수 있는 매우 강력한 모델로서, 특히 복잡한 분류 문제, 작거나 중간 크기의 데이터셋에 적합하다.

<p align="center">
    <img width="700" alt="svm_1" src="https://github.com/zacinthepark/TIL/assets/86648892/34d99770-bf1f-4451-8faa-a83e04645a8d">
</p>

좌표평면상에 존재하는 빨간색과 파란색 집단을 어떻게 하면 잘 나눌 수 있을까? 빨간색과 파란색을 나누는 분류 선은 무수히 많이 그릴 수 있지만 대표적으로 1, 2, 3번 직선이 있다고 가정하자. 그렇다면 1, 2, 3번 중 **어느 직선이 가장 두 집단을 잘 분류했다고 할 수 있을까?** **그리고 잘 분류했다는 것은 어떤 의미일까?**

이와 관련한 것이 서포트 벡터 머신의 개념이다. **서포트 벡터 머신은 여러 집단들을 가장 잘 구분할 수 있는 최적의 선을 찾는 것이 목표이다.** 1, 2, 3번 직선 모두 train data로 학습할 때는 집단을 100% 잘 분류할 수 있을지는 몰라도, 그보다 중요한 것은 새로운 데이터가 들어왔을 때 잘 분류를 할 수 있을지가 관건이다. 따라서 그을 수 있는 수많은 선들 중 **최적의 직선을 골라 모델을 만들어야 하는 것이다.** 위 그림에서는 1번 직선이 두 집단을 가장 잘 분류한 최적의 직선이라 할 수 있다.

### 2. 최적의 결정 경계 (Decision Boundary), 초평면 (Hyperplane)

> 최적의 결정 경계는 마진을 최대화한다.

> n개의 속성을 가진 데이터에는 최소 n+1 개의 서포트 벡터가 존재한다.

<p align="center">
    <img width="700" alt="svm_2" src="https://github.com/zacinthepark/TIL/assets/86648892/5c4b8b82-f0c9-490c-91ad-1415bef5136b">
</p>

> 서포트 벡터: 마진을 만들 때 기준이 되고, 도와주는 벡터 (결정 경계와 가까이 있는 데이터 포인트들)

위 그림의 경우, 영역의 경계 부분에 위치한 데이터들의 사이가 최대로 떨어져있으면 두 집단이 잘 분류되었다고 간주한다. 따라서 최적의 직선을 구하는 *첫번째 단계는 경계 인접 부분에 위치한 두 서포트 벡터들을 지나는 평행 직선을 그리는 것*이다.

<p align="center">
    <img width="700" alt="svm_3" src="https://github.com/zacinthepark/TIL/assets/86648892/8017a65b-9126-4d9a-a016-bdafd6ee1a26">
</p>

*두번째 단계는 평행으로 그은 두 직선에 직교(직각)하는 선을 긋는다.* 이것을 `마진(Margin)`이라 하며, 마진은 두 집단 사이의 거리라고 볼 수 있는데, 이 거리가 최대로 멀수록 두 집단이 잘 분류되었다고 생각하면 된다. 이 때 **'거리'를 '유사도'라고 볼 수 있다.** 거리가 멀수록 두 집단 간의 유사도가 적다, 즉 잘 분류되어있다고 할 수 있는 것이다.

<p align="center">
    <img width="700" alt="svm_4" src="https://github.com/zacinthepark/TIL/assets/86648892/346638e5-f84b-4b50-b814-013602bc7974">
</p>

왼쪽 그림에 비해 오른쪽 그림에서 두 집단 사이의 거리가 멀다. 오른쪽의 경우에 새로운 데이터가 들어왔을 때 그 데이터가 어느 집단에 속할지 헷갈리지 않고 더 잘 분류될 수 있을 것이다.

우리가 가진 데이터들을 좌표평면상에 그렸을 때 바로 그 직선의 길이(거리)를 구하기 힘들기에 여기서 유클리드 거리의 개념이 사용되는 것이다.

<p align="center">
    <img width="700" alt="svm_5" src="https://github.com/zacinthepark/TIL/assets/86648892/fed73457-5db9-46c9-965d-5e8e14d73c4e">
</p>

*마지막으로 두 서포특 벡터들의 중앙을 지나면서 직교(직각)하는 직선을 구한다.* 이 직선은 두 집단을 분류하는 최적의 직선이며, `초평면(Hyperplane)` 혹은 `결정 경계(Decision Boundary)`라고 하며, **이것을 구하는 것이 서포트 벡터 머신의 핵심** 이라고 할 수 있다. 또한 서포트 벡터 머신은 스케일링에 따라 데이터들이 찍히는 위치가 달라지고, 그에 따라서 결정 경계가 달라지기에 스케일링을 잘해주는 것이 중요하다.

<p align="center">
    <img width="350" height="280" alt="svm_6" src="https://github.com/zacinthepark/TIL/assets/86648892/f9e8881f-6e84-489b-a97f-b3ff7b056f38">
    <img width="350" height="280" alt="svm_7" src="https://github.com/zacinthepark/TIL/assets/86648892/b56682b5-c58a-4896-908d-a7c20d87668b">
</p>

데이터에 2개의 속성(Feature)만 있다면 결정 경계는 선의 형태, 속성이 3개로 늘어난다면 면의 형태가 될 것이다. 우리가 시각적으로 인지할 수 있는 범위는 3차원까지이다. 차원, 즉 속서으이 개수가 늘어날수록 복잡해질 것이며, 결정 경계도 단순 평면을 넘어 고차원이 될텐데, 이를 초평면이라 부르는 것이다.

### 3. 하드 마진 SVM과 소프트 마진 SVM

> 이상치(Outlier)를 얼마나 허용할 것인가?

<p align="center">
    <img width="350" height="300" alt="svm_8" src="https://github.com/zacinthepark/TIL/assets/86648892/93cbbed8-7e28-4f97-b118-d3bcd3a2de2d">
    <img width="350" height="300" alt="svm_9" src="https://github.com/zacinthepark/TIL/assets/86648892/f12993e0-644d-44d9-97b7-47e00d70a7d3">
</p>

먼저 마진 값을 타이트하게 잡는 하드 마진 SVM은 **이상치(Outlier)들을 허용하지 않는다.** 때문에 과적합(overfitting)이 발생하기 쉽고, 노이즈로 인해 최적의 결정 경계를 잘못 구분하거나 못 찾는 경우가 발생할 수 있다.

이러한 하드 마진 SVM의 특징을 보완하기 위해 소프트 마진 SVM을 사용한다. 소프트 마진은 이상치들을 어느 정도 허용하면서 결정 경계를 설정하는 것이다.

scikit-learn에서는 파라미터 `C`를 통해 지정할 수 있다.

```python
from sklearn.svm import SVC

classifier = SVC(C=0.01)  # default=1
```

### 4. SVM의 분류와 회귀

<p align="center">
    <img width="700" alt="svm_10" src="https://github.com/zacinthepark/TIL/assets/86648892/e2d56f0e-beb0-4acf-bb71-e94fd59c4417">
</p>

<p align="center">
    <img width="700" alt="svm_11" src="https://github.com/zacinthepark/TIL/assets/86648892/39857611-1726-4754-af44-d7edcb75c745">
</p>

먼저 분류 문제에 서포트 벡터 머신을 사용할 경우, 각 집단의 경계에 인접해있는 데이터들의 거리가 가장 멀어지게 폭(마진)을 설정하여 마진의 가운데를 결정 경계로 잡는다. 이러한 분류의 경우, 두 집단 사이의 거리(마진)가 클수록 좋기에 소프트 마진을 사용하는 것이 좋다.

반면 회귀 문제로 서포트 벡터 머신을 사용하는 경우에는 데이터들을 대표하는 직선을 만드는 것이 목표이기에 데이터들을 아우를 수 있게 마진을 잡고 그 중앙에 회귀선을 그어주는 방식으로 작동한다. 따라서 마진이 좁을수록 데이터들을 대표할 수 있는 회귀선을 잘 만들 수 있기에 하드 마진을 사용하는 것이 좋다.

#### SVC

```python
from sklearn.svm import SVC

classifier = SVC(kernel='linear')

training_points = [[1, 2], [1, 5], [2, 2], [7, 5], [9, 4], [8, 2]]
labels = [1, 1, 1, 0, 0, 0]

classifier.fit(training_points, labels)
```

```python
print(classifier.predict([[3, 2]]))
```

<pre>
[1]
</pre>

```python
print(classifier.support_vectors_)
```

<pre>
[[7. 5.]
 [8. 2.]
 [2. 2.]]
</pre>

#### SVR

```python
import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, explained_variance_score

california = fetch_california_housing()
X = pd.DataFrame(california.data, columns=california.feature_names)
y = pd.DataFrame(california.target, columns=['MedHouseVal'])
y = y.values.ravel()
s = 1000
e = 100
X_train, y_train = X[:s], y[:s]
X_test, y_test = X[s:s+e], y[s:s+e]

# SVR
# kernel: 벡터 변형 커널
# C: cost, 학습 오류에 대한 페널티, C값이 클수록 모델이 train data에 더 최적화됨, 너무 크면 overfitting 발생
# epsilon: 임계값, 예측한 값이 범위 안에 있으면 페널티 부여 x
svr = SVR(kernel='linear', C=1.0, epsilon=0.1)
svr.fit(X_train, y_train)

y_pred = svr.predict(X_test)

print('MSE: ', mean_squared_error(y_test, y_pred))
print('EVS: ', explained_variance_score(y_test, y_pred))
```

<pre>
MSE:  11.400273864726405
EVS:  -9.37250140114155
</pre>

### 5. 커널 트릭

단순한 데이터 세트의 경우 쉽고 간단하게 선으로(linear) 분리가 가능하지만 데이터 세트가 복잡하고 많아지면 하나의 선 혹은 면으로 분리하기 어려워진다. 예를 들어, 2차원 좌표평면 상에 복잡하게 존재하는 데이터들은 어떻게 분류할 수 있을까?

<p align="center">
    <img width="700" alt="svm_12" src="https://github.com/zacinthepark/TIL/assets/86648892/fc548227-6b72-4a47-89eb-cfb848576dab">
</p>

이러한 경우, 2차원 평면에 있는 데이터들을 3차원으로 차원을 변환시켜보면 두 집단을 어떻게 분류할 수 있을지가 더 쉽게 보인다. 이처럼 **저차원에서 해결하기 어려운 문제들을 고차원으로 변환시켜 문제를 해결할 때 사용** 하는 것이 **커널 함수(kernel function)** 이다.

<p align="center">
    <img width="700" alt="svm_13" src="https://github.com/zacinthepark/TIL/assets/86648892/1f534da2-0b37-476a-a37a-3e1d5eaa9258">
</p>

왼쪽 그림처럼 커널 함수를 사용하여 2차원 평면에 있던 데이터들을 3차원으로 변환시켜 두 집단을 구분하는 하나의 면을 생성한다. 그 다음 오른쪽 그림과 같이 다시 2차원으로 차원을 축소해주면 두 집단이 잘 분류되었음을 알 수 있다.

#### 5-1. 다항식 (Polynomial)

<p align="center">
    <img width="350" alt="svm_14" src="https://github.com/zacinthepark/TIL/assets/86648892/df0004e2-0b28-40f4-b3ed-d3b34b9b2f06">
    <img width="350" alt="svm_15" src="https://github.com/zacinthepark/TIL/assets/86648892/6421ee91-be23-4df2-9969-80fe31b1645d">
</p>

$$
(x, y) \to (\sqrt{2}xy, x^2, y^2)
$$

위 예시는 2차원에서 3차원으로 변환한 예시이다. 이처럼 다항식(polynomial) 커널을 사용하면 데이터를 더 높은 차원으로 변형하여 나타냄으로써 초평면을 구할 수 있다.

#### 5-2. 방사 기저 함수 (RBF: Radial Bias Function)

RBF 커널은 2차원의 점을 무한한 차원의 점으로 변환한다. scikit-learn의 SVM 모델에서 `kernel`의 기본값이 `'rbf'`이다.

```python
from sklearn.svm import SVC

# kernel options: 'rbf', 'linear', 'poly', 'sigmoid'
classifier = SVC(kernel='rbf', C=2, gamma=0.5)
```

#### 5-3. `gamma`

<p align="center">
    <img width="350" alt="svm_16" src="https://github.com/zacinthepark/TIL/assets/86648892/6632420d-15ad-4df2-bcd3-425100eff510">
    <img width="350" alt="svm_17" src="https://github.com/zacinthepark/TIL/assets/86648892/9f55100c-3055-4383-b23f-a02b8e24b021">
</p>

`gamma`는 **결정 경계를 얼마나 유연하게 그을 것인지** 정해주는 것이다. 학습 데이터에 얼마나 민감하게 반응할 것인지 모델을 조정하는 것으로 `C`와 비슷한 개념이다.

`gamma` 값을 높이면 학습 데이터에 많이 의존해서 결정 경계를 구불구불 긋게 되며, 오버피팅을 초래할 수 있다. 반대로 `gamma`를 낮추면 학습 데이터에 별로 의존하지 않고, 결정 경계를 직선에 가깝게 긋게 되며, 언더피팅이 발생할 수 있다.
