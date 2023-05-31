## HTTP란?

---

Hypertext Transfer Protocol: 인터넷 상에서 클라이언트와 서버가 자원을 주고 받을 때 쓰는 통신 규약

### 클라이언트 → 서버 업로드 과정 이해하기

1. 파일 업로드를 구현할 때, 클라이언트가 웹 브라우저라면 폼을 통해서 파일을 등록해서 전송한다
2. 웹 브라우저가 보내는 HTTP 메시지는 `Content-Type` 속성이 `multipart/form-data` 로 지정되고 정해진 형식에 따라 메시지를 인코딩하여 전송한다
3. 이를 처리하기 위한 서버는 멀티파트 메시지에 대해서 각 파트 별로 분리하여 개별 파일의 정보를 얻게 된다

- 이미지 파일을 전송한다고 해서 이메일에 첨부파일을 붙여 메일을 보내는 것처럼 **png나 jpg 파일 자체가 전송되는 것이 아니다!**
- 이미지 파일도 문자로 이루어져 있기 때문에 **이미지 파일을 문자로 생성하여 HTTP request body에 담아 서버로 전송하는 것이다**

<img width="393" alt="request-structure" src="https://github.com/zacinthepark/TIL/assets/86648892/d78c1bfb-c630-46e5-b387-14bcf7c4737d">

- HTTP(request와 response)는 위 이미지와 같이 4개의 파트로 나눌 수 있다
- 여기서 Message Body에 들어가는 데이터 타입을 `HTTP Header`에 명시해줄 수 있다
- 이 때 명시할 수 있도록 해주는 필드가 바로 `Content-type` 이다
- 추가적으로 `Content-type` 필드에 MIME(Multipurpose Internet Mail Extensions) 타입을 기술해줄 수 있는데, 여러 타입 중 하나가 바로 `multipart` 이다

## `multipart` & `multipart/form-data`

---

### form이란?

form은 입력 양식 전체를 감싸는 태그이다

- `name`
    - form의 이름, 서버로 보내질 때 이름의 값으로 데이터 전송한다

- `action`
    - form이 전송되는 서버 url 또는 html 링크

- `method`
    - 전송 방법 설정, `get` 이 `default`

- `autocomplete`
    - 자동 완성
    - on으로 하면 form 전체에 자동 완성 허용

- `enctype`
    - 폼 데이터(form data)가 서버로 제출될 때 해당 데이터가 인코딩되는 방법을 명시한다
    - `<form>` 의 method 속성값이 `post` 인 경우에만 사용할 수 있음
    - `application/x-www-form-urlencoded`
        - default 값으로, 모든 문자들을 서버로 보내기 전에 인코딩됨을 명시한다
    - `text/plain`
        - 공백 문자(space)는 “+” 기호로 변환하지만, 나머지 문자는 모두 인코딩되지 않음을 명시한다
    - `multipart/form-data`
        - 모든 문자를 인코딩하지 않음을 명시한다
        - 이 방식은 `<form>` 요소가 **파일이나 이미지를 서버로 전송할 때 주로 사용한다**

```html
<form action="/home/uploadfiles" method="post" enctype="multipart/form-data">
    파일명 : <input type="file" name="myfile">
    <button type="submit">제출하기</button>
</form>
```

### Multipart가 생긴 배경

HTML의 input의 type 중 “file”이 있다 (`<input type=”file” />`)
- 파일 업로드를 위한 input 컨트롤, 즉 사용자 컴퓨터에서 서버로 파일을 전송하기 위한 input

form이 submit되면 form 안에 있는 컨트롤들의 데이터가 서버로 전송된다

이 때 이런 데이터들은 HTTP Request 형태로 서버로 전송된다

파일 업로드의 원리는 HTTP Request가 가지고 있는데, 그 원리는 다음과 같다
- HTTP Request는 Body에 클라이언트가 전송하려고 하는 데이터를 넣을 수 있다
- Body에 들어가는 데이터의 타입을 HTTP Header에 명시해줌으로써 서버가 타입에 따라 알맞게 처리하게 한다
- 이 Body의 타입을 명시하는 Header가 `Content-type` 이다

> 중요한 점은 보통 HTTP Request의 Body는 한 종류의 타입이 대부분이고, Content-type도 타입을 하나만 명시할 수 있다 ( ex. text이면 `text/plain` , xml이면 `text/xml` , jpg 이미지이면 `image/jpeg` 등)

일반적인 form의 submit에 의한 데이터들의 `Content-type` 은 `application/x-www-form-urlencoded` 이다

사진 설명과 사진을 올리는 파일 업로드 상황의 경우, 사진에 대한 설명을 위한 `input` 과 사진 파일을 위한 `input` 2개가 들어간다
- 그런데 두 `input` 간의 `Content-type` 이 전혀 다르다
- 두 `input` 의 `Content-type` 은 사진 설명의 경우 `application/x-www-form-urlencoded` , 사진 파일의 경우 `image/jpeg` 이다

이처럼 두 종류의 데이터가 하나의 `HTTP Request Body` 에 들어가야 하는데, 한 `Body` 에서 두 종류의 데이터를 구분해서 넣어주는 방법이 필요해졌고, 그래서 등장하는 것이 `multipart` 타입이다

## React + axios를 통한 이미지 업로드 예제

---

```html
<form
  name="photo"
  encType="multipart/form-data"
  onSubmit={handleSubmit}
>
  <input
    type="file"
    name="photo"
    accept="image/*,audio/*,video/mp4,video/x-m4v,application/pdf,application/vnd.ms-excel,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/vnd.ms-powerpoint,application/vnd.openxmlformats-officedocument.presentationml.presentation,.csv"
    onChange={handleUpload}
  />
    ...
```

- form이 제출될 때 어떤 형식인지 알려줌
- input에 필요한 이벤트 핸들러 작성
- 어떤 파일들이 올라갈지 `accept` 라는 attribute 지정

```jsx
const handleSubmit = async(event) => {
    event.preventDefault();
    const formData = new FormData();
    formData.append("photo", files.length && files[0].uploadedFile);
    formData.append("comment", commentValue);
    formData.append("content_id", classData.content_id);

   await axios({
      method: "post",
      url: process.env.REACT_APP_STREAMING_COMMENT_URL, //환경변수
      data: formData,
      headers: { "Content-Type": "multipart/form-data", Authorization: localStorage.getItem("access_token") }
    });
    setCommentValue("");
    setFiles([]);
  };

const handleUpload = (event) => {
  event.preventDefault();
  const file = event.target.files[0];
  setFiles([...files, { uploadedFile: file }]);
};
```

- method는 `POST` 로 설정
- file의 구성

```jsx
// event.target.files
fileList: {
  0: {name: file1, ...},
  length: 1,
  item: {...}
}
```

- `event.target.files[0]`
    - 우리가 필요한 것은 파일이기 때문에 0이라는 키에 접근
- form 태그는 a 태그와 마찬가지로 페이지를 reload 시키기에 먼저 `preventDefault()` 를 적용
- 새로운 FormData를 생성
- 백엔드에 보내기 위해 필요한 data들을 formData에 key, value 형태로 append
- data 키에 formData를 담아 axios 요청을 백엔드 API로 보냄
