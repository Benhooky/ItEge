def f(first,turn):
    if first>198:
        if turn==2:
            return True
        else:
            return False
    if turn>2:
        return False
    else:
        if turn%2==0:
            return (f(first +1,turn+1)
                    or f(first+5,turn+1)
                    or f(first*3,turn +1))
        else:return (f(first +1,turn+1)
                     or f(first+5,turn+1)
                     or f(first*3,turn +1))
for S in range(1,199):
    if f(S,0):
        print(S)
        break