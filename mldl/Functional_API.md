## Functional API

---

> 1. Input 지정
> 2. 직접 연결을 지정
> 3. 모델로 시작과 끝을 묶기

### Sequential API vs. Functional API

- `Input()`
- `Dense()`
- `Model()`
- 다중 출력은 권장하지 않음

### 다중 입력

- 명시적으로 학습하는 Feature 그룹을 구분하고 싶을 때 사용할 수 있음
- 여러 개의 Input Layer가 있을 때, 학습하는 데이터의 분석 단위(개수)는 동일해야한다
- 모델 선언, 학습, 예측 시에 다중 입력 층들을 리스트로 제공해야한다
