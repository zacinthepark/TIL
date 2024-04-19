### Softmax Classification

<p align="center">
    <img width="600" alt="softmax_classification_1" src="https://github.com/zacinthepark/TIL/assets/86648892/0fa2d00c-a46a-4e83-819f-ccec78740ea0">
</p>

- Softmax를 이용한 다중분류의 아이디어는 A, B, C가 있을 때 A인지 아닌지, B인지 아닌지, C인지 아닌지의 이진분류 문제로 분할하여 풀어가는 것
- input vector의 크기가 n이고, 분류하고자 하는 클래스의 개수가 m일 때, `nxm` weight matrix를 만들어 `nx1`짜리 이진분류기 m개를 만든다고 생각

<p align="center">
    <img width="600" alt="softmax_classification_2" src="https://github.com/zacinthepark/TIL/assets/86648892/39cc6934-b62c-47e4-a456-8d320b0ced13">
</p>

- 각각의 이진분류기 (A일지 아닐지, B일지 아닐지, C일지 아닐지)에 대한 확률 계산을 `sigmoid`를 통해 수행
- 이 확률값들에 대하여 전체를 1로 하도록 비율 계산 (proportional calculation)
- 이를 One-Hot Encoding하여 해당하는 클래스 분류

<p align="center">
    <img width="600" alt="softmax_classification_3" src="https://github.com/zacinthepark/TIL/assets/86648892/5fc38611-3093-4a3d-b65a-73e01c9feb62">
</p>

- 그렇다면 각각의 이진분류기들의 w, b는 어떤 손실함수를 통해 업데이트할까?
- 이진분류와 비슷하게 $-log$ 함수를 사용
- Loss Function은 bit가 엇갈리면 무한대, 엇갈리지 않으면 0이라는 오차를 부여

$\infty$

### ANN

<p align="center">
    <img width="600" alt="conventional_ann_1" src="https://github.com/zacinthepark/TIL/assets/86648892/df395ed0-8f4a-48fd-80dd-1bed18893002">
</p>

<p align="center">
    <img width="600" alt="conventional_ann_2" src="https://github.com/zacinthepark/TIL/assets/86648892/a08e2326-a7cf-451e-81af-442459ef5b7f">
</p>

- hidden layer 1
    - weight의 matrix size는 `[3, 4]`
    - bias의 size는 `[4]`
    - 노드 1개당 1x3 사이즈의 `input vector와 3x1 weight를 matmul한 값 + bias`하여 값 1개 생성
    - 이러한 값이 4개가 되어 `[1, 4]` hidden layer 1 vector 생성

- hidden layer 2
    - weight의 matrix size는 `[4, 4]`
    - bias의 size는 `[4]`
    - 노드 1개당 1x4 사이즈의 `hidden layer 1 vector와 4x1 weight를 matmul한 값 + bias`하여 값 1개 생성
    - 이러한 값이 4개가 되어 `[1, 4]` hidden layer 2 vector 생성

- output layer
    - weight의 matrix size는 `[4, 1]`
    - bias size는 `[1]`
    - `hidden layer 2 vector와 4x1 weight를 matmul한 값 + bias`하여 값 1개 생성

- 업데이트되는 값은
    - w: `[3, 4]`, `[4, 4]`, `[4, 1]` 하여 총 32개의 weight 값
    - b: `[4]`, `[4]`, `[1]` 하여 총 9개의 bias 값
    - 총 41개의 값

#### ANN to DNN

<p align="center">
    <img width="600" alt="ann_to_dnn" src="https://github.com/zacinthepark/TIL/assets/86648892/86acd8b8-1c4c-4c03-95e7-723ca6840b4b">
</p>

- 딥러닝은 다음의 한계점들을 극복하면서 발전해왔다

    - 데이터가 부족하다
        - &rarr; 빅데이터 시대의 도래

    - 컴퓨팅 기술이 딥러닝 연산을 처리하기엔 느렸다
        - &rarr; 그래픽을 위한 3차원 행렬 연산을 위해 등장했던 GPU가 딥러닝 행렬 연산에 사용

    - input이 2차원 이상 값이더라도, 가중치 행렬과의 곱 + bias를 통해 하나의 값이 되어 1차원 벡터 값으로 변환된다
        - &rarr; CNN을 통해 해결

    - sigmoid를 활성화 함수로 사용하는 경우 기울기 소실 문제로 인해 레이어를 많이 쌓지 못한다
        - &rarr; ReLU(Rectified Linear Unit)을 통해 해결
