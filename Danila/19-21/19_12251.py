def f(first,turn):
    if first >= 301:
        if turn == 2:
            return 1
        else:
            return 0
    if turn>2:
        return 0
    else:
        if turn%2==0:#Ходит ПЕТЯ
            return f(first+3,turn+1) and f(first*5,turn+1)
        else:#Ходит ВАНЯ
            return f(first+3,turn+1) or f(first*5,turn+1)

for S in range (1,301):
    if f(S,0):
        print(S)