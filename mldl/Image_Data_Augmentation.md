## Image Data Augmentation

---

1. 부족한 Data의 양을 늘려보려고
2. 학습 과정에서 Data 변형을 하여 다양성을 늘리려고

이를 통해 모델이 일반적인 상황에서 잘 동작하기를 기대

keras 3.x version부터는 Modeling 과정에 Augmentation Layer를 생성
이전 version에서는 데이터를 증강시키는 방향이었다면, 현 버전에서는 이미지를 변형시키는 방향
