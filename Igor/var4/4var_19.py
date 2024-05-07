def f(first,turn):
    if first>=105:
        if turn == 2:
            return True
        else:
            return False
    if turn > 2:
        return False
    else:
        if turn%2==0: #P
            return (
                f(first+1,turn+1) and
                f(first+5,turn+1) and 
                f(first*4,turn+1) 
            )
        else: #V
            return (
                f(first+1,turn+1) or
                f(first+5,turn+1) or 
                f(first*4,turn+1) 
            )
for S in range(1,105):
    if f(S,0):
        print(S)