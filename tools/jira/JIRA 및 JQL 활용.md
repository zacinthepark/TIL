## JIRA

---

- 버그 추적, 이슈 추적, 프로젝트 관리 기능 제공

### Issue Tracking (Project Management)

- 이슈, 티켓 등으로 표현
- Issue Tracking Tools

![issue_tracking_tools](https://github.com/zacinthepark/TIL/assets/86648892/dfe2175d-ebcc-4045-bb0a-d01d5c9228d7)

- JIRA
    - Project Management
    - JIRA는 프로젝트 매니저 입장에서 프로젝트를 관리하기 쉽게끔 visualizing해주는 측면이 있음

### Agile

- 애자일 소프트웨어 개발 선언
    - 우리는 소프트웨어를 개발하고, 또 다른 사람의 개발을 도와주면서 소프트웨어 개발의 더 나은 방법들을 찾아가고 있다. 이 작업을 통해 우리는 다음을 가치 있게 여기게 되었다.
        - 공정과 도구보다 개인과 상호작용을
        - 포괄적인 문서보다 작동하는 소프트웨어를
        - 계약 협상보다 고객과의 협력을
        - 계획을 다르기보다 변화에 대응하기를
        - 가치있게 여긴다. 이 말은 왼쪽에 있는 것도 가치가 있지만, 우리는 오른쪽에 있는 것들에 더 높은 가치를 둔다는 것이다.
- 애자일 방법론을 기반으로 한 대표적인 방법론
    
![scrum_kanban](https://github.com/zacinthepark/TIL/assets/86648892/8ebb4766-3c08-4a0b-8a47-397a74c2cd9e)
    
- Scrum
    - 이슈들을 백로그(타지 않은 장작)에 쌓아놓고
    - 2-3주 정도의 스프린트를 생성
    - 해당 이슈를 해결하는데 집중
- Kanban
    - 이슈들에 대해 어떤 상태에 있는지 관리
    - 전체적인 줄기 안에서 관리

### DevOps

![devops](https://github.com/zacinthepark/TIL/assets/86648892/a1c5db14-9809-4cda-8f97-74cb7e8b8d44)

![dev](https://github.com/zacinthepark/TIL/assets/86648892/b28a30ae-5604-4238-976b-8cf023da6825)

![jira](https://github.com/zacinthepark/TIL/assets/86648892/80df4c6e-b1c6-4fe9-aea6-8be25032c423)

- Development + Operations
    - 사일로 현상(Silo Effect)라는 조직 간 이기주의 해결
- DevOps를 잘 수행하기 위한 조건
    - 반복적인 작업들을 Tool을 이용해서 자동화
    - 팀원 모두가 알고 있는 하나의 공유된 지표가 필요
    - 실시간 소통이 중요
    - 장애나 이슈가 있을 때 혼자만 알지 말고 팀원들과 공유 필요
- DevOps 여러 단계에 대하여 Jira에서 서비스를 제공함

### SRE

- 배포 등의 작업이 DevOps 체계에서 자동화되었을 때 운영팀은 어떤 일을 할 수 있을까?
- Site Reliability Engineering
    - 장애가 나지 않기 위해 지표를 만들어보고 미리 플래닝해보자
    - 장애를 누구에게 책임지우지 않고 모두의 공동 책임을 갖고 장애를 최소화하기 노력한다
- “class SRE implements DevOps”

## JIRA 활용

---

### JIRA 사용하기

1. 백로그에서 스프린트 생성
2. 스프린트에 이슈 등록
3. 생성된 이슈에 스토리 포인트 설정
4. 스프린트 시작
5. 이슈관리
6. 스프린트 종료

### 백로그? 스프린트?

- 백로그 : 프로젝트에서 해야 하는 일(요구사항)을 보여줌
- 스프린트 : 스크럼 보드의 개발 주기 단위

### 이슈?

- 오류, 버그, 새로운 기능, 작업 요청, 질문이나 의견 등 개발에 관한 모든 것
- Issue 종류 : Epic(큰틀), Story(이야기-회원관련, Task(작업), SUB-TASK(부작업), BUG(버그)

### Sprint 생성

- 백로그에서 스프린트 만들기 누르기
- 스프린트가 생기면 이슈 생성 버튼을 통해 만들어서 넣어주어야 한다.
- 스토리, 작업, 버그, 에픽중에 선택하여 만든다. 
- 밑에 이슈를 스토리, 작업에 연결하고 싶은 경우 연결할 이슈를 선택하면 된다.
- 이슈 만들기를 내리다보면 담당자를 선택할 수 있다.
- 레이블은 원하는대로 선택하여 사용하면 된다.

### Story Point 설정

### Story Point

- 특정 기능을 개발하는데 필요한 노력의 양의 추정치, 이슈 별 최대 4 point 할당
- 1point = 1h
- 팀원 1명이 하루 동안 일할 수 있는 시간은 8시간
- 일주일(5일간) 총 근무 시간은 8 * 5 = 40시간이므로 총 Story Point 40
- 기능 별로 개발 난이도를 고려하여 스토리 포인트 책정, 할 일 분배

### 번다운 차트

- 어떻게 이슈를 해결해왔는지 알 수 있다.
- 이슈 먼저 만들고 스프린트 추가하기

## JQL

---

- Jira Query Language
- Jira Issue를 구조적으로 검색하기 위해 제공하는 언어
- SQL(Standard Query Language)과 비슷한 문법
- Jira의 각 필드들에 맞는 특수한 예약어들을 제공
- 쌓인 Issue들을 재가공해 유의미한 데이터를 도출해내는데 활용
    - Gadget, Agile Board 등

### Basic Query & Advanced Query

- 선택해서 검색하면 basic query
- 쿼리문을 작성하면 advanced query
- ex) `project = "DP" and issuetype in (Epic, Story) and updated > startOfWeek(1d) and updated < endOfWeek(-1d)`

### JQL Operators

- `=, !=, >, >=`
- `in, not in`
- `~(contains), !~(not contains)`
- `is empty, is not empty, is null, is not null`

### JQL Keywords

- `AND`
- `OR`
- `NOT`
- `EMPTY`
- `NULL`
- `ORDER BY`

### JQL Dates

- JQL만의 편리한 기능
- 날짜를 상대적인 것으로 제공
    - -1d, -2d, 1d, 2d, -1w, -2w, 1w, 2w…
- JQL query에서 `created > -2d` , `updated > -1w` 과 같이 사용 가능

### JQL Functions

- `endOfDay(), startOfDay()`
- `endOfWeek(), startOfWeek()`
    - `startOfWeek(1d)` 는 월요일
- `endOfMonth(), startOfMonth(), endOfYear(), startOfYear()`
- `currentUser()`

### JQL 활용예시: Filter Share

- `project = "DP" and assignee = currentUser() and resolution = unresolved`
    - Save Filter
        - “나의 미완료 이슈”로 필터 저장
        - 프로젝트 및 프로젝트 멤버들에게 필터 공유 가능
- Filters 탭에서 나에게 공유된 필터들을 확인 가능
- 기존 필터의 경우 Details - Edit Permission으로 새로운 멤버 지정 가능

### JQL 활용예시: Dashboard, Gadget

- 차트나 여러 visualizer 활용 가능
- 필터와 마찬가지로 생성한 대시보드를 공유할 수 있음
- 대시보드를 생성하면 여러 가젯을 추가할 수 있음
