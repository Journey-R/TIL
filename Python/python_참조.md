# python의 참조

## import

- 표준 라이브러리에 있는 모듈 참조
- 특정 패키지 참조

```python
import math
math.sqrt(4.0)     # 모듈.함수() 형식으로 모듈 내부 함수 사용
```



- 모듈 참조 후 이름 지정

```python
import math as m	
m.sqrt(4.0)
```



- 복수 개의 모듈 참조

```python
import datetime, time
```



## from import

- 모듈의 모든 변수, 함수, 클래스 참조

```python
from math import *
```



- 모듈의 특정 변수, 함수, 클래스 참조

```python
from math import sqrt
```



- 모듈의 특정 변수들, 함수들, 클래스들 참조

```python
from math import sqrt, pi
```



- 참조 후 이름 지정

```python
from math import sqrt as s, pi as p 
```



## del

- 참조 해제

```python
del math
```