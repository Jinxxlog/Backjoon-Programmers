import sys
def input(): return sys.stdin.readline().rstrip()

n = int(input())
st = list(map(int, [input() for i in range(n)]))
ch = []
res = []
cnt = 1

for i in st:
    while cnt <= i:
        ch.append(cnt)
        res.append('+')
        cnt += 1

    if ch[-1] == i:
        res.append('-')
        ch.pop()
    else:
        res.append('NO')
        break

if 'NO' in res:
    print('NO')
else:
    for i in res:
        print(i)
