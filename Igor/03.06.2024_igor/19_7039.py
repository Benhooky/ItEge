def f(first,turn):
    if first == 42:
        if turn == 2:
            return True
        else:
            return False
    if first > 42:
        if turn%2!=0:
            return True
        else:
            return False
    if turn > 2:
        return False
    else:
        if turn%2==0:
            return (
                f(first+1,turn+1) and f(first+3,turn+1) and f(first+7,turn+1)
                )
        else:(
                f(first+1,turn+1) or f(first+3,turn+1) or f(first+7,turn+1)
                )
for S in range(1,42):
    S = 40
    if f(S,0):
        print(S)