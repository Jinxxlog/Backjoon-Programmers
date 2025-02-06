def solution(n):
    list1 = ['1', '2', '4']
    res = ''
    
    while n > 0:
        n -= 1
        res = list1[n%3] + res
        n //= 3
    
    return res