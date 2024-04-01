## Hidden Layer와 활성화 함수

---

### Hidden Layer

| Layer (type) | Output Shape | Param # | 옵션 |
| ---- | ---- | ---- | ---- |
| dense (Dense) | (None, 8) | 104 | node, input_shape, activation |
| dense_1 (Dense) | (None, 4) | 36 | node, activation |
| dense_2 (Dense) | (None, 1) | 5 | node |

```python
target = 'medv'
x = data.drop(target, axis=1)
y = data.loc[:, target]
x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=.2, random_state=20)

scaler = MinMaxScaler()
x_train = scaler.fit_transform(x_train)
x_val = scaler.transform(x_val)

nfeatures = x_train.shape[1]
nfeatures

clear_session()

model = Sequential([Dense(8, input_shape=(nfeatures,), activation='relu'),
                    Dense(4, activation='relu'),
                    Dense(1)])

model.summary()
```

<pre>
Model: "sequential_1"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 dense_2 (Dense)             (None, 8)                 104       
                                                                 
 dense_3 (Dense)             (None, 4)                 36        
                                                                 
 dense_4 (Dense)             (None, 1)                 5         
                                                                 
=================================================================
Total params: 145 (580.00 Byte)
Trainable params: 145 (580.00 Byte)
Non-trainable params: 0 (0.00 Byte)
</pre>

### Hidden Layer와 Feature Representation

#### 연결

- Fully Connected: 모든 노드 간에 연결
- Locally Connected: 노드의 연결을 제어

#### 학습

![z_dl_2_1](https://github.com/zacinthepark/TIL/assets/86648892/236bca7e-16f6-4694-b7a7-c564886e5e6d)

- 선언한 구조에 따라 연결 생성
- 학습 과정에서 예측값과 실제값 간 오차를 loss function을 통해 계산하고
- 오차를 줄이기 위해 파라미터(가중치)를 업데이트

![z_dl_2_2](https://github.com/zacinthepark/TIL/assets/86648892/06a62bf0-4ef4-4337-b4cb-bacf092ba516)
![z_dl_2_3](https://github.com/zacinthepark/TIL/assets/86648892/0653384d-5c03-4b35-b7d8-4492f87859e9)

- 학습 과정을 통해 **오차를 최소화하는 파라미터(가중치) w1, w2, w3, w4, w5를 찾음**
- 이를 바탕으로 새로운 정보(노드) z1, z2 생성
- z1, z2의 의미는 정확히 알 수 없지만, **내부요인 점수** , **외부요인 점수** 라고 볼 수도 있음
- 최종 집값을 예측하는데 내부요인과 외부요인에 가중치를 주고 예측할 것임
- 오차를 최소화하는 과정을 거쳐 내부요인은 70%, 외부요인은 30% 가중치를 준다면
    - `집값 = 0.7 * 내부요인 + 0.3 * 외부요인`

![dl_feature_representation](https://github.com/zacinthepark/TIL/assets/86648892/240eb822-362f-4edf-98e4-c26be6326ecb)

- 결국 Hidden Layer에서는
    - 기존 데이터를 받아들여
    - (정확히 무엇인지 알기 어렵지만) **새로운 특징(Feature)** 을 만듬
    - 그 특징은 예측값과 실제값 사이의 오차를 **최소화** 해주는 **유익한 특징** 일 것
    - Hidden Layer에서는 기존 데이터가 **새롭게 표현(Representation)** 됨
    - 즉, **Feature Engineering** 이 진행된 것

### 활성화 함수 (Activation Function)

![activation_functions](https://github.com/zacinthepark/TIL/assets/86648892/30342fe9-76d8-4965-8ee7-20877bb34dd7)

![z_dl_2_4](https://github.com/zacinthepark/TIL/assets/86648892/488ebdc1-b4c2-4063-8e0a-5a861957f176)

- 현재 레이어(각 노드)의 결과값을 다음 레이어(연결된 각 노드)로 어떻게 전달할지 결정, 변환해주는 함수
- 만약 없다면 그림과 같이 히든 레이어를 아무리 추가해도 그냥 선형회귀(선형모델) 형태가 됨
- Hidden Layer에서는
    - Regression, 2-Class, Multi-Class: `relu`
        - 선형함수를 비선형 함수로 변환
    - RNN: `tanh`
- Output Layer에서는
    - 결과값을 다른 값으로 변환해주는 역할
    - 회귀 모델링에서는 필요하지 않음
    - 2-Class: `sigmoid`
    - Multi-Class: `softmax`
