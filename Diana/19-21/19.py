def f(first,turn):
    if first>=512:
        if turn==2:
            return True
        else:
            return False
    elif turn>2:
        return False
    else:
        if turn%2==0:
            return (f(first+2,turn+1)
                    and f(first+3,turn+1)
                    and f(first+4,turn+1)
                    and f(first+5,turn+1)
                    and f(first*2,turn+1))
        else:
            return (f(first + 2, turn + 1)
                    or f(first + 3, turn + 1)
                    or f(first + 4, turn + 1)
                    or f(first + 5, turn + 1)
                    or f(first * 2, turn + 1))
for s in range(1,512):
    if f(s,0):
        print(s)
