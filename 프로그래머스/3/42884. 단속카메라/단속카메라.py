def solution(routes):
    routes.sort()
    
    aws = 1
    now = 30000
    
    for i, j in routes:
        if i > now:
            aws += 1
            now = j
        now = min(now, j)
    
    return aws