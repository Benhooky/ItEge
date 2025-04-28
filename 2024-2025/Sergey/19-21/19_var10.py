def f(first,second,turn):
    if first+second<=69:
        if turn==2:
            return True
        else:
            return False
    if turn>4:
        return False
    if turn%2==0: # Петя 
        return f(first//2,second,turn+1) and f(first,second//2,turn+1) and f(first-5,second+2,turn+1) and f(first+2,second-5,turn+1)
    if turn%2!=0: # Ваня
        return f(first//2,second,turn+1) or f(first,second//2,turn+1) or f(first-5,second+2,turn+1) or f(first+2,second-5,turn+1)
for S in range(51,1000):
    if f(35,S,0):
        print(S)