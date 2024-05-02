def f(first,second,turn):
    if 70<=first*second:#признак конца игры
        if turn == 2 and first*second<=110:
            return True
        else:
            return False
    if turn > 2:
        return False
    if turn%2 == 0:#Снегурочка
        return f(first+1,second,turn+1) or f(first*2,second,turn+1)  or f(first,second*2,turn+1) or f(first,second+1,turn+1)
    else:#Дед мороз
        return f(first+1,second,turn+1) or f(first*2,second,turn+1)  or f(first,second*2,turn+1) or f(first,second+1,turn+1)
for  S in range(1,66):
    if f(5,S,0):
        print(S)