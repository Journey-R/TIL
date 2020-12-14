# DECLARE (테이블 변수)

- 테이블 변수 사용 목적
  - 테이블 변수를 이용하면 쿼리의 복잡성을 낮출 수 있다.
  - 속도 개선에 도움이 될 수 있다.



### 1. 테이블 변수 정의

```mssql
-- declare @테이블변수명 table
-- (
-- 컬러명 데이터타입,
-- 컬러명 데이터타입,
-- 컬러명 데이터타입,
-- ...
-- )
declare @sampleTable table
(
	id nvarchar(10),
    menu nvarchar(20)
)
```



---



### 2. 테이블 변수에 데이터 추가

```mssql
-- insert into @테이블변수명
-- select insert할 컬럼명, insert할 컬럼명,
-- from insert할 데이터가 있는 테이블명
insert into @sampleTable
select ID, NAME
from MenuList
```



---



### 3. 테이블 변수 사용

```mssql
-- select * from @테이블변수명
select *
from @sampleTable
```

