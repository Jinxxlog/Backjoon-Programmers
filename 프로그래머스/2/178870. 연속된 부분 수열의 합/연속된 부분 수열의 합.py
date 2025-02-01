def solution(sequence, k):
    answer = []
    lst1 = []
    csum = 0
    L = 0

    for R in range(len(sequence)):
        csum += sequence[R]

        while csum > k and L <= R:
            csum -= sequence[L]
            L += 1

        if csum == k:
            lst1.extend([L, R])

    lenth = len(sequence) + 1
    for i in range(0, len(lst1), 2):
        a = lst1[i+1] - lst1[i]

        if a < lenth:
            lenth = a
            answer = lst1[i], lst1[i+1]
    
    return answer