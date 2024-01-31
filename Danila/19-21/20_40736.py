def f(first, turn, type):
    if first >= 34:
        if turn == 3:
            return 1
        else:
            return 0
    if turn>3:
        return 0
    else:
        if turn%2 == 0:
            if type == 1:
                return f(first+2, turn+1,2) or f(first*2, turn+1,3)
            elif type == 2:
                return f(first+1, turn+1, 1) or f(first*2, turn+1,3)
            elif type == 3:
                return f(first+1, turn+1, 1) or f(first+2, turn+1,2)
            else:
                return f(first+1, turn+1, 1) or f(first+2, turn+1,2) or f(first*2, turn+1,3)
        else:
            if type == 1:
                return f(first+2, turn+1,2) and f(first*2, turn+1,3)
            elif type == 2:
                return f(first+1, turn+1, 1) and f(first*2, turn+1,3)
            elif type == 3:
                return f(first+1, turn+1, 1) and f(first+2, turn+1,2)
            else:
                return f(first+1, turn+1, 1) and f(first+2, turn+1,2) and f(first*2, turn+1,3)
for S in range(1, 34):
    if f(S,0, 0):
        print(S)