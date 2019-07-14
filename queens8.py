def queen(A, row=0):
    if row == len(A):
        print(A)
        return 0
    for col in range(len(A)):
        A[row], flag = col, True
        for i in range(row):
            if A[i] == col or abs(col - A[i]) == row - i:
                flag = False
                break
        if flag:
            queen(A, row + 1)


queen([None] * 8)
