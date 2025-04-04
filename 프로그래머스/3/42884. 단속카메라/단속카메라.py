def solution(routes):
    routes.sort()
    
    aws = 1
    m = 30000
    
    for i, j in routes:
        if i > m:
            aws += 1
            m = j
        m = min(m, j)
    
    return aws