from xml. sax.handler import property_declaration_handler

# 2024.3.4. 이용희교수님과 파이썬 첫 수업
# 1주차

print("안녕하세요, \n만나서 \t\t반갑습니다")
print("오늘은", "화요일")
print(5/3)

s = "열심히 해보겠습니다."
print(s)

import sys
print(sys.version)

a = int(10.999989)   # floor 버림, ceiling 올림, round 반올림
b = float(10.3)
c = str(10.3)
print(type(a), type(b), type(c))
print(a)

sec1  = 1300; sec2 =120
seca = sec1 + sec2
secs = sec1 - sec2
secm = sec1 * sec2
secd = sec1 / sec2
secq = sec1 // sec2
seqr = sec1 % sec2
print(f'{seca=}, {secs=}, {secm=}, {secd=}, {secq=}, {seqr=}') # f string

# 화시를 섭씨로 바꿈
# tc =  (tf - 21) * 5/9
# tf = (tc X 9/5) + 32
tf = 100
tc= ( tf-21) * 5/9
print(f'{tf=} ===> {tc=}')

print(2 ** 3, 2 ** (1/2), 2 ** (-1/2))


