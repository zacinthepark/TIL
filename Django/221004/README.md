### Brief DDL and DML Summary
- **SQL** <br>
DDL과 DML <br>
DDL은 ```CREATE TABLE```, ```ALTER TABLE```, ```DROP TABLE``` <br>
DML은 SELECT INSERT UPDATE DELETE

<hr>

- **DDL** <br>
테이블 형성 시 ```INTEGER PRIMARY KEY``` 주면 ```rowid``` 대체함

```
CREATE TABLE contacts (
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    email TEXT NOT NULL UNIQUE
);
```

```
ALTER TABLE contacts RENAME TO new_contacts;
ALTER TABLE new_contacts RENAME COLUMN name TO last_name;
ALTER TABLE new_contacts ADD COLUMN address TEXT NOT NULL;
ALTER TABLE new_contacts ADD COLUMN address TEXT NOT NULL DEFAULT 'no address';
ALTER TABLE new_contacts DROP COLUMN address;
```

```
DROP TABLE new_contacts;
```

<hr>

- **DML**
```
SELECT DISTINCT 컬럼, 컬럼 FROM 테이블 ORDER BY 컬럼 DESC 내림 ASC 오름;
SELECT 컬럼, 컬럼 FROM 테이블 WHERE 컬럼 LIKE '_문자열%';
SELECT 컬럼, 컬럼 FROM 테이블 WHERE 컬럼 BETWEEN 숫자 AND 숫자;
SELECT 컬럼, 컬럼 FROM 테이블 WHERE 컬럼 NOT BETWEEN 숫자 AND 숫자;
SELECT 컬럼, 컬럼 FROM 테이블 WHERE 컬럼 IN ('값', '값');
SELECT 컬럼, 컬럼 FROM 테이블 LIMIT 10;
SELECT 컬럼, 컬럼 FROM 테이블 LIMIT 10 OFFSET 10;
```

```SELECT 컬럼, Aggregate Function(컬럼) AS alias명 FROM 테이블 GROUP BY 컬럼, 컬럼```
Aggregate Function은 `AVG`, `SUM`, `MIN`, `MAX`, `COUNT` 등 존재

```
INSERT INTO 테이블이름 (컬럼, 컬럼, 컬럼) VALUES (값, 값, 값);
INSERT INTO 테이블이름 VALUES (값, 값, 값), (값, 값, 값), (값, 값, 값);
```

```
UPDATE 테이블이름 SET 컬럼=값, 컬럼=값 WHERE 조건분기;
UPDATE 테이블이름 SET 컬럼=값, 컬럼=값; -- 전부 다
DELETE FROM 테이블이름; -- 전체 삭제
DELETE FROM 테이블이름 WHERE 조건분기; -- 일부 삭제
```