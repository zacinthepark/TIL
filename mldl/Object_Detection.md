## Object Detection

---

- Classification + Localiztion
- Multi-Labeled Classification + Bounding Box Regression
- 주요 개념
    - 1: Bounding Box
    - 2: Class Classification
    - 3: Confidence Score
    - 4: IoU
    - 5: NMS
    - 6: Precision, Recall, AP, mAP
    - 7: Annotation

### Bounding Box

- 하나의 Object가 포함된 최소 크기 박스
- 모델에 따라 Bounding Box를 표현하는 방식이 다름
    - x min, y min, x max, y max
    - x center, y center, width, height
    - 표현 방식에는 차이가 있어도 결국 **위치 정보** 를 표기
- Bounding Box Regression
    - Object가 있는 위치를 예측
    - Ground-Truth Box(실제 위치)와 Predicted Box(예측 위치)

### Confidence Score

- Bounding Box의 신뢰성
- Object가 Bounding Box 안에 있는지, 이에 대한 확신의 정도
- Ground-Truth Box의 Confidence Score = `1`
- Predicted Box의 Confidence Score = `0 ~ 1`
    - 1에 가까울수록 Object가 있다고 판단
    - 0에 가까울수록 Object가 없다고 판단

### IoU

<img src="https://github.com/zacinthepark/TIL/assets/86648892/21304a93-7d9d-4bda-8cd9-1151e40e1246" width=300>
<img src="https://github.com/zacinthepark/TIL/assets/86648892/81ba5698-f7dc-4186-a096-20b4f55de0a9" width=311>

### NMS (Non-Maximum Suppression)

- NMS 알고리즘을 통해 동일 Object에 대한 Bounding Box들 중 가장 부합하는 박스를 추출

### Precision, Recall, AP, mAP

### Annotation

#### roboflow를 활용한 annotation

- Create Project
- Upload Image
- Manual Labeling
- Annotation 진행
- Train, Valid, Test 비율 설정
- Generate
- Export Dataset

#### ybat-master를 활용한 annotation

- Images Upload
- Classes Upload
- Annotation 진행
- Save YOLO
    - Annotation한 정보에 대한 labels 생성
- yaml 파일 생성
