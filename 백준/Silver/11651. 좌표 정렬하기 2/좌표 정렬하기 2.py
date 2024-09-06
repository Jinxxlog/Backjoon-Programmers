import sys

N = int(input())
res = [0] * N

for i in range(N):
    res[i] = list(map(int, input().split()))

res.sort(key = lambda x: (x[1], x[0]))

for i in range (N):
    print(*res[i])