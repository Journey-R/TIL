# python의 string formatting



## % operator

- C언어의 printf() 스타일과 유사
- python3에서 권장하지 않는 방식 (오래된 방식)
- 단점 : 데이터 타입을 정확하게 알고 작성해야함

```python
print('country :%s' % 'Seoul')
print('age : %d' % 25)
print('weight : %.1f kg' % 57.1)
```

```python
print('country : %s, age : %d, weight : %.1fkg, year : %d, month : %d, day : %d' % ('Seoul', 25, 57.1, 2021, 1, 14))
```



##  str.format

- python3부터 사용

```python
print('country : {}'.format('Seoul'))
print('age : {}'.format(25))
print('weight : {}kg'.format(57.1))
```



- {}순서와 format() 파라미터 순서 동일

```python
print('country : {}, age : {}, weight : {}kg'.format('Seoul', 25, 57.1))
```



- {}에 들어갈 파라미터 순서 기재

```python
print('country : {1}, age : {2}, weight : {0}kg'.format(57.1,'Seoul', 25))
```



- {}에 이름 지정하여 format 파라미터에 이름별로 값 대입

```python
s = 'country : {country}, age : {age}, weight : {weight}kg'
s = s.format(country = 'Seoul', age = 25, weight = 57.1)
print(s)
```



## f-string

- python 3.6 이상부터 지원
- 변수에 값 대입 후, {} 안에 변수명 기재

```python
country = 'Seoul'
age = 25
weight = 57.1

print(f'country : {country}, age : {age}, weight : {weight}kg')
```

