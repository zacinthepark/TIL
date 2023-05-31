## Access Token의 문제점

---

### 사용자의 잦은 로그아웃 경험

Access Token만을 사용하여 사용자를 인증할 경우, 토큰의 유효 기간을 길게 한다면 보안 문제가 발생할 수 있다. 이로 인해 유효 기간을 짧게 한다면, 사용자는 잦은 로그아웃 경험을 하게 될 것이다.

### 보안 문제

토큰 기반 인증 방식에서 토큰은 세션과 다르게 stateless하다. 서버가 상태를 보관하고 있지 않다. 서버는 한번 발급한 토큰에 대해서 제어권을 가지고 있지 않다. 이런 토큰이 탈취된다면? 사용자는 계정의 제어권을 해커에게 속수무책으로 내어줄 수 밖에 없다. 서버 측에서도 토큰이 만료될 때까지 기다리는 것 말고는 어찌할 도리가 없다.

## Refresh Token은 왜 필요한가?

---

JWT는 발급한 후 삭제가 불가능하기 때문에, 접근에 관여하는 토큰에 유효시간을 부여하는 식으로 탈취 문제에 대해 대응해야 한다. 이처럼 토큰 유효기간을 짧게 하면 토큰 남용을 방지하는 것이 해결책이 될 수 있지만, 유효기간이 짧은 토큰의 경우 그만큼 사용자는 로그인을 자주 해서 새롭게 토큰을 발급받아야 하는 불편함이 있다. 그렇다고 무턱대고 유효기간을 늘리자면, 토큰을 탈취당했을 때 보안에 더 취약해지게 된다.

Refresh Token은 “유효기간은 짧게 하면서 잦은 로그아웃은 필요없도록 하는 방법이 있을까?”라는 질문에 대한 답이다.

이름은 다르지만 형태 자체는 Refresh Token은 Access Toekn과 똑같은 JWT이다. 단지 Access Token은 접근에 관여하는 토근이고, Refresh Token은 재발급에 관여하는 토큰으로 역할이 다르다.

예를 들어 처음 로그인을 했을 떄, 서버는 로그인을 성공시키면서 클라이언트에게 Access Token과 Refresh Token을 동시에 발급한다. 서버는 데이터베이스에 Refresh Token을 저장하고, 클라이언트는 Access Token과 Refresh Token을 쿠키, 세션, 혹은 웹스토리지에 저장하고 요청이 있을 때마다 이 둘을 헤더에 담아서 보낸다. 이 Refresh Token은 긴 유효기간을 가지면서, Access Token이 만료되었을 때 새로 재발급해주는 열쇠가 된다. 따라서 만일 만료된 Access Token을 서버에 보내면, 서버는 같이 보내진 Refresh Token을 DB에 있는 것과 비교해서 일치하면 다시 Access Token을 재발급하는 간단한 원리이다. 그리고 사용자가 로그아웃을 하면 저장소에서 Refresh Token을 삭제하여 사용이 불가능하도록 하고 새로 로그인하면 서버에서 다시 재발급해서 DB에 저장한다.

## Access and Refresh Token 재발급 원리

---

1. 기본적으로 로그인같은 과정을 하면 Access Token과 Refresh Token을 모두 발급한다.

- 이 때, Refresh Token만 서버 측의 DB에 저장하며, Refresh Token과 Access Token을 쿠키 혹은 웹 스토리지에 저장한다.

2. 사용자가 인증이 필요한 API에 접근하고자 하면, 가장 먼저 토큰을 검사한다.

- 이 때, 토큰을 검사함과 동시에 각 경우에 대해서 토큰의 유효기간을 확인하여 재발급 여부를 결정한다.

    - access token과 refresh token 모두 만료된 경우
        - 에러 발생 (재로그인하여 둘 다 새로 발급)

    - access token은 만료됐지만, refresh token은 유효한 경우
        - refresh token을 검증하여 access token 재발급
        - 클라이언트(쿠키, 웹스토리지)에 저장되어있는 refresh token과 서버 DB에 저장되어있는 refresh token 일치성을 확인한 뒤 access token을 재발급한다.

    - access token은 유효하지만, refresh token은 만료된 경우
        - access token을 검증하여 refresh token 재발급
        - access token이 유효하다라는 것은 이미 인증된 것과 마찬가지이니 바로 refresh token을 재발급한다.

    - access token과 refresh token 모두가 유효한 경우
        - 정상 처리

3. 로그아웃을 하면 Access Token과 Refresh Token을 모두 만료시킨다.

## Refresh Token 인증 과정

---

![token](https://github.com/zacinthepark/TIL/assets/86648892/51556d7f-4eb3-4e55-8683-d1edba53055e)

(1) 사용자가 ID, PW를 통해 로그인한다.

(2) 서버에서는 회원 DB에서 값을 비교한다.

(3-4) 로그인이 완료되면 Access Toekn, Refresh Token을 발급, 이 때 회원 DB에도 Refresh Token을 저장한다.

(5) 사용자는 Refresh Token은 안전한 저장소에 저장 후, Access Token을 헤더에 실어 요청을 보낸다.

(6-7) Access Token을 검증하여 이에 맞는 데이터를 보낸다.

(8) 시간이 지나 Access Token이 만료된다.

(9) 사용자는 이전과 동일하게 Access Token을 헤더에 실어 요청을 보낸다.

(10-11) 서버는 Access Token이 만료됨을 확인하고 권한없음을 신호로 보낸다.
- Access Token이 만료될 때마다 9-11의 과정을 거칠 필요는 없다. 사용자(프론트엔드)에서 Access Token의 Payload를 통해 유효기간을 알 수 있다. 따라서 프론트엔드 단에서 API 요청 전에 토큰이 만료됐다면 곧바로 재발급 요청을 할 수도 있다.

(12) 사용자는 Refresh Token과 Access Token을 함께 서버로 보낸다.

(13) 서버는 받은 Access Token이 조작되지 않았는지 확인한 후, Refresh Token과 사용자의 DB에 저장되어 있던 Refresh Token을 비교한다. Token이 동일하고 유효기간도 지나지 않았다면 새로운 Access Token을 발급해준다.

(14) 새로운 Access Token을 헤더에 실어 다시 API 요청 및 응답을 진행한다.
