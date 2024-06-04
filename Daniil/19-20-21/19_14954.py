def f(first,second,third,turn):
    if first>=20 or second>=20 or third>=20 or first+second+third>=25:
        if turn == 2:
            return True
        else:
            return False
    if turn>2:
        return False
    if turn%2==0:#Петя
        return f(first*2,second,third,turn+1) and f(first+2,second,third,turn+1) and f(first,second*2,third,turn+1) and f(first,second+2,third,turn+1) and f(first,second,third*2,turn+1) and f(first,second,third+2,turn+1)
    else:#Ваня
        return f(first*2,second,third,turn+1) or f(first+2,second,third,turn+1) or f(first,second*2,third,turn+1) or f(first,second+2,third,turn+1) or f(first,second,third*2,turn+1) or f(first,second,third+2,turn+1)

for S in range(1,20):
    if f(2,3,S,0):
        print(S)