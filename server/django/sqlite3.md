## sqlite3

---

### sqlite3 settings

- sqlite3는 sqlite와 직접적으로 소통할 수 있는 실행 환경 (shell)

- Download
    - https://www.sqlite.org/download.html
    - sqlite-dll-win-x64-3460000.zip
    - sqlite-tools-win-x64-3460000.zip

- Installation
    - C드라이브에 sqlite 폴더 생성 후 압축 푼 모든 파일을 sqlite 폴더로 이동
    - 시스템 환경변수 편집
        - 환경변수에 등록한다는 것은 여기에 등록되어 있는 위치가 컴퓨터가 항상 참조할 수 있는 위치라는 것
        - `고급 - 환경변수 - Path - 편집 - sqlite 폴더 경로 추가`
        - 이를 통해 sqlite 폴더 안에 있는 파일들을 컴퓨터가 항상 참조할 수 있는 상태가 됨

- Alias
    - `winpty sqlite3`: C드라이브의 sqlite 폴더 안에서 sqlite3를 찾아 실행할 수 있게 하는 커맨드
    - bash alias 설정
        - `code ~/.bashrc`: .bashrc 실행
        - `alias sqlite3="winpty sqlite3"`: alias 설정 저장
        - `source .bashrc`: .bashrc 변경사항 적용

### sqlite3 사용하기

- `sqlite3`: alias를 통해 shell 실행
    - `sqlite > .open mydb.sqlite3`: 데이터베이스 파일 열기
    - `sqlite3 mydb.sqlite3`와 같이 shell 실행하면서 DB를 열 수도 있음

- `.exit`: sqlite3 종료

- `.help`: commands 확인

- CSV 파일 SQLite 테이블로 가져오기
    - `DML.sql` 파일 생성하여 테이블 생성
    - `sqlite3 mydb.sqlite3`: 데이터베이스 파일 열기
    - `sqlite > .mode csv`: 모드를 csv로 설정
    - `sqlite > .import users.csv users`: csv 데이터를 테이블로 가져오기

### SQLite

- 응용 프로그램에 *파일 형식* 으로 넣어 사용하는 비교적 가벼운 데이터베이스
- 안드로이드, iOS, macOS에 기본적으로 탑재되어 있으며 임베디드 소프트웨어에서도 많이 활용됨
- 오픈소스 프로젝트이기에 자유롭게 사용 가능

- 장점
    - 어떤 환경에서나 실행 가능한 호환성
    - 데이터 타입이 비교적 적고 강하지 않기에 유연한 학습 환경 제공
    - Django Framework의 기본 데이터베이스

- 단점
    - 대규모 동시 처리 작업에 적합하지 않음
    - 다른 RDBMS에서 지원하는 SQL 기능을 지원하지 않을 수 있음

### SQLite Data Types

- Data Types
    - `NULL`
        - NULL value
        - 정보가 없거나 알 수 없음을 의미 (missing information or unknown)
    - `INTEGER`
        - 정수
        - 크기에 따라 0, 1, 2, 3, 4, 6 또는 8바이트와 같은 가변 크기를 가짐
    - `REAL`
        - 실수
        - 8바이트 부동 소수점을 사용하는 10진수 값이 있는 실수
    - `TEXT`
        - 문자 데이터
    - `BLOB` (Binary Large Object)
        - 입력된 그대로 저장된 데이터 덩어리 (대용 타입 없음)
        - 바이너리 등 멀티미디어 파일
        - 예시
            - 이미지 데이터

- Boolean Type?
    - SQLite에는 별도의 Boolean 타입이 없음
    - 대신 Boolean 값은 정수 0(false)과 1(true)로 저장됨

- Date & Time Datatype?
    - SQLite에는 날짜 및 시간을 저장하기위한 타입이 없음
    - 대신 SQLite의 built-in 'Date And Time Functions”'으로 TEXT, REAL 또는 INTEGER 값으로 저장할 수 있음
    - https://www.sqlite.org/lang_datefunc.html

- Binary Data
    - 데이터의 저장과 처리를 목적으로 0과 1의 이진 형식으로 인코딩된 파일
    - 기본적으로 컴퓨터의 모든 데이터는 binary data
        - 다만, 이를 필요에 따라서 텍스트 타입으로 변형해서 사용하는 것

