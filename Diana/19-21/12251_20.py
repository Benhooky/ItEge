def f(first,turn):
    if first>=301:
        if turn==3:
            return True
        else: return False
    elif turn>3:
        return False
    else:
        if turn%2==0:
            return(f(first+3,turn+1) or f(first*5,turn+1))
        else:return(f(first+3,turn+1) and f(first*5,turn+1))
for s in range(301):
    if f(s,0):
        print(s)

