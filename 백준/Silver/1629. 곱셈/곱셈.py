import sys

a, b, c = map(int, sys.stdin.readline().split())

res = 1

while b > 0: #b가 0보다 클 때
    if b % 2 != 0: # b가 홀수일 때만
        res = (res * a) % c # 현재값에 a를 곱하고 c로 나눈 나머지를 저장

    b = b // 2  # b를 절반으로 감소
    a = (a * a) % c # a 제곱 -> c로 나눈 나머지 저장

print(res)