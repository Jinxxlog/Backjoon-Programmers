N = int(input())
A = list(map(int, input().split()))

if N == 1:
    print(A[0] ** 2)
else:
    A.sort()
    print(A[0] * A[-1])