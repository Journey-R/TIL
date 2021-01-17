str01 = "I am Python"
str02 = 'Python'
str03 = """"this is a 
multiline 
sample text"""
str03_2 = '''this is a 
multiline
sample text2'''

# db 쿼리 사용시 용이
qr = """
select *
from   emp
wherer deptno = {no}
order by eno desc
"""

print(qr)

seqText = "Talk is cheap. Show me the code"
print(seqText)

# slicing : 하나의 문자열을 위치별 인덱싱 가능
# 문자열 index : 0~-1(0부터 시작하고 가장 마지막 글자는 -1 혹은 글자 길이 -1)
print(seqText[3]) # seqText = "Talk is cheap. Show me the code" -> print : k
print(seqText[-1]) # [-n] : 역순으로 위치 시작하며 0이 아닌 1부터 시작
print(seqText[0:3]) # 마지막 인덱스 : 마지막 인덱스 -1, 0:3의 경우 0~2(3-1)번째 글자까지 추출

str_slicing = "Nice Python"
print(str_slicing[0:4]) # Nice만 추출
print(str_slicing[5:])  # Python만 추출(마지막 인덱스 미지정시 마지막 글자까지)
print(str_slicing[0:])  # 전체 데이터 추출
print(str_slicing[:])
print(str_slicing[-6:]) # -6번째 인덱스에서부터 오른쪽 전체 데이터 추출

# [첫번째 인덱스 : 마지막 인덱스 : step(몇칸씩 띄울지)]
# step = -n : 뒤에서부터 n개씩
print(str_slicing[0:6:2]) # print : Nc
print(str_slicing[0:len(str_slicing):2])   # print : Nc yhn
print(str_slicing[::2])
print(str_slicing[::-1])

# len() : 길이 정보 반환
# 길이 정보는 1부터 시작, index는 0부터 시작
print(len(str_slicing))

# 아래의 문자열 중 홀만 출력
string = "홀짝홀짝홀짝홀짝"
print(string[::2])
print(string[0:len(string):2])

# 아래의 문자열을 거꾸로 뒤집어서 출력
string = "PYTHON"
print(string[::-1])

# 문자열 변수.capitalize() : 첫문자만 대문자로 변환
string = "python"
print("Caplitalize : ", string.capitalize())

str01 = "phone"
print("Caplitalize : ", str01.capitalize())

#  문자열 변수.replace("원본 문자열에서 바꿀 글자", "치환할 글자") : 문자열 치환
# -문자를 공백으로 치환하고 싶다면?
phone_number = "010-4603-2283"
print("replace : ", phone_number.replace("-", " "))

# 아래의 문자열에서 소문자 'a'를 대문자 'A'로 변경한다면
string = "abcdefe2a345a345a"
print("replace : ", string.replace("a", "A"))

# 문자열.split("쪼갤 구분자") : 글자 쪼개기(반환 값 데이터 타입 : list)
# 아래의 문자열에서 도메인만 출력한다면
url = "http://naver.com"
print("split : ", url.split("."))       # '.' 기준으로 쪼개면 2개의 문자열이 나옴
print("split : ", url.split(".")[-1])   # 그중에 뒤에서 첫번째 데이터 추출

string = "삼성전자/LG/Naver/Google"
interest = string.split("/")
print(interest, type(interest))

# 문자열 변수.strip() : 좌우 공백 제거
# 문자열 변수.rstrip() : 오른쪽 공백 제거
# 문자열 변수.lstrip() : 왼쪽 공백 제거
data = "    삼성전자     "
print(data.strip())   # print : '삼성전자'
print(data.rstrip())  # print : '    삼성전자'
print(data.lstrip())  # print : '삼성전자     '

# 문자열.upper() : 대문자로 변환
# 문자열.lower() : 소문자로 변환
ticker = "btc_krw"
upper = ticker.upper()
lower = upper.lower()
print("upper : ", upper, ", lower : ", lower )

# 문자열.endswith() : 마지막에 어떠한 문자열로 끝나는가(반환값 bool)
file_name = "report.xls"
print(file_name.endswith((".xls", ".xlsx")))

# in : 특정 문자열 포함 여부 (반환 값 데이터 타입 : bool)
#      "문자열" in 문자열(포함 여부 검증)
# not in : 특정 문자열 미포함 여부 (반환 값 데이터 타입 : bool)
#         "문자열" not in 문자열(미포함 여부 검증)
myStr = "This is a sample Text"
print("sample" in myStr)
print("sample" not in myStr)
print("text" not in myStr)
print("this" in myStr.lower())  # myStr.lower()한 데이터 중에 "this"의 포함 여부 -> print : True

brand_name = "cocacola"
result = len(brand_name)
print(result)

# 문자열.count("검색문자열") : 검색 문자열이 몇개 있는지 갯수 카운트
result = brand_name.count("c")
print(result)

# 문자열.find("검색 문자열") : 검색 문자열의 첫번째 찾아서 위치 반환
# 존재하지 않는 문자열일 경우 : -1 반환
result = brand_name.find("o")
print(result)

result = brand_name.find("f")   # -1 반환
print(result)

# 문자열.index("검색 문자열") : 검색 문자열의 첫번째 찾아서 위치 반환
# 존재하지 않는 문자열일 경우 에러 발생: ValueError: substring not found
result = brand_name.index("a")
print(result)

#result = brand_name.index("f")
print(result)

# 문자 -> 아스키 코드 번호 반환 : ord("문자")
# 아스키 코드 -> 문자 반환 : chr(아스키코드 값)
print(ord("A"))
print(chr(65))