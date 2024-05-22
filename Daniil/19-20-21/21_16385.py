def f(first,turn):
    if first>=435:
        if turn == 2 or turn == 4:
            return True
        else:
            return False
    if turn>4:
        return False
    if turn%2==0:#Петя
        return f(first+5,turn+1) and f(first*3,turn+1)
    else:#Ваня
        return f(first+5,turn+1) or f(first*3,turn+1)
for S in range(1,435):
    if f(S,0):
        print(S)