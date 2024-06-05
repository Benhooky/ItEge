def f(first,second,turn):
    if first+second<=36:
        if turn == 2 or turn == 4:
            return True
        else:
            return False
    if turn>4:
        return False
    else:
        if turn%2==0:    
            return (f(first-3,second,turn+1) 
                    and f(first//2,second,turn+1)
                    and f(first,second-3,turn+1) 
                    and f(first,second//2,turn+1)
                    )
        else:    
            return (f(first-3,second,turn+1) 
                    or f(first//2,second,turn+1)
                    or f(first,second-3,turn+1) 
                    or f(first,second//2,turn+1)
                    )
for S in range(16,1000):
    if f(20,S,0):
        print(S)
        break