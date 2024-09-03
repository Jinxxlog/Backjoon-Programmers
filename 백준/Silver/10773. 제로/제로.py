K = int(input())
res = []

for i in range(K):
    n = int(input())

    if n != 0:
        res.append(n)
    elif n == 0:
        res.pop()

print(sum(res))