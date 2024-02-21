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

### 실습

```python
import matplotlib.pyplot as plt
import numpy as np

# 브라우저 내부(inline)에 바로 그려지도록 해주는 코드
%matplotlib inline
```

```python
# 정규분포에서 난수 추출

np.random.seed(0)  # 동일한 난수가 나오게끔 시드 설정

x = np.arange(50)  # 0부터 49까지 1씩 증가하는 정수 생성
y = np.random.randn(50)  # 정규분포 난수 생성
print(y)
```

<pre>
[ 1.76405235  0.40015721  0.97873798  2.2408932   1.86755799 -0.97727788
  0.95008842 -0.15135721 -0.10321885  0.4105985   0.14404357  1.45427351
  0.76103773  0.12167502  0.44386323  0.33367433  1.49407907 -0.20515826
  0.3130677  -0.85409574 -2.55298982  0.6536186   0.8644362  -0.74216502
  2.26975462 -1.45436567  0.04575852 -0.18718385  1.53277921  1.46935877
  0.15494743  0.37816252 -0.88778575 -1.98079647 -0.34791215  0.15634897
  1.23029068  1.20237985 -0.38732682 -0.30230275 -1.04855297 -1.42001794
 -1.70627019  1.9507754  -0.50965218 -0.4380743  -1.25279536  0.77749036
 -1.61389785 -0.21274028]
</pre>

#### 기본 그래프 그리기

```python
plt.figure()
plt.plot(x, y)
plt.show()
```

<img width="855" alt="matplotlib1" src="https://github.com/zacinthepark/TIL/assets/86648892/d00b46e7-f21a-4038-8724-a78688d48e22">

#### figure 크기 설정 & 축 제목 표기

```python
plt.figure(figsize=(8, 4))
plt.plot(x, y)
plt.xlabel('Period (t)')
plt.ylabel('Change of Interest Rate over Last 50 Days')
# plt.savefig('./data/interest_rate.png')
plt.show()
```

<img width="857" alt="matplotlib2" src="https://github.com/zacinthepark/TIL/assets/86648892/fcde815a-2b42-4194-a79c-403f5e9768b4">

#### 그래프에 데이터 추가

```python
np.random.seed(2)

z = np.random.randn(50)
print(z)
```

<pre>
[-4.16757847e-01 -5.62668272e-02 -2.13619610e+00  1.64027081e+00
 -1.79343559e+00 -8.41747366e-01  5.02881417e-01 -1.24528809e+00
 -1.05795222e+00 -9.09007615e-01  5.51454045e-01  2.29220801e+00
  4.15393930e-02 -1.11792545e+00  5.39058321e-01 -5.96159700e-01
 -1.91304965e-02  1.17500122e+00 -7.47870949e-01  9.02525097e-03
 -8.78107893e-01 -1.56434170e-01  2.56570452e-01 -9.88779049e-01
 -3.38821966e-01 -2.36184031e-01 -6.37655012e-01 -1.18761229e+00
 -1.42121723e+00 -1.53495196e-01 -2.69056960e-01  2.23136679e+00
 -2.43476758e+00  1.12726505e-01  3.70444537e-01  1.35963386e+00
  5.01857207e-01 -8.44213704e-01  9.76147160e-06  5.42352572e-01
 -3.13508197e-01  7.71011738e-01 -1.86809065e+00  1.73118467e+00
  1.46767801e+00 -3.35677339e-01  6.11340780e-01  4.79705919e-02
 -8.29135289e-01  8.77102184e-02]
</pre>

```python
plt.figure(figsize=(8, 4))
plt.plot(x, y, label='Korea')
plt.plot(x, z, label='United States')
plt.xlabel('Period (t)')
plt.ylabel('Percent change')
plt.title('Percent Change of interest Rates over Last 50 Days')
plt.legend()  # legend를 이용하면 범례 표기 가능
plt.tight_layout()  # 그림을 사이즈에 맞게 변경하여 출력
# plt.savefig('./data/interest_rate.png')
plt.show()
```

<img width="853" alt="matplotlib3" src="https://github.com/zacinthepark/TIL/assets/86648892/c0fc4a07-5560-4d35-a780-b69f5b746071">

#### 여러 그래프 그리기 - subplot

```python
a = np.linspace(0.0, 3.0, 31)  # 0과 3 사이에 있는 실수 30개를 균등한 간격으로 생성
print(a)
```

<pre>
[0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.  1.1 1.2 1.3 1.4 1.5 1.6 1.7
 1.8 1.9 2.  2.1 2.2 2.3 2.4 2.5 2.6 2.7 2.8 2.9 3. ]
</pre>

```python
sin = np.sin(2 * np.pi * a)
print(sin)

decaying_sin = np.sin(2 * np.pi * a) * np.exp(-a)
print(decaying_sin)
```

