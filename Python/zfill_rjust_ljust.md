# zfill, rjust, ljust

- 지정한 자리 수보다 문자열의 길이가 짧을 경우, 문자열 앞/뒤로 '0'이나 fillchar로 채움



## zfill

- 지정한 자리 수보다 문자열의 길이가 짧을 경우, 문자열 앞을 '0' 채움
- str.zfill(width)

```python
'99'.zfill(4) # print : 0099
```



## rjust

- 지정한 자리 수보다 문자열의 길이가 짧을 경우, 문자열 앞을 fillchar로 채움
- str.rjust(width, fillchar)
- fillchar : 기본값은 공백

```python
'99'.rjust(4)  # print : '  99'
'99'.rjust(4, '0')  # print : '0099'
'99'.rjust(4, 'A')  # print : 'AA99'
```



## ljust

- 지정한 자리 수 보다 문자열의 길이가 짧을 경우, 문자열 뒤를  fillchar로 채움
- str.ljust(width, fillchar)
- fillchar : 기본값은 공백

```python
'99'.ljust(4) # print : '99  '
'99'.ljust(4, '0')   # print : '9900'
'99'.ljust(4, 'A')   # print : '99AA'
```

