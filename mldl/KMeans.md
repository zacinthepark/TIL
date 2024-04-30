## Clustering (군집화)

---

### 클러스터링이란

`클러스터링(Clustering) = 군집화 = 군집분석`

- 비지도학습의 일종으로 class 정보(label)없이 속성 정보(feature, 독립변수)만으로 유사한 속성을 가진 객체들을 군집으로 묶어주는 데이터마이닝 기법
    - 군집 간 분산 최대화: 서로 다른 군집 간에는 멀리 떨어져있어야함
    - 군집 내 분산 최소화: 같은 군집 내에서는 잘 뭉쳐져있어야함

- 유사성 척도
    - 거리(distance) 척도: 값이 작을수록 두 객체가 유사함
        - 유클리디안 거리: 가장 일반적인 거리 척도
        - 민코프스키 거리: 유클리디안 거리의 일반화 방법
    - 상관계수(correlation) 척도: 값이 클수록 두 객체가 유사함

### 클러스터링 종류

#### 1. 중심기반 클러스터링

동일 클러스터에 속하는 객체는 특정 중심을 기준으로 분포할 것이라는 기본 전제 &rarr; 클러스터의 모양이 원의 형태로 형성 (단, 계층적의 경우 다른 분포를 잡아내기도함)

> 1-1. 계층적 클러스터링

- 유사도가 높은 객체들을 단계적으로 묶어나가는 방식
- 사전에 군집 수(k)를 정하지 않고 단계적으로 군집 트리를 제공
- **Agglomerative Clustering**

> 1-2. 비계층적 클러스터링 (분할적 클러스터링)

- 전체 객체들을 한 번에 군집화하는 방법
- 사전에 군집 수 정의가 필요하며 임의의 초기값에 따라서 결과가 달라짐
- 데이터 분포가 특이할 경우 군집이 잘 이루어지지 않음
- 단순하며 계산 복잡성이 낮음
- **KMeans Clustering**

#### 2. 밀도기반 클러스터링

동일 클러스터에 속하는 객체는 서로 근접하게 분포할 것이라는 기본 전제 &rarr; 불특정한 모양의 클러스터 형성

- 객체가 세밀하게 몰려 있어서 밀도가 높은 부분을 군집화하는 방식
- 군집 수 지정이 미필요하며, 불특정 모양의 군집도 발견 가능
- 잡음(noise)의 분류가 가능하며, 이상치에 의해 군집화 성능이 하락하는 것을 방지
- **DBSCAN(Density-Based Spatial Clustering of Applications with Noise) Clustering**

## KMeans Clustering

---

> 거리 기반 군집화: 군집 중심점(centroid)이라는 특정한 임의의 지점을 선택해 해당 중심에 가장 가까운 포인트들을 선택해 군집화하는 방식

> 수행<br>
> 1: 군집 중심점을 임의의 위치에 놓는다. (일반적으로 초기화 알고리즘으로 적합한 위치에 놓기)<br>
> 2: 각 데이터는 가장 가까운 곳에 위치한 중심점에 소속된다.<br>
> 3: 군집 중심점을 소속된 데이터의 평균 중심으로 이동한다.<br>
> 4: 각 데이터는 기존에 속한 중심점보다 더 가까운 중심점이 있다면 해당 중심점으로 다시 소속을 변경한다.<br>
> 5: 다시 중심을 소속된 데이터의 평균으로 이동한다.<br>
> 6: 중심점을 이동했는데 데이터의 중심점 소속 변경이 없으면 군집화를 종료한다.<br>

- 장점
    - 일반적으로 가장 많이 사용되는 알고리즘으로 쉽고 간결함

- 단점
    - 속성의 개수가 많을 경우 군집화 정확도가 떨어짐 (PCA가 필요할 수도 있음)
    - 반복이 많을수록 수행시간이 느려짐
    - 몇 개의 군집을 선택할지 가이드하기 어려움
    - 개별 군집 내의 데이터가 원형으로 흩어져 있는 경우에 효과적으로 군집화가 수행될 수 있지만, 데이터가 길쭉한 타원형으로 늘어선 경우와 같을 떄는 군집화를 잘 수행하지 못함

