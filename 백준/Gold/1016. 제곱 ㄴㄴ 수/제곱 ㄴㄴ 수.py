n, m = map(int, input().split())

res = [True] * (m-n+1)

for i in range(2, int(m ** 0.5)+1):
    a = i ** 2
    st = max(a, (n+a-1) // a*a)
    
    for j in range(st, m+1, a):
        res[j-n] = False

print(sum(res))