import sys
import heapq
input = sys.stdin.readline

N = int(input())
q = []


for i in range(N):
    a = int(input())
    if a != 0:
        heapq.heappush(q, a)
    else:
        if q:
            print(heapq.heappop(q))
        else: print(0)