- SQLite은 다음 규칙을 기반으로 데이터 타입을 결정
    - 값에 둘러싸는 따옴표와 소수점 또는 지수가 없으면 `INTEGER`
    - 값에 따옴표가 없고, 소수점, 지수가 있으면 `REAL`
    - 값이 작은 따옴표나 큰 따옴표로 묶이면 `TEXT`
    - 값이 따옴표 없이 NULL이면 `NULL`

### SQLite Data Types 특징

1. SQLite는 다른 모든 SQL 데이터베이스 엔진(MySQL, PostgreSQL 등)의 정적이고 엄격한 타입(static, rigid typing)이 아닌
    - *동적 타입 시스템(dynamic type system)* 을 사용
        - 컬럼에 선언된 데이터 타입에 의해서가 아니라 *컬럼에 저장된 값에 따라 데이터 타입이 결정* 됨
    - 타입을 선언하여 정적 타입 시스템을 사용할 수도, 선언하지 않고 동적 타입 시스템을 사용할 수도 있음

<p align="center">
    <img width="500" alt="db17" src="https://user-images.githubusercontent.com/86648892/212545593-7bf37a9b-c83a-405a-9345-b04946eb5bba.png">
</p>

2. 테이블을 생성할 때 컬럼에 대해 특정 데이터 타입을 선언하지 않아도 됨
    - 예를 들어 동일한 컬럼에 정수 1을 넣을 경우 INTEGER로 타입이 지정되고
        - 문자 ‘1’을 넣을 경우는 TEXT 타입으로 지정됨
    - 이러한 SQLite의 동적 타입 시스템을 사용하면 기존의 엄격하게 타입이 지정된 데이터베이스에서는 불가능한 작업을 유연하게 수행할 수 있음
    - 또한 정적 타입 시스템이 지정된 데이터베이스에서 작동하는 SQL문이 SQLite에서 동일한 방식으로 작동
        - 즉, 정적 타입 시스템이 하지 못하는 작업을 할 수도 있으면서, 정적 타입 시스템에서 작동하는 것을 동일하게 작동할 수 있다는 것
    - 그러나, 다른 데이터베이스와의 호환성 문제가 있기 때문에 테이블 생성 시 *데이터 타입을 지정하는 것을 권장*

3. 데이터 타입을 지정하게 되면 SQLite는 데이터의 타입을 지정된 데이터 타입으로 변환
    - 예를 들어, TEXT 타입 컬럼에 정수 1을 저장할 경우 문자 타입의 ‘1’로 저장됨
    - 허용 가능한 타입 변환은 다음과 같음

<p align="center">
    <img width="500" alt="db16" src="https://user-images.githubusercontent.com/86648892/212545594-dfda2ceb-e83d-454c-9a28-72907567df8d.png">
</p>

#### Type Affinity

<p align="center">
    <img width="500" alt="db18" src="https://user-images.githubusercontent.com/86648892/212545591-dc347d4e-2809-4629-b138-656999480ffc.png">
</p>

- SQLite의 독특한 특징으로, 제공하는 Datatype의 종류가 많지 않기에, 호환성에 대비하여 내부적으로 타입을 선호하는, 선호도라는 것이 존재함

- 데이터 타입 작성 시, SQLite의 5가지 데이터 타입이 아닌 다른 데이터 타입을 선언한다면, 내부적으로 각 타입의 지정된 선호도에 따라 5가지 선호도로 인식됨

- 타입 선호도 존재 이유
    - 다른 데이터베이스 엔진 간의 호환성을 최대화하기 위함
    - 정적이고 엄격한 타입을 사용하는 데이터베이스의 SQL문을 SQLite에서도 작동하도록 하기 위함

### Constraints

- 입력하는 자료에 대해 제약을 정하며 제약에 맞지 않다면 입력이 거부됨

- 데이터의 무결성을 유지하기 위해 테이블의 특정 컬럼에 설정하는 제약

