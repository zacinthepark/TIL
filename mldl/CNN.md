## Convolutional Neural Networks

---

### Convolutional Layers

참조 링크: https://keras.io/api/layers/convolution_layers/

이미지 정보 구조를 파괴하지 않은 채로 Feature를 추출하는 것이 Conv Layer의 목적

![convolutional_layer_filter](https://github.com/zacinthepark/TIL/assets/86648892/0bb49d3d-ec52-4405-8660-38da6c4fac97)

CIFAR 데이터를 Flatten에서 학습시키면 위치 정보가 소실된다
Convolutional Layer의 필터가 동작해서 파란색, 연두색, ... Feature Map 10개를 만들었다
Feature Map(Activation Map)은 Convolutional Layer를 거쳐 만들어진 서로 다른 Feature의 모임
3x3 Convolutional Layer Filter가 있다고 가정하면 Sliding 해가며 곱을 하고, 이를 통해 Feature Map을 생성
합성곱 레이어의 Stride를 조정할 수 있고, 이는 Feature Map 크기에 영향을 준다

![zero_padding](https://github.com/zacinthepark/TIL/assets/86648892/704eef58-0725-4249-9b94-4ac33ba3643d)

Zero Padding은 Feature Map의 크기를 이미지 크기에 맞게 유지하고, 외곽 정보를 더 반영시키는 효과가 있다

각각의 Filter를 하나의 Feature라고 보면 쉽다
filter 개수는 결과적으로는 출력층의 차원의 수로, 각 필터 별로 다른 가중치들을 통한 연산을 수행함
학습을 하면서 구분이 잘 되는 필터들 쪽으로 최적화가 되면서 모델이 완성

필터의 depth는 input의 channel, 혹은 이전 feature map의 depth size를 따라간다
28x28 이미지의 특징이 32개 추출되었다

Pooling Layer는 Feature Map의 가로 세로 사이즈 조절 (depth에는 영향을 주지 않음)
연산량을 줄이고 학습속도를 높이기 위해서 사용
그렇다면 필요한 정보를 남기는 것이 중요
ReLU의 의미는 값이 크면 클수록 그 영향이 클 것이다
Maxpooling Layer: ReLU를 적용한 pooling layer로 해당 픽셀 영역에서 영향력이 높은 픽셀을 가져가는 것
Average Pooling Layer: 해당 픽셀 영역의 정보를 골고루 반영

> 특징 추출(conv layer) > 사진 줄이기(pooling) > 특징 추출(conv layer) > 사진 줄이기(pooling) 반복

> pooling을 통해 정보의 손실은 발생할 수 있으나 연산량을 줄일 수 있음

### from keras.layers import Conv2D, MaxPool2D

- `Conv2D`
    - `filters`: 새롭게 제작하려는 feature map의 수
    - `kernel_size`: Conv2D filter의 사이즈 (keras에서 depth는 보정)
    - `strides`: Conv2D filter의 이동 보폭
    - `padding`: 이전 feature map의 크기(가로, 세로) 유지 + 외곽 정보 더 반영
    - `activation`: 빼먹지 않기
- `MaxPool2D`
    - `pool_size`: MaxPool Filter의 사이즈
    - `strides`: 기본적으로 pool_size를 따름 (이동 보폭)

### LeNet-5

![lenet5](https://github.com/zacinthepark/TIL/assets/86648892/c12da7b9-b47c-492c-b1b5-b684d3814377)

`filters`
`pooling_size = (2, 2)`
`strides = (2, 2)`
400으로 flatten하여 120개의 노드를 가진 Dense Layer와 Fully Connected

### AlexNet

![alexnet](https://github.com/zacinthepark/TIL/assets/86648892/69a4a269-13c7-4b69-93f6-e24401c794b2)

`filter_size = (11, 11, 3)`
`filters = 96`
`strides = (4, 4)`

`pool_size = (3, 3)`
`strides = (2, 2)`

ImageNet 대회 1000개 클래스 분류