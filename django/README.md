# Database Basics and Django

- [Database](#database)
- [QuerySet API Advanced](#queryset-api-advanced)
- [Django](#django)
- [Django N:1 Relationship](#django-n1-relationship)
- [Django M:N Relationship](#django-mn-relationship)
- [Django Static Files](#django-static-files)
- [Django REST Framework and Serializer](#django-rest-framework-and-serializer)

---

# Database

# sqlite3 설치

- sqlite3는 sqlite와 직접적으로 한줄 한줄 소통할 수 있는 shell (실행 환경)

1. Download

   - [https://www.sqlite.org/download.html](https://www.sqlite.org/download.html)

   <img width="846" alt="db1" src="https://user-images.githubusercontent.com/86648892/212545610-bced487d-9199-47da-8378-231b325530d2.png">

2. Installation

   - 폴더 생성

   <img width="865" alt="db2" src="https://user-images.githubusercontent.com/86648892/212545609-c17622a4-1483-48f4-b63e-5fc9aa6b1f2b.png">

   - Path 설정 (시스템 환경 변수 편집)
     - 고급 탭
       - 환경 변수
         - Path - 편집 - sqlite 폴더 경로 추가
         - 환경 변수에 등록하는 것은 여기에 등록되어 있는 위치는 컴퓨터가 항상 참조할 수 있는 위치라는 것
           - 터미널 어디서든 시스템 환경변수의 path에 있는 애들은 무조건 잡을 수 있도록 전역으로 설정하는 것
           - 시스템 환경변수 path에 sqlite 폴더를 등록해주는 것은, 이 컴퓨터가 앞으로 sqlite 폴더 안쪽의 파일들을 항상 참조할 수 있는 상태가 되는 것
             - `winpty sqlite3`
               - C 드라이브의 sqlite 폴더 안에서 sqlite3를 찾아서 실행할 수 있는 것
               - `.exit` 하거나 `ctrl+c` 하면 나가짐

3. alias 생성
   - `.bashrc` 실행
     - `code ~/.bashrc`
   - alias 설정 저장
     - `alias sqlite3="winpty sqlite3"`
   - `.bashrc` 변경사항 적용
     - `source .bashrc`

## sqlite3 사용하기

<img width="789" alt="db3" src="https://user-images.githubusercontent.com/86648892/212545608-7c6b0e5c-6c1f-4db6-8366-e51b356c28d4.png">

<img width="856" alt="db4" src="https://user-images.githubusercontent.com/86648892/212545607-3ad3d2e2-2cf1-4a44-9f2b-6ceec7010836.png">

<img width="864" alt="db5" src="https://user-images.githubusercontent.com/86648892/212545606-e28ef3af-cc22-49a2-bcb7-ace52d19ede8.png">

<img width="864" alt="db6" src="https://user-images.githubusercontent.com/86648892/212545605-ecaae61f-761a-4e87-b481-46622baa925a.png">

<img width="864" alt="db7" src="https://user-images.githubusercontent.com/86648892/212545604-9015e723-8da1-493c-8fc2-ed51e391531b.png">

---

# Database Intro

- 서비스 혹은 애플리케이션들이 데이터를 저장하는 곳
  - 데이터베이스
    - 데이터베이스의 변천
      - 파일을 이용한 데이터 관리
        - 장점
          - 운영체제에 관계없이 어디에서나 쉽게 사용 가능
          - 이메일이나 메신저를 이용해 간편한 전송 가능
        - 단점
          - 성능과 보안적 측면의 한계가 명확
          - 대용량 데이터에 부적합
          - 데이터의 구조적 정리 어려움
          - 확장이 불가능한 구조
      - 스프레드 시트를 이용한 데이터 관리
        - 컬럼(열)을 통해 데이터 유형 지정
        - 레코드(행)를 통해 구체적인 데이터 값을 포함
        - 스프레드 시트 자체를 데이터베이스라 부를 수는 없지만 데이터베이스로 가는 길목 정도로 생각할 수 있음
      - Database
        - 스프레드 시트와 달리 프로그램이 언어를 사용해 작동시킬 수 있음
        - 많은 형태 중 **_RDB(Relational Database)_**, **_관계형 데이터베이스_**가 가장 많이 사용됨
        - 데이터베이스의 종류는 크게 관계형 데이터베이스(RDB)와 NoSQL 데이터베이스 2종류로 나뉨
          - **_관계형 DB(RDB)는 테이블 형식으로 저장_**
            - 즉, 하나의 데이터베이스 안에 여러 개의 테이블이 존재한다!
            - 관계형 DB를 조작하는 대표적인 프로그램이 MySQL, Sqlite, PostgreSQL, Oracle 등
              - 이러한 프로그램들을 **_DBMS(Database Management System)_**라 함
              - DBMS에서 DB를 조작할 때 사용하는 언어가 **_SQL_**
            - NoSQL DB는 Key-Value 형식으로 저장

### “데이터베이스에 데이터를 어떻게 입력하고, 어떻게 출력하는가”

- 입력
  - 저장, 수정, 삭제
- 출력
  - 조회

## Database 정의

- 체계화된 데이터의 모임
- 여러 사람이 공유하고 사용할 목적으로 통합 관리되는 **_정보의 집합_**
- 검색, 구조화같은 작업을 보다 쉽게하기 위해 **_조직화된 데이터_**를 수집하는 저장 시스템
  - 내용을 고도로 구조화함으로써 **_검색과 갱신의 효율화_**를 꾀한 것
  - 즉, 자료 파일을 조직적으로 통합하여 자료 항목의 중복을 없애고 구조화하여 기억시켜놓은 **_자료의 집합체_**
- 이러한 Database를 조작하는 프로그램 = **_DBMS(Database Management System)_**
  - Oracle, MySQL, SQLite 등이 모두 DBMS
  - DBMS에서 Database를 조작하기위해 사용하는 언어를 **_SQL_**이라함
- 웹 개발에서 대부분의 데이터베이스는 ‘관계형 데이터베이스 관리 시스템(RDBMS)’을 사용하여 SQL로 데이터와 프로그래밍을 구성

---

# RDB

- Relational Database (관계형 데이터베이스)
- 데이터를 **_테이블_**, 행, 열 등으로 나누어 구조화하는 방식
- 자료를 여러 테이블로 나누어서 관리하고, 이 **_테이블 간 관계를 설정_**해 여러 데이터를 쉽게 조작할 수 있다는 장점
- SQL을 사용하여 데이터를 조회하고 조작

### [참고] 테이블 간 관계 설정 예시

<img width="881" alt="db8" src="https://user-images.githubusercontent.com/86648892/212545603-b607f514-b2a9-49e5-8a81-4ebe9ee2dd76.png">

## RDB 기본 구조

1. 스키마
   - 테이블의 구조(Structure)
   - 데이터베이스에서 자료의 구조, 표현 방법, 관계 등 전반적인 명세를 기술한 것
2. 테이블
   - 필드와 레코드를 사용해 조직된 데이터 요소들의 집합
   - 관계(Relation)라고도 부름
   - 필드(Field)
     - 속성, 컬럼(Column)
     - 각 필드에는 고유한 데이터 형식(타입)이 지정됨
   - 레코드(Record)
     - 튜플, 행(Row)
     - 테이블의 데이터는 레코드에 저장됨
   - 기본 키(Primary Key)
     - 각 레코드의 고유한 값
       - 각각의 데이터를 구분할 수 있는 고유값
     - 기술적으로 다른 항목과 절대로 중복될 수 없는 단일 값(unique)

<img width="821" alt="db9" src="https://user-images.githubusercontent.com/86648892/212545602-d030ca06-503c-4d02-88c7-b56989d709cb.png">

<img width="888" alt="db10" src="https://user-images.githubusercontent.com/86648892/212545601-a5941de6-9aec-4130-85e6-899d3cc58367.png">

### 관계형 데이터베이스의 이점

- 데이터를 직관적으로 표현 가능
- 관련한 각 데이터에 쉽게 접근 가능
- 대량의 데이터도 효율적으로 관리 가능

## RDBMS

- Relational Database Management System (관계형 데이터베이스 관리 시스템)
- 관계형 데이터베이스를 만들고, 업데이트하고, 관리하는데 사용하는 프로그램
- SQLite, MySQL, PostgreSQL, Microsoft SQL Server, Oracle Database 등

## SQLite

- 응용 프로그램에 **_파일 형식_**으로 넣어 사용하는 비교적 가벼운 데이터베이스
- 안드로이드, iOS, macOS에 기본적으로 탑재되어 있으며 임베디드 소프트웨어에서도 많이 활용됨
- 오픈소스 프로젝트이기에 자유롭게 사용 가능
- 장점
  - 어떤 환경에서나 실행 가능한 호환성
  - 데이터 타입이 비교적 적고 강하지 않기에 유연한 학습 환경 제공
  - Django Framework의 기본 데이터베이스
- 단점
  - 대규모 동시 처리 작업에 적합하지 않음
  - 다른 RDBMS에서 지원하는 SQL 기능을 지원하지 않을 수 있음

---

# SQL

## SQL이란

- “Structured Query Language”
  - 구조 명령 언어
- RDBMS 데이터를 관리하기위해 설계된 **_특수 목적의 프로그래밍 언어_**
- RDBMS에서 데이터베이스 스키마를 생성 및 수정할 수 있으며
  - 테이블에서의 자료 검색 및 관리도 할 수 있음
- 데이터베이스 객체에 대한 처리를 관리하거나 접근 권한을 설정하여 허가된 사용자만 RDBMS를 관리할 수 있도록 할 수 있음
- 많은 데이터베이스 관련 프로그램들이 SQL을 표준으로 채택하고 있음

## SQL 정리

- SQL은 데이터베이스와 상호작용하는 방법
- 따라서 SQL을 배우면서 데이터베이스의 동작원리 또한 익힐 수 있음

---

# SQL Commands

- 명령어는 특성에 따라 다음 3가지 그룹으로 분류
  1. DDL (Data Definition Language)
  2. DML (Data Manipulation Language)
  3. DCL (Data Control Language)

<img width="1423" alt="db11" src="https://user-images.githubusercontent.com/86648892/212545600-7f4e4ff3-06b2-4c0d-bc36-30f82f0f4d85.png">

<img width="850" alt="db12" src="https://user-images.githubusercontent.com/86648892/212545598-d63cc0d0-bf28-4cbd-bd04-6139cc20e6a9.png">

- DDL에서 데이터를 정의
  - 테이블과 스키마를 정의
  - 테이블을 정의하는 과정
- DML에서 데이터를 조작
  - CRUD
  - 정의한 테이블에 데이터를 추가, 조회, 변경, 삭제

---

# SQL Syntax

## SQL Syntax

<img width="861" alt="db13" src="https://user-images.githubusercontent.com/86648892/212545597-87019316-2948-4452-be77-c39270c6db1d.png">

### [참고] Statement & Clause

- Statement (문)
  - 독립적으로 실행할 수 있는 완전한 코드 조각
  - statement는 clause로 구성됨
- Clause (절)
  - statement의 하위 단위

<img width="741" alt="db14" src="https://user-images.githubusercontent.com/86648892/212545596-af26e829-647a-4932-ae98-0463b2ae9151.png">

---

# DDL

- “Data Definition”
  - 테이블 구조를 관리
    - `CREATE`, `ALTER`, `DROP`
      - `CREATE`할 때 Data Types, Constraints 고려
- 테이블(스키마)을 정의하는 언어
  - 데이터를 조작하기 위한 틀을 정의
  - 테이블을 수정하는 것도 데이터 정의에 해당

---

# CREATE TABLE

- “Create a new table in the database”
- 데이터베이스에 새 테이블을 생성
- 스키마를 정의

<img width="476" alt="db15" src="https://user-images.githubusercontent.com/86648892/212545595-fdccfd7c-2ba8-4b10-b45f-fb4f323cdd65.png">

- 세미콜론으로 구문 마무리
- SQL에서는 기본 키를 정의하지 않으면 `rowid` 라는 컬럼으로 기본 키 컬럼을 만듬

---

# SQLite Data Types

## Data Types 종류

1. NULL
   - NULL value
   - 정보가 없거나 알 수 없음을 의미 (missing information or unknown)
2. INTEGER
   - 정수
   - 크기에 따라 0, 1, 2, 3, 4, 6 또는 8바이트와 같은 가변 크기를 가짐
3. REAL
   - 실수
   - 8바이트 부동 소수점을 사용하는 10진수 값이 있는 실수
4. TEXT
   - 문자 데이터
5. BLOB (Binary Large Object)
   - 입력된 그대로 저장된 데이터 덩어리 (대용 타입 없음)
   - 바이너리 등 멀티미디어 파일
   - 예시
     - 이미지 데이터

### [참고] Boolean type

- SQLite에는 별도의 Boolean 타입이 없음
- 대신 Boolean 값은 정수 0(false)과 1(true)로 저장됨

### [참고] Date & Time Datatype

- SQLite에는 날짜 및 시간을 저장하기위한 타입이 없음
- 대신 SQLite의 built-in “Date And Time Functions”으로 TEXT, REAL 또는 INTEGER 값으로 저장할 수 있음
- [https://www.sqlite.org/lang_datefunc.html](https://www.sqlite.org/lang_datefunc.html)

### [참고] Binary Data

- 데이터의 저장과 처리를 목적으로 0과 1의 이진 형식으로 인코딩된 파일
- 기본적으로 컴퓨터의 모든 데이터는 binary data
  - 다만, 이를 필요에 따라서 텍스트 타입으로 변형해서 사용하는 것

## SQLite는 다음 규칙을 기반으로 데이터 타입을 결정

- 값에 둘러싸는 따옴표와 소수점 또는 지수가 없으면
  - INTEGER
- 값에 따옴표가 없고, 소수점, 지수가 있으면
  - REAL
- 값이 작은 따옴표나 큰 따옴표로 묶이면
  - TEXT
- 값이 따옴표 없이 NULL이면
  - NULL

## SQLite Datatypes 특징

1. SQLite는 다른 모든 SQL 데이터베이스 엔진(MySQL, PostgreSQL 등)의 정적이고 엄격한 타입(static, rigid typing)이 아닌
   - **_“동적 타입 시스템(dynamic type system)”_**을 사용
     - 컬럼에 선언된 데이터 타입에 의해서가 아니라 **_컬럼에 저장된 값에 따라 데이터 타입이 결정_**됨
   - 타입을 선언하여 정적 타입 시스템을 사용할 수도, 선언하지 않고 동적 타입 시스템을 사용할 수도 있음
2. 테이블을 생성할 때 컬럼에 대해 특정 데이터 타입을 선언하지 않아도 됨
   - 예를 들어 동일한 컬럼에 정수 1을 넣을 경우 INTEGER로 타입이 지정되고
     - 문자 ‘1’을 넣을 경우는 TEXT 타입으로 지정됨
   - 이러한 SQLite의 동적 타입 시스템을 사용하면 기존의 엄격하게 타입이 지정된 데이터베이스에서는 불가능한 작업을 유연하게 수행할 수 있음
   - 또한 정적 타입 시스템이 지정된 데이터베이스에서 작동하는 SQL문이 SQLite에서 동일한 방식으로 작동
     - 즉, 정적 타입 시스템이 하지 못하는 작업을 할 수도 있으면서, 정적 타입 시스템에서 작동하는 것을 동일하게 작동할 수 있다는 것
   - 그러나, 다른 데이터베이스와의 호환성 문제가 있기 때문에 테이블 생성 시 **_데이터 타입을 지정하는 것을 권장_**
3. 데이터 타입을 지정하게 되면 SQLite는 데이터의 타입을 지정된 데이터 타입으로 변환

   - 예를 들어, TEXT 타입 컬럼에 정수 1을 저장할 경우 문자 타입의 ‘1’로 저장됨
   - 허용 가능한 타입 변환은 다음과 같음

   <img width="532" alt="db16" src="https://user-images.githubusercontent.com/86648892/212545594-dfda2ceb-e83d-454c-9a28-72907567df8d.png">

### [참고] “static, rigid typing” 데이터베이스

<img width="869" alt="db17" src="https://user-images.githubusercontent.com/86648892/212545593-7bf37a9b-c83a-405a-9345-b04946eb5bba.png">

## Type Affinity

- “타입 선호도”
- SQLite의 독특한 특징으로, 제공하는 Datatype의 종류가 많지 않기에, 호환성에 대비하여 내부적으로 타입을 선호하는, 선호도라는 것이 존재함

<img width="818" alt="db18" src="https://user-images.githubusercontent.com/86648892/212545591-dc347d4e-2809-4629-b138-656999480ffc.png">

- 데이터 타입 작성 시, SQLite의 5가지 데이터 타입이 아닌 다른 데이터 타입을 선언한다면, 내부적으로 각 타입의 지정된 선호도에 따라 5가지 선호도로 인식됨
- 타입 선호도 존재 이유
  - 다른 데이터베이스 엔진 간의 호환성을 최대화하기 위함
  - 정적이고 엄격한 타입을 사용하는 데이터베이스의 SQL문을 SQLite에서도 작동하도록 하기 위함

---

# Constraints

## Constraints

- “제약조건”
- 입력하는 자료에 대해 제약을 정함
- 제약에 맞지 않다면 입력이 거부됨
- 사용자가 원하는 조건의 데이터만 유지하기 위한
  - 즉, **_데이터의 무결성_**을 유지하기 위한 보편적인 방법으로
    - 테이블의 특정 컬럼에 설정하는 제약
      - 데이터의 무결성?
        - 데이터베이스 내의 데이터에 대한 정확성, 일관성을 보장하기 위해 데이터 변경 혹은 수정 시 여러 제한을 두어 데이터의 정확성을 보증하는 것

## Constraints 종류

1. `NOT NULL`
   - 컬럼이 NULL 값을 허용하지 않도록 지정
   - 기본적으로 테이블의 모든 컬럼은 NOT NULL 제약 조건을 명시적으로 사용하는 경우를 제외하고는 NULL 값을 허용함
2. `UNIQUE`
   - 컬럼의 모든 값이 서로 구별되거나 고유한 값이 되도록 함
   - 처음에 들어간 값이 동일 컬럼의 다른 레코드에 들어갈 수 없음
3. `PRIMARY KEY`

   - 테이블에서 행의 고유성을 식별하는데 사용되는 컬럼
   - 각 테이블엔 하나의 기본 키만 있음
     - id column은 하나
     - PRIMARY KEY를 따로 정의해주지 않으면 `rowid` 라는 이름으로 자동으로 만들어졌음
   - 만약 직접 pk를 선언하고 싶다면 PRIMARY KEY라는 제약 조건을 선언
   - 암시적으로 NOT NULL 제약 조건이 포함되어 있음

   <img width="476" alt="db19" src="https://user-images.githubusercontent.com/86648892/212545588-35b72922-ce1f-49f1-a156-14888a08196f.png">

   - **_주의) INTEGER 타입에만 사용 가능 (INT BIGINT 등 불가능)_**

4. `AUTOINCREMENT`
   - 사용되지 않은 값이나 이전에 삭제된 행의 값을 재사용하는 것을 방지
     - 1, 2, 3행이 있었는데 3이 삭제되고, 행 하나 추가하면 다시 3이 들어감
       - AUTOINCREMENT를 INTEGER PRIMARY KEY에 다음에 작성하면 해당 rowid를 다시 재사용하지 못하도록 함
         - `id INTEGER PRIMARY KEY AUTOINCREMENT`
         - Django에서 테이블 생성 시 id 컬럼에 기본적으로 AUTOINCREMENT를 제약 조건으로 사용
5. 그 외 기타 Constraints

## rowid의 특징

- 테이블을 생성할 때마다 rowid라는 암시적 자동 증가 컬럼이 자동으로 생성됨
  - 즉, 별도로 속성값을 주지 않아도 자동으로 다음값으로 증가하는 컬럼이라는 뜻
- 테이블의 행을 고유하게 식별하는 64비트 부호 있는 정수 값
  - 64비트의 컴퓨터가 허용할 수 있는 최대 크기까지 정수 값을 가지고 있다고 보면 됨
- 테이블에 새 행을 삽입할 때마다 정수 값을 자동으로 할당
  - 값은 1에서 시작
  - 데이터 삽입 시에 rowid 또느 INTEGER PRIMARY KEY 컬럼에 명시적으로 값이 지정되지 않은 경우, SQLite는 테이블에서 가장 큰 rowid보다 하나 큰 다음 순차 정수를 자동으로 할당
    - AUTOINCREMENT가 제약 조건일 시 삭제된 행의 다음 순차 정수
- 만약 `INTEGER PRIMARY KEY` 키워드를 가진 컬럼을 직접 만들면 이 컬럼은 rowid 컬럼의 별칭(alias)이 됨
  - 내부적으로 rowid가 없어진 것은 아님
  - 우리가 만든 PRIMARY KEY이름으로 rowid에 접근한다고 생각하면 됨
  - 즉, 새 컬럼 이름으로 rowid에 액세스 할 수 있으며, rowid 이름으로도 여전히 액세스 가능
- 한 테이블의 PK가 최대 어디까지 저장될까?
  - 한 테이블의 행의 최대 개수는 `2^64` 까지 이론상으론 들어갈 수 있음
    - 그러나 실제론 `2^64` 까진 도달하기 어렵다고 한다
  - Limits in SQLite
    - [https://www.sqlite.org/limits.html](https://www.sqlite.org/limits.html)
- 만약 꽉 찬 상태의 테이블에 데이터를 넣는다면?
  - 데이터가 최대 값에 도달하고 새 행을 삽입하려고 하면 SQLite는 **_사용되지 않는 정수를 찾아 사용_**
  - SQLite가 사용되지 않은 정수를 찾을 수 없으면 **_SQLITE_FULL 에러_**가 발생
    - 또한 일부 행을 삭제하고 새 행을 삽입하면 SQLite는 삭제된 행에서의 rowid 값을 재사용하려고 시도
      - AUTOINCREMENT가 없다면 pk는 기본적으로 삭제되었을 때 재사용하려고 시도됨

---

# ALTER TABLE

- “Modify the structure of an existing table”
- 기존 테이블의 구조를 수정(변경)
- SQLite의 ALTER TABLE문을 사용하면 기존 테이블을 다음과 같이 변경할 수 있음
  1. **Rename** a table
  2. **Rename** a column
  3. **Add** a new column to a table
  4. **Delete** a column
  - [https://www.sqlite.org/lang_altertable.html](https://www.sqlite.org/lang_altertable.html)

<img width="708" alt="db20" src="https://user-images.githubusercontent.com/86648892/212545587-b4f838a2-bfda-4463-b855-d7031f312e00.png">

### ADD COLUMN 시 주의사항 및 해결방법

<img width="856" alt="db21" src="https://user-images.githubusercontent.com/86648892/212545585-b9573128-528c-42be-ac7e-3e0f9a278503.png">

<img width="881" alt="db22" src="https://user-images.githubusercontent.com/86648892/212545583-515dadd1-088f-4286-85d3-a28f5a3f19f2.png">

### [참고] DEFAULT 제약 조건

- column 제약 조건 중 하나
- 데이터를 추가할 때 값을 생략할 시에 기본값을 설정함

### DROP COLUMN 시 주의사항 (삭제하지 못하는 경우)

<img width="819" alt="db23" src="https://user-images.githubusercontent.com/86648892/212545780-9dba9733-8b76-4f85-aae9-d4250a1f1bd4.png">

1. 컬럼이 다른 부분에서 참조되는 경우
   - FOREIGN KEY
2. PRIMARY KEY인 경우
3. UNIQUE 제약 조건이 있는 경우

---

# DROP TABLE

- “Remove a table from the database”
- 데이터베이스에서 테이블을 제거
  - `DROP TABLE table_name;`
- 존재하지 않는 테이블을 제거하면 SQLite에서 오류가 발생
  - `no such table: table_name`
- 한 번에 하나의 테이블만 삭제할 수 있음
  - 여러 테이블을 제거하려면 여러 DROP TABLE문을 실행해야함
- DROP TABLE 문은 실행 취소하거나 복구할 수 없음
  - 따라서 각별히 주의하여 수행

---

# DDL 정리

- “데이터 정의 언어”
- CREATE TABLE
  - 데이터 타입과 제약 조건
- ALTER TABLE
  - RENAME
    - `ALTER TABLE contacts RENAME TO new_contacts;`
  - RENAME COLUMN
    - `ALTER TABLE new_contacts RENAME COLUMN name TO last_name;`
  - ADD COLUMN
    - `ALTER TABLE new_contacts ADD COLUMN address TEXT NOT NULL DEFAULT 'no address;`
  - DROP COLUMN
    - `ALTER TABLE new_contacts DROP COLUMN address;`
- DROP TABLE
  - `DROP TABLE new_contacts;`

---

# DML Index

- Simple query
- Sorting rows
- Filtering data
- Grouping data
- Changing data

---

# DML

- CRUD
  - DML을 통해 데이터를 조작하기
  - INSERT (C)
  - SELECT (R)
  - UPDATE (U)
  - DELETE (D)

---

# Simple query

- 단일 테이블에서 데이터 조회
  - `SELECT`

<img width="777" alt="db24" src="https://user-images.githubusercontent.com/86648892/212545779-607b9e46-f0eb-4981-9cf0-6ff5f96bb7d1.png">

- 다양한 절과 함께 사용할 수 있음
  - ORDER BY
  - DISTINCT
  - WHERE
  - LIMIT
  - LIKE
  - GROUP BY
- 이름과 나이 조회하기
  - `SELECT first_name, age FROM users;`
- 전체 데이터 조회하기
  - `SELECT * FROM users;`
- rowid와 이름 조회
  - `SELECT rowid, first_name FROM users;`

---

# Sorting rows

<img width="802" alt="db25" src="https://user-images.githubusercontent.com/86648892/212545777-1f13a142-4ff4-420a-b604-5c67c1688481.png">

- 이름과 나이를 나이가 어린 순서대로 조회하기
  - `SELECT first_name, age FROM users ORDER BY age ASC;`
    - ASC는 기본값으로 생략 가능
- 이름과 나이를 나이가 많은 순서대로 조회하기
  - `SELECT first_name, age FROM users ORDER BY age DESC;`
- 이름, 나이, 계좌 잔고를 나이가 어린순으로, 만약 같은 나이라면 계좌 잔고가 많은 순으로 정렬해서 조회하기
  - `SELECT first_name, age, balance FROM users ORDER BY age ASC, balance DESC;`
    - ORDER BY 절은 하나 이상의 컬럼을 정렬할 경우 첫번째 열을 사용하여 행을 정렬한 뒤
      - 그 다음 두번째 컬럼을 사용하여 정렬되어있는 행을 정렬하는 방식

### [참고] Sorting NULLS

- 데이터에 NULL이 있다면?
- 정렬과 관련하여 SQLite는 NULL을 다른 값보다 작은 것으로 간주
  - 즉, ASC를 사용하는 경우 결과의 시작 부분에 NULL이 표시되고, DESC를 사용하는 경우 결과의 끝에 NULL이 표시됨

---

# Filtering data

- 데이터를 필터링하여 중복 제거, 조건 설정 등 쿼리를 제어하기
- Clause
  - `SELECT DISTINCT`
  - `WHERE`
  - `LIMIT`
- Operator
  - `LIKE`
  - `IN`
  - `BETWEEN`

## SELECT DISTINCT clause

<img width="809" alt="db26" src="https://user-images.githubusercontent.com/86648892/212545775-0bb251ee-8e72-4da9-b988-e10c4a4d11ac.png">

- 모든 지역 조회하기
  - `SELECT country FROM users;`
- 중복없이 모든 지역 조회하기
  - `SELECT DISTINCT country FROM users;`
- 지역 순으로 오름차순 정렬하여 중복없이 모든 지역 조회하기
  - `SELECT DISTINCT country FROM users ORDER BY country;`
- 이름과 지역이 중복없이 모든 이름과 지역 조회하기
  - `SELECT DISTINCT first_name, country FROM users;`
    - 각 컬럼의 중복을 따로 계산하는 것이 아니라 **_두 컬럼을 하나의 집합으로 보고 중복을 제거_**
      - 두 쌍이 모두 같은 경우만 제거
- 이름과 지역 중복없이 지역 순으로 오름차순 정렬하여 모든 이름과 지역 조회하기
  - `SELECT DISTINCT first_name, country FROM users ORDER BY country;`

### [참고] NULL with DISTINCT

- SQLite는 NULL 값을 중복으로 간주
- NULL 값이 있는 컬럼에 DISTINCT 절을 사용하면 SQLite는 NULL 값의 한 행을 유지
  - 즉, NULL도 하나의 값으로 생각하여 NULL이 여러 개면 하나만 남김

## WHERE clause

<img width="875" alt="db27" src="https://user-images.githubusercontent.com/86648892/212545774-fa1ee8cb-dc61-4731-8ead-0b7bf7fcdae7.png">

<img width="790" alt="db28" src="https://user-images.githubusercontent.com/86648892/212545772-99bd39c7-78cf-4964-958a-bdb310453fd2.png">

### 비교연산자

<img width="799" alt="db29" src="https://user-images.githubusercontent.com/86648892/212545771-f0ba2e7b-0f03-4abd-b9a4-e1cc1240fec5.png">

### 논리연산자

<img width="815" alt="db30" src="https://user-images.githubusercontent.com/86648892/212545770-3868313d-5936-4e4f-8692-9121a1539c4c.png">

- 나이가 30살 이상인 사람들의 이름, 나이, 계좌 잔고 조회하기
  - `SELECT first_name, age, balance FROM users WHERE age >= 30;`
- 나이가 30살 이상이고 계좌 잔고가 50만원 초과인 사람들의 이름, 나이, 계좌 잔고 조회하기
  - `SELECT first_name, age, balance FROM users WHERE age >= 30 AND balance > 500000;`

### LIKE operator

- “Query data based on pattern matching”
  - 패턴 일치를 기반으로 데이터를 조회
  - SELECT, DELETE, UPDATE 문의 WHERE 절에서 사용
  - 기본적으로 대소문자를 구분하지 않음
    - `'A' LIKE 'a'`
      - True

<img width="835" alt="db31" src="https://user-images.githubusercontent.com/86648892/212545769-4581a4f5-7970-442f-9bb4-6cf718c66a00.png">

- `%` 은 **_0개 이상의 문자_**가 올 수 있음을 의미
  - `‘김%’`
    - 김치냉장고, 김치, 김밥, 김밥먹자, 김김김
- `_` 는 **_단일(1개) 문자_**가 있음을 의미
  - `‘김_’`
    - 김밥, 김치, 김씨

<img width="857" alt="db32" src="https://user-images.githubusercontent.com/86648892/212545767-82bef6b4-157f-401e-9560-b863a6ac68b5.png">

<img width="839" alt="db33" src="https://user-images.githubusercontent.com/86648892/212545766-9e871916-c9d5-4c45-aa2f-6701f23211f1.png">

- 이름에 ‘호’가 포함되는 사람들의 이름과 성 조회하기
  - `SELECT first_name, last_name FROM users WHERE first_name LIKE '%호%';`
- 이름이 ‘준’으로 끝나는 사람들의 이름 조회하기
  - `SELECT first_name FROM users WHERE first_name LIKE '%준';`
- 서울 지역 전화번호를 가진 사람들의 이름과 전화번호 조회하기
  - `SELECT first_name, phone FROM users WHERE phone LIKE '02-%';`
- 나이가 20대인 사람들의 이름과 나이 조회하기
  - `SELECT first_name, age FROM users WHERE age LIKE ‘2_’;`
- 전화번호 중간 4자리가 51로 시작하는 사람들의 이름과 전화번호 조회하기
  - `SELECT first_name, phone FROM users WHERE phone LIKE '%-51__-%';`

### IN operator

- “Determine whether a value matches any value in a list of values”
  - 값이 값 목록 결과에 있는 값과 일치하는지 확인
  - 표현식이 값 목록의 값과 일치하는지 여부에 따라 True or False를 반환
  - IN 연산자의 결과를 부정하려면 `NOT IN` 연산자를 사용
- 경기도 혹은 강원도에 사는 사람들의 이름과 지역 조회하기
  - `SELECT first_name, country FROM users WHERE country in ('경기도', '강원도');`
  - `SELECT first_name, country FROM users WHERE country = '경기도' OR country = '강원도';`
- 경기도 혹은 강원도에 살지 않는 사람들의 이름과 지역 조회하기
  - `SELECT first_name, country FROM users WHERE country NOT IN (’경기도’, ‘강원도’);`

### BETWEEN operator

<img width="849" alt="db34" src="https://user-images.githubusercontent.com/86648892/212545765-94f3266f-7a3d-416c-8804-e2f94e7c9c85.png">

- 나이가 20살 이상, 30살 이하인 사람들의 이름과 나이 조회하기
  - `SELECT first_name, age FROM users WHERE age BETWEEN 20 AND 30;`
  - AND 연산자 활용 가능
    - `SELECT first_name, age FROM users WHERE age >= 20 AND age <= 30;`
- 나이가 20살 이상, 30살 이하가 아닌 사람들의 이름과 나이 조회하기
  - `SELECT first_name, age FROM users WHERE age NOT BETWEEN 20 AND 30;`
  - OR 연산자 활용 가능
    - `SELECT first_name, age FROM users WHERE age < 20 OR age > 30;`

---

## LIMIT clause

<img width="857" alt="db35" src="https://user-images.githubusercontent.com/86648892/212545764-d3613eb3-814b-4d7b-8e74-caf38aecdd3c.png">

- 첫번째부터 열번째 데이터까지 rowid와 이름 조회하기
  - `SELECT rowid, first_name FROM users LIMIT 10;`
- 계좌 잔고가 가장 많은 10명의 이름과 계좌 잔고 조회하기
  - `SELECT first_name, balance FROM users ORDER BY balance DESC LIMIT 10;`
    - 이와 같이 ORDER BY 절을 LIMIT 절 이전에 배치하여 우선 정렬한 후, 지정된 행 수를 가져올 수 있음
- 나이가 가장 어린 5명의 이름과 나이 조회하기
  - `SELECT first_name, age FROM users ORDER BY age LIMIT 5;`

### OFFSET keyword

<img width="878" alt="db36" src="https://user-images.githubusercontent.com/86648892/212545761-7aed1e38-272e-4b67-a9b9-08832453abcf.png">

---

# Grouping data

## GROUP BY clause

<img width="867" alt="db37" src="https://user-images.githubusercontent.com/86648892/212545759-59854474-89c1-4ad0-836c-2b9b8abef6ce.png">

## Aggregate Function

<img width="809" alt="db38" src="https://user-images.githubusercontent.com/86648892/212545758-01e56ef2-7d4d-421d-8bdf-de481d5bc87e.png">

- users 테이블의 전체 행 수 조회하기
  - `SELECT COUNT(*) FROM users;`
- 나이가 30살 이상인 사람들의 평균 나이 조회하기
  - `SELECT AVG(age) FROM users WHERE age >= 30;`
- 각 지역별로 몇 명씩 살고 있는지 조회하기
  - ‘각 지역별’은 지역 별로 그룹을 나눌 필요가 있음을 의미
    - country 컬럼으로 그룹화
      - 몇 명씩 사는지 계산하기 위해 Aggregate Function 중 COUNT 사용
  - `SELECT country, COUNT(*) FROM users GROUP BY country;`
    - 각 지역별로 그룹이 나뉘어져있기 때문에 `COUNT(*)` 는 지역별 데이터 개수를 셈
    - `COUNT()` , `COUNT(age)` , `COUNT(last_name)` 등 어떤 컬럼을 넣어도 결과는 같음
      - 현재 쿼리에서는 그룹화된 country를 기준으로 카운트하는 것이기에 어떤 컬럼을 카운트해도 전체 개수는 동일하기 때문
- 각 성씨가 몇 명씩 있는지 조회하기
  - `SELECT last_name, COUNT(*) FROM users GROUP BY last_name;`

### `AS`

- `SELECT last_name, COUNT(*) AS number_of_name FROM users GROUP BY last_name;`
  - 컬럼명이 COUNT(\*)가 아닌 number_of_name으로 변경하여 조회
- 인원이 가장 많은 성씨 순으로 조회하기
  - `SELECT last_name, COUNT(*) FROM users GROUP BY last_name ORDER BY COUNT(*) DESC;`
- 각 지역별 평균 나이 조회하기
  - `SELECT country, AVG(age) FROM users GROUP BY country;`

---

# Changing data

- 데이터를 삽입, 수정 삭제하기
  - INSERT
  - UPDATE
  - DELETE

## INSERT statement

<img width="810" alt="db39" src="https://user-images.githubusercontent.com/86648892/212545757-5c595fa4-9338-4639-88b8-94c3bf72d017.png">

<img width="817" alt="db40" src="https://user-images.githubusercontent.com/86648892/212545754-0a61c4b5-420d-4af3-a6e8-c6ab7f80a685.png">

<img width="802" alt="db41" src="https://user-images.githubusercontent.com/86648892/212545753-fe9fe7fa-18db-4a67-b19f-010f6daa82c1.png">

## UPDATE STATEMENT

<img width="818" alt="db42" src="https://user-images.githubusercontent.com/86648892/212545744-d0370699-a015-4495-97d1-aad963bca43f.png">

- 2번 데이터의 이름을 ‘김철수한무두루미’, 주소를 ‘제주도’로 수정하기
  - `UPDATE classmates SET name = '김철수한무두루미' address = '제주도' WHERE rowid = 2;`

## DELETE STATEMENT

<img width="810" alt="db43" src="https://user-images.githubusercontent.com/86648892/212545741-628ba27c-719a-4dff-aabe-c7841be4b985.png">

<img width="847" alt="db44" src="https://user-images.githubusercontent.com/86648892/212545738-152580a9-f6d1-4382-a797-08b9c4e48fb5.png">

- 이름에 ‘영’이 포함되는 데이터 삭제하기
  - `DELETE FROM classmates WHERE name LIKE '%영%';`
- 테이블의 모든 데이터 삭제하기
  - `DELETE FROM classmates;`

---

## 정리

- Database
  - RDB
- SQL
  - DDL
    - CREATE TABLE
      - Data Type
      - Constraints
    - ALTER TABLE
    - DROP TABLE
  - DML
    - SELECT (R)
      - SELECT DISTINCT
    - ORDER BY
    - WHERE
      - LIKE, IN, BETWEEN
    - LIMIT, OFFSET
    - GROUP BY
      - Aggregate Function
    - INSERT (C), UPDATE (U), DELETE (D)

---

## 데이터 구조화의 중요성

- 다루고자 하는 데이터를 구조화해서 저장하면 데이터의 가공 및 확장이 용이
- 모든 서비스는 데이터를 효율적으로 다루는 것이 필수적
  - 빅데이터, 인공지능과 같은 대규모 데이터로부터 의미있는 분석결과를 뽑아낼 수 있음

## 데이터베이스의 미래

- 오늘날 인터넷에서의 방대한 데이터 수집은 세상을 빠르게 변화시키고 있음
- 이전에는 데이터를 단순히 저장하고 조회하기 위한 용도였다면, 이제는 저장된 데이터를 분석하고 활용하는 시대
  - 기업들은 이러한 분석을 통해 더 나은 의사 결정을 하고 기업의 확장성과 민첩성을 높임
- 따라서 데이터에 대한 액세스 및 처리량을 최적화하는 것이 점점 중요해지고 있으며 앞으로 데이터베이스는 점점 자동화되어 클라우드 기술, 머신러닝 등을 사용해 더욱더 고도화된 데이터를 다루고 처리하게 될 것

---

## BRIEF SQL SUMMARY (DDL, DML)

### DDL

```sql
-- Create a table
CREATE TABLE contacts (
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    email TEXT NOT NULL UNIQUE
);

-- 1. Rename a table
ALTER TABLE contacts
RENAME TO new_contacts;

-- 2. Rename a column
ALTER TABLE new_contacts
RENAME COLUMN name TO last_name;

-- 3. Add a new column to a table
ALTER TABLE new_contacts
ADD COLUMN address TEXT NOT NULL;

-- 4. Delete a column
ALTER TABLE new_contacts
DROP COLUMN address;

-- Delete a table
DROP TABLE new_contacts;
```

### DML

```sql
-- R

CREATE TABLE users (
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTEGER NOT NULL
);

-- [1] Simple query

-- 이름과 나이 조회하기
SELECT first_name, age
FROM users;
-- 전체 데이터 조회
-- asterisk에도 rowid는 포함되지 않음
SELECT * FROM users;
-- rowid 출력
SELECT rowid, first_name
FROM users;

-- [2] Sorting rows (레코드 정렬)

-- 이름과 나이를 나이가 어린 순서대로 조회하기
SELECT first_name, age FROM users
ORDER BY age ASC;
-- 이름과 나이를 최연장자 순으로 조회하기
SELECT first_name, age FROM users
ORDER BY age DESC;
-- 이름, 나이, 계좌 잔고를 나이가 어린 순으로, 만약 같은 나이라면 계좌 잔고가 많은 순으로 정렬해서 조회하기
SELECT first_name, age, balance FROM users
ORDER BY age ASC, balance DESC;

-- [3] Filtering data (데이터를 필터링하여 중복 제거, 조건 설정 등 쿼리를 제어하기)

-- SELECT DISTINCT clause
-- 모든 지역 조회하기
SELECT country FROM users;
-- 중복없이 모든 지역 조회하기
SELECT DISTINCT country FROM users;
-- 지역 순으로 내림차순 정렬하여 중복없이 모든 지역 조회하기
SELECT DISTINCT country FROM users
ORDER BY country;
-- 이름과 지역이 중복없이 모든 이름과 지역 조회하기
-- 이름 중복 제거, 지역 중복 제거 따로 하는 것이 아닌 (이름-지역) 같은 쌍의 중복 제거
SELECT DISTINCT first_name, country FROM users;
-- 이름과 지역 중복없이 지역 순으로 내림차순 정렬하여 모든 이름과 지역 조회하기
SELECT DISTINCT first_name, country FROM users
ORDER BY country DESC;

-- WHERE clause
-- 나이가 30살 이상인 사람들의 이름, 나이, 계좌 잔고 조회하기
SELECT first_name, age, balance FROM users
WHERE age >= 30;
-- 나이가 30살 이상이고 계좌 잔고가 50만원 초과인 사람들의 이름, 나이, 계좌 잔고 조회하기
SELECT first_name, age, balance FROM users
WHERE age >= 30 AND balance > 500000;

-- LIKE (패턴 일치를 기반으로 데이터 조회)
-- 이름에 '호'가 포함되는 사람들의 이름과 성 조회하기
SELECT first_name, last_name FROM users
WHERE first_name LIKE '%호%';
-- 이름이 '준'으로 끝나는 사람들의 이름 조회하기
SELECT first_name FROM users
WHERE first_name LIKE '%준';
-- 서울 지역 전화번호를 가진 사람들의 이름과 전화번호 조회하기
SELECT first_name, phone FROM users
WHERE phone LIKE '02-%';
-- 나이가 20대인 사람들의 이름과 나이 조회하기
SELECT first_name, age FROM users
WHERE age LIKE '2_';
-- 전화번호 중간 4자리가 51로 시작하는 사람들의 이름과 전화번호 조회하기
SELECT first_name, phone FROM users
WHERE phone LIKE '%-51__-%';

-- IN operator
-- 경기도 혹은 강원도에 사는 사람들의 이름과 지역 조회하기
SELECT first_name, country FROM users
WHERE country IN ('경기도', '강원도');
-- OR 연산자도 활용 가능
SELECT first_name, country FROM users
WHERE country = '경기도' OR country = '강원도';
-- 경기도 혹은 강원도에 살지 않는 사람들의 이름과 지역 조회하기
SELECT first_name, country FROM users
WHERE country NOT IN ('경기도', '강원도');

-- BETWEEN operator
-- 값이 값 범위에 있는지 테스트
-- 나이가 20살 이상, 30살 이하인 사람들의 이름과 나이 조회하기
SELECT first_name, age FROM users
WHERE age BETWEEN 20 AND 30;
-- AND와 논리 연산자로도 구현 가능
SELECT first_name, age FROM users
WHERE age >= 20 AND age <= 30;
-- 나이가 20살 이상, 30살 이하가 아닌 사람들의 이름과 나이 조회하기
SELECT first_name, age FROM users
WHERE age NOT BETWEEN 20 AND 30;
-- OR와 논리 연산자로도 구현 가능
SELECT first_name, age FROM users
WHERE age < 20 OR age > 30;

-- LIMIT clause (쿼리에서 반환되는 행 수를 제한)
-- 첫번째부터 열번째 데이터까지 rowid와 이름 조회하기
SELECT rowid, first_name FROM users
LIMIT 10;
-- 계좌 잔고가 가장 많은 10명의 이름과 계좌 잔고 조회하기
SELECT first_name, balance FROM users
ORDER BY balance DESC LIMIT 10;
-- 나이가 가장 어린 5명의 이름과 나이 조회하기
SELECT first_name, age FROM users
ORDER BY age LIMIT 5;
-- 11번째부터 20번째 데이터의 rowid와 이름 조회하기
SELECT rowid, first_name FROM users
LIMIT 10 OFFSET 10;

-- [4] Grouping Data
-- 각 지역별로 몇 명씩 살고 있는지 조회하기
-- GROUP BY country로 지역별로 그룹을 나눔
-- 각 지역별로 그룹이 나뉘어졌기 때문에 COUNT(*)는 지역별 데이터 개수를 세게 됨
SELECT country, COUNT(*) FROM users
GROUP BY country;
-- 각 성씨가 몇 명씩 있는지 조회하기
SELECT last_name, COUNT(*) FROM users
GROUP BY last_name;
-- 각 성씨가 몇 명씩 있는지 조회하기
-- AS 키워드를 사용해 컬럼명을 임시로 변경하여 조회할 수 있음
SELECT last_name, COUNT(*) AS number_of_name FROM users
GROUP BY last_name;
-- 인원이 가장 많은 성씨 순으로 조회하기
SELECT last_name, COUNT(*) FROM users
GROUP BY last_name ORDER BY COUNT(*) DESC;
-- 각 지역별 평균 나이 조회하기
SELECT country, AVG(age) FROM users
GROUP BY country;

-- CUD

-- CREATE
CREATE TABLE classmates (
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    address TEXT NOT NULL
);

-- INSERT
INSERT INTO classmates (name, age, address)
VALUES ('홍길동', 23, '서울');
-- 여러 행 삽입하기
INSERT INTO classmates
VALUES
    ('김철수', 30, '경기'),
    ('이영미', 31, '강원'),
    ('박진성', 26, '전라'),
    ('최지수', 12, '충청'),
    ('정요한', 28, '경상');

-- UPDATE
-- 2번 데이터의 이름을 '김철수한무두루미', 주소를 '제주도'로 수정하기
UPDATE classmates
SET name = '김철수한무두루미',
    address = '제주도'
WHERE rowid = 2;

-- DELETE
-- 5번 데이터 삭제하기
DELETE FROM classmates
WHERE rowid = 5;
-- 삭제된 것 확인하기
SELECT rowid, * FROM classmates;
-- 이름에 '영'이 포함되는 데이터 삭제하기
DELETE FROM classmates
WHERE name LIKE '%영%';
-- 테이블의 모든 데이터 삭제하기
DELETE FROM classmates;
```

---

# QuerySet API Advanced

## CRUD

### 모든 user 레코드 조회

- `User.objects.all()`

### 101번 user 레코드 조회

- `User.objects.get(pk=101)`

### 101번 user 레코드의 last_name을 ‘김’으로 수정

- `user = User.objects.get(pk=101)`
  - `user.last_name = '김'`
    - `user.save()`

### 101번 user 레코드 삭제

- `user = User.objects.get(pk=101)`
  - `user.delete()`

### 전체 인원 수 조회

1. `User.objects.count()`
   - `***.count()***`
     - QuerySet과 일치하는 데이터베이스의 개체 수를 나타내는 정수를 반환
     - `.all()` 을 사용하지 않아도 됨
2. `len(User.objects.all())`

## Sorting Data

### 나이가 어린 순으로 이름과 나이 조회

- `User.objects.order_by('age').values('first_name', 'age')`
  - `***order_by()***`
    - `.order_by(*fields)`
      - QuerySet의 정렬을 재정의
        - 기본적으로 오름차순으로 정렬하며
        - **_필드명에 hyphen(`-`)을 작성하면 내림차순으로 정렬_**
          - **_인자로 (`?`)를 입력하면 랜덤으로 정렬_**
    - order_by 주의사항
      - `User.objects.order_by('balance').order_by('-age')`
        - 다음과 같이 작성할 경우 앞의 호출은 모두 지워지고 마지막 호출만 적용됨
          - `User.objects.order_by('-age')` 와 같음
  - `***values()***`
    - `.values(*fields, **expressions)`
      - 모델 인스턴스가 아닌 딕셔너리 요소들을 가진 QuerySet을 반환
      - `*fields` 는 선택인자이며, 조회하고자 하는 필드명을 가변인자로 받음
        - 필드를 지정하면 각 딕셔너리에는 지정한 필드에 대한 key와 value만을 출력
        - 입력하지 않을 경우 각 딕셔너리에는 레코드의 모든 필드에 대한 key와 value를 출력
  - values 사용 여부에 따른 출력 비교
    <img width="1061" alt="db45" src="https://user-images.githubusercontent.com/86648892/212546081-5f88479f-6cd3-40f7-98b0-6162bcff4756.png">

### 이름과 나이를 나이가 많은 순서대로 조회

- `User.objects.order_by('-age').values('first_name', 'age')`

### 이름, 나이, 계좌 잔고를 나이가 어린순으로, 만약 같은 나이라면 계좌 잔고가 많은 순으로 정렬해서 조회

- `User.objects.order_by('age', '-balance').values('first_name', 'age', 'balance')`

## Filtering Data

### 중복없이 모든 지역 조회

- `User.objects.distinct().values('country')`

### 지역 순으로 오름차순 정렬하여 중복없이 모든 지역 조회

- `User.objects.distict().values('country').order_by('country')`

### 이름과 지역 중복없이 모든 이름과 지역 조회

- `User.objects.distinct().values('first_name', 'country')`

### 이름과 지역 중복없이 오름차순 정렬하여 모든 이름과 지역 조회

- `User.objects.distinct().values('first_name', 'country').order_by('country')`

### 나이가 30살인 사람들의 이름 조회

- `User.objects.filter(age=30).values('first_name')`

### 나이가 30살 이상인 사람들의 이름과 나이 조회

- `User.objects.filter(age__gte=30).values(’first_name’, ‘age’)`

### 나이가 30살 이상이고 계좌 잔고가 50만원 초과인 사람들의 이름, 나이, 계좌 잔고 조회

- `User.objects.filter(age__gte=30, balance__gt=500000).values(’first_name’, ‘age’, ‘balance’)`

### 이름에 ‘호’가 포함되는 사람들의 이름과 성 조회

- `User.objects.filter(first_name__contains='호').values('first_name', 'last_name')`

### 핸드폰 번호가 011로 시작하는 사람들의 이름과 핸드폰 번호 조회

- `User.objects.filter(phone__startswith='011-').values('first_name', 'phone')`
  - SQL에서의 `%` 와일드카드와 같음
  - `_`(underscore)는 별도로 정규 표현식을 사용해야함

### 이름이 ‘준’으로 끝나는 사람들의 이름 조회

- `User.objects.filter(first_name__endswith='준').values('first_name')`

### 경기도 혹은 강원도에 사는 사람들의 이름과 지역 조회

- `User.objects.filter(country__in=['경기도', ‘강원도’]).values(’first_name’, ‘country’)`

### 경기도 혹은 강원도에 살지 않는 사람들의 이름과 지역 조회

- `User.objects.exclude(country__in=['경기도', '강원도']).values('first_name', 'country')`
  - `***exclude()***`
    - `exclude(**kwargs)`
      - 주어진 매개변수와 일치하지 않는 객체를 포함하는 QuerySet 반환

### 나이가 가장 어린 10명의 이름과 나이 조회

- `User.objects.order_by('age').values('first_name', 'age')[:10]`

### 나이가 30이거나 성이 김씨인 사람들 조회

```python
# shell_plus에서는 import문 생략 가능
from django.db.models import Q
User.objects.filter(Q(age=30) | Q(last_name='김'))
```

- **`Q` object**

  - [https://docs.djangoproject.com/en/4.1/topics/db/queries/#complex-lookups-with-q-objects](https://docs.djangoproject.com/en/4.1/topics/db/queries/#complex-lookups-with-q-objects)
  - 기본적으로 filter()와 같은 메서드의 키워드 인자는 AND statement를 따름
  - 만약 더 복잡한 쿼리를 실행해야하는 경우가 있다면 Q 객체가 필요함

  ```python
  # 예시
  from django.db.models import Q
  Q(question__startswith='What')

  # & 및 | 를 사용하여 Q 객체를 결합할 수 있음
  Q(question__startswith='Who') | Q(question__startswith='What')

  # 조회를 하면서 여러 Q 객체를 제공할 수도 있음
  Article.objects.get(
  	Q(title__startswith='Who',
  	Q(created_at=date(2005, 5, 2)) | Q(created_at=date(2005, 5, 6))
  )
  ```

## Aggregation (Grouping Data)

### `aggregate()`

- “Aggregate calculates values for the entire queryset”
- 전체 queryset에 대한 값을 계산
- 특정 필드 전체의 합, 평균, 개수 등을 계산할 때 사용
- **_딕셔너리를 반환_**
- Aggregate Functions
  - `Avg` , `Count` , `Max` , `Min` , `Sum` 등
  - [https://docs.djangoproject.com/en/4.1/topics/db/aggregation/#](https://docs.djangoproject.com/en/4.1/topics/db/aggregation/#)

### 나이가 30살 이상인 사람들의 평균 나이 조회

```python
from django.db.models import Avg
User.objects.filter(age__gte=30).aggregate(Avg('age'))
# {'age__avg': 37.65909090909091}

# 딕셔너리 key 값을 수정 가능
User.objects.filter(age__gte=30).aggregate(avg_value=Avg('age'))
# {'avg_value': 37.65909090909091}
```

### 가장 높은 계좌 잔액 조회

```python
from django.db.models import Max
User.objects.aggregate(Max('balance'))
# {'balance__max': 1000000}
```

### 모든 계좌 잔액 총액 조회

```python
from django.db.models import Sum
User.objects.aggregate(Sum('balance'))
# {'balance__sum': 14435040}
```

### `annotate()`

- 쿼리의 각 항목에 대한 요약 값을 계산
- SQL의 `GROUP BY` 에 해당
- “주석을 단다”라는 뜻
  - 어떠한 데이터를 조회하면서 추가 정보를 덧붙이는 것
  - 데이터에 존재하는 컬럼이 아니라 계산을 통해서 만들어낸 것
    - 테이블 입장에서는 잠깐 주석이 붙은 것
  - 요약값을 만드는 것이기에 Aggregate Functions와 함께 사용

### 각 지역별로 몇명씩 살고 있는지 조회

```python
from django.db.models import Count
User.objects.values('country').annotate(Count('country'))

"""
<QuerySet [
	{'country': '강원도', 'country__count': 14},
	{'country': '경기도', 'country__count': 9},
	{'country': '경상남도', 'country__count': 9},
	...
]>
"""

# aggregate와 마찬가지로 딕셔너리의 key 값을 변경 가능

from django.db.models import Count
User.objects.values('country').annotate(num_of_country=Count('country'))

"""
<QuerySet [
	{'country': '강원도', 'num_of_country': 14},
	{'country': '경기도', 'num_of_country': 9},
	{'country': '경상남도', 'num_of_country': 9},
	...
]>
"""
```

### 각 지역별로 몇명씩 살고 있는지 + 지역별 계좌 잔액 평균 조회

```python
# 한번에 여러 값을 계산해 조회 가능
User.objects.values('country').annotate(Count('country'), avg_balance=Avg('balance'))
```

### 각 성씨가 몇명씩 있는지 조회

- `User.objects.values('last_name').annotate(Count('last_name'))`

### N:1 예시

```python
# Comment-Article의 관계가 N:1인 경우

Article.objects.annotate(
	number_of_comment=Count('comment'),
	pub_date=Count('comment', filter=Q(comment__created_at__lte='2000-01-01'))
)
```

- 전체 게시글을 조회하면서 (`Article.objects.all()`)
  - annotate로 각 게시글의 댓글 개수(`number_of_comment`)와
    - 2000-01-01보다 나중에 작성된 댓글의 개수(`pub_date`)를 함께 조회하는 것

---

# Django

# Django Intro

- Django는 Full-stack Framework이다
  - Full-stack이란 프론트엔드와 백엔드를 합친 것
  - 즉, Django는 프론트와 서버 모두를 개발할 수 있는 프레임워크이다
    - 그러나 현업에서는 백엔드로만 주로 사용된다
  - 프론트엔드로는 자바스크립트 기반 프론트 프레임워크인 Vue.js를 많이 사용한다

### Framework란?

- 서비스 개발에 필요한 기능들을 미리 구현해서 모아놓은 것
- Frame + Work
  - 일정한 뼈대, 틀을 가지고 일하다
  - 제공받은 도구들과 뼈대, 규약을 가지고 무언가를 만드는 일
  - 특정 프로그램을 개발하기 위한 여러 도구들과 규약을 제공하는 것
  - “소프트웨어 프레임워크"는 복잡한 문제를 해결하거나 서술하는데 사용되는 기본 개념 구조
- 장점
  - 잘 사용하면 내가 만들고자 하는 본질(로직)에 집중하여 개발할 수 있음
  - 소프트웨어의 생산성과 품질을 높임

### Web Frameworks

- 2020 Github Stars 기준

<img width="364" alt="dj_1" src="https://user-images.githubusercontent.com/86648892/188303732-f321deca-c770-45eb-9599-74be2cbad55a.png">

<img width="364" alt="dj_2" src="https://user-images.githubusercontent.com/86648892/188303735-49e07db5-23c2-41e1-bca5-fbc7a561243e.png">

- Django의 장점
  - Django는 Python으로 작성된 프레임워크
    - Python이라는 언어의 강력함과 거대한 커뮤니티
  - 수많은 유용한 기능들
  - 검증된 웹 프레임워크
    - 화해, Toss, 두나무, 당근마켓, 요기요 등
      - 유명한 서비스들이 사용한다는 것은 곧 안정적인 서비스가 가능하다는 것

---

## WEB

### WWW(World Wide Web)

- 인터넷이란 전세계에 퍼져있는 거미줄같은 연결망
  - 실제로 해저케이블로 전세계는 연결되어 있음
    - Space X의 “스타링크 프로젝트"는 이러한 유선 연결을 넘어 무선 연결을 추구
- 인터넷을 이용한다는 것은 결국 전세계의 컴퓨터가 연결되어 있는 하나의 인프라를 이용하는 것

## 클라이언트와 서버

<img width="773" alt="dj_3" src="https://user-images.githubusercontent.com/86648892/188303737-89466c50-92bb-40ab-8c60-f802b075c2f9.png">

### 클라이언트

- 웹 사용자의 인터넷에 연결된 장치 (wi-fi에 연결된 컴퓨터 또는 모바일 등)
- Chrome 또는 Firefox와 같은 웹 브라우저
- **_서비스를 요청하는 주체_**

### 서버

- 웹 페이지, 사이트 또는 앱을 저장하는 컴퓨터
- 클라이언트가 웹 페이지에 접근하려고할 때
  - 서버에서 클라이언트 컴퓨터로 웹 페이지 데이터를 응답해 사용자의 웹 브라우저에 표시됨
- **_요청에 대해 서비스를 응답하는 주체_**

### 클라이언트-서버

- Google 홈페이지에 접속한다는 것은?
  - 클라이언트에서 인터넷에 연결되어 있는 구글 컴퓨터에게
    - Google 홈페이지 html 달라고 요청
      - 구글 컴퓨터는 요청에 따라 인터넷을 통해 html 반환
        - 반환받은 html 파일을 브라우저가 렌더링하여 보여줌
- 결국 어떠한 자원(resource)을 요청(request)하는 것은 클라이언트, 자원을 제공하는 쪽은 서버(server)
- 웹은 클라이언트-서버 구조
  - Django는 서버 구현에 사용됨

---

## Web browser와 Web page

### Web browser?

- 웹에서 **페이지를 찾아 보여주고**, **사용자가 하이퍼링크를 통해 다른 페이지로 이동**할 수 있도록 하는 프로그램
- 웹 페이지 파일을 우리가 보는 화면으로 렌더링(rendering)하는 프로그램

### Web page?

- 웹에 있는 문서로 우리가 보는 화면 하나하나가 웹 페이지

### Web page 종류

- 정적 웹 페이지
  - Static Web Page
  - 있는 그대로를 제공하는 것(served as-is)
  - 한 번 작성된 html 파일의 내용이 변하지 않고 모든 사용자에게 동일한 모습으로 전달되는 것
  - 서버에 미리 저장된 HTML 파일 그대로 전달된 웹 페이지
- 동적 웹 페이지
  - Dynamic Web Page
  - 사용자와 요청에 따라 웹 페이지에 추가적인 수정이 되어 클라이언트에게 전달되는 웹 페이지
    - 웹 페이지의 내용을 바꿔주는 주체가 서버(server)
      - 서버에서 동작하고 있는 프로그램이 웹 페이지를 변경해줌
  - **_사용자의 요청에 따라 적절한 응답을 만들어주는 프로그램_**을 만들어야한다!
    - 파일을 처리하고, 데이터베이스와 상호작용
    - 이를 쉽게 할 수 있도록 도와주는 프레임워크가 Django

---

# MTV Design Pattern

## Design Pattern

- Design Pattern이란 자주 사용되는 구조가 있다는 것을 알게 되고, 이를 일반화해서 하나의 공법으로 만들어둔 것
- 소프트웨어에서의 Design Pattern
  - 설계 문제의 처리 과정에서의 유사점을 패턴이라 한다
  - 클라이언트-서버 구조도 소프트웨어 디자인 패턴 중 하나

## Design Pattern의 목적

- 특정 문맥에서 공통적으로 발생하는 문제에 대해 재사용 가능한 해결책 제시
- 프로그래머가 어플리케이션이나 시스템을 디자인할 때 발생하는 공통된 문제들을 해결하는데 형식화된 가장 좋은 관행
- 커뮤니케이션이 간단해짐
  - “우리 이거 클라이언트-서버 구조로 개발하자”
  - 다수의 엔지니어들이 일반화된 패턴으로 소프트웨어 개발을 할 수 있도록 한 규칙, 커뮤니케이션의 효율성을 높이는 기법

---

## MTV Design Pattern

- Model - Template - View
- Django에서의 디자인 패턴
- MVC 디자인 패턴을 기반으로 조금 변형된 패턴

### MVC 디자인 패턴

- Model - View- Controller
- 데이터 및 논리 제어를 구현하는데 널리 사용되는 소프트웨어 디자인 패턴
- 하나의 프로그램을 3가지 역할로 구분한 개발 방법론
  1. Model: 데이터와 관련된 로직을 관리
  2. View: 레이아웃과 화면을 처리
  3. Controller: 명령을 model과 view부분으로 연결

### MVC 디자인 패턴의 목적

- “관심사 분리”
- 더 나은 업무의 분리와 향상된 관리 제공
- 각 부분을 독립적으로 개발할 수 있어, 하나를 수정하고 싶을 때 모두 건들지 않아도 됨
  - 개발 효율성 및 유지보수가 쉬워짐
  - 다수의 멤버로 개발하기 용이함

## MTV 디자인 패턴

<img width="1084" alt="dj_4" src="https://user-images.githubusercontent.com/86648892/188303738-cf774953-b658-492a-950c-445c3ad2600d.png">

### Model

- 데이터와 관련된 로직을 관리
- 프로그램의 **_데이터 구조를 정의_**하고, **_데이터베이스의 기록을 관리_**

### Template

- 레이아웃과 화면을 처리
- 화면상의 사용자 인터페이스 구조와 레이아웃을 정의

### View

- Model, Template과 관련한 로직을 처리해서 응답을 반환
- 클라이언트의 요청에 대해 처리를 분기하는 역할
  - Request → URL 주소를 보고 어디로(Template) 요청을 보내야할지 판단 → View가 필요한 데이터가 있을 시 Model과 소통 → Model에서 데이터를 가져오고 → 해당 Template으로 보내 화면을 구성하고 → 구성된 화면을 응답으로 클라이언트에게 반환
- 중간처리와 응답반환을 한다고 생각하면 된다

<img width="700" alt="dj_5" src="https://user-images.githubusercontent.com/86648892/188303740-506ea720-0375-42cf-94b8-6b8fbe43791d.png">

---

# Django 환경설정

- **_설치 전 가상환경 설정 및 활성화를 마치고 진행_**

## Virtual Environment

### 가상환경 설정

- `python -m venv venv`
  - 가상환경을 만들 것(-m venv)이고 그 이름은 venv
- `source ./venv/Scripts/activate`
  - 가상환경 활성화
  - 맥에서는 venv의 하위 폴더로 bin이 잡혀있는 경우가 있으므로 확인
    - `source venv/bin/activate`
    - 맥 가상환경의 경우 pyenv 사용을 알아보자

## Package

### 패키지 설치

- `$ pip list`
  - 현재 가상환경 내 설치된 모듈 확인
- `$ pip install`
  - `$ pip install django==3.2.13`
    - Django 설치
      - Django와 Django에 필요한 다른 것들도 설치되었음을 확인 가능
    - Django 4.0 릴리즈로 인해 3.2(LTS) 버전을 명시해서 설치
      - LTS(Long Term Support)란 장기 지원 버전으로, 일반적인 경우보다 장기간에 걸쳐 지원하도록 고안된 소프트웨어의 버전
        - 컴퓨터 소프트웨어의 제품 수명주기 관리 정책
        - 배포자는 LTS 확정을 통해 장기적이고 안정적인 지원을 보장함
  - `$ pip install ipython`
  - `$ pip install django-extensions`
    - `settings.py` 의 `INSTALLED_APPS`에 `django_extensions` 추가 필수!
      - 추가할 때 언더바인점 주의

### 패키지 목록 생성

- `pip freeze > requirements.txt`
  - `pip install -r requirements.txt`
    - 현재 있는 `requirements.txt` 파일을 바탕으로 recursive하게 패키지를 다운받아줄 것이다

## Project

### 프로젝트 생성

- `$ django-admin startproject firstpjt .`
  - `.` 은 현재 디렉토리를 의미하는 것으로 현재 디렉토리 내에 바로 프로젝트 디렉토리를 생성하게 됨
    - 붙이지 않는다면 `firstpjt` 라는 이름의 껍데기 폴더가 생성되고 그 안에 프로젝트 디렉토리가 생성되어 불편함
  - 프로젝트 이름에는 Python이나 Django에서 사용 중인 키워드 및 ‘-’(하이픈) 사용 불가

### 서버 실행

- `python manage.py runserver`
  - url을 `ctrl+클릭` 하면 로켓화면 확인가능
  - 서버종료는 `ctrl+c`

### 프로젝트 구조

<img width="439" alt="dj_6" src="https://user-images.githubusercontent.com/86648892/188303741-32b2ad55-9c0e-4b45-bf61-9fedbfcf3157.png">

- `manage.py`
  - Django 프로젝트 전반에 대한 명령을 내릴 수 있는 파일
  - Django 프로젝트와 다양한 방법으로 상호작용하는 커맨드라인 유틸리티
  - `$ python manage.py <command> [options]`
- `firstpjt`
  - `__init__.py`
    - 패키지로 인식시키는 파일
    - Python에게 이 디렉토리를 하나의 Python 패키지로 다루도록 지시
    - 별도로 추가 코드를 작성하지 않음
  - `asgi.py`
    - Asynchronous Server Gateway Interface
    - Django 애플리케이션이 비동기식 웹 서버와 연결 및 소통하는 것을 도움
    - 추후 배포 시에 사용
  - `settings.py`
    - Django 프로젝트 전반에 대한 설정을 관리
    - `SECRET_KEY` 는 프로젝트 고유 키 값
  - `urls.py`
    - 사이트의 url과 적절한 views의 연결을 지정
    - `urlpatterns` 에 어떤 url이 들어오면 어떤 처리를 하라는 것을 지정
  - `wsgi.py`
    - Web Server Gateway Interface
    - Django 애플리케이션이 웹 서버와 연결 및 소통하는 것을 도움
    - 추후 배포 시에 사용
- `db.sqlite3`
  - 향후 데이터베이스 생성 시 생성됨
  - 데이터베이스
    - 데이터가 들어있는 곳

## Application

### 어플리케이션 생성

- 프로젝트 내에 기능 단위로 여러 개의 앱이 들어갈 수 있다
  - ex) 회원 관련, 게시글 관련, 결제 관련 등등
  - 싱글앱, 멀티앱은 개발방식 선호의 차이
- `$ python manage.py startapp articles`
  - articles라는 앱을 만든다
  - 일반적으로 어플리케이션의 이름은 ‘복수형'으로 작성하는 것을 권장
- `settings.py` 의 `INSTALLED_APPS` 에 추가
  - 참고) third party apps는 `pip install` 해서 받은 것들

### 어플리케이션 구조

<img width="372" alt="dj_7" src="https://user-images.githubusercontent.com/86648892/188303742-c9b71a00-766d-4b85-ac78-45d870ac1cd1.png">

- `admin.py`
  - 관리자용 페이지를 설정하는 곳
- `apps.py`
  - 앱의 정보가 작성된 곳
  - 별도로 추가 코드를 작성하지 않음
- `models.py`
  - 애플리케이션에서 사용하는 Model을 정의하는 곳
  - MTV 패턴의 M에 해당
- `tests.py`
  - 프로젝트의 테스트 코드를 작성하는 곳
- `views.py`
  - view 함수들이 정의되는 곳
  - MTV 패턴의 V에 해당
- `migrations`
  - 데이터베이스 변경 히스토리가 모여있는 곳

### 어플리케이션 등록

<img width="567" alt="dj_8" src="https://user-images.githubusercontent.com/86648892/188303743-da8633ea-d299-4e17-bf30-57f9e7ab564d.png">

- 프로젝트에서 앱을 사용하기 위해서는 반드시 `INSTALLED_APPS` 리스트에 추가해야 함
  - `INSTALLED_APPS`는 Django Installation에 활성화된 모든 앱을 지정하는 문자열 목록
- 반드시 생성 후 등록
  - `INSTALLED_APPS` 에 먼저 작성하고 생성하려면 앱이 생성되지 않음

<img width="509" alt="dj_9" src="https://user-images.githubusercontent.com/86648892/188303744-d3d96988-9fc3-424c-a058-5785353e6d7f.png">

- Local apps - Third party apps - Django apps 순서
  - 해당 순서를 지키지 않아도 당장은 문제가 없으나, 추후 advanced한 내용을 다룰 시를 대비하여 지키는 것을 권장

## Project & Application 정리

### Project

- “collection of apps”
- 프로젝트는 앱의 집합
- 프로젝트에는 여러 앱이 포함될 수 있음
- 앱은 여러 프로젝트에 있을 수 있음

### Application

- 앱은 실제 요청을 처리하고 페이지를 보여주는 등의 역할을 담당
- 일반적으로 앱은 하나의 역할 및 기능 단위로 작성하는 것을 권장함

---

# 요청과 응답

- 설계 순서
  1. url 설계
  2. 그에 맞는 view 설계
  3. model, template 설계

### URLs

<img width="457" alt="dj_10" src="https://user-images.githubusercontent.com/86648892/188303745-71b9698d-1198-4d96-8622-806058623eff.png">

- `path('index/', views.index)`
  - index라는 경로로 들어오면 views에 있는 기능을 수행해주면 된다는 명령
  - `views.index` 를 사용하기 위해 `from articles import views` 필요

### View

<img width="491" alt="dj_11" src="https://user-images.githubusercontent.com/86648892/188303747-52599cb4-44be-4bf7-8c68-42c10296c0ba.png">

- browser의 url → `urls.py` → `views.py` → `index()`
  - `index(request)` 내의 request 파라미터에 django가 알아서 request를 넣어서 넘겨줌
- HTTP 요청을 수신하고 HTTP 응답을 반환하는 함수 작성
- Template에게 HTTP 응답 서식을 맡김

<img width="998" alt="dj_12" src="https://user-images.githubusercontent.com/86648892/188303748-1570ac25-78dc-41ff-8bce-16d976ca4bc8.png">

- `templates` 디렉토리 생성 및 `index.html` 파일 생성
- `return render(request, 'index.html')`
  - 해당 request에 대하여 index.html파일을 렌더링해줘
  - context는 data라고 생각하자
  - `settings.py` 에 TEMPLATES
    - 여기에 `APP_DIRS` 에 `True` 가 기본값으로 설정되어있어 articles 앱 내부의 template을 인식할 수 있음
    - **_그 외 따로 디렉토리를 만들어 인식시켜주고 싶을 경우 `DIRS`에 정의_**

### Templates

<img width="481" alt="dj_13" src="https://user-images.githubusercontent.com/86648892/188303749-f15779c7-5b32-40d2-847d-aff5f28ee02f.png">

- 실제 내용을 보여주는데 사용되는 파일
- 파일의 구조나 레이아웃을 정의
- `app_name/templates/`
  - 템플릿 폴더의 이름은 반드시 **templates**라고 지정해야함

### 코드 작성 순서

<img width="1054" alt="dj_14" src="https://user-images.githubusercontent.com/86648892/188303752-ae37cfb7-5802-44f0-b0af-16d3724df1b4.png">

---

## 추가 설정

- `settings.py` 에서 설정

### LANGUAGE_CODE

- 모든 사용자에게 제공되는 번역을 결정
- 이 설정이 적용되려면 `USE_I18N` 이 활성화(True)되어 있어야함
- [Unicode Language Identifiers](http://www.i18nguy.com/unicode/language-identifiers.html)

### TIME_ZONE

- 데이터베이스 연결의 시간대를 나타내는 문자열 지정
- `USE_TZ` 가 True이고 이 옵션이 설정된 경우 데이터베이스에서 날짜 시간을 읽으면, UTC 대신 새로 설정한 시간대의 인식 날짜&시간이 반환됨
- `USE_TZ` 가 False인 상태로 이 값을 설정하는 것은 error가 발생하므로 주의
- [List of TZ Database Time Zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)

### USE_I18N

- Django의 번역 시스템을 활성화해야하는지 여부를 지정

### USE_L10N

- 데이터의 지역화된 형식(localized formatting)을 기본적으로 활성화할지 여부를 지정
- True일 경우, Django는 현재 locale의 형식을 사용하여 숫자와 날짜를 표시

### USE_TZ

- datetimes가 기본적으로 시간대를 인식하는지 여부를 지정
- True일 경우 Django는 내부적으로 시간대 인식 날짜 / 시간을 사용

## 유용한 VSCode Extensions

- Django
- Excel Viewer
- SQLite
- Material Icon Theme

---

# Django Template

## Django Template

- Template System의 기본 목표를 숙지하자
  - **_데이터 표현을 제어하는 도구이자 표현에 관련된 로직_**
  - Django Template을 이용한 HTML 정적 부분과 동적 컨텐츠 삽입

## DTL(Django Template Language)

- Django template에서 사용하는 built-in template system
  - html 파일을 조금 더 쉽게 만들어주는 Django만의 문법
    - 실무에서는 잘 사용하지 않는다
- 조건, 반복, 변수 치환, 필터 등의 기능을 제공
  - Python처럼 일부 프로그래밍 구조(if, for 등)를 사용할 수 있지만 이것은 **_Python 코드로 실행되는 것이 아님_**
  - Django 템플릿 시스템은 단순히 Python이 아닌 HTML에 포함된 것이 아니니 주의
- 프로그래밍적 로직이 아니라 프레젠테이션을 표현하기위한 것임을 명심할 것

## DTL Syntax

### Variable

- `{{ variable }}`
  - 변수명은 영어, 숫자와 밑줄(`_`)의 조합으로 구성될 수 있으나 밑줄로는 시작할 수 없음
    - 공백이나 구두점 문자 또한 사용할 수 없음
  - `.` 을 사용하여 변수 속성에 접근할 수 있음
  - `render()` 의 세번째 인자로 `{'key': value}` 와 같이 딕셔너리 형태로 넘겨주며, 여기서 정의한 key에 해당하는 문자열이 template에서 사용가능한 변수명이 됨
    - `views` 에의 함수 내에서 `models` 로부터 받아온 데이터를 바탕으로 ,보통 `context` 라는 이름으로 딕셔너리를 정의하여 이 정보를 연결된 `templates` 파일에 넘겨줌

### Filters

- `{{ variable|filter }}`
  - 표시할 변수를 수정할 때 사용
  - 예시
    - `{{ name|lower }}`
      - name 변수를 모두 소문자로 출력
  - 60개의 built-in template filters를 제공
  - chained가 가능하며 일부 필터는 인자를 받기도 함
    - `{{ name|truncatewords:30 }}`

### Tags

- `{% tag %}`
  - 출력 텍스트를 만들거나, 반복 또는 논리를 수행하여 제어 흐름을 만드는 등 변수보다 복잡한 일들을 수행
  - 일부 태그는 시작과 종료 태그가 필요
    - `{% if %} {% endif %}`
  - 약 24개의 built-in template tags를 제공

### Comments

- `{# #}`
  - Django template에서 라인의 주석을 표현하기 위해 사용
  - 아래처럼 유효하지 않은 템플릿 코드가 포함될 수 있음
    - `{# {% if %} text {% endif %} #}`
- `{% comment %} {% endcomment %}`
  - 여러 줄 주석에 사용

<img width="1231" alt="dj_15" src="https://user-images.githubusercontent.com/86648892/188303753-c3605294-4d31-45b6-a899-d69707ed3392.png">

<img width="1238" alt="dj_16" src="https://user-images.githubusercontent.com/86648892/188303754-60f618fe-f462-488e-aec3-d4033311dffd.png">

<img width="1230" alt="dj_17" src="https://user-images.githubusercontent.com/86648892/188303755-3cd42d50-db74-4d92-9ae9-30a596bbd466.png">

<img width="1222" alt="dj_18" src="https://user-images.githubusercontent.com/86648892/188303756-b66d9a18-7863-4ff4-8cfc-15e3a90be021.png">

<img width="1210" alt="dj_19" src="https://user-images.githubusercontent.com/86648892/188303757-286705a5-69de-4a7f-b99e-f656c588e327.png">

---

## Trailing URL Slashes (참고)

- Django에서는 trailing slash 옵션이 True
  - Django는 URL 끝에 `/` 가 없다면 자동으로 붙여주는 것이 기본 설정
    - 그래서 모든 주소가 `/` 로 끝나도록 구성되어있음
    - 모든 프레임워크가 이렇게 동작하는 것은 아님
    - 검색 엔진 로봇이나 웹 트래픽 분석 도구에서는 `/` 이 붙은 것과 붙지 않은 것을 다른 페이지로 보며, Django는 URL을 정규화하여 검색 엔진 로봇이 혼동하지 않도록 함
  - url을 적어줄 때 끝에 `/` 를 붙여주자
  - [Trailing URL Slashes?](https://djkeh.github.io/articles/Why-do-we-put-slash-at-the-end-of-URL-kor/)
- 앞에 `/` 는 현재 슬래시가 시작점이라는 의미
  - `/index/` 로 anchoring하면
    - `greetings/index/` 와 같이 현재 url에서 index라는 path를 덧붙여주는 형태로 됨

---

## Template Interitance

### 템플릿 상속

- 기본 ‘skeleton’ 템플릿을 만들어
  - 사이트의 모든 공통 요소를 포함하고, 하위 템플릿이 재정의(override)할 수 있는 블록을 정의
  - 코드의 재사용성
- `base.html`
  - base라는 이름의 skeleton 템플릿 작성
  - `base.html` 에서 바뀌어야될 부분은 block으로 구멍을 뚫어줌
  - `base.html` 을 상속받는 템플릿은 `{% extends base.html %}` 을 통해 상속받음을 선언하고, 같은 이름의 block 태그를 선언 뒤, 해당 block 태그 내에 추가할 부분을 작성

<img width="1194" alt="dj_20" src="https://user-images.githubusercontent.com/86648892/188303759-35b15e9c-0146-4f2d-b2ee-54c2f71c0bb6.png">

### 추가 템플릿 경로 추가하기

<img width="1210" alt="dj_21" src="https://user-images.githubusercontent.com/86648892/188303760-b489e68f-b076-4cc7-ab55-d86415d65756.png">

- `settings.py` 의 DIRS에 추가하여 너 templates 찾을 때 이쪽도 찾아달라고 명령
  - `BASE_DIR` 은 프로젝트 홈 디렉토리를 가리키도록 설정해놓은 값
  - `BASE_DIR / templates`
    - 홈 디렉토리 바로 하위에 있는 templates
    - trailing comma 써주는 습관을 들이자

### BASE_DIR

- `settings.py`
  - `BASE_DIR = Path(__file__).resolve().parent.parent`
  - `settings.py` 에서 특정 경로를 절대경로로 편하게 작성할 수 있도록 Django에서 미리 지정해둔 경로 값
  - “객체 지향 파일 시스템 경로”
    - 운영체제별로 파일 경로 표기법이 다르기 때문에 어떤 운영체제에서 실행되더라도 각 운영체제 표기법에 맞게 해석될 수 있도록 하기 위해 사용
    - [Python Docs Pathlib](https://docs.python.org/3/library/pathlib.html)

---

# Sending and Retrieving form data

### `<form></form>`

- form 태그
- WEB에서 사용자 Input을 받는 방법
- `<form target="_blank">`
  - 새 탭에서 열기

## Client & Server Architecture

<img width="522" alt="dj_22" src="https://user-images.githubusercontent.com/86648892/188303762-08c454f8-1b8a-4944-b929-55c18658df79.png">

- 웹은 기본적으로 클라이언트-서버 아키텍처를 사용
  - 클라이언트(일반적으로 웹 브라우저)가 서버에 요청을 보내고, 서버는 클라이언트의 요청에 응답
- 클라이언트 측에서 **_HTML form_**은 HTTP 요청을 서버에 보내는 가장 편리한 방법
- 이를 통해 **_사용자는 HTTP 요청에서 전달할 정보를 제공_**할 수 있음

## Sending form data (Client)

### HTML <form> element

- 데이터가 전송되는 방법을 정의
- 웹에서 사용자 정보를 입력하는 여러 방식(text, button, submit 등)을 제공하고, **_사용자로부터 할당된 데이터를 서버로 전송_**하는 역할을 담당
- “데이터를 어디(action)로 어떤 방식(method)으로 보낼지”
  - 핵심 속성
    - action
    - method

### HTML form’s attributes

1. **_action_**
   - 입력 데이터가 전송될 URL을 지정
   - 데이터를 어디로 보낼 것인지 지정하는 것이며 이 값은 반드시 유효한 URL이어야함
   - 만약 이 속성을 지정하지 않으면 데이터는 현재 form이 있는 페이지의 URL로 보내짐
2. **_method_**
   - 데이터를 어떻게 보낼 것인지 정의
   - 입력 데이터의 HTTP request methods를 지정
     - HTML form 데이터는 GET, POST 2가지 방법으로만 전송할 수 있음
     - READ 시 `GET`
     - CREATE, UPDATE, DELETE 시 `POST`
   - 정의하지 않을 시 기본값 GET 적용

### HTML <input> element

- 사용자로부터 데이터를 입력받기 위해 사용
- `type` 속성에 따라 동작 방식이 달라짐
  - input 요소의 동작 방식은 type 특성에 따라 현격히 달라지므로 MDN 문서 참고하여 사용
  - 지정하지 않은 경우 기본값은 text
- `<label>`과 주로 함께 사용하여 label의 `for` 과 input의 `id` 가 연결
- input의 `name` 속성
  - form을 통해 데이터를 제출(submit)했을 때 name 속성에 설정된 값을 서버로 전송하고, 서버는 name 속성에 설정된 값을 통해 사용자가 입력한 데이터 값에 접근할 수 있음
    - 즉, name 속성이 요청 데이터의 key값이 됨
    - GET, POST 방식으로 서버에 전달하는 파라미터(name은 key, value는 value)로 매핑
      - GET 방식에서는 URL에서 `?key=value&key=value/` 형식으로 데이터를 전달

### HTTP request methods

- HTTP
  - HTML 문서와 같은 리소스(데이터, 자원)들을 가져올 수 있도록 해주는 프로토콜(규칙)
  - 웹에서 이루어지는 모든 데이터 교환의 기초
  - HTTP는 주어진 리소스가 수행할 원하는 작업을 나타내는 request methods를 정의
- HTTP request methods
  - 자원에 대한 행위(수행하고자 하는 동작)을 정의
  - GET, POST, PUT, DELETE
  - GET
    - 서버로부터 정보를 **_조회_**하는데 사용
      - 즉, 서버에게 리소스를 요청하기 위해 사용
    - **_데이터를 가져올 때만 사용해야함_**
    - **_데이터를 서버로 전송할 때 Query String Parameters를 통해 전송_**
      - 데이터는 URL에 포함되어 서버로 보내짐

### Query String parameters

- 사용자가 입력 데이터를 전달하는 방법 중 하나
  - URL 주소에 데이터를 파라미터를 통해 넘기는 것
- 앰퍼샌드(`&`)로 연결된 `key=value` 쌍으로 구성되며, 기본 URL과 물음표(`?`)로 구분됨
  - 정해진 주소 이후에 물음표를 쓰는 것으로 Query String이 시작함을 알림
  - `=` 로 key와 value가 구분됨
  - 파라미터가 여러 개일 경우 `&` 를 붙여 여러 개의 파라미터를 넘길 수 있음

## Retrieving the data (Server)

- 데이터 가져오기
- 서버는 클라이언트로 받은 key-value 쌍의 목록과 같은 데이터를 받게됨
- 목록에 접근하는 방법은 사용하는 프레임워크에 따라 다름
- “모든 요청 데이터는 view 함수의 첫번째 인자 request에 들어있다”

<img width="1201" alt="dj_23" src="https://user-images.githubusercontent.com/86648892/188303763-3b08893a-bba8-4423-9926-86eeec9c4769.png">

<img width="1096" alt="dj_24" src="https://user-images.githubusercontent.com/86648892/188303764-44b69b3c-e71f-4a04-bfb6-7f9bde4d8993.png">

<img width="1115" alt="dj_25" src="https://user-images.githubusercontent.com/86648892/188303766-343865cf-56f6-4dea-8b3d-b1bd7a7d71ac.png">

<img width="1215" alt="dj_26" src="https://user-images.githubusercontent.com/86648892/188303769-7bab033d-ccc3-4b3a-8058-90655c952449.png">

### 요청과 응답 객체 흐름 정리

- 페이지가 요청되면 Django는 요청에 대한 메타데이터를 포함하는 HttpRequest object를 생성
  - 그리고 해당하는 적절한 view 함수를 로드하고 HttpRequest를 첫번째 인자로 전달
    - 마지막으로 view 함수는 HttpResponse object를 반환

---

# Variable Routing

- URL 주소를 변수로 사용하는 것을 의미
  - URL의 일부를 변수로 지정하여 view 함수의 인자로 넘길 수 있음
    - 즉, 변수 값에 따라 하나의 `path()` 에 여러 페이지를 연결시킬 수 있음
- Routing(라우팅)이란 어떤 네트워크 안에서 통신 데이터를 보낼 때 최적의 경로를 선택하는 과정을 뜻함
- `<type: name>`
  - 변수는 `<>` 에 정의하며 view 함수의 인자로 할당됨
  - type이 적혀있지 않다면 str이 기본값
    - str
    - int
    - slug
    - uuid
    - path

<img width="618" alt="dj_27" src="https://user-images.githubusercontent.com/86648892/188303770-8fac5cfd-208c-445f-ad4e-15dc713c4f22.png">

<img width="614" alt="dj_28" src="https://user-images.githubusercontent.com/86648892/188303771-dd92a0d1-2049-45e9-97af-b3d8998fab91.png">

<img width="498" alt="dj_29" src="https://user-images.githubusercontent.com/86648892/188303772-17be78b7-95df-4fd5-a4ba-9e12ebda86cc.png">

---

# App URL Mapping

- 앱이 많아졌을 때 `urls.py` 를 각 app에 매핑하는 방법
  - app의 view 함수가 많아지면서 사용하는 `path()` 가 많아지고, app 또한 더 많이 작성되기에 프로젝트의 `urls.py` 에서 모두 관리하는 것은 프로젝트 유지보수에 좋지 않음
- `python manage.py startapp pages`
  - pages 앱 생성
    - `settings.py` → `INSTALLED_APPS` 에 pages 추가
- `include()` 를 통해 분기 처리
  - `path('articles/', include('articles.urls'))`
    - `articles/` 로 끝나는 것을 보자마자 `include` 내에 있는 것으로 위임

<img width="1077" alt="dj_30" src="https://user-images.githubusercontent.com/86648892/188303773-67782775-c171-4dd4-867d-d8e9b41e586c.png">

<img width="1181" alt="dj_31" src="https://user-images.githubusercontent.com/86648892/188303774-4964b1bb-b41a-40c3-a3df-861afa81aa7b.png">

<img width="864" alt="dj_32" src="https://user-images.githubusercontent.com/86648892/188303775-20940db2-319d-4b7a-8647-a62a22ab5d7f.png">

---

# Naming URL patterns

- 분기된 url 주소를 모두 하나하나 주소를 바꿔줘야 하는가?
- 너무 번거롭다
- 각 url 주소에 이름을 붙여주자

## Naming URL patterns

- `path()` 함수의 `name` 인자 활용
  - 정의된 `name` 은 향후 `{% url ' ' %}` DTL 태그를 활용하여 접근 가능
    - 주어진 URL 패턴 이름 및 선택적 매개 변수와 일치하는 절대경로 주소를 반환
    - 템플릿에 URL을 하드코딩하지 않고도 DRY 원칙을 위반하지 않으면서 링크를 출력

<img width="1144" alt="dj_33" src="https://user-images.githubusercontent.com/86648892/188303776-1993e49d-fc2c-4f50-bfe0-f09fee1501d4.png">

<img width="1169" alt="dj_34" src="https://user-images.githubusercontent.com/86648892/188303778-9e0d4410-9028-4c04-84d1-2a94ce890dcf.png">

---

## Django의 설계 철학 (Templates System)

1. “표현과 로직(view)을 분리”
   - 템플릿 시스템은 표현을 제어하는 도구이자 표현에 관련된 로직일 뿐
     - 즉, 템플릿 시스템은 이러한 기본 목표를 넘어서는 기능을 지원하지 말아야함
2. “중복을 배제”
   - 대다수의 동적 웹사이트는 공통 header, footer, navbar 같은 사이트 공통 디자인 가짐
   - Django 템플릿 시스템은 이러한 요소를 한 곳에 저장하기 쉽게하여 중복코드를 없애야함
   - 템플릿 상속의 기초가 되는 철학

## Framework의 성격

- 독선적(Opinionated)
  - 독선적인 프레임워크들은 어떤 특정 작업을 다루는 ‘올바른 방법'에 대한 분명한 의견(규약)을 가지고 있음
  - 대체로 특정 문제 내에서 빠른 개발 방법을 제시
  - 어떤 작업에 대한 올바른 방법이란 보통 잘 알려져 있고 문서화가 잘 되어있기 때문
  - 하지만 주요 상황을 벗어난 문제에 대해서는 그리 유연하지 못한 해결책을 제시할 수 있음
- 관용적(Unopinionated)
  - 관용적인 프레임워크들은 구성 요소를 한데 붙여서 해결해야 한다거나 심지어 어떤 도구를 써야한다는 ‘올바른 방법'에 대한 제약이 거의 없음
  - 이는 개발자들이 특정 작업을 완수하는데 가장 적절한 도구들을 이용할 수 있는 자유도가 높음
  - 하지만 개발자 스스로 그 도구들을 찾아야한다는 수고가 필요

## Django Framwork의 성격

- ‘다소 독선적’
  - 양쪽 모두에게 최선의 결과를 준다고 강조
- 결국 하고자 하는 말은 현대 개발에 있어서 가장 중요한 것들 중 하나는 **_‘생산성’_**
- 프레임워크는 우리가 하는 개발을 방해하기위해 규칙, 제약을 만들어놓은 것이 아님
- 우리가 온전히 만들고자하는 것에만 집중할 수 있게 도와주는 것
- “수레바퀴를 다시 만들지말라”

---

# Namespace

- 이름 중복을 쉽게 구분 및 접근하기 위한 구조 설계
- URL Namespace
  - `articles` 앱과 `pages` 앱에 동일하게 path(`index/` )라는 url이 있다면?
    - `app_name` 및 `path()` 의 `name` 속성으로 해결
- Template Namespace
  - `articles` 앱과 `pages` 앱에 동일하게 `index.html` 이 있다면?
    - 샌드위치 구조로 해결

## URL namespace

- URL namespace를 사용하면 서로 다른 앱에서 동일한 URL 이름을 사용하는 경우에도 이름이 지정된 URL을 고유하게 사용할 수 있음
- `app_name` attribute을 작성해 URL namespace를 설정

<img width="867" alt="dj_35" src="https://user-images.githubusercontent.com/86648892/188497998-0edf4015-89aa-4e73-a3a7-cffcde25faab.png">

- `{% url 'app_name: url_name' %}`
  - app name을url 태그도 바뀌어야 함
    - url 참조는 `:` 연산자를 통해 지정
  - app name을 정의한 순간 url name에 app name을 빼고 호출하면 NoReverseMatch 발생
    - NoReverseMatch 발생하면 url 태그만 찾아보면 된다

<img width="1209" alt="dj_36" src="https://user-images.githubusercontent.com/86648892/188498007-82fbf91f-feb9-40c3-828e-61250b6a18e7.png">

## Template namespace

- Django는 기본적으로 `app_name/templates/` 경로에 있는 templates 파일들만 찾을 수 있으며, `settings.py` 의 INSTALLED_APPS에 작성한 app 순서로 template을 검색 후 렌더링함
  - `settings.py` 의 TEMPLATES 내부 `APP_DIRS: True` 가 해당 경로를 활성화하고 있음
  - 쉽게 말해 등록된 앱들 중 같은 이름의 템플릿이 있을 경우 앱 순서에 따라 먼저 등록된 것을 렌더링
- Django templates의 기본 경로 자체를 변경할 수는 없기에 물리적으로 이름 공간을 만든다
- 하위 디렉토리 경로를 하나 더 줘서 샌드위치 구조로 templates 경로를 재설정
  - `app_name/templates/app_name`

<img width="1151" alt="dj_37" src="https://user-images.githubusercontent.com/86648892/188498013-b999a577-cc83-4e34-a4ba-a6b3e7b96962.png">

---

# Database

- 데이터베이스란 무엇인가?
  - 체계화된 데이터의 모임
  - 검색 및 구조화같은 작업을 보다 쉽게하기 위해 조직화된 데이터를 수집하는 저장 시스템

## Database의 구조

1. **_스키마 (Schema)_**

   - 뼈대
   - 데이터베이스에서 자료의 구조, 표현 방법, 관계 등을 정의한 구조

   <img width="404" alt="dj_38" src="https://user-images.githubusercontent.com/86648892/188498017-d0daf2cb-5752-425b-ac49-88c12eefc995.png">

2. **_테이블 (Table)_**

   - 필드(field)와 레코드(record)를 사용해 조직된 데이터 요소들의 집합
     - 필드(field)
       - 속성, 컬럼(Column)
       - 각 필드에는 고유한 데이터 타입이 지정됨
         - INT, TEXT 등
     - 레코드(record)
       - 튜플, 행(Row)
       - 테이블의 데이터는 레코드에 저장됨
         - ex) 4명의 고객정보가 있을 시 레코드는 4개가 존재
   - 관계(Relation)라고도 부름

   <img width="780" alt="dj_39" src="https://user-images.githubusercontent.com/86648892/188498020-0db68358-fd0a-49d3-970a-3b65a7712dfe.png">

- 데이터베이스는 결국 수많은 테이블들의 모음
  - 사용자들의 회원정보, 게시글 등등의 여러 테이블 모음

## Primary Key (PK)

- 기본 키
- 각 레코드의 고유한 값
- 기술적으로 다른 항목과 절대로 중복되어 나타날 수 없는 단일값(unique)을 가짐
- 데이터베이스 관리 및 테이블 간 관계 설정 시 주요하게 활용됨

## Query

- 데이터를 조회하기 위한 명령어
  - 데이터 처리를 “문의”
- 조건에 맞는 데이터를 추출하거나 조작하는 명령어 (주로 테이블형 자료구조에서)
- 쿼리를 날린다는 곧 데이터베이스를 조작한다는 것

---

# Model

- Django는 웹 어플리케이션의 데이터를 구조화하고 조작하기 위한 모델을 제공함
  - Model을 사용하지 않고는 데이터를 저장할 수 없음
    - Model을 통해 데이터에 접속하고 관리
- 단일한 데이터에 대한 정보를 가짐
- 사용자가 저장하는 데이터들의 필수적인 필드들과 동작들을 포함
- 저장된 데이터베이스의 구조(layout)
- **일반적으로 각각의 모델은 하나의 데이터베이스 테이블에 매핑(mapping)**
  - **모델 클래스 1개 == 데이터베이스 테이블 1개**

<img width="1046" alt="dj_40" src="https://user-images.githubusercontent.com/86648892/188498024-f64a025e-c1a1-43a8-8c29-058eb07120c4.png">

## `models.py`

- 모델 클래스를 작성하는 것은 **_데이터베이스 테이블의 스키마를 정의_**하는 것
  - 모델 클래스 == 테이블 스키마
- 장고의 모델과 데이터베이스가 같은 것은 아니다
  - 장고에서 제공하는 모델을 통해 데이터베이스에 간접적으로 소통
  - View에서 1번 데이터 줘 → Model에서 Database한테 1번 데이터 내놔 → 받고 → View로 돌려줌

```python
from django.db import models

# Create your models here.
# 내가 원하는 데이터베이스의 스키마 구조를 정의한 것
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 객체 출력용 메서드
    def __str__(self):
        return self.title
```

- `id` 컬럼은 테이블 생성 시 Django가 자동으로 생성
- 각 모델은 `django.models.Model` 클래스의 서브클래스로 표현됨
  - 즉, 각 모델은 `django.models.Model` 클래스를 상속받음
    - 클래스 상속 기반 형태의 Django 프레임워크 개발
- 클래스 변수명
  - `title`, `content`
    - DB 필드를 나타냄
- 클래스 변수값
  - `models.CharField()` , `models.TextField()`
    - DB 필드의 데이터 타입을 나타냄

## Django Model Field

- Django는 모델 필드를 통해 테이블의 필드(컬럼)에 저장할 데이터 유형을 정의
  - [Django Model Fields](https://docs.djangoproject.com/en/4.1/ref/models/fields/)
- 데이터 유형에 따라 다양한 모델 필드를 제공

### `CharField(max_length=None, **options)`

- 길이의 제한이 있는 문자열을 넣을 때 사용
- `max_length`
  - 필드의 최대 길이(문자)
  - CharField의 필수 인자
  - 데이터베이스와 Django의 유효성 검사에서 활용됨
    - 사용자는 말을 듣지 않는다
      - 유효성 검사가 필요

### `TextField(**options)`

- 글자의 수가 많을 때 사용
- `max_length` 옵션 작성 시 입력 단계에서는 반영되지만, 모델과 데이터베이스 단계에서는 적용되지 않음
  - 실제로 저장될 때 길이에 대한 유효성을 검증하지 않음
  - 쉽게 말해, 의미가 없다

### `DateTimeField()`

- Python의 datetime.datetime 인스턴스로 표시되는 날짜 및 시간을 값으로 사용하는 필드
- `DateField()` 를 상속받는 클래스
- 선택 인자
  - `auto_now_add`
    - 최초 생성 일자 (Useful for creation of timestamps)
    - Django ORM이 최초 insert(테이블에 데이터 입력)시에만 현재 날짜와 시간으로 갱신
      - 테이블에 어떤 값을 최초로 넣을 때
  - `auto_now`
    - 최종 수정 일자 (Useful for “last-modified” timestamps)
    - Django ORM이 save를 할 때마다 현재 날짜와 시간으로 갱신

---

# Migrations

- 작성한 모델의 클래스를 실제 데이터베이스에 반영하는 과정
- `models.py` 에서 작성한 것이 테이블의 스키마라고 할 때, DB에 직접 만들 테이블의 설계도가 migrations 파일들
  - `$ python manage.py makemigrations`
    - 실제로 DB에 옮길 설계도 생성
  - `$ python manage.py migrate`
    - 해당 설계도 파일을 바탕으로 DB에 동기화

## makemigrations

- `$ python manage.py makemigrations`
- 모델을 작성 혹은 변경한 것에 기반한 새로운 migration(설계도, 청사진, 혹은 마이그레이션)을 만들 때 사용
- “테이블을 만들기 위한 설계도를 생성하는 것”

<img width="918" alt="dj_41" src="https://user-images.githubusercontent.com/86648892/188498027-7bf335ed-b7c3-4284-8067-50fae4812ba6.png">

- `migrations/0001_initial.py` 모습
  - “파이썬으로 작성된 최종 설계도”
    - blueprint
    - 아직 DB에 테이블이 생긴 것은 아님

## migrate

- `$ python manage.py migrate`
- “모델과 DB의 동기화”
- makemigrations로 만든 설계도를 실제 `db.sqlite3` DB 파일에 반영하는 과정
  - `db.sqlite3` 라는 파일로서 데이터베이스가 존재
    - migrate되었을 때 여기가 채워짐
    - 확인하기 위해서는 SQLite 확장프로그램 설치

<img width="878" alt="dj_42" src="https://user-images.githubusercontent.com/86648892/188498030-8a64362d-3739-4da3-9492-b437d28b90f6.png">

<img width="680" alt="dj_43" src="https://user-images.githubusercontent.com/86648892/188498032-d887ccc3-e126-4282-945c-c987c8eb34a5.png">

- migration 파일들의 특징은 앞에 숫자 4개가 붙는다
- `0001_initial` 외에 나머지는 무엇인가?
  - settings의 INSTALLED APPS에는 우리가 등록한 앱 외에 기본 내장 앱들이 있다
    - 이 앱들에 대한 설계도도 같이 migrate된 것이다
    - Django를 구동하기 위한 기본 내장 앱에 대한 설계도가 내부적으로 존재함
    - 처음 migrate할 때는 이 설계도를 같이 migrate함

## 기타 명령어

### showmigrations

- `$ python manage.py showmigrations`
  - migrations 파일들이 migrate 됐는지 안됐는지 여부를 확인하는 용도
  - [x] 표시가 있으면 migrate가 완료되었음을 의미

### sqlmigrate

- `$ python manage.py sqlmigrate articles 0001`
  - 해당 migrations 파일이 SQL문으로 어떻게 해석될지 미리 확인할 수 있음
  - 앱 이름, 설계도 번호 입력
  - `0001_initial.py` 파일은 파이썬으로 작성되어있는 것으로 이것이 migrate된다는 것은 무엇인가에 의해 DB에 저장되기 위해 SQL문으로 바뀌었다는 것이고, 이를 미리 확인해보기 위함

<img width="839" alt="dj_44" src="https://user-images.githubusercontent.com/86648892/188498034-73ba9285-8cf1-4e30-b506-829bb9eb39f4.png">

---

## 추가 필드 정의 (추가 migrations)

- `models.py` 에 변경사항이 생긴다면
  - 추가 모델 필드 작성 후 다시 한번 migrations 진행
- 추가 필드를 작성한다는 것은 기존의 테이블에 새로운 컬럼을 추가하는 상황
  - 이미 존재하는 테이블에 새로운 컬럼이 추가되는 상황에는 컬럼들을 빈 값인 상태로 추가할 수 없음
  - 추가되는 칼럼에 대한 기본값을 설정해야함
- 데이터베이스 원칙 중 무결성의 원칙
  - 빈 값을 데이터베이스에 추가할 수 없다
    - 기본값이 NOT NULL

<img width="1084" alt="dj_45" src="https://user-images.githubusercontent.com/86648892/188498035-9165adde-f2ba-4b0d-a6c3-dc2f45caf40b.png">

- 1)은 현재 이 대화에서 입력하는 값을 넣겠다
- 2)는 대화에서 나가서 코드상 default값을 넣어서 다시 makemigrations
- 1이 enter로 해결할 수 있기에 더 편하다
- 0002 설계도 확인
  - `dependencies` 에 0001 initial 설계도가 있음
    - 2번 설계도는 의존성이 있기에 1번 설계도가 있어야 의미가 있는 설계도
    - 만약 `models.py` 에 새로운 class를 생성하고 3번 설계도를 만든다면 다른 테이블이기에 의존성이 없음
- 설계도를 쌓아나가는 이유?
  - 모델이 망가졌을 때 망한 설계도를 버리고 잘 돌아갔던 시점에서 다시 누적하기 위함
- migrate를 통해 다시 반영

---

## MIGRATIONS 정리

1. `models.py` 변경
   - 데이터를 **_구조화_**하고 **_조작_**하기 위한 도구
2. 설계도 생성 (makemigrations)
3. 설계도 DB 반영 (migrate)

---

# ORM

## 그런데 설계도는 어떻게, 누가 해석할까?

- Django(i speak python) —> DB(i speak SQL)
- 중간에 SQL 언어로 번역해주는 친구가 필요함

## ORM

- Object-Relational-Mapping
- Django Framework는 내장된 Django ORM이 있음
  - 한 마디로 SQL을 사용하지 않고 데이터베이스를 조작할 수 있게 만들어주는 매개체
- 객체지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에 데이터를 변환하는 프로그래밍 기술
  - 객체지향 프로그래밍에서 데이터베이스를 연동할 때, 데이터베이스와 객체지향 프로그래밍 언어 간의 호환되지 않는 데이터를 변환하는 프로그래밍 기법

<img width="1125" alt="dj_46" src="https://user-images.githubusercontent.com/86648892/188498037-a31c3dd8-7e77-4cdb-9514-0debe061338c.png">

## ORM 장단점

### 장점

- SQL을 잘 알지 못해도 객체지향 언어로 DB 조작이 가능
- 객체지향적 접근으로 인한 높은 생산성
  - “생산성”
    - 현시대 개발의 키워드

### 단점

- ORM만으로 완전한 서비스를 구현하기 어려운 경우가 있음

---

## [참고] Shell이란?

- 운영체제 상에서 다양한 기능과 서비스를 구현하는 인터페이스를 제공하는 프로그램
- 셸(껍데기)은 사용자와 운영체제 내부 사이의 인터페이스를 감싸는 층이기 때문에 그러한 이름이 붙음
- “사용자" ↔ 셸 ↔ ”운영체제”
- 코드 테스트할 때 유용
- python shell 실행 명령어
  - git bash (windows)
    - `$ python -i`
  - zsh (macOS)
    - `$ python`
- django shell
  - `$ pip install django-extensions`
  - `$ python manage.py shell_plus`
    - django-extension이 제공하는 shell_plus
    - 자주 사용하는 모듈을 자동으로 import해줌
    - 없다면 `$ python manage.py shell`
- shell 종료 시 `exit()`

<img width="1005" alt="dj_47" src="https://user-images.githubusercontent.com/86648892/188498039-8d7305fb-bd82-4429-9ba9-992c4a42d811.png">

---

# QUERYSET API

- ORM이 사용하는 라이브러리 이름
- Django가 기본적으로 ORM을 제공함에 따라 DB를 편하게 조작할 수 있도록 도움
- Model을 만들면 Django는 객체들을 만들고, 읽고, 수정하고, 지울 수 있는 (CRUD) DB API를 자동으로 만듬

<img width="905" alt="dj_48" src="https://user-images.githubusercontent.com/86648892/188498044-f5c93166-6381-4f9d-819b-411813e21a8e.png">

- `Article.objects.all()`
  - 전체 데이터를 조회하는 ORM 코드
    - DB에게 전체 데이터 다 내놓으라고 하는 것
    - 결과가 QuerySet이라는 객체로 나옴
- Queryset API 부분에서 CRUD

## objects manager

- 다양한 Queryset API를 제공해주는 친구
  - “DB를 Python class로 조작할 수 있도록 여러 메서드를 제공하는 manager”
- Django 모델이 데이터베이스 쿼리 작업을 가능하게 하는 인터페이스
- Django는 기본적으로 모든 Django 모델 클래스에 대해 objects라는 Manager 객체를 자동으로 추가함
- 이 Manager(objects)를 통해 특정 데이터를 조작(메서드)할 수 있음

## Query

- 데이터베이스에 날리는 요청
  - “쿼리문을 작성한다”
    - 원하는 데이터를 얻기 위해 데이터베이스에 요청을 보낼 코드를 작성한다
- 이에 대한 응답으로 QuerySet이라는 자료형이 돌아옴
- Client → python(query) → ORM → SQL → Database → SQL → ORM → python(QuerySet)

## QuerySet

- 데이터베이스에게서 전달받은 객체 목록 (데이터 모음)
  - 리스트는 아니지만 리스트와 같은 특성을 가짐
    - iterable함
    - index로 접근 가능
- Django ORM을 통해 만들어진 자료형이며, 필터를 걸거나 정렬 등을 수행할 수 있음
- “objects” manager를 사용하여 **_복수의 데이터_**를 가져오는 queryset method를 사용할 때 반환되는 객체
  - **_단일한 객체 반환 시에는 모델의 인스턴스를 반환_**

<img width="1169" alt="dj_49" src="https://user-images.githubusercontent.com/86648892/188498047-fe72b8ae-57af-44e7-b7a4-5ffb2bb8276d.png">

---

# QuerySet API METHODS (CRUD)

## CRUD

- Create, Read, Update, Delete
  - 생성, 조회, 수정, 삭제
- 대부분의 컴퓨터 소프트웨어가 가지는 기본적인 데이터 처리 기능 4가지를 지칭

---

## READ

- 데이터 조회
  - QuerySet API methods that “return new querysets”
  - QuerySet API methods that “do not return querysets”

### `all()`

- QuerySet return
- 전체 데이터 조회

<img width="1096" alt="dj_50" src="https://user-images.githubusercontent.com/86648892/188498051-1b43737c-5ae7-4a91-9254-0d8d431ebe51.png">

### `get()`

- 유니크한 데이터, 고유성(uniqueness)을 보장하는 조회에서 사용해야함
  - 대표적으로 primary key
- 단일 데이터 조회
- 객체를 찾을 수 없으면 DoesNotExist 예외를 발생시키고, 둘 이상의 객체를 찾으면 MultipleObjectsReturned 예외를 발생시킴

<img width="970" alt="dj_51" src="https://user-images.githubusercontent.com/86648892/188498055-4cc49318-6668-4901-908a-22174b97a2a9.png">

### `filter()`

- QuerySet return
- 지정된 조회 매개 변수와 일치하는 객체를 포함하는 새 QuerySet을 반환
- 항상 QuerySet으로 반환함
  - 없으면 빈 QuerySet
  - 단일 객체도 QuerySet으로
- pk에는 부적합
  - QuerySet으로 주기에 한번 더 벗겨내야하는 불편함
  - 데이터를 조회했는데 없음에도 불구하고 빈 QuerySet을 반환해버림
    - 예외처리가 어려움

<img width="1099" alt="dj_52" src="https://user-images.githubusercontent.com/86648892/188498056-f5113ac0-6945-491b-a435-6d15582c3979.png">

## Field lookups

- 조건을 설정하여 조회하는 것
  - SQL WHERE 절의 상세한 조건을 지정하는 방법
- 특정 레코드에 대한 조건을 설정하는 방법
- QuerySet method `filter()`, `exclude()` 및 `get()` 에 대한 키워드 인자로 지정됨
- 문법 규칙
  - 필드명 뒤에 "double-underscore" 이후 작성함
  - `field__lookuptype=value`
- 참고 문서
  - [QuerySet API Reference](https://docs.djangoproject.com/en/4.1/ref/models/querysets/)
  - [QuerySet Field Lookups Reference](https://www.w3schools.com/django/django_ref_field_lookups.php)

<img width="646" alt="dj_53" src="https://user-images.githubusercontent.com/86648892/188498058-8983af76-f9ab-4a0c-96b1-7381fa010b66.png">

---

## CREATE

### 데이터 객체 생성 방법

1. `article = Article()`
   - 클래스를 통한 인스턴스 생성
     - `article.title = 'x'`
       - 클래스 변수명과 같은 이름의 인스턴스 변수를 생성 후 값 할당
         - `article.save()`
           - 인스턴스로 save 메서드 호출
             - `article.save()` 해야 DB에 등록됨
2. `article = Article(title = 'x')`
   - `article.save()`
3. `Article.objects.create(title = ‘x’)`
   - QuerySet API 중 `create()` 메서드 활용
     - `save()` 필요없음
       - save 이전에 유효성 검사를 하지 못하므로 좋은 것은 아니다

### `.save()`

- “Saving object”
- 객체를 데이터베이스에 저장함
- 데이터 생성 시 save를 호출하기 전에는 객체의 id값은 None
  - id 값은 Django가 아니라 데이터베이스에서 계산되기 때문
- 단순히 모델 클래스를 통해 인스턴스를 생성하는 것은 DB에 영향을 미치지 않기 때문에 반드시 save를 호출해야 테이블에 레코드가 생성됨

### 예시 코드

```html
{% extends 'base.html' %} {% block content %}
<h1>NEW</h1>
<form action="{% url 'articles:create' %}" method="GET">
  <label for="title">Title: </label>
  {% comment %} name은 url querystring에 들어갈 키 명칭 {% endcomment %}
  <input type="text" name="title" id="title" /><br />
  <label for="content">Content: </label>
  <input type="text" name="content" id="content" /><br />
  <input type="submit" />
</form>
<hr />
<a href="{% url 'articles:index' %}">Go Back to Index</a>
{% endblock content %}
```

```python
# new page의 input에서 쏴준 request 속에 데이터가 있다
# 요청에 대한 모든 데이터는 request에 있다
# input에 정의한 name이 key
def create(request):
    # 사용자의 데이터를 받아서 DB에 저장
    # 데이터 받기
    title = request.GET.get('title')
    content = request.GET.get('content')

    # DB에 저장
    #1
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    #2 (왼쪽이 DB의 필드, 오른쪽이 요청에서 받아온 변수)
    article = Article(title=title, content=content)
    article.save()

    # #3
    # Article.objects.create(title=title, content=content)

    return render(request, 'articles/create.html')
```

---

## UPDATE

- update 과정
  - 수정하고자 하는 인스턴스 객체를 조회 후 반환 값을 저장
    - 인스턴스 객체의 인스턴스 변수 값을 새로운 값으로 할당
      - `save()` 인스턴스 메서드 호출

<img width="613" alt="dj_54" src="https://user-images.githubusercontent.com/86648892/188498060-96aa0d6c-9d99-44ec-a405-cd02270908ed.png">

---

## DELETE

- 삭제하고자 하는 인스턴스 객체를 조회 후 반환 값을 저장
  - `delete()` 인스턴스 메서드 호출

<img width="622" alt="dj_55" src="https://user-images.githubusercontent.com/86648892/188498061-ccfe2eed-b555-413c-9c94-6672c600c4b9.png">

- 그렇다면 pk 1번이 삭제되고 새로 추가되는 항목은 pk 1번에 들어갈까? 끝 순서로 들어갈까?
  - 끝 순서로 들어간다
- 대부분의 데이터베이스는 삭제된 값을 재사용하지 않는다

## 출력 참고

<img width="614" alt="dj_56" src="https://user-images.githubusercontent.com/86648892/188498063-8fe75887-df99-4b42-92c8-5be7bec33a23.png">

<img width="1515" alt="dj_57" src="https://user-images.githubusercontent.com/86648892/188498065-4d337d1c-05ff-4e01-8715-e8496a0dd9aa.png">

- migrations?
  - DB에 영향을 끼치는 변경이 아니기에 새롭게 생성할 migrations가 없다!

---

# CRUD with view functions

### 고려사항

- `GET` method는 Read(조회)에만 사용
  - `GET` 은 Query String Parameter로 데이터를 보내기에 url을 통해 데이터를 보냄
    - ex) `/articles/create/?title=11&content=22`
- Create(생성), Update(수정), Delete(삭제)과 같이 데이터 조작하는 경우 `POST` method
- 페이지에서 입력을 받아 데이터를 생성한 경우(Create)
  - 생성되었다는 페이지를 따로 render하지 말고 목록 페이지로 redirect
- 개별 게시글 상세 페이지(detail page)의 경우 개별 게시글마다 뷰 함수와 템플릿 파일을 만들 수 없음
  - 글의 번호(pk)를 활용하여 하나의 뷰 함수와 템플릿 파일로 대응
    - Variable Routing 활용

### 요구사항

- 목록을 나타내는 페이지(`index.html`), 새로운 데이터 생성 입력 페이지(`new.html`), 상세정보 페이지(`detail.html`), 정보수정 페이지(`edit.html`)
- 기능 (`views.py`)
  - index 페이지 렌더링
  - new 페이지 렌더링
  - new 페이지에서 받은 데이터 create
    - 그리고 상세정보 페이지로 redirect
  - detail 페이지 렌더링
    - edit 페이지로 이동하는 버튼
    - delete 버튼
  - edit 페이지 렌더링
    - 데이터 update

### `redirect()`

- `from django.shortcuts import redirect`
- 동작 원리 (하기 코드 참고)
  - 클라이언트가 create url로 요청을 보냄
    - create view 함수의 redirect 함수가 302 status code를 응답
      - 응답받은 브라우저는 redirect 인자에 담긴 주소(index)로 사용자를 이동시키기 위해 index url로 Django에 재요청
        - index page를 정상적으로 응답받음 (200 status code)

### HTTP response code

- 클라이언트에게 특정 **HTTP 요청이 성공적으로 완료되었는지 여부**를 알려줌

  - 5개의 응답 그룹

    1. Information responses (1xx)
    2. Successful responses (2xx)
    3. Redirection messages (3xx)
       - 302 Found
         - 해당 상태 코드를 응답받으면 브라우저는 사용자를 해당 URL의 페이지로 이동시킴
    4. Client error response (4xx)

       - 403 Forbidden
         - 서버에 요청이 전달되었지만, 권한때문에 거절되었다는 것을 의미
         - 서버에 요청은 도달했으나 서버가 접근을 거부할 때 반환됨
         - Django 입장에서 작성자가 누구인지 모르기에 함부로 작성할 수 없다는 의미
         - 모델(DB)을 조작하는 것은 단순 조회와 달리 최소한의 신원 확인이 필요
           - 즉, POST 요청을 할 때는 **_CSRF Token_**이 필요하다
             - **_CSRF_**
               - Cross-Site-Request-Forgery (사이트 간 요청 위조)
                 - 사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여 특정 웹페이지를 보안에 취약하게 하거나 수정, 삭제 등의 작업을 하게 만드는 공격 방법 (2008년 옥션 해킹 사건)
             - **_CSRF Token_**
               - Security Token 사용 방식
                 - 사용자의 데이터에 임의의 난수 값(token)을 부여해 매 요청마다 해당 난수 값을 포함시켜 전송시키도록 함
                 - 이후 서버에서 요청을 받을 때마다 전달된 token값이 유효한지 검증
                 - 일반적으로 데이터 변경이 가능한 `POST` , `PATCH` , `DELETE` Method 등에 적용
                 - Django는 DTL에서 csrf_token 템플릿 태그를 제공 - `{% csrf_token %}` - 템플릿에서 내부 URL로 향하는 `POST` form을 사용하는 경우에 사용 - 해당 태그가 없으면 Django 서버는 요청에 대해 403 forbidden으로 응답 - 외부 URL로 향하는 `POST` form에 대해서는 CSRF 토큰이 유출되어 취약성을 유발할 수 있기에 사용하지 않음 - input type이 hidden으로 작성되며 value는 Django에서 생성한 hash 값으로 설정
                   <img width="1216" alt="dj_58" src="https://user-images.githubusercontent.com/86648892/188498066-84442092-876e-4b23-a2af-3ae4af4bc352.png">

    5. Server error responses (5xx)

- [HTTP CAT](https://http.cat/)
- [HTTP Status Codes](https://developer.mozilla.org/ko/docs/Web/HTTP/Status)

### HTTP request method

- HTTP는 request method를 정의하여
  - 주어진 리소스에 대해 수행하길 원하는 행동을 나타냄
- `GET`
  - 특정 리소스를 가져오도록 요청할 때 사용
  - 반드시 데이터를 가져올 때만 사용
  - DB에 변화를 주지 않음
  - CRUD 중 R 역할을 담당
  - ex) 검색
    - 검색은 서버에 영향을 미치는 것이 아닌 특정 데이터를 조회만 하는 요청
- `POST`
  - 서버로 데이터를 전송할 때 사용
  - 서버에 변경사항을 만듬
  - 리소스를 생성, 변경하기 위해 데이터를 **_HTTP body_**에 담아 전송
    - 개발자도구 - NETWORK 탭 - Payload 탭의 Form-Data 확인
  - `GET` 의 Query String Parameter와 다르게 **_URL로 보내지지 않음_**
  - CRUD 중 C, U, D 역할을 담당
  - ex) 로그인

---

## Code Snippets

<img width="1573" alt="dj_59" src="https://user-images.githubusercontent.com/86648892/188498067-bcb242bb-0f9e-4b7d-bb81-11361579a7a5.png">

### `/templates/base.html`

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx"
      crossorigin="anonymous"
    />
    <title>Document</title>
  </head>
  <body>
    {% block content %} {% endblock content %}

    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa"
      crossorigin="anonymous"
    ></script>
  </body>
</html>
```

### `/pjt02/urls.py`

```python
"""pjt02 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
]
```

### `/articles/models.py`

```python
from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 객체 출력용 메서드
    def __str__(self):
        return self.title
```

### `/articles/urls.py`

```python
from django.urls import path
from . import views

app_name = "articles"
urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
    path('<int:pk>/', views.detail, name="detail"),
    path('<int:pk>/delete/', views.delete, name="delete"),
    path('<int:pk>/edit/', views.edit, name="edit"),
    path('<int:pk>/update/', views.update, name="update"),
]
```

### `/articles/views.py`

```python
from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article(title=title, content=content)
    article.save()

    # detail url에 필요한 파라미터 pk를 같이 넘겨줌
    return redirect('articles:detail', article.pk)

# url로부터 pk를 잘라서 같이 보내줌
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }

    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()

    return redirect('articles:index')

# edit 템플릿을 보여주는 view
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/edit.html', context)

# 실제 데이터 수정
def update(request, pk):
    # 1. pk로 수정할 게시글을 가져온다
    article = Article.objects.get(pk=pk)
    # 2. request에서 사용자가 입력한 title과 content를 가져온다
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    # 3. DB에서 수정할 데이터로 조작한다
    article.save()
    # 4. 모든 조작이 끝나면 어디론가 보낸다
    return redirect('articles:detail', article.pk)
```

### `/articles/templates/articles/index.html`

```html
{% extends 'base.html' %} {% block content %}
<h1>Index 목록</h1>
<a href="{% url 'articles:new' %}">글 작성</a><br />
<hr />
{% for article in articles %}
<p>번호: {{ article.pk }}</p>
{% comment %} 위에 for문으로 들어온 article의 pk값을 적용한 detail이라는 이름의
url로 이동 {% endcomment %}
<a href="{% url 'articles:detail' article.pk %}">제목: {{ article.title }}</a>
<hr />
<br />
{% endfor %} {% endblock content %}
```

### `/articles/templates/articles/new.html`

```html
{% extends 'base.html' %} {% block content %}
<h1>글작성</h1>
<form action="{% url 'articles:create' %}" method="POST">
  {% csrf_token %}
  <label for="title">제목</label>
  <input type="text" name="title" id="title" /><br />

  <label for="content">내용</label>
  <textarea type="text" name="content" id="content"></textarea><br />

  <input type="submit" value="작성" /><br />

  <a href="{% url 'articles:index' %}">글 목록 보기</a>
</form>
{% endblock content %}
```

### `/articles/templates/articles/detail.html`

```html
{% extends 'base.html' %} {% block content %}
<h1>글 상세</h1>
<h3>{{ article.pk }}번째 글</h3>
<hr />
<p>제목: {{ article.title }}</p>
<p>내용: {{ article.content }}</p>
<p>생성시간: {{ article.created_at }}</p>
<p>수정시간: {{ article.updated_at }}</p>
<hr />

{% comment %} 단순히 수정 페이지로 이동하는 것이므로 a태그 사용 {% endcomment %}
<a href="{% url 'articles:edit' article.pk %}">수정</a>
{% comment %} delete url로 이동하면 -> views의 delete 호출 -> delete 함수가
index 페이지로 redirect {% endcomment %}
<form action="{% url 'articles:delete' article.pk %}" method="POST">
  {% csrf_token %}
  <input type="submit" value="삭제" />
</form>
<a href="{% url 'articles:index' %}">글 목록 보기</a>
{% endblock content %}
```

### `/articles/templates/articles/edit.html`

```html
{% extends 'base.html' %} {% block content %}
<h1>글 수정</h1>
<form action="{% url 'articles:update' article.pk %}" method="POST">
  {% csrf_token %}
  <label for="title">제목</label>
  {% comment %} value를 통해 넘겨받은 article의 title 채우기 {% endcomment %}
  <input type="text" name="title" id="title" value="{{article.title}}" /><br />

  <label for="content">내용</label>
  {% comment %} 넘겨받은 article의 content 채우기 {% endcomment %}
  <textarea type="text" name="content" id="content">
{{article.content}}</textarea
  ><br />

  <input type="submit" value="수정" /><br />
</form>
<a href="{% url 'articles:index' %}">글 목록 보기</a>
{% endblock content %}
```

---

# Admin Site

- **_Django의 가장 강력한 기능 중 하나인 automatic admin interface_**
- “관리자 페이지”
  - 사용자가 아닌 서버의 관리자가 활용하기 위한 페이지
  - 모델 class를 `admin.py` 에 등록하고 관리
  - 레코드 생성 여부 확인에 매우 유용하며 직접 레코드를 삽입할 수도 있음

### admin 계정 생성

- `$ python manage.py createsuperuser`
  - username과 password를 입력해 관리자 계정 생성
    - email은 선택사항이기에 입력하지 않고 enter를 입력하는 것이 가능
    - 비밀번호 생성 시 보안상 터미널에 입력되지 않으니 무시하고 입력을 이어가도록 함

### admin site 로그인

- `/admin/` 을 붙인 url로 접속 후 로그인

### admin에 모델 클래스 등록

- 모델의 record를 보기 위해서는 `admin.py`에 관리하고자 하는 모델 등록 필요

<img width="613" alt="dj_60" src="https://user-images.githubusercontent.com/86648892/188498087-00c8718b-fa96-44d5-8190-5ea3632ebd6b.png">

### 데이터 CRUD in admin

- admin 사이트에서 직접 CRUD 가능

---

## 정리

- Model
  - Django는 Model을 통해 데이터에 접속하고 관리
- ORM
  - 객체지향 프로그래밍을 이용한 DB 조작
- Migrations
  - 모델에 생긴 변화(필드 추가, 모델 삭제 등)를 DB에 반영하는 방법(과정)
- HTTP request & response
  - 요청의 행동을 표현하는 HTTP request method
  - 요청에 대한 성공 여부 응답을 숫자로 표현하는 HTTP response status codes

---

# Django Form

### 참고 링크

- [Django Github - Forms](https://github.com/django/django/blob/main/django/forms/models.py)
- [Django Docs - The Forms API](https://docs.djangoproject.com/en/4.1/ref/forms/api/#django.forms.Form.errors)
- [Django Docs - Form fields (linked to ChoiceField)](https://docs.djangoproject.com/en/4.1/ref/forms/fields/#)
- [Django Docs - Widgets (linked to Selector and checkbox widgets)](https://docs.djangoproject.com/en/4.1/ref/forms/widgets/#selector-and-checkbox-widgets)
- [Django Docs - Coding Style](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/)
- [Django Docs - Working with forms (linked to Rendering fields manually](https://docs.djangoproject.com/en/4.1/topics/forms/#rendering-fields-manually)
- [django-bootstrap-v5 Docs](https://django-bootstrap-v5.readthedocs.io/en/latest/)

## Django Form

- HTML `<input>` 태그를 직접 사용하지 않고 **_Django Form_**이라는 프레임워크를 통해 사용자로부터 데이터를 받자
- WHY?
  - **_유효성 검증_**
    - 사용자의 요청 중에는 비정상적인 혹은 악의적인 요청이 있음
    - 사용자가 입력한 데이터가 우리가 원하는 데이터 형식에 맞는지 유효성 검증이 필요
      - 이러한 유효성 검증은 많은 부가적인 것들을 고려해서 구현해야 하는데, 이는 개발 생산성을 늦추고, 쉽지도 않음
        - Django Form은 이 과정에서 과중한 작업과 반복적 코드를 줄여줌으로써 훨씬 쉽게 유효성 검증을 진행할 수 있도록 만듬
  - 유효성 검증 외에도 빠르게 form 작업을 수행할 수 있음

### Form에 대한 Django의 역할

- Form은 Django의 **_유효성 검사 도구 중 하나로 외부의 악의적 공격 및 데이터 손상에 대한 중요한 방어 수단_**
- Django는 Form과 관련한 유효성 검사를 **_단순화하고 자동화_**할 수 있는 기능을 제공하여, 개발자가 직접 작성하는 코드보다 더 안전하고 빠르게 수행하는 코드를 작성할 수 있음
  - **_개발자가 필요한 핵심 부분만 집중_**할 수 있도록 돕는 프레임워크의 특성
- Django는 Form과 관련한 작업의 3가지 부분을 처리해줌
  1. 렌더링을 위한 데이터 준비 및 재구성
  2. 데이터에 대한 HTML forms 생성
  3. 클라이언트로부터 받은 데이터 수신 및 처리

---

# Django Form Class

- Form Class
  - Django form 관리 시스템의 핵심

## Form Class 선언

- 상속을 통해 선언
  - forms 라이브러리의 Form 클래스를 상속받음
    - Model Class를 models 라이브러리의 Model 클래스를 상속받는 것과 유사
- `forms.py`

  - 앱 폴더에 생성 후 form class 선언
    <img width="616" alt="dj_61" src="https://user-images.githubusercontent.com/86648892/189478360-f3ae2e67-30be-4459-af7e-87f1b885b3de.png">

    - 모델에 관련없이
      - 사용자로부터 무엇을 받을 것인지, 어떤 타입으로 받을지 고려하여 작성
    - form에는 model field와 달리 TextField가 존재하지 않음
    - Form Class를 forms.py에 작성하는 것은 규약은 아니다
      - 파일 이름이 달라도 되고, models.py나 다른 어디에도 작성이 가능하지만 관행적으로 forms.py에 작성하는 것을 권장
    - form class에서 `Charfield()`의 `max_length`는 models와 다르게 필수 인자는 아님
      - 그냥 편리하게 길이 제한을 걸려고 쓰는 용도

## Form Rendering options

- html 파일에서 렌더링 시 views의 함수의 context에 담아 넘겨받은 form을
  - `{{ form.as_p }}` 와 같이 접근하여 사용
- `<label>` & `<input>` 쌍에 대한 3가지 출력 옵션
  1. `as_p()`
     - 각 필드가 단락(`<p>` 태그)으로 감싸져서 렌더링
  2. `as_ul()`
     - 각 필드가 목록 항목(`<li>` 태그)으로 감싸져서 렌더링
     - `<ul>` 태그는 직접 작성해야함
  3. `as_table()`
     - 각 필드가 테이블(`<tr>` 태그) 행으로 감싸져서 렌더링
- 주로 `as_p()` 를 많이 사용함

## Form fields & Widgets

- 그런데 `{{ form }}` 과 같이 한 덩어리로 묶어서 렌더링하면 안에 세부적인 처리를 어떻게 할 것인가에 대한 의문이 생김
- Django의 2가지 HTML input 요소 표현
  1. **_Form fields_**
     - ex) `forms.CharField()`
     - **_입력에 대한 유효성 검사 로직을 처리_**
     - 템플릿에서 직접 사용됨
  2. **_Widgets_**
     - ex) `forms.CharField(widget=forms.Textarea)`
     - 웹 페이지의 **_HTML input 요소 렌더링을 담당_**
       - 단순히 HTML 렌더링, 출력을 처리하는 것이며 유효성 검증과 아무런 관계가 없음
         - “웹 페이지에서 input element의 단순 raw한 렌더링만을 처리하는 것일 뿐”
     - Widgets은 반드시 form fields에 할당됨
       - form fields의 core field arguments 확인
  - 쉽게 말해 Form fields는 사용자의 입력이 어떠한 입력값이어야하는지 정의하고, 유효한 입력값인지 판단하기 위함이며, Widgets는 input값의 출력을 어떻게 해줄지 세부적으로 조정하기 위함

### 드랍다운을 만들어보자

```python
# articles/forms.py

from django import forms

class ArticleForm(forms.Form):
    NATION_A = 'kr'
    NATION_B = 'ch'
    NATION_C = 'jp'
    NATION_CHOICES = [
        (NATION_A, '한국'),
        (NATION_B, '중국'),
        (NATION_C, '일본'),
    ]
    title = forms.CharField(max_length=10)
    content = forms.CharField(widget=forms.Textarea)
    nation = forms.ChoiceField(choices=NATION_CHOICES)

# NATION_CHOICES = [ ('kr', '한국'), ('ch', '중국'), ('jp', '일본'), ]
# 이렇게 선언하는 것은 동작은 같지만
# Django Style Guide에 어긋난다
# ChoiceField는 <select> 태그, choices의 인자들은 <select> 태그 안의 <option>들로 들어간다
```

- [Django Docs - Widgets (linked to Selector and checkbox widgets)](https://docs.djangoproject.com/en/4.1/ref/forms/widgets/#selector-and-checkbox-widgets)
- [Django Docs - Coding Style](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/)

---

# Django ModelForm

## ModelForm Class

- Model을 기반으로 한 Form Class
- Model을 통해 Form Class를 만들 수 있는 helper class
  - 기반으로 하는 모델의 필드를 따로 재정의하지 않아도 됨
- ModelForm은 Form과 똑같은 방식으로 view 함수에서 사용

## ModelForm 선언

- 상속을 통해 선언
  - forms 라이브러리에서 파생된 ModelForm 클래스 상속
  - 정의한 ModelForm 클래스 안에 inner class인 Meta 클래스 선언
    - 어떤 모델을 기반으로 form을 작성할 것인지에 대한 정보를 Meta 클래스에 지정
      <img width="527" alt="dj_62" src="https://user-images.githubusercontent.com/86648892/189478363-35f7863f-a5f7-405b-b9ce-e233243ad3ab.png">

### Meta Class

- ModelForm의 정보를 작성하는 곳
  - model, fields라는 변수명은 정해져 있음
- `model = Article`
  - 참조할 모델
    - 인스턴스가 아닌 참조값
  - 참조하는 모델에 정의된 field 정보를 Form에 적용함
    - input값을 받는 field들
- 어떤 모델을 기반으로 form을 작성할 것인지에 대해 inner class인 Meta 클래스에 지정

  - `model = Article`
    - 참조값을 줌 (인스턴스가 아님)
    - 참조값과 반환값
  - `fields = '__all__'`

    - 모델의 **_입력받아야 할_** 모든 필드를 포함
    - 필드 중 사용자가 입력하지 않는 필드는 포함하지 않음

      - ex) `auto_now_add = True` 인 `created_at` 이나 `auto_add = True` 인 `updated_at` 등
        <img width="1086" alt="dj_63" src="https://user-images.githubusercontent.com/86648892/189478364-db5106b4-8175-44b9-a04a-bae25345d820.png">

    - `exclude` 속성을 사용하여 모델에서 포함하지 않을 필드를 지정할 수 있음
      - fields와 exclude를 함께 작성해도 되나 권장하지 않음

### [참고] Meta Data?

- 데이터를 표현하기 위한 데이터

### [참고] 참조값과 반환값

- 언제 참조값을 사용할까?

  - 함수를 호출하지 않고 함수 자체를 그대로 전달하여, 다른 함수에서 “필요한 시점"에 호출하는 경우

    - view 함수의 참조값을 그대로 넘김으로써, path 함수가 내부적으로 해당 view 함수를 “필요한 시점"에 사용하기 위해서
      <img width="756" alt="dj_64" src="https://user-images.githubusercontent.com/86648892/189478365-9bee80ec-525a-4a6e-b7f1-7b5c870ec329.png">

  - 클래스도 마찬가지
    - Article이라는 클래스를 “호출하지 않고(==model을 인스턴스로 만들지 않고)” 작성하는 이유는 ArticleForm이 해당 클래스를 필요한 시점에 사용하기 위함
    - 더불어 이 경우에는 인스턴스가 필요한 것이 아닌, 실제 Article 모델의 참조값을 통해 해당 클래스의 필드나 속성 등을 내부적으로 참조하기 위한 이유도 있음

---

# ModelForm with view functions (CRUD)

## CREATE

<img width="679" alt="dj_65" src="https://user-images.githubusercontent.com/86648892/189478366-3205d78b-db05-486e-890d-40fbf7447101.png">

- `data=request.POST`
  - `BaseModelForm()`의 첫번째 인자는 data임
  - request에 담긴 데이터를 바탕으로 ArticleForm 인스턴스 생성
- 유효성 검사를 통과하면
  - `article = form.save()`
    - ModelForm의 `save()` 는 input 값들을 채운 해당 모델 instance를 반환
    - 상세화면 페이지로 넘어갈 때 해당 모델 인스턴스를 넘겨줘야하므로 article에 할당
  - 이후 상세화면으로 리다이렉트
- 통과하지 못하면
  - 작성 페이지로 리다이렉트

### `is_valid()`

- 유효성 검사를 실행하고, 데이터가 유효한지 여부를 boolean으로 반환
  - `max_length` 등과 같이 모델에 설정해둔 유효성 기준에 따라 판단
    - CharField()에 숫자를 넣으면 안되는것과 같은 기본적인 내장 유효성 검사 외에 추가적으로 유효성 검사 기준 인자를 잘 설계하는 것이 중요
- 데이터 유효성 검사를 보장하기 위한 많은 테스트에 대해 Django는 `is_valid()` 를 제공하여 개발자의 편의를 도움
- `BaseForm()` 에 정의되어 있음

### is_valid()의 결과가 False라면?

- `is_valid()` 의 반환 값이 False인 경우 form 인스턴스의 errors 속성에 값이 저장됨
  - 기본적으로는 빈 값
    - 유효성 검증 실패 시 실패한 원인이 딕셔너리 형태로 저장됨
      - `forms.py`에서 정의한 `error_messages` 나 기본적으로 정의된 에러 메세지를 포함한 페이지를 렌더링해줌
  - [참고] 공백과 빈 값은 다르다
    - 빈 값
      - “이 입력란을 작성하세요”
        - Django와 관련없음
          - HTML과 관련있음
            - input 태그의 required라는 속성에 의해 Django에 요청이 가기 전에 이미 막힘
              - 개발자 도구를 통해 required를 지우고 보내면 Django에서 유효성 검사 진행 가능
    - 공백
      - Django에서 에러를 주는 경우

<img width="872" alt="dj_66" src="https://user-images.githubusercontent.com/86648892/189478368-ebc39828-b613-40ad-872c-a8fbd5a9562c.png">

### `form.save()`

- `return self.instance`
- form 인스턴스에 바인딩된 데이터를 통해 데이터베이스 객체를 만들고 저장
- ModelForm의 하위 클래스는 키워드 인자 `instance` 여부를 통해 CREATE, UPDATE 여부를 결정
  - 제공되지 않는 경우 `save()` 는 지정된 모델의 새 인스턴스를 만듬 (CREATE)
  - 제공된 경우 `save()` 는 해당 인스턴스를 수정 (UPDATE)

<img width="478" alt="dj_67" src="https://user-images.githubusercontent.com/86648892/189478369-2bdd9a37-01ab-43fe-9994-a699bb99a01f.png">

---

## UPDATE

- ModelForm의 인자 instance는 수정 대상이 되는 객체(기존 객체)를 지정
  1. `request.POST`
     - 사용자가 form을 통해 전송한 데이터 (새로운 데이터)
  2. `instance`
     - 수정이 되는 대상
- CREATE에서는
  - `form = ArticleForm(request.POST)`
    - Create 버튼을 통해 들어온 POST 요청에 들어있는 입력 데이터들을 바탕으로 ArticleForm의 모델인 Article의 인스턴스를 반환해 form에 할당
- UPDATE에서는
  - `article = Article.objects.get(pk=pk)`
    - 일단 수정할 인스턴스를 들고온 뒤
  - `form = ArticleForm(request.POST, instance=article)`
    - Update 버튼을 통해 들어온 POST 요청에 들어있는 입력 데이터들을 바탕으로, 위에 할당한 article이라는 인스턴스를 수정한 결과를 form에 할당

<img width="802" alt="dj_68" src="https://user-images.githubusercontent.com/86648892/189478370-050edb5b-0b0a-43a2-8429-11b7e24494c2.png">

<img width="827" alt="dj_69" src="https://user-images.githubusercontent.com/86648892/189478372-4e51086b-53c2-46c5-af64-a606d5be3476.png">

<img width="821" alt="dj_70" src="https://user-images.githubusercontent.com/86648892/189478374-ef4fe4fd-9010-448e-ae80-856289c419a4.png">

### [참고] ModelForm의 인자 구조

<img width="1113" alt="dj_71" src="https://user-images.githubusercontent.com/86648892/189478375-b9809196-81af-43da-a0d5-e99c0aacfedf.png">

---

## Form & ModelForm

- Form과 ModelForm은 모델을 기반으로 안하냐의 차이
- 누가 더 좋은 것이 아니라 역할이 다른 것
  - **_사용자로부터 받는 데이터가 DB에 영향을 미치는가 여부_**
    - **_로그인은 사용자의 데이터를 받아 인증 과정에서만 사용 후 별도로 DB에 저장하지 않으므로 Form_**
    - **_회원가입으로 유저 데이터를 추가하거나, 게시판 글 작성처럼 아티클 데이터를 추가하는 경우 ModelForm_**

### Form

- 사용자의 입력을 필요로 하며 직접 입력 데이터가 DB 저장에 사용되지 않거나 일부 데이터만 사용될 때
  - ex) 로그인
    - 사용자의 데이터를 받아 인증 과정에서만 사용 후 별도로 DB에 저장하지 않음

### ModelForm

- 사용자의 입력을 필요로 하며 입력 받은 것을 그대로 DB 필드에 맞춰 저장할 때
- 데이터의 유효성 검사가 끝나면 데이터를 각각 어떤 레코드에 매핑해야할지 이미 알고있기 때문에 곧바로 `save()` 호출이 가능

---

# Handling HTTP requests

- HTTP requests 처리에 따른 view 함수 구조 변화를 구현해보자
  - 하나의 view 함수에서 HTTP request method에 따라 로직이 분리되도록 변경
- new-create, edit-update의 view 함수 역할에는 공동의 목적과 차이점이 있음
  - 공통점
    - new-create는 “생성”
    - edit-update는 “수정”
  - 차이점
    - new, edit는 페이지 렌더링 (GET)
    - create, update는 DB 조작 (POST)

## CREATE

<img width="789" alt="dj_72" src="https://user-images.githubusercontent.com/86648892/189478376-5cd263c9-dc5e-47da-a179-3dcaf38b77f2.png">

- `views.py` 의 new 함수와 create 함수를 create 함수로 통합
  - 불필요해진 new 함수의 url path를 삭제
    - new.html의 이름을 create.html로 변경 후 url path를 변경된 이름으로 수정
      - index.html의 새 게시글 생성 페이지를 렌더링하는 버튼의 링크를 articles의 create url path로 변경
        - 기존 new 함수의 `return render(request, 'articles/new.html', context)` 를 `return render(request, 'articles/create.html', context)` 로 변경
- context의 들여쓰기 위치 주의
  - `if form.is_valid()` 가 False로 평가받았을 때 에러 정보가 담긴 form 인스턴스가 context로 넘어갈 수 있도록 설정
- 분기처리를 할 때 왜 POST를 if의 조건으로 쓸까?
  - DB 조작 관련 코드를 POST일때만 수행한다고 설정할 수 있음
  - if에 GET을 쓰고 else에서 DB 조작 코드를 쓴다면
    - POST외에 다른 request method에 대해서도 DB 조작이 가능한 상태가 되어버림

## UPDATE

- CREATE와 동일

<img width="747" alt="dj_73" src="https://user-images.githubusercontent.com/86648892/189478377-cf75d70b-25c8-4aeb-a2be-a9126248b080.png">

## DELETE

- POST 요청에 대해서만 삭제가 가능하도록 수정

<img width="849" alt="dj_74" src="https://user-images.githubusercontent.com/86648892/189478379-b35ac0fa-8d13-439b-a6fa-5f70ef8144e8.png">

---

# View Decorators

- View decorators를 활용하여 view 함수를 단단하게 만들어보자

## Decorator

- 기존에 작성된 함수에 기능을 추가하고싶을 때
  - 해당 함수를 수정하지 않고 기능을 추가해주는 함수
- ## 데코레이터 동작 예시
    <img width="901" alt="dj_75" src="https://user-images.githubusercontent.com/86648892/189478381-c459b80f-0b8e-41e9-8e8a-590283a86a15.png">

## Allowed HTTP methods

- Django는 다양한 HTTP 기능을 지원하기 위해 view 함수에 적용할 수 있는 데코레이터 제공
  - `from django.views.decorators.http`
    - `import require_http_methods`
      - `@require_http_methods` 시 직접 뒤에 붙인 HTTP request method일 때만 허용
        - ex) `@require_http_methods(['GET', 'POST'])`
    - `import require_safe`
      - `@require_safe` 시 GET 요청일 때만 허용
    - `import require_POST`
      - `@require_POST` 시 POST 요청일 때만 허용
- 일치하지 않는 메서드 요청이라면 **_405 Method Not Allowed_**를 반환
  - 405 Method Not Allowed
    - 요청 방법이 서버에게 전달되었으나 사용 불가능한 상태

## 적용

- index
  - 단순 전체 게시글 데이터 조회 (GET)
    - `@require_safe`
- create
  - 새 게시글 생성 페이지 렌더링 요청 (GET), 작성 후 새 게시글 생성 요청 (POST)
    - `@require_http_methods(['GET', 'POST'])`
- update
  - 게시글 수정 페이지 렌더링 요청 (GET), 작성 후 수정된 게시글 인스턴스 저장 요청 (POST)
    - `@require_http_methods(['GET', 'POST'])`
- delete

  - 게시글 DB에서 삭제 요청 (POST)

    - `@require_POST`

      - url로 delete를 시도하면 405 http status code 반환
        <img width="1013" alt="dj_76" src="https://user-images.githubusercontent.com/86648892/189478383-e4ab8b97-9751-4c7d-95a9-98e053d82c35.png">

    - `@require_POST` 작성했으므로 기존에 있던 `if request.method == 'POST':` 필요없음

---

# Custom Form Layout

### 참고 링크

- [Django Docs - Working with forms (linked to Rendering fields manually](https://docs.djangoproject.com/en/4.1/topics/forms/#rendering-fields-manually)
  - **subject는 컬럼의 이름**
- [django-bootstrap-v5 Docs](https://django-bootstrap-v5.readthedocs.io/en/latest/)

### 코드 예시 (create.html)

```html
{% extends 'base.html' %} {% load bootstrap5 %} {% block content %}
<h1>CREATE</h1>
<form action="{% url 'articles:create' %}" method="POST">
  {% csrf_token %} {{ form.as_p }}
  <input type="submit" />
</form>
<hr />
<a href="{% url 'articles:index' %}">뒤로가기</a>

<hr />

<h2>수동으로 Form 작성</h2>
<form action="#">
  <div>{{ form.title.errors }} {{ form.title.label_tag }} {{ form.title }}</div>
  <div>
    {{ form.content.errors }} {{ form.content.label_tag }} {{ form.content }}
  </div>
</form>

<hr />

<h2>Looping over the form’s fields</h2>
<form action="#">
  {% for field in form %} {{ field.errors }} {{ field.label_tag }} {{ field }}
  {% endfor %}
</form>

<hr />

<h2>bootstrap v5 라이브러리 사용하기</h2>
<form action="#">
  {% bootstrap_form form %} {% buttons %}
  <button type="submit" class="btn btn-primary">Submit</button>
  {% endbuttons %}
</form>
{% endblock content %}
```

<img width="1318" alt="dj_77" src="https://user-images.githubusercontent.com/86648892/189478385-284b3ec1-89b7-49de-8dbd-e9d5c3ccedf5.png">

<img width="1321" alt="dj_78" src="https://user-images.githubusercontent.com/86648892/189478387-b92345d6-80bb-4462-8095-39eee6e5325c.png">

<img width="1319" alt="dj_79" src="https://user-images.githubusercontent.com/86648892/189478388-6f300af7-185a-454a-96e0-5f6df1fcea36.png">

<img width="1325" alt="dj_80" src="https://user-images.githubusercontent.com/86648892/189478389-2e88b8bf-7d96-4ae6-a7ea-e4ab25cf83eb.png">

---

## 정리

- Django Form Class
  - Django 프로젝트의 주요 유효성 검사 도구
  - 공격 및 데이터 손상에 대한 중요한 방어 수단
  - 유효성 검사에 대해 개발자에게 강력한 편의를 제공
- View 함수 구조 변화
  - HTTP requests 처리에 따른 구조 변화

---

# The Django authentication system

### 참고 링크

- [Django Github - built-in auth models](https://github.com/django/django/blob/main/django/contrib/auth/models.py)
- [Django Github - builit-in auth forms](https://github.com/django/django/blob/main/django/contrib/auth/forms.py)
- [Django Docs - Built-in forms](https://docs.djangoproject.com/en/4.1/topics/auth/default/#module-django.contrib.auth.forms)
- [Django Github - global_settings.py](https://github.com/sebleier/django/blob/master/django/conf/global_settings.py)
- [Django Docs - Substituting a custom User model](https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#substituting-a-custom-user-model)
- [Python Docs - Abstract Base Classes](https://docs.python.org/3/library/abc.html)
- [Django Docs - How to use sessions](https://docs.djangoproject.com/en/4.1/topics/http/sessions/)
- [Django Docs - Built-in template context processors](https://docs.djangoproject.com/en/4.1/ref/templates/api/#built-in-template-context-processors)
- [Django Docs - User model Fields](https://docs.djangoproject.com/en/4.1/ref/contrib/auth/#fields)
- [Django Docs - Password management in Django](https://docs.djangoproject.com/en/3.2/topics/auth/passwords/)

## The Django authentication system

- Django authentication system(인증 시스템)은 인증(Authentication)과 권한(Authorization) 부여를 함께 제공(처리)하며, 이러한 기능을 일반적으로 인증 시스템이라함
- 필수 구성은 `settings.py` 에 이미 포함되어 있으며 INSTALLED_APPS에서 확인 가능
  - built-in app
    - `django.contrib.auth`
      - Django에서는 admin, staff, 일반 user가 있음
- Authentication(인증)
  - 신원 확인
  - 사용자가 자신이 누구인지 확인하는 것
- Authorization(권한)
  - 권한 부여
  - 인증된 사용자가 수행할 수 있는 작업을 결정

## 유저 관리용 accounts 앱 만들기

- 유저 인증과 관련된 앱
  - `$ python manage.py startapp accounts`
    - INSTALLED_APPS에 추가
    - **_auth와 관련한 경로나 키워드들은 Django 내부적으로 accounts라는 이름으로 사용하고 있기에 되도록 accounts로 지정하는 것을 권장_**
    - 다른 이름으로 설정해도 되지만 나중에 추가 설정을 해야할 일들이 생김
  - url 분리 및 매핑 실행

---

# Substituting a custom User model

- “Custom User Model”로 **_대체_**하기
- 기본 User Model을 Custom User Model로 대체할 것을 권장
  - Django에서는 기본적인 인증 시스템과 여러가지 필드가 포함된 User Model을 제공, 대부분의 개발 환경에서는 기본 User Model을 Custom User Model로 대체함
    - 개발자들이 작성하는 일부 프로젝트에서는 Django에서 제공하는 built-in User Model의 기본 인증 요구사항이 적절하지 않을 수 있음
      - ex) 내 서비스의 회원가입 시 username 대신 email을 식별 값으로 사용하는 것이 더 적합한 사이트인 경우, Django의 User Model은 기본적으로 username을 식별 값으로 사용하기 때문에 적합하지 않음
- Django는 현재 프로젝트에서 사용할 User Model을 결정하는 **AUTH_USER_MODEL** 설정 값으로 Default User Model을 재정의(override)할 수 있도록 함
- **_첫 migrations를 진행하기 전에 대체 작업을 진행해야함_**
  - migrations 과정에서 기본 user model도 포함되기 때문

## `AUTH_USER_MODEL`

- 프로젝트에서 User를 나타낼 때 사용하는 모델
  - auth 앱의 User 클래스라는 뜻
    - `django.contrib.auth`
      - Django의 contrib 모듈 안에 있는 auth
- 프로젝트가 진행되는동안 (모델을 만들고 마이그레이션한 후) 변경할 수 없음
  - 프로젝트 시작 시 설정하기 위한 것이며, 참조하는 모델은 첫번째 마이그레이션에서 사용할 수 있어야함
    - 즉, 첫번째 마이그레이션 이전에 확정지어야하는 값
- settings의 로드 구조
  - `settings.py` 에 기본값으로 `AUTH_USER_MODEL = 'auth.User'` 을 가지고 있음
    - AUTH_USER_MODEL은 `settings.py` 에 보이지 않는데 어디에 기본값이 작성되어 있는걸까?
      - 우리가 작성하는 `settings.py` 는 `global_settings.py` 를 상속받아 재정의하는 파일
        - [Django Github - global_settings.py](https://github.com/sebleier/django/blob/master/django/conf/global_settings.py)

## Custom User Model 대체 진행 방법

- 공식문서 참고
  - [Django Docs - Substituting a custom User model](https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#substituting-a-custom-user-model)

1. Custom User Model 작성

   - AbstractUser를 상속받는 커스텀 User 클래스 작성
     - 기존 User 클래스도 AbstractUser를 상속받기 때문에 커스텀 User 클래스도 완전히 같은 모습을 가지게 됨
       <img width="1110" alt="dj_81" src="https://user-images.githubusercontent.com/86648892/189502176-31307fca-dcfc-425c-9302-80eb5f310082.png">

2. Django 프로젝트에서 User를 나타내는데 사용하는 모델을 방금 생성한 커스텀 User 모델로 저장

<img width="616" alt="dj_82" src="https://user-images.githubusercontent.com/86648892/189502179-71ee98f1-23e4-4192-bb76-3d2be6c9e938.png">

3. `admin.py` 에 커스텀 User 모델을 등록

   - 기존 User 모델이 아니기 때문에 등록하지 않으면 admin site에 출력되지 않음

   <img width="614" alt="dj_83" src="https://user-images.githubusercontent.com/86648892/189502180-c81ecf0b-eb74-4e84-9247-e8f3c16b482d.png">

## [참고] User 모델 상속 관계

<img width="265" alt="dj_84" src="https://user-images.githubusercontent.com/86648892/189502185-e95cec36-78f9-4131-aaff-9bd51c3de265.png">

## [참고] AbstractUser

- “관리자 권한과 함께 완전한 기능을 가지고 있는 User model을 구현하는 추상 기본클래스”
  - Abstract이 붙는 클래스는 테이블에 생성되는 것이 아닌 기본 클래스로서 존재
- **_Abstract Base Classes (추상 기본 클래스)_**
  - 몇가지 공통 정보를 여러 다른 모델에 넣을 때 사용하는 클래스
  - 데이터베이스 테이블을 만드는데 사용되지 않으며, 대신 다른 모델의 기본클래스로 사용되는 경우 해당 필드가 하위 클래스의 필드에 추가됨
  - [Python Docs - Abstract Base Classes](https://docs.python.org/3/library/abc.html)

## 데이터베이스 초기화

- 프로젝트 중간에 AUTH_USER_MODEL을 변경하는 것은 모델 관계에 영향을 미치기에 더 어려운 작업이 필요
  - 예를 들어 변경사항이 자동으로 수행될 수 없기에 DB 스키마를 직접 수정하고, 이전 사용자 테이블에서 데이터를 이동하고, 일부 마이그레이션을 수동으로 다시 적용해야 하는 등
    - 결론은 **프로젝트 처음에 진행하자**
- 프로젝트 중간이라면?
  - 데이터베이스 초기화 후 진행
    1. migrations 파일 삭제
       - migrations 폴더 및 `__init__.py` 는 삭제하지 않음
       - 번호가 붙은 파일만 삭제
    2. db.sqlite3 삭제
    3. migrations 진행
       - makemigrations
       - migrate
- 이제 auth_user 테이블이 아니라 accounts_user 테이블을 사용하게 됨

## 반드시 User 모델을 대체해야 할까?

- Django는 새 프로젝트를 시작하는 경우 비록 기본 User 모델이 충분하더라도 커스텀 User 모델을 설정하는 것을 **강력하게 권장(highly recommended)**
- 커스텀 User 모델은 **기본 User 모델과 동일하게 작동하면서도 필요한 경우 나중에 맞춤 설정할 수 있기 때문**
  - 단, User 모델 대체 작업은 프로젝트의 모든 migrations 혹은 첫 migrate를 실행하기 전에 이 작업을 마쳐야함

---

# HTTP Cookies

- 로그인과 로그아웃을 이해하기에 앞서 핵심적인 개념

## HTTP

- Hyper Text Transefer Protocol
  - 웹상에서 데이터를 주고받는 약속
- 웹(WWW)에서 이루어지는 모든 데이터 교환의 기초
- HTML 문서와 같은 리소스들을 가져올 수 있도록 해주는 프로토콜(규칙, 규약)
- 클라이언트-서버 프로토콜이라고도 부름

## 요청과 응답

- **_요청(requests)_**
  - 클라이언트(브라우저)에 의해 전송되는 메세지
- **_응답(response)_**
  - 서버에서 응답으로 전송되는 메세지

## HTTP 특징

1. **_비연결지향(connectionless)_**
   - 연결되어있는 상태가 아니라 요청이 있을 때만 응답을 주고 끝
   - 서버는 요청에 대한 응답을 보낸 후 연결을 끊음
     - ex) 우리가 네이버 메인 페이지를 보고 있을 때 우리는 네이버 서버와 연결되어 있는 것이 아님
       - 네이버 서버는 우리에게 메인 페이지를 응답하고 연결을 끊은 것
2. **_무상태(stateless)_**
   - 비연결지향에 의해 상태 정보가 유지되지 않음
   - 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며 상태 정보가 유지되지 않음
   - 클라이언트와 서버가 주고받는 메세지들은 서로 완전히 독립적

## 어떻게 로그인 상태를 유지할까?

- HTTP 특성에 의해서 원래는 로그인하고 난 뒤 다른 페이지로 이동하면 로그인 상태가 유지되지 않아야함
  - “쿠키와 세션"으로 로그인 상태를 유지할 수 있음
- 비연결지향에 의해 무상태가 나오고
  - 이를 해결하기 위한 기술이 쿠키와 세션
- **_서버와 클라이언트 간 지속적인 상태 유지를 위해 “쿠키와 세션"이 존재_**

# 쿠키(Cookie)

- HTTP 쿠키는 “상태가 있는 세션”을 만들도록 해줌

## 개념

- 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각이다
  - 쉽게 말해 브라우저에서 했던 행동을 저장해놓을 수 있는 곳
    - KEY-VALUE 형태로 저장
- 사용자가 웹사이트를 방문할 경우 해당 웹사이트의 서버를 통해 사용자의 컴퓨터에 설치되는 작은 기록 정보 파일
  1. 브라우저(클라이언트)는 쿠키를 로컬에 KEY-VALUE의 데이터 형식으로 저장
  2. 이렇게 쿠키를 저장해 놓았다가, **_동일한 서버에 재요청 시 저장된 쿠키를 함께 전송_**
- 쿠키는 두 요청이 동일한 브라우저에서 들어왔는지 아닌지를 판단할 때 주로 사용됨
  - 이를 이용해 사용자의 로그인 상태를 유지할 수 있음
    - 쿠키에 “나 로그인된 사용자야"라는 정보를 담아 매 요청마다 서버에 전송하는 것
  - 상태가 없는(stateless) HTTP 프로토콜에서 상태 정보를 기억시켜주기 때문
- 즉, 웹 페이지에 접속하면 웹 페이지를 응답한 서버로부터 쿠키를 받아 브라우저에 저장하고, 클라이언트가 같은 서버에 재요청 시마다 요청과 함께 저장해둔 쿠키도 함께 전송

<img width="1176" alt="dj_85" src="https://user-images.githubusercontent.com/86648892/189502186-1f8fd6e9-96f0-409a-b32c-1e969f5c9022.png">

## 쿠키 사용 목적

1. 세션 관리(Session Management)
   - 로그인, 아이디 자동완성, 공지 하루 안보기, 팝업 체크, 장바구니 등의 정보 관리
2. 개인화(Personalization)
   - 사용자 선호, 테마 등의 설정
3. 트래킹(Tracking)
   - 사용자 행동을 기록 및 분석
     - 어떤 상품을 많이 봤는지 등

## 쿠키 확인

- 개발자도구 - Network 탭

<img width="647" alt="dj_86" src="https://user-images.githubusercontent.com/86648892/189502187-073710a1-dd7b-474a-96a3-c3214d9a2f02.png">

- 서버는 Set-Cookie 응답 헤더를 브라우저에게 전송
  - 이 헤더를 통해 클라이언트에게 쿠키를 저장하라고 전달

<img width="697" alt="dj_87" src="https://user-images.githubusercontent.com/86648892/189502189-634de91f-41be-4202-b8f9-149678e5e125.png">

- 브라우저 역시 서버로 전송되는 모든 요청에 Cookie HTTP 헤더를 사용해 서버로 이전에 저장했던 모든 쿠키들을 함께 전송
  - 위 예시는 쿠팡 장바구니 정보를 저장
- 개발자도구 - Application 탭 - Cookies
  - 저장되어 있는 쿠키 확인

<img width="755" alt="dj_88" src="https://user-images.githubusercontent.com/86648892/189502190-f6e16994-6d70-4ddd-ab06-192f4982cf6b.png">

- 쿠키를 지우면(우측 클릭 - Clear) 상태가 유지되지 않는 것을 확인할 수 있음

# 세션(Session)

- 사이트와 특정 브라우저 사이의 “state(상태)”를 유지시키는 것
- 클라이언트가 서버에 접속하면
  - 서버가 특정 session id를 발급하고, 클라이언트는 session id를 쿠키에 저장
    - 클라이언트가 다시 동일한 서버에 접속하면 요청과 함께 쿠키(session id가 저장된)를 서버에 전달
      - 쿠키는 요청 때마다 서버에 함께 전송되므로 서버에서 session id를 확인해 알맞은 로직을 처리
- session id는 세션을 구별하기위해 필요하며, 쿠키에는 session id만 저장

### 쿠키 Lifetime(수명)

1. **_Session cookie_**
   - 현재 세션(current session)이 종료되면 삭제됨
   - 브라우저 종료와 함께 세션이 삭제됨
2. **_Persistent cookies_**
   - Expires 속성에 지정된 날짜 혹은 Max-Age 속성에 지정된 기간이 지나면 삭제됨

## Session in Django

- Django는 **_database-backed sessions 저장 방식_**을 기본값으로 사용
  - session 정보는 Django DB의 **_django_session 테이블_**에 저장됨
  - 설정을 통해 다른 저장 방식으로 변경 가능
    - [Django Docs - How to use sessions](https://docs.djangoproject.com/en/4.1/topics/http/sessions/)
- Django는 특정 session id를 포함하는 쿠키를 사용해서 각각의 브라우저와 사이트가 연결된 session을 알아냄
- 사용자에게는 session_key만 줌
  - 사용자에 대한 중요한 정보는 session_data에 담아 서버가 들고있음

---

# Authentication in Web requests

- Django가 제공하는 인증 관련 built-in forms
  - 인증은 직접 form을 구현하기 어렵기에 Django에서 로그인, 가입, 비밀번호 변경 등 인증 관련 built-in forms를 제공함
    - [Django Docs - Built-in forms](https://docs.djangoproject.com/en/4.1/topics/auth/default/#module-django.contrib.auth.forms)

# Login

- 로그인은 **_Session을 Create_**하는 과정

## AuthenticationForm

- 로그인을 위한 built-in form
  - 로그인하고자 하는 사용자 정보를 입력받음
  - 기본적으로 username과 password를 받아 데이터가 유효한지 검증

### 로그인 구현

- 로그인 로직
  - ID와 PW를 비교하여 일치하는지 확인하고
    - 일치한다면 session을 생성하고
      - 해당 sessionid를 돌려주고 쿠키에 담음
  - 이것을 AuthenticationForm을 통해 쉽게 구현
- 로그인 페이지 구현
  - 페이지 렌더링
    - GET
  - 인증
    - POST
- `AuthenticationForm()`
  - `class AuthenticationForm(forms.Form)`
    - request를 첫번째 인자로 취함
    - Form을 상속받음
      - 인증에만 쓰이고 DB를 다루는 것은 아니기에 ModelForm일 필요없음

<img width="500" alt="dj_89" src="https://user-images.githubusercontent.com/86648892/189502191-2590ffef-2ee7-4f72-acd4-41b9cb0f5f35.png">

<img width="617" alt="dj_90" src="https://user-images.githubusercontent.com/86648892/189502193-9b534508-c8a6-4ca0-b606-09644b3aadfc.png">

- `from django.contrib.auth.forms import AuthenticationForm`
- `login()`
  - `login(request, user, backend=None)`
    - 인증된 사용자를 로그인시키는 로직으로 view 함수에서 사용
      - 입력된 데이터 판단 → 현재 세션에 데이터를 입력 → 로그인
    - 현재 세션에 연결하려는 인증된 사용자가 있는 경우 사용
    - HttpRequest 객체와 User 객체가 필요
  - views 함수의 login 함수와 이름 중복을 피하기 위해 `import login as auth_login`
  - `get_user()`
    - AuthenticationFrom의 인스턴스 메서드
    - 유효성 검사를 통과했을 경우 로그인한 사용자 객체를 반환

### 세션 데이터 확인

- 로그인 후 개발자 도구와 DB에서 Django로부터 발급받은 세션 확인
  - django_session 테이블에서 확인
  - 브라우저의 개발자도구 - Application - Cookies에서 확인

## Templates and Context Processors

- 템플릿에서 인증 관련 데이터 출력

<img width="614" alt="dj_91" src="https://user-images.githubusercontent.com/86648892/189502194-162af42e-cad5-409e-acfd-336f7e405eaa.png">

- context 데이터가 없는데 user 변수를 어떻게 사용할 수 있을까?

  - `settings.py`의 **_context processors_** 설정값 때문
  - `context_processors`

    - 템플릿이 렌더링될 때 호출 가능한 컨텍스트 데이터 목록

      - 작성된 컨텍스트 데이터는 기본적으로 템플릿에서 사용가능한 변수로 포함됨
      - 즉, Django에서 자주 사용하는 데이터 목록을 미리 템플릿에 로드해둔 것
        <img width="584" alt="dj_92" src="https://user-images.githubusercontent.com/86648892/189502195-14fe5b93-697e-4b49-a95e-b4adcab57e4d.png">

      - user 변수를 담당하는 프로세서는 `django.contrib.auth.context_processors.auth`
        - [Django Docs - Built-in template context processors](https://docs.djangoproject.com/en/4.1/ref/templates/api/#built-in-template-context-processors)
      - `user` 의 경우 인증된 사용자라면 `User()` 클래스 인스턴스로 출력, 인증되지 않은 사용자라면 `AnonymousUser()` 클래스 인스턴스로 출력

# Logout

- 로그아웃은 **_Session을 Delete_**하는 과정
  - 클라이언트(sessionid)와 서버에 있는 세션 정보를 삭제
  - 유저 정보 삭제가 아님
    - 유저 정보 삭제는 회원탈퇴
- `logout(request)`
  - HttpRequest 객체를 인자로 받고 반환값이 없음
  - 사용자가 로그인하지 않은 경우 오류를 발생시키지 않음
  - 2가지 일 처리
    1. 현재 요청에 대한 session data를 DB에서 삭제
    2. 클라이언트의 쿠키에서도 sessionid를 삭제
    - 이는 다른 사람이 동일한 웹 브라우저를 사용하여 로그인하고, 이전 사용자의 세션 데이터에 액세스하는 것을 방지하기 위함

<img width="1191" alt="dj_93" src="https://user-images.githubusercontent.com/86648892/189502196-6fab2e54-ee7b-4276-a1ee-1a0f3c70f572.png">

---

# 회원 가입

- 회원가입은 User를 **_Create_**하는 것이며 **_UserCreationForm_**이라는 built-in form 사용

## UserCreationForm

- 주어진 username과 password로 권한이 없는 새 user를 생성하는 ModelForm
- 3개의 필드를 가짐
  1. username (from the user model)
  2. password1
  3. password2
- `signup()`
  - 회원가입 페이지를 렌더링할 페이지 생성
  - 새로운 유저 모델 생성

<img width="533" alt="dj_94" src="https://user-images.githubusercontent.com/86648892/189502197-aa0c7e9c-2804-4e80-a0f4-d32cfe32b174.png">

<img width="634" alt="dj_95" src="https://user-images.githubusercontent.com/86648892/189502198-f99cdf80-c22a-4169-bbd4-c40ef035a204.png">

<img width="718" alt="dj_96" src="https://user-images.githubusercontent.com/86648892/189502199-c47a2024-7c9b-4cff-af36-9f3b709db91a.png">

### 에러 페이지 확인

<img width="945" alt="dj_97" src="https://user-images.githubusercontent.com/86648892/189502201-697a1e10-a251-44f4-a6f4-60ab7d861edd.png">

- `UserCreationForm()`은 ModelForm으로 우리가 대체한 커스텀 유저 모델이 아닌 기존 유저 모델을 바탕으로 작성된 클래스
  - built-in User model인 ‘auth.User’를 바탕으로 만들어짐
    - class Meta에 `model = User` 로 적혀있음
    - 상속을 통해 Meta 정보를 바꿔줘야 한다
      - accounts의 `forms.py`에서 `CustomUserCreationForm()` 생성

# Custom user & Built-in auth forms

- 기존 User 모델을 참조하는 Form인지 여부

### AbstractBaseUser의 모든 subclass와 호환되는 forms

- User 모델을 대체하더라도 커스텀하지 않아도 되는 Form 클래스
  1. AuthenticationForm
  2. SetPasswordForm
  3. PasswordChangeForm
  4. AdminPasswordChangeForm
- 기존 User 모델을 참조하는 Form이 아님

### 커스텀 유저 모델을 사용하려면 다시 작성하거나 확장해야하는 forms

1. UserCreationForm
   - 회원가입
2. UserChangeForm
   - 회원정보수정

- 두 form 모두 `class Meta: model = User` 가 등록된 form이기에 반드시 커스텀(확장)해야함

## CustomUserCreationForm()

<img width="849" alt="dj_98" src="https://user-images.githubusercontent.com/86648892/189502202-81532ad9-5622-4759-87b1-2fd7d1ec9be6.png">

### `get_user_model()`

- **_현재 프로젝트에서 활성화된 사용자 모델(active user model)_**을 반환
- 직접 커스텀 유저 모델을 import해서 참조할 수도 있으나
  - Django는 User 클래스를 직접 참조하는 대신 `get_user_model()` 을 사용해 참조해야한다고 강조함
- 직접 참조하지 않는 이유
  - 예를 들어 기존 User 모델이 아닌 User 모델을 커스텀한 상황에서는 커스텀 User 모델을 자동으로 반환해주기 때문

<img width="724" alt="dj_99" src="https://user-images.githubusercontent.com/86648892/189502203-a09403a1-1f7e-45a1-8dbe-5c1a2244957b.png">

<img width="749" alt="dj_100" src="https://user-images.githubusercontent.com/86648892/189502204-ced07494-fb5e-40e4-a3d4-a34f1106cf1e.png">

### [참고] UserCreationForm의 save()

- user를 반환함

<img width="771" alt="dj_101" src="https://user-images.githubusercontent.com/86648892/189502205-7cade324-21f5-4fc1-b2f9-7ee5dff4b131.png">

# 회원 탈퇴

- 회원 탈퇴는 DB에서 유저 모델을 **_Delete_**하는 것

<img width="517" alt="dj_102" src="https://user-images.githubusercontent.com/86648892/189502207-a78c2b8a-583a-465c-80bf-1ee0bc1d89e0.png">

<img width="555" alt="dj_103" src="https://user-images.githubusercontent.com/86648892/189502208-a464a491-710d-4392-be36-37a82514010b.png">

<img width="613" alt="dj_104" src="https://user-images.githubusercontent.com/86648892/189502210-197d028d-adb2-4c93-9b45-dd21558b1c20.png">

### [참고] 탈퇴하면서 해당 유저의 세션 정보도 함께 지우고 싶을 경우

- 순서가 중요
- `request.user.delete()`
  - 탈퇴
  - `auth_logout(request)`
    - 로그아웃
- 로그아웃을 먼저 하면 요청의 객체 정보가 사라져 탈퇴에 필요한 정보가 사라짐

# 회원정보 수정

- 회원정보 수정은 User를 **_Update_**하는 것이며 **_UserChangeForm_** built-in form을 사용

## UserChangeForm

- 사용자의 정보 및 권한을 변경하기 위해 admin 인터페이스에서 사용되는 ModelForm
  - admin 페이지에서 이미 쓰고있는 것을 사용자에게도 보여주자는 것
- UserChangeForm 또한 ModelForm이기에 instance 인자 설정
- CustomUserCreationForm과 같이 CustomUserChangeForm 사용
- 유저 모델을 다루기에 ModelForm
- admin 인터페이스에서 사용됨 (admin 페이지)
- admin 페이지에서 이미 쓰고있는 것을 사용자에게도 보여주자

<img width="537" alt="dj_105" src="https://user-images.githubusercontent.com/86648892/189502211-4aef9f08-8bef-455d-bc0c-9e948fa21bd8.png">

<img width="539" alt="dj_106" src="https://user-images.githubusercontent.com/86648892/189502212-960971b6-de62-4ccb-a1d8-d59d5f88f271.png">

<img width="742" alt="dj_107" src="https://user-images.githubusercontent.com/86648892/189502213-ddfcbbe1-35e2-438f-8596-d9f2527a733f.png">

<img width="839" alt="dj_108" src="https://user-images.githubusercontent.com/86648892/189502214-f08ca6d0-d437-44b5-8c54-a592b92236c6.png">

<img width="510" alt="dj_109" src="https://user-images.githubusercontent.com/86648892/189502216-3b29a597-dc96-49ee-bb2d-7b2690e96ccb.png">

### UserChangeForm의 필드 변경

<img width="935" alt="dj_110" src="https://user-images.githubusercontent.com/86648892/189502217-c94ae010-58e0-4ee5-b75a-7b3414479ae6.png">

- 필드 설정을 하지 않을 시 일반 사용자가 접근해서는 안될 정보들(fields)까지 모두 수정이 가능해짐
  - admin 인터페이스에서 사용되는 ModelForm이기 때문
- 따라서 UserChangeForm을 상속받아 작성해둔 서브클래스 CustomUserChangeForm에서 접근 가능한 필드를 조정
- User 모델의 fields명은 migrations 파일이나 공식문서에서 확인
  - [Django Docs - User model Fields](https://docs.djangoproject.com/en/4.1/ref/contrib/auth/#fields)

---

# 비밀번호 변경

## PasswordChangeForm

- 사용자가 비밀번호를 변경할 수 있도록 하는 Form
- 이전 비밀번호를 입력하여 비밀번호를 변경할 수 있도록 함
- 이전 비밀번호를 입력하지 않고 비밀번호를 설정할 수 있는 SetPasswordForm을 상속받는 서브클래스
- Django에서 내부적으로 폼을 누르면 `/accounts/password/` 로 보냄
  - 여기에 맞춰서 url 설정
- `from django.contrib.auth.forms import PasswordChangeForm`

<img width="556" alt="dj_111" src="https://user-images.githubusercontent.com/86648892/189502218-10a11997-5813-4e5b-ab4b-57568dc13253.png">

<img width="557" alt="dj_112" src="https://user-images.githubusercontent.com/86648892/189502219-575582e1-4298-4d56-b250-79e680baf093.png">

<img width="804" alt="dj_113" src="https://user-images.githubusercontent.com/86648892/189502220-0a84a68e-e24e-4735-982a-4e534dcdcace.png">

### 암호 변경 시 세션 무효화 방지

- 비밀번호 변경이 성공적으로 진행되면 로그아웃됨
  - 비밀번호가 변경되면 기존 세션과의 회원 인증 정보가 일치하지 않아서 로그인 상태가 유지되지 못함
  - 비밀번호는 잘 변경되었으나 비밀번호가 변경되면서 기존 세션과의 회원 인증 정보가 일치하지않기 때문
  - 기존 세션과의 싱크업 과정이 필요함
    - `update_session_auth_hash(request, user)`

### `update_session_auth_hash(request, user)`

- 현재 요청(current request)과 새 session data가 파생될 업데이트된 user 객체를 가져오고, session data를 적절하게 업데이트
- 암호가 변경되어도 로그아웃되지 않도록 새로운 password의 session data로 session을 업데이트

---

# Limiting access to logged-in users

- 로그인 사용자에 대한 접근 제한하기
- 로그인 사용자에 대해 접근을 제한하는 2가지 방법
  1. `is_authenticated` attribute
  2. `login_required` decorator

## is_authenticated

- User model의 속성(attributes) 중 하나
- 사용자가 인증되었는지 여부를 알 수 있는 방법
- 모든 User 인스턴스에 대해 항상 True인 읽기 전용 속성
  - AnonymousUser에 대해서는 항상 False
- 일반적으로 `request.user` 에서 이 속성을 사용
  - `request.user.is_authenticated`
- 권한(permission)과는 관련이 없으며, 사용자가 활성화 상태(active)이거나 유효한 세션(valid session)을 가지고 있는지도 확인하지 않음

<img width="848" alt="dj_114" src="https://user-images.githubusercontent.com/86648892/189502222-52c4c831-f217-4881-a62e-4f5c0f299d32.png">

### is_authenticated 적용

- 로그인과 비로그인 상태에서 출력되는 링크를 다르게 설정

<img width="750" alt="dj_115" src="https://user-images.githubusercontent.com/86648892/189502224-e7c19354-43b5-442e-9a64-ac4600f8cb91.png">

- 인증된 사용자만 게시글 작성 링크를 볼 수 있도록 처리
  - 아직 비로그인 상태로도 URL을 직접 입력하면 게시글 작성 페이지로 갈 수 있긴함
    - `login_required` 데코레이터를 향후 활용하여 처리

<img width="886" alt="dj_116" src="https://user-images.githubusercontent.com/86648892/189502225-08a8fb0e-4777-4a1f-bf92-c8c8cff46611.png">

- 인증된 사용자라면 로그인 로직을 수행할 수 없도록 처리

<img width="629" alt="dj_117" src="https://user-images.githubusercontent.com/86648892/189502227-e0e1c5b2-d7b9-49ac-95e5-0b8bb0612c1c.png">

## login_required

- login_required decorator
- 사용자가 로그인되어 있다면 정상적으로 view 함수 실행
- 로그인하지 않은 사용자의 경우 `settings.py` 의 `LOGIN_URL` 문자열 주소로 redirect
  - `LOGIN_URL`의 기본값은 `/accounts/login/`
  - app 이름을 accounts로 했던 이유 중 하나!
  - `/articles/create/` 로 강제 접속을 시도해보면 로그인 페이지로 리다이렉트 후 `/accounts/login/?next=/articles/create/` url을 확인할 수 있음
    - **_인증 성공 시 사용자가 redirect되어야하는 경로는 “next”라는 쿼리 문자열 매개 변수에 저장됨_**

### login_required 적용

- 로그인 상태에서만 글을 작성, 수정, 삭제할 수 있도록 변경

<img width="760" alt="dj_118" src="https://user-images.githubusercontent.com/86648892/189502228-0c477880-3631-4702-95f7-dc7fc44d07af.png">

### “next” query string parameter

- 로그인이 정상적으로 진행되면 이전에 요청했던 주소로 redirect하기 위해 Django가 제공해주는 쿼리 스트링 파라미터
- 해당 값을 처리할지 말지는 자유이며 별도로 처리해주지 않으면 view에 설정한 redirect 경로로 이동하게됨

<img width="903" alt="dj_119" src="https://user-images.githubusercontent.com/86648892/189502229-8feaee79-3b9c-4e4a-9178-a381bedffa09.png">

<img width="731" alt="dj_120" src="https://user-images.githubusercontent.com/86648892/189502230-b4977862-a594-44da-8606-ce65566161d2.png">

- `/accounts/login/` 과 `/accounts/login/?next=...` 인 경우 2가지를 처리해야 하므로 현재 url로 요청을 보내도록 `action=""` 으로 변경

---

### `@login_required` 와 `@require_POST` 충돌

- `@login_required` 는 GET request method를 처리할 수 있는 view 함수에서만 사용
- 게시글 삭제(delete) 함수 예시
  - 원래는 게시글 삭제 버튼 누르면 해당 url로 POST 요청하여 삭제
  - 비로그인 상태로 detail 페이지에서 게시글 삭제 시도
    - login_required에 의해 로그인 페이지로 리다이렉트
      - `http://127.0.0.1:8000/accounts/login/?next=/articles/1/delete/`
      - 로그인 완료하면
        - 더이상 버튼에 의한 POST 요청이 아닌 해당 url을 통해 GET 요청으로 변함
        - require_POST와 충돌
          - 405(Method Not Allowed) status code
- 2가지 문제가 발생
  1. redirect 과정에서 POST 요청 데이터의 손실
  2. redirect로 인한 요청은 GET 요청 메서드로만 요청됨
- POST method만 허용하는 delete같은 함수는 내부에서 `is_authenticated` 속성을 통해 처리

<img width="667" alt="dj_121" src="https://user-images.githubusercontent.com/86648892/189502231-94a64121-3512-43cf-9f60-b94e0957a3a6.png">

---

### accounts view 함수에도 이처럼 데코레이터 및 속성값 적용

<img width="913" alt="dj_122" src="https://user-images.githubusercontent.com/86648892/189502232-8c482901-5c4a-4440-a1e0-cee796cb0402.png">

---

## 정리

- The Django authentication system
  - User 모델 대체하기
- HTTP Cookies
  - 상태가 있는 세션 구성
- Authentication in Web requests
  - auth built-in form 사용하기
- Authentication in User
  - User Object와 User CRUD

---

# [추가] 패스워드 저장

- [안전한 패스워드 저장](https://d2.naver.com/helloworld/318732)
- [Django Docs - Password management in Django](https://docs.djangoproject.com/en/3.2/topics/auth/passwords/)

## 패스워드 저장 알고리즘

- password는 유저 모델의 필드가 아니다
  - 따로 저장됨
- 비밀번호를 저장할 땐 어떤 방식(알고리즘)을 사용하는가?
  - 단순 텍스트
    - 말도 안됨
  - 단방향 해쉬 함수의 다이제스트
    - 보완 알고리즘
      - 솔팅(Salting)
      - 키 스트레칭(Key Stretching)

<img width="857" alt="dj_123" src="https://user-images.githubusercontent.com/86648892/189502470-8db20282-1b2b-4d91-a5e4-d644acf53e70.png">

- 솔팅과 키 스트레칭을 바탕으로 한 검증된 Adaptive Key Derivation Function
  - PBKDF2
  - bcrypt
  - scrypt

## 패스워드 저장 in Django

Django는 비밀번호 저장을 위해 salting과 key stretching을 바탕으로 한 adaptive key derivation function 중 PBKDF2를 기본으로 채택하고 있다.

- User 객체의 password 속성에 부여되는 비밀번호 값은 `<algorithm>$<iterations>$<salt>$<hash>` 포맷의 문자열이다.
- 이러한 저장값을 생성하기 위해 사용하는 해쉬 함수는 Django의 `PASSWORD_HASHERS`를 통해 설정되며, 기본 코드는 다음과 같다.

```python
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]
```

- Django는 `PASSWORD_HASHERS`의 첫번째 값, 즉 `settings.PASSWORD_HASHERS[0]`을 참조하여 암호 저장 알고리즘을 채택한다.
- 위 코드의 경우 PBKDF2 방식으로 저장은 하지만, 암호 검사 시 PBKDF2SHA1, argon2, bcrypt 방식도 지원함을 뜻한다.

---

# Django N:1 Relationship

- A-many-to-one-relationship
- N : 1 (Comment - Article)
- N : 1 (Article - User)
- N : 1 (Comment - User)

---

# A-many-to-one-relationship

- 관계형 데이터베이스에서의 외래키 속성을 사용해 모델간 N:1 관계 설정하기
- 외래 키(ForeignKey)를 사용하여 RDB의 테이블 간 관계를 만들 수 있음
  - 관계(Relationship)란?
    - 테이블 간의 상호작용을 기반으로 설정되는 여러 테이블 간의 논리적인 연결

### 테이블 간 관계 예시

<img width="1176" alt="dj_124" src="https://user-images.githubusercontent.com/86648892/212546968-e41f595f-7e34-4ab4-8970-35446e7ecceb.png">

## RDB에서의 관계

1. `1:1`
   - One-to-one relationships
   - 한 테이블의 레코드 하나가 다른 테이블의 레코드 단 한 개와 관련된 경우
2. `N:1`
   - Many-to-one relationships
   - 한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 한 개와 관련된 경우
   - 기준 테이블에 따라 1:N, One-to-many relationships라고도 함
3. `M:N`
   - Many-to-many relationships
   - 한 테이블의 0개 이상의 레코드가 다른 테이블의 0개 이상의 레코드와 관련된 경우
   - 양쪽 모두에서 N:1 관계를 가짐

## Django Relationship Fields

1. `OneToOneField()`
   - A one-to-one relationship
2. `ForeignKey()`
   - A many-to-one relationship
3. `ManyToManyField()`
   - A-many-to-many relationship

---

## Foreign Key

- 외래 키 (외부 키)
- 관계형 데이터베이스에서 다른 테이블의 행을 식별할 수 있는 키
- 참조되는 테이블의 기본 키(Primary Key)를 가리킴
- 참조하는 테이블의 행 1개의 값은, 참조되는 측 테이블의 행 값에 대응됨
  - 즉, 참조하는 테이블의 행에는, 참조되는 테이블에 나타나지 않는 값을 포함할 수 없음
- 참조하는 테이블 행 여러 개가, 참조되는 테이블의 동일한 행을 참조할 수 있음
- **_부모 테이블의 유일한 값을 참조_**
  - **_참조 무결성_**
  - **_외래 키의 값이 반드시 부모 테이블의 Primary Key일 필요는 없지만 유일한 값이어야 함_**

### [참고] 참조 무결성

- 데이터베이스 관계 모델에서 관련된 2개의 테이블 간의 일관성을 말함
- 외래 키가 선언된 테이블의 외래 키 속성(열)의 값은 그 테이블의 부모가 되는 테이블의 기본 키 값으로 존재해야 함

## `ForeignKey(to, on_delete, **options)`

- A many-to-one relationship을 담당하는 Django의 모델 필드 클래스
- Django 모델에서 관계형 데이터베이스의 외래 키 속성을 담당
- 2개의 필수 위치 인자가 필요
  1. **_참조하는 model class_**
  2. `***on_delete` 옵션\*\*\*
     - 외래 키가 참조하는 객체가 사라졌을 때, 외래 키를 가진 객체를 어떻게 처리할지 정의
     - 데이터 무결성을 위해 매우 중요한 설정
     - `on_delete` 옵션 값
       - `CASCADE`
         - 부모 객체(참조된 개체)가 삭제되었을 때 이를 참조하는 객체도 삭제
       - `PROJECT`
         - 참조하는 객체가 있다면 참조되는 해당 객체를 못지우도록 설정
       - `SET_NULL`
         - 부모 객체가 삭제되었을 때 참조하는 객체의 값을 NULL로 설정
       - `SET_DEFAULT`
         - 부모 객체가 삭제되었을 때 참조하는 객체의 값을 설정한 기본값으로 대체

### [참고] 데이터 무결성 (Data Integrity)

- 데이터의 정확성과 일관성을 유지하고 보증하는 것
- 데이터베이스나 RDBMS의 중요한 기능
- 무결성 제한의 유형
  1. 개체 무결성 (Entity Integrity)
  2. 참조 무결성 (Referential Integrity)
  3. 범위 무결성 (Domain Integrity)

---

## Related Manager (관계 모델 참조)

- Related manager는 N:1 혹은 M:N 관계에서 사용가능한 문맥(context)
- Django는 모델 간 N:1 혹은 M:N 관계가 설정되면 `역참조` 할 때에 사용할 수 있는 manager를 생성
  - 이전에 모델 생성 시 `objects` 라는 매니저를 통해 queryset api를 사용했던 것처럼
    - Related manager를 통해 queryset api를 사용할 수 있게 됨
- N:1 관계에서 생성되늰 Related manager 이름은 참조하는 **_“모델명\_set”_** 이름 규칙으로 만들어짐
  - `ForeignKey()` 설정 시 `related_name` 옵션을 통해 역참조 시 사용할 매니저 이름을 설정 가능
    - 작성 후 migration 과정 필요
    - 설정 시 기존의 `modelName_set` 은 더이상 사용할 수 없고, 대체됨

## 역참조

- 나를 참조하는 테이블(나를 외래 키로 지정한)을 참조하는 것
  - 본인을 외래 키로 참조 중인 다른 테이블에 접근하는 것
  - N:1에서는 1이 N을 참조하는 상황

<img width="1163" alt="dj_125" src="https://user-images.githubusercontent.com/86648892/212546967-3acdd5b9-c4b5-45df-81b3-a240c8f7b9e0.png">

<img width="1090" alt="dj_126" src="https://user-images.githubusercontent.com/86648892/212546965-bef1a122-25cb-402b-9978-f9f6229b8a2c.png">

---

# Referencing the User Model

## Django에서 User 모델을 참조하는 2가지 방법

1. `settings.AUTH_USER_MODEL`
   - 문자열을 반환
     - 반환값은 ‘accounts.User’ (문자열)
   - User 모델에 대한 외래 키 또는 M:N 관계를 정의할 때 사용
   - **_`models.py`의 모델 필드에서 User 모델을 참조할 때 사용_**
     - 장고 내부적인 동작순서에 따라 아직 유저 객체가 생성되지 않은 시점에서 `models.py` 가 임시로 참조할 수 있도록 문자열을 주는 것
2. `get_user_model()`
   - 객체를 반환
     - 반환값은 User Object (객체)
   - 현재 활성화(Active)된 User 모델을 반환
     - 커스터마이징한 User 모델이 있을 경우는 Custom User 모델, 그렇지 않으면 User를 반환
   - **_`models.py` 가 아닌 다른 모든 곳에서 유저 모델을 참조할 때 사용_**

---

# N : 1 (Comment - Article)

- Comment(N) - Article(1)
- Comment 모델과 Article 모델 간 관계 설정
- “0개 이상의 댓글은 1개의 게시글에 작성될 수 있음”

<img width="1068" alt="dj_127" src="https://user-images.githubusercontent.com/86648892/212546962-d8c3df94-0bf4-4c13-bfdb-d6fd8085367e.png">

## Comment 모델 정의

<img width="815" alt="dj_128" src="https://user-images.githubusercontent.com/86648892/212546960-57b2b1a5-8516-432e-9a8d-45ab168403dd.png">

- 외래 키 필드는 ForeignKey 클래스를 작성하는 위치와 관계없이 필드의 마지막에 작성됨
- `ForeignKey()` 클래스의 인스턴스 이름은 참조하는 모델 클래스 이름의 단수형(소문자)으로 작성하는 것을 권장
  - migration 과정 진행
    <img width="1068" alt="dj_129" src="https://user-images.githubusercontent.com/86648892/212546959-901cce13-1e0e-4a21-a31b-9f54c93ea9f8.png">

<img width="1046" alt="dj_130" src="https://user-images.githubusercontent.com/86648892/212546958-c2b7c241-b9cd-45dc-ac8c-5f55dd9a790f.png">

<img width="1031" alt="dj_131" src="https://user-images.githubusercontent.com/86648892/212546957-46ab927b-8bec-4c80-8105-3f5b87e3b176.png">

<img width="1025" alt="dj_132" src="https://user-images.githubusercontent.com/86648892/212546956-631d339f-286c-46c0-8803-82cb36939db4.png">

<img width="1030" alt="dj_133" src="https://user-images.githubusercontent.com/86648892/212546954-72bf657e-4e90-41c1-a457-54af27b340aa.png">

---

# Comment CRUD 구현

## CREATE

- CommentForm 작성
  - 외래 키 필드는 사용자로부터 받는 입력이 아니므로 출력에서 제외
- 기존의 ArticleForm 클래스의 인스턴스명을 `form` 으로 작성했기에 헷갈리지 않도록 `comment_form` 으로 작성
- 출력에서 제외된 외래 키의 경우 url에서 `variable routing` 을 활용하여 받아온 pk값을 활용
- `***save(commit=False)` 옵션 활용\*\*\*
  - “Create, but don’t save the new instance”
    - 아직 데이터베이스에 저장되지 않은 인스턴스를 반환
    - 저장하기 전에 객체에 대한 사용자 지정 처리를 수행할 때 유용하게 사용
  - commit 옵션을 활용해 DB에 저장되기 전 comment 객체에 article 객체 저장하기

<img width="605" alt="dj_134" src="https://user-images.githubusercontent.com/86648892/212546952-62aaed63-6e6e-4ff6-85b5-38d784e89232.png">

<img width="717" alt="dj_135" src="https://user-images.githubusercontent.com/86648892/212546951-b6de9101-d9b6-453f-adf5-d7b8a86426fa.png">

<img width="562" alt="dj_136" src="https://user-images.githubusercontent.com/86648892/212546950-d099bacf-1862-4ca7-ae28-804bd4e9e0cb.png">

<img width="560" alt="dj_137" src="https://user-images.githubusercontent.com/86648892/212546949-40d98ce4-ba67-4f74-9161-cdcac7eaadf2.png">

---

## READ

- 작성한 댓글 목록 출력하기
- 특정 article에 있는 모든 댓글을 가져온 후 context에 추가
- detail 템플릿에서 댓글 목록 출력하기

<img width="723" alt="dj_138" src="https://user-images.githubusercontent.com/86648892/212546948-e64c7719-527d-4ca0-afc1-0359ff91df7a.png">

<img width="723" alt="dj_139" src="https://user-images.githubusercontent.com/86648892/212546947-f749bcae-b663-4ff8-9837-1911b56d5c8e.png">

## DELETE

- 댓글 삭제 구현하기
- 댓글을 삭제할 수 있는 버튼을 각각의 댓글 옆에 출력될 수 있도록 함

<img width="1154" alt="dj_140" src="https://user-images.githubusercontent.com/86648892/212546945-88fc2e31-b48e-4e90-aa17-e7f68412c031.png">

<img width="710" alt="dj_141" src="https://user-images.githubusercontent.com/86648892/212546943-ddfed818-4ea8-4950-bc36-8d2cd3f195dc.png">

<img width="1026" alt="dj_142" src="https://user-images.githubusercontent.com/86648892/212546939-04c8bad3-623c-4dd1-8a41-c3ee25b536c2.png">

## UPDATE

- 댓글 수정은 구현하지 않음
  - 댓글 수정을 구현할 경우 게시글 수정 페이지가 필요했던 것처럼 댓글 수정 페이지가 필요
  - 하지만 일반적으로 댓글 수정은 수정 페이지로의 이동없이 현재 페이지를 유지한 상태로 댓글 작성 Form 부분만 변경되어 수정할 수 있도록 함
  - 이처럼 페이지의 일부 내용만 업데이트하는 것은 JavaScript의 영역이기 때문에 JavaScript를 학습한 후 별도로 진행

---

## DTL(Django Template Language)과 QuerySet API를 활용한 추가 댓글 구현 사항

### 댓글 개수 출력하기

<img width="768" alt="dj_143" src="https://user-images.githubusercontent.com/86648892/212546934-3a161a94-3fe7-4288-b76d-273c8d44e032.png">

<img width="951" alt="dj_144" src="https://user-images.githubusercontent.com/86648892/212546930-87135284-fbee-403e-9cbd-5b38dccb1970.png">

### 댓글이 없는 경우 대체 컨텐츠 출력하기

<img width="1162" alt="dj_145" src="https://user-images.githubusercontent.com/86648892/212546925-90d84a12-d382-4864-998d-a70c5ef51533.png">

---

# N : 1 (Article - User)

- Article(N) - User(1)
- Article 모델과 User 모델 간 관계 설정
- “0개 이상의 게시글은 1개의 회원에 의해 작성될 수 있음”
- Article 모델에 User 모델을 참조하는 외래 키 작성
  - migration 진행

<img width="1072" alt="dj_146" src="https://user-images.githubusercontent.com/86648892/212546924-3268cef1-0d14-4b05-8023-2b8c66154396.png">

<img width="1091" alt="dj_147" src="https://user-images.githubusercontent.com/86648892/212546923-3aefe3fb-9fc7-4c86-807d-93d3518bf9b5.png">

<img width="1071" alt="dj_148" src="https://user-images.githubusercontent.com/86648892/212546920-b2fa8f66-0adf-4aa7-a90c-3d00e0cd2514.png">

- 기본적으로 모든 컬럼은 `NOT NULL` 제약조건이 있기에 데이터가 없이는 새로 추가되는 외래 키 필드 user_id가 생성되지 않음
- 기본값을 어떻게 작성할지 선택
- 1을 입력하고 Enter 진행

<img width="1069" alt="dj_149" src="https://user-images.githubusercontent.com/86648892/212546918-e7f98d17-cd34-40b1-9b31-0e5d59031a9e.png">

- articel의 user_id에 어떤 데이터를 넣을 것인지 직접 입력
- 1 입력 후 Enter 진행
- 기존에 작성된 게시글은 모두 1번 회원이 작성한 것으로 처리됨

---

# Article CRUD 구현

## CREATE

- 인증된 회원의 게시글 작성 구현하기
- 작성하기 전 로그인을 먼저 진행한 상태로 진행
- ArticleForm의 출력 필드 수정
  - 사용자로부터 키를 받아오는 것이 아닌 `save(commit=False)` 를 통해 request를 보내는 사용자의 정보를 저장

<img width="606" alt="dj_150" src="https://user-images.githubusercontent.com/86648892/212546914-cfa7d769-9db6-4eab-9f8a-444612069e17.png">

<img width="773" alt="dj_151" src="https://user-images.githubusercontent.com/86648892/212547213-17588ae1-d352-44ef-8c48-cbad2e457c2e.png">

## DELETE

- 이제 게시글에 작성자 정보가 함께 들어있기 때문에 현재 삭제를 요청하려는 사람과 게시글을 작성한 사람을 비교하여 본인의 게시글만 삭제할 수 있도록 함

<img width="723" alt="dj_152" src="https://user-images.githubusercontent.com/86648892/212547212-bacff37d-662c-41d1-b0e3-9b65c8badd5c.png">

## UPDATE

- 수정도 마찬가지로 수정을 요청하려는 사람과 게시글을 작성한 사람을 비교하여 본인의 게시글만 수정할 수 있도록 함
- 추가로 해당 게시글의 작성자가 아니라면, 수정 및 삭제 버튼을 출력하지 않도록 함

<img width="1046" alt="dj_153" src="https://user-images.githubusercontent.com/86648892/212547210-53984eb4-101a-4134-88ce-34cd100daa68.png">

<img width="928" alt="dj_154" src="https://user-images.githubusercontent.com/86648892/212547209-9fb5da4f-bfe3-401d-ba3e-aea72c348d30.png">

## READ

- 게시글 작성자 출력
  - index 템플릿과 detail 템플릿에서 각 게시글의 작성자 출력

<img width="670" alt="dj_155" src="https://user-images.githubusercontent.com/86648892/212547208-01f2ca1f-a5c7-4856-97b5-0d94f03432da.png">

<img width="483" alt="dj_156" src="https://user-images.githubusercontent.com/86648892/212547207-22992f2a-e007-4a67-a636-aad3e22ef4bc.png">

---

# N : 1 (Comment - User)

- Comment(N) - User(1)
- Comment 모델과 User 모델 간 관계 설정
- “0개 이상의 댓글은 1개의 회원에 의해 작성될 수 있음”
- Comment는 Article의 id, User의 id 2개의 ForeignKey를 가지게 됨
- 마찬가지로 migration 진행 및 NOT NULL 제약조건 해결 진행

<img width="1068" alt="dj_157" src="https://user-images.githubusercontent.com/86648892/212547204-5f5d654c-0de0-4569-924a-ba206e4df450.png">

<img width="1066" alt="dj_158" src="https://user-images.githubusercontent.com/86648892/212547202-5c51c9c7-b939-4bc1-a150-dece6c8f0cb5.png">

<img width="1073" alt="dj_159" src="https://user-images.githubusercontent.com/86648892/212547201-6ac030da-782e-4528-9ea9-5c4253c97556.png">

<img width="1069" alt="dj_160" src="https://user-images.githubusercontent.com/86648892/212547199-efc96456-2a57-4a9e-8362-5c45dcef9ccb.png">

---

# Comment CRUD 구현

## CREATE

- 인증된 회원의 댓글 작성 구현하기
- 작성하기 전 로그인을 먼저 진행한 상태로 진행
- CommentForm 출력 필드 수정
  - 사용자로부터 키를 받아오는 것이 아닌 `save(commit=False)` 를 통해 request를 보내는 사용자의 정보를 저장

<img width="607" alt="dj_161" src="https://user-images.githubusercontent.com/86648892/212547198-c074ae3f-5e7c-4759-abea-f024bd10d5a1.png">

<img width="778" alt="dj_162" src="https://user-images.githubusercontent.com/86648892/212547194-7b900712-8877-4e48-a699-aa6439763405.png">

## READ

- detail 템플릿에서 각 게시글의 작성자 출력

<img width="1023" alt="dj_163" src="https://user-images.githubusercontent.com/86648892/212547192-01df4af7-fb52-4973-827b-88026c1c5e3b.png">

## DELETE

- 이제 댓글에는 작성자 정보가 함께 들어있기 때문에 현재 삭제를 요청하려는 사람과 댓글을 작성한 사람을 비교하여 본인의 댓글만 삭제할 수 있도록 함
- 추가로 해당 댓글의 작성자가 아니라면, 삭제 버튼을 출력하지 않도록 함

<img width="776" alt="dj_164" src="https://user-images.githubusercontent.com/86648892/212547191-323eab57-2704-46a4-a23c-6913167a69c2.png">

<img width="1038" alt="dj_165" src="https://user-images.githubusercontent.com/86648892/212547190-433cc569-cf5a-43d7-9e71-0d8a95c019ae.png">

---

## 인증된 사용자에 대한 접근 제한하기

- `is_authenticated`
- `View Decorators`

### 인증된 사용자인 경우만 댓글 작성 및 삭제하기

<img width="923" alt="dj_166" src="https://user-images.githubusercontent.com/86648892/212547189-abb6d252-8fac-4cee-a595-0535c1deecce.png">

<img width="847" alt="dj_167" src="https://user-images.githubusercontent.com/86648892/212547186-bfeeaba8-ce4a-419e-8a9f-6daa54e6a986.png">

### 비인증 사용자는 CommentForm을 볼 수 없도록 하기

<img width="1035" alt="dj_168" src="https://user-images.githubusercontent.com/86648892/212547185-f65b0425-d54d-4624-b1fb-59d395f87102.png">

---

## 정리

- 다대일 관계 (A many-to-one relationship)
  - Foreign Key
  - Django Relationship Fields
  - Related Manager
  - Referencing the User Model
- N : 1 모델 관계 설정
  - Comment - Article
  - Article - User
  - Comment - User
- 작성 과정
  - models에서 참조 키를 설정
  - forms에서 필드를 가리기
  - view 함수에서 동작을 처리
  - html에서 조건에 따라 출력 여부 설정

---

## 참고 [Django Coding Style Guide about Imports]

- import와 관련한 coding style guide
  - [https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/#imports](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/#imports)
  - isort 사용
    - **`$** python -m pip install "isort >= 5.1.0"`
    - **`$** isort .`
      - `$ isort accounts/views.py`
- 띄어쓰기, 좌우 공백
- camelCase말고 언더바 사용

---

# Django M:N Relationship

- Many to many relationship
- M:N (Article-User)
  - Like
- M:N (User-User)
  - Follow
- Fixtures

---

# Many-to-many relationship practice (patients-doctors)

### target and source model?

- target model
  - 관계 필드를 가지지 않은 모델
  - N:1에서는 1에 해당
- source model
  - 관계 필드를 가진 모델
  - N:1에서는 N에 해당

### `models.py`

```python
from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'

class Patient(models.Model):
    # doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)  # [1] 1명의 의사 - N명의 환자인 경우 (한계: 동일한 환자가 여러 의사에게 예약을 받는 경우를 구현하기 어려움)
    # [3] M:N 필드 (중개모델을 Django에서 알아서 생성해줌)
    doctors = models.ManyToManyField(Doctor, related_name='patients', through='Reservation')
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'

# [2] 중개모델 작성 (예약을 단위로 기록)
# class Reservation(models.Model):
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'

# [3-1] ManyToManyField의 extra data 작성 (through argument와 연결)
class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptom = models.TextField()
    reserved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'
```

### 정리

- M:N 관계로 맺어진 두 테이블에는 변화가 없음
- Django의 ManyToManyField는 중개 테이블을 자동으로 생성함
- Django의 ManyToManyField는 M:N 관계를 맺는 두 모델 어디에 위치해도 상관 없음
  - 대신 필드 작성 위치에 따라 참조와 역참조 방향을 주의할 것
- N:1은 완전한 종속의 관계였지만 M:N은 의사에게 진찰받는 환자, 환자를 진찰하는 의사의 2가지 형태로 모두 표현이 가능한 것

---

# `ManyToManyField(to, **options)`

## ManyToManyField란

- 다대다 관계 설정 시 사용하는 모델 필드
- 하나의 필수 위치인자가 필요
  - M:N 관계로 설정할 모델 클래스
- 모델 필드의 RelatedManager를 사용하여 관련 개체를 추가, 제거, 혹은 만들 수 있음
  - `add()` , `remove()` , `create()` , `clear()` …

## 데이터베이스에서의 표현

- Django는 다대다 관계를 나타내는 중개 테이블을 생성
- ManyToManyField는 중개 테이블에 별도 생성되는 것이며 기존 모델 테이블에 컬럼이 추가되지 않음
  - 중개 테이블 이름은 **_appname_ManyToManyField를 포함한 modelname_ManyToManyFieldname_**
    - ex) `articles_article_like_users`
    - `db_table` arguments를 사용하여 중개 테이블의 이름을 변경할 수도 있음
  - 중개 테이블의 컬럼 이름
    - source model과 target model이 다른 경우
      - id
      - **_<containing_model>\_id_**
        - 참조하는 모델 이름
      - **_<other_model>\_id_**
        - 역참조하는 모델 이름
    - 동일한 모델의 관계인 경우
      - id
      - **_from\_<model>\_id_**
      - **_to\_<model>\_id_**

## ManyToManyField Arguments

1. `related_name`
2. `through`
3. `symmetrical`

- blank=True
  - db의 유효성 검사와 관련없음 (값이 있어야함)
    - 사용자가 입력할 때 blank를 허용하는 것

### `related_name` argument

- target model이 source model을 참조할 때 사용할 manager name
- ForeignKey의 related_name과 동일

### `through` argument

- 중개 테이블을 수동으로 지정하려는 경우 `through` 옵션을 사용하여 사용하려는 중개 테이블을 나타내는 Django 모델을 지정할 수 있음
- 가장 일반적인 용도는 중개 테이블에 extra data를 추가하여 다대다 관계와 연결하려는 경우
- ManyToManyField를 조회할 때 해당 중개 테이블을 ‘통해서’ 조회를 하겠다는 뜻
- ManyToManyField에 자동으로 생성하는 것을 이제는 through 테이블로 대체하겠다는 뜻
- 예약을 주체로 예약을 생성하는 것도 가능하지만
  - 환자 혹은 의사를 주체로 관계를 추가하는 것이 더 합리적
- `add()` 시 `through_defaults={'key': 'value'}` argument 필요
  - `through_defaults` 값에 딕셔너리 타입으로 입력
  - ex) `patient2.doctors.add(doctor1, through_defaults={'symptom': 'flu'})`

### `symmetrical` argument

- 기본값은 True
- **_ManyToManyField가 동일한 모델(on self)을 가리키는 정의_**에서만 사용
- 재귀 참조 (self 참조)
  <img width="833" alt="dj_169" src="https://user-images.githubusercontent.com/86648892/212547774-196ab395-d15f-464b-b960-1a30529cb380.png">

- `symmetrical=True` 일 경우
  - \_set 매니저를 추가하지 않음
  - source 모델의 인스턴스가 target 모델의 인스턴스를 참조하면
    - 자동으로 target 모델 인스턴스도 source 모델 인스턴스를 참조하도록 함 (대칭)
      - 쉽게 말해 1-2의 관계가 추가된다면, 2-1의 관계도 추가됨
  - 대칭을 원하지 않는 경우 `False` 로 설정

## ManyToManyField Related Manager

- N:1 혹은 M:N 관계에서 사용 가능한 문맥(context)
- Django는 모델 간 N:1 혹은 M:N 관계가 설정되면 역참조 시에 사용할 수 있는 manager를 생성
  - 모델 생성 시 obejcts라는 매니저를 통해 queryset api를 사용했던 것처럼 related manager를 통해 queryset api 사용 가능
- N:1, M:N 관계에 따라 다르게 사용 및 동작됨
  - N:1
    - target 모델 객체만 사용 가능
  - M:N
    - 관련된 두 객체 모두 사용 가능
- 메서드 종류
  - `add()` , `remove()` , `create()` , `clear()` , `set()` …

## Methods (ManyToManyField)

### `add()`

- “지정된 객체를 관련 객체 집합에 추가”
- 이미 존재하는 관계에 사용하면 관계가 복제되지 않음
- 모델 인스턴스, 필드 값(PK)을 인자로 허용

### `remove()`

- “관련 객체 집합에서 지정된 모델 개체를 제거”
- 내부적으로 `QuerySet.delete()` 를 사용하여 관계가 삭제됨
- 모델 인스턴스, 필드 값(PK)을 인자로 허용

## 중개 테이블 필드 생성 규칙

<img width="962" alt="dj_170" src="https://user-images.githubusercontent.com/86648892/212547771-e43b0d22-2295-4120-afc2-2fee1e39623e.png">

---

# M:N (Article-User)

- Article과 User의 M:N 관계 설정을 통한 좋아요 기능 구현하기

## Like 기능 구현하기

### 모델 관계 설정

<img width="968" alt="dj_171" src="https://user-images.githubusercontent.com/86648892/212547769-a727db36-6b1a-4798-9eb6-89078f77aa32.png">

- `like_users` 필드 생성 시 자동으로 역참조에는 `.article_set` 매니저가 생성됨
- 그러나 이전 N:1 (Aritcle-User) 관계에서 이미 해당 매니저를 사용 중
  - `user.article_set.all()`
    - 해당 유저가 작성한 모든 게시글 조회
  - **_user가 작성한 글들(`user.article_set`)과 user가 좋아요를 누른 글(`user.article_set`)을 구분할 수 없게 됨_**
  - 이런 경우 user와 관계된 ForeignKey 혹은 ManyToManyField 중 하나에 `related_name` 을 작성해야 함

<img width="1022" alt="dj_172" src="https://user-images.githubusercontent.com/86648892/212547765-07fbe386-c6af-4cdb-bb0c-3257d092b1d8.png">

- 생성된 중개 테이블 확인

<img width="485" alt="dj_173" src="https://user-images.githubusercontent.com/86648892/212547761-5dcf4b86-f09a-4cfa-bfd5-94886cd7c232.png">

<img width="1000" alt="dj_174" src="https://user-images.githubusercontent.com/86648892/212547757-9fa18eb3-8299-436d-82c5-96f30988daf6.png">

### LIKE 구현

### url과 view 함수 설정

<img width="586" alt="dj_175" src="https://user-images.githubusercontent.com/86648892/212547755-78740740-e653-4bb4-9518-f4e233613d38.png">

<img width="590" alt="dj_176" src="https://user-images.githubusercontent.com/86648892/212547751-e2de49dd-ce83-4c3a-a12e-f7347a7fd8bc.png">

### `.exists()`

- QuerySet에 결과가 포함되어 있으면 True를 반환하고 그렇지 않으면 False를 반환
- 특히 큰 QuerySet에 있는 특정 개체의 존재와 관련된 검색에 유용

### index 템플릿에서 각 게시글에 좋아요 버튼 출력하기

<img width="810" alt="dj_177" src="https://user-images.githubusercontent.com/86648892/212547747-ec70756d-eb73-4ce1-b563-f299d8d9cbdf.png">

### 데코레이터 및 is_authenticated 추가

<img width="825" alt="dj_178" src="https://user-images.githubusercontent.com/86648892/212547743-6d270f89-6121-48c2-8358-92f30092ed1b.png">

---

# M:N (User-User)

- User 자기 자신과의 M:N 관계 설정을 통한 팔로우 기능 구현하기

## Profile 구현

- 자연스러운 follow 흐름을 위한 프로필 페이지를 먼저 작성

### url 및 view 함수 작성

- urlpatterns는 위에서부터 매칭한다
  - 만약 `path(’<str:username>/’, views.profile, name=’profile’),` 를 맨 위에 작성해버리면 그 아래에 있는 login, logout, signup 등 모든 문자열 시작 url들이 죽어버린다

<img width="895" alt="dj_179" src="https://user-images.githubusercontent.com/86648892/212547738-b4ed5f5d-525f-400e-a073-d81f2ac7deb6.png">

<img width="894" alt="dj_180" src="https://user-images.githubusercontent.com/86648892/212547736-853d38ea-5ce4-40ee-a771-782407629a39.png">

### profile 템플릿 작성

<img width="498" alt="dj_181" src="https://user-images.githubusercontent.com/86648892/212547731-c4abdd82-0efa-43de-b5b6-73b6a588e3bc.png">

<img width="553" alt="dj_182" src="https://user-images.githubusercontent.com/86648892/212547727-b3db06a2-a500-448e-9b71-cfa3eed85c31.png">

### profile 템플릿으로 이동할 수 있는 하이퍼링크 작성

<img width="1069" alt="dj_183" src="https://user-images.githubusercontent.com/86648892/212547722-d4e0b25b-6a59-40fc-a703-3f6241d41e61.png">

<img width="1065" alt="dj_184" src="https://user-images.githubusercontent.com/86648892/212547719-8524bedc-cb15-4f51-8c47-8fb9467add67.png">

---

## Follow 구현

### 모델 관계 설정

<img width="1092" alt="dj_185" src="https://user-images.githubusercontent.com/86648892/212547715-1457bffd-f9bf-4463-8f14-1082f398c070.png">

- 참조할 때 이름은 followings
  - followings 당하는 입장에서 역참조는 followers
- migration 진행
- 생성된 중개 테이블 확인
  <img width="574" alt="dj_186" src="https://user-images.githubusercontent.com/86648892/212547713-0728164b-2e05-4426-9a7d-9e87d65a02eb.png">

### url 및 view 함수 작성

<img width="897" alt="dj_187" src="https://user-images.githubusercontent.com/86648892/212547709-a8143bf5-526c-4991-ae33-2f3b5330f74d.png">

<img width="893" alt="dj_188" src="https://user-images.githubusercontent.com/86648892/212547704-186239f6-6034-497c-be86-040912fb44ec.png">

### 프로필 유저의 팔로잉, 팔로워 수 & 팔로워, 언팔로우 버튼 작성

<img width="931" alt="dj_189" src="https://user-images.githubusercontent.com/86648892/212547701-312080a9-efc5-4d96-9aef-774960b70c0f.png">

### 데코레이터 및 is_authenticated 추가

<img width="830" alt="dj_190" src="https://user-images.githubusercontent.com/86648892/212547697-71d002b3-cb8d-4f5f-8dec-64974165e521.png">

---

# Fixtures

- 프로젝트를 시작할 때 모델에 초기 데이터를 제공하는 방법

## 초기 데이터의 필요성

- 협업의 경우
  - gitignore 설정으로 인해 DB(venv, db.sqlite3)는 업로드하지 않음
    - requirements.txt로 설정 대체
  - Django에서는 fixtures를 사용해 앱에 초기 데이터(Initial data)를 제공할 수 있음
  - 즉, migrations와 fixtures를 사용하여 data와 구조를 공유하게 됨

## Providing data with fixtures

- Fixtures?
  - Django가 데이터베이스로 가져오는 방법을 알고 있는 데이터 모음
    - 가져오는 방법을 알고있다?
      - Django가 데이터들을 하나의 구조화된 파일로 만듬
        - 다른 프로젝트에서 같은 모델 구조로 일치한다면
          - 그대로 import하여 초기 데이터를 넣은 상태로 시작 가능

## fixtures 생성 및 로드

- `app_name/fixtures/` 가 기본 경로
  - Django는 설치된 모든 app의 디렉토리에서 fixtures 폴더 이후의 경로로 fixtures 파일을 찾음
- **_fixtures 파일은 직접 만드는 것이 아니라 dumpdata를 사용하여 생성하는 것이다_**
  - **_dumpdata의 출력 결과물은 loaddata의 입력으로 사용됨_**

### 생성 (데이터 추출)

- `dumpdata`

  - 응용 프로그램과 관련된 데이터베이스의 모든 데이터를 표준 출력으로 출력함
  - 여러 모델을 하나의 json 파일로 만들 수 있음
  - `python manage.py dumpdata [app_name[.ModelName] [app_name[.ModelName]] ...]] > {filename}.json`
    - `>` 앞에서 나온 문자열을 json 파일로 만들겠다는 것
  - `python manage.py dumpdata --indent 4 articles.article > articles.json`
    - articles 앱에 있는 article 모델 데이터를 articles.json으로 추출하겠다는 뜻
      - manage.py와 동일한 위치에 data가 담긴 articles.json 파일이 생성됨
    - `--indent 4` 는 옵션

  ```python
  # -Xutf8이라는 옵션을 통해 유니코드 형태로 인코딩 설정

  python -Xutf8 mange.py dumpdata --indent 4 articles.comment > comment.json
  ```

  - 추가로 나머지 모델에 대한 데이터를 dump
    - `python manage.py dumpdata --indent 4 articles.user > users.json`
    - `python manage.py dumpdata --indent 4 articles.comment > comments.json`

### [참고] 모든 모델을 한번에 dump하기

<img width="1047" alt="dj_191" src="https://user-images.githubusercontent.com/86648892/212547694-ea233db8-e783-444d-aa7f-5857b96502b7.png">

### 로드 (데이터 입력)

- `loaddata`
  - migrate 우선 진행
    - `python manage.py migrate`
  - 데이터 로드
    - `python manage.py loaddata articles/article.json`
    - `python manage.py loaddata articles.json comments.json users.json`
      - namespace 따로 설정안했다면 그냥 파일 이름 적어주면 됨
      - 띄어쓰기해서 한번에 로드 가능
  - 외래키에 의해 관계가 정해진 모델이 있다면 먼저 로드가 되어있어야 함
    - user - article - comment 순으로 로드하는 것이 좋음
    - 한번에 로드하는 경우는 순서를 알아서 매칭시켜줌
- dumpdata해서 만든 것을 약속된 기본 경로에 넣어줘야 load할 때 읽을 수 있음

### [참고] loaddata를 하는 순서

<img width="1182" alt="dj_192" src="https://user-images.githubusercontent.com/86648892/212547690-67bb0dfb-2924-42f5-a3d3-a4bbbc8a6cc4.png">

### [참고] loaddata 시 encoding codec 관련 에러가 발생하는 경우

<img width="1188" alt="dj_193" src="https://user-images.githubusercontent.com/86648892/212547681-dc067f4e-f0aa-4d03-b494-411e50f687c5.png">

---

# Improve Query

## Query를 개선하는 방법

- improve query의 목표는 Django가 DB를 hit하는 수를 줄이는 것
  - N:1 problem을 해결하는 것
    - N:1 problem?
      - 1번의 쿼리를 보냈는데 이 main query에 N번의 subquery가 붙는 것
        - 왜 이렇게 될까?
          - ORM의 lazy한 특성으로 인한 것
          - 데이터를 가져올 때는 DB를 실제로 히트하는 것이 아님
          - for문 등 실제로 필요할 때 DB를 히트함
- “DB에 main query를 보내는 시점에 아예 N번 히트해야할 데이터를 미리 한번에 가져오자”
  - 한 번에 가져온다?
    - SQL JOIN 연산
      - JOIN은 데이터베이스의 테이블을 어떻게 합칠까에 대한 연산
      - INNER JOIN, OUTER JOIN 등 여러 방식
        - INNER JOIN은 A와 B 테이블의 교집합이 되는 부분만 가져오는 것
  - 즉, “처음에 READ(조회)할 때 잘 들고오자”
    - `annotate`
    - `select_related`
    - `prefetch_related`

## annotate

- index-1 페이지 확인
  - DEBUG Toolbar의 SQL란을 통해 비슷한 쿼리가 발생하는 것을 확인
    - 각 게시글마다 똑같이 댓글의 개수를 세고 있음
      - 애초에 게시글을 가져올 때 댓글 개수까지 카운팅한 값을 한번에 가져오는 것으로 개선 가능
        - `views.py`
          - `articles = Article.objects.annotate(Count('comment')).order_by('-pk')`
        - `index_1.html`
          - `{{ article.comment__count }}`

## select_related

- 1:1 또는 N:1 참조 관계에서 쿼리 개선
- SQL에서 `INNER JOIN` 절을 활용
  - SQL의 `INNER JOIN` 을 사용하여 참조하는 테이블의 일부를 가져오고, `SELECT FROM` 을 통해 관련된 필드들을 가져옴
- 각 게시글마다 user를 참조하고 있음
  - `articles = Article.objects.select_related('user').order_by('-pk')`
    - 원래는 article 전체를 다 가져오는 것에서 그쳤는데
      - article을 가져오면서 article이 참조하고 있는 user id값도 처음 한번에 다 들고와서 중복적인 쿼리 요청을 1번으로 줄임

## prefetch_related

- M:N 또느 N:1 역참조 관계에서 쿼리 개선
- SQL이 아닌 Python을 통한 JOIN이 진행됨
- 각 게시글에서 댓글을 조회하는 쿼리를 10번 수행
  - `articles = Article.objects.prefetch_related(’comment_set’).order_by(’-pk’)`
    - SQL문을 확인해보면 `IN`을 사용하고 있음
      - 게시글 전체를 가져오면서 거기에 묶여있는 댓글 정보들도 한번에 다 들고옴

## index-4.html

- 중복 상황
  - 게시글 출력하면서 댓글 목록 출력
    - 댓글 출력하면서 각 댓글의 작성자를 출력
      - 100번의 쿼리
- 댓글 가져오면서, 유저를 한번에 붙이고
  - 게시글을 가져오면서, 댓글을 한번에 붙여서 가져옴
    - 2번의 쿼리로 개선

```python
articles = Articles.objects.prefetch_related(
    Prefetch('comment_set', queryset=Comment.objects.select_related('user'))
).order_by('-pk')
```

- SQL문의 `INNER JOIN`과 `IN`이 한번에 이루어짐

---

## Improve Query Codes

### views.py

```python
from django.shortcuts import render
from .models import Article, Comment
from django.db.models import Count

# Create your views here.
def index_1(request):
    # articles = Article.objects.order_by('-pk')
    articles = Article.objects.annotate(Count('comment')).order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index_1.html', context)

def index_2(request):
    # articles = Article.objects.order_by('-pk')
    articles = Article.objects.select_related('user').order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index_2.html', context)

def index_3(request):
    # articles = Article.objects.order_by('-pk')
    articles = Article.objects.prefetch_related('comment_set').order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index_3.html', context)

from django.db.models import Prefetch

def index_4(request):
    # articles = Article.objects.order_by('-pk')
    # articles = Article.objects.prefetch_related('comment_set').order_by('-pk')
    articles = Article.objects.prefetch_related(
        Prefetch('comment_set', queryset=Comment.objects.select_related('user'))
    ).order_by('-pk')

    context = {
        'articles': articles,
    }
    return render(request, 'articles/index_4.html', context)
```

### index_1.html

```html
{% extends 'base.html' %} {% block content %}
<h1>Articles</h1>
{% for article in articles %}
<p>제목 : {{ article.title }}</p>
{% comment %}
<p>댓글개수 : {{ article.comment_set.count }}</p>
{% endcomment %}
<p>댓글개수 : {{ article.comment__count }}</p>
<hr />
{% endfor %} {% endblock content %}
```

### index_2.html

```html
{% extends 'base.html' %} {% block content %}
<h1>Articles</h1>
{% for article in articles %}
<h3>작성자 : {{ article.user.username }}</h3>
<p>제목 : {{ article.title }}</p>
<hr />
{% endfor %} {% endblock content %}
```

### index_3.html

```html
{% extends 'base.html' %} {% block content %}
<h1>Articles</h1>
{% for article in articles %}
<p>제목 : {{ article.title }}</p>
<p>댓글 목록</p>
{% for comment in article.comment_set.all %}
<p>{{ comment.content }}</p>
{% endfor %}
<hr />
{% endfor %} {% endblock content %}
```

### index_4.html

```html
{% extends 'base.html' %} {% block content %}
<h1>Articles</h1>
{% for article in articles %}
<p>제목 : {{ article.title }}</p>
<p>댓글 목록</p>
{% for comment in article.comment_set.all %}
<p>{{ comment.user.username }} : {{ comment.content }}</p>
{% endfor %}
<hr />
{% endfor %} {% endblock content %}
```

## 섣부른 최적화를 하지 말자

- “작은 효율성(small efficiency)에 대해서는, 말하자면 97% 정도에 대해서는 잊어버려라. 섣부른 최적화(premature optimization)는 모든 악의 근원이다.”
  - 도널드 커누스(Donald E. Knuth)

---

# Django Static Files

- Managing static files
- Image Upload
- Image Resizing

---

# Managing static files

## Static files

### 정적 파일

- 응답할 때 별도의 처리없이 파일 내용을 그대로 보여주면 되는 파일
  - 사용자의 요청에 따라 내용이 바뀌는 것이 아니라 요청한 것을 그대로 보여주는 파일
- **_파일 자체가 고정_**되어있고, 서비스 중에도 추가되거나 **_변경되지않고 고정_**되어있음
  - ex) 웹 사이트는 일반적으로 이미지, JS, CSS와 같은 미리 준비된 추가 파일(움직이지 않는)을 제공해야함
- Django에서는 이러한 파일들을 “static file”이라함
  - Django는 `staticfiles` 앱을 통해 정적 파일과 관련된 기능을 제공

### Media File

- 미디어 파일
- 사용자가 웹에서 업로드하는 정적 파일 (user-uploaded)
- 유저가 업로드한 모든 정적 파일

### 웹 서버와 정적 파일

<img width="795" alt="dj_194" src="https://user-images.githubusercontent.com/86648892/212550666-31ef3168-0ec4-4878-9ebb-1212b44d9ff5.png">

- 웹 서버의 기본동작은
  - 특정 위치(URL)에 있는 자원을 요청(HTTP request)받아서
    - 응답(HTTP response)을 처리하고 제공(serving)하는 것
- 즉, “자원과 자원에 접근 가능한 주소가 있다”
  - ex) 사진 파일은 자원이고, 해당 **_사진 파일을 얻기 위한 경로인 웹 주소(URL)_**가 존재함
- 웹 서버는 요청받은 URL로 서버에 존재하는 정적 자원(static resource)을 제공함

## Static files 구성하기

### Django에서 정적 파일을 구성하고 사용하기 위한 몇 가지 단계

1. `INSTALLED_APPS` 에 `django.contrib.staticfiles` 가 포함되어 있는지 확인
2. settings.py에서 `***STATIC_URL***` 을 정의하기
3. 앱의 static 폴더에 정적 파일을 위치하기
   - ex) `my_app/static/sample_img.jpg`
4. 템플릿에서 static 템플릿 태그를 사용하여 지정된 경로에 있는 정적 파일의 URL 만들기

<img width="713" alt="dj_195" src="https://user-images.githubusercontent.com/86648892/212550665-41fc9fe7-3fb6-4083-80dc-f6269df3a357.png">

### Django template tag for static

- `{% load %}`
  - load tag
  - 특정 라이브러리, 패키지에 등록된 모든 템플릿 태그와 필터를 로드
- `{% static '' %}`
  - static tag
  - `STATIC_ROOT` 에 저장된 정적 파일에 연결

### Static files 관련 Core settings

1. `STATIC_ROOT`
2. `STATICFILES_DIRS`
3. `STATIC_URL`

### `1. STATIC_ROOT`

- Default: None
- Django 프로젝트에서 사용하는 모든 정적 파일을 한 곳에 모아 넣는 경로
- `collectstatic`
  - 배포를 위해 정적 파일을 수집하는 디렉토리의 절대 경로
  - admin 폴더에는 기본적으로 생성되는 admin 페이지 관련 내장 정적 파일들이 들어있음
- **_개발 과정에서 settings.py의 DEBUG 값이 True로 설정되어 있으면 해당 값은 작용되지 않음_**
- 실 서비스 환경(배포 환경)에서 Django의 모든 정적 파일을 다른 웹 서버가 직접 제공하기위해 사용
- 배포 환경에서는 Django를 직접 실행하는 것이 아니라
  - 다른 서버에 의해 실행되기 때문에
    - 실행하는 다른 서버는 Django에 내장되어 있는 정적 파일들을 인식하지 못함
      - 이것이 내장되어 있는 정적 파일들을 밖으로 꺼내는 이유

### [참고] collectstatic

<img width="1509" alt="dj_196" src="https://user-images.githubusercontent.com/86648892/212550663-536860d0-112f-4ae8-bd5c-cf478ef2e90a.png">

### [참고] 소프트웨어 배포(Deploy)

- 프로그램 및 어플리케이션을 서버와 같은 기기에 설치하여 서비스를 제공하는 것
- 클라우드 컴퓨팅 서비스(AWS, Google Cloud, MS Azure 등)에 프로그램 및 어플리케이션을 설치해 제공하는 것

<img width="605" alt="dj_197" src="https://user-images.githubusercontent.com/86648892/212550660-e73e86c1-f219-4ef3-b156-43398b82b525.png">

### `2. STATICFILES_DIRS`

- Default: [] (Empty List)
- `app/static/` 디렉토리 경로를 사용하는 것(기본 경로) 외에 추가적인 정적 파일 경로 목록을 정의하는 리스트
- 추가 파일 디렉토리에 대한 전체 경로를 포함하는 문자열 목록으로 작성되어야 함

<img width="474" alt="dj_198" src="https://user-images.githubusercontent.com/86648892/212550659-f2b42f85-4e79-45a8-8a5e-50311b38e521.png">

### `3. STATIC_URL`

- Default: None
- `STATIC_ROOT` 에 있는 정적 파일을 참조할 때 사용할 URL
- 개발 단계에서는 실제 정적 파일들이 저장되어 있는 `app/static/` 경로(기본 경로) 및 `STATICFILES_DIRS` 에 정의된 추가 경로들을 탐색
- 실제 파일이나 디렉토리가 아니며, URL로만 존재
- 비어있지 않은 값으로 설정한다면 반드시 slash(`/`)로 끝나야 함

<img width="412" alt="dj_199" src="https://user-images.githubusercontent.com/86648892/212550657-d11bea73-fd17-4b28-9fc1-5ee00f490d0a.png">

---

## Static files 가져오기

### 1. 기본 경로에 있는 static file 가져오기

- `articles/static/articles` 경로에 이미지 파일 배치

<img width="275" alt="dj_200" src="https://user-images.githubusercontent.com/86648892/212550656-13a6f064-2159-492f-884f-8d53eb567e6d.png">

- static tag를 사용해 이미지 파일 출력 및 확인

<img width="692" alt="dj_201" src="https://user-images.githubusercontent.com/86648892/212550655-2b3707c1-6fac-4f7d-a147-4e86892d04fd.png">

<img width="445" alt="dj_202" src="https://user-images.githubusercontent.com/86648892/212550653-ffb1656a-0a0c-4f4c-ba98-debf45dd945f.png">

### 2. 추가 경로에 있는 static file 가져오기

- **_추가 경로 작성_**

<img width="716" alt="dj_203" src="https://user-images.githubusercontent.com/86648892/212550651-be461fa8-7af6-40d6-bc1b-02c463943ef3.png">

- `static/` 경로에 이미지 파일 배치

<img width="288" alt="dj_204" src="https://user-images.githubusercontent.com/86648892/212550649-d9abe969-c6a4-45da-baf3-34e375326028.png">

- statig tag를 사용해 이미지 파일 출력 및 확인

<img width="757" alt="dj_205" src="https://user-images.githubusercontent.com/86648892/212550647-1db5d487-1ceb-4dfc-8cf4-6faf4d238969.png">

<img width="438" alt="dj_206" src="https://user-images.githubusercontent.com/86648892/212550646-d0b2a1f2-71af-47b7-ab87-9750708fd236.png">

### `STATIC_URL` 확인하기

- `http://127.0.0.1:8000/static/articles/sample_img_1.png`
  - Django가 해당 이미지를 클라이언트에게 응답하기 위해 만든 image url
    - 개발자 도구 이미지 Current Source 확인
      - img src의 경로에서 서버 내부적으로 인식하는 경로를 확인할 수 있음
    - Network 탭에서 Request URL 확인
      - 클라이언트에게 이미지를 응답하기 위한 요청 URL을 만든 것
  - **_“STATIC_URL + static file 경로”_**로 설정됨
    - `/static/` 이 STATIC_URL에서 정의한 부분
    - 클라이언트는 이 URL로 요청을 해야 해당 이미지를 볼 수 있음

<img width="707" alt="dj_207" src="https://user-images.githubusercontent.com/86648892/212550641-c7ec6f29-f0eb-4eec-80a5-161f8983e4d9.png">

- 정리하자면 서버에 올라가있는 static file 자원을 제공하려면 제공을 할 URL, 자원의 위치가 필요
  - 그 경로를 담당하는 것이 `STATIC_URL`
    - 그리고 이 주소를 static 태그를 통해 만들어낼 수 있다

---

# Image Upload

- Django ImageField를 사용하여 사용자가 업로드한 정적 파일(미디어 파일) 관리하기

## `ImageField()`

- 이미지 업로드에 사용하는 모델 필드
- FileField를 상속받는 서브클래스로서 FileField의 모든 속성 및 메서드를 사용 가능함과 더불어
  - 사용자에 의해 업로드된 파일이 유효한 이미지인지 검사
- ImageField의 인스턴스는 DB에 이미지 덩어리로서 들어가지 않는다
  - 최대 길이가 100자인 **_문자열로 DB에 생성_**되며
    - **_업로드된 파일의 경로가 저장_**됨
    - max_length 인자를 사용하여 최대 길이를 변경할 수 있음

## `FileField()`

- `FileField(upload_to='', storage=None, max_length=100, **options)`
- 파일 업로드에 사용하는 모델 필드
- 2개의 선택 인자
  1. `upload_to`
  2. `storage`

## FileField와 ImageField를 사용하기 위한 단계

1. settings.py에 `MEDIA_ROOT` , `MEDIA_URL` 설정
2. `upload_to` 속성을 정의하여 업로드된 파일에 사용할 `MEDIA_ROOT` 의 하위 경로를 지정 (선택사항)
   - `upload_to`
     - 어떤 경로에 이 파일을 업로드할 것인지 문자열로 작성
     - `MEDIA_ROOT/path`
       - MEDIA_ROOT 이후의 경로(path)를 지정

## `MEDIA_ROOT`

- Default: ‘’ (Empty String)
- 사용자가 업로드한 파일(미디어 파일)들을 보관할 디렉토리의 절대경로
  - 즉, 사용자가 파일을 업로드했을 때 **_실제 파일을 어디에 둘 것인지_** 정의
- Django는 성능을 위해 업로드 파일은 데이터베이스에 저장하지 않음
  - 데이터베이스에 저장되는 것은 “파일 경로”
- MEDIA_ROOT는 STATIC_ROOT와 반드시 다른 경로로 지정해야함

<img width="385" alt="dj_208" src="https://user-images.githubusercontent.com/86648892/212550640-6c24274c-8225-4898-aac7-d73e7112cfd0.png">

## `MEDIA_URL`

- Default: ‘’ (Empty String)
- **_MEDIA_ROOT에서 제공되는 미디어 파일을 처리하는 URL_**
- 업로드된 파일의 주소(URL)를 만들어주는 역할
  - 웹 서버 사용자가 사용하는 public URL
- 비어있지 않은 값으로 설정한다면 반드시 slash(`/`)로 끝나야함
- MEDIA_URL은 STATIC_URL과 반드시 다른 경로로 지정해야함

<img width="392" alt="dj_209" src="https://user-images.githubusercontent.com/86648892/212550639-bd7c2d22-0461-4074-ac37-05d4a72e3007.png">

## 개발 단계에서 사용자가 업로드한 미디어 파일 제공하기

<img width="720" alt="dj_210" src="https://user-images.githubusercontent.com/86648892/212550634-8dc88134-5b1a-4eb6-841f-4780b9adaa50.png">

- 사용자로부터 업로드된 파일이 프로젝트에 업로드 되고나서, 실제로 사용자에게 제공하기 위해서는 업로드된 파일의 URL이 필요함
  - 업로드된 **_파일의 URL_** == `settings.MEDIA_URL`
  - 위 **_URL을 통해 참조하는 파일의 실제 위치_** == `settings.MEDIA_ROOT`

---

# CREATE

## ImageField 작성

<img width="879" alt="dj_211" src="https://user-images.githubusercontent.com/86648892/212550858-c6da5b00-d1a5-4ec0-bc64-057a970f3c43.png">

## blank

- Default: False
- True인 경우 필드를 비워둘 수 있음
  - 이럴 경우 DB에는 ‘’(빈 문자열)이 저장됨
- 유효성 검사에서 사용됨 (is_valid)
  - “Validation-related”
  - 필드에 `blank=True` 가 있으면 form 유효성 검사에서 빈 값을 입력할 수 있음

## null

- Default: False
- True인 경우 Django는 빈 값을 DB에 NULL로 저장함
  - “Database-related”

## null 관련 주의사항

- ImageField에는 왜 blank 옵션을 줄까?
  - **_“CharField, TextField와 같은 문자열 기반 필드에는 null 옵션 사용을 피해야함”_**
    - 문자열 기반 필드들은 빈 문자열을 통해 빈 값이라는 의미를 가짐
    - 문자열 필드가 아닌 다른 필드들은 NULL이라는 값을 통해 빈 값이라는 의미를 가짐
    - 문자열 기반 필드에서 `null=True` 로 설정 시 데이터 없음에 대한 표현이 “빈 문자열”과 “NULL” 2가지 모두 가능하게 됨
      - “데이터 없음”에 대한 표현에 2개의 가능한 값을 갖는 것은 좋지 않음
        - 데이터베이스의 일관성에 어긋남
    - Django는 문자열 기반 필드에서 NULL이 아닌 빈 문자열을 사용하는 것이 규칙

## Pillow 설치

- ImageField를 사용하려면 반드시 Pillow 라이브러리가 필요
  - Pillow 설치없이는 makemigrations 실행 불가

<img width="475" alt="dj_212" src="https://user-images.githubusercontent.com/86648892/212550857-53a864c4-98f4-47ec-bd20-6d502dc3df2d.png">

### [참고] Pillow

- 광범위한 파일 형식 지원, 효율적이고 강력한 이미지 처리 기능을 제공하는 라이브러리
- 이미지 처리 도구를 위한 견고한 기반을 제공

## ArticleForm의 enctype 속성 변경

- 기본적인 form 태그는 파일을 업로드할 수 없음
  - 파일 또는 이미지 업로드 시에는 form 태그에 enctype(encoding type) 속성을 바꿔줘야 파일까지 업로드 가능

<img width="753" alt="dj_213" src="https://user-images.githubusercontent.com/86648892/212550856-70ef479a-ec82-4adc-9821-602793e17c97.png">

### [참고] form 태그의 enctype(인코딩) 속성 값

1. `application/x-www-form-urlencoded`
   - 기본값
   - 모든 문자 인코딩
2. `multipart/form-data`
   - 파일 및 이미지 업로드 시에 반드시 사용
   - 전송되는 데이터의 형식을 지정
   - `<input type="file">` 을 사용할 경우 사용
3. `text/plain`

## `request.FILES`

- 파일 및 이미지는 request의 POST 속성값으로 넘어가지 않고 FILES 속성값에 담겨 넘어감
  - 문자열 데이터만 `request.POST` 에 담김
    - 파일은 `request.FILES` 라는 속성값에 별도로 담김

<img width="582" alt="dj_214" src="https://user-images.githubusercontent.com/86648892/212550854-7d7e544b-9178-4f5f-ad7e-7d96070eb687.png">

### [참고] `request.FILES` 가 두번째 위치 인자인 이유

- BasModelForm Class의 생성자 함수에 2번째 위치 인자로 정의

<img width="281" alt="dj_215" src="https://user-images.githubusercontent.com/86648892/212550852-15cb7c7f-3e07-45ce-a42c-23d2b448a957.png">

## 이미지 업로드 후 확인

<img width="846" alt="dj_216" src="https://user-images.githubusercontent.com/86648892/212550850-26b64681-1fc6-46f6-adc1-39227806cd92.png">

<img width="833" alt="dj_217" src="https://user-images.githubusercontent.com/86648892/212550849-f32ab5b1-bc8f-4984-bbf2-fe1dccfc3265.png">

- 이미지 업로드에 성공했다면 자동으로 MEDIA_ROOT 경로에서 정의한 media 디렉토리가 생성됨
  - 테이블에는 파일이 아닌 이미지 경로가 저장됨
  - 이미지를 첨부한 경우 MEDIA_ROOT 경로에 이미지가 업로드됨
  - 이미지를 첨부하지 않으면 `blank=True` 속성으로 인해 빈 문자열이 저장됨
- 서로 다른 사용자가 같은 이름으로 파일을 업로드한다면 Django는 파일 이름 끝에 임의의 난수 문자열을 붙여서 구분 및 저장함

---

# READ

## 업로드된 이미지 출력

- 업로드된 파일의 상대 URL은 Django가 제공하는 url 속성을 통해 얻을 수 있음

<img width="667" alt="dj_218" src="https://user-images.githubusercontent.com/86648892/212550847-c9e31954-228d-4352-9b97-8f8d5247be7b.png">

- `article.image.url`
  - 업로드 파일의 경로
- `article.image`
  - 업로드 파일의 파일 이름

### 출력 확인

<img width="744" alt="dj_219" src="https://user-images.githubusercontent.com/86648892/212550846-e3060818-93c8-4e79-8ba8-de94b565a1a9.png">

### MEDIA_URL 확인

<img width="700" alt="dj_220" src="https://user-images.githubusercontent.com/86648892/212550845-98a0edf3-9978-4f6a-a57e-28ab46c520be.png">

### 이미지를 업로드하지 않은 경우 detail 템플릿 출력 불가 문제 해결

- 이미지 데이터가 있는 경우에만 이미지를 출력하도록 처리

<img width="609" alt="dj_221" src="https://user-images.githubusercontent.com/86648892/212550843-9eb9e164-86d5-4108-81fe-fbf5e0f9315f.png">

---

# UPDATE

- 이미지는 바이너리 데이터이기 때문에 텍스트처럼 일부만 수정 불가
  - 그러므로 새로운 사진으로 대체하는 방식을 사용

<img width="1481" alt="dj_222" src="https://user-images.githubusercontent.com/86648892/212550842-0e84412a-8397-441a-8e24-88bc97f391bf.png">

<img width="1162" alt="dj_223" src="https://user-images.githubusercontent.com/86648892/212550841-dbb65130-3e23-4245-8f38-80e57b9cca6b.png">

---

# upload_to argument

### `upload_to` argument를 활용하여 MEDIA_ROOT 이후 추가 경로 작성 가능

- ImageField는 업로드 디렉토리와 파일 이름을 2가지 방법을 통해 설정 가능
  1. 문자열 값 및 경로 지정 방법
  2. 함수 호출 방법

### 문자열 값 및 경로 지정 방법

<img width="768" alt="dj_224" src="https://user-images.githubusercontent.com/86648892/212550837-853ec6a5-9ead-408e-bed0-eba2eb65341e.png">

<img width="746" alt="dj_225" src="https://user-images.githubusercontent.com/86648892/212550836-7e29c8da-14f9-4193-a63a-3faf06edf1d3.png">

<img width="776" alt="dj_226" src="https://user-images.githubusercontent.com/86648892/212550835-7ddb9f6e-602d-4647-a0d0-70233f852311.png">

<img width="713" alt="dj_227" src="https://user-images.githubusercontent.com/86648892/212550833-947e1ede-7194-473f-a4eb-3645cca181bc.png">

- `upload_to` 에 작성하는 문자열을 MEDIA_ROOT 이후 추가 경로로 설정
- 단순 문자열 뿐만 아니라 파이썬 time 모듈의 `strftime()` 형식도 포함될 수 있으며
  - 이는 파일 업로드 날짜 및 시간으로 대체됨
- 변경 후 migration 과정 진행 필요

### 함수 호출 방법

<img width="776" alt="dj_228" src="https://user-images.githubusercontent.com/86648892/212550831-9bf5e146-69bc-4e47-a0df-642c458d50ce.png">

<img width="654" alt="dj_229" src="https://user-images.githubusercontent.com/86648892/212550830-2326d3b0-2700-44eb-870f-b1ae18838400.png">

- `upload_to` 는 독특하게 함수처럼 호출이 가능하며
  - 해당 함수가 호출되면서 반드시 2개의 인자를 받음
    1. `instance`
       - FileField가 정의된 모델의 인스턴스
       - 대부분 이 객체는 아직 데이터베이스에 저장되기 전이므로 아직 PK 값이 없을 수 있으니 주의
    2. `filename`
       - 기존 파일 이름
- 변경 후 migration 과정 진행 필요
- 상단의 결과는 username이 test인 회원이 업로드한 결과

---

# Image Resizing

- 실제 원본 이미지를 서버에 그대로 로드하는 것은 부담이 큼
- HTML <img> 태그에서 직접 사이즈를 조정할 수도 있지만
  - 업로드 될 때 이미지 자체를 resizing하는 방법을 사용해볼 것

### django-imagekit 모듈 설치 및 등록

<img width="522" alt="dj_230" src="https://user-images.githubusercontent.com/86648892/212550829-9d805075-7830-44e9-885b-31ce189cf06e.png">

- django-imagekit
  - 이미지 처리를 위한 Django 앱
    - 썸네일, 해상도, 사이즈, 색깔 등을 조정할 수 있음

## 썸네일 만들기

- 2가지 방식으로 썸네일 만들기 진행
  1. 원본 이미지 저장 x
     - `ProcessedImageField()`
  2. 원본 이미지 저장 o
     - `ImageField()` 와 `ImageSpecField()`

### `ProcessedImageField()` (원본 이미지 저장 x)

- 원본 이미지를 저장하지 않는 방식
- `ProcessedImageField()` 의 parameter로 작성된 값들은 makemigrations 후에 변경이 되더라도 다시 makemigrations 해줄 필요없이 즉시 반영됨
- processors에 작성하는 여러 클래스는 해당 라이브러리 문서를 별도로 확인
  - [https://github.com/matthewwithanm/pilki](https://github.com/matthewwithanm/pilkit)

<img width="648" alt="dj_231" src="https://user-images.githubusercontent.com/86648892/212550828-434661a8-0cd7-4147-b556-e917dcbd5cf8.png">

<img width="741" alt="dj_232" src="https://user-images.githubusercontent.com/86648892/212550826-99487a5b-4ecb-4d08-a1cc-4b6393341380.png">

<img width="712" alt="dj_233" src="https://user-images.githubusercontent.com/86648892/212550824-01db136e-bf17-4e3b-9400-8b290eded2b5.png">

### `ImageField()` 와 `ImageSpecField()` (원본 이미지 저장 o)

<img width="758" alt="dj_234" src="https://user-images.githubusercontent.com/86648892/212550821-bd051fff-6b0e-44ad-a9e5-9fde87d8c0c0.png">

<img width="781" alt="dj_235" src="https://user-images.githubusercontent.com/86648892/212550818-cae79a66-c3af-4532-972d-47d0a56c9e2d.png">

<img width="867" alt="dj_236" src="https://user-images.githubusercontent.com/86648892/212550817-9dbecc54-bb44-412b-832d-6bd2fc5257c0.png">

<img width="845" alt="dj_237" src="https://user-images.githubusercontent.com/86648892/212550816-3d638d8a-1799-4cfd-8058-ccb53e8a814e.png">

<img width="801" alt="dj_238" src="https://user-images.githubusercontent.com/86648892/212550814-b9e91c26-81ff-4fbd-9f4f-b176ec7783ae.png">

- `ImageSpecField()`
  - 테이블에 생성되는 물리적인 column은 아니다
    - 출력을 할 때 CACHE에 생성해준다
      - CACHE?
        - 브라우저가 이미지를 memory cache에 들고있다가 사용
        - 이미 받았던 것은 서버로부터 받지 않고 캐시에서 사용
          - 시간이 빠름

## model 필드 예제 코드

```python
# models.py

from django.db import models
from django.conf import settings
from imagekit.processors import Thumbnail
from imagekit.models import ProcessedImageField, ImageSpecField

def articles_image_path(instance, filename):
    return f'images/{instance.user.username}/{filename}'

# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    content = models.TextField()
    image = models.ImageField(blank=True)
    # image = models.ImageField(blank=True, upload_to='images/')
    # image = models.ImageField(blank=True, upload_to='%Y/%m/%d/')
    # image = models.ImageField(blank=True, upload_to=articles_image_path)

    # 원본 저장하지 않는 방식 (Processed ImageField)
    # image = ProcessedImageField(
    #     blank=True,
    #     upload_to='thumbnails/',
    #     processors=[Thumbnail(200,300)],
    #     format='JPEG',
    #     options={'quality': 80},
    # )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 원본 저장하는 방식 (source image 필요)
    image_thumbnail=ImageSpecField(
        source='image',
        processors=[Thumbnail(200,300)],
        format='JPEG',
        options={'quality': 80},
    )

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
```

---

# Django REST Framework and Serializer

- REST API
- Response JSON
- Django REST framework - Single Model
- Django REST framework - N:1 Relation

---

# HTTP

- HyperText Transfer Protocol
- HTML 문서와 같은 리소스(resource, 자원)들을 가져올 수 있도록 하는 프로토콜(규칙, 약속)
- 웹 상에서 컨텐츠를 전송하기 위한 약속
- 웹에서 이루어지는 모든 데이터 교환의 기초가 됨
- “클라이언트-서버 프로토콜”이라고도 부름
- 클라이언트와 서버는 다음과 같은 개별적인 메세지 교환에 의해 통신
  - 요청(request)
    - 클라이언트에 의해 전송되는 메세지
    - 행위를 정의
  - 응답(response)
    - 서버에서 응답으로 전송되는 메세지
    - 상태를 정의
- 실제로는 브라우저와 요청을 처리하는 서버 사이에는 더 많은 기술 및 컴퓨터들이 존재
  - 현재는 HTTP의 기본 명세에 대해 집중

## HTTP 특징

### Stateless (무상태)

- 동일한 연결(connection)에서 연속적으로 수행되는 두 요청 사이에 링크가 없음
  - 즉, 응답을 마치고 연결을 끊는 순간 클라이언트와 서버 간 통신이 끝나며
    - 상태 정보가 유지되지 않음
- 이는 특정 페이지와 일관되게 상호작용하려는 사용자에게 문제가 될 수 있으며
  - 이를 해결하기 위해
    - 쿠키와 세션을 사용해
      - 서버 상태를 요청과 연결함

## HTTP Request Methods

- 리소스에 대한 행위(수행하고자 하는 동작)를 정의
  - 즉, 리소스에 대해 수행할 원하는 작업을 나타내는 메서드 모음을 정의
- HTTP verbs라고도 칭함
- HTTP Request Methods
  1. **GET (R)**
     - 서버에 리소스의 표현을 요청
     - GET을 사용하는 요청은 데이터만 검색해야함
  2. **POST (C)**
     - 데이터를 지정된 리소스에 제출(submit)
     - 서버의 상태를 변경
  3. **PUT (U)**
     - 요청한 주소의 리소스를 수정
  4. **DELETE (D)**
     - 지정된 리소스를 삭제

### [참고] 리소스 (resource)

- **리소스(resource)**
  - HTTP 요청의 대상을 리소스(resource, 자원)라고 함

## HTTP response status codes

- 특정 HTTP 요청이 성공적으로 완료되었는지 여부를 나타냄
- 응답은 5개의 그룹으로 구분
  1. Informational responses (100-199)
  2. Successful responses (200-299)
  3. Redirection messages (300-399)
  4. Client error responses (400-499)
  5. Server error response (500-599)

---

# Identifying resources on the Web

### 웹에서의 리소스 식별

- HTTP 요청의 대상을 리소스(resource)라고 함
  - 리소스는 문서, 사진 또는 기타 어떤 것이든 될 수 있음
    - 각 리소스는 식별을 위해 **_URI_**로 식별됨
- 자원의 식별자 (URI)
  - 자원의 **_위치_**로 자원을 식별 (URL)
  - 고유한 **_이름_**으로 자원을 식별 (URN)

## URI

- Uniform Resource Identifier
  - 통합 자원 식별자
- 인터넷에서 하나의 리소스를 가리키는 문자열
- **_URL_**
  - 가장 일반적인 URL는 웹 주소로 알려진 URL

![dj_239](https://user-images.githubusercontent.com/86648892/212551498-8af5bd3b-3dfb-41ef-9974-bd813e368851.png)

- **_URN_**
  - 특정 이름공간에서 이름으로 리소스를 식별하는 URI는 URN

![dj_240](https://user-images.githubusercontent.com/86648892/212551497-404f8f1b-7c57-4a42-b785-bd06a0b3e02d.png)

## URL

- Uniform Resource Locator
  - 통합 자원 위치
- 웹에서 주어진 리소스의 주소
- 네트워크 상에 리소스가 어디 있는지(주소)를 알려주기 위한 약속
  - 이러한 리소는 HTML, CSS, 이미지 등이 될 수 있음

![dj_241](https://user-images.githubusercontent.com/86648892/212551494-ac1d0105-dabe-40cc-9581-f78b47367b2b.png)

### URL 구조

- **_Scheme (or protocol)_**
  - 브라우저가 리소스를 요청하는데 사용해야 하는 프로토콜
  - URL의 첫 부분은 브라우저가 어떤 규약을 사용하는지를 나타냄
  - 기본적으로 웹은 HTTP(S)를 요구하며 메일을 열기 위한 `mailto:`, 파일을 전송하기 위한 `ftp:` 등 다른 프로토콜도 존재
    ![dj_242](https://user-images.githubusercontent.com/86648892/212551493-cdf340f3-792b-454f-9e9a-ea7816674425.png)
- **_Authority_**
  - Scheme 다음으로 문자 패턴 `://` 으로 구분된 Authority(권한)이 작성됨
  - Authority는 domain과 port를 모두 포함하며 둘은 `:` (colon)으로 구분됨
    ![dj_243](https://user-images.githubusercontent.com/86648892/212551492-66fde450-cb27-4bed-ab37-50662b72c61d.png)
  - **_Domain Name_**
    - `www.example.com`
    - 요청 중인 웹 서버를 나타냄
    - 어떤 웹 서버가 요구되는지를 가리키며 직접 IP 주소를 사용하는 것도 가능
      - ex) 도메인 google.com의 IP 주소는 142.251.42.142
  - **_Port_**
    - `80`
    - 웹 서버의 리소스에 접근하는데 사용되는 기술적인 문 (Gate)
    - HTTP 프로토콜의 표준 포트는 다음과 같고 생략 가능 (나머지는 생략 불가)
      - HTTP
        - 80
      - HTTPS
        - 443
    - Django의 경우 8000(80+00)이 기본 포트로 설정되어 있음
- **_Path_**
  - 웹 서버의 리소스 경로
  - 초기에는 실제 파일이 위치한 물리적 위치를 나타냈지만
    - 오늘날은 실제 위치가 아닌 추상화된 형태의 구조를 표현 - ex) `/articles/create/` 가 실제 articles 폴더 안의 create 폴더 안을 나타내는 것은 아님
      ![dj_244](https://user-images.githubusercontent.com/86648892/212551491-cd332a29-034e-4be4-9898-70061fab280d.png)
- **_Parameters_**
  - 웹 서버에 제공하는 추가적인 데이터
  - `&` 기호로 구분되는 key-value 쌍 목록
  - 서버는 리소스를 응답하기 전에 이러한 파라미터를 사용하여 추가 작업을 수행할 수 있음
    ![dj_245](https://user-images.githubusercontent.com/86648892/212551490-af5a135c-d465-4450-95ae-ee3e78d3bae9.png)
- **_Anchor_**
  - 리소스의 다른 부분에 대한 앵커
    - 하이퍼링크와 비슷한 기능을 하는 인터넷 상의 다른 문서와 연결된 문자 혹은 그림
  - 리소스 내부 일종의 “북마크”를 나타내며 브라우저의 해당 북마크 지점에 있는 컨텐츠를 표시
    - ex) HTML 문서에서 브라우저는 앵커가 정의한 지점으로 스크롤함
  - fragment identifier(부분 식별자)라 부르는 `#` 이후 부분은 서버에 전송되지 않음
    - ex) `https://docs.djangoproject.com/en/3.2/intro/install/#quick-install-guide` 요청에서 `#quick-install-guide` 는 서버에 전달되지 않고 브라우저에게 해당 지점으로 이동할 수 있도록 함
      ![dj_246](https://user-images.githubusercontent.com/86648892/212551487-804cc47a-8b3b-4fac-b89d-41b19b376be1.png)

### [참고] URN

- Uniform Resource Name
  - 통합 자원 이름
- URL과 달리 자원의 위치에 영항을 받지 않는 유일한 이름 역할을 함 (독립적 이름)
- URL의 단점을 극복하기 위해 등장
  - 자원이 어디에 위치한지 여부와 관계없이 이름만으로 자원을 식별
- 그러나 이름만으로 실제 리소스를 찾는 방법은 보편화되어있지 않아 현재는 URL을 대부분 사용
- 예시
  - ISBN
    - 국제표준 도서번호
      - 국제적으로 책에 붙이는 고유 식별자
  - ISAN
    - 국제표준 시청각 자료번호
      - 도서의 ISBN과 유사항 시청각 작품 및 관련 버전의 고유 식별자

---

# REST API

## API

- Application Programming Interface
- 어플리케이션과 프로그래밍으로 소통하는 방법
  - 개발자가 복잡한 기능을 보다 쉽게 만들 수 있도록 프로그래밍 언어로 제공되는 구성
- API를 제공하는 어플리케이션과 다른 소프트웨어 및 하드웨어 등의 것들 사이의 간단한 계약(인터페이스)이라고 볼 수 있음
- API는 복잡한 코드를 추상화하여 대신 사용할 수 있는 더 쉬운 구문을 제공
  - 일상생활에 비유하자면 우리는 가전 제품의 플러그를 소켓에 꽂기만 하면 되고
    - 우리는 가전 제품에 전기를 공금하기 위해 직접 배선을 하지 않는다!

## Web API

- 웹 서버 또는 웹 브라우저를 위한 API
- 현재 웹 개발은 모든 것을 하나부터 열까지 직접 개발하기보다 여러 Open API를 활용하는 추세
  - Open API?
    - 개발자라면 누구나 사용할 수 있도록 공개된 API
    - 개발자에게 사유 응용 소프트웨어나 웹 서비스의 프로그래밍적 권한을 제공
- 대표적인 Third Party Open API 서비스 목록
  - Youtube API
  - Naver Papago API
  - Kakao Map API
- API는 다양한 타입의 데이터를 응답
  - HTML
  - XML
  - JSON
  - etc
  - 현대 API는 대부분 JSON 타입의 데이터를 응답

## REST

- Representational State Transfer
- API Server를 개발하기 위한 일종의 소프트웨어 설계 방법론
  - 2000년 로이 필딩의 박사학위 논문에서 처음으로 소개된 후 네트워킹 문화에 널리 퍼짐
- “A group of software architecture design constraints”
  - 소프트웨어 아키텍쳐 디자인 제약 모음
- REST 원리는 따르는 시스템을 **_RESTful_**하다고 부름
- REST의 기본적은 근간은 리소스(자원)
  - 자원을 정의하고 자원에 대한 주소를 지정하는 전반적인 방법을 서술
  - **_자원을 어떻게 할 것인가_**
    - **_자원을 어떻게 정의할 것_**인가
      - 어떤 식으로 설계하고 표현할 것인가
    - **_주소를 어떤 식으로 지정할 것_**인가

### REST에서 자원을 정의하고 주소를 지정하는 방법

1. 자원의 **_식별_**
   - **_URI_**
     - URI로 자원을 식별한다
2. 자원의 **_행위_**
   - **_HTTP Method_**
     - GET, POST, PUT, DELETE
       - 이 메소드들로 자원의 행위를 결정한다
3. 자원의 **_표현_**
   - 자원과 행위를 통해 궁극적으로 표현되는 (추상화된) **_결과물_**
   - JSON으로 표현된 데이터를 제공
     - JSON으로 자원을 표현한다

- **_즉, RESTful API란 자원을 URI로 식별하고, 자원의 행동을 HTTP Method로 결정하고, 해당 자원의 최종적인 표현을 JSON으로 표현하자는 방법론을 약속으로 지키는 API를 의미_**

## JSON

- JSON is a lightweight data-interchange format
- JavaScript의 표기법을 따른 **_단순 문자열_**
- 파이썬의 dictionary, 자바스크립트의 object처럼
  - C 계열의 언어가 갖고 있는 자료구조로 쉽게 변환할 수 있는
    - **_key-value 형태의 구조_**를 갖고 있음
- 사람이 읽고 쓰기 쉽고
  - 기계가 파싱(해석&분석)하고 만들어내기 쉽기 때문에
    - 현재 API에서 가장 많이 사용하는 데이터 타입
- JSON 파일 예시
  <img width="479" alt="dj_247" src="https://user-images.githubusercontent.com/86648892/212551486-da92c751-1257-4fe5-afdf-a823bd2044c7.png">

## REST 정리

- “자원을 정의하고 자원에 대한 주소를 지정하는 방법의 모음”

1. 자원의 식별
   - URL
2. 자원에 대한 행위
   - HTTP Methods
3. 자원을 표현
   - JSON

- 설계 방법론은 지키지 않았을 때 잃는 것보다 지켰을 때 얻는 것이 훨씬 많음
  - 단, 설계 방법론을 지키지 않더라도 동작 여부에 큰 영향을 미치지는 않음
  - 말 그대로 방법론일 뿐이며 규칙이나 규약은 아님
- **_RESTful한 서버를 만든다는 것은 결국 해당 데이터베이스에 대한 클라이언트의 요청과 관련하여_**
  - **_JSON으로 응답을 반환하고_**
    - **_해당 요청 자원은 URL로 식별 가능하며_**
      - **_그 과정에 있어서 HTTP Methods를 사용하는 서버를 뜻한다고 이해하자_**
- RESTful API는 결국
  1. **_행위는 method로_**
  2. **_자원은 path로_**
  - 다룬다는 2가지 규칙을 지키는 것을 의미한다

---

# Response JSON

- JSON 형태로의 서버 응답 변화
  - 페이지 반환이 아닌 JSON 데이터 반환
- 다양한 방법으로 JSON을 응답

### 서버가 응답하는 것

- 서버는 사용자에게 페이지(html)만 응답하는 것이 아니라
  - 다양한 데이터 타입을 응답할 수 있음
    - html을 응답하는 서버를 JSON 데이터를 응답하는 서버로 변환
      - 그렇다면 사용자에게 보여질 화면은 누가 구성?
        - Front-end Framework가 담당

<img width="853" alt="dj_248" src="https://user-images.githubusercontent.com/86648892/212551485-b0094561-b83f-499f-9f99-08eca9dd5a80.png">

<img width="843" alt="dj_249" src="https://user-images.githubusercontent.com/86648892/212551482-ba6add9f-95ab-435a-a0b1-f6ab8867e56d.png">

---

# Response

- 다양한 방법으로 JSON 데이터 응답해보기
  1. HTML 응답
  2. `JsonResponse()` 를 사용한 JSON 응답
  3. **_Django Serializer_**를 사용한 JSON 응답
  4. **_Django REST framework_**를 사용한 JSON 응답

## ‘Content-Type’ entity header

- 리소스의 media type(MIME type, content type)을 나타내기 위해 사용됨
- 응답 내에 있는 컨텐츠의 컨텐츠 유형이 실제로 무엇인지 클라이언트에게 알려줌

## Serialization이란?

- “직렬화”
- 데이터 구조나 객체 상태를 동일 혹은 다른 컴퓨터 환경에 저장하고
  - 나중에 재구성할 수 있는 포맷으로 변환하는 과정
    - 즉, 어떠한 언어나 환경에서도 나중에 쉽게 재구성할 수 있는 포맷인 serialized data로 변환하는 과정
      - serialized data란 가공된 데이터로
        - 다른 포맷으로 쉽게 재구성할 수 있는 파일이라는 특징
          - 변환 포맷은 대표적으로 json, xml, yaml이 있으면 json이 가장 보편적으로 쓰임
- Django의 `serialize()` 는 QuerySet 객체 및 Model Instance와 같은 복잡한 데이터를
  - JSON, XML 등의 유형으로 쉽게 변환할 수 있는 Python 데이터 타입으로 만들어줌

<img width="850" alt="dj_250" src="https://user-images.githubusercontent.com/86648892/212551481-fec1e18f-2cc6-4dce-ba28-3b9522727772.png">

<img width="832" alt="dj_251" src="https://user-images.githubusercontent.com/86648892/212551480-75ef0e69-dbac-4f62-8622-3c7ed077041e.png">

## 1. HTML 응답

```python
def article_html(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/article.html', context)
```

```html
<body>
  <h1>Article List</h1>
  <hr>
  <p>
    {% for article in articles %}
      <h2>{{ article.pk }}번 글. {{ article.title }}</h2>
      <p>{{ article.content }}</p>
      <hr>
    {% endfor %}
  </p>
</body>
```

<img width="634" alt="dj_252" src="https://user-images.githubusercontent.com/86648892/212551479-20330f29-bfd9-4587-9d87-e98e1aab0046.png">

## 2. JsonResponse()를 사용한 JSON 응답

- Django가 기본적으로 제공하는 JsonResponse 객체를 활용하여 Python 데이터 타입을 손쉽게 JSON으로 변환하여 응답 가능
- 컬럼을 일일이 정의하여 딕셔너리 생성
- `JsponResponse()`
  - JSON-encoded response를 만드는 클래스
  - `safe` parameter
    - 기본값은 True
    - `JsonResponse()` 에 들어오는 인자가 dictionary가 아니면 `safe=False` 로 설정해야함
      - False로 설정 시 모든 타입의 객체를 serialization 할 수 있음
        - 그렇지 않으면 dictionary 인스턴스만 허용
- 출력 확인을 위해 Chrome 확장 프로그램에 JSON Viewer 설치

```python
# 직접 JSON 응답 객체 작성 (JsonResponse())

from django.http.response import JsonResponse

def article_json_1(request):
    articles = Article.objects.all()
    articles_json = []
    # article 데이터 하나씩 딕셔너리 형태로 리스트에 넣음
    for article in articles:
        articles_json.append(
            {
                'id': article.pk,
                'title': article.title,
                'content': article.content,
                'created_at': article.created_at,
                'updated_at': article.updated_at,
            }
        )
    # 만든 딕셔너리 리스트를 JSON으로 변환
    return JsonResponse(articles_json, safe=False)
```

<img width="583" alt="dj_253" src="https://user-images.githubusercontent.com/86648892/212551477-5f824975-dfc4-477d-bad8-8487fc7a28d7.png">

## 3. Django Serializer를 사용한 JSON 응답

- Django 내장 `HttpResponse()` 를 활용한 JSON 응답
- 모델 구조를 기반으로 JSON 데이터를 생성
  - JSON의 모든 필드를 다 작성할 필요 없음

```python
# Django 내장 HttpResponse()와 serializers 활용

from django.http.response import HttpResponse

def article_json_2(request):
    articles = Article.objects.all()
    data = serializers.serialize('json', articles)
    return HttpResponse(data, content_type='application/json')
```

<img width="699" alt="dj_254" src="https://user-images.githubusercontent.com/86648892/212551476-83ac2af1-e096-4d53-910e-c8695ef500ac.png">

## 4. Django REST framework를 사용한 JSON 응답

### Django REST framework (DRF)

- Django에서 Restful API 서버를 쉽게 구축할 수 있도록 도와주는 오픈소스 라이브러리
- Web API 구축을 위한 강력한 toolkit을 제공
- REST framework를 작성하기 위한 여러 기능을 제공
- DRF의 serializer는 Django의 Form 및 ModelForm 클래스와 매우 유사하게 작동
  - DRF에서 일부러 구성을 맞춰둔 것
    - ModelForm과 동일한 일을 하는 것은 아님
      - `serialize()`를 담당
- [https://www.django-rest-framework.org/](https://www.django-rest-framework.org/)

```python
# settings.py

INSTALLED_APPS = [
    'articles',
    'rest_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

```python
# articles/serializers.py

from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'
```

```python
# articles/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response

# @api_view(['GET'])
@api_view()
def article_json_3(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)
```

<img width="583" alt="dj_255" src="https://user-images.githubusercontent.com/86648892/212551472-813a56ac-3f27-4fd9-b949-0ea82aa34513.png">

- DRF가 자체적으로 JSON 데이터를 담은 DRF 내장 템플릿을 반환
  - `Content-Type: text/html;`
  - 브라우저 상에서만 그런 것이고, 실제 코드에서 프로그래밍적으로 소통할 때는 JSON을 반환

### 직접 requests 라이브러리를 사용하여 JSON 응답 받아보기

- requests 라이브러리 설치
  - `pip install requests`
    - Terminal 화면을 나누어 Django 서버를 켜놓고 파일 실행

```python
# gogo.py

# 요청보낼 때 requests 라이브러리 사용
import requests
from pprint import pprint

response = requests.get('http://127.0.0.1:8000/api/v1/json-3/') # requests가 GET Method로 해당 url에 요청을 보냄
result = response.json()                                        # 응답받은 것을 JSON으로 변환

pprint(result)
# pprint(result[0])
# pprint(result[0].get('title'))
```

<img width="674" alt="dj_256" src="https://user-images.githubusercontent.com/86648892/212551470-938710ff-6204-4371-83eb-9fec1a05b9a0.png">

---

# Django REST framework (Single Model)

- 단일 모델의 data를 Serialization하여 JSON으로 변환하는 방법 학습
- DRF를 활용하여 JSON 데이터를 응답하는 Django 서버 구축

## ModelSerializer

- ModelSerializer 클래스는 모델 필드에 해당하는 필드가 있는 Serializer 클래스를 자동으로 만들 수 있는 shortcut을 제공
  1. Model 정보에 맞춰 자동으로 필드를 생성
  2. serializer에 대한 유효성 검사기를 자동으로 생성
     - 이름도 `is_valid()` 로 같음
     - serialize하기 전 유효성 검사
  3. `.create()` 및 `.update()` 의 간단한 기본 구현이 포함됨
     - 이후 수정이나 생성을 할 때 쓰는 메서드를 기본 구현에 포함하고 있음
- 쿼리셋이나 모델 인스턴스 객체를 넣어주기만 하면 알아서 그 필드에 맞춰서 JSON 데이터를 key-value에 맞춰 생성
- 최대한 Django의 ModelForm과 비슷하게 구현해놓음

### 단일 모델 인스턴스 serialize

- Model Instance 객체 serialize
  - `article = Article.objects.get(pk=1)`
  - `serializer = ArticleListSerializer(article)`
  - `serializer.data`

<img width="624" alt="dj_257" src="https://user-images.githubusercontent.com/86648892/212551468-1508ad08-db57-4cbb-ab78-269e98dec476.png">

### QuerySet 객체 serialize

- QuerySet 객체 serialize
  - 단일 객체 인스턴스 대신 QuerySet 또는 객체 목록을 serialize하려면
    - `many=True` 옵션이 필요함

<img width="774" alt="dj_258" src="https://user-images.githubusercontent.com/86648892/212551467-d3c58515-cc8f-4b8d-a8c2-e6e93c4b40ba.png">

<img width="773" alt="dj_259" src="https://user-images.githubusercontent.com/86648892/212551466-82f16d27-9d5e-45a7-b8f4-67f4f8caf366.png">

---

# Build RESTful API (Article and Comment)

<img width="838" alt="dj_260" src="https://user-images.githubusercontent.com/86648892/212551464-5618e163-34c3-407d-b032-96d68e00749f.png">

- URL은 2개이고, 기능은 7개인 서버를 구현
  - URL이 2개인데 기능이 7개가 가능한 이유는 똑같은 URL이지만 Http Methods로 행동을 정의할 수 있기에 가능

## `api_view` decorator

- DRF에서 `api_view` 데코레이터 작성은 필수
- DRF view 함수가 응답해야하는 HTTP 메서드 목록을 받음
- 기본적으로 GET 메서드만 허용되며 다른 메서드 요청에 대해서는
  - 405 Method Not Allowed로 응답

## raising an exception on invalid data

- serializer의 데이터에 대한 유효성 검사 실행 시 줄 수 있는 옵션
  - 유효하지 않은 데이터에 대해 예외 발생시키기
    - `is_valid()` 는 유효성 검사 오류가 있는 경우 ValidationError 예외를 발생시키는 선택적 `raise_exception` 인자를 사용할 수 있음
      - DRF에서 제공하는 기본 예외 처리기에 의해 자동으로 처리되며 기본적으로 HTTP 400 응답을 반환

## passing additional attributes to `.save()`

- `save()` 메서드는 특정 Serializer 인스턴스를 저장하는 과정에서 추가적인 데이터를 받을 수 있음
- 아래 사진은 `CommentSerializer` 를 통해 Serialize되는 과정에서 Parameter로 넘어온 `article_pk` 에 해당하는 article 객체를 추가적인 데이터를 넘겨 저장

<img width="677" alt="dj_261" src="https://user-images.githubusercontent.com/86648892/212551775-b623c2e4-81a9-4fcf-88a5-e9450185ee1f.png">

## `read_only_fields` 설정

- `read_only_fields` 를 사용해 외래키 필드를 읽기 전용 필드로 설정
- 읽기 전용 필드는 데이터를 전송하는 시점에
  - 해당 필드를 유효성 검사에서 제외시키고 데이터 조회 시에는 출력하도록 함

<img width="593" alt="dj_262" src="https://user-images.githubusercontent.com/86648892/212551774-480fe870-7d69-403a-ad31-0955826d466d.png">

---

# Code Snippets

### `articles/models.py`

```python
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

### `articles/serializers.py`

```python
from rest_framework import serializers  # DRF 패키지에서 serializers 기능을 차용
from .models import Article, Comment    # ModelSerializer에 사용할 모델 import

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',) # 최종적으로 조회는 되나, 유효성 검사에서 제외됨

# 게시글의 목록(게시글들의 QuerySet)을 serialize해서 나눌 것이기에 이름을 ArticleListSerializer로 명명
class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article                         # 해당 모델 정보에 맞춰 자동으로 필드 생성
        # 전체 게시글 목록에서는 생성일, 수정일은 빼고 보여주기
        fields = ('id', 'title', 'content',)    # 어떤 필드를 serialize할지 결정 (사용자에게 최종적으로 JSON에 보여질 것을 결정)

# 단일 게시글에 대한 상세 정보를 제공하는 serializer
# serialize하는 fields가 달라지면 다른 serializer를 만들어줘야함
class ArticleSerializer(serializers.ModelSerializer):
    # article 입장에서 comment는 N이기에 many=True 필요, 또한 유효성 검사에서 제외되어야 함
    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True) # 기존 역참조용 필드를 override
    comment_set = CommentSerializer(many=True, read_only=True)  # 역참조할 시 pk말고 CommentSerializer에서 출력하는 모든 정보 출력 가능
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)    # 새로운 필드 추가

    class Meta:
        model = Article
        fields = '__all__'
```

### `articles/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('articles/<int:article_pk>/comments/', views.comment_create),
]
```

### `articles/views.py`

```python
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import get_object_or_404, get_list_or_404

from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer

# @api_view()는 기본값이 GET만 허용
@api_view(['GET', 'POST'])
def article_list(request):
    # 전체 게시글 조회
    if request.method == 'GET':
        # articles = Article.objects.all()
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    # 게시글 작성
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)   # ArticleSerializer를 사용한 이유는 게시글이 생성됐을 때 전체 필드를 출력하는 JSON을 사용하고 싶어서 사용
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    # 단일 게시글 조회
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    # 단일 게시글 삭제
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # 단일 게시글 수정
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)  # ModelForm과 다르게 앞쪽에 인스턴스가 들어감
        # serializer = ArticleSerializer(instance=article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['GET'])
def comment_list(request):
    # 댓글 목록 조회
    if request.method == 'GET':
        # comments = Comment.objects.all()
        comments = get_list_or_404(Comment)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    # comment = Comment.objects.get(pk=comment_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    # 특정 댓글 조회
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    # 특정 댓글 삭제
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # 특정 댓글 수정
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

# 단일 댓글 데이터 생성
@api_view(['POST'])
def comment_create(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):   # 아래줄에서 article이 들어가기 전 유효성 검사 진행 (read_only_fields 설정 필요)
            serializer.save(article=article)        # 외래키 삽입 (ModelForm과 달리 commit=False를 사용하지 않음)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
```

## GET (List)

### 게시글 데이터 목록 조회하기

<img width="1491" alt="dj_263" src="https://user-images.githubusercontent.com/86648892/212551772-a2d86c82-2186-4340-af6b-3e07d9e87d79.png">

## GET - Detail

### 단일 게시글 데이터 조회하기

<img width="1496" alt="dj_264" src="https://user-images.githubusercontent.com/86648892/212551771-ef86a807-6c56-4845-bf1e-007f47679da0.png">

## POST

### 게시글 데이터 생성하기

<img width="1371" alt="dj_265" src="https://user-images.githubusercontent.com/86648892/212551770-ba13e92b-c337-4375-adc3-ccea7a3df854.png">

- 요청에 대한 데이터 생성이 성공했을 경우 201 Created 상태 코드를 응답하고 실패했을 경우는 400 Bad request를 응답
  - `from rest_framework import status`
    - `return Response(serializer.data, status=status.HTTP_201_CREATED`
    - `return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST`
      - `if serializer.is_valid(raise_exception=True):` 와 같이 raise exception option을 주면 더이상 400을 따로 설정하지 않아도 됨

## DELETE

### 게시글 데이터 삭제하기

<img width="1328" alt="dj_266" src="https://user-images.githubusercontent.com/86648892/212551768-293984e0-9b5e-4a0e-a6c7-a9242b6081c7.png">

- 요청에 대한 데이터 삭제가 성공했을 경우는 204 No Content 상태 코드 응답
  - API는 반드시 요청에 대한 결과를 정확한 상태 코드로 전달해야 한다
    - 그래야 소통이 가능하다

## PUT

### 게시글 데이터 수정하기

<img width="1322" alt="dj_267" src="https://user-images.githubusercontent.com/86648892/212551767-3cad5381-a10f-403d-8154-407ea8d40efe.png">

- 요청에 대한 데이터 수정이 성공했을 경우는 200 OK 상태 코드 응답

---

# Django REST framework (N:1 Relation)

- N:1 관계에서의 모델 data를 Serialization하여 JSON으로 변환하는 방법 학습
- Serializer의 필드를 정의하는 것은 모델을 바탕으로 한 JSON 데이터에 추가적으로 덧붙이고 싶은 정보가 있을 때 정의한다고 생각하자
  - 역참조를 하는 related manager의 이름으로 필드를 정의하면
    - serializer에 역참조하는 데이터들을 넣어주는 로직을 쓰지 않아도 알아서 인식하여 넣어주는 것 뿐
      - 예시
        - `comment_set = CommentSerializer(many=True, read_only=True)`
        - `comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)`

## GET (List)

### 댓글 데이터 목록 조회하기

<img width="1507" alt="dj_268" src="https://user-images.githubusercontent.com/86648892/212551766-cf212aa2-56c7-4983-bb27-9b101886a18e.png">

## GET (Detail)

### 단일 댓글 데이터 조회하기

<img width="1502" alt="dj_269" src="https://user-images.githubusercontent.com/86648892/212551765-4739720f-47c9-450f-8d90-5051d993dded.png">

### POST

### 단일 댓글 데이터 생성하기

<img width="1325" alt="dj_270" src="https://user-images.githubusercontent.com/86648892/212551763-dbba2a11-3285-4084-898f-ce2e66b3d52c.png">

- CommentSerializer에서 article field의 데이터는 사용자로부터 입력받는 것이 아니므로
  - CommentSerializer에서 article은 read only field로 설정

### DELETE & PUT

### 댓글 데이터 삭제 및 수정 구현하기

<img width="1254" alt="dj_271" src="https://user-images.githubusercontent.com/86648892/212551761-fae71e32-bb35-4851-b62c-7cdcbfe8b700.png">

<img width="1261" alt="dj_272" src="https://user-images.githubusercontent.com/86648892/212551760-812c213a-d12d-403b-8e72-e94389278b85.png">

---

# N:1 역참조 데이터 조회

1. 특정 게시글에 작성된 댓글 목록 출력하기
   - **_기존 필드 override_**
2. 특정 게시글에 작성된 댓글의 개수 출력하기
   - **_새로운 필드 추가_**

## 특정 게시글에 작성된 댓글 목록 출력하기

### 기존 필드 Override (역참조 덮어씌우기)

1. **_PrimaryKeyRelatedField()_**
   - `comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)`

<img width="1455" alt="dj_273" src="https://user-images.githubusercontent.com/86648892/212551759-a42410eb-4376-4f4e-af99-3b14a21e9b5b.png">

1. **_Nested Relationships_**
   - `comment_set = CommentSerializer(many=True, read_only=True)`
     - 역참조 시 pk말고 CommentSerializer에서 출력하는 모든 정보 출력 가능

<img width="1259" alt="dj_274" src="https://user-images.githubusercontent.com/86648892/212551756-1ac50631-3d57-4b27-8bbe-99cb5334cdda.png">

## 특정 게시글에 작성된 댓글의 개수 출력하기

### 새로운 필드 추가

- `comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)`
  - `source`
    - serializers field’s argument
    - 필드를 채우는데 사용할 속성의 이름
    - 점 표기법(dotted notation)을 사용하여 속성을 탐색할 수 있음
    - source에 ORM 명령어 작성
      - `article.comment_set.count()`
        - ArticleSerializer 안이므로 article 생략, 문자열 안이어서 끝 괄호 생략
  - comment_count와 같이 변수명은 정의하고싶은 것으로 정의
  - 숫자를 다룰 것이므로 `IntegerField()`
  - 유효성 검사를 통과해야하므로 `read_only`는 True

<img width="1352" alt="dj_275" src="https://user-images.githubusercontent.com/86648892/212551753-1aeae757-f7dc-4138-b159-9d66aeae495b.png">

### [주의] 읽기 전용 필드 지정 이슈

- 기존에 물리적으로 존재했던 필드는 `read_only_fields` 지정 가능
- override되거나 추가된 필드의 경우에는 `read_only_fields`에 추가할 수 없음
- `read_only_fields` 에 지정하는 것들은 DB→클라이언트로 조회만 가능하고, 클라인어트→DB로 조작은 불가한 필드를 설정하는 것

<img width="715" alt="dj_276" src="https://user-images.githubusercontent.com/86648892/212551750-097f9c7d-a213-4a5f-aac8-4966a7afe5e0.png">

---

# Django shortcuts functions

- `django.shortcuts` 패키지는 개발에 도움될 수 있는 여러 함수와 클래스를 제공
- 제공되는 shortcuts 목록
  - `render()` , `redirect()` , `get_object_or_404()` , `get_list_or_404()`
    - `get()` 대신 `get_object_or_404()`
    - `all()` 대신 `get_list_or_404()`
  - [https://docs.djangoproject.com/en/4.1/topics/http/shortcuts/](https://docs.djangoproject.com/en/4.1/topics/http/shortcuts/)

## `get_object_or_404()`

- `objects.get()` 과 같은 코드의 경우 해당 pk의 값이 없거나, 혹은 2개 이상인 경우 모두 예외가 발생함
  - `objects.get()` 의 경우 코드 진행이 더 이상 이루어지지 않고
    - Django는 500 status를 반환함
- `get_object_or_404()` 의 경우 예외 발생 시 404 status와 함께 코드 진행 가능
  - 해당 객체가 없을 때 DoesNotExist 예외 대신 Http404를 raise함

<img width="607" alt="dj_277" src="https://user-images.githubusercontent.com/86648892/212551749-c2eee230-4f90-4015-9464-621c6b75a604.png">

## `get_list_or_404()`

- 빈 쿼리셋을 주는 것이 아닌 404 status를 반환

<img width="629" alt="dj_278" src="https://user-images.githubusercontent.com/86648892/212551747-4b59ae5c-47ac-46cc-8a32-c584fed83dc9.png">

## WHY?

- API 서버의 기본은 정확한 상태 코드를 반환하여 클라이언트와 소통하는 것
- 클라이언트 입장에서 “서버에 오류가 발생하여 요청을 수행할 수 없다(500)”라는 원인이 정확하지 않은 에러를 마주하기보다는, 서버가 적절한 예외 처리를 하고 클라이언트에게 올바른 에러를 전달하는 것 또한 중요한 요소

---

### [추가] SerializerMethodField

- [SerializerMethodField](https://www.django-rest-framework.org/api-guide/fields/#serializermethodfield)
- [SerializerMethodField로 모델에서 변형된 JSON을 내려주기](https://eunjin3786.tistory.com/m/268)
- [APIView, api_view란?](https://hangjastar.tistory.com/m/203)

---