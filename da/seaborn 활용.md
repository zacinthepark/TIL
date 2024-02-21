## seaborn 활용

---

- Seaborn 시각화 라이브러리의 특징
    - Matplotlib 기반의 시각화 라이브러리
    - 다채로운 시각화 테마 보유
    - 간결한 코드로 고품질 데이터 시각화 가능
    - 통계 패키지 statsmodels를 이용한 고등 통계 차트 기능 보유 (예: 회귀 플롯)

### Seaborn

- Matplotlib을 기반으로 하여 다채로운 디자인 테마와 통계용 차트 등이 추가된 강력한 시각화 라이브러리
- 한 줄의 코드로 강력한 시각화 가능

### Seaborn 특징

<img width="754" alt="sb1" src="https://github.com/zacinthepark/TIL/assets/86648892/c5fdde7b-5077-4b67-ba0c-63a9a51f0e43">

<img width="752" alt="sb2" src="https://github.com/zacinthepark/TIL/assets/86648892/4747ca2c-bb81-4fe5-ab44-06718b728262">

<img width="755" alt="sb3" src="https://github.com/zacinthepark/TIL/assets/86648892/61fb578f-7b61-4b91-b8f9-aebb7605c316">

### Seaborn 그래프 그리기

<img width="724" alt="sb4" src="https://github.com/zacinthepark/TIL/assets/86648892/6d8b883c-6731-40e8-952c-bca7467fde5e">

### 실습

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

```python
sns.get_dataset_names()
```

<pre>
['anagrams',
 'anscombe',
 'attention',
 'brain_networks',
 'car_crashes',
 'diamonds',
 'dots',
 'dowjones',
 'exercise',
 'flights',
 'fmri',
 'geyser',
 'glue',
 'healthexp',
 'iris',
 'mpg',
 'penguins',
 'planets',
 'seaice',
 'taxis',
 'tips',
 'titanic',
 'anagrams',
 'anagrams',
 'anscombe',
 'anscombe',
 'attention',
 'attention',
 'brain_networks',
 'brain_networks',
 'car_crashes',
 'car_crashes',
 'diamonds',
 'diamonds',
 'dots',
 'dots',
 'dowjones',
 'dowjones',
 'exercise',
 'exercise',
 'flights',
 'flights',
 'fmri',
 'fmri',
 'geyser',
 'geyser',
 'glue',
 'glue',
 'healthexp',
 'healthexp',
 'iris',
 'iris',
 'mpg',
 'mpg',
 'penguins',
 'penguins',
 'planets',
 'planets',
 'seaice',
 'seaice',
 'taxis',
 'taxis',
 'tips',
 'tips',
 'titanic',
 'titanic',
 'anagrams',
 'anscombe',
 'attention',
 'brain_networks',
 'car_crashes',
 'diamonds',
 'dots',
 'dowjones',
 'exercise',
 'flights',
 'fmri',
 'geyser',
 'glue',
 'healthexp',
 'iris',
 'mpg',
 'penguins',
 'planets',
 'seaice',
 'taxis',
 'tips',
 'titanic']
</pre>

```python
df = sns.load_dataset('iris')
display(df.head())
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sepal_length</th>
      <th>sepal_width</th>
      <th>petal_length</th>
      <th>petal_width</th>
      <th>species</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5.1</td>
      <td>3.5</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.9</td>
      <td>3.0</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.7</td>
      <td>3.2</td>
      <td>1.3</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.6</td>
      <td>3.1</td>
      <td>1.5</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5.0</td>
      <td>3.6</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
  </tbody>
</table>
</div>

```python
df['species'].unique()
```

<pre>
array(['setosa', 'versicolor', 'virginica'], dtype=object)
</pre>

#### seaborn의 scatterplot, regplot, lmplot

#### 산점도: scatterplot

```python
# scatterplot은 총 2개의 수치형 변수 x, y가 필요함
sns.scatterplot(x='sepal_length', y='petal_length', data=df)
plt.show()
```

<img width="855" alt="seaborn1" src="https://github.com/zacinthepark/TIL/assets/86648892/6052abfe-e32b-40f0-8f9f-d2a11f936bbf">

##### scatterplot의 `hue` 옵션

```python
# hue 인수의 값을 설정해준다면, 종류를 색상으로 나타낼 수 있음
# 붓꽃 종류별로 다른 색상의 점을 나타내고 싶다면, hue의 인수값으로 'species'로 설정하면됨
sns.scatterplot(x='sepal_length', y='petal_length', hue='species', data=df)
plt.show()
```

<img width="855" alt="seaborn2" src="https://github.com/zacinthepark/TIL/assets/86648892/cc8059d7-6758-44d6-9949-996b834d091c">

##### scatterplot의 `marker`, `alpha` 옵션

```python
# marker는 점의 모양, alpha는 투명도
plt.figure(figsize= (10, 4))
sns.scatterplot(x='sepal_length', 
                y='petal_length', 
                hue='species', 
                marker='+', 
                alpha=0.8, 
                data=df)
