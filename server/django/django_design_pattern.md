## Django Design Pattern

---

### Web Application Structure

<p align="center">
    <img width="600" alt="web_frameworks" src="https://github.com/zacinthepark/TIL/assets/86648892/2ada550e-e4c1-4ac7-84b1-6641281ec51e">
</p>

### Django?

- Python Fullstack Web Framework
- 확장성이 뛰어나 복잡한 요구사항과 통합이 필요한 개발에 적합하다
- 불필요한 중복을 없애고 많은 양의 코드를 줄여 유지보수가 쉽고 재사용하기 좋은 디자인 원칙과 패턴들을 사용한다
- 리눅스, 윈도우 그리고 맥OS 등등 다양한 운영체제에서 작동할 수 있다
- 비밀번호, 세션, 크로스사이트 요청 위조등의 보안 취약점을 보완할 방법을 기본적으로 제공한다

### Django의 요소

- View: HTTP의 요청을 처리
- Model: 데이터베이스 처리
- Template: 사용자의 인터페이스 처리
- Form: 사용자의 입력 데이터 처리
- Static 파일: 정적 파일 관리
- Media 파일: 사용자가 업로드한 파일 관리
- Message Framework: 일회성 메시지 처리
- Send Email: 이메일 작성 및 전송
- Admin 앱: 관리자를 위한 쉬운 DB 데이터 관리 UI 제공
- Auth 앱: 사용자 인증에 관련된 서비스 제공
- Session 앱: 사용자별로 사용되는 데이터 서비스 제공

### Django MTV Design Pattern

<p align="center">
    <img width="400" alt="dj_5" src="https://user-images.githubusercontent.com/86648892/188303740-506ea720-0375-42cf-94b8-6b8fbe43791d.png">
</p>

- Model
    - DB 데이터 처리 담당
    - 데이터와 관련된 로직을 관리
    - 프로그램의 데이터 구조를 정의하고, 데이터베이스의 기록을 관리

- Template
    - 서비스 요청 화면 또는 서비스 처리 결과 화면 처리 담당
    - 레이아웃과 화면을 처리
    - 화면상의 사용자 인터페이스 구조와 레이아웃을 정의

- View
    - 사용자의 요청에 대한 서비스 처리 담당
    - Model, Template과 관련한 로직을 처리해서 응답을 반환
    - 클라이언트의 요청에 대해 처리를 분기하는 역할
    - Request → URL 주소를 보고 어디로(Template) 요청을 보내야할지 판단 → View가 필요한 데이터가 있을 시 Model과 소통 → Model에서 데이터를 가져오고 → 해당 Template으로 보내 화면을 구성하고 → 구성된 화면을 응답으로 클라이언트에게 반환
