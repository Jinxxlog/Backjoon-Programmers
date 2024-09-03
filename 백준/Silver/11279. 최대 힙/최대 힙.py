import sys
import heapq
input = sys.stdin.readline

N = int(input())
res = []

for i in range(N):
    a = int(input())
    if a != 0:
        heapq.heappush(res, (-a, a))
    else:
        if res:
            print(heapq.heappop(res)[1])
        else: print(0)

