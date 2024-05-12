def f(first,second,turn):
    if first+second>=342:
        if turn == 3:
            return True
        else:
            return False
    if turn > 3:
        return False
    else:
        if turn%2==0:    #петр
            return (f(first+2,second,turn+1) or
                    f(first*5,second,turn+1) or
                    f(first,second+2,turn+1) or
                    f(first,second*5,turn+1) 
            )
        else:
            return (f(first+2,second,turn+1) and
                f(first*5,second,turn+1) and
                f(first,second+2,turn+1) and
                f(first,second*5,turn+1) 
            )
for S in range(1,325):
    if f(11,S,0):
        print(S)