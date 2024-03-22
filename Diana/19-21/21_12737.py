def f(first,second,turn):
    if first*second >= 385:
        if turn == 4 or turn ==2:
            return True
        else:
            return False
    elif turn>4:
        return False
    else:
        if turn%2==0:#Петя
            return f(first+5,second,turn+1) and f(first*2,second,turn+1) and f(first,second+5,turn+1) and f(first,second*2,turn+1)
        else:#Ваня
            return f(first+5,second,turn+1) or f(first*2,second,turn+1) or f(first,second+5,turn+1) or f(first,second*2,turn+1)
for S in range(1,55):
    if f(8,S,0):
        print(S)