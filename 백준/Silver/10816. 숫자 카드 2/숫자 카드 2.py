import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))
m = int(input())
res = list(map(int, input().split()))

cc = Counter(card)

print(' '.join(str(cc[x]) for x in res))