L = int(input())
M = list(map(ord, input()))

for i in range(L):
    M[i] = (M[i] - 96) * (31 ** i)

print(sum(M) % 1234567891)