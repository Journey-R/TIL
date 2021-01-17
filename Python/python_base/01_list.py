# python list(자료 구조에서 매우 중요)
# 파이썬에는 배열(array)이 존재하지 않음
# 1차원 자료구조로서 R의 Vector와 같은 자료형이다.
# 순서 존재, 중복 허용, 추가/수정/삭제 가능
# 한 list에 다양한 데이터 타입의 값을 담을 수 있다.
# index : 0부터 시작
# [] 이용하여 변수 선언

# 선언
# 빈 list 선언
a = list()
a = []

# 초기화, 값 할당
a = [1,2,3]
a = [1,2,"hello", 3,4, True, 1.15]              # 한 list에 다양한 데이터 타입을 담을 수 있음
a = [1,2,["show", "me", "the", "money"], 3.15]  # 중첩 list

print(a, type(a))

# 슬라이싱 가능
print(a[0])
print(a[-1])
print(a[2])

# 중첩 list의 내부 list에 접근('me' 출력)
inner_list = a[2]
print(inner_list[1])

print(a[2][1])      # 1번째
print(a[2][2:])     # 2번째부터 전체
print(a[2][1:3])    # 1~2(3-1)    start index는 index(0부터 시작), end index는 len(1부터 시작)

# money 출력
print(a[2][-1])
print(a[-2][3])

# list + list = 하나의 list
# list의 결합이기 때문에 길이는 중요치 않음
a = [1,2,3]
b = [4,5,6]
print(a+b)

c = a+b
print(c, type(c))

# "데이터" * n : 데이터 n개 반복 출력
print("*" * 50)
print(len("*" * 50))

a = [1,2,3]
print(a * 3)  # list도 반복 가능

# list(index) = 데이터 : 특정 index의 값 수정
a = [1,2,3]
a[0] = 5
print(a)

# list.append() : 마지막 index에 데이터 추가
a.append(4)
print(a)

# list.insert() : 특정 index에 데이터 추가하고 해당 index부터 한 자리씩 밀려남
# 원하는 index에 데이터 추가용
a.insert(0, 6)
print(a)

# list.sort() : 오름차순 정렬
a.sort()
print(a)

# list.reverse() : 내림차순 정렬
a.reverse()
print(a)

# list.pop() : 원하는 index의 값을 반환 및 해당 값 삭제
# default = 마지막 index
# index 설정시 = 해당 index의 값 제거
print(a.pop())
print(a)

movie_rank = ["강철비2", "반도", "다만 악에서 구하소서", "인셉션"]
idx = movie_rank.index("다만 악에서 구하소서")
print(idx)
print(movie_rank.pop(idx))


# list.remove("데이터") : list에서 데이터 제거
# del list[index] : list 중 index에 해당하는 데이터만 삭제

# list.extend(데이터) : list에 데이터를 Append
ex = [4,3]
a.extend(ex)
print(a)

# list.indext(데이터) : list에서 데이터 값의 index 반환
movie_rank = ["강철비2", "반도", "다만 악에서 구하소서", "인셉션"]
idx = movie_rank.index("다만 악에서 구하소서")
del movie_rank[idx]
print(movie_rank)

# 실습-------
movie_rank = ["강철비2", "반도", "다만 악에서 구하소서", "인셉션"]
print(movie_rank)

# 1. 해당 리스트에 '배트맨' 추가
movie_rank.append("배트맨")
print(movie_rank)

# 2. 강철비2와 반도 사이에 슈퍼맨 추가
movie_rank.insert(1, "슈퍼맨")
print(movie_rank)

# 3. 리스트에 '인셉션' 삭제
movie_rank.remove("인셉션")
print(movie_rank)

# 4. 리스트에서 '다만 악에서 구하소서'와 '배트맨' 삭제
del movie_rank[3]
del movie_rank[3]
print(movie_rank)

# 특정 값이 있는 index를 찾아 삭제
movie_rank = ["강철비2", "반도", "다만 악에서 구하소서", "인셉션"]
idx = movie_rank.index("다만 악에서 구하소서")
del movie_rank[idx]
print(movie_rank)

# pop()을 활용한 특정 index의 값 제거
movie_rank = ["강철비2", "반도", "다만 악에서 구하소서", "인셉션"]
idx = movie_rank.index("다만 악에서 구하소서")
print(idx)
print(movie_rank.pop(idx))


# 실습2---

# 다음 리스트에서 최대값, 최소값, 총합, 평균 출력
# min(), max(), 함수 사용
num = [1,2,3,4,5,6,7]
print("최대값 : ", max(num), ", 최소값 : ", min(num),", 총합 : ", sum(num), ", 평균 : ", sum(num) / len(num))

# 리스트에 저장된 데이터의 개수 출력
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소세지", "라면", "팥빙수", "김치전"]
print("cook length : ", len(cook))

# price 변수에는 날짜와 종가 정보가 저장돼있다.
# 해당 날짜 정보를 제외하고 가격 정보만 출력
price = ["20180728", 100, 130, 140, 150, 160, 170]
print("price : ", price[1:])

# 슬라이싱을 사용해서 홀수, 짝수 출력
nums = [1,2,3,4,5,6,7,8,9,10]
print("홀수 : ", nums[0::2])
print("짝수 : ", nums[1::2])

# 슬라이싱을 사용해서 리스트의 숫자를 역방향으로 출력하라
nums = [1,2,3,4,5]
#print("nums 역순 : ", nums[::-1])
#print("nums 역순(reverse) : ", nums.reverse())

nums.sort(reverse = True)
print("nums 역순(sort(reverse = True)) : ", nums)

# interest 리스트 중 삼성전자, Naver만 출력
interest = ["삼성전자", "LG전자", "Naver"]
idx1 = interest.index("삼성전자")
idx2 = interest.index("Naver")
print("삼성전자, Naver만 출력 : ", interest[idx1], interest[idx2])

# "구분자".join(list) : list 내부의 데이터들을 구분자로 합침
# 데이터 타입이 변경됨
interest = ["삼성전자", "LG전자", "Naver", "SK하이닉스", "미래에셋"]
print(interest, type(interest))             # ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋'] <class 'list'>

interestJoin = (" ".join(interest))
print(interestJoin, type(interestJoin))     # 삼성전자 LG전자 Naver SK하이닉스 미래에셋 <class 'str'>

interestJoin = ("\n".join(interest))
print(interestJoin, type(interestJoin))     # class 'str'

# range() : sequance 타입
# 숫자 sequance,  주로 for loop에서 사용
# range(10) : 0~10
# range(1,11,2) : 1~11까지 2씩 증가
range01 = range(10)
print("range : ", range01)

range02 = range(1,11,2)
print("range2 : ", range02)

print(10 in range01)

# python의 for 구문
# : 뒤에서 Enter 치면 자동으로 들여쓰기가 되고 그 칸에서 탭/공백 등을 주거나 위치를 변경할 경우 오류 발생
#   오류 메시지 -> IndentationError: expected an indented block
for idx in range(10) :
    print(idx)


