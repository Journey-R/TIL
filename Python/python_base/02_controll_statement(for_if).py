# python의 제어문

# python 사용자 입력 함수 : input()
# input 받은 데이터의 type : 문자열(default)

# name = input("Input Your Name : ")
# grade = input("Input Your Grade : ")
# company = input("Input Your Company Name : ")
# print("Name : {}, Grade : {}, Company : {}".format(name, grade, company))

# score = input("Input your score : ")
# print(score, type(score))       # print : 100 <class 'str'>
#
# score = int(input("Input your score : "))
# print(score + 100, type(score))     # 200 <class 'int'>

# python의 제어문
# 조건식 : if, if~else, if~elif~else
# bool -> True : 0이 아닌 수,
#                문자, 데이터가 있는 list/tuple/dict
# bool -> Fasle : 0,
#                 데이터가 없는 list/tuple/dict

# if
# if  True :
#     print("True")
#
# if not False :
#     print("not False")
#
# if 0 == False :
#     print("Bad")

# if~else
# if False :
#     print("Bad")
# else :
#     print("Good")

# 아래의 값이 3의 배수인지 5의 배수인지, 둘다 아닌지 검증
# number = 15
#
# if  (number % 3 == 0) & (number % 5 == 0) :
#     print("3과 5의 배수 : {}".format(number))
# elif  number % 3 == 0 :
#     print("3의 배수 : {}".format(number))
# elif number % 5 == 0 :
#     print("5의 배수 : {}".format(number))
# else :
#     print("3, 5의 배수 아님 : {}".format(number))

# 윤년의 조건
# 1. 4의 배수, 100의 배수 X
# 2. 400의 배수

# if구문을 사용하여 연도, 월 입력받아서 월의 마지막 일을 출력
# 내가 짠 코드-----------------------------------------------------
# lastday = [28, 29, 30, 31, -1]
# yeartype = ["윤년", "평년"]
#
# input_year = int(input("Input year : "))
# input_month = int(input("Input month : "))
#
# # 1. 2월 - 윤년, 평년
# lastday_result = 0
# yeartype_result = ""
#
# # 평년 윤년
# if ((input_year % 4 == 0) & (input_year % 100 != 0)) | (input_year % 400 == 0):
#     yeartype_result = yeartype[0]
# else :
#     yeartype_result = yeartype[1]
#
# # 마지막 일
# # 2월
# if  (input_month < 0) | (input_month > 12) :
#   lastday_result =  lastday[4]
#
# elif input_month == 2 :
#     # 윤년
#     if yeartype_result == yeartype[0] :
#         lastday_result = lastday[1]
#     # 평년
#     else :
#         lastday_result = lastday[0]
# elif (input_month == 7) | (input_month == 8) :
#     lastday_result = lastday[3]
# elif input_month < 7 :
#     if input_month % 2 == 0 :
#         lastday_result = lastday[2]
#     else :
#         lastday_result = lastday[3]
# elif (input_month == 7) | (input_month == 8) :
#     lastday_result = lastday[3]
# elif input_month > 8 :
#     if input_month % 2 == 0 :
#         lastday_result = lastday[3]
#     else :
#         lastday_result = lastday[2]
#
# if lastday_result == -1 :
#     print("입력한 월이 정상 범위 밖에 있습니다. : 입력 월 {}".format(input_month))
# else :
#     print("{}년 {}월의 마지막 일 : {}({})".format(input_year, input_month, lastday_result, yeartype_result))


# 다른 학생이 짠 코드-----------------------------------------------------
# year_month      = [31,28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# leap_year_month = [31,29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
# if((input_year % 4 == 0) & (input_year % 100 != 0)) | (input_year % 400 == 0):
#     print("{}년 {}월의 마지막 일 : {}(윤년)".format(input_year, input_month, leap_year_month[input_month-1]))
# else :
#     print("{}년 {}월의 마지막 일 : {}(평년)".format(input_year, input_month, year_month[input_month - 1]))
#

# 관련 라이브러리 참조한 결과(개인적으로 찾아봄)-------------------------------------------
# import calendar
# print (calendar.monthrange(input_year, input_month)[1])

'''
# calendar.monthrange 소스코드 확인(개인적으로 찾아봄)----------------------------------
link : https://github.com/python/cpython/blob/3.8/Lib/calendar.py

def monthrange(year, month):
    """Return weekday (0-6 ~ Mon-Sun) and number of days (28-31) for
       year, month."""
    if not 1 <= month <= 12:
        raise IllegalMonthError(month)
    day1 = weekday(year, month, 1)
    ndays = mdays[month] + (month == February and isleap(year))
    return day1, ndays
'''

# 중첩 조건문
# A학점이면서 95 이상의 점수면 장학금 100%
# A학점이면서 90 이상의 점수면 장학금 90%
# A학점이 아니면 장학금 50%

# grade = input("학점 : ")
# total = int(input("점수 : "))
#
# jhg = 0
# if grade.upper() == "A" :
#     if total >= 95 :
#         jhg = 100
#     elif total >= 90 :
#         jhg = 90
# else:
#     jhg = 50
#
# print("장학금 : {}%".format(jhg))
#
# area = ["seoul", "busan", "jeju"]
# region = "suwon"
#
# if region in area:
#     pass
# else:
#     print("{} 지역은 포함되지 않습니다.".format(region))
#

# myDict = {"seoul" : 100,
#           "gwangju" : 200}
# region = "busan"
#
# if region in myDict :
#     print("키 값이 dict 안에 있습니다.")
# else :
#     print("키 값이 dict 안에 없습니다.")


# if~else와 삼항연산자
# num = 9
# result  = 0
# if num >= 5:
#     result = num *2
# else:
#     result = num +2
#
# print(result)
#
# # 삼항연산자 (위의 코드 삼항연산자로 사용 가능)
# # if가 true일 때 if(조건) else if가 false일 때
# result = num * 2 if(num >=5) else num + 2

# 참, 거짓 판별 종류
# city = ""       # 빈데이터 = false
# city2 = " "     # 데이터가 있으면 = true(공백도 문자로 인식)
# if city :
#     print(city)
# else :
#     print("Please enter your city")
#
# money = 1
# if money :
#     print("Buy")
# else :
#     print("Hungry")






