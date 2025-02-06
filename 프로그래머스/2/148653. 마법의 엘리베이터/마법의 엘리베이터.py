def solution(storey):
    cnt = 0
    n = 10 
    
    while storey != 0:

        while storey % n != 0:
            a = min(abs(0 - storey % n), abs(n - storey % n))
            if a == 5: 
                if storey // n >= 5:
                    storey += a
                else:
                    storey -= a

            elif a == storey % n:
                storey -= a
            else:
                storey += a
            cnt += a // (n // 10)

        n *= 10
    
    return cnt