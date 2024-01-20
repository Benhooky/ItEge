def f(first, turn):
    if first < 117:
        if turn == 3:
            return 1
        else:
            return 0
    if turn>3:
        return 0
    else:
        if turn%2 == 0:
            return f(first-7, turn+1) or f(first//3, turn+1)
        else:
            return f(first-7, turn+1) and f(first//3, turn+1)
for S in range(117, 10001):
    if f(S,0):
        print(S)