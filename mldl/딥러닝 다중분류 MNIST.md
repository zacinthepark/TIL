## DNN MNIST

---

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.metrics import *
from sklearn.preprocessing import StandardScaler, MinMaxScaler

from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.backend import clear_session
from keras.optimizers import Adam
from keras.datasets import mnist, fashion_mnist
```

```python
# 학습곡선 함수
def dl_history_plot(history):
    plt.figure(figsize=(10, 6))
    plt.plot(history['loss'], label='train_err')
    plt.plot(history['val_loss'], label='val_err')

    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend()
    plt.grid()
    plt.show()
```

![mnist](https://wikidocs.net/images/page/60324/mnist.png)

```python
# 케라스 데이터셋으로 부터 mnist 불러오기
(x_train, y_train), (x_val, y_val) = mnist.load_data()
```

```python
# 28x28 데이터가 60000개
x_train.shape, y_train.shape
```

<pre>
((60000, 28, 28), (60000,))
</pre>

```python
class_names = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
```

```python
# 아래 숫자를 바꿔가며 화면에 그려보기
n = 20

plt.figure()
plt.imshow(x_train[n], cmap=plt.cm.binary)
plt.colorbar()
plt.show()
```

<img width="800" alt="z_dl_6_3_1" src="https://github.com/zacinthepark/TIL/assets/86648892/420b4f83-9e91-486f-bf05-3daf76d0cc98">

```python
# 픽셀을 나타냄
np.set_printoptions(threshold=np.inf, linewidth=np.inf)
print(x_train[n])
```

<pre>
[[  0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0  38 190  25   0   0   0   0   0   0   0   0]
 [  0   0   0  13  25  10   0   0   0   0   0   0   0   0   0   0   0 112 252 125   4   0   0   0   0   0   0   0]
 [  0   0   0 132 252 113   0   0   0   0   0   0   0   0   0   0   0  61 252 252  36   0   0   0   0   0   0   0]
 [  0   0   0 132 252 240  79   0   0   0   0   0   0   0   0   0   0  84 252 252  36   0   0   0   0   0   0   0]
 [  0   0   0 132 252 252 238  52   0   0   0   0   0   0   0   0  12 198 252 252 122   0   0   0   0   0   0   0]
 [  0   0   0  99 252 252 252 181  17   0   0   0   0   0   0   0  49 252 252 252 122   0   0   0   0   0   0   0]
 [  0   0   0   3 125 252 252 252 100   0   0   0   0   0   0   0  26 218 252 252  36   0   0   0   0   0   0   0]
 [  0   0   0   0  15 216 252 252 207  19   0   0   0   0   0   0  49 252 252 252  36   0   0   0   0   0   0   0]
 [  0   0   0   0   0 157 252 252 252  48   0   0   0   6 109 109 194 252 252 252  36   0   0   0   0   0   0   0]
 [  0   0   0   0   0 100 252 252 252 105   0  58 116 128 252 252 252 252 252 212  19   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0 164 253 253 253 253 253 253 255 253 253 253 253 253 253  99   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0  49 252 252 252 252 252 252 253 252 252 252 252 252 252 155   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0  49 252 252 252 252 252 252 217 216 141 126 252 252 252 155   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0  49 252 252 252 234 204  89   0   0   0  49 252 252 252 155   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0  14 158 192 151  45   0   0   0   0   0  49 252 252 252 225  17   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0  49 252 252 252 252  23   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0  33 228 252 252 252 157   4   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0  55 229 252 252 252  11   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0  53 232 252 252  63   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0  90 206 131  11   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0]]
</pre>

```python
plt.figure(figsize=(10, 10))
for i in range(25):
    plt.subplot(5, 5, i+1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(x_train[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[y_train[i]])
plt.tight_layout()
plt.show()
```

<img width="800" alt="z_dl_6_3_2" src="https://github.com/zacinthepark/TIL/assets/86648892/76653abe-fee4-4841-b989-27d5369ac585">

#### Flatten(reshape)하여 2차원 이미지 데이터 정보를 1차원으로 펼치기

![mnist_flatten](https://github.com/zacinthepark/TIL/assets/86648892/c811ee17-294e-4d57-9e44-cf7fdcd6229c)

```python
x_train.shape, y_train.shape, x_val.shape, y_val.shape
```

<pre>
((60000, 28, 28), (60000,), (10000, 28, 28), (10000,))
</pre>

```python
a = np.array([[1,2,3], [4,5,6]])
a, a.shape
```

<pre>
(array([[1, 2, 3],
        [4, 5, 6]]),
 (2, 3))
</pre>

```python
print(a.reshape(3, 2))
print(a.reshape(6, 1))
print(a.reshape(6, -1))
```

<pre>
[[1 2]
 [3 4]
 [5 6]]
[[1]
 [2]
 [3]
 [4]
 [5]
 [6]]
[[1]
 [2]
 [3]
 [4]
 [5]
 [6]]
</pre>

```python
# 28x28 픽셀 정보를 784개의 픽셀 정보를 하나의 행으로 나열하고, 이러한 데이터의 수가 60000개
x_train = x_train.reshape(60000, -1)
x_val = x_val.reshape(10000, -1)
```

```python
x_train.shape, x_val.shape
```

<pre>
((60000, 784), (10000, 784))
</pre>

#### Scaling

```python
# 픽셀값의 min은 0, max는 255

x_train = x_train / 255.
x_test = x_val / 255.
```

#### 모델링 1

```python
nfeatures = x_train.shape[1]
nfeatures
```

<pre>
784
</pre>

```python
clear_session()
m1 = Sequential(Dense(10, input_shape=(nfeatures,), activation='softmax'))
m1.summary()
```

<pre>
Model: "sequential"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 dense (Dense)               (None, 10)                7850      
                                                                 
=================================================================
Total params: 7850 (30.66 KB)
Trainable params: 7850 (30.66 KB)
Non-trainable params: 0 (0.00 Byte)
_________________________________________________________________
</pre>

```python
m1.compile(optimizer=Adam(learning_rate=0.001), loss='sparse_categorical_crossentropy')
history = m1.fit(x_train, y_train, epochs=10, validation_split=0.2, verbose=0).history
```

```python
dl_history_plot(history)
```

![z_dl_6_3_3](https://github.com/zacinthepark/TIL/assets/86648892/c8aafeb4-3074-4402-b9de-267e6754721b)

```python
p1 = m1.predict(x_test)
print(p1[:5])
p1 = p1.argmax(axis=1)
print('=' * 30)
print(p1[:5])
```

<pre>
313/313 [==============================] - 1s 2ms/step
[[6.1213689e-07 5.4348470e-12 3.0630583e-06 4.1739792e-03 2.1455712e-07 1.4020594e-05 5.9777617e-12 9.9528354e-01 1.1645395e-05 5.1294401e-04]
 [6.1537823e-05 8.1039543e-06 9.9669385e-01 3.1200907e-05 2.0535348e-14 3.4056720e-04 2.8311412e-03 1.1054121e-17 3.3678007e-05 2.1629168e-14]
 [1.3179980e-06 9.8372364e-01 9.6980147e-03 1.8401140e-03 1.3478285e-04 4.9117388e-04 7.5377926e-04 4.6265448e-04 2.6191243e-03 2.7540443e-04]
 [9.9971491e-01 5.1778467e-11 6.0950060e-05 3.5605483e-06 9.8143978e-08 5.8995494e-05 1.0766500e-04 2.1547996e-05 1.0438151e-05 2.1898039e-05]
 [2.2702945e-04 1.6186063e-07 1.3516279e-03 1.8734825e-05 9.6989495e-01 4.0381292e-05 1.3362439e-03 1.5765890e-03 3.2428969e-03 2.2311434e-02]]
==============================
[7 2 1 0 4]
</pre>

```python
print(confusion_matrix(y_val, p1))
print(classification_report(y_val, p1))
```

<pre>
[[ 959    0    0    2    1    6    9    2    1    0]
 [   0 1117    3    2    0    1    4    2    6    0]
 [   4   12  931   15   11    3   12   10   30    4]
 [   3    0   19  925    2   17    2   12   19   11]
 [   1    2    5    2  911    0    9    5    5   42]
 [   7    3    5   35   11  768   14    9   31    9]
 [   8    3    7    1    7   11  917    2    2    0]
 [   1    6   22    6    6    0    0  945    2   40]
 [   6   10    6   22    9   21    9   13  862   16]
 [   9    7    1    8   19    5    0   17    5  938]]
              precision    recall  f1-score   support

           0       0.96      0.98      0.97       980
           1       0.96      0.98      0.97      1135
           2       0.93      0.90      0.92      1032
           3       0.91      0.92      0.91      1010
           4       0.93      0.93      0.93       982
           5       0.92      0.86      0.89       892
           6       0.94      0.96      0.95       958
           7       0.93      0.92      0.92      1028
           8       0.90      0.89      0.89       974
           9       0.88      0.93      0.91      1009

    accuracy                           0.93     10000
   macro avg       0.93      0.93      0.93     10000
weighted avg       0.93      0.93      0.93     10000
</pre>

#### 모델링 2

```python
nfeatures = x_train.shape[1]
nfeatures
```

<pre>
784
</pre>

```python
m2 = Sequential([Dense(128, input_shape=(nfeatures,), activation='relu'),
                 Dense(64, activation='relu'),
                 Dense(16, activation='relu'),
                 Dense(10, activation='softmax')])
m2.summary()
```

<pre>
Model: "sequential_1"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 dense_1 (Dense)             (None, 128)               100480    
                                                                 
 dense_2 (Dense)             (None, 64)                8256      
                                                                 
 dense_3 (Dense)             (None, 16)                1040      
                                                                 
 dense_4 (Dense)             (None, 10)                170       
                                                                 
=================================================================
Total params: 109946 (429.48 KB)
Trainable params: 109946 (429.48 KB)
Non-trainable params: 0 (0.00 Byte)
_________________________________________________________________
</pre>

```python
m2.compile(optimizer=Adam(learning_rate=0.0001), loss='sparse_categorical_crossentropy')
hist = m2.fit(x_train, y_train, epochs=10, validation_split=.2, verbose=0).history
```

```python
dl_history_plot(hist)
```

![z_dl_6_3_4](https://github.com/zacinthepark/TIL/assets/86648892/5a227b9e-d2ba-42bf-a323-061cb2d31494)

```python
p2 = m2.predict(x_test)
p2 = p2.argmax(axis=1)
```

<pre>
313/313 [==============================] - 1s 2ms/step
</pre>

```python
print(confusion_matrix(y_val, p2))
print(classification_report(y_val, p2))
print(accuracy_score(y_val, p2))
```

<pre>
[[ 965    1    1    1    1    3    6    1    1    0]
 [   0 1117    3    3    0    1    5    1    5    0]
 [   5    1  999    7    2    1    5    6    6    0]
 [   0    0    7  981    0    8    0    3    8    3]
 [   2    0    2    0  955    0    7    2    1   13]
 [   5    0    0    7    1  861    8    1    5    4]
 [   7    3    1    0    5    7  932    0    3    0]
 [   2    8   13    8    1    1    0  983    0   12]
 [   6    0    4   16    4   12   10    5  915    2]
 [  10    5    0   10   12    5    1    9    3  954]]
 
              precision    recall  f1-score   support

           0       0.96      0.98      0.97       980
           1       0.98      0.98      0.98      1135
           2       0.97      0.97      0.97      1032
           3       0.95      0.97      0.96      1010
           4       0.97      0.97      0.97       982
           5       0.96      0.97      0.96       892
           6       0.96      0.97      0.96       958
           7       0.97      0.96      0.96      1028
           8       0.97      0.94      0.95       974
           9       0.97      0.95      0.96      1009

    accuracy                           0.97     10000
   macro avg       0.97      0.97      0.97     10000
weighted avg       0.97      0.97      0.97     10000

0.9662
</pre>
