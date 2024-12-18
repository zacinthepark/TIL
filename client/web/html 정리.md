# HTML

## 1. HTML 이란?

- HTML은 Hyper Text Markup Language의 약자로 웹 문서를 작성하는 마크업 언어 입니다.

## 2. HTML 구성 요소

- Document : 한페이지를 나타내는 단위

- Element : 하나의 레이아웃을 나타내는 단위 : 시작태그, 끝태그, 텍스트로 구성

- Tag : 엘리먼트의 종류를 정의 : 시작태그(속성값), 끝태그

- Attribute : 시작태그에서 태그의 특정 기능을 하는 값

    - id : 웹 페이지에서 유일한 값
    - class : 동일한 여러개의 값 사용 가능 : element를 그룹핑 할때 사용
    - attr : id와 class를 제외한 나머지 속성들

- Text : 시작태그와 끝태그 사이에 있는 문자열

- 엘리먼트는 서로 계층적 구조를 가질수 있습니다.

```python
# spacial command : ipython에서 제공하는 특별한 기능을 갖는 명령어
# %(하나의 명령어로 실행), %%(셀 전체를 명령어로 실행)
```

```python
data1, data2 = 1, 'py'
```

```python
%whos
```

<pre>
Variable   Type    Data/Info
----------------------------
data1      int     1
data2      str     py
</pre>

```python
data = [1, 2]
```

```python
%%html
<!-- comment -->
<div id='contents' class='wrap'>
    <button class='btn no1' type='button' value='1'>Btn1</button>
    <button class='btn no2' type='button' value='2'>Btn2</button>
</div>
```

<!-- comment -->
<div id='contents' class='wrap'>
    <button class='btn no1' type='button' value='1'>Btn1</button>
    <button class='btn no2' type='button' value='2'>Btn2</button>
</div>

## 3. HTML 구조

- DOCTYPE
  - 문서의 종류를 선언하는 태그 입니다.

- html

  - head
    - meta
      - 웹페이지에 대한 정보를 넣습니다.

    - title
      - 웹페이지의 제목 정보를 넣습니다.

  - body
    - 화면을 구성하는 엘리먼트가 옵니다.

```

<!-- HTML 웹문서의 기본적인 구조 -->

<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="utf-8">

    <title></title>

</head>

<body>



</body>

</html>
```

### 4. HTML  태그

- html에서 문자를 나타내는 태그들

### 4.1 head

- title을 나타낼때 사용

- Head는 총 6가지 종류의 태그가 있습니다.(h1~h6)

- 숫자가 커질수록 문자의 크기가 줄어듭니다.

```python
%%html
<h1>Title</h1>
<h3>Title</h3>
```

<h1>Title</h1>
<h3>Title</h3>

### 4.2 p

- 한줄의 문자열을 출력하기 위한 태그

```python
%%html
<p>html1</p>
<p>html2</p>
```

<p>html1</p>
<p>html2</p>

### 4.3 span

- 한블럭의 문자열을 표현하기 위한 태그

```python
%%html
<span>html1</span>
<span>html2</span>
```

<span>html1</span>
<span>html2</span>

### 4.4 pre

- 줄바꿈이나 띄어쓰기가 적용되는 태그

```python
%%html
<pre>
    html1
    html2
</pre>
```

<pre>
    html1
    html2
</pre>

### 4.5 code

- 코드를 작성하는 태그
- 들여쓰기나 두칸 이상의 공백은 적용이 안됩니다.

```python
%%html
<code>
    html1
    html2
</code>
```

<code>
    html1
    html2
</code>

## 5. 문자 이외의 HTML 태그

### 5.1 div

- 레이아웃을 나타내는 태그

```python
%%html
<div>
    <div>div1</div>
    <div>div2</div>
</div>
<div>div3</div>
```

<div>
    <div>div1</div>
    <div>div2</div>
</div>
<div>div3</div>

### 5.2 table

- 로우와 컬럼이 있는 테이블 모양을 나타낼때 사용하는 태그

