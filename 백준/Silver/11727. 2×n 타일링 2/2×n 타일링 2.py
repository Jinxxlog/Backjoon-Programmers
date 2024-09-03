N = int(input())
sq = [1 for _ in range(N+1)]

for i in range(2, N+1):
    sq[i] = (sq[i-1] + 2*sq[i-2])

print(sq[N] % 10007)