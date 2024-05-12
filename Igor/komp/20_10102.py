def f(first,turn):
    if first >= 129:
        if turn == 3:
            return True
        else:
            return False
    if turn > 3:
        return False
    else:
        if turn%2==0: #peta
            return (f(first + 1 ,turn + 1)
                or f(first * 2, turn + 1))
        else:
            return (f(first + 1 ,turn + 1)
                and f(first * 2, turn + 1))
for S in range(1,128):
    if f(S,0):
        print(S)