- 하이퍼파라미터
    - `n_clusters`: 군집화할 개수 (군집 중심점의 개수)
    - `init`: 초기에 군집 중심점의 좌표를 설정할 방식 (보통 임의로 설정하지 않고 `k-means++` 방식으로 설정)
        - 임의로 설정하고 싶다면 `init='random'`
        - `k-means++`
            - 1. 데이터포인트 중에서 무작위로 1개를 선택하여 중심점으로 지정
            - 2. 나머지 데이터포인트들에 대해 첫번째 중심점까지의 거리 계산
            - 3. 지정된 중심점으로부터 가장 멀리있는 데이터포인트를 다음 중심점으로 지정
            - 4. 중심점이 k개가 될 때까지 2, 3번 반복
    - `max_iter`: 최대 반복 횟수 (이 횟수 이전에 모든 데이터의 중심점 이동이 없으면 종료)
    - `random_state`

- 속성
    - `labels_`: 각 데이터포인트가 속한 군집중심점 레이블
    - `cluster_centers_`: 각 군집중심점 좌표
        - shape은 `[cluster개수, feature개수]`
        - 이를 이용해 시각화 가능

### 1. KMeans

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import scale
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

import warnings
warnings.filterwarnings('ignore')
```

```python
iris = load_iris()
# 편리한 data handling을 위해 DataFrame으로 변환
iris_df = pd.DataFrame(data=iris.data, columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])
iris_df.head(5)
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5.1</td>
      <td>3.5</td>
      <td>1.4</td>
      <td>0.2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.9</td>
      <td>3.0</td>
      <td>1.4</td>
      <td>0.2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.7</td>
      <td>3.2</td>
      <td>1.3</td>
      <td>0.2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.6</td>
      <td>3.1</td>
      <td>1.5</td>
      <td>0.2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5.0</td>
      <td>3.6</td>
      <td>1.4</td>
      <td>0.2</td>
    </tr>
  </tbody>
</table>
</div>

```python
kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=300, random_state=0)
kmeans.fit(iris_df)

iris_df['target'] = iris.target
iris_df['cluster'] = kmeans.labels_
iris_df.head(5)
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
      <th>target</th>
      <th>cluster</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5.1</td>
      <td>3.5</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.9</td>
      <td>3.0</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.7</td>
      <td>3.2</td>
      <td>1.3</td>
      <td>0.2</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.6</td>
      <td>3.1</td>
      <td>1.5</td>
      <td>0.2</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5.0</td>
      <td>3.6</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>

```python
iris_result = iris_df.groupby(['target', 'cluster'])['sepal_length'].count()
print(iris_result)
```

<pre>
target  cluster
0       1          50
1       0          48
        2           2
2       0          14
        2          36
Name: sepal_length, dtype: int64
</pre>

```python
# iris 4개의 속성을 2차원 평면에 그리기 위해 PCA로 2개로 차원 축소
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
pca_transformed = pca.fit_transform(iris.data)

iris_df['pca_x'] = pca_transformed[:, 0]
iris_df['pca_y'] = pca_transformed[:, 1]

# cluster 값이 0, 1, 2인 경우마다 별로의 index로 추출
marker0_ind = iris_df[iris_df['cluster'] == 0].index
marker1_ind = iris_df[iris_df['cluster'] == 1].index
marker2_ind = iris_df[iris_df['cluster'] == 2].index

# cluster값 0, 1, 2에 해당하는 index로 각 cluster 레벨의 pca_x, pca_y 값 추출
plt.scatter(x=iris_df.loc[marker0_ind, 'pca_x'], y=iris_df.loc[marker0_ind, 'pca_y'], marker='o')
plt.scatter(x=iris_df.loc[marker1_ind, 'pca_x'], y=iris_df.loc[marker1_ind, 'pca_y'], marker='s')
plt.scatter(x=iris_df.loc[marker2_ind, 'pca_x'], y=iris_df.loc[marker2_ind, 'pca_y'], marker='^')

