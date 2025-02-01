def solution(board):
    a = (len(board))
    b = (len(board[0]))

    for i in range(1, a):
        for j in range(1, b):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1


    lst = []
    for i in range(a):
        lst.append(max(board[i]))

    return max(lst) ** 2