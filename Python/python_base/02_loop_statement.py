# python 반복문
# for, while
# for index in <collection> :
# -> for each와 비슷하게 사용되며, index는 첨자이자 collection의 값이다.
# - collection : list, dict, str, range()의 length
# range(start index, stop length, step) : parameter가 1개일 경우, 0~stop-1까지

# strValue = "abcdefg"
#
# for i in strValue :
#     print(i)          # index는 첨자이자 collection의 값이다.
#
# for i in range(2, 11, 2) :
#     print(i, end = " ")

# scores = []
#
# for i in range(5) :
#     scores.append(int(input("성적 입력 : ")))

# print(scores)

# for i in scores :
#     print(i)

# for i in range(len(scores)):
#     print(scores[i], "\t", end = " ")

# 입력받은 성적의 총합과 평균을 구하세요
# print("sum : {}, mean : {}".format(sum(scores), (sum(scores)/len(scores))))


# 리스트 자료형에 들어 있는 값별 개수를 세어보자
# cnt_list = [1,3,5,3,2,1,5,5,3,3,2,2,1,3,3,3,2,4,1,"", "", "",""]
#
# freq = {}
# for i in cnt_list :
#     print("i : {}, type(i) : {}".format(i, type(i)))
#     if i in freq :
#         freq[i] += 1
#     else :
#         freq[i] = 1
#
# print(freq)


# 단어의 빈도수
# word_vec = ["corona", "corona", "corona", "love", "word", "bigdata", "bigdata", "word", "data", "data", "data", "jslim", "seop", "seop", "seop"]
# word_dict = {}
#
# for i in word_vec :
#     if i in word_dict :
#         word_dict[i] += 1
#     else :
#         word_dict[i] = 1
#
# print(word_dict)

# 1~1000 합
# range_sum = 0
#
# for value in range(1, 1001) :
#     range_sum += value
#
# print(range_sum)

# 구구단의 3단 출력
# dan = 3
# for i in range(1,10) :
#     print("3 * {} = {}".format(i, 3*i))


# 구구단의 3단 중 홀수번째만 출력
# dan = 3
# for i in range(1,10, 2) :
#     print("3 * {} = {}".format(i, 3*i))

# list가 tuple 담을 때(dict형 처럼 사용하는 예)
# my_list = [("name",2),("age",4),("gender",6)]
#
# # key와 value 출력
# for(key, value) in my_list :
#     print("key : {}, value : {}".format(key, value))
#
# temp_list = list(range(1,10))
# print(temp_list)

# list의 값을 꺼내서 list 생성
# score01 = [idx for idx in temp_list]                # list의 값 꺼내서 list 생성
# score02 = [idx *3 for idx in temp_list]             # list의 값 꺼내서 idx *3 연산한 결과를 list로 생성
# score03 = [idx *3 for idx in temp_list if idx % 2 == 0]     # list의 값을 꺼내서 idx*3 연산 결과에 조건에 부합하는 값만 list로 생성
# # 순서 : for -> 연산 -> if
# print("score01 : {}".format(score01))
# print("score02 : {}".format(score02))
# print("score03 : {}".format(score03))

# 올림픽은 4년마다 개최, 2000~2050년 사이의 올림픽 개최하는 년 반환
# olympic_list = []
# for i in range(2000, 2051, 4) :
#     olympic_list.append(i)
#
# print("올림픽 개최 년도 : {}".format(olympic_list))

# 아래 리스트에서 20보다 작은 3의 배수 출력
# list = [12, 21, 12, 14, 30, 38, 34, 18]
#
# for i in list :
#     if (i < 20) & (i % 3 == 0) :
#         print(i, end = " ")


# 아래 리스트에서 세글자 이상의 문자를 출력
# list = ["I", "am", "study", "python", "language", "!"]
# for i in list :
#     if  len(i) >= 3 :
#         print(i, end = " ")

# 아래 리스트에서 대문자만 화면에 출력
# list = ["I", "A", "study", "PYTHON", "JSLIM", "for", "if", "!"]
#
# for i in list :
#     if i.isupper() == True :
#         print(i, end = " ")


# 아래 리스트에서 첫글자를 대문자로 변경 출력
# list = ["dog", "cat", "pig", "parrot", "horse"]
# for i in list :
#     #print(i[0].upper() + i [1:], end = " ")   # 내가 쓴 코드
#     print(i.capitalize(), end = " ")            # capitalize() : 첫글자만 대문자로 변환


# 아래 리스트에서 파일 확장자 제거하고 파일 이름만
# list = ["greeting.py", "ex01.py", "intro.hwp", "bigdata.doc"]
#
# for i in list :
#     print((i.split("."))[0], end = " ")


# 문자열 loop
# word = "Handsome"
#
# for i in word :
#     if  i == word[len(word)-1] :
#         print("word -", i)
#     else :
#         print("word -", i, end=", ")

#
# my_dict = {"name" : "jslim",
#            "age" : 48,
#            "city" : "seoul"}
#
# cnt = 1
# for key in my_dict.keys():
#     if  (cnt == len(my_dict.keys())) :
#         print(key)
#     else :
#         print(key, end = ", ")
#     cnt += 1

