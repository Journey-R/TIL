# MSSQL - DDL

## DDL

- Data Definition Language (데이터 정의 언어)
- DB의 구조 정의
  - SQL에 의해 정의되는 관계형 DB의 구조는 쌍(레코드/행), 속성(컬럼/열), 관계(테이블), 인덱스 파일 위치 등 DB 고유의 특성을 포함
- DDL의 종류

| 종류      | 설명                             | 상세                             |
| --------- | -------------------------------- | -------------------------------- |
| CREATE    | DB 및 DB 객체 생성               | TABLE, VIEW, INDEX, SP 등 생성   |
| DROP      | DB 및 DB 객체 삭제               | TABLE, VIEW, INDEX, SP 등 삭제   |
| ALTER     | DB 및 DB 객체 재정의             | TABLE, VIEW, INDEX, SP 등 재정의 |
| TRAUNCATE | TABLE 초기화<br/>(ROLLBACK 불가) | TABLE의 모든 레코드 삭제<BR/>    |



---



### 1. 테이블생성 (CREATE)

```mssql
  -- creat table 생성할 테이블명
  -- (
  --      컬럼명      데이터 타입      제약 조건
  --    , 컬럼명      데이터 타입      제약 조건
  -- )
    
create table UserInfo
  (
 
         ID                      INT
       , [NAME]                  NVARCHAR(10)
       , CELLPHONE_NUMBER        INT
       , [ADDRESS]               NVARCHAR(50)
       , FINAL_ACCESS_DATETIME   DATETIME
 
  )
```

- 제약 조건
  - 생략 가능 
    - 생략시  default : 'NULL' 허용



---



### 2. 테이블 삭제 (drop)

```mssql
-- drop table 삭제할 테이블명
drop table UserInfo
```

- TRUNCATE는 모든 레코드 삭제, DROP은 테이블을 삭제한다. (데이터와 테이블의 구조까지)



---



### 3. 테이블 수정 (alter)

#### 3.1 컬럼 추가

```mssql
-- alter table 수정할 테이블명
-- add  추가할 컬럼명     데이터 타입     제약조건
alter table UserInfo
add testCol             nvarchar(10)  not null
```



#### 3.2 컬럼 수정

```mssql
-- alter table 수정할 테이블명
-- alter column 수정할 컬럼명       데이터 타입     제약조건
alter table UserInfo
alter column ID         int  not null
```



#### 3.3 컬럼 삭제

```mssql
-- alter table 수정할 테이블명
-- drop column 삭제할 컬럼명
alter table UserInfo
drop column testCol
```



#### 3.4 제약 조건 추가 

#### 3.4.1 Primary Key 추가 

```mssql
-- alter table 수정할 테이블 명
-- add constraint 키 이름 primary key (컬럼명)
alter table testTable
add constraint PK_testTable primary key (ID)
```



#### 3.4.2 Foreign Key 추가

```mssql
-- alter table 수정할 테이블 명
-- add constraint 키 이름 foreign key (컬럼명)
-- references 참조할 테이블명(참조할 컬럼명)
alter table UserInfo
add constraint FK_UserInfo foreign key (ID)
references testTable(ID)
```



#### 3.4.3 제약조건 삭제

```mssql
-- alter table 수정할 테이블
-- drop constraint 제약조건 이름
alter table UserInfo
drop constraint FK_UserInfo
```



---



### 4. 테이블의 모든 행 삭제 (TRUNCATE)

```mssql
-- truncate table 테이블명
truncate table UserInfo
```

- 조건문을 쓸 수 없다. (DML의 DELETE와의 차이점)