plt.show()
```

<img width="854" alt="seaborn3" src="https://github.com/zacinthepark/TIL/assets/86648892/88b8a5fc-b661-4ff0-aaea-c82074be13d2">

#### 산점도 + 추세선: regplot

```python
# regplot 호출
sns.regplot(x='sepal_length', y='petal_length', data=df)
plt.title('Scatter Plot with Regression Line')
plt.show()
```

<img width="855" alt="seaborn4" src="https://github.com/zacinthepark/TIL/assets/86648892/eec8ca9e-0b3f-4752-8973-51a3630fadb7">

##### 신뢰구간 제거: `ci` 인수

```python
sns.regplot(x='sepal_length', y='petal_length', ci=None, data=df)
plt.title('Scatter Plot with Regression Line')
plt.show()
```

<img width="858" alt="seaborn5" src="https://github.com/zacinthepark/TIL/assets/86648892/6f6a9ba2-a52f-4035-8ce7-7ce68f4d7740">

#### 범주별 산점도 + 추세선: lmplot

```python
sns.lmplot(x='sepal_length', y='petal_length', hue='species', data=df)
plt.title('Linear Model (LM) Plot')
plt.show()
```

<img width="858" alt="seaborn6" src="https://github.com/zacinthepark/TIL/assets/86648892/a2abb626-4c65-44a9-b66f-1dc6187eaa2b">

#### 점도표: rugplot

```python
plt.figure(figsize= (9, 4))
sns.rugplot(data=df, x='petal_length', hue='species')
plt.title('Distribution of Petal Length of Iris by Species')
plt.show()
```

<img width="854" alt="seaborn7" src="https://github.com/zacinthepark/TIL/assets/86648892/eedde6a3-bf16-4f56-b4a5-30d1f227ba1d">

#### 단변량 & 다변량 시각화: pairplot

```python
sns.pairplot(df)
plt.tight_layout()
plt.show()
```

<img width="856" alt="seaborn8" src="https://github.com/zacinthepark/TIL/assets/86648892/59743664-e635-490d-827e-e497404cbbee">

#### 범주별 pairplot: `hue` 옵션

```python
# pairplot by species
plot = sns.pairplot(df, hue='species')

# fig.suptitle 기능 활용
plot.fig.suptitle('Pair Plot of Iris by Species', y=1.05, fontsize=15)  # y값을 통해 타이틀 위치 조정

plt.show()
```

<img width="851" alt="seaborn9" src="https://github.com/zacinthepark/TIL/assets/86648892/24619407-13e6-4487-9536-27318e730ea5">

#### seaborn의 `heatmap`

```python
import pandas as pd

