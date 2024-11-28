import sys
def input(): return sys.stdin.readline().rstrip()

n = int(input())
st = list(map(int, [input() for i in range(n)]))
ch = []
res = []
cnt = 0

for i in st:
    while cnt < i:
        res.append('+')
        cnt += 1

    if i < cnt and i+1 not in ch:
        res.append('NO')
        break

    res.append('-')
    ch.append(i)

if 'NO' in res:
    print('NO')
else:
    for i in res:
        print(i)
