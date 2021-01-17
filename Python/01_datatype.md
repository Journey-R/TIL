# python의 data type

- Text Type : `str`
- Numeric Types :` int`, `float`, `complex`
- Sequence Types : `list`, ` tuple`
- Mapping Type : `dict`
- Set Types : `set`
- Boolean Type : `bool`

---

## Text Type

- ### str

  - 문자열
  - `''`, `""` 모두 허용
  - 여러 줄의 문자열 표현 : `'''str'''`, `"""str """`
  - https://github.com/Journey-R/TIL/blob/master/Python/python_base/01_str.py 

## Numeric Types 

- ### int

  - 정수 (integer)
  - 메모리가 허용하는 범위 상의 모든 정수

- ### float

  - 실수
  - 부동 소수형
    - 저장 공간의 효율적인 사용위해 8byte만 사용해서 소수 저장 (정밀도의 한계 존재)

- ### complex

  - 복소수 (실수 + 허수)
  - a+bi 형태 (a, b 는 실수, i는 허수, i² = -1)

```python
i = 12345
f = 3.14

c = 3 + 0.45j
print(c.real) # print : 3.0
print(c.imag) # print : 0.45
```



## Sequence Types 

- ### list

  - 파이썬에는 배열(array)이 존재하지 않음
  - 1차원 자료구조
  - 순서 존재, 중복 허용, 추가/수정/삭제 가능
  -  한 list에 다양한 데이터 타입의 값을 담을 수 있다.
  - index : 0부터 시작
  - `[]`
  - https://github.com/Journey-R/TIL/blob/master/Python/python_base/01_list.py

- ### tuple

  - list와 공통점 : 순서 있음, 중복 허용
  - list와 차이점 : 추가/수정/삭제 불가 -> 읽기 전용
  - `()`
  - https://github.com/Journey-R/TIL/blob/master/Python/python_base/01_tuple.py

  

## Mapping Type

- ### dict

  - key와 value의 대응관계 type
  - 순서 X, 키 중복 X, 추가/수정/삭제 O
  - `{}`
  - https://github.com/Journey-R/TIL/blob/master/Python/python_base/01_dict.py



## Set Types

- ### set

  - 집합 (교집합, 합집한, 차집합 등)
  - 순서 X, 중복 X, 추가/삭제/수정 가능
  - https://github.com/Journey-R/TIL/blob/master/Python/python_base/01_set.py

  ### 

## Boolean Type

- ### bool

  - True, False 반환
  - https://github.com/Journey-R/TIL/blob/master/Python/python_base/01_bool.py



---

## variable

- 변수 선언 시, 데이터 타입 미지정

```python
str1 = 'python'
num1 = 1234
```



## Type Check

```python
str1 = 'python'
print(type(str1)) # print : str
```



## Type Casting

- int(), str(), float() 등

```python
year = '2021'
year = int(year)  # '2021' -> 2021
str(year) # 2021 -> '2021'
```