```python
%%html
<table>
    <caption>테이블제목</caption>
    <thead>
        <tr>
            <th>table1</th>
            <th>table2</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>data1</td>
            <td>data2</td>
        </tr>
        <tr>
            <td>data3</td>
            <td>data4</td>
        </tr>
    </tbody>
</table>
```

<table>
    <caption>테이블제목</caption>
    <thead>
        <tr>
            <th>table1</th>
            <th>table2</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>data1</td>
            <td>data2</td>
        </tr>
        <tr>
            <td>data3</td>
            <td>data4</td>
        </tr>
    </tbody>
</table>

### 5.3 ul, li

- 리스트를 나타내는 태그

```python
%%html
<ul>
    <li>data1</li>
    <li>data2</li>
</ul>
```

<ul>
    <li>data1</li>
    <li>data2</li>
</ul>

### 5.4 a

- 링크를 나타내는 태그

- href 속성에 url을 넣습니다.
  - url과 상대경로를 모두 사용 가능
  - `target="_blank"`는 링크를 열때 새탭에서 열도록 하는 기능이 있습니다.

```python
%%html
<a href='https://kt.com' target='_blank'>Move KT</a>
```

<a href='https://kt.com' target='_blank'>Move KT</a>

### 5.5 image

- 이미지를 나타내는 태그

```python
%%html
<img src='https://cfm.kt.com/images/v2/layout/gnb-ktlogo.png' alt='kt logo'></img>
```

<img src='https://cfm.kt.com/images/v2/layout/gnb-ktlogo.png' alt='kt logo'></img>

### 5.4 iframe

- 외부 url 링크 페이지를 보여주기 위한 엘리먼트
- 모든 웹 페이지를 보여줄 수 있는 것은 아니고 iframe으로만 출력이 되거가 안되거나 하는 등의 설정을 할 수 있습니다.
- 웹사이트에서 데이터가 안불러와진다면 해당 부분이 iframe인지 확인하고, iframe이라면 iframe에 해당하는 url을 사용합니다.

```python
%%html
<iframe src='https://kt.com' width='100%' height='200px'></iframe>
```

![z123123](https://github.com/zacinthepark/TIL/assets/86648892/ed5d78e2-e51e-4420-a53f-7702c7f10b54)

### 5.5 input

#### 5.5.1 text

- 문자열을 입력받을때 사용하는 input 타입

```python
%%html
<input type='text' placeholder='이메일'></input>
```

<input type='text' placeholder='이메일'></input>

#### 5.5.2 password

- 비밀번호를 입력받을때 사용하는 input 타입

```python
%%html
<input type='password' placeholder='비밀번호'></input>
```

<input type='password' placeholder='비밀번호'></input>

#### 5.5.3 radio

- 여러개의 버튼중에서 한개의 버튼만 체크되는 버튼
- radio 버튼은 name 속성값으로 그룹핑을 합니다.

```python
%%html
<input type='radio' name='no1'>btn 1</input>
<input type='radio' name='no1'>btn 2</input>
<input type='radio' name='no2'>btn 3</input>
<input type='radio' name='no2'>btn 4</input>
```

<input type='radio' name='no1'>btn 1</input>
<input type='radio' name='no1'>btn 2</input>
<input type='radio' name='no2'>btn 3</input>
<input type='radio' name='no2'>btn 4</input>

#### 5.5.4 checkbox

- 여러개의 버튼이 체크되는 버튼

```python
%%html
<input type='checkbox' name='no1'>btn 1</input>
<input type='checkbox' name='no1'>btn 2</input>
```

<input type='checkbox' name='no1'>btn 1</input>
<input type='checkbox' name='no1'>btn 2</input>

#### 5.5.5 select, option

- 옵션선택을 할수 있는 드랍다운 태그

```python
%%html
<select>
    <option>opt1</option>
    <option>opt2</option>
    <option>opt3</option>
</select>
```

<select>
    <option>opt1</option>
    <option>opt2</option>
    <option>opt3</option>
</select>

### 5.6 textarea

- 여러줄을 입력이 가능한 태그

```python
%%html
<textarea rows='4' cols='50'></textarea>
```

<textarea rows='4' cols='50'></textarea>
