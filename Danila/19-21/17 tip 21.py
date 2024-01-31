def f(first, turn):
    if first >= 52:
        if turn == 2 or turn == 4:
            return 1
        else:
            return 0
    if turn>4:
        return 0
    else:
        if turn%2 == 0:
            return f(first+1, turn+1) and f(first+10, turn+1)
        else:
            return f(first+1, turn+1) or f(first+10, turn+1)
for S in range(1, 52):
    if f(S,0):
        print(S)