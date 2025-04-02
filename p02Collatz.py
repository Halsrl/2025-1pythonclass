# 2025.4.2 파이썬수업 프로젝트 두번째
# 쿨라츠 추측, 또는 우박수
# 1부터 1000까지 숫자중,가장 많은 단계를 거쳐서 1로가는 수는 무엇인가?, 가장많은 단계는 몇단계인가
# 규칙: n이 짝수 -> n/2
#      n이 홀수 -> 3 * n + 1
#
# 예: 5 -> 16 -> 8 -> 4 -> 2 -> 1  (5단계)




n=5



# 단계의 갯수를 셀것
# n을 1부터 99까지 변화하면서, 각각의 단계쑤를 출력할 것
# 그중 가장 큰 수를 찾을 것

# 테스트
while n!= 1:
    if n % 2 ==1:
        n = 4* n + 1
    else:
        n = n/2
    print(n)


def collatz_steps(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

# 1부터 1000까지의 숫자 중에서 가장 많은 단계를 거친 숫자 찾기
max_steps = 0
max_number = 0

for i in range(1, 1001):
    steps = collatz_steps(i)
    if steps > max_steps:
        max_steps = steps
        max_number = i

print(f"가장 많은 단계를 거친 수는 {max_number}이고, 그 단계는 {max_steps}입니다.")