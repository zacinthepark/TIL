## t-test

![t_test_1](https://github.com/zacinthepark/TIL/assets/86648892/b58fa961-1f60-46ef-a118-4e82c9e7fb08)
![t_test_2](https://github.com/zacinthepark/TIL/assets/86648892/1f572187-f488-4c26-bf26-22ca3c0968f4)

t-test
- Student의 t-test
- 두 집단의 평균의 차이를 보기위한 통계량
- t는 그룹 간 평균 차이에 비례하는 변수
- `표본평균값의 차이 / 표본평균이 갖는 불확실도`
- 표본평균값의 차이를 불확실도로 나눠줘서 차이가 유의하게 큰지 확인할 수 있음

1. 그룹 간 평균 차가 클수록 t-value는 크다
2. t-value는 평균 차이를 불확실도로 나눈 것
3. 즉, 평균차가 클수록 t값은 커진다
4. 불확실도가 적을수록 t값은 커진다

독립표본 t-test: 두 그룹에 들어있는 사람들이 전혀 다른 사람들이다
대응표본 t-test: 두 그룹에 들어있는 사람들이 같은 사람들이다 (비포-애프터 검정)

## ANOVA

![anova_1](https://github.com/zacinthepark/TIL/assets/86648892/72b183d1-a1c2-4836-8550-c1cc6c43c1e0)
![anova_2](https://github.com/zacinthepark/TIL/assets/86648892/2bc79d39-cd4f-4512-9cf9-4a56314e0087)
![anova_3](https://github.com/zacinthepark/TIL/assets/86648892/a7d8a122-6ae6-4760-8f0b-5e119467f213)
![anova_4](https://github.com/zacinthepark/TIL/assets/86648892/62de3b44-f8d3-435d-8e76-4190fa9e59a4)
![anova_5](https://github.com/zacinthepark/TIL/assets/86648892/baf89db7-345f-42b7-b2a8-4f759d4f86a3)
![anova_6](https://github.com/zacinthepark/TIL/assets/86648892/1d808c70-8652-4eda-aef5-fedc9b373dec)
![anova_7](https://github.com/zacinthepark/TIL/assets/86648892/6ecd9629-21dd-41b9-b5a9-ff6abaf99dd7)
![anova_8](https://github.com/zacinthepark/TIL/assets/86648892/a9c39ca7-9ab3-4be0-8ee7-16a66862e329)
![anova_9](https://github.com/zacinthepark/TIL/assets/86648892/255deab3-b657-4634-9f2f-8e06601c7262)
![anova_10](https://github.com/zacinthepark/TIL/assets/86648892/d281a5c6-afb7-4b10-a887-4ed51dde1a5a)

### ANOVA (분산분석)

- 여러 집단 평균의 차이를 보기 위한 통계량
- 모든 그룹의 평균이 동일한지, 최소한 하나의 그룹의 평균은 유의하게 다른지 판별할 수 있음
- Analysis Of Variance
    - 분산을 이용한 분석

- 분자
- 세 그룹이 있을 때 표본 평균들의 차이를 어떻게 계산할 수 있을까?
    - 세 그룹의 평균의 평균으로부터 떨어진 정도를 이용하는 것이 아이디어
    - 즉, **표본 평균 간 분산** 을 이용해 여러 그룹의 차이를 표현
- 분모
    - 분자에 분산을 넣었으니 분모도 분산을 이용해서 불확실도를 표현
    - 불확실도는 결국 각 그룹의 데이터들 평균적으로 퍼진 정도를 의미
    - 즉, **표본 그룹 내의 분산** 을 이용해 여러 그룹의 평균적 불확실도 표현

- 변화량을 불확실도로 나눠줘서 변화량이 유의하게 큰지 확인할 수 있음

- ANOVA는 t-test 이전에 수행해주는 것
    - 여러 그룹 간 평균 비교를 할 때
    - 그룹 pair별로 t-test를 바로 수행해주는 것이 아닌
    - 전체적으로 차이가 있는 그룹이 있는지 ANOVA를 이용해 확인한 후
    - 그룹 pair별로 t-test를 수행하는 것
    - ANOVA 뒤에 수행한 t-test를 사후분석이라 부르기도 함

### F-value

- ANOVA에서 사용되는 표본 평균들의 변화량을 나타내는 값
- 그룹들의 평균값과 그룹 내 분산값이 변하는 케이스
    1. 그룹 간 평균이 멀어지거나
    2. 그룹 간 평균이 가까워지거나
    3. 그룹 내 분산이 작아지거나
    4. 그룹 내 분산이 커지거나
- F 값이 큰 경우
    - 각 그룹의 평균들이 멀리 떨어진 경우
    - 각 그룹 내 분산이 작은 경우
