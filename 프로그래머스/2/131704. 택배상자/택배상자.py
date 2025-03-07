from collections import deque

def solution(order):
    maincon = deque([n for n in range(1, len(order)+1)])
    subcon = deque([])
    cnt = 0

    for i in order:
        while maincon and maincon[0] <= i:
            subcon.append(maincon.popleft())

        if subcon and subcon[-1] == i:
            subcon.pop()
            cnt += 1
        else:
            break    
    
    return cnt