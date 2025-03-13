def solution(n, s):
    answer = []
    
    share, remainder = s//n, s%n
    
    for i in range(n-remainder):
        answer.append(share)
        
    for i in range(remainder):
        answer.append(share+1)
        
    
    
    return [-1] if 0 in answer else answer