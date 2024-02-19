## matplotlib 활용

---

- Matplotlib
    - 파이썬의 대표 시각화 라이브러리
    - pyplot 모듈을 이용하여 데이터를 쉽고 빠르게 시각화할 수 있음
    - 옵션을 이용하면 더 많은 정보를 전달할 수 있음
- subplot과 subplots
    - 두 커맨드를 이용하면 여러 그래프를 그리는 것이 가능
    - 하나의 figure에 여러 개의 axes를 만들어 그래프를 나타낼 수 있음
    - 하나의 ax에 두 개의 다른 종류의 그래프를 나타낼 수 있음

### Matplotlib

- 파이썬의 가장 인기 있는 데이터 시각화 라이브러리로, 2D 형태의 그래프와 이미지를 그릴 때 많이 사용
- pyplot 모듈을 많이 사용, 주로 plt라는 별칭을 이용하여 호출

### Matplotlib 그래프 그리기

- `plt.figure()`: 새로운 그래프를 담을 도화지 생성
- `plt.plot()`: 데이터 시각화 기능 담당, 그래프 유형(plot, hist, pie 등)과 변수를 주어 설정 가능
- `plt.show()`: 그래플 출력

### Matplotlib 그래프 구성 요소

<img width="671" alt="pyplot" src="https://github.com/zacinthepark/TIL/assets/86648892/89faae33-9b32-49ea-a92b-02a0700e9399">

- pyplot을 이용하면 figure, axes, axis를 쉽게 조작 가능

### 여러 개의 그래프 그리기

- 여러 개의 그래프를 하나의 figure에 담는다면 한번에 더 많은 정보를 효과적으로 전달할 수 있음
- Matplotlib의 pyplot 모듈에서는 `subplot`과 `subplots` 커맨드를 활용하여 여러 그래프 구현 가능

### `subplot`

<img width="670" alt="subplot" src="https://github.com/zacinthepark/TIL/assets/86648892/d77590b7-e035-46bc-a9fc-f67a2cae2ef7">

### `subplots`

<img width="668" alt="subplots" src="https://github.com/zacinthepark/TIL/assets/86648892/20e68f3d-4b18-46bf-9352-7aecd7aad29d">

- `subplots`를 사용할 때 axes 객체의 `twinx` 메서드를 이용하면 x축을 공유하는 2개의 그래프를 동시에 그릴 수 있음
- `subplot`처럼 하나의 figure 안에 나눠서 그리는 것도 가능함
