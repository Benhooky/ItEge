def f(first,second,turn):
    if first+second>=21:
        if turn%2!=0 and turn!=1:
            return True
        else:
            return False
    if turn%2!=0: # Ваня
        return f(first+3,second,turn+1) and f(first,second+3,turn+1) and f(first*2,second,turn+1) and f(first,second*2,turn+1)
    else: # Петя
        return f(first+3,second,turn+1) or f(first,second+3,turn+1) or f(first*2,second,turn+1) or f(first,second*2,turn+1)

for S in range(1,20):
    if f(3,S,0):
        print(S)