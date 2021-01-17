# tuple
# list와 비교할 수 있어야 함
# list와 공통점 : 순서 있음, 중복 허용,
# list와 차이점 : 추가/수정/삭제 불가 -> 읽기 전용
# ()로 변수 선언

# tuple 생성
my_tuple = ()
movie_rank = ("반도", "강철비2", "아이언맨")
test_tuple = (1)                # 요소가 1개일 때는 해당 요소의 데이터타입이 요소의 데이터 타입
print(type(test_tuple))         # print : <class 'int'>

test_tuple2 = (1,)              #(1,) : 요소가 1여도 ','가 있어야 튜플
print(type(test_tuple2))        # print : <class 'tuple'>

# () 생략 가능
test_tuple = 1,2,3,4,5
print(test_tuple, type(test_tuple))     # print : (1, 2, 3, 4, 5) <class 'tuple'>

multi_tuple = (100, 1000, "Ace", "Base", "Captine")
print(multi_tuple, type(multi_tuple))
print()

# indexing 가능
print(">>>>>>>>>>>> 튜플 인덱싱")
print(multi_tuple[0])
print(multi_tuple[-1])
print(multi_tuple[0]+multi_tuple[1])                # 인덱스의 값으로 산술연산
print(multi_tuple[2:], type(multi_tuple[2:]))       # 'ACE'~'Captine'까지 출력

# tuple -> list 형변환 : list(tuple 데이터)
# (tuple은 readonly여서 list로 형변환해서 데이터 조작)
list = list(multi_tuple[2:])
print(type(list))       # print : <class 'list'>

# list -> tuple 형변환 : tuple(list 데이터)
casting_tuple = tuple(list)
print(type(casting_tuple))          # <class 'tuple'>

# 1~100 정수 중 짝수만 저장된 튜플 생성
tuple = tuple(range(2, 100, 2))
print(tuple)