# 전체 대문자로 출력
# fruit_name = "FineApplE"
#
# # upper() 활용
# print(fruit_name.upper())
#
# # fot loop 활용
# for name in fruit_name :
#     if name.isupper() == False :
#         print(name.upper(), end = "")
#     else :
#         print(name, end = "")

# break, continue
# numbers = [14, 3, 6, 17, 34, 25]

# for~else : for 내부 조건식이 만족하지 않을 경우 else 실행됨
# for i in numbers:
#     if i == 100 :
#         print(i, "break")
#         break
# else :
#     print("not found")

# for i in numbers:
#     if i == 17 :
#         continue
#         print(i)            # 출력되지 않음
#     else :
#         print(i)
#


# 구구단(5단 제외)
# for i in range(2,10) :
#     if  i == 5 :
#         continue
#     else :
#         print("-------------", i, "단-------------")
#         for j in range(1, 10) :
#           #  print("{} * {} = {}".format(i, j, i*j))
#             print("{} * {} = {}".format(i,j,i*j), end = "\t")
#
#     print()


string = """
저는 파이썬 강의 중인 임섭순입니다.
주소는 광주광역시입니다.
나이는 숫자에 불과하지만 성인병이 있네요.
"""

# \ 안쓰면 오류
string = \
"""
저는 파이썬 강의 중인 임섭순입니다.
주소는 광주광역시입니다.
나이는 숫자에 불과하지만 성인병이 있네요.
"""



# append(value), insert(index, value)

string = \
"""
저는 파이썬 강의 중인 임섭순입니다.
주소는 광주광역시입니다.
나이는 숫자에 불과하지만 성인병이 있네요.
"""
# sentences = []
# words = []
#
# # 위의 string을 문장(. 기준으로)과 단어(공백별로)별로 list에 담기
#
# for s in string.split("\n") :
#     if  s == "" :
#         continue
#     else :
#         sentences.append(s)             # 문장 list에 담기
#         for s in sentences:
#             for w in s.split(" "):
#                 words.append(w, )         # 단어 list에 담기
#
#
# print(len(sentences), " : ", sentences)
# print(len(words), " : ", words)


# 실습 : 분류 정확도 확인
# answer : 정답, predict : 예측
# answer  = [1,0,2,1,0]
# predict = [1,0,2,0,0]
# count = 0
#
# # 내가 짠 코드
# for i in range(len(answer)) :
#     if answer[i] == predict[i] :
#         count += 1
#
# print()
# print("정확한 갯수 : {}, 정확도 : {}".format(count, (count / len(answer) * 100)))
#
# # 쌤이 짠 코드
# acc = 0
# for i in range(len(answer)) :
#     fit = answer[i] == predict[i]       # 연산하지 않아서 fit을 외부에서 선언하지 않아도 됨
#     acc += int(fit) * 20                # True = 1, False = 0 // 20 = len(answer) / 100
#
# print("정확도 : ", acc)

# enumerate(collection) : index, value 형식으로 반환
# 반복문을 사용할 때 몇 번째 반복문인지 확인이 필요하다면
# 인덱스 번호와 컬렉션 요소를 확인할 수 있다.

# list = ["SQL", "R", "TEXT-MINING", "DATA-MINING", "PYTHON"]
#
# # for value in list :
# #     print(value)
#
# for idx, value in enumerate(list) :         # idx = index, value = value
#     print("index : {}, value : {}".format(idx, value))


# count()를 활용한 단어의 빈도수 체크
# word_vec = ("corona", "corona", "corona", "love", "word", "bigdata", "bigdata", "word", "data", "data", "data", "jslim", "seop", "seop", "seop")
# freq = {}
#
# for i in word_vec :
#     freq[i] = word_vec.count(i)
#
# print(freq)
#
# word_vec = ["corona", "corona", "corona", "love", "word", "bigdata", "bigdata", "word", "data", "data", "data", "jslim", "seop", "seop", "seop"]
# freq = {}
#
# for i in word_vec :
#     freq[i] = word_vec.count(i)
#
# print(freq)




# while(표현식)
#    satement(증감식 포함)
# python에서는 허용되지 않는 증감식 : --, ++
# python에서 허용되는 증감식 : +=, -=

# n = 5
# while n > 0 :
#     print(n)
#     n -= 1

# a = ["foo", "bar", "baz"]
# while a :               # 데이터가 있을 때 = True, 비어있을 때 = False
#     print(a.pop())      # pop() 마지막 데이터 꺼내서 반환 후 제거
#


# while 이용하여 1~100까지의 합,
# 5배수의 합,
# 3의 배수이면서 5의 배수가 아닌 수의 합
# num = 1
# sum1to100 = 0
# sum5 = 0
# sum3_not5 = 0
#
# while num < 101 :
#     sum1to100 += num
#     if num % 5 == 0 :
#         sum5 += num
#     elif (num % 3 == 0) :
#         sum3_not5 += num
#     num += 1
#
# print("1~100의합 : {},   5의 배수의 합 : {},   3의 배수 & 5의 배수가 아닌 수의 합 : {}".format(sum1to100, sum5, sum3_not5))


# while~else
cnt = 10
while cnt > 0 :
    if cnt == 5 :   # 조건에 맞는 값이 있으므로 else 코드 실행되지 않음
    #if cnt == 11 :  # 조건에 맞는 값이 없으므로 else 코드 실행됨
        break
    cnt -= 1
else :
    print("while~else")


