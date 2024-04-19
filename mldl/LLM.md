### LLM

- Generative Pre-Trained Model
    - Generative
        - 생성망
        - Generative Model을 학습시키는 과정
    - Pre-Trained
        - 학습시켜 배포
- Generation 기반 모델을 사전학습시켜 배포한 모델

- RNN Cell에 가중치를 부여하여 집중하는 attention 알고리즘
- 인코더는 현실세계에 있는 태그를 가지고 학습을 할 때 이를 숫자로 바꿔주는 것
- 디코더는 이를 현실세계의 것으로 변환

- Encoding -> RNN Cell에 학습하여 가중치 부여 -> Decoding하여 문장 생성

- 분류, 키워드 추출, 문서 요약 등 응용 태스크
- 많이 사용하는 응용 태스크를 적용

### 트랜스포머

Positional Encdoing
I am a boy 일 때 주요한 부분(I, boy)
Feed Forward: 생성망 모델

인코딩 (왼쪽)
학습을 위한 디코딩 (오른쪽 3번째 Add Norm부터 아래)
추론을 위한 디코딩 (오른쪽 그 위)

### 강화학습기반 LLM

LLM은 강화학습을 기반으로 한다

Step 1 Pretrain
Step 2 성능을 높이기 위한 튜닝
Step 3 GPT를 agent로 하여 질문을 넣고 리워드를 통해 강화학습

RLHF: Reinforcement Learning with Human Feedback
Human Feedback을 바탕으로 몬테카를로 트리서치를 통해 성능 개선
