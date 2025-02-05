def f(first,second,turn):
    if first+second<=100:
        if turn==2:
            return True
        else:
            return False
    if turn>4:
        return False
    if turn%2!=0:
        return f(first-3,second-3,turn+1) or f(first//2,second,turn+1) or f(first,second//2,turn+1)
    else:
        return f(first-3,second-3,turn+1) or f(first//2,second,turn+1) or f(first,second//2,turn+1)
for S in range(53,1000):
    if f(48,S,0):
        print(S)