N, M = map(int, input().split())
site = {}

for i in range(N):
    A, B = (input().split())
    site[A] = B
    site[B] = A

for i in range(M):
        print(site[input()])