<pre>
[ 0.00000000e+00  5.87785252e-01  9.51056516e-01  9.51056516e-01
  5.87785252e-01  1.22464680e-16 -5.87785252e-01 -9.51056516e-01
 -9.51056516e-01 -5.87785252e-01 -2.44929360e-16  5.87785252e-01
  9.51056516e-01  9.51056516e-01  5.87785252e-01  3.67394040e-16
 -5.87785252e-01 -9.51056516e-01 -9.51056516e-01 -5.87785252e-01
 -4.89858720e-16  5.87785252e-01  9.51056516e-01  9.51056516e-01
  5.87785252e-01  6.12323400e-16 -5.87785252e-01 -9.51056516e-01
 -9.51056516e-01 -5.87785252e-01 -7.34788079e-16]
[ 0.00000000e+00  5.31850090e-01  7.78659218e-01  7.04559996e-01
  3.94004237e-01  7.42785831e-17 -3.22583386e-01 -4.72280689e-01
 -4.27337239e-01 -2.38975650e-01 -9.01044760e-17  1.95656714e-01
  2.86452718e-01  2.59193138e-01  1.44946059e-01  8.19766909e-17
 -1.18671796e-01 -1.73742356e-01 -1.57208585e-01 -8.79142286e-02
 -6.62951686e-17  7.19780826e-02  1.05380066e-01  9.53518266e-02
  5.33226751e-02  5.02625654e-17 -4.36569139e-02 -6.39162408e-02
 -5.78338063e-02 -3.23418373e-02 -3.65829443e-17]
</pre>

```python
plt.subplot(2, 1, 1)  # 2개의 행과 1개의 열을 사용, 그리고 첫번째(위)에 그리겠다고 명시
plt.plot(a, decaying_sin, '-g.')  # 라인: - / 초록색: g / 도트: . 으로 마커 설정
plt.title('Sine Graph Approaching to Zero')

plt.subplot(2, 1, 2)
plt.plot(a, sin, 'o-')
plt.title('Sine Graph')

plt.tight_layout()
plt.show()
```

<img width="854" alt="matplotlib4" src="https://github.com/zacinthepark/TIL/assets/86648892/0703e816-e399-4ff0-bd1d-916058cb12c5">

#### `sharex`: x축 공유

```python
plt.subplot(2, 1, 1)
plt.plot(a, decaying_sin, '-g.', label='decaying_sin')
plt.xticks(visible=False)  # visible=False x축 값 안보임
plt.title('Sine Graph Approaching to Zero')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(a, sin, 'o-', label='sine')
plt.title('Sine Graph')
plt.xlabel('Num Cycle')
plt.legend()

plt.suptitle('Two Different Sine Graph', y=1.05, fontsize=20)  # suptitle을 이용하여 타이틀 설정

plt.show()
```

<img width="853" alt="matplotlib5" src="https://github.com/zacinthepark/TIL/assets/86648892/ac664fbe-493f-4034-ba5f-0bfeea894e01">

#### 여러 그래프 그리기 - subplots

```python
fig, ax = plt.subplots(2, 1)  # figure와 ax를 같이 설정해줘야함
ax[0].plot(a, decaying_sin, 'g-')  # ax[행 번호, 열 번호], 지금은 2개의 그래프이기에 인덱스 하나로 표현 가능
ax[1].plot(a, sin, 'b-.')
plt.show()
```

<img width="854" alt="matplotlib6" src="https://github.com/zacinthepark/TIL/assets/86648892/fa0716f1-ce76-4582-86db-df2e5729c71b">

#### 두 종류의 그래프 하나에 담기: 바 그래프 & 라인 그래프

```python
# 토이 데이터

periods = np.arange(1951, 1961)
housing_prices = np.array([15, 25, 31, 24, 22, 27, 40, 55, 60, 58])
num_trading = np.array([6, 6.6, 7, 4.5, 4, 6, 9.5, 11, 20, 18])
```

```python
fig, ax1 = plt.subplots(figsize=(9,5))
# ax1
# 집값 그래프는 라인으로 표기 plot 이용
ax1.plot(periods, housing_prices, 'o-', linewidth=1, alpha=0.8, label='housing price')
ax1.set_xlabel('Year', fontsize=13)
ax1.set_ylabel('Price ($000)', fontsize=13)
ax1.set_ylim(0, 70)  # ax1의 y축 범위 설정 0부터 70까지만 표기

# 총 거래량 그래프는 막대 그래프로 표기 bar 이용
ax2 = ax1.twinx()  # twinx는 x축은 공유하지만 y축은 공유하지 않게 함
ax2.bar(periods, num_trading, color='coral', alpha=0.3, label='#houses traded')  # bar 그래프 생성
ax2.set_ylabel('#house traded (millions)', fontsize=13)
ax2.set_ylim(0, 22)

ax1.legend(loc='upper left')  # legend에 loc 인수를 설정하면 범례의 위치를 설정할 수 있음
ax2.legend(loc='upper right')

plt.title('Housing Prices and Demands of ABC Country between 1941 and 1960', fontsize=16)  # figure에 대한 타이틀
plt.tight_layout()

plt.show()
```

<img width="856" alt="matplotlib7" src="https://github.com/zacinthepark/TIL/assets/86648892/1c20b1ce-6b33-4116-ae72-31cef89712d9">
