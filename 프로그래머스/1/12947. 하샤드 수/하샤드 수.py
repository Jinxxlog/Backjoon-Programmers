def solution(x):
    ha = sum(map(int, str(x)))

    if x % ha == 0:
        answer = True
    else:
        answer = False
    
    return answer

