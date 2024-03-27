def f(first,turn):
    if first>198:
        if turn==3:
            return True
        else:
            return False
    elif turn>3:
        return False
    else:
        if turn%2==0:
            return (f(first +1,turn+1)
                    or f(first+5,turn+1)
                    or f(first*3,turn +1))
        else:
            return (f(first +1,turn+1)
                     and f(first+5,turn+1)
                     and f(first*3,turn +1))
cnt=0
for s in range(1,199):
    if f(s,0) and cnt<2:
        cnt+=1
        print(s)