# DML

- Data Manipulation Language (데이터 조작어)
- 레코드를 조회/추가/수정/삭제 하는 언어



- DML 종류

| 종류   | 설명        |
| ------ | ----------- |
| SELECT | 레코드 조회 |
| INSERT | 레코드 추가 |
| UPDATE | 레코드 수정 |
| DELETE | 레코드 삭제 |



---



### 1. 레코드 조회 (SELECT)

#### 1.1 전체 레코드 조회

```MSSQL
-- SELECT 
-- * 
-- FROM 테이블명
SELECT 
*
FROM UserInfo
```



#### 1.2 특정 컬럼만 조회

```MSSQL
-- SELECT 
-- 컬럼1, 컬럼2, ...
-- FROM 테이블명
SELECT 
  ID
, [NAME]
FROM UserInfo
```



#### 1.3 조회 조건 추가

```MSSQL
-- SELECT 
-- * 
-- FROM 테이블명
-- WHERE 조건
SELECT 
*
FROM  UserInfo
WHERE ADDRESS LIKE '서울시%'
```



---



### 2. 레코드 추가 (INSERT)

#### 2.1 단일 레코드 추가



#### 2.1.1 전체 컬럼의 데이터 추가

#### 2.1.1.1 컬럼명 명시

```mssql
-- insert into 데이터를 추가할 테이블명(컬럼명1, 컬럼명2, 컬럼명3)
-- values(컬럼1에 추가할 데이터, 컬럼2에 추가할 데이터, 컬럼3에 추가할 데이터)
insert into testTable(ID, [NAME], REMARKS)
values(1, 'test1', 'testData')
```



#### 2.1.1.2 컬럼명 명시하지 않음

- 컬럼명을 명시하고 추가할 경우, 전체 컬럼에 대한 데이터 입력에 한하여 가능하며, 전체 컬럼을 테이블에서의 컬럼 순서대로 기재해야한다.

```mssql
--  insert into 데이터를 추가할 테이블명
--  values(컬럼1에 추가할 데이터, 컬럼2에 추가할 데이터, 컬럼3에 추가할 데이터)
insert into testTable
values(2, 'test2', 'testData')
```



#### 2.1.2.1 일부 컬럼의 데이터만 추가

- 명시하지 않을 컬럼의 데이터는 'null'이 들어간다.

- 명시하지 않은 컬럼 중에 null 허용되지 않는 컬럼이 있을 경우, 데이터가 추가되지 않는다.

  - 오류 메시지 : Cannot insert the value NULL into column 'ID', table 'Test_Ryu.dbo.testTable'; column does not allow nulls. INSERT fails. 

    ​						The statement has been terminated.

```MSSQL
-- insert into testTable(컬럼명1, 컬럼명2)
-- values(컬럼1에 추가할 데이터, 컬럼2에 추가할 데이터)
insert into testTable(ID, [NAME])
values(3, 'test3')
```



#### 2.1.3 일부 컬럼의 값을 NULL으로 추가

- null이 허용되지 컬럼에 대해서만 null값을 명시적으로 추가할 수 있다.

```mssql
insert into testTable
values(4, 'test4', null)
```



---



### 2. 레코드 추가 (INSERT)

#### 2.2 다중 레코드 추가

```mssql
-- insert into 데이터 추가할 테이블명
-- values(컬럼1에 추가할 데이터, 컬럼2에 추가할 데이터)
-- , (컬럼1에 추가할 데이터, 컬럼2에 추가할 데이터)
-- , (컬럼1에 추가할 데이터, 컬럼2에 추가할 데이터)
insert into testTable
values(5, 'test5', null)
, (6, null, 'testData')
, (7, 'test7', 'testData')
, (8, null, null)
```



---



### 2. 레코드 추가 (INSERT)

#### 2.3 다른 테이블의 데이터 조회(복사)하여 추가



#### 2.3.1 다른 테이블의 전체 컬럼 조회하여 추가

#### 2.3.1.1 조회할 테이블과 데이터 추가할 테이블의 컬럼의 순서와 형식이 같은 경우

```mssql
-- insert into 데이터를 추가할 테이블명
-- select *
--  from 추가할 데이터를 조회해올 테이블명
insert into testTable2
select *
from testTable
```



#### 2.3.1.2 조회할 테이블과 데이터 추가할 테이블의 컬럼의 순서와 형식이 다르거나 테이블의 컬럼 갯수가 다를 경우, 데이터를 추가할 컬럼명을 명시

```mssql
--  insert into 데이터를 추가할 테이블명(데이터 추가할 컬럼명1, 데이터 추가할 컬럼명2, 데이터 추가할 컬럼명3)
-- select *
--   from 추가할 데이터를 조회해올 테이블명
insert into testTable3(_id, _name, _remarks)
select *
from testTable
```



#### 2.3.2 일부 컬럼만 조회하여 추가

```mssql
--  insert into 데이터를 추가할 테이블명
--  select 1번째 컬럼에 추가할 데이터를 조회해올 컬럼명, 2번째 컬럼에 추가할 데이터를 조회해올 컬럼명, 3번째 컬럼에 추가할 데이터를 조회해올 컬럼명
--   from 추가할 데이터를 조회해올 테이블명
insert into testTable2
select _id, _name, _remarks
from testTable3
```



#### 2.3.3 조회할 테이블에 조건 추가

```mssql
-- insert into 데이터를 추가할 테이블명
-- select *
--  from 추가할 데이터를 조회해올 테이블명
-- where 조회할 데이터의 조건
insert into testTable2
select *
from testTable
where id < 3
```



---



### 2. 레코드 추가 (INSERT)

#### 2.4. 특정한 컬럼에만 데이터 추가

```mssql
-- insert into 테이블명(데이터 추가할 컬럼명)
-- valeus(추가할 데이터)
insert into testTable (ID)
values(9)
```



---



### 3. 레코드 수정 (UPDATE)

- 조건이 없을 경우, 해당 컬럼의 데이터가 모두 set 절의 값으로 수정된다.

```mssql
-- update수정할 데이터가 있는 테이블명
-- set 수정할 데이터의 컬럼명 = 수정할 데이터
-- where 수정할 데이터의 조건
update EMS_Users
set USER_NAME = 'testUser'
where USER_ID = 'test7'
```



---



### 4. 레코드 삭제 (DELETE)

- 조건이 없을 경우, 모든 레코드가 삭제된다.

```mssql
-- delete 삭제할 데이터가 있는 테이블명
-- where 삭제할 데이터의 조건
delete EMS_Users
where USER_ID = 'updateTest5'
```

