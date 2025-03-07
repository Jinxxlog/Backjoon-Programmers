from collections import deque

def solution(x, y, n):
    if x == y:
        return 0
    
    q = deque([(x, 0)])
    
    visit = {10}
    
    
    while q:
        val, cnt = q.popleft()
    
        for i in (val+n, val*2, val*3):
            if i == y:
                return cnt + 1
            elif i < y and i not in visit:
                visit.add(i)
                q.append((i, cnt+1))
    
    return -1