plt.xlabel('PCA 1')
plt.ylabel('PCA 2')
plt.title('3 Clusters Visualization by 2 PCA Components')
plt.show()
```

<p align="center">
  <img width="500" alt="z_kmeans_1" src="https://github.com/zacinthepark/TIL/assets/86648892/17d45982-db95-4b5b-9f62-97aa50ae5274">
</p>

### 2. 군집화 알고리즘 테스트를 위한 데이터 생성

- `make_blobs()`: Feature 데이터, Target 데이터 생성
    - `n_samples`: 생성할 총 데이터 개수 (default=100)
    - `n_features`: 데이터의 feature 개수
    - `centers`: 군집의 개수
    - `cluster_std`: 생성될 군집 데이터의 표준편차
        - `float`으로 입력
        - `[float, ...]`으로 입력 시 각 군집의 순서대로 각각의 표준편차가 만들어짐

- `make_classification()`: 노이즈를 포함한 데이터 생성
- `make_circle(), make_moon()`: 중심기반의 군집화로 해결하기 어려운 데이터 생성

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# 테스트 데이터 생성
X, y = make_blobs(n_samples=200, n_features=2, centers=3, cluster_std=0.8, random_state=0)
print(X.shape, y.shape)
```

<pre>
(200, 2) (200,)
</pre>

```python
# y target 값의 분포를 확인
unique, counts = np.unique(y, return_counts=True)
print(unique, counts)
```

<pre>
[0 1 2] [67 67 66]
</pre>

```python
# DataFrame 생성
cluster_df = pd.DataFrame(data=X, columns=['ftr1', 'ftr2'])
cluster_df['target'] = y

target_list = np.unique(y)  # 3개의 cluster 영역으로 구분한 데이터셋을 생성했으므로 [0, 1, 2]
markers = ['o', 's', '^', 'P', 'D', 'H', 'x']

for target in target_list:
    target_cluster = cluster_df[cluster_df['target'] == target]
    plt.scatter(x=target_cluster['ftr1'], y=target_cluster['ftr2'], edgecolor='k', marker=markers[target])

plt.show()
```

<p align="center">
  <img width="500" alt="z_kmeans_2" src="https://github.com/zacinthepark/TIL/assets/86648892/445f5bf0-e27f-4f62-b5ba-513daab7656a">
</p>

#### KMeans 객체를 이용하여 X 데이터를 KMeans 클러스터링 수행 후 시각화

```python
kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=200, random_state=0)
cluster_labels = kmeans.fit_predict(X)
cluster_df['kmeans_label'] = cluster_labels

# cluster_centers_: 개별 클러스터의 중심 위치 좌표, 시각화를 위해 추출
centers = kmeans.cluster_centers_
unique_labels = np.unique(cluster_labels)
markers=markers = ['o', 's', '^', 'P', 'D', 'H', 'x']

# 군집된 label 유형별로 iteration하면서 marker별로 scatterplot
for label in unique_labels:
    label_cluster = cluster_df[cluster_df['kmeans_label'] == label]
    center_x_y = centers[label]
    plt.scatter(x=label_cluster['ftr1'], y=label_cluster['ftr2'], edgecolor='k', marker=markers[label])
    
    # 군집별 중심 위치 좌표 시각화
    plt.scatter(x=center_x_y[0], y=center_x_y[1], s=200, color='white', alpha=0.9, edgecolor='k', marker=markers[label])
    plt.scatter(x=center_x_y[0], y=center_x_y[1], s=70, color='k', edgecolor='k', marker='$%d$' % label)

plt.show()

print(cluster_df.groupby('target')['kmeans_label'].value_counts())
```

<p align="center">
  <img width="500" alt="z_kmeans_3" src="https://github.com/zacinthepark/TIL/assets/86648892/84051d4a-91dc-4d47-8827-ec3287da997d">
</p>

<pre>
target  kmeans_label
0       0               66
        1                1
1       2               67
2       1               65
        2                1
Name: count, dtype: int64
</pre>

### 3. 군집 평가 (Cluster Evalution): 실루엣 분석

대부분의 군집화 데이터셋은 타깃 레이블을 가지고 있지 않다. 그래서 비지도 학습의 특성상 정확한 성능 평가는 어렵지만 군집화의 성능을 평가하는 방법으로 실루엣 분석이 있다.

#### Silhouette Analysis

> 각 군집 간의 거리가 얼마나 효율적으로 분리되어 있는가?

효율적 분리란 다른 군집과는 떨어져있고, 동일 군집끼리의 데이터는 서로 가깝게 잘 뭉쳐있는 것이다. 군집화가 잘될수록 개별 군집은 비슷한 정도의 여유 공간을 가지고 떨어져있다.

#### 실루엣 계수(silhouette coefficient)

$$\Large
s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}
$$

