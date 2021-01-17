# dict : 딕셔너리
# 범용적으로 가장 많이 사용하는 데이터 타입
# key와 value의 대응관계 type
# 순서 X, 키 중복 X, 추가/수정/삭제 O
# {}

# class : 실세계의 명사적/동사적 특징을 추상화시켜 하나의 틀(템플릿)을 모델링한 형태
#         하나의 템플릿인 class를 통해 다른 객체(인스턴스)를 만든다.
# object : 실세계의 객체
# dir() :

# 실세계의 Object -> 명사적 특징과 동사적 특징 -> 추상화 -> Class(인스턴스를 생성하기 위한 템플릿)
# 명사적 특징 : 변수, 동사적 특징 : 함수
# instance.변수 : class로 만든 인스턴스에 정의된 변수에 접근
# instance.함수 : class로 만든 인스턴스에 정의된 함수에 접근

# temp = {}
# print(type(temp))           # print : <class 'dict'>

# dic 생성(3가지 방법)
# 1. 일반적인 dict 생성
# dic = {"key1" : "value",
#        "key2" : "value",
#        "key3" : "value"}
dic01 = {"name"     : "seop",
         "age"      : 48,
         "address"  : "seoul",
         "birth"    : "730910",
         "gender"   : True}

# print("dic01 : ", type(dic01), dic01)

# 2. tuple을 이용한 dict 생성
# dic = dict(
#             [
#                ("key1", "value"),
#                ("key2", "value"),
#                ("key3", "value"),
#              ]
#               )
dic02 = dict([("name", "seop"),
             ("age", 48),
             ("address", "seoul"),
             ("birth", "730910"),
             ("gender", True)])

# print("tuple을 이용한 dict 생성 : ", dic02)

# 3. dict 함수 아용하여 dict 생성
dic03 = dict(name   = "seop",
            age     = 48,
            address = "seoul",
            birth   = "730910",
            gender  = True)


# print : dic01 :  <class 'dict'> {'name': 'seop', 'age': 48, 'address': 'seoul', 'birth': '730910', 'gender': True}

# print(dir(dic01))
# print("name" in dic01)   # print : True -> "name"이라는 키 존재 여부 확인
# print("seop" in dic01)   # print : Fasle -> 값의 존재 여부 확은 불가

# 요소 추가하는 방법
# 키/값 추가
# dic01["marriage"] = False
# print(dic01)

# 값 수정
# dic01["marriage"] = True
# print(dic01)

# 특정 키의 데이터 확인 : dic["key name"], dic.get("key name")
#print(dic01["birth"])

# 데이터 출력(key를 대소문자 다르게 입력한 경우의 반환값)
#print("dic03 - ", dic03["Name"])        # KeyError: 'Name'
#print("dic03 - ", dic03.get("Name"))    # dic03 -  None

#print("len - ", len(dic03))     # print : len -  5  -> key 갯수 반환

# dict_keys, dict_values, dict_items
# -> 반환값의 타입을 list로 형변환을 원할경우, list() 사용(데이터 이용할 때 list로 형변환하는 경우 많음)
# dict.keys() : key 목록 반환  <class 'dict_keys'>
# dict.values() : value 목록 반환  <class 'dict_values'>
# dict.itmes() : key와 value 목록 반환  <class 'dict_items'>
#print("dict_keys - ", dic03.keys(), type(dic03.keys()), list(dic03.keys()))
# print : dict_keys -  dict_keys(['name', 'age', 'address', 'birth', 'gender'])  <class 'dict_keys'>
# #                    ['name', 'age', 'address', 'birth', 'gender']

#print("dict_values - ", dic03.values(), type(dic03.values()), list(dic03.values()))
# print : dict_values -  dict_values(['seop', 48, 'seoul', '730910', True]) <class 'dict_values'>
#                        ['seop', 48, 'seoul', '730910', True]

#print("dict_items - ", dic03.items(), type(dic03.items()), list(dic03.items()))
# print : dict_items -  dict_items([('name', 'seop'), ('age', 48), ('address', 'seoul'), ('birth', '730910'), ('gender', True)]) <class 'dict_items'>
#                       [('name', 'seop'), ('age', 48), ('address', 'seoul'), ('birth', '730910'), ('gender', True)]

# dict의 키 가지고 와서 출력
# for key in dic03.keys() :
#     print("{0} : {1}".format(key, dic03[key]))
    #print("{0} : {1}".format(key, dic03.get(key)))  # 위, 아래 둘다 결과 동일

# value 가지고 와서 출력
# for value in dic03.values() :
#     print(value)

# tuple의 패킹과 언패킹
# 패킹 : tuple 선언
# 언패킹 : tuple 자료형의 데이터를 요소 하나씩 풀어서 다른 변수에 담음
#          tuple의 요소 수만큼의 변수가 선언되어야 함

t = ("foo", "bar", "baz", "qux")  # 패킹
#print(type(t))

(x1, x2, x3, x4) = t                                # 언패킹
#print(x1, x2, x3, x4)

(x1, x2, x3, x4) = ("foo", "bar", "baz", "qux")     # 언패킹 : ("foo", "bar", "baz", "qux")는 튜플형식의 데이터이므로 이 코드도 언패킹

#a, b , c = (0,1,2,3,4,5)  # 언패킹시, 좌측의 변수 갯수와 우측의 튜플 요소수가 다를 경우 오류 -> ValueError: too many values to unpack (expected 3)
# a, b , *c = (0,1,2,3,4,5)   # *변수 = 가변형(우측의 튜플의 값을 전달받음), **변수 = 가변형(우측의 dict의 값을 전달받음)
# print(a)    # 0
# print(b)    # 1
# print(c)    # [2, 3, 4, 5]

# a, *b , c = (0,1,2,3,4,5)
# print(a)    # 0
# print(b)    # [1, 2, 3, 4]
# print(c)    # 5

 # for (key, value) in dic03.items() :
 #     print("{0} : {1}".format(key, value))

# 삭제 : pop(), del
# del dic["key"]
# pop
del dic03["gender"]
print(dic03)

print("pop - ", dic03.pop("birth"))     #  마지막 꺼내서 출력 후 제거
print(dic03)

# dict 변수 제거 : dic.clear()
dic03.clear()
print(dic03)    # print : {}