- Constraints
    - `NOT NULL`
        - 컬럼이 NULL 값을 허용하지 않도록 지정
        - 기본적으로 테이블의 모든 컬럼은 NOT NULL 제약 조건을 명시적으로 사용하는 경우를 제외하고는 NULL 값을 허용함

    - `UNIQUE`
        - 컬럼의 모든 값이 서로 구별되거나 고유한 값이 되도록 함
        - 처음에 들어간 값이 동일 컬럼의 다른 레코드에 들어갈 수 없음

    - `PRIMARY KEY`
        - 테이블에서 행의 고유성을 식별하는데 사용되는 컬럼
        - 각 테이블엔 하나의 기본 키만 있음
            - id column은 하나
            - PRIMARY KEY를 따로 정의해주지 않으면 `rowid` 라는 이름으로 자동으로 만들어졌음
        - 만약 직접 pk를 선언하고 싶다면 PRIMARY KEY라는 제약 조건을 선언
        - 암시적으로 NOT NULL 제약 조건이 포함되어 있음
        - *INTEGER 타입에만 사용 가능 (INT BIGINT 등 불가능)*

    - `AUTOINCREMENT`
        - 사용되지 않은 값이나 이전에 삭제된 행의 값을 재사용하는 것을 방지
            - 1, 2, 3행이 있었는데 3이 삭제되고, 행 하나 추가하면 다시 3이 들어감
            - AUTOINCREMENT를 INTEGER PRIMARY KEY에 다음에 작성하면 해당 rowid를 다시 재사용하지 못하도록 함
            - `id INTEGER PRIMARY KEY AUTOINCREMENT`
            - Django에서 테이블 생성 시 id 컬럼에 기본적으로 AUTOINCREMENT를 제약 조건으로 사용

    - 그 외 기타

### rowid

- 테이블을 생성할 때마다 `rowid`라는 암시적 자동 증가 컬럼이 자동으로 생성됨
    - 즉, 별도로 속성값을 주지 않아도 자동으로 다음값으로 증가하는 컬럼이라는 뜻

- 테이블의 행을 고유하게 식별하는 64비트 부호 있는 정수 값
    - 64비트의 컴퓨터가 허용할 수 있는 최대 크기까지 정수 값을 가지고 있다고 보면 됨

- 테이블에 새 행을 삽입할 때마다 정수 값을 자동으로 할당
    - 값은 1에서 시작
    - 데이터 삽입 시에 rowid 또느 INTEGER PRIMARY KEY 컬럼에 명시적으로 값이 지정되지 않은 경우, SQLite는 테이블에서 가장 큰 rowid보다 하나 큰 다음 순차 정수를 자동으로 할당
    - `AUTOINCREMENT`가 제약 조건일 시 삭제된 행의 다음 순차 정수

- 만약 `INTEGER PRIMARY KEY` 키워드를 가진 컬럼을 직접 만들면 이 컬럼은 rowid 컬럼의 별칭(alias)이 됨
    - 내부적으로 rowid가 없어진 것은 아님
    - 우리가 만든 PRIMARY KEY이름으로 rowid에 접근한다고 생각하면 됨
    - 즉, 새 컬럼 이름으로 rowid에 액세스 할 수 있으며, rowid 이름으로도 여전히 액세스 가능

- 한 테이블의 PK가 최대 어디까지 저장될까?
    - 한 테이블의 행의 최대 개수는 `2^64` 까지 이론상으론 들어갈 수 있음
    - 그러나 실제론 `2^64` 까진 도달하기 어렵다고 한다
    - https://www.sqlite.org/limits.html

- 만약 꽉 찬 상태의 테이블에 데이터를 넣는다면?
    - 데이터가 최대 값에 도달하고 새 행을 삽입하려고 하면 SQLite는 *사용되지 않는 정수를 찾아 사용*
    - SQLite가 사용되지 않은 정수를 찾을 수 없으면 *SQLITE_FULL* 에러가 발생
        - 또한 일부 행을 삭제하고 새 행을 삽입하면 SQLite는 삭제된 행에서의 rowid 값을 재사용하려고 시도
        - AUTOINCREMENT가 없다면 pk는 기본적으로 삭제되었을 때 재사용하려고 시도됨