- 개별 데이터가 가지는 군집화 지표
- 해당 데이터가 같은 군집 내의 데이터와 얼마나 가깝게 군집화되어있고, 다른 군집에 있는 데이터와는 얼마나 멀리 분리되어있는지 나타내는 지표
- 개별 객체의 실루엣 계수를 확인하고, 클러스터별로 그 값의 분포에 문제가 없는지 확인하는 방식으로 유효성 검증
    - 해당 객체와 내부와의 거리가 짧을 수록, 해당 객체와 외부와의 거리가 길수록 값 증가
    - `-1 ~ 1` 사이의 값을 가짐
        - `객체와 내부 간의 거리 > 객체와 외부 간의 거리`일 경우 음수 값
    - 일반적으로 `0.5` 이상일 경우 군집화가 타당하다고 평가

<p align="center">
    <img width="500" alt="silhouette_coefficient" src="https://github.com/zacinthepark/TIL/assets/86648892/6d0e45f1-a5a2-452c-8b9c-8894c637345a">
</p>

- $a_{ij}$: i번째 데이터에서 **자신이 속한 클러스터 내** 의 **다른 데이터포인트** 까지의 거리
- $a(i)$: i번째 데이터에서 **자신이 속한 클러스터 내** 의 **다른 데이터포인트** 까지의 거리의 평균
    - `a(1) = avg(a12, a13, ...)`
- $b(i)$: i번째 데이터에서 **가장 가까운 타 클러스터 내** 의 **다른 데이터포인트** 까지의 거리의 평균
    - `b(1) = avg(b14, b15, ...)`
- $s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}$
    - `1`에 가까운 경우: $b(i) > a(i)$: 근처의 군집과 더 멀리 떨어져 있다는 것
    - `0`에 가까운 경우: $b(i) - a(i) = 0$: 클러스터 내 거리와 타 클러스터와의 거리의 차이가 없음: 근처의 군집과 가까워진다는 것
    - `-1`에 가까운 경우: $b(i) < a(i)$: 클러스터 내 거리가 타 클러스터와 거리보다 큼: 다른 군집 데이터가 할당됨

#### `sklearn` silhouette analysis

- `silhouette_samples(X, labels, metric='euclidean', **kwds)`: 각 데이터의 실루엣 계수를 계산하여 반환

- `silhoueete_score(X, labels, metric='euclidean', sample_size=None, **kwds)`: 전체 데이터의 실루엣 계수 값을 평균하여 반환
    - `np.mean(silhouette_samples())`와 같음
    - 일반적으로 이 값이 높을수록 군집화가 잘되었다고 판단할 수 있지만, 무조건 그런 것은 아님

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import scale
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score

import warnings
warnings.filterwarnings('ignore')
```

```python
iris = load_iris()
feature_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
iris_df = pd.DataFrame(data=iris.data, columns=feature_names)
kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=300, random_state=0).fit(iris_df)

iris_df['cluster'] = kmeans.labels_

