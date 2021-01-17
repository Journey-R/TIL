# python의 제어문

- 조건문 : `if~elif~else`
  - python의 조건문에는 `case`문이 없다.
- 반복문 : `for`, `while`

---

## 조건문

- ### if~elif~else

  ```python
  number = 15
  
  if  (number % 3 == 0) & (number % 5 == 0) :
      print("3과 5의 배수 : {}".format(number))
  elif  number % 3 == 0 :
      print("3의 배수 : {}".format(number))
  elif number % 5 == 0 :
      print("5의 배수 : {}".format(number))
  else :
      print("3, 5의 배수 아님 : {}".format(number))
  ```

  



## 반복문

- ### for

  - `for index in <collection> :`

- ### while

  - `while 조건 :`

- ### 반복문 관련 예제
  -  https://github.com/Journey-R/TIL/blob/master/Python/python_base/02_loop_statement.py



## 조건문 반복문을 함께 쓴 예제

- https://github.com/Journey-R/TIL/blob/master/Python/python_base/02_controll_statement(for_if).py