click_data = pd.read_csv('./data/click_sample_data.csv')
display(click_data)
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>category</th>
      <th>Journal</th>
      <th>article_id</th>
      <th>num_click</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>사설</td>
      <td>C일보</td>
      <td>zZyl1B7YkU</td>
      <td>1209</td>
    </tr>
    <tr>
      <th>1</th>
      <td>사회</td>
      <td>B일보</td>
      <td>ZZyBooxf21</td>
      <td>241</td>
    </tr>
    <tr>
      <th>2</th>
      <td>공학</td>
      <td>C일보</td>
      <td>zzyaTfPiwF</td>
      <td>1323</td>
    </tr>
    <tr>
      <th>3</th>
      <td>증권</td>
      <td>E뉴스</td>
      <td>zZwZozan2n</td>
      <td>84</td>
    </tr>
    <tr>
      <th>4</th>
      <td>부동산</td>
      <td>B일보</td>
      <td>ZZtYZSM0Sn</td>
      <td>264</td>
    </tr>
    <tr>
      <th>5</th>
      <td>경제</td>
      <td>B일보</td>
      <td>zzrgXrpELg</td>
      <td>260</td>
    </tr>
    <tr>
      <th>6</th>
      <td>사설</td>
      <td>C일보</td>
      <td>ZzozRX0bQZ</td>
      <td>649</td>
    </tr>
    <tr>
      <th>7</th>
      <td>정치</td>
      <td>D일보</td>
      <td>ZzMXGgLSs1</td>
      <td>741</td>
    </tr>
    <tr>
      <th>8</th>
      <td>부동산</td>
      <td>D일보</td>
      <td>ZZMGwKlPEf</td>
      <td>593</td>
    </tr>
    <tr>
      <th>9</th>
      <td>사회</td>
      <td>B일보</td>
      <td>ZzidNNbuC2</td>
      <td>1606</td>
    </tr>
    <tr>
      <th>10</th>
      <td>스포츠</td>
      <td>B일보</td>
      <td>zziciGuWlK</td>
      <td>920</td>
    </tr>
    <tr>
      <th>11</th>
      <td>경제</td>
      <td>B일보</td>
      <td>ZZiBYbV7ZT</td>
      <td>2594</td>
    </tr>
    <tr>
      <th>12</th>
      <td>사설</td>
      <td>B일보</td>
      <td>ZZH1bm0lEt</td>
      <td>372</td>
    </tr>
    <tr>
      <th>13</th>
      <td>사회</td>
      <td>B일보</td>
      <td>zzeSAhr63k</td>
      <td>219</td>
    </tr>
    <tr>
      <th>14</th>
      <td>연예</td>
      <td>B일보</td>
      <td>zZe7GukJir</td>
      <td>89</td>
    </tr>
    <tr>
      <th>15</th>
      <td>스포츠</td>
      <td>C일보</td>
      <td>dnasidl2</td>
      <td>392</td>
    </tr>
    <tr>
      <th>16</th>
      <td>경제</td>
      <td>C일보</td>
      <td>apsADN23</td>
      <td>49</td>
    </tr>
    <tr>
      <th>17</th>
      <td>사회</td>
      <td>C일보</td>
      <td>QZAPD2edl</td>
      <td>503</td>
    </tr>
    <tr>
      <th>18</th>
      <td>정치</td>
      <td>C일보</td>
      <td>Zzdia23</td>
      <td>234</td>
    </tr>
    <tr>
      <th>19</th>
      <td>사설</td>
      <td>C일보</td>
      <td>ZxkqweK3B</td>
      <td>68</td>
    </tr>
  </tbody>
</table>
</div>

```python
# heatmap을 사용하기 위해서는 피벗 테이블 형태로 변환해야함
click_pivot = pd.pivot_table(click_data, index='category', columns='Journal', values='num_click')  # (데이터프레임, 인덱스, 컬럼, 값)
display(click_pivot)
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Journal</th>
      <th>B일보</th>
      <th>C일보</th>
      <th>D일보</th>
      <th>E뉴스</th>
    </tr>
    <tr>
      <th>category</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>경제</th>
      <td>1427.000000</td>
      <td>49.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>공학</th>
      <td>NaN</td>
      <td>1323.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>부동산</th>
      <td>264.000000</td>
      <td>NaN</td>
      <td>593.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>사설</th>
      <td>372.000000</td>
      <td>642.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>사회</th>
      <td>688.666667</td>
      <td>503.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>스포츠</th>
      <td>920.000000</td>
      <td>392.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>연예</th>
      <td>89.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>정치</th>
      <td>NaN</td>
      <td>234.0</td>
      <td>741.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>증권</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>84.0</td>
    </tr>
  </tbody>
</table>
</div>

```python
# 히트맵 생성
plt.figure(figsize=(5, 2))
sns.heatmap(click_pivot)
plt.title('Heatmap of Click Numbers', fontsize=15)
plt.show()
```

<img width="832" alt="seaborn10" src="https://github.com/zacinthepark/TIL/assets/86648892/9fa466e2-490b-42fa-a895-6ae6b25b3d38">

```python
# 히트맵 옵션 부여

plt.figure(figsize=(5, 2))
sns.heatmap(click_pivot, # 데이터셋
            cbar=True, # 그래프 우측 컬러바 표기 여부
            linewidths=0.5, # cell 사이의 간격 설정
            annot=False, # 히트맵 빈도수 표기
            cmap='Blues' # 히트맵 색상 설정
           )
plt.title('Heatmap of Click Numbers', fontsize=15)
plt.show()
```

<img width="833" alt="seaborn11" src="https://github.com/zacinthepark/TIL/assets/86648892/4a37a56d-81ec-488e-8f3e-88b99626f9a1">
