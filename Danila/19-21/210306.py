def f(first, second, turn):
    if first*second>=541:
        if turn==2:
            return True
        else:
            return False
    if turn>4:
        return False
    else:
        if turn%2==0:
            return f(first+10, second, turn+1) and f(first*2, second, turn+1) and f(first, second+10, turn+1) and f(first, second*2, turn+1)
        else:
            return f(first+10, second, turn+1) or f(first*2, second, turn+1) or f(first, second+10, turn+1) or f(first, second*2, turn+1)
for S in range(1, 91):
    if f(6, S, 0):
        print(S)