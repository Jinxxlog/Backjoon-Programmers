def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)
    idxa = 0
    idxb = 0

    for i in range(len(A)):
        if B[idxb] > A[idxa]:
            idxa +=1
            idxb +=1
            answer +=1
        else:
            B.pop()
            idxa +=1


    return answer