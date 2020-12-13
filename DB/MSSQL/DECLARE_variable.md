# DECLARE (변수)

### 1. 변수 선언

```mssql
-- declare @변수명 데이터타입
declare @menuName varchar(20);
```



---



### 2. 변수 값 대입

#### 2.1 변수 값 대입

```mssql
-- set @변수명 = 변수의 값
set @menuName = '꾜'
```



#### 2.2 변수 값 대입 (테이블의 값 조회해서 대입)

```mssql
-- select @변수명 = 컬럼명 from 테이블명 where 조건식
--    -> Insert into시, Select후 특정 값 대입하는 것과 비슷함
--    -> 만약에 where 절이 없을 경우, 제일 마지막 row의 값이 대입됨
select @menuName = NAME
  from MenuList
 where ID = 'EM0110';
```



---



### 3. 변수의 값 출력

```mssql
 -- select @변수명
 select @menuName;
```



---



### 4. 변수의 사용 예 (where절에 조건으로 사용)

```mssql
 select *
   from MenuList
  where NAME = @menuName;
```



