# boolean : True, False 반환
# Python만의 boolean 특이한 케이스 : 세미 boolean
# - 0 = False, 1 = True(0이 아닌 값은 True)
# Or, |의 차이 :
#               A Or B일 경우 A가 True여도 B의 값까지 확인한 후 결과값 반환됨
#               A | B일 경우 A가 True일 때 B의 값 확인하지 않고 결과값 반환됨


a = 5
b = 0
print(a&b)              # bit 연산 + & 연산 결과 출력
print(bool(a&b))        # a = 0101 & b = 0000 -> result : 0(False)
print(bool(0))

print("bool(1,2,3): ", bool((1,2,3)))   # print : bool(1,2,3):  True

# 데이터가 있는 변수에 bool -> True
# 데이터가 없는 변수에 bool -> False
temp = {}
print("bool {} : ", bool((temp)))  # print : bool {} :  False

print("bool not", bool(not 0))      # 0이 아니면 True

trueFlag = True
falseFalg = False
print(int(trueFlag))    # print : 1
print(int(falseFalg))   # print : 0

print(trueFlag & falseFalg)
print(trueFlag | falseFalg)

print("and : ", trueFlag and falseFalg)
print("or : ", trueFlag or falseFalg)
print(not trueFlag)
