# CSS Selector

- CSS 셀렉터는 CSS 스타일을 적용시킬 HTML 엘리먼트를 찾기 위한 방법입니다.

## 1. Element Selector

- 엘리먼트를 이용하여 선택할때 사용

- css selector로 `div`를 사용하면 가장 위에 있는 dss1이 선택

```
<div>dss1</div>

<p>dss2</p>

<span>dss3</span>
```

## 2. ID Selector

- 아이디를 이용하여 선택할때 사용

- 아이디를 셀렉할때는 `#(아이디 이름)`으로 선택

- css selector로 `#ds2`를 사용하면 dss2가 선택

- 여러개를 셀렉할때는 ,로 구분

- css selector로 `#ds2, #ds3`를 사용하면 dss2와 dss3가 선택

```
<p id="ds1">dss1</p>

<p id="ds2">dss2</p>

<p id="ds3">dss3</p>
```

## 3. Class Selector

- 클래스를 이용하여 선택할때 사용

- 클래스를 셀렉할때는 `.(클래스 이름)`으로 선택

- 엘리멘트를 그룹핑하여 스타일을 적용할때 사용

- css selector로 `.ds2`를 사용하면 dss2, dss3가 선택

```
<p class="ds1">dss1</p>

<p class="ds2">dss2</p>

<p class="ds2">dss3</p>
```

```python
# attr 이용하여 선택 : tag, id, class 선택 제외
# data2 선택 : [data='no1']
# <p value='no1' data='no1'>data1</p>
# <p value='no2'>data2</p>
```

## 4. not Selector

- 셀렉터로 엘리먼트를 하나만 제거하고 싶을때 사용

- not을 사용하여 셀렉트 할때에는 `:not(선택에서 제거하고 싶은 셀렉터)`으로 선택

- 아래의 HTML에서 `.ds:not(.ds2)`으로 셀렉트 하면 class가 ds2인 클래스를 제외 하고 나머지 ds1, ds3, ds4, ds5가 선택

```
<p class="ds ds1">ds1</p>

<p class="ds ds2">ds2</p>

<p class="ds ds3">ds3</p>

<p class="ds ds4">ds4</p>

<p class="ds ds5">ds5</p>
```

## 5. first-child Selector

- 엘리먼트로 감싸져있는 가장 처음 엘리먼트가 설정한 셀렉터와 일치하면 선택

- `.ds:first-child`로 설정하면 ds1과 ds3가 선택

- `nth-child(1)`과 동일하다고 생각

```
<body>

    <p class="ds" id="ds1">ds1</p>

    <p class="sc" id="ds2">ds2</p>



    <div class="ds">

        <p class="ds ds1">ds3</p>

        <p class="ds ds2">ds4</p>

        <p class="ds ds3">ds5</p>

        <p class="ds ds4">ds6</p>

        <p class="ds ds5">ds7</p>

    </div>

</body>
```

- `div.ds` 엘리먼트의 가장 처음 `.ds`를 선택하고 싶으면 `div.ds > .ds:first-child`로 셀렉터를 작성

## 6. last-child Selector

- 엘리먼트로 감싸져있는 가장 마지막 엘리먼트가 설정한 셀렉터와 일치하면 선택

- 하위 엘리먼트에서 가장 마지막 엘리먼트를 선택

- `.ds:last-child`로 `div.ds`가 선택되어 ds3~ds7이 선택

```
<body>

    <p class="ds" id="ds1">ds1</p>

    <p class="sc" id="ds2">ds2</p>



    <div class="ds">

        <p class="ds ds1">ds3</p>

        <p class="ds ds2">ds4</p>

        <p class="ds ds3">ds5</p>

        <p class="ds ds4">ds6</p>

        <p class="ds ds5">ds7</p>

    </div>

</body>
```

## 7. nth-child Selector

- 엘리먼트로 감싸져있는 n번째 엘리먼트가 설정한 셀렉터와 일치하면 선택

- `.ds:nth-child(3), .ds:nth-child(4)`로 설정하면 ds4, ds5가 선택

- `.p:nth-child(3)`로 설정하면 ds5가 아닌 ds4가 선택
    - 처리 순서가 (1) `nth-child(3)`, (2) 해당 엘리먼트가 `p` 인지 판단
    - p가 아니라면 값이 없음

- `nth-child`의 ()안의 숫자는 가장 첫번째가 0이 아니라 1로 시작

```
<div class="wrap">

    <span class="ds">ds2</span>

    <p class="ds ds1">ds3</p>

    <p class="ds ds2">ds4</p>

    <p class="ds ds3">ds5</p>

    <p class="ds ds4">ds6</p>

    <p class="ds ds5">ds7</p>

</div>
```

## 8. 모든 하위 depth(공백) Selector

- 공백문자로 하위 엘리먼트를 셀렉트 했을때, 모든 하위 엘리먼트를 선택

- `.contents h1`를 선택하면 inner_1, inner_2가 선택

```
<div class="contents">

    <h1>inner_1</h1>

    <div class="txt">

        <h1>inner_2</h1>

    </div>

</div>
```

## 9. 바로 아래 depth(>) Selector

- `>`문자로 하위 엘리먼트를 셀렉트 했을때, 바로 아래 엘리먼트를 선택

- `.contents > h1`를 선택하면 inner_1이 선택

```
<div class="contents">

    <h1>inner_1</h1>

    <div class="txt">

        <h1>inner_2</h1>

    </div>

</div>
```

```python
# 하나의 엘리먼트 선택
# tag : div
# id : #data
# class : .data
# attr : [value='no1']
```

```python
# .data:not(.data1) : data 클래스 모두에서 data1 클래스 엘리먼트 제외
# .data:nth-child(3) : 3번째 하위 엘리먼트에서 .data 클래스 가진 엘리먼트 선택
```

```python
# 공백 : #data .btn : data 아이디 하위의 모든 btn 클래스 엘리먼트를 선택
# > : #data > .btn : data 아이디 한단계 하위의 btn 클래스 엘리먼트를 선택
```

```python
# .d1, .d2 : d1, d2 클래스 둘다 선택
```

```python
#_SECTION_HEADLINE_LIST_jxnlh > li:nth-child(2) > div > div > div.sa_text > a > strong
```
