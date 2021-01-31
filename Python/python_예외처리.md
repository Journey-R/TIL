# 예외처리



## try, except, finally

### 1. 모든 오류에 대한 예외 처리

```python
try :
	...
except :
	...
```



### 2. 특정 오류에 대한 예외 처리

```python
try :
	...
except 오류 as 변수 :
	...
except 오류 as 변수 :
	pass 	# 해당 오류에 대한 pass
```



### 3. finally

- 오류 발생 여부와 무관하게 수행

```python
f = open('foo.txt', 'w')
try:
    ...
finally:
    f.close()
```

