def f(first,turn):
    if first>=25:
        if turn == 2:
            return True
        else:
            return False
    if turn>3:
        return False
    if turn%2==0:#Петя
        return f(first+1,turn+1) and f(first*2,turn+1)
    else:#Ваня
        return f(first+1,turn+1) or f(first*2,turn+1)
for S in range(1,25):
    if f(S,0):
        print(S)