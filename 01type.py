# 2025.3.12
# 파이썬 수업 - 변수, 타입, 출력
# 타입 (형) - 정수 : int (integer)
#            실수 : float(floating point)
#            문자열: str(string)
#            논리값: bool (boolean)

title = "시간계산"
sec = 3700
min = sec/ 60
bigger = min > sec
print(sec, min, bigger)
print(type(title), type(sec), type(min), type(bigger))



# 사칙연산중에서 0으로 나누는 것은 혀용하지 않음
#print(3/0)


a= "True"
print("변수 a의 자료형은"  type(a))
a='3'
b=float(a)

print(b**int(a))

a='3.5'
b=4
print(a*b)