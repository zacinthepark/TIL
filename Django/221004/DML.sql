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