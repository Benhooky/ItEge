def f(first, second, turn):
    if first+second>=342:
        if turn == 2:
            return 1
        else:
            return 0
    if turn>2:
        return 0
    else:
        if turn%2 == 0:
            return f(first+2, second, turn+1) or f(first*5, second, turn+1) or f(first, second+2, turn+1) or f(first, second*5, turn+1)
        else:
            return f(first+2, second, turn+1) or f(first*5, second, turn+1) or f(first, second+2, turn+1) or f(first, second*5, turn+1)
for S in range(1, 326):
    if f(11, S, 0):
        print(S)
        break