# iris의 모든 개별 데이터의 실루엣 계수값을 구함
score_samples = silhouette_samples(iris.data, iris_df['cluster'])
print('silhouette samples shape: ', score_samples.shape)
print(np.mean(silhouette_samples(iris.data, iris_df['cluster'])))
print(silhouette_score(iris.data, iris_df['cluster']))
```

<pre>
silhouette samples shape:  (150,)
0.5528190123564095
0.5528190123564095
</pre>

```python
# iris_df에 실루엣 계수 컬럼 추가
iris_df['silhouette_coef'] = score_samples
# 모든 데이터의 평균 실루엣 계수값을 구함
total_sil_score = silhouette_score(iris.data, iris_df['cluster'])
print(f'Iris Dataset Silhouette Analysis Score: {total_sil_score}')
# 군집별 평균 실루엣 계수
print(iris_df.groupby('cluster')['silhouette_coef'].mean())
```

<pre>
Iris Dataset Silhouette Analysis Score: 0.5528190123564095
cluster
0    0.417320
1    0.798140
2    0.451105
Name: silhouette_coef, dtype: float64
</pre>

#### 군집별 평균 실루엣 계수의 시각화를 통한 군집 개수 최적화

- 전체 실루엣 계수의 평균값이 0~1 사이의 값을 가지며, 1에 가까울수록 좋음
- 전체 실루엣 계수의 평균값과 더불어, 개별 군집의 평균값의 편차가 크지 않아야함
- 즉, 개별 군집의 실루엣 계수 평균값이 전체 실루엣 계수 평균값에서 크게 벗어나지 않는 것이 좋음

```python
# 여러 개의 클러스터링 개수를 list로 입력받아 각각의 실루엣 계수를 면적으로 시각화
def visualize_silhouette(cluster_lists, X_features):
    from sklearn.cluster import KMeans
    from sklearn.metrics import silhouette_samples, silhouette_score
    
    import matplotlib.pyplot as plt
    import matplotlib.cm as cm
    
    # 입력값으로 클러스터링 개수들을 리스트로 받아서, 각 개수별로 클러스터링을 적용하고 실루엣 계수를 구함
    n_cols = len(cluster_lists)
    
    # subplots
    fig, axs = plt.subplots(figsize=(4 * n_cols, 10), nrows=2, ncols=n_cols)
    
    # 실루엣 계수 시각화
    for ind, n_cluster in enumerate(cluster_lists):
        # KMeans 클러스터링 수행, 실루엣 스코어와 개별 데이터의 실루엣 값 계산
        clusterer = KMeans(n_clusters=n_cluster, max_iter=500, random_state=0)
        cluster_labels = clusterer.fit_predict(X_features)
        centers = clusterer.cluster_centers_
        
        sil_avg = silhouette_score(X_features, cluster_labels)
        sil_values = silhouette_samples(X_features, cluster_labels)
        
        y_lower = 10
        # plot 틀 잡기
        axs[0, ind].set_title('Number of Cluster: ' + str(n_cluster) + '\n' + 'Silhouette Score: ' + str(round(sil_avg, 3)))
        axs[0, ind].set_xlabel('Silhouette Coef Values')
        axs[0, ind].set_ylabel('Cluster Label')
        axs[0, ind].set_xlim([-0.1, 1])
        axs[0, ind].set_ylim([0, len(X_features) + (n_cluster+1) * 10])
        axs[0, ind].set_yticks([])  # clear the yaxis labels and ticks
        axs[0, ind].set_xticks([0, 0.2, 0.4, 0.6, 0.8, 1])
        
        # 클러스터링 개수별로 fill_betweenx() 형태의 막대 그래프 표현
        for i in range(n_cluster):
            i_cluster_sil_values = sil_values[cluster_labels == i]
            i_cluster_sil_values.sort()
            
            size_cluster_i = i_cluster_sil_values.shape[0]
            y_upper = y_lower + size_cluster_i
            
            color = cm.nipy_spectral(float(i) / n_cluster)
            axs[0, ind].fill_betweenx(np.arange(y_lower, y_upper), 0, i_cluster_sil_values, facecolor=color, edgecolor=color, alpha=0.7)
            axs[0, ind].text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))
            y_lower = y_upper + 10

            # 클러스터링된 데이터 시각화
            axs[1, ind].scatter(X_features[:, 0], X_features[:, 1], marker='.', s=30, lw=0, alpha=0.7, c=cluster_labels)
            axs[1, ind].set_title('Clustered Data')
            axs[1, ind].set_xlabel('Feature Space for the 1st Feature')
            axs[1, ind].set_ylabel('Feature Space for the 2nd Feature')
            
        # 군집별 중심 위치 좌표 시각화
        unique_labels = np.unique(cluster_labels)
        for label in unique_labels:
            center_x_y = centers[label]
            axs[1, ind].scatter(x=center_x_y[0], y=center_x_y[1], s=70, color='k', edgecolor='k', marker='$%d$' % label)
        
        axs[0, ind].axvline(x=sil_avg, color='red', linestyle='--')
```

```python
from sklearn.datasets import make_blobs
X, y = make_blobs(n_samples=500, n_features=2, centers=4, cluster_std=1, center_box=(-10.0, 10.0), shuffle=True, random_state=1)
visualize_silhouette([2, 3, 4, 5], X)
```

<p align="center">
  <img width="700" alt="z_kmeans_4" src="https://github.com/zacinthepark/TIL/assets/86648892/ad4a90cc-2268-4e94-8576-c08d97c4738a">
</p>

```python
iris = load_iris()
visualize_silhouette([2, 3, 4, 5], iris.data)
```

<p align="center">
  <img width="700" alt="z_kmeans_5" src="https://github.com/zacinthepark/TIL/assets/86648892/fb766fa9-bbc4-4553-912d-31b70bd787cf">
</p>
