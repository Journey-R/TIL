# set : 집합(교집합, 합집합, 차집합..)
# 순서 X, 중복 X, 추가/삭제/수정 가능

# set 타입 선언/할당
# set() : 빈 set 선언
# set([value, value, ...]) : set 초기화, 할당
# {value, value, ~~~} : set 초기화, 할당
# 다양한 데이터 타입 요소로 사용 가능 : 정수, 실수, 문자

# temp = set()
# print(type(temp))       # print : <class 'set'>
#
# temp = {"jslim", "teacher"}
# print(type(temp))       # print : <class 'set'>

#b = set(1,2,3,4,5)      # TypeError: set expected at most 1 arguments, got 5
# b = set([1,2,3,4,5])    #
# b = set([1,2,3,4,5,5,5,5])
# print(type(b))
#
# c =  set([1, 3.14, "Pen", False])
# print(c, ", 길이 - ", len(c))

# 형변환
# t = tuple(c)
# print("casting - ", t, t[1:3])
# print("casting - ", list(c))

# 두 집합 비교
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

# 교집합 : &, intersection
# set1 & set2
# set1.intersection(set2)
# print(" & - ", s1&s2)
# print("intersction - ", s1.intersection(s2))

# 합집합 : |, union
# set1|set2
# set1.union(set2)
# print("| - ", s1|s2)
# print("union - ", s1.union(s2))

# 차집합 : -, difference
# set1 : 기준이 되는 set
# set1-set2
# set1.difference(set2)
# print("- - ", s1-s2)
# print("difference - ", s1.difference(s2))

# set에 데이터 추가 : set.add(data)
# s1 = set([1,2,3,4,5,6])
# s1.add(7)
# print(s1)

# set에 데이터 삭제 : set.remove(data)
# s1.remove(7)
# print(s1)

#s1.remove(9)    # 없는 값 삭제시 오류 -> KeyError: 9
# s1.discard(9)    # 없는 값 삭제시에도 오류 발생하지 않음

# 중복 제거(핵심)
gender = ["남", "여","남", "여","남", "여"]
print(gender)

# set은 중복 비허용하므로, set으로 형변환을 함으로써 중복 제거
sgender = set(gender)       # {'여', '남'}
print(sgender)

# set은 index가 없으므로 index 사용이 필요할 경우, list로 형변환
lgender = list(sgender)
print(lgender[0])

s1 = set([1,2,3,4,5,6])
print(dir(s1))

for idx in s1 :
    print(idx, end = " ")