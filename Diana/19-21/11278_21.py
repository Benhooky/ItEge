def f(first,second,turn):
    if first+second>=449:
        if turn==2 or turn==4:
            return True
        else: return False
    elif turn>4:
        return False
    else:
        if turn%2==0:
            return( f(first+1,second,turn+1)
                    and f(first*2,second,turn+1)
                    and f(first,second+1,turn+1)
                    and f(first,second*2,turn+1))
        else:
            return (f(first + 1, second, turn + 1)
                    or f(first * 2, second, turn + 1)
                    or f(first, second + 1, turn + 1)
                    or f(first, second * 2, turn + 1))

for s in range(1,436):
    if f(11,s,0) :
        print